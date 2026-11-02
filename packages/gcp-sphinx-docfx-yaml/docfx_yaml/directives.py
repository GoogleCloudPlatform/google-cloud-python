# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
This module is used to add extra supported directives to sphinx.
"""

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

from .nodes import remarks


class RemarksDirective(BaseAdmonition):
    """A directive to handle 'remarks' blocks."""

    node_class = remarks


class TodoDirective(Directive):
    """A directive to ignore 'todo' blocks."""

    # Enable content in the directive
    has_content = True

    def run(self) -> list[nodes.Node]:
        """This directive is ignored, so return empty list."""
        return_nodes = []

        return return_nodes
