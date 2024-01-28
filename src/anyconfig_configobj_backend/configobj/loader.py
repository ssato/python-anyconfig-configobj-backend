#
# Copyright (C) 2013 - 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
r"""Configobj loader backend:

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
import collections.abc
import io

import configobj

import anyconfig.backend.base

from . import base


def load(path_or_strm, container, **opts):
    """
    :param path_or_strm: input config file path or file/file-like object
    :param container: callble to make a container object
    :param opts: keyword options passed to :class:`configobj.ConfigObj`

    :return: Mapping object
    """
    ret = configobj.ConfigObj(path_or_strm, **opts)

    if isinstance(ret, (dict, collections.abc.Mapping)):
        return container(ret.dict())

    return ret


class Loader(base.Base, anyconfig.backend.base.BinaryLoaderMixin):
    """
    Loader for Ini-like config files which configobj supports.
    """
    load_from_path = load_from_stream = anyconfig.backend.base.to_method(load)

    def load_from_string(self, content: str, container, **kwargs):
        """Load config from given string 'cnf_content'.

        :param content: Config content string
        :param container: callble to make a container object later
        :param kwargs: optional keyword parameters to be sanitized :: dict

        :return: Dict-like object holding config parameters
        """
        return self.load_from_stream(io.BytesIO(content),
                                     container, **kwargs)
