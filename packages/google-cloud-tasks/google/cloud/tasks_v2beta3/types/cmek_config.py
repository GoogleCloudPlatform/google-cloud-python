# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.tasks.v2beta3",
    manifest={
        "CmekConfig",
    },
)


class CmekConfig(proto.Message):
    r"""Describes the customer-managed encryption key (CMEK)
    configuration associated with a project and location.

    Attributes:
        name (str):
            Output only. The config resource name which includes the
            project and location and must end in 'cmekConfig', in the
            format
            projects/PROJECT_ID/locations/LOCATION_ID/cmekConfig\`
        kms_key (str):
            Resource name of the Cloud KMS key, of the form
            ``projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING_ID/cryptoKeys/KEY_ID``,
            that will be used to encrypt the Queues & Tasks in the
            region. Setting this as blank will turn off CMEK encryption.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
