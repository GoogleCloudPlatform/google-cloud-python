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
    package="google.cloud.networksecurity.v1",
    manifest={
        "UrlFilteringProfile",
        "UrlFilter",
    },
)


class UrlFilteringProfile(proto.Message):
    r"""UrlFilteringProfile defines filters based on URL.

    Attributes:
        url_filters (MutableSequence[google.cloud.network_security_v1.types.UrlFilter]):
            Optional. The list of filtering configs in
            which each config defines an action to take for
            some URL match.
    """

    url_filters: MutableSequence["UrlFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="UrlFilter",
    )


class UrlFilter(proto.Message):
    r"""A URL filter defines an action to take for some URL match.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        filtering_action (google.cloud.network_security_v1.types.UrlFilter.UrlFilteringAction):
            Required. The action taken when this filter
            is applied.
        urls (MutableSequence[str]):
            Required. The list of strings that a URL must
            match with for this filter to be applied.
        priority (int):
            Required. The priority of this filter within
            the URL Filtering Profile. Lower integers
            indicate higher priorities. The priority of a
            filter must be unique within a URL Filtering
            Profile.

            This field is a member of `oneof`_ ``_priority``.
    """

    class UrlFilteringAction(proto.Enum):
        r"""Action to be taken when a URL matches a filter.

        Values:
            URL_FILTERING_ACTION_UNSPECIFIED (0):
                Filtering action not specified.
            ALLOW (1):
                The connection matching this filter will be
                allowed to transmit.
            DENY (2):
                The connection matching this filter will be
                dropped.
        """

        URL_FILTERING_ACTION_UNSPECIFIED = 0
        ALLOW = 1
        DENY = 2

    filtering_action: UrlFilteringAction = proto.Field(
        proto.ENUM,
        number=1,
        enum=UrlFilteringAction,
    )
    urls: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=3,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
