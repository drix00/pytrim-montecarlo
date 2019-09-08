#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.options

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Options for the Monte Carlo simulation program.
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
from trim.montecarlo.options.source import Source

# Globals and constants variables.
GROUP_OPTIONS = "options"


class Options:
    def __init__(self):
        self.source = Source()

    def write(self, parent_group):
        options_group = parent_group.require_group(GROUP_OPTIONS)

        self.source.write(options_group)

    def read(self, parent_group):
        options_group = parent_group.require_group(GROUP_OPTIONS)

        self.source.read(options_group)
