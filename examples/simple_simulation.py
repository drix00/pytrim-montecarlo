#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: simple_simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Write simple simulation input file.
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
from trim.montecarlo.simulation import Simulation
from trim.montecarlo import get_current_module_path

# Globals and constants variables.


if __name__ == '__main__':  # pragma: no cover
    input_file_path = get_current_module_path(__file__, "simple_simulation.hdf5")

    simulation = Simulation(input_file_path, None)
    simulation.write()
