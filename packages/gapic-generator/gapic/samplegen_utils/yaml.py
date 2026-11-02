# Copyright (C) 2019  Google LLC
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

import dataclasses

from abc import abstractmethod, ABC
from textwrap import indent
from typing import List, Optional

"""Module containing classes used for dramatically simplified yaml rendering.

The yaml used for generating the samplegen manifest is simple and self contained,
The classes and rendering logic in this module are highly domain specific:
it is not advised for general use.
"""


class Element(ABC):
    """Abstract element that can be rendered."""

    INDENT_SPACES: int = 2

    @abstractmethod
    def render(self, spaces: int = 0) -> str:
        return ""


@dataclasses.dataclass(frozen=True)
class Null(Element):
    def render(self, spaces: int = 0) -> str:
        return ""


@dataclasses.dataclass(frozen=True)
class KeyVal(Element):
    """A single key/value entry."""

    key: str
    val: str

    def render(self, spaces: int = 0) -> str:
        whitespace = " " * spaces
        return f"{whitespace}{self.key}: {self.val}"


@dataclasses.dataclass(frozen=True)
class Collection(Element):
    """An ordered list of subobjects."""

    name: str
    elements: List[List[Element]]

    def render(self, spaces: int = 0) -> str:
        # This gives us output like
        # - cephalopod: squid
        #   bivalve: clam
        #   gastropod: whelk
        #
        # instead of
        # -  cephalopod: squid
        #   bivalve: clam
        #   gastropod: whelk
        return f"{self.name}:\n" + "\n".join(
            indent(
                "-"
                + "\n".join(
                    r for r in (e.render(spaces + self.INDENT_SPACES) for e in l) if r
                )[1:],
                " " * (spaces),
            )
            for l in self.elements
        )


@dataclasses.dataclass(frozen=True)
class Alias(Element):
    """An anchor to a map."""

    target: str

    def render(self, spaces: int = 0) -> str:
        whitespace = " " * spaces
        return f"{whitespace}<<: *{self.target}"


@dataclasses.dataclass(frozen=True)
class Map(Element):
    """A named collection with a list of attributes."""

    name: str
    anchor_name: Optional[str]
    elements: List[Element]

    def render(self, spaces: int = 0):
        maybe_anchor = (" &" + self.anchor_name) if self.anchor_name else ""
        element_str = "\n".join(
            e.render(spaces=spaces + self.INDENT_SPACES) for e in self.elements
        )
        whitespace = " " * spaces
        return f"{whitespace}{self.name}:{maybe_anchor}\n{element_str}"

    def get(self, key, default=None):
        # Use iter([]) instead of a generator expression due to a bug in pytest.
        # See https://github.com/pytest-dev/pytest-cov/issues/310 for details.
        return next(
            iter(
                [
                    e.val
                    for e in self.elements
                    if e.key == key  # type: ignore
                ]  # type: ignore
            ),
            default,
        )


@dataclasses.dataclass(frozen=True)
class Doc(Element):
    """A yaml document"""

    elements: List[Element]

    def render(self):
        return "---\n{}\n".format("\n".join(e.render() for e in self.elements))
