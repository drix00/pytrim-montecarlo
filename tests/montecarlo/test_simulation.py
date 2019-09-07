#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.test_simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.simulation` module.
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
import pytest

# Local modules.

# Project modules.
from trim.montecarlo.simulation import Simulation

# Globals and constants variables.


def test_init():
    input_file_path = "input.hdf5"
    output_file_path = "output.hdf5"

    simulation = Simulation(input_file_path, None)
    assert simulation.input_file_path == input_file_path
    assert simulation.output_file_path == input_file_path

    simulation = Simulation(input_file_path, output_file_path)
    assert simulation.input_file_path == input_file_path
    assert simulation.output_file_path == output_file_path

    with pytest.raises(ValueError) as exception_info:
        _simulation = Simulation(None, output_file_path)
    exception_message = exception_info.value.args[0]
    assert exception_message == "Need an input file path"
