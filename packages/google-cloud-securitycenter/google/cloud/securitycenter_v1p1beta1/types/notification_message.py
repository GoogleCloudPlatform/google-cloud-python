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

from google.cloud.securitycenter_v1p1beta1.types import finding as gcs_finding
from google.cloud.securitycenter_v1p1beta1.types import resource as gcs_resource

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1p1beta1",
    manifest={
        "NotificationMessage",
    },
)


class NotificationMessage(proto.Message):
    r"""Security Command Center's Notification

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        notification_config_name (str):
            Name of the notification config that
            generated current notification.
        finding (google.cloud.securitycenter_v1p1beta1.types.Finding):
            If it's a Finding based notification config,
            this field will be populated.

            This field is a member of `oneof`_ ``event``.
        resource (google.cloud.securitycenter_v1p1beta1.types.Resource):
            The Cloud resource tied to the notification.
    """

    notification_config_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    finding: gcs_finding.Finding = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="event",
        message=gcs_finding.Finding,
    )
    resource: gcs_resource.Resource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcs_resource.Resource,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
