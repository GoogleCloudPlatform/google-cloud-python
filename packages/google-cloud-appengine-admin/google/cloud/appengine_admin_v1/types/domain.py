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
    package="google.appengine.v1",
    manifest={
        "AuthorizedDomain",
    },
)


class AuthorizedDomain(proto.Message):
    r"""A domain that a user has been authorized to administer. To authorize
    use of a domain, verify ownership via `Search
    Console <https://search.google.com/search-console/welcome>`__.

    Attributes:
        name (str):
            Full path to the ``AuthorizedDomain`` resource in the API.
            Example: ``apps/myapp/authorizedDomains/example.com``.

            @OutputOnly
        id (str):
            Fully qualified domain name of the domain authorized for
            use. Example: ``example.com``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
