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
    package="google.ads.datamanager.v1",
    manifest={
        "ItemParameter",
    },
)


class ItemParameter(proto.Message):
    r"""A bucket of any `event parameters related to an
    item <https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events>`__
    to be included within the event that were not already specified
    using other structured fields.

    Attributes:
        parameter_name (str):
            Required. The name of the parameter to use.
        value (str):
            Required. The string representation of the
            value of the parameter to set.
    """

    parameter_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
