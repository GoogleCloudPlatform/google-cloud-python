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
    package="google.cloud.websecurityscanner.v1beta",
    manifest={
        "CrawledUrl",
    },
)


class CrawledUrl(proto.Message):
    r"""A CrawledUrl resource represents a URL that was crawled
    during a ScanRun. Web Security Scanner Service crawls the web
    applications, following all links within the scope of sites, to
    find the URLs to test against.

    Attributes:
        http_method (str):
            The http method of the request that was used
            to visit the URL, in uppercase.
        url (str):
            The URL that was crawled.
        body (str):
            The body of the request that was used to
            visit the URL.
    """

    http_method: str = proto.Field(
        proto.STRING,
        number=1,
    )
    url: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
