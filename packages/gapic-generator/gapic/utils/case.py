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


def to_snake_case(s: str) -> str:
    """Convert any string to snake case.

    This is provided to templates as the ``snake_case`` filter.

    Args:
        s (str): The input string, provided in any sane case system without spaces.

    Returns:
        str: The string in snake case (and all lower-cased).
    """
    # Replace all capital letters that are preceded by a lower-case letter.
    s = re.sub(r"(?<=[a-z])([A-Z])", r"_\1", str(s))

    # Find all capital letters that are followed by a lower-case letter,
    # and are preceded by any character other than underscore.
    # (Note: This also excludes beginning-of-string.)
    s = re.sub(r"(?<=[^_])([A-Z])(?=[a-z])", r"_\1", s)

    # Numbers are a weird case; the goal is to spot when they _start_
    # some kind of name or acronym (e.g. 2FA, 3M).
    #
    # Find cases of a number preceded by a lower-case letter _and_
    # followed by at least two capital letters or a single capital and
    # end of string.
    s = re.sub(r"(?<=[a-z])(\d)(?=[A-Z]{2})", r"_\1", s)
    s = re.sub(r"(?<=[a-z])(\d)(?=[A-Z]$)", r"_\1", s)

    # Done; return the camel-cased string.
    return s.lower()


def to_camel_case(s: str) -> str:
    """Convert any string to camel case.

    This is provided to templates as the ``camel_case`` filter.

    Args:
        s (str): The input string, provided in any sane case system without spaces.

    Returns:
        str: The string in lower camel case.
    """

    items = re.split(r"[_-]", to_snake_case(s))
    return items[0].lower() + "".join(x.capitalize() for x in items[1:])
