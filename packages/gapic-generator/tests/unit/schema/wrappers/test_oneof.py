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

import collections

import pytest

from google.api import field_behavior_pb2
from google.protobuf import descriptor_pb2

from gapic.schema import metadata
from gapic.schema import wrappers

from test_utils.test_utils import (
    make_oneof_pb2,
)


def test_wrapped_oneof():
    oneof_pb = make_oneof_pb2("oneof_name")
    wrapped = wrappers.Oneof(oneof_pb=oneof_pb)

    assert wrapped.oneof_pb == oneof_pb
    assert wrapped.name == oneof_pb.name
