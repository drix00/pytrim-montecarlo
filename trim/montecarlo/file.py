#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: trim.montecarlo.file

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
import h5py

# Local modules.

# Project modules.

# Globals and constants variables.
logger = getLogger(__name__)


def read(file_path):
    hdf5_file = h5py.File(file_path, 'r', driver='core', backing_store=True)
    _log_hdf5_file(hdf5_file)
    return hdf5_file


def write(file_path):
    hdf5_file = h5py.File(file_path, 'a', driver='core', backing_store=True)
    _log_hdf5_file(hdf5_file)
    return hdf5_file


def _log_hdf5_file(hdf5_file):
    logger.info("HDF5 file path: {}".format(hdf5_file.filename))
    logger.debug("HDF5 ID: {}".format(hdf5_file.id))
    logger.debug("HDF5 mode: {}".format(hdf5_file.mode))
    logger.debug("HDF5 driver: {}".format(hdf5_file.driver))
    logger.debug("HDF5 library version: {}".format(hdf5_file.libver))
    logger.debug("HDF5  user block size (bytes): {}".format(hdf5_file. userblock_size))
