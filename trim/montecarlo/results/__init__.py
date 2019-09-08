#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.results

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Results for the Monte Carlo simulation program.
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
GROUP_RESULTS = "results"


class Results:
    def __init__(self):
        pass

    def write(self, parent_group):
        results_group = parent_group.require_group(GROUP_RESULTS)

    def read(self, parent_group):
        results_group = parent_group.require_group(GROUP_RESULTS)
