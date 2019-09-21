#
# Copyright (C) 2011 - 2018 Satoru SATOH <ssato at redhat.com>
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
# pylint: disable=ungrouped-imports
from __future__ import absolute_import

import copy
import os.path
import tempfile
import unittest

from os import linesep as lsep

import anyconfig.compat
import anyconfig.ioinfo

from anyconfig.compat import OrderedDict
from anyconfig.utils import is_dict_like


CNF_0 = OrderedDict((("DEFAULT", OrderedDict((("a", "0"), ("b", "bbb"),
                                              ("c", "5")))),
                     ("sect0", OrderedDict((("a", "0"), ("b", "bbb"),
                                            ("c", "5"),
                                            ("d", "x,y,z"))))))
CNF_1 = copy.deepcopy(CNF_0)
CNF_1["sect0"]["d"] = CNF_1["sect0"]["d"].split()


def _bytes(astr):
    """
    Convert a string to bytes. Do nothing in python 2.6.
    """
    return bytes(astr, 'utf-8') if anyconfig.compat.IS_PYTHON_3 else astr


CNF_2 = OrderedDict((("a", 0.1), ("b", _bytes("bbb")),
                     ("sect0", OrderedDict((("c", [_bytes("x"), _bytes("y"),
                                                   _bytes("z")]), )))))


def selfdir():
    """
    >>> os.path.exists(selfdir())
    True
    """
    return os.path.dirname(__file__)


def setup_workdir():
    """
    >>> workdir = setup_workdir()
    >>> assert workdir != '.'
    >>> assert workdir != '/'
    >>> os.path.exists(workdir)
    True
    >>> os.rmdir(workdir)
    """
    return tempfile.mkdtemp(dir="/tmp", prefix="python-anyconfig-tests-")


def cleanup_workdir(workdir):
    """
    FIXME: Danger!

    >>> from os import linesep as lsep
    >>> workdir = setup_workdir()
    >>> os.path.exists(workdir)
    True
    >>> open(os.path.join(workdir, "workdir.stamp"), 'w').write("OK!" + lsep)
    >>> cleanup_workdir(workdir)
    >>> os.path.exists(workdir)
    False
    """
    assert workdir != '/'
    assert workdir != '.'

    os.system("rm -rf " + workdir)


def dicts_equal(dic, ref, ordered=False):
    """Compare (maybe nested) dicts.
    """
    if not is_dict_like(dic) or not is_dict_like(ref):
        return dic == ref

    fnc = list if ordered else sorted
    if fnc(dic.keys()) != fnc(ref.keys()):
        return False

    for key in ref.keys():
        if key not in dic or not dicts_equal(dic[key], ref[key]):
            return False

    return True


class Test(unittest.TestCase):

    def test_dicts_equal(self):
        dic0 = {'a': 1}
        dic1 = OrderedDict((('a', [1, 2, 3]),
                            ('b', OrderedDict((('c', "CCC"), )))))
        dic2 = dic1.copy()
        dic2["b"] = None

        dic3 = OrderedDict((('b', OrderedDict((('c', "CCC"), ))),
                            ('a', [1, 2, 3])))

        self.assertTrue(dicts_equal({}, {}))
        self.assertTrue(dicts_equal(dic0, dic0))
        self.assertTrue(dicts_equal(dic1, dic1))
        self.assertTrue(dicts_equal(dic2, dic2))
        self.assertTrue(dicts_equal(dic1, dic3))

        self.assertFalse(dicts_equal(dic0, {}))
        self.assertFalse(dicts_equal(dic0, dic1))
        self.assertFalse(dicts_equal(dic1, dic2))
        self.assertFalse(dicts_equal(dic1, dic3, ordered=True))


class MyDict(dict):
    pass


class HasParserTrait(object):

    psr = None  # Must be a parser instance.
    cnf_s = None  # Do.
    cnf = cnf_0 = CNF_0
    cnf_1 = CNF_1

    def is_ready(self):
        return self.psr is not None


class TestBase(unittest.TestCase, HasParserTrait):

    def _to_ioinfo(self, path):
        return anyconfig.ioinfo.make(path)

    def _assert_dicts_equal(self, cnf, ordered=False, cls=None, ref=None):
        if ref is None:
            ref = self.cnf
        self.assertTrue(dicts_equal(cnf, ref, ordered=ordered),
                        "%s %r%svs.%s %r" % (lsep, cnf, lsep, lsep, ref))
        # .. note::
        #    `cnf` may not be an instance of `cls` even if ac_dict option was
        #    given because parsers may not allow customize dict class to used
        #    for making results.
        if cls is None or not self.psr.dict_options():
            cls = OrderedDict if ordered else dict
        self.assertTrue(isinstance(cnf, cls),
                        "cnf=%r [type: %r], cls=%r" % (cnf, type(cnf), cls))


class Test_10_dumps_and_loads(TestBase):

    load_options = {}  # Must be set to a dict in children classes.
    dump_options = {}  # Do.
    empty_patterns = ['']  # Do.

    def test_10_loads(self):
        if self.is_ready():
            cnf = self.psr.loads(self.cnf_s)
            self.assertTrue(cnf)  # Check if it's not None nor {}.
            self._assert_dicts_equal(cnf)

    def test_12_loads_with_options(self):
        if self.is_ready():
            cnf = self.psr.loads(self.cnf_s, **self.load_options)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

    def test_14_loads_with_invalid_options(self):
        if self.is_ready():
            cnf = self.psr.loads(self.cnf_s, not_exist_option_a=True)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

    def test_16_loads_with_ac_ordered_option(self):
        if self.is_ready():
            cnf = self.psr.loads(self.cnf_s, ac_ordered=True)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf, ordered=self.psr.ordered())

    def test_18_loads_with_ac_dict_option(self):
        if self.is_ready():
            cnf = self.psr.loads(self.cnf_s, ac_dict=MyDict)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf, cls=MyDict)
            # for debug:
            # raise RuntimeError("psr=%r, cnf=%r "
            #                    "[%r]" % (self.psr, cnf, type(cnf)))

    def test_20_loads_with_dict_option(self):
        if self.is_ready():
            dopts = self.psr.dict_options()
            if dopts:
                opts = {dopts[0]: MyDict}
                cnf = self.psr.loads(self.cnf_s, **opts)
                self.assertTrue(cnf)
                self._assert_dicts_equal(cnf, cls=MyDict)

    def test_22_loads_empty_data(self):
        if self.is_ready():
            for pat in self.empty_patterns:
                cnf = self.psr.loads(pat)
                self.assertEqual(cnf, dict())

    def test_30_dumps(self):
        if self.is_ready():
            cnf_s = self.psr.dumps(self.cnf)
            self.assertTrue(cnf_s)  # Check if it's not empty.
            cnf = self.psr.loads(cnf_s)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

    def test_32_dumps_with_options(self):
        if self.is_ready():
            cnf = self.psr.loads(self.psr.dumps(self.cnf, **self.dump_options))
            self._assert_dicts_equal(cnf)


class TestBaseWithIO(TestBase):

    def setUp(self):
        super(TestBaseWithIO, self).setUp()
        if self.is_ready():
            self.workdir = setup_workdir()

            exts = self.psr.extensions()
            ext = exts[0] if exts else "conf"
            self.cnf_path = os.path.join(self.workdir, "cnf_0." + ext)
            self.ioi = self._to_ioinfo(self.cnf_path)

            with self.psr.wopen(self.cnf_path) as out:
                out.write(self.cnf_s)

    def tearDown(self):
        if self.is_ready():
            cleanup_workdir(self.workdir)


class Test_20_dump_and_load(TestBaseWithIO):

    def test_10_load(self):
        if self.is_ready():
            cnf = self.psr.load(self.ioi)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

    def test_12_load_from_stream(self):
        if self.is_ready():
            with self.psr.ropen(self.cnf_path) as strm:
                ioi = self._to_ioinfo(strm)
                cnf = self.psr.load(ioi)

            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

    def test_14_load_with_ac_ordered_option(self):
        if self.is_ready():
            cnf = self.psr.load(self.ioi, ac_ordered=True)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf, ordered=self.psr.ordered())

    def test_16_load_with_ac_dict_option(self):
        if self.is_ready():
            cnf = self.psr.load(self.ioi, ac_dict=MyDict)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf, cls=MyDict)

    def test_30_dump(self):
        if self.is_ready():
            self.psr.dump(self.cnf, self.ioi)
            cnf = self.psr.load(self.ioi)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

    def test_32_dump_to_stream(self):
        if self.is_ready():
            with self.psr.wopen(self.cnf_path) as strm:
                ioi = self._to_ioinfo(strm)
                self.psr.dump(self.cnf, ioi)

            cnf = self.psr.load(self.ioi)
            self.assertTrue(cnf)
            self._assert_dicts_equal(cnf)

# vim:sw=4:ts=4:et:
