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
    package="google.cloud.securitycenter.v2",
    manifest={
        "Source",
    },
)


class Source(proto.Message):
    r"""Security Command Center finding source. A finding source
    is an entity or a mechanism that can produce a finding. A source
    is like a container of findings that come from the same scanner,
    logger, monitor, and other tools.

    Attributes:
        name (str):
            The relative resource name of this source. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Example:
            "organizations/{organization_id}/sources/{source_id}".
        display_name (str):
            The source's display name.
            A source's display name must be unique amongst
            its siblings, for example, two sources with the
            same parent can't share the same display name.
            The display name must have a length between 1
            and 64 characters (inclusive).
        description (str):
            The description of the source (max of 1024
            characters). Example:

            "Web Security Scanner is a web security scanner
            for common vulnerabilities in App Engine
            applications. It can automatically scan and
            detect four common vulnerabilities, including
            cross-site-scripting (XSS), Flash injection,
            mixed content (HTTP in HTTPS), and outdated or
            insecure libraries.".
        canonical_name (str):
            The canonical name of the finding source. It's either
            "organizations/{organization_id}/sources/{source_id}",
            "folders/{folder_id}/sources/{source_id}", or
            "projects/{project_number}/sources/{source_id}", depending
            on the closest CRM ancestor of the resource associated with
            the finding.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    canonical_name: str = proto.Field(
        proto.STRING,
        number=4,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
