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
    package="google.cloud.phishingprotection.v1beta1",
    manifest={
        "ReportPhishingRequest",
        "ReportPhishingResponse",
    },
)


class ReportPhishingRequest(proto.Message):
    r"""The ReportPhishing request message.

    Attributes:
        parent (str):
            Required. The name of the project for which the report will
            be created, in the format "projects/{project_number}".
        uri (str):
            Required. The URI that is being reported for
            phishing content to be analyzed.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uri: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ReportPhishingResponse(proto.Message):
    r"""The ReportPhishing (empty) response message."""


__all__ = tuple(sorted(__protobuf__.manifest))
