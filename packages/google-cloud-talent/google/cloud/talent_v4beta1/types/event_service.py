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

from google.cloud.talent_v4beta1.types import event

__protobuf__ = proto.module(
    package="google.cloud.talent.v4beta1",
    manifest={
        "CreateClientEventRequest",
    },
)


class CreateClientEventRequest(proto.Message):
    r"""The report event request.

    Attributes:
        parent (str):
            Required. Resource name of the tenant under which the event
            is created.

            The format is "projects/{project_id}/tenants/{tenant_id}",
            for example, "projects/foo/tenant/bar". If tenant id is
            unspecified, a default tenant is created, for example,
            "projects/foo".
        client_event (google.cloud.talent_v4beta1.types.ClientEvent):
            Required. Events issued when end user
            interacts with customer's application that uses
            Cloud Talent Solution.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    client_event: event.ClientEvent = proto.Field(
        proto.MESSAGE,
        number=2,
        message=event.ClientEvent,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
