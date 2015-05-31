"""anyconfig configobj backend plugin.
"""
from __future__ import absolute_import

from .globals import AUTHOR, VERSION
from .configobj import Parser

__author__ = AUTHOR
__version__ = VERSION
__all__ = ["Parser", ]

# vim:sw=4:ts=4:et:
