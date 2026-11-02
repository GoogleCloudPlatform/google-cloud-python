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

import sys

from google.api_core.protobuf_helpers import get_messages
from google.protobuf import any_pb2, empty_pb2, field_mask_pb2, timestamp_pb2
from google.rpc import status_pb2

from grafeas.grafeas_v1.proto import (
    attestation_pb2,
    build_pb2,
    common_pb2,
    cvss_pb2,
    deployment_pb2,
    discovery_pb2,
    grafeas_pb2,
    image_pb2,
    package_pb2,
    provenance_pb2,
    upgrade_pb2,
    vulnerability_pb2,
)

_shared_modules = [
    any_pb2,
    empty_pb2,
    field_mask_pb2,
    timestamp_pb2,
    status_pb2,
]

_local_modules = [
    attestation_pb2,
    build_pb2,
    common_pb2,
    cvss_pb2,
    deployment_pb2,
    discovery_pb2,
    grafeas_pb2,
    image_pb2,
    package_pb2,
    provenance_pb2,
    upgrade_pb2,
    vulnerability_pb2,
]

names = []

for module in _shared_modules:  # pragma: NO COVER
    for name, message in get_messages(module).items():
        setattr(sys.modules[__name__], name, message)
        names.append(name)
for module in _local_modules:
    for name, message in get_messages(module).items():
        message.__module__ = "grafeas.grafeas_v1.types"
        setattr(sys.modules[__name__], name, message)
        names.append(name)


__all__ = tuple(sorted(names))
