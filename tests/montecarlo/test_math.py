#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.test_math

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.math` module.
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
from trim.montecarlo.math import Point
from trim.montecarlo import get_current_module_path
from trim.montecarlo.file import read, write

# Globals and constants variables.


def test_point_init():
    point = Point(1, 2, 3)
    assert point.x == 1
    assert point.y == 2
    assert point.z == 3


def test_point_equal():
    assert Point(1, 2, 3) == Point(1, 2, 3)
    assert Point(1, 2, 3) != Point(4, 2, 3)
    assert Point(1, 2, 3) != Point(1, 4, 3)
    assert Point(1, 2, 3) != Point(1, 2, 4)


def test_point_read():
    file_path = get_current_module_path(__file__, "../../test_data/test_Point.hdf5")
    if not os.path.isfile(file_path):  # pragma: no cover
        pytest.skip("File does not exist: {}".format(file_path))

    hdf5_file = read(file_path)
    point = Point(0, 0, 0)
    assert point.x != 1
    assert point.y != 2
    assert point.z != 3

    point.read(hdf5_file)
    assert point.x == 1
    assert point.y == 2
    assert point.z == 3


def test_write(tmpdir):
    file_path = tmpdir.join("output.hdf5")
    point = Point(-1, -2, -3)

    hdf5_file = write(file_path)
    point.write(hdf5_file)
    hdf5_file.close()

    point = Point(1, 2, 3)
    hdf5_file = read(file_path)
    point.read(hdf5_file)
    assert point.x == -1
    assert point.y == -2
    assert point.z == -3
