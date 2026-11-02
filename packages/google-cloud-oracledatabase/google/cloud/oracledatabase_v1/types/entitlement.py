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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "Entitlement",
        "CloudAccountDetails",
    },
)


class Entitlement(proto.Message):
    r"""Details of the Entitlement resource.

    Attributes:
        name (str):
            Identifier. The name of the Entitlement
            resource with the format:
            projects/{project}/locations/{region}/entitlements/{entitlement}
        cloud_account_details (google.cloud.oracledatabase_v1.types.CloudAccountDetails):
            Details of the OCI Cloud Account.
        entitlement_id (str):
            Output only. Google Cloud Marketplace order
            ID (aka entitlement ID)
        state (google.cloud.oracledatabase_v1.types.Entitlement.State):
            Output only. Entitlement State.
    """

    class State(proto.Enum):
        r"""The various lifecycle states of the subscription.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            ACCOUNT_NOT_LINKED (1):
                Account not linked.
            ACCOUNT_NOT_ACTIVE (2):
                Account is linked but not active.
            ACTIVE (3):
                Entitlement and Account are active.
            ACCOUNT_SUSPENDED (4):
                Account is suspended.
            NOT_APPROVED_IN_PRIVATE_MARKETPLACE (5):
                Entitlement is not approved in private
                marketplace.
        """

        STATE_UNSPECIFIED = 0
        ACCOUNT_NOT_LINKED = 1
        ACCOUNT_NOT_ACTIVE = 2
        ACTIVE = 3
        ACCOUNT_SUSPENDED = 4
        NOT_APPROVED_IN_PRIVATE_MARKETPLACE = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_account_details: "CloudAccountDetails" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="CloudAccountDetails",
    )
    entitlement_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class CloudAccountDetails(proto.Message):
    r"""Details of the OCI Cloud Account.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_account (str):
            Output only. OCI account name.
        cloud_account_home_region (str):
            Output only. OCI account home region.
        link_existing_account_uri (str):
            Output only. URL to link an existing account.

            This field is a member of `oneof`_ ``_link_existing_account_uri``.
        account_creation_uri (str):
            Output only. URL to create a new account and
            link.

            This field is a member of `oneof`_ ``_account_creation_uri``.
    """

    cloud_account: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cloud_account_home_region: str = proto.Field(
        proto.STRING,
        number=2,
    )
    link_existing_account_uri: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    account_creation_uri: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
