#
# Copyright (C) 2013, 2014 Satoru SATOH <ssato @ redhat.com>
# License: MIT
#
from configobj import ConfigObj
from anyconfig.backend.base import ConfigParser


class ConfigObjParser(ConfigParser):
    _type = "configobj"
    _priority = 10
    _supported = True
    _extensions = ["ini"]

    _load_opts = ["cls", "configspec", "encoding", "interpolation",
                  "raise_errors", "list_values", "create_empty", "file_error",
                  "stringify", "indent_type", "default_encoding", "unrepr",
                  "_inspec", ]
    _dump_opts = ["cls", "encoding", "list_values", "indent_type",
                  "default_encoding", "unrepr", "write_empty_values", ]

    @classmethod
    def load_impl(cls, config_fp, **kwargs):
        """
        :param config_fp:  Config file object
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: dict object holding config parameters
        """
        return ConfigObj(config_fp)

    @classmethod
    def dumps_impl(cls, data, **kwargs):
        """
        :param data: Data to dump :: dict
        :param kwargs: backend-specific optional keyword parameters :: dict

        :return: string represents the configuration
        """
        conf = ConfigObj(**kwargs)
        conf.update(data)
        conf.filename = None

        return '\n'.join(conf.write())

    @classmethod
    def dump_impl(cls, data, config_path, **kwargs):
        """
        :param data: Data to dump :: dict
        :param config_path: Dump destination file path
        :param kwargs: backend-specific optional keyword parameters :: dict
        """
        conf = ConfigObj(**kwargs)
        conf.update(data)

        conf.write(open(config_path, 'w'))

# vim:sw=4:ts=4:et:
