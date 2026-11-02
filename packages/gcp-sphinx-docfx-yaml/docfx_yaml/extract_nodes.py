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

"""
**DEPRECATED**

This was an approach that pulls domain data from doctree.

This approach will work for non-autodoc domains.
However,
the approach used in this extension is easiest for autodoc.

In order to build the approach going forward,
a bit more work needs to be done to pull docstrings in raw format.
"""

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util.console import bold, red
from sphinx.util.docfields import _is_single_paragraph

from .utils import _get_desc_data

TITLE_MAP = {
    "Returns": "return",
    "Return type": "return_type",
    "Raises": "raises",
    "Parameters": "params",
}


def doctree_resolved(app: Sphinx, doctree: nodes.document, docname: str) -> None:
    """
    Render out the YAML from the Sphinx domain objects

    Args:
        app (Sphinx): The sphinx application.
        doctree (nodes.document): The doctree.
        docname (str): The name of the document.
    """
    yaml_data, yaml_modules = extract_yaml(app, doctree, ignore_patterns=None)
    extract_info_lists(app, doctree)
    # if yaml_data:
    #     app.env.docfx_yaml_data[docname] = yaml_data
    # if yaml_modules:
    #     for module in yaml_modules:
    #         app.env.docfx_yaml_modules[module] = yaml_modules[module]


def _get_full_data(node: nodes.Node) -> dict:
    """Extracts data from a field list node.

    Args:
        node (nodes.Node): The field list node.

    Returns:
        dict: The extracted data.
    """
    data = {}
    parent_desc = node.parent.parent
    name, uid = _get_desc_data(parent_desc)
    if not name:
        return

    for field in node:
        fieldname, fieldbody = field
        try:
            # split into field type and argument
            fieldtype, _ = fieldname.astext().split(None, 1)
        except ValueError:
            # maybe an argument-less field type?
            fieldtype = fieldname.astext()

        # collect the content, trying not to keep unnecessary paragraphs
        if _is_single_paragraph(fieldbody):
            content = fieldbody.children[0].children
        else:
            content = fieldbody.children

        data.setdefault(uid, {})

        if fieldtype == "Returns":
            for child in content:
                ret_data = child.astext()
                data[uid].setdefault(fieldtype, []).append(ret_data)

        if fieldtype == "Raises":
            for child in content:
                ret_data = child.astext()
                data[uid].setdefault(fieldtype, []).append(ret_data)
    return data


def extract_info_lists(app: Sphinx, doctree: nodes.document) -> None:
    """Extracts info lists from the doctree.

    Args:
        app (Sphinx): The sphinx application.
        doctree (nodes.document): The doctree.
    """
    data = []

    for node in doctree.traverse(nodes.field_list):
        data.append(_get_full_data(node))

    print(data)


def extract_yaml(
    app: Sphinx, doctree: nodes.document, ignore_patterns: list[str]
) -> tuple[list[dict], dict]:
    """Iterate over all Python domain objects and output YAML.

    Args:
        app (Sphinx): The sphinx application.
        doctree (nodes.document): The doctree.
        ignore_patterns (list[str]): A list of patterns to ignore.

    Returns:
        tuple[list[dict], dict]: A tuple containing the list of items and
            a dictionary of modules.
    """
    items = []
    modules = {}

    for desc_node in doctree.traverse(addnodes.desc):
        if desc_node.attributes["domain"] != "py":
            app.info(
                bold("[docfx_yaml] ")
                + red("Skipping Domain Object (%s)" % desc_node.attributes["domain"])
            )
            continue

        module = desc_node[0].attributes["module"]

        if not module:
            app.info(bold("[docfx_yaml] ") + red("Skipping object with no module"))
            continue

        if module not in modules:
            modules[module] = [
                {
                    "module": str(module),
                    "uid": str(module),
                    "type": "Namespace",
                    "type": "module",
                    "name": str(module),
                    "children": [],
                }
            ]

        _type = desc_node.attributes["objtype"]
        full_name = desc_node[0].attributes["fullname"]
        try:
            uid = desc_node[0].attributes["ids"][0]
        except Exception:
            uid = f"{module}.{full_name}"
            print("Non-standard id: %s" % uid)
        name = desc_node[0].attributes["names"][0]
        source = desc_node[0].source
        try:
            summary = desc_node[1][0].astext()
        except (KeyError, IndexError):
            summary = ""

        try:
            args = [arg.strip() for arg in desc_node[0][3].astext().split(",")]
        except Exception:
            args = []

        if args:
            full_name += f"({', '.join(args)})"

        datam = {
            "module": str(module),
            "uid": uid,
            "type": _type,
            "name": name,
            "fullName": full_name,
            "summary": summary,
            "rst_source": source,
        }

        if _type == "method":
            datam["class"] = ".".join(name.split(".")[:-1])
        if _type == "class":
            datam["children"] = []

        # insert_children(_type, datam, modules)
        items.append(datam)

        modules[module].append(datam)

    return (items, modules)
