#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.pytrim_montecarlo

.. moduleauthor:: Hendrix Demers <hendrix.demers@mail.mcgill.ca>

Main of the application pyTRIM-MonteCarlo.
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
import logging.config
import os

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo import get_current_module_path

# Globals and constants variables.
logger = getLogger(__name__)


def get_log_file_path():
    path = get_current_module_path(__file__, "../../logs")
    logger.debug("log_file_path: %s", path)
    if not os.path.isdir(path):  # pragma: no cover
        os.makedirs(path)

    return path


def setup_logger():
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)

    log_format = '%(asctime)s : %(name)-40s : %(levelname)-10s : %(message)s'
    formatter = logging.Formatter(log_format)

    ch.setFormatter(formatter)

    root_logger.addHandler(ch)

    path = get_log_file_path()
    log_file_path = os.path.join(path, "{}.log".format("pytrim_montecarlo"))
    fh = logging.FileHandler(log_file_path)
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    root_logger.addHandler(fh)


if __name__ == '__main__':  # pragma: no cover
    setup_logger()
    logger.warning("test warning log")
    logger.info("test info log")
    logger.debug("test debug log")
