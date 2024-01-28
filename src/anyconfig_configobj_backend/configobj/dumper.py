#
# Copyright (C) 2013 - 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
r"""Configobj backend:

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
import os

import configobj

import anyconfig.backend.base

from . import base


def make_configobj(cnf, **kwargs):
    """
    Make a configobj.ConfigObj initalized with given config 'cnf'.

    :param cnf: Configuration data
    :param kwargs: optional keyword parameters passed to ConfigObj.__init__

    :return: An initialized configobj.ConfigObj instance
    """
    cobj = configobj.ConfigObj(**kwargs)
    cobj.update(cnf)

    return cobj


class Dumper(base.Base,
             anyconfig.backend.base.ToStreamDumperMixin,
             anyconfig.backend.base.BinaryDumperMixin):
    """
    Dumper for Ini-like config files which configobj supports.
    """

    def dump_to_string(self, cnf, **kwargs):
        """
        Dump config 'cnf' to a string.

        :param cnf: Configuration data to dump
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: string represents the configuration
        """
        return os.linesep.join(make_configobj(cnf, **kwargs).write())

    def dump_to_stream(self, cnf, stream, **kwargs):
        """
        :param cnf: Configuration data to dump
        :param stream: Config file or file-like object
        :param kwargs: backend-specific optional keyword parameters :: dict
        """
        make_configobj(cnf, **kwargs).write(stream)
