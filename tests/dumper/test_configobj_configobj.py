#
# Copyright (C) 2012 - 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
# pylint: disable=ungrouped-imports
"""Test cases for the loader.
"""
import pathlib
import typing

import pytest

from ..common import (
    tdi_base, dumper
)


class TDI(tdi_base.TDI):
    _cid = tdi_base.name_from_path(__file__)
    _is_loader = False


(TT, DATA, DATA_IDS) = TDI().get_all()

if TT is None:
    pytest.skip(
        f"skipping tests: {TDI().cid()} as it's not available.",
        allow_module_level=True
    )

assert DATA


class TestCase(dumper.TestCase):
    psr_cls = TT.Parser
    exact_match = False

    @pytest.mark.parametrize(
        ("ipath", "aux"), DATA, ids=DATA_IDS,
    )
    def test_dumps(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
    ):
        self._assert_dumps(ipath, aux)

    @pytest.mark.parametrize(
        ("ipath", "aux"), DATA, ids=DATA_IDS,
    )
    def test_dump(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
        tmp_path: pathlib.Path
    ):
        self._assert_dump(ipath, aux, tmp_path)

    @pytest.mark.parametrize(
        ("ipath", "aux"), DATA, ids=DATA_IDS,
    )
    def test_plugin_dumps(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
    ):
        self._assert_dumps(ipath, aux, plugin=True)

    @pytest.mark.parametrize(
        ("ipath", "aux"), DATA, ids=DATA_IDS,
    )
    def test_plugin_dump(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any],
        tmp_path: pathlib.Path
    ):
        self._assert_dump(ipath, aux, tmp_path, plugin=True)
