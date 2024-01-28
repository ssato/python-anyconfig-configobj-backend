#
# Copyright (C) 2013 - 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
r"""Base class for loader and dumper classes for configobj.
"""
import inspect

import configobj

try:
    _MOD_OPTIONS = [
        a for a in inspect.getfullargspec(configobj.ConfigObj).args
        if a not in {'self', 'infile'}
    ]
except (TypeError, AttributeError):
    _MOD_OPTIONS = (
        "options configspec encoding interpolation raise_errors"
        "list_values create_empty file_error stringify"
        "indent_type default_encoding unrepr write_empty_values"
        "_inspec"
    ).split()


# pylint: disable=too-few-public-methods
class Base:
    """Base class for the loader and dumper classes.
    """
    _cid = "configobj.configobj"
    _type = "configobj"
    _priority = 10
    _extensions = ["configobj", "ini"]
    _load_opts = _MOD_OPTIONS  # options on dump will be just ignored.
    _dump_opts = _MOD_OPTIONS  # Likewise.
    _ordered = True
    _allow_primitives = True
