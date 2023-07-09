#
# Copyright (C) 2019 Satoru SATOH <satoru.satoh @ gmail.com>
# License: MIT
#
# pylint: disable=missing-docstring,invalid-name
from __future__ import absolute_import, print_function

import os.path
import unittest
import anyconfig
import configobj

from tests.common import dicts_equal


_CURDIR = os.path.dirname(__file__)
_CID = "configobj"  # .. seealso:: anyconfig_configobj_backend/configobj.py


class Test(unittest.TestCase):

    conf_path = os.path.join(_CURDIR, "res/0.configobj")
    conf_ref = configobj.ConfigObj(conf_path)

    def _co_assert_equals(self, cnf):
        self.assertTrue(dicts_equal(cnf, self.conf_ref.dict()))

    def _load_helper(self, **kwargs):
        try:
            anyconfig.api.load_plugins()
            return anyconfig.load(self.conf_path, **kwargs)
        except anyconfig.UnknownFileTypeError:
            for psr in anyconfig.api.Parsers().list():
                print("%r: type=%r, exts=%r" % (psr, psr.type(),
                                                psr.extensions()))
            raise

    def test_22_load__explicit_use(self):
        cnf = self._load_helper(ac_parser=_CID)
        self._co_assert_equals(cnf)

# vim:sw=4:ts=4:et:
