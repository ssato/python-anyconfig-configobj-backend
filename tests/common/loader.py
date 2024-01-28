#
# Copyright (C) 2023, 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring,too-few-public-methods
r"""Loader test cases.
"""
import pathlib
import typing
import warnings

import anyconfig
import anyconfig.api
import anyconfig.ioinfo


class TestCase:
    """Base class for loader test cases.
    """
    psr_cls = None

    def _get_all(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any]
    ):
        if self.psr_cls is None:
            warnings.warn(  # noqa
                f"Failed to ini test target: {__file__}"
            )
            psr = None
        else:
            psr = self.psr_cls()  # pylint: disable=not-callable

        ioi = anyconfig.ioinfo.make(ipath)

        return (
            aux["e"],  # It should NOT fail.
            aux.get("o", {}),
            psr,
            ioi
        )

    def _assert_plugin(self, cid: str):
        anyconfig.api.load_plugins()
        psrs = dict(anyconfig.list_by_cid())
        assert cid in psrs, f"{cid} not found: {psrs!r}"

    def _assert_loads(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
        plugin: bool = False
    ):
        (exp, opts, psr, _ioi) = self._get_all(ipath, aux)
        if 'b' in psr._open_read_mode:  # pylint: disable=protected-access
            content = ipath.read_bytes()
        else:
            content = ipath.read_text()

        if plugin:
            self._assert_plugin(psr.cid())
            loads = anyconfig.loads
        else:
            loads = psr.loads

        res = loads(content, **opts)
        assert res == exp, f"'{res!r}' vs. '{exp!r}'"

    def _assert_load(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
        plugin: bool = False
    ):
        (exp, opts, psr, ioi) = self._get_all(ipath, aux)

        if plugin:
            self._assert_plugin(psr.cid())
            load = anyconfig.load
        else:
            load = psr.load

        res = load(ioi, **opts)
        assert res == exp, f"'{res!r}' vs. '{exp!r}'"
