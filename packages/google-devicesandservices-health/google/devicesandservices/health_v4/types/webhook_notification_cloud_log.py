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

import google.rpc.http_pb2 as http_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.devicesandservices.health.v4",
    manifest={
        "WebhookNotificationCloudLog",
    },
)


class WebhookNotificationCloudLog(proto.Message):
    r"""Log message for a webhook notification sent by the Google
    Health API to a subscriber's endpoint. Includes the HTTP
    response received from the endpoint.

    Attributes:
        http_response (google.rpc.http_pb2.HttpResponse):
            Required. Represents the HTTP response.
            This message includes the status code, reason
            phrase, headers, and body.
    """

    http_response: http_pb2.HttpResponse = proto.Field(
        proto.MESSAGE,
        number=1,
        message=http_pb2.HttpResponse,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
