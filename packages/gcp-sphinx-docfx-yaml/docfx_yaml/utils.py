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

import re
from collections import namedtuple
from inspect import signature

from docutils import nodes
from docutils.frontend import OptionParser
from docutils.utils import new_document
from sphinx import addnodes
from sphinx.application import Sphinx

from .writer import MarkdownTranslator
from .writer import MarkdownWriter as Writer

_DEFAULT_SETTINGS = OptionParser(components=(Writer,)).get_default_values()


def slugify(value: str) -> str:
    """Converts to lowercase, removes non-word characters.

    Converts non-word characters (alphanumerics and
    underscores) and converts spaces to hyphens. Also strips leading and
    trailing whitespace.

    Args:
        value (str): The string to convert.

    Returns:
        str: The converted string.
    """
    value = re.sub(r"[^\w\s-]", "", value).strip()
    return re.sub(r"[-\s]+", "-", value)


def transform_string(app: Sphinx, string: str) -> str:
    """Transforms a string by parsing it and then writing it out.

    This is useful for resolving references in the string.

    Args:
        app (Sphinx): The sphinx application.
        string (str): The string to transform.

    Returns:
        str: The transformed string.
    """
    ret = []
    for para in string.split("\n\n"):
        tmp = nodes.paragraph(para, para)
        ret.append(transform_node(app, tmp))
    return "\n\n".join(ret)


def transform_node(app: Sphinx, node: nodes.Node) -> str:
    """Transforms a docutils node to a string.

    Args:
        app (Sphinx): The sphinx application.
        node (nodes.Node): The node to transform.

    Returns:
        str: The transformed node as a string.
    """
    if node.parent is not None:
        node = node.deepcopy()
    doc = new_document(b"<partial node>", _DEFAULT_SETTINGS)
    doc.append(node)

    # Resolve refs only when the node actually contains pending cross-references
    doc["docname"] = "inmemory"
    if any(True for _ in node.traverse(addnodes.pending_xref)):
        app.env.resolve_references(
            doctree=doc, fromdocname="inmemory", builder=app.builder
        )

    visitor = MarkdownTranslator(doc, app.builder)
    doc.walkabout(visitor)
    return visitor.body
