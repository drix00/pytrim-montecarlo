#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.options.test_material

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.options.material` module.
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
from trim.montecarlo.options.material import Material, get_vacuum_material, get_silicon_material
from trim.montecarlo.options.element import get_silicon_element, get_vacuum_element

# Globals and constants variables.


def test_init():
    material = Material()
    assert material.elements == []
    assert material.mass_density_g_cm3 == 0.0


def test_read():
    file_path = get_current_module_path(__file__, "../../../test_data/test_Material.hdf5")
    if not os.path.isfile(file_path):  # pragma: no cover
        pytest.skip("File does not exist: {}".format(file_path))

    hdf5_file = read(file_path)
    material = Material()
    material.read(hdf5_file)

    assert material != get_vacuum_material()
    assert material == get_silicon_material()


def test_write(tmpdir):
    file_path = tmpdir.join("output.hdf5")

    material = get_silicon_material()

    hdf5_file = write(file_path)
    material.write(hdf5_file)
    hdf5_file.close()

    material = Material()
    hdf5_file = read(file_path)
    material.read(hdf5_file)

    assert material != get_vacuum_material()
    material_si = get_silicon_material()
    assert material == material_si


def test_equality():
    material_default = Material()
    material_vacuum = get_vacuum_material()
    material_silicon = get_silicon_material()

    assert material_default == Material()
    assert material_default != material_vacuum
    assert material_default != material_silicon

    assert material_vacuum != Material()
    assert material_vacuum == material_vacuum
    assert material_vacuum != material_silicon

    assert material_silicon != Material()
    assert material_silicon != material_vacuum
    assert material_silicon == material_silicon

    material_2_elements = Material()
    material_2_elements.elements.append(get_silicon_element())
    material_2_elements.elements.append(get_silicon_element())

    material_2_elements2 = Material()
    material_2_elements2.elements.append(get_silicon_element())
    material_2_elements2.elements.append(get_vacuum_element())

    assert material_2_elements != Material()
    assert material_2_elements != material_vacuum
    assert material_2_elements != material_silicon
    assert material_2_elements == material_2_elements
    assert material_2_elements != material_2_elements2

    assert material_2_elements2 != Material()
    assert material_2_elements2 != material_vacuum
    assert material_2_elements2 != material_silicon
    assert material_2_elements2 != material_2_elements
    assert material_2_elements2 == material_2_elements2
