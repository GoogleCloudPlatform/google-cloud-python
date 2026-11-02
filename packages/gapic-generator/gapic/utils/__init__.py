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

from gapic.utils.cache import cached_property
from gapic.utils.cache import cached_proto_context
from gapic.utils.case import to_snake_case
from gapic.utils.case import to_camel_case
from gapic.utils.checks import is_msg_field_pb
from gapic.utils.checks import is_str_field_pb
from gapic.utils.code import empty
from gapic.utils.code import nth
from gapic.utils.code import partition
from gapic.utils.code import make_private
from gapic.utils.constants import UUID4_RE
from gapic.utils.doc import doc
from gapic.utils.filename import to_valid_filename
from gapic.utils.filename import to_valid_module_name
from gapic.utils.lines import sort_lines
from gapic.utils.lines import wrap
from gapic.utils.options import Options
from gapic.utils.reserved_names import RESERVED_NAMES
from gapic.utils.rst import rst
from gapic.utils.uri_conv import convert_uri_fieldnames


__all__ = (
    "cached_property",
    "cached_proto_context",
    "convert_uri_fieldnames",
    "doc",
    "empty",
    "is_msg_field_pb",
    "is_str_field_pb",
    "make_private",
    "nth",
    "Options",
    "partition",
    "RESERVED_NAMES",
    "rst",
    "sort_lines",
    "to_snake_case",
    "to_camel_case",
    "to_valid_filename",
    "to_valid_module_name",
    "UUID4_RE",
    "wrap",
)
