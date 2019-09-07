#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.test_pytrim_montecarlo

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Tests for module `pytrim_montecarlo`.
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
from trim.montecarlo.pytrim_montecarlo import TrimMonteCarloCli

# Globals and constants variables.


def test_init():
    cli = TrimMonteCarloCli()
    assert cli.arguments is None


def test_run():
    cli = TrimMonteCarloCli()
    assert cli.arguments is None

    # Remove all command arguments, keep only the first argument.
    sys.argv = [sys.argv[0]]

    # Add arguments for testing the run method.
    sys.argv.append("-v")
    sys.argv.append("-i")
    sys.argv.append("input_file")
    sys.argv.append("-o")
    sys.argv.append("output_file")

    cli.run()

    assert cli.arguments is not None
    assert cli.arguments.verbose is True
    assert cli.arguments.input == "input_file"
    assert cli.arguments.output == "output_file"
