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
from functools import partial
from typing import Any

import sphinx.application
from docutils import nodes
from sphinx import addnodes, directives
from sphinx.addnodes import desc, desc_signature
from sphinx.util import docfields
from sphinx.util.docfields import _is_single_paragraph

from .nodes import remarks
from .utils import transform_node as _transform_node

TYPE_SEP_PATTERN = r"(\[|\]|, |\(|\))"


def _get_desc_data(node: nodes.Node) -> tuple[str | None, str | None]:
    """Gets the description data from a node.
    Args:
        node (nodes.Node): The node to get the description data from.
    Returns:
        tuple[str | None, str | None]: A tuple containing the full name
            and uid of the node.
    """
    assert node.tagname == "desc"
    if node.attributes["domain"] != "py":
        print("Skipping Domain Object (%s)" % node.attributes["domain"])
        return None, None

    try:
        module = node[0].attributes["module"]
        full_name = node[0].attributes["fullname"].split(".")[-1]
    except KeyError as e:
        print(
            "[docfx_yaml] There maybe some syntax error in docstring near: "
            + node.astext()
        )
        raise e

    try:
        uid = node[0].attributes["ids"][0]
    except Exception:
        uid = f"{module}.{full_name}"
        print("Non-standard id: %s" % uid)
    return full_name, uid


def _is_desc_of_enum_class(node: nodes.Node) -> bool:
    """Checks if the node is a description of an enum class.
    Args:
        node (nodes.Node): The node to check.
    Returns:
        bool: True if the node is a description of an enum class,
            False otherwise.
    """
    assert node.tagname == "desc_content"
    if (
        node[0]
        and node[0].tagname == "paragraph"
        and node[0].astext() == "Bases: enum.Enum"
    ):
        return True

    return False


def _hacked_transform(typemap: dict, node: nodes.Node) -> tuple[list, dict]:
    """
    Taken from docfields.py from sphinx.

    This does all the steps around gathering data,
    but doesn't actually do the node transformations.
    """
    entries = []
    groupindices = {}
    types = {}

    # step 1: traverse all fields and collect field types and content
    for field in node:
        fieldname, fieldbody = field
        try:
            # split into field type and argument
            fieldtype, fieldarg = fieldname.astext().split(None, 1)
        except ValueError:
            # maybe an argument-less field type?
            fieldtype, fieldarg = fieldname.astext(), ""
        typedesc, is_typefield = typemap.get(fieldtype, (None, None))

        # sort out unknown fields
        if typedesc is None or typedesc.has_arg != bool(fieldarg):
            # either the field name is unknown, or the argument doesn't
            # match the spec; capitalize field name and be done with it
            new_fieldname = fieldtype[0:1].upper() + fieldtype[1:]
            if fieldarg:
                new_fieldname += " " + fieldarg
            fieldname[0] = nodes.Text(new_fieldname)
            entries.append(field)
            continue

        typename = typedesc.name

        # collect the content, trying not to keep unnecessary paragraphs
        if _is_single_paragraph(fieldbody):
            content = fieldbody.children[0].children
        else:
            content = fieldbody.children

        # if the field specifies a type, put it in the types collection
        if is_typefield:
            # filter out only inline nodes; others will result in invalid
            # markup being written out
            content = [
                n
                for n in content
                if isinstance(n, nodes.Inline) or isinstance(n, nodes.Text)
            ]
            if content:
                types.setdefault(typename, {})[fieldarg] = content
            continue

        # also support syntax like ``:param type name:``
        if typedesc.is_typed:
            try:
                argtype, argname = fieldarg.split(None, 1)
            except ValueError:
                pass
            else:
                types.setdefault(typename, {})[argname] = [nodes.Text(argtype)]
                fieldarg = argname

        translatable_content = nodes.inline(fieldbody.rawsource, translatable=True)
        translatable_content.source = fieldbody.parent.source
        translatable_content.line = fieldbody.parent.line
        translatable_content += content

        # grouped entries need to be collected in one entry, while others
        # get one entry per field
        if typedesc.is_grouped:
            if typename in groupindices:
                group = entries[groupindices[typename]]
            else:
                groupindices[typename] = len(entries)
                group = [typedesc, []]
                entries.append(group)
            entry = typedesc.make_entry(fieldarg, [translatable_content])
            group[1].append(entry)
        else:
            entry = typedesc.make_entry(fieldarg, [translatable_content])
            entries.append([typedesc, entry])

    return (entries, types)


def patch_docfields(app: sphinx.application.Sphinx) -> None:
    """
    Grab syntax data from the Sphinx info fields.

    This is done by monkeypatching into the DocFieldTransformer,
    which is what Sphinx uses to transform the docutils ``nodes.field``
    into the sphinx ``docfields.Field`` objects.

    See usage in Sphinx
    `here <https://github.com/sphinx-doc/sphinx/blob/master/sphinx/directives/__init__.py#L180>`_.

    This also performs the RST doctree to Markdown transformation on the content,
    using the :class:`docfx_yaml.writers.MarkdownWriter`.
    """

    transform_node = partial(_transform_node, app)

    def get_data_structure(
        entries: list, types: dict, field_object: nodes.Node
    ) -> dict:
        """
        Get a proper docfx YAML data structure from the entries & types
        """

        data = {
            "parameters": [],
            "variables": [],
            "exceptions": [],
            "return": {},
            "references": [],
        }

        def make_param(_id, _description, _type=None, _required=None):
            ret = {"id": _id, "description": _description.strip(" \n\r\t")}
            if _type:
                ret["type"] = _type

            if _required is not None:
                ret["isRequired"] = _required

            return ret

        def transform_para(para_field):
            if isinstance(para_field, addnodes.pending_xref):
                return transform_node(para_field)
            else:
                return para_field.astext()

        def resolve_type(data_type):
            # Remove @ ~ and \n for cross reference in parameter/return value type to apply to docfx correctly
            data_type = re.sub("[@~\n]", "", data_type)

            # Add references for docfx to resolve ref if type contains TYPE_SEP_PATTERN
            _spec_list = []
            _spec_fullnames = re.split(TYPE_SEP_PATTERN, data_type)

            _added_reference = {}
            if len(_spec_fullnames) > 1:
                _added_reference_name = ""
                for _spec_fullname in _spec_fullnames:
                    if _spec_fullname != "":
                        _spec = {}
                        _spec["name"] = _spec_fullname.split(".")[-1]
                        _spec["fullName"] = _spec_fullname
                        if re.match(TYPE_SEP_PATTERN, _spec_fullname) is None:
                            _spec["uid"] = _spec_fullname
                        _spec_list.append(_spec)
                        _added_reference_name += _spec["name"]

                _added_reference = {
                    "uid": data_type,
                    "name": _added_reference_name,
                    "fullName": data_type,
                    "spec.python": _spec_list,
                }

            return data_type, _added_reference

        def extract_exception_desc(field_object):
            ret = []
            if len(field_object) > 0:
                for field in field_object:
                    if (
                        "field_name" == field[0].tagname
                        and field[0].astext() == "Raises"
                    ):
                        assert field[1].tagname == "field_body"
                        field_body = field[1]

                        children = [
                            n for n in field_body if not isinstance(n, nodes.Invisible)
                        ]

                        for child in children:
                            if isinstance(child, nodes.paragraph):
                                pending_xref_index = child.first_child_matching_class(
                                    addnodes.pending_xref
                                )
                                if pending_xref_index is not None:
                                    pending_xref = child[pending_xref_index]
                                    raise_type_index = (
                                        pending_xref.first_child_matching_class(
                                            nodes.literal
                                        )
                                    )
                                    if raise_type_index is not None:
                                        raise_type = pending_xref[raise_type_index]
                                        ret.append(
                                            {
                                                "type": pending_xref["reftarget"],
                                                "desc": raise_type.astext(),
                                            }
                                        )

            return ret

        for entry in entries:
            if isinstance(entry, nodes.field):
                # pass-through old field
                pass
            else:
                fieldtype, content = entry
                fieldtypes = types.get(fieldtype.name, {})
                if fieldtype.name == "exceptions":
                    for _type, _description in content:
                        data["exceptions"].append(
                            {
                                "type": _type,
                                "description": transform_node(_description[0]).strip(
                                    " \n\r\t"
                                ),
                            }
                        )
                if fieldtype.name == "returntype":
                    for returntype_node in content[1]:
                        returntype_ret = transform_node(returntype_node)
                        if returntype_ret:
                            # Support or in returntype
                            for returntype in re.split("[ \n]or[ \n]", returntype_ret):
                                returntype, _added_reference = resolve_type(returntype)
                                if _added_reference:
                                    if len(data["references"]) == 0:
                                        data["references"].append(_added_reference)
                                    elif any(
                                        r["uid"] != _added_reference["uid"]
                                        for r in data["references"]
                                    ):
                                        data["references"].append(_added_reference)

                                data["return"].setdefault("type", []).append(returntype)
                if fieldtype.name == "returnvalue":
                    returnvalue_ret = transform_node(content[1][0])
                    if returnvalue_ret:
                        data["return"]["description"] = returnvalue_ret.strip(" \n\r\t")
                if fieldtype.name in ["parameter", "variable", "keyword"]:
                    for field, node_list in content:
                        _id = field
                        _description = transform_node(node_list[0])
                        if field in fieldtypes:
                            _type = "".join(
                                transform_para(n) for n in fieldtypes[field]
                            )
                        else:
                            _type = None

                        _para_types = []
                        if fieldtype.name == "parameter" or fieldtype.name == "keyword":
                            if _type:
                                # Support or in parameter type
                                for _s_type in re.split("[ \n]or[ \n]", _type):
                                    _s_type, _added_reference = resolve_type(_s_type)
                                    if _added_reference:
                                        if len(data["references"]) == 0:
                                            data["references"].append(_added_reference)
                                        elif any(
                                            r["uid"] != _added_reference["uid"]
                                            for r in data["references"]
                                        ):
                                            data["references"].append(_added_reference)

                                    _para_types.append(_s_type)

                            _data = make_param(
                                _id=_id,
                                _type=_para_types,
                                _description=_description,
                                _required=False
                                if fieldtype.name == "keyword"
                                else True,
                            )
                            data["parameters"].append(_data)

                        if fieldtype.name == "variable":
                            if _type:
                                # Support or in variable type
                                for _s_type in re.split("[ \n]or[ \n]", _type):
                                    _s_type, _added_reference = resolve_type(_s_type)
                                    if _added_reference:
                                        if len(data["references"]) == 0:
                                            data["references"].append(_added_reference)
                                        elif any(
                                            r["uid"] != _added_reference["uid"]
                                            for r in data["references"]
                                        ):
                                            data["references"].append(_added_reference)

                                    _para_types.append(_s_type)

                            _data = make_param(
                                _id=_id, _type=_para_types, _description=_description
                            )
                            data["variables"].append(_data)

                    ret_list = extract_exception_desc(field_object)
                    for ret in ret_list:
                        # only use type in exceptions
                        data.setdefault("exceptions", []).append({"type": ret["type"]})

        return data

    class PatchedDocFieldTransformer(docfields.DocFieldTransformer):
        @staticmethod
        def type_mapping(type_name: str) -> str:
            """Maps a type name to a docfx type name.
            Args:
                type_name (str): The type name to map.
            Returns:
                str: The mapped type name.
            """
            mapping = {
                "staticmethod": "method",
                "classmethod": "method",
                "exception": "class",
            }

            return mapping[type_name] if type_name in mapping else type_name

        def __init__(self, directive: Any):
            """Initializes the transformer.
            Args:
                directive (Any): The directive.
            """
            self.directive = directive
            super(PatchedDocFieldTransformer, self).__init__(directive)

        def transform_all(self, node: nodes.Node) -> None:
            """Transform all field list children of a node."""
            # don't traverse, only handle field lists that are immediate children
            summary = []
            data = {}
            name, uid = _get_desc_data(node.parent)
            for child in node:
                if isinstance(child, remarks):
                    remarks_string = transform_node(child)
                    data["remarks"] = remarks_string
                elif isinstance(child, addnodes.desc):
                    if child.get("desctype") == "attribute":
                        attribute_map = {}  # Used for detecting duplicated attributes in intermediate data and merge them

                        for item in child:
                            if isinstance(item, desc_signature) and any(
                                isinstance(n, addnodes.desc_annotation) for n in item
                            ):
                                # capture attributes data and cache it
                                data.setdefault("added_attribute", [])

                                item_ids = item.get("ids", [""])

                                if (
                                    len(item_ids) == 0
                                ):  # find a node with no 'ids' attribute
                                    curuid = (
                                        item.get("module", "")
                                        + "."
                                        + item.get("fullname", "")
                                    )
                                    # generate its uid by module and fullname
                                else:
                                    curuid = item_ids[0]

                                if len(curuid) > 0:
                                    parent = curuid[: curuid.rfind(".")]
                                    name = item.children[0].astext()

                                    if curuid in attribute_map:
                                        if (
                                            len(item_ids) == 0
                                        ):  # ensure the order of docstring attributes and real attributes is fixed
                                            attribute_map[curuid]["syntax"][
                                                "content"
                                            ] += " " + item.astext()
                                            # concat the description of duplicated nodes
                                        else:
                                            attribute_map[curuid]["syntax"][
                                                "content"
                                            ] = (
                                                item.astext()
                                                + " "
                                                + attribute_map[curuid]["syntax"][
                                                    "content"
                                                ]
                                            )
                                    else:
                                        if _is_desc_of_enum_class(node):
                                            addedData = {
                                                "uid": curuid,
                                                "id": name,
                                                "parent": parent,
                                                "langs": ["python"],
                                                "name": name,
                                                "fullName": curuid,
                                                "type": item.parent.get("desctype"),
                                                "module": item.get("module"),
                                                "syntax": {
                                                    "content": item.astext(),
                                                    "return": {"type": [parent]},
                                                },
                                            }
                                        else:
                                            addedData = {
                                                "uid": curuid,
                                                "class": parent,
                                                "langs": ["python"],
                                                "name": name,
                                                "fullName": curuid,
                                                "type": "attribute",
                                                "module": item.get("module"),
                                                "syntax": {"content": item.astext()},
                                            }

                                        attribute_map[curuid] = addedData
                                else:
                                    raise Exception(
                                        "ids of node: " + repr(item) + " is missing."
                                    )
                                    # no ids and no duplicate or uid can not be generated.
                        if "added_attribute" in data:
                            data["added_attribute"].extend(
                                attribute_map.values()
                            )  # Add attributes data to a temp list

                    # Don't recurse into child nodes
                    continue
                elif isinstance(child, nodes.field_list):
                    (entries, types) = _hacked_transform(self.typemap, child)
                    _data = get_data_structure(entries, types, child)
                    data.update(_data)
                elif isinstance(child, addnodes.seealso):
                    data["seealso"] = transform_node(child)
                elif (
                    isinstance(child, nodes.admonition)
                    and "Example" in child[0].astext()
                ):
                    # Remove the admonition node
                    child_copy = child.deepcopy()
                    child_copy.pop(0)
                    data["example"] = transform_node(child_copy)
                else:
                    content = transform_node(child)

                    # skip 'Bases' in summary
                    if not content.startswith("Bases: "):
                        summary.append(content)

            if "desctype" in node.parent and node.parent["desctype"] == "class":
                data.pop(
                    "exceptions", ""
                )  # Make sure class doesn't have 'exceptions' field.

            if summary:
                data["summary"] = "\n".join(summary)
            # Don't include empty data
            for key, val in data.copy().items():
                if not val:
                    del data[key]
            data["type"] = (
                PatchedDocFieldTransformer.type_mapping(node.parent["desctype"])
                if "desctype" in node.parent
                else "unknown"
            )
            self.directive.env.docfx_info_field_data[uid] = data
            super(PatchedDocFieldTransformer, self).transform_all(node)

    directives.DocFieldTransformer = PatchedDocFieldTransformer
