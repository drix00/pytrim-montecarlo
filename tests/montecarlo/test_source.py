#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.test_source

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.source` module.
"""

# Copyright 2019 Hendrix Demers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard library modules.
import os.path

# Third party modules.
import pytest

# Local modules.

# Project modules.
from trim.montecarlo.source import Source
from trim.montecarlo.math import Point
from trim.montecarlo import get_current_module_path
from trim.montecarlo.file import read, write

# Globals and constants variables.


def test_init():
    source = Source()
    assert source.position_nm == Point(0.0, 0.0, 0.0)
    assert source.direction == Point(0.0, 0.0, -1.0)
    assert source.kinetic_energy_keV == 6.0
    assert source.mass_amu == 39.962
    assert source.atomic_number == 18


def test_read():
    file_path = get_current_module_path(__file__, "../../test_data/test_Source.hdf5")
    if not os.path.isfile(file_path):  # pragma: no cover
        pytest.skip("File does not exist: {}".format(file_path))

    hdf5_file = read(file_path)
    source = Source()
    source.read(hdf5_file)
    assert source.position_nm == Point(-1, -2, -3)
    assert source.direction == Point(0.2, 0.4, 0.6)
    assert source.kinetic_energy_keV == 53.1156
    assert source.mass_amu == 68.93
    assert source.atomic_number == 31


def test_write(tmpdir):
    file_path = tmpdir.join("output.hdf5")

    source = Source()
    source.position_nm = Point(-1, -2, -3)
    source.direction = Point(0.2, 0.4, 0.6)
    source.kinetic_energy_keV = 53.1156
    source.mass_amu = 68.93
    source.atomic_number = 31

    hdf5_file = write(file_path)
    source.write(hdf5_file)
    hdf5_file.close()

    source = Source()
    hdf5_file = read(file_path)
    source.read(hdf5_file)
    assert source.position_nm == Point(-1, -2, -3)
    assert source.direction == Point(0.2, 0.4, 0.6)
    assert source.kinetic_energy_keV == 53.1156
    assert source.mass_amu == 68.93
    assert source.atomic_number == 31
