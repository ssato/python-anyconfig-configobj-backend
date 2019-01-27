# -*- coding: utf-8 -*-
#
# pylint:disable=invalid-name
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                os.path.pardir)))

extensions = ['sphinx.ext.autodoc']
source_suffix = '.rst'
master_doc = 'index'

project = u'python-anyconfig-configobj-backend'
copyright = u'2015, Satoru SATOH <satoru.satoh@gmail.com>'
version = '0.0.4'
release = version

exclude_patterns = []

html_theme = 'default'

autodoc_member_order = 'bysource'
