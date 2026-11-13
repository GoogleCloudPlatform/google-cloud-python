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

import google.api.monitored_resource_pb2 as monitored_resource_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.monitoring.dashboard.v1",
    manifest={
        "IncidentList",
    },
)


class IncidentList(proto.Message):
    r"""A widget that displays a list of alerts

    Attributes:
        monitored_resources (MutableSequence[google.api.monitored_resource_pb2.MonitoredResource]):
            Optional. The monitored resource for which
            alerts are listed. The resource doesn't need to
            be fully specified. That is, you can specify the
            resource type but not the values of the resource
            labels. The resource type and labels are used
            for filtering.
        policy_names (MutableSequence[str]):
            Optional. A list of alert policy names to filter the alert
            list by. Don't include the project ID prefix in the policy
            name. For example, use ``alertPolicies/utilization``.
    """

    monitored_resources: MutableSequence[monitored_resource_pb2.MonitoredResource] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=monitored_resource_pb2.MonitoredResource,
        )
    )
    policy_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
