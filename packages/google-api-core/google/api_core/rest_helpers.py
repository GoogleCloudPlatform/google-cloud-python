# Copyright 2021 Google LLC
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

"""Helpers for rest transports."""

import functools
import json
import operator
from typing import Any, Dict, List, Optional, Tuple

from google.protobuf import json_format

from google.api_core import path_template

__all__ = ["flatten_query_params", "transcode", "transcode_request"]


def flatten_query_params(obj, strict=False):
    """Flatten a dict into a list of (name,value) tuples.

    The result is suitable for setting query params on an http request.

    .. code-block:: python

        >>> obj = {'a':
        ...         {'b':
        ...           {'c': ['x', 'y', 'z']} },
        ...      'd': 'uvw',
        ...      'e': True, }
        >>> flatten_query_params(obj, strict=True)
        [('a.b.c', 'x'), ('a.b.c', 'y'), ('a.b.c', 'z'), ('d', 'uvw'), ('e', 'true')]

    Note that, as described in
    https://github.com/googleapis/googleapis/blob/48d9fb8c8e287c472af500221c6450ecd45d7d39/google/api/http.proto#L117,
    repeated fields (i.e. list-valued fields) may only contain primitive types (not lists or dicts).
    This is enforced in this function.

    Args:
      obj: a possibly nested dictionary (from json), or None
      strict: a bool, defaulting to False, to enforce that all values in the
              result tuples be strings and, if boolean, lower-cased.

    Returns: a list of tuples, with each tuple having a (possibly) multi-part name
      and a scalar value.

    Raises:
      TypeError if obj is not a dict or None
      ValueError if obj contains a list of non-primitive values.
    """

    if obj is not None and not isinstance(obj, dict):
        raise TypeError("flatten_query_params must be called with dict object")

    return _flatten(obj, key_path=[], strict=strict)


def _flatten(obj, key_path, strict=False):
    if obj is None:
        return []
    if isinstance(obj, dict):
        return _flatten_dict(obj, key_path=key_path, strict=strict)
    if isinstance(obj, list):
        return _flatten_list(obj, key_path=key_path, strict=strict)
    return _flatten_value(obj, key_path=key_path, strict=strict)


def _is_primitive_value(obj):
    if obj is None:
        return False

    if isinstance(obj, (list, dict)):
        raise ValueError("query params may not contain repeated dicts or lists")

    return True


def _flatten_value(obj, key_path, strict=False):
    return [(".".join(key_path), _canonicalize(obj, strict=strict))]


def _flatten_dict(obj, key_path, strict=False):
    items = (
        _flatten(value, key_path=key_path + [key], strict=strict)
        for key, value in obj.items()
    )
    return functools.reduce(operator.concat, items, [])


def _flatten_list(elems, key_path, strict=False):
    # Only lists of scalar values are supported.
    # The name (key_path) is repeated for each value.
    items = (
        _flatten_value(elem, key_path=key_path, strict=strict)
        for elem in elems
        if _is_primitive_value(elem)
    )
    return functools.reduce(operator.concat, items, [])


def _canonicalize(obj, strict=False):
    if strict:
        value = str(obj)
        if isinstance(obj, bool):
            value = value.lower()
        return value
    return obj


def transcode_request(
    http_options: List[Dict[str, str]],
    request: Any,
    required_fields_default_values: Optional[Dict[str, Any]] = None,
    rest_numeric_enums: bool = False,
) -> Tuple[Dict[str, Any], Optional[str], Dict[str, Any]]:
    """Transcodes a request into HTTP method, URI, body, and query parameters.

    Args:
        http_options (List[Dict[str, str]]): List of HTTP transcoding rules.
        request (Any): The protobuf or proto-plus request message.
        required_fields_default_values (Optional[Dict[str, Any]]): Dictionary
            of required fields default values to merge into query parameters if missing.
        rest_numeric_enums (bool): Whether to encode enums as integers.

    Returns:
        Tuple[Dict[str, Any], Optional[str], Dict[str, Any]]: A tuple containing:
            - The raw transcoded request dictionary (containing keys like 'uri', 'method').
            - The serialized request body JSON string, or None if no body.
            - The query parameters dictionary.
    """
    if request is None:
        raise TypeError("request cannot be None")

    # Convert proto-plus message to its underlying protobuf message if needed
    pb_request = getattr(request, "_pb", request)

    transcoded_request = path_template.transcode(http_options, pb_request)

    body_json = None
    if transcoded_request.get("body") is not None:
        body_json = json_format.MessageToJson(
            transcoded_request["body"],
            use_integers_for_enums=rest_numeric_enums,
        )

    query_params_json = {}
    if transcoded_request.get("query_params") is not None:
        query_params_json = json.loads(
            json_format.MessageToJson(
                transcoded_request["query_params"],
                use_integers_for_enums=rest_numeric_enums,
            )
        )

    # If required_fields_default_values is provided, we merge default values for missing
    # required fields into the query parameters.
    if required_fields_default_values:
        for k, v in required_fields_default_values.items():
            if k not in query_params_json:
                query_params_json[k] = v

    if rest_numeric_enums:
        query_params_json["$alt"] = "json;enum-encoding=int"

    return transcoded_request, body_json, query_params_json


transcode = transcode_request
