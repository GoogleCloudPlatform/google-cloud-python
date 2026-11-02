# Copyright 2020 Google LLC
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

from gapic.utils import checks
from test_utils.test_utils import make_field, make_message


def test_is_str_field_pb():
    msg_field = make_field("msg_field", message=make_message("test_msg"))
    str_field = make_field("str_field", type=9)
    int_field = make_field("int_field", type=5)
    assert not checks.is_str_field_pb(msg_field.field_pb)
    assert checks.is_str_field_pb(str_field.field_pb)
    assert not checks.is_str_field_pb(int_field.field_pb)


def test_is_msg_field_pb():
    msg_field = make_field("msg_field", message=make_message("test_msg"))
    str_field = make_field("str_field", type=9)
    int_field = make_field("int_field", type=5)
    assert checks.is_msg_field_pb(msg_field.field_pb)
    assert not checks.is_msg_field_pb(str_field.field_pb)
    assert not checks.is_msg_field_pb(int_field.field_pb)
