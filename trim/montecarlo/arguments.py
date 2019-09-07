#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.arguments

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

CLI arguments for the program.
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
import argparse
from logging import getLogger

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo import __version__

# Globals and constants variables.
logger = getLogger(__name__)


def get_arguments():  # pragma: no cover
    description = 'TRansport of Ions in Matter (TRIM) Monte Carlo implemented in Python'
    parser = argparse.ArgumentParser(description=description,
                                     fromfile_prefix_chars='@',
                                     allow_abbrev=False)

    parser.add_argument('-v',
                        '--verbose',
                        action='store_true',
                        help='verbosity of the output')

    parser.add_argument('--version',
                        action='version',
                        help='version of the program')

    parser.add_argument('-i',
                        '--input',
                        type=str,
                        help='simulation options file',
                        required=True)

    parser.add_argument('-o',
                        '--output',
                        type=str,
                        help='simulation results file')

    parser.version = __version__

    arguments = parser.parse_args()
    logger.info("CLI arguments: {}".format(arguments))

    return arguments
