#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.simulation

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>


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
from logging import getLogger

# Third party modules.

# Local modules.

# Project modules.

# Globals and constants variables.
logger = getLogger(__name__)


class Simulation:
    def __init__(self, input_file_path, output_file_path):
        logger.info("Simulation init")

        if input_file_path is None:
            raise ValueError("Need an input file path")

        self.input_file_path = input_file_path
        if output_file_path is None:
            self.output_file_path = self.input_file_path
        else:
            self.output_file_path = output_file_path

        logger.debug("input_file_path: {}".format(self.input_file_path))
        logger.debug("output_file_path: {}".format(self.output_file_path))

    def run(self):
        self.read_options()
        self.initialize_models()
        self.compute_trajectories()
        self.compute_results()
        self.write_results()

    def read_options(self):
        logger.info("Simulation read option")

    def initialize_models(self):
        logger.info("Simulation initialize models")

    def compute_trajectories(self):
        logger.info("Simulation compute trajectories")

    def compute_results(self):
        logger.info("Simulation compute results")

    def write_results(self):
        logger.info("Simulation write results")
