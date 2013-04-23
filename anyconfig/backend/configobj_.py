#
# Copyright (C) 2013 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
from configobj import ConfigObj

from anyconfig.compat import StringIO, iteritems
from anyconfig.globals import LOGGER as logging

import anyconfig.backend.base as Base
import sys


_LOAD_OPTS = ["cls", "configspec", "encoding", "interpolation", "raise_errors",
              "list_values", "create_empty", "file_error", "stringify",
              "indent_type", "default_encoding", "unrepr", "_inspec", ]

_DUMP_OPTS = ["cls", "encoding", "list_values", "indent_type",
              "default_encoding", "unrepr", "write_empty_values", ]


class ConfigObjParser(Base.ConfigParser):
    _type = "configobj"
    _priority = 10
    _supported = True
    _extensions = ["ini"]

    @classmethod
    def loads(cls, config_content, **kwargs):
        sio = StringIO(config_content)
        create = cls.container().create

        return create(ConfigObj(sio, **Base.mk_opt_args(_LOAD_OPTS, kwargs)))
        
    @classmethod
    def load(cls, config_path, **kwargs):
        create = cls.container().create

        return create(ConfigObj(config_path,
                      **Base.mk_opt_args(_LOAD_OPTS, kwargs)))

    @classmethod
    def dumps(cls, data, **kwargs):
        conf = ConfigObj(**Base.mk_opt_args(_DUMP_OPTS, kwargs))
        conf.update(cls.container().convert_to(data))
        conf.filename = None

        return '\n'.join(conf.write())

    @classmethod
    def dump(cls, data, config_path, **kwargs):
        conf = ConfigObj(**Base.mk_opt_args(_DUMP_OPTS, kwargs))
        conf.update(cls.container().convert_to(data))

        Base.mk_dump_dir_if_not_exist(config_path)
        conf.write(open(config_path, 'w'))

# vim:sw=4:ts=4:et:
