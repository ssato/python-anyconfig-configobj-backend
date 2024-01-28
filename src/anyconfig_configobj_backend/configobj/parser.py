#
# Copyright (C) 2013 - 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
r"""Configobj parser (loader and dumper) backend:

- Format to support: configobj,
  https://bit.ly/2TgURnL (https://configobj.readthedocs.io)
- Requirements: configobj (https://pypi.python.org/pypi/configobj/)
- Development Status :: 4 - Beta
- Limitations: AFAIK, configobj does not keep the order of configuration items
  and not have options to change this behavior like configparser, so this
  backend does not keep the order of configuration items even if the ac_ordered
  option was used.

- Special options:

  - All options except for 'infile' passed to configobj.ConfigObj.__init__
    should work.

  - See also: http://configobj.readthedocs.io/en/latest/configobj.html

Chnagelog:

.. versionchanged:: 0.14.0

   split dumper and loader.

.. versionchanged:: 0.5.0

   - Now loading and dumping options are detected automatically from inspection
     result if possible. Also these became not distinguished because these will
     be passed to configobj.Configuration anyway.
"""
import anyconfig.backend.base

from . import loader, dumper


class Parser(
    loader.Loader, dumper.Dumper,
    anyconfig.backend.base.Parser,
):
    """
    Parser (Loader and dumper) for Ini-like config files which configobj
    supports.
    """
