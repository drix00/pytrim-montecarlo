#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.options.element

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.options.element` module.
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
from trim.montecarlo import get_current_module_path
from trim.montecarlo.file import read, write
from trim.montecarlo.options.element import Element, get_vacuum_element, get_silicon_element, generate_group_name

# Globals and constants variables.


def test_init():
    element = Element()
    assert element.symbol == ""
    assert element.name == ""
    assert element.atomic_number == 0
    assert element.mass_amu == 0.0
    assert element.displacement_energy_eV == 0.0
    assert element.surface_binding_energy_eV == 0.0
    assert element.lattice_binding_energy_eV == 0.0


def test_read():
    file_path = get_current_module_path(__file__, "../../../test_data/test_Element.hdf5")
    if not os.path.isfile(file_path):  # pragma: no cover
        pytest.skip("File does not exist: {}".format(file_path))

    hdf5_file = read(file_path)
    element = Element()
    element.read(hdf5_file)

    assert element != get_vacuum_element()
    assert element == get_silicon_element()


def test_write(tmpdir):
    file_path = tmpdir.join("output.hdf5")

    element = get_silicon_element()

    hdf5_file = write(file_path)
    element.write(hdf5_file)
    hdf5_file.close()

    element = Element()
    hdf5_file = read(file_path)
    element.read(hdf5_file)

    assert element != get_vacuum_element()
    assert element == get_silicon_element()


def test_generate_group_name_width1():
    width = 1
    element_id = 1
    name_ref = "element_1"
    name = generate_group_name(element_id, width)
    assert name == name_ref


def test_generate_group_name_width5():
    width = 5
    element_id = 456
    name_ref = "element_00456"
    name = generate_group_name(element_id, width)
    assert name == name_ref
