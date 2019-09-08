#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.options.material

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Composition of homogeneous region of the sample.
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

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo.options.element import Element, get_vacuum_element, get_silicon_element

# Globals and constants variables.
GROUP_MATERIAL = "material"
GROUP_ELEMENTS = "elements"

ATTRIBUTE_NUMBER_ELEMENTS = "number of elements"
ATTRIBUTE_MASS_DENSITY = "mass density (g/cm3)"


class Material:
    def __init__(self):
        self.elements = []
        self.mass_density_g_cm3 = 0.0

    def write(self, parent):
        group = parent.require_group(GROUP_MATERIAL)

        number_elements = len(self.elements)
        group.attrs[ATTRIBUTE_NUMBER_ELEMENTS] = number_elements
        group.attrs[ATTRIBUTE_MASS_DENSITY] = self.mass_density_g_cm3

        width = len(str(number_elements))
        for element_id, element in enumerate(self.elements, start=1):
            element.write(group, element_id, width)

    def read(self, parent):
        group = parent.require_group(GROUP_MATERIAL)

        number_elements = group.attrs[ATTRIBUTE_NUMBER_ELEMENTS]
        self.mass_density_g_cm3 = float(group.attrs[ATTRIBUTE_MASS_DENSITY])

        width = len(str(number_elements))
        for element_id in range(1, number_elements+1):
            element = Element()
            element.read(group, element_id, width)
            self.elements.append(element)

    def __eq__(self, other):
        if self.mass_density_g_cm3 != other.mass_density_g_cm3:
            return False
        if len(self.elements) != len(other.elements):
            return False

        for element1, element2 in zip(self.elements, other.elements):
            if element1 != element2:
                return False

        return True


def get_vacuum_material():
    material = Material()
    material.elements.append(get_vacuum_element())
    material.mass_density_g_cm3 = 0.0

    return material


def get_silicon_material():
    material = Material()
    material.elements.append(get_silicon_element())
    material.mass_density_g_cm3 = 2.3212

    return material
