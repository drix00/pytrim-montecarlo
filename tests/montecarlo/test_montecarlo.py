#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule:: tests.montecarlo.test_montecarlo

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
import os.path
import logging

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo import __author__, __email__, __version__, __copyright__, __project_name__
from trim.montecarlo import get_current_module_path
from trim.montecarlo import get_log_file_path, setup_logger

# Globals and constants variables.


def test_author():
    assert __author__ != ""


def test_email():
    assert __email__ != ""


def test_version():
    assert __version__ != ""


def test_current_version():
    assert __version__ == '0.1.0'


def test_copyright():
    assert __copyright__ != ""


def test_project_name():
    assert __project_name__ != ""


def test_get_current_module_path():
    path = get_current_module_path(__file__)
    assert os.path.isdir(path)


def test_get_current_module_path_invalid_file():
    path = get_current_module_path(__file__, 'bad_file.bad')
    assert not os.path.isdir(path)
    assert not os.path.isfile(path)
    assert not os.path.exists(path)


def test_get_log_file_path():
    assert os.path.isdir(get_log_file_path())


def test_setup_logger():
    assert logging.getLogger().name == "root"
    assert logging.getLogger().hasHandlers()
    assert logging.getLogger().getEffectiveLevel() == logging.WARNING
    setup_logger()
    assert logging.getLogger().name == "root"
    assert logging.getLogger().hasHandlers()
    assert logging.getLogger().getEffectiveLevel() == logging.DEBUG
