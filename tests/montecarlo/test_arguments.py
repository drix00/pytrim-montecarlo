#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.test_arguments

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for the `trim.montecarlo.arguments` module.
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
import sys

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo.arguments import get_arguments

# Globals and constants variables.


def test_get_arguments():
    # Remove all command arguments, keep only the first argument.
    sys.argv = [sys.argv[0]]

    # Add arguments for testing the run method.
    sys.argv.append("-v")
    sys.argv.append("-i")
    sys.argv.append("input_file")
    sys.argv.append("-o")
    sys.argv.append("output_file")

    arguments = get_arguments()

    assert arguments is not None
    assert arguments.verbose is True
    assert arguments.input == "input_file"
    assert arguments.output == "output_file"
