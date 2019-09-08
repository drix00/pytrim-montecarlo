#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.options.element

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Properties of atomic element of the region.
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

# Globals and constants variables.
GROUP_ELEMENT = "element"
ATTRIBUTE_SYMBOL = "symbol"
ATTRIBUTE_NAME = "name"
ATTRIBUTE_ATOMIC_NUMBER = "atomic number"
ATTRIBUTE_MASS = "mass (amu)"
ATTRIBUTE_DISPLACEMENT_ENERGY = "displacement energy (eV)"
ATTRIBUTE_SURFACE_BINDING_ENERGY = "surface binding energy (eV)"
ATTRIBUTE_LATTICE_BINDING_ENERGY = "lattice binding energy (eV)"


class Element:
    def __init__(self):
        self.symbol = ""
        self.name = ""
        self.atomic_number = 0
        self.mass_amu = 0.0
        self.displacement_energy_eV = 0.0
        self.surface_binding_energy_eV = 0.0
        self.lattice_binding_energy_eV = 0.0

    def write(self, parent, element_id=1, width=1):
        group_name = generate_group_name(element_id, width)
        group = parent.require_group(group_name)

        group.attrs[ATTRIBUTE_SYMBOL] = self.symbol
        group.attrs[ATTRIBUTE_NAME] = self.name
        group.attrs[ATTRIBUTE_ATOMIC_NUMBER] = self.atomic_number
        group.attrs[ATTRIBUTE_MASS] = self.mass_amu
        group.attrs[ATTRIBUTE_DISPLACEMENT_ENERGY] = self.displacement_energy_eV
        group.attrs[ATTRIBUTE_SURFACE_BINDING_ENERGY] = self.surface_binding_energy_eV
        group.attrs[ATTRIBUTE_LATTICE_BINDING_ENERGY] = self.lattice_binding_energy_eV

    def read(self, parent, element_id=1, width=1):
        group_name = generate_group_name(element_id, width)
        group = parent.require_group(group_name)

        self.symbol = group.attrs[ATTRIBUTE_SYMBOL]
        self.name = group.attrs[ATTRIBUTE_NAME]
        self.atomic_number = group.attrs[ATTRIBUTE_ATOMIC_NUMBER]
        self.mass_amu = group.attrs[ATTRIBUTE_MASS]
        self.displacement_energy_eV = group.attrs[ATTRIBUTE_DISPLACEMENT_ENERGY]
        self.surface_binding_energy_eV = group.attrs[ATTRIBUTE_SURFACE_BINDING_ENERGY]
        self.lattice_binding_energy_eV = group.attrs[ATTRIBUTE_LATTICE_BINDING_ENERGY]

    def __eq__(self, other):
        return ((self.symbol == other.symbol) and
                (self.name == other.name) and
                (self.atomic_number == other.atomic_number) and
                (self.mass_amu == other.mass_amu) and
                (self.displacement_energy_eV == other.displacement_energy_eV) and
                (self.surface_binding_energy_eV == other.surface_binding_energy_eV) and
                (self.lattice_binding_energy_eV == other.lattice_binding_energy_eV)
                )


def generate_group_name(element_id, width):
    name = "{}_{:0{width}d}".format(GROUP_ELEMENT, element_id, width=width)
    return name


def get_vacuum_element():
    element = Element()
    element.symbol = "Vac"
    element.name = "vacuum"
    element.atomic_number = 0
    element.mass_amu = 0.0
    element.displacement_energy_eV = 0.0
    element.surface_binding_energy_eV = 0.0
    element.lattice_binding_energy_eV = 0.0

    return element


def get_silicon_element():
    element = Element()
    element.symbol = "Si"
    element.name = "silicon"
    element.atomic_number = 14
    element.mass_amu = 28.8
    element.displacement_energy_eV = 15.0
    element.surface_binding_energy_eV = 2.0
    element.lattice_binding_energy_eV = 4.7

    return element
