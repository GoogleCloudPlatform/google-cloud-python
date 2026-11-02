# -*- coding: utf-8 -*-
#
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


from __future__ import absolute_import

from typing import List

from google.api_core.protobuf_helpers import get_messages

from google.cloud.orgpolicy.v1 import orgpolicy_pb2

_modules = [orgpolicy_pb2]

names: List[str] = []

for module in _modules:
    for name, message in get_messages(module).items():
        message.__module__ = module.__name__
