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
This module is used to add extra supported nodes to sphinx.
"""

from docutils import nodes


class remarks(nodes.paragraph, nodes.Element):
    """A docutils node for 'remarks' messages."""

    @staticmethod
    def visit_remarks(self, node: nodes.Node) -> None:
        """Visit a 'remarks' node."""
        self.visit_paragraph(node)

    @staticmethod
    def depart_remarks(self, node: nodes.Node) -> None:
        """Depart a 'remarks' node."""
        self.depart_paragraph(node)
