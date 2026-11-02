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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.iam.v1.logging",
    manifest={
        "AuditData",
    },
)


class AuditData(proto.Message):
    r"""Audit log information specific to Cloud IAM. This message is
    serialized as an ``Any`` type in the ``ServiceData`` message of an
    ``AuditLog`` message.

    Attributes:
        policy_delta (google.iam.v1.policy_pb2.PolicyDelta):
            Policy delta between the original policy and
            the newly set policy.
    """

    policy_delta: policy_pb2.PolicyDelta = proto.Field(
        proto.MESSAGE,
        number=2,
        message=policy_pb2.PolicyDelta,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
