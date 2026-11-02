# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re


def to_valid_filename(filename: str) -> str:
    """Given any string, return a valid filename.

    For this purpose, filenames are expected to be all lower-cased,
    and we err on the side of being more restrictive with allowed characters,
    including not allowing space.

    Args:
        filename (str): The input filename.

    Returns:
        str: A valid filename.
    """
    return re.sub(r"[^a-z0-9.$_-]+", "-", filename.lower())


def to_valid_module_name(module_name: str) -> str:
    """Given any string, return a valid Python module name.

    Args:
        module_name (str): The input filename

    Returns:
        str: A valid module name. Extensions (e.g. *.py), if present,
        are untouched.
    """
    return to_valid_filename(module_name).replace("-", "_")
