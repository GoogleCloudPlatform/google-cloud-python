# Copyright 2021 Google LLC
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

from gapic.utils.reserved_names import RESERVED_NAMES
from google.api_core import path_template


def convert_uri_fieldnames(uri: str) -> str:
    """Modify field names in uri_templates to avoid reserved names.

    Args:
        uri: a uri template, optionally containing field references in {} braces.

    Returns:
        the uri with any field names modified if they conflict with
        reserved names.
    """

    def _fix_name_segment(name_seg: str) -> str:
        return name_seg + "_" if name_seg in RESERVED_NAMES else name_seg

    def _fix_field_path(field_path: str) -> str:
        return ".".join(
            (_fix_name_segment(name_seg) for name_seg in field_path.split("."))
        )

    last = 0
    pieces = []
    for match in path_template._VARIABLE_RE.finditer(uri):
        start_pos, end_pos = match.span("name")
        if start_pos == end_pos:
            continue
        pieces.append(uri[last:start_pos])
        fixed_field_path = _fix_field_path(uri[start_pos:end_pos])
        pieces.append(fixed_field_path)
        last = end_pos
    pieces.append(uri[last:])

    return "".join(pieces)
