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
    package="google.ads.admanager.v1",
    manifest={
        "CdnSecurityPolicyTypeEnum",
    },
)


class CdnSecurityPolicyTypeEnum(proto.Message):
    r"""Wrapper message for
    [CdnSecurityPolicyType][google.ads.admanager.v1.CdnSecurityPolicyTypeEnum.CdnSecurityPolicyType]

    """

    class CdnSecurityPolicyType(proto.Enum):
        r"""Indicates the type of security policy associated with access
        to a CDN. Different security policies require different
        parameters in a SecurityPolicy.

        Values:
            CDN_SECURITY_POLICY_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            AKAMAI (1):
                Security policy for accessing content on the
                Akamai CDN.
            CLOUD_MEDIA (2):
                Security policy for access content on Google
                Cloud Media CDN.
            NONE (3):
                Indicates that no authentication is
                necessary.
        """

        CDN_SECURITY_POLICY_TYPE_UNSPECIFIED = 0
        AKAMAI = 1
        CLOUD_MEDIA = 2
        NONE = 3


__all__ = tuple(sorted(__protobuf__.manifest))
