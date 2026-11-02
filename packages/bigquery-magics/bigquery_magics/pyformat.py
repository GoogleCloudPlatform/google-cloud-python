# Copyright 2025 Google LLC
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

"""Helpers for the --pyformat feature."""

from __future__ import annotations

import numbers
import string
from typing import Any


def _field_to_template_value(name: str, value: Any) -> Any:
    """Convert value to something embeddable in a SQL string.

    Does **not** escape strings.
    """
    _validate_type(name, value)
    # TODO(tswast): convert DataFrame objects to gbq tables or literals subquery.
    return value


def _validate_type(name: str, value: Any):
    """Raises TypeError if value is unsupported."""
    if not isinstance(value, (str, numbers.Real)):
        raise TypeError(
            f"{name} has unsupported type: {type(value)}. "
            "Only str, int, float are supported."
        )


def _parse_fields(sql_template: str) -> list[str]:
    return [
        field_name
        for _, field_name, _, _ in string.Formatter().parse(sql_template)
        if field_name is not None
    ]


def pyformat(sql_template: str, user_ns: dict) -> str:
    """Unsafe Python-style string formatting of SQL string.

    Only some data types supported.

    Warning: strings are **not** escaped. This allows them to be used in
    contexts such as table identifiers, where normal query parameters are not
    supported.

    Args:
        sql_template (str):
            SQL string with 0+ {var_name}-style format options.
        user_ns (dict):
            IPython variable namespace to use for formatting.

    Raises:
        TypeError: if a referenced variable is not of a supported type.
        KeyError: if a referenced variable is not found.
    """
    fields = _parse_fields(sql_template)

    format_kwargs = {}
    for name in fields:
        value = user_ns[name]
        format_kwargs[name] = _field_to_template_value(name, value)

    return sql_template.format(**format_kwargs)
