#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. py:currentmodule::

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

# Third party modules.

# Local modules.

# Project modules.
from trim.montecarlo.options.element import get_silicon_element
from trim.montecarlo import get_current_module_path
from trim.montecarlo.file import write

# Globals and constants variables.


def create_source_file():
    source = get_silicon_element()

    input_file_path = get_current_module_path(__file__, "../test_data/test_Element.hdf5")
    hdf5_file = write(input_file_path)

    source.write(hdf5_file)


if __name__ == '__main__':  # pragma: no cover
    create_source_file()
