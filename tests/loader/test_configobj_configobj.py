#
# Copyright (C) 2012 - 2024 Satoru SATOH <satoru.satoh @ gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=missing-docstring,invalid-name,too-few-public-methods
# pylint: disable=ungrouped-imports
"""Test cases for the loader originally camee from
tests/backend/loaders/json/test_json_stdlib.py.
"""
import pathlib
import typing

import pytest

from ..common import (
    tdi_base, loader
)


class TDI(tdi_base.TDI):
    _cid = tdi_base.name_from_path(__file__)


(TT, DATA, DATA_IDS) = TDI().get_all()

if TT is None:
    pytest.skip(
        f"skipping tests: {TDI().cid()} as it's not available.",
        allow_module_level=True
    )

assert DATA


class TestCase(loader.TestCase):
    psr_cls = TT.Parser

    @pytest.mark.parametrize(
        ("ipath", "aux"), DATA, ids=DATA_IDS,
    )
    def test_loads(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any]
    ):
        self._assert_loads(ipath, aux)

    @pytest.mark.parametrize(
        ("ipath", "aux"), DATA, ids=DATA_IDS,
    )
    def test_load(
        self, ipath: pathlib.Path, aux: typing.Dict[str, typing.Any]
    ):
        self._assert_load(ipath, aux)
