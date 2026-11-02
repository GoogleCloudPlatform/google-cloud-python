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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.ads.admanager_v1.types import site_enums

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "Site",
        "DisapprovalReason",
    },
)


class Site(proto.Message):
    r"""A Site represents a domain owned or represented by a network.
    For a parent network managing other networks as part of Multiple
    Customer Management "Manage Inventory" model, it could be the
    child's domain.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Identifier. The resource name of the ``Site``. Format:
            ``networks/{network_code}/sites/{site_id}``
        url (str):
            Required. The URL of the Site.

            This field is a member of `oneof`_ ``_url``.
        child_network_code (str):
            Optional. The network code of the child if
            the Site is being managed for an MCM child
            network, or null if owned by this network.

            This field is a member of `oneof`_ ``_child_network_code``.
        approval_status (google.ads.admanager_v1.types.SiteApprovalStatusEnum.SiteApprovalStatus):
            Output only. Status of the review performed
            on the Site by Google.

            This field is a member of `oneof`_ ``_approval_status``.
        approval_status_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The latest Site approval status
            change time.

            This field is a member of `oneof`_ ``_approval_status_update_time``.
        disapproval_reasons (MutableSequence[google.ads.admanager_v1.types.DisapprovalReason]):
            Output only. Provides reasons for
            disapproving the Site. It is null when the Site
            is not disapproved.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    url: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    child_network_code: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )
    approval_status: site_enums.SiteApprovalStatusEnum.SiteApprovalStatus = proto.Field(
        proto.ENUM,
        number=5,
        optional=True,
        enum=site_enums.SiteApprovalStatusEnum.SiteApprovalStatus,
    )
    approval_status_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        optional=True,
        message=timestamp_pb2.Timestamp,
    )
    disapproval_reasons: MutableSequence["DisapprovalReason"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="DisapprovalReason",
    )


class DisapprovalReason(proto.Message):
    r"""Represents the reason for which Google disapproved the Site.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        type_ (google.ads.admanager_v1.types.SiteDisapprovalReasonEnum.SiteDisapprovalReason):
            Output only. The type of policy violation
            found for the Site.

            This field is a member of `oneof`_ ``_type``.
        details (str):
            Output only. Additional details for the
            disapproval of the Site.

            This field is a member of `oneof`_ ``_details``.
    """

    type_: site_enums.SiteDisapprovalReasonEnum.SiteDisapprovalReason = proto.Field(
        proto.ENUM,
        number=1,
        optional=True,
        enum=site_enums.SiteDisapprovalReasonEnum.SiteDisapprovalReason,
    )
    details: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
