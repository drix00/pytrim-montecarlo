#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: math

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Create HDF5 files for math tools.
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
from trim.montecarlo.math import Point
from trim.montecarlo import get_current_module_path
from trim.montecarlo.file import write

# Globals and constants variables.


def create_point_file():
    input_file_path = get_current_module_path(__file__, "test_Point.hdf5")
    hdf5_file = write(input_file_path)

    point = Point(1, 2, 3)
    point.write(hdf5_file)


if __name__ == '__main__':  # pragma: no cover
    create_point_file()
