#
# Copyright (C) 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring,too-few-public-methods
r"""Dumper test cases.
"""
import pathlib
import typing
import warnings

import anyconfig
import anyconfig.ioinfo

import tests.common.load


class TestCase:
    """Base class for dumper test cases."""
    psr_cls = None

    exact_match: bool = True

    def _get_all(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
    ):
        if self.psr_cls is None:
            warnings.warn(  # noqa
                f"Failed to initialize test target: {__file__}",
            )
            psr = None
        else:
            psr = self.psr_cls()  # pylint: disable=not-callable

        idata = tests.common.load.load_data(ipath)

        return (
            aux["e"],  # It should NOT fail.
            aux.get("o", {}),
            psr,
            idata
        )

    def _assert_plugin(self, cid: str):
        anyconfig.api.load_plugins()
        psrs = dict(anyconfig.list_by_cid())
        assert cid in psrs, f"{cid} not found: {psrs!r}"

    def _assert_dumps(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
        plugin: bool = False
    ):
        (exp, opts, psr, idata) = self._get_all(ipath, aux)

        if plugin:
            self._assert_plugin(psr.cid())
            opts["ac_parser"] = psr.cid()
            dumps = anyconfig.dumps
            loads = anyconfig.loads
        else:
            dumps = psr.dumps
            loads = psr.loads

        out_s: typing.Union[str, bytes] = dumps(idata, **opts)

        if 'b' in psr._open_read_mode:  # pylint: disable=protected-access
            out_s = bytes(out_s, "utf-8")

        assert loads(out_s, **opts) == idata
        if self.exact_match:
            assert out_s == exp, f"'{out_s}' vs. '{exp}'"

    def _assert_dump(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
        tmp_path: pathlib.Path,
        plugin: bool = True
    ):
        (exp, opts, psr, idata) = self._get_all(ipath, aux)

        if plugin:
            self._assert_plugin(psr.cid())
            opts["ac_parser"] = psr.cid()
            dump = anyconfig.dump
            load = anyconfig.load
        else:
            dump = psr.dump
            load = psr.load

        opath = tmp_path / f"{ipath.name}.{psr.extensions()[0]}"
        ioi = anyconfig.ioinfo.make(opath)
        dump(idata, ioi, **opts)

        out_s: typing.Union[str, bytes] = psr.ropen(str(opath)).read()

        assert load(ioi, **opts) == idata
        if self.exact_match:
            assert out_s == exp, f"'{out_s}' vs. '{exp}'"
