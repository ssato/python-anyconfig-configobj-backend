#
# Copyright (C) 2013 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
import anyconfig.backend.configobj_ as T
import os
import sys
import tempfile
import unittest


CONF_0 = """\
# This is the 'initial_comment'
# Which may be several lines
keyword1 = value1
'keyword 2' = 'value 2'

[ "section 1" ]
# This comment goes with keyword 3
keyword 3 = value 3
'keyword 4' = value4, value 5, 'value 6'

    [[ sub-section ]]    # an inline comment
    # sub-section is inside "section 1"
    'keyword 5' = 'value 7'
    'keyword 6' = '''A multiline value,
that spans more than one line :-)
The line breaks are included in the value.'''

        [[[ sub-sub-section ]]]
        # sub-sub-section is *in* 'sub-section'
        # which is in 'section 1'
        'keyword 7' = 'value 8'

[section 2]    # an inline comment
keyword8 = "value 9"
keyword9 = value10     # an inline comment
# The 'final_comment'
# Which also may be several lines
"""


class Test_ConfigObjParser(unittest.TestCase):

    def setUp(self):
        (_, conf) = tempfile.mkstemp(prefix="ac-bc-test-")
        open(conf, 'w').write(CONF_0)
        self.config_path = conf

    def tearDown(self):
        os.remove(self.config_path)

    def test_00_supports(self):
        self.assertTrue(T.ConfigObjParser.supports("/a/b/c/d.ini"))
        self.assertFalse(T.ConfigObjParser.supports("/a/b/c/d.json"))

    def test_10_loads(self):
        c = T.ConfigObjParser.loads(CONF_0)

        self.assertEquals(c['keyword1'], 'value1')
        self.assertEquals(c['keyword 2'], 'value 2')
        self.assertEquals(c['section 1']['keyword 3'], 'value 3')
        self.assertEquals(c['section 1']['keyword 4'],
                          ['value4', 'value 5', 'value 6'])
        self.assertEquals(c['section 1']['sub-section']['keyword 5'],
                          'value 7')
        self.assertEquals(c['section 1']['sub-section']['keyword 6'],
                          """A multiline value,
that spans more than one line :-)
The line breaks are included in the value.""")
        self.assertEquals(
            c['section 1']['sub-section']['sub-sub-section']['keyword 7'],
            'value 8'
        )
        self.assertEquals(c['section 2']['keyword8'], 'value 9')
        self.assertEquals(c['section 2']['keyword9'], 'value10')

    def test_20_load(self):
        c = T.ConfigObjParser.load(self.config_path)

        self.assertEquals(c['keyword1'], 'value1')
        self.assertEquals(c['keyword 2'], 'value 2')
        self.assertEquals(c['section 1']['keyword 3'], 'value 3')
        self.assertEquals(c['section 1']['keyword 4'],
                          ['value4', 'value 5', 'value 6'])
        self.assertEquals(c['section 1']['sub-section']['keyword 5'],
                          'value 7')
        self.assertEquals(c['section 1']['sub-section']['keyword 6'],
                          """A multiline value,
that spans more than one line :-)
The line breaks are included in the value.""")
        self.assertEquals(
            c['section 1']['sub-section']['sub-sub-section']['keyword 7'],
            'value 8'
        )
        self.assertEquals(c['section 2']['keyword8'], 'value 9')
        self.assertEquals(c['section 2']['keyword9'], 'value10')

    def test_30_dumps(self):
        c = T.ConfigObjParser.loads(CONF_0)
        s = T.ConfigObjParser.dumps(c)
        c = T.ConfigObjParser.loads(s)

        self.assertEquals(c['keyword1'], 'value1')
        self.assertEquals(c['keyword 2'], 'value 2')
        self.assertEquals(c['section 1']['keyword 3'], 'value 3')
        self.assertEquals(c['section 1']['keyword 4'],
                          ['value4', 'value 5', 'value 6'])
        self.assertEquals(c['section 1']['sub-section']['keyword 5'],
                          'value 7')
        self.assertEquals(c['section 1']['sub-section']['keyword 6'],
                          """A multiline value,
that spans more than one line :-)
The line breaks are included in the value.""")
        self.assertEquals(
            c['section 1']['sub-section']['sub-sub-section']['keyword 7'],
            'value 8'
        )
        self.assertEquals(c['section 2']['keyword8'], 'value 9')
        self.assertEquals(c['section 2']['keyword9'], 'value10')

    def test_40_dump(self):
        c = T.ConfigObjParser.loads(CONF_0)
        T.ConfigObjParser.dump(c, self.config_path)
        c = T.ConfigObjParser.load(self.config_path)

        self.assertEquals(c['keyword1'], 'value1')
        self.assertEquals(c['keyword 2'], 'value 2')
        self.assertEquals(c['section 1']['keyword 3'], 'value 3')
        self.assertEquals(c['section 1']['keyword 4'],
                          ['value4', 'value 5', 'value 6'])
        self.assertEquals(c['section 1']['sub-section']['keyword 5'],
                          'value 7')
        self.assertEquals(c['section 1']['sub-section']['keyword 6'],
                          """A multiline value,
that spans more than one line :-)
The line breaks are included in the value.""")
        self.assertEquals(
            c['section 1']['sub-section']['sub-sub-section']['keyword 7'],
            'value 8'
        )
        self.assertEquals(c['section 2']['keyword8'], 'value 9')
        self.assertEquals(c['section 2']['keyword9'], 'value10')

# vim:sw=4:ts=4:et:
