# -*- coding: utf-8 -*-
#
# pylint:disable=invalid-name
"""conf.py for sphinx."""
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.resolve() / 'src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints'
]
source_suffix = '.rst'
master_doc = 'index'

project = u'python-anyconfig-configobj-backend'
copyright = u'2024, Satoru SATOH <satoru.satoh@gmail.com>'
version = '0.2.0'
release = version

exclude_patterns = []

html_theme = 'default'

autodoc_member_order = 'bysource'
