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

from google.ads.admanager_v1.types import conversion_event_enum

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "VideoTrackingUrl",
    },
)


class VideoTrackingUrl(proto.Message):
    r"""Represents a
    [ConversionEvent][google.ads.admanager.v1.ConversionEventEnum.ConversionEvent]
    to URL pair that will be pinged when the event happens.

    Attributes:
        conversion_event (google.ads.admanager_v1.types.ConversionEventEnum.ConversionEvent):
            Required. All possible tracking event types.
        url (str):
            Optional. A URL that should be pinged for the
            conversion event.
    """

    conversion_event: conversion_event_enum.ConversionEventEnum.ConversionEvent = (
        proto.Field(
            proto.ENUM,
            number=1,
            enum=conversion_event_enum.ConversionEventEnum.ConversionEvent,
        )
    )
    url: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
