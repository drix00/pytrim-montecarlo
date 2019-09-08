#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.math

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Mathematical tools for the Monte Carlo simulation.
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
GROUP_POINT = "point"
ATTRIBUTE_POINT_X = "x"
ATTRIBUTE_POINT_Y = "y"
ATTRIBUTE_POINT_Z = "z"


class Point:
    """
    3D point representation.
    """
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def write(self, parent):
        group = parent.require_group(GROUP_POINT)

        group.attrs[ATTRIBUTE_POINT_X] = self.x
        group.attrs[ATTRIBUTE_POINT_Y] = self.y
        group.attrs[ATTRIBUTE_POINT_Z] = self.z

    def read(self, parent):
        group = parent.require_group(GROUP_POINT)

        self.x = float(group.attrs[ATTRIBUTE_POINT_X])
        self.y = float(group.attrs[ATTRIBUTE_POINT_Y])
        self.z = float(group.attrs[ATTRIBUTE_POINT_Z])
