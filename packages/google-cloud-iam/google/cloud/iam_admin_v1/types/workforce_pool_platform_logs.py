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
    package="google.iam.admin.v1",
    manifest={
        "WorkforcePoolAttributeSyncEventLog",
    },
)


class WorkforcePoolAttributeSyncEventLog(proto.Message):
    r"""Log payload for Workforce Pool Provider background user
    attribute sync events.

    Attributes:
        subject (str):
            The raw subject identifier of the user whose
            attributes are being synced. This identifies the
            specific user within the workforce pool.
        failure_reason (str):
            A machine-readable code indicating the reason for failure.
            Only populated when ``severity`` is ``ERROR``.

            Possible values include, but are not limited to:

            - ``PROVIDER_NOT_FOUND``: The user was not found in the
              identity provider.
            - ``IDP_UNREACHABLE``: The identity provider could not be
              reached.
            - ``ATTRIBUTE_MAPPING_ERROR``: The attribute mapping
              configuration is invalid.
            - ``INTERNAL_ERROR``: An internal error occurred during
              attribute synchronization.
        message (str):
            Human-readable details describing the
            attribute sync result. For successful syncs,
            this contains the updated user attributes if
            detailed audit logging is enabled. For failures,
            this describes the cause of the failure.
    """

    subject: str = proto.Field(
        proto.STRING,
        number=1,
    )
    failure_reason: str = proto.Field(
        proto.STRING,
        number=2,
    )
    message: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
