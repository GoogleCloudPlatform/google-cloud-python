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

__protobuf__ = proto.module(
    package="google.cloud.cloudcontrolspartner.v1",
    manifest={
        "AccessApprovalRequest",
        "ListAccessApprovalRequestsRequest",
        "ListAccessApprovalRequestsResponse",
        "AccessReason",
    },
)


class AccessApprovalRequest(proto.Message):
    r"""Details about the Access request.

    Attributes:
        name (str):
            Identifier. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}/accessApprovalRequests/{access_approval_request}``
        request_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which approval was requested.
        requested_reason (google.cloud.cloudcontrolspartner_v1.types.AccessReason):
            The justification for which approval is being
            requested.
        requested_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            The requested expiration for the approval. If
            the request is approved, access will be granted
            from the time of approval until the expiration
            time.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    requested_reason: "AccessReason" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AccessReason",
    )
    requested_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )


class ListAccessApprovalRequestsRequest(proto.Message):
    r"""Request for getting the access requests associated with a
    workload.

    Attributes:
        parent (str):
            Required. Parent resource Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``
        page_size (int):
            Optional. The maximum number of access
            requests to return. The service may return fewer
            than this value. If unspecified, at most 500
            access requests will be returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListAccessApprovalRequests`` call. Provide this to
            retrieve the subsequent page.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListAccessApprovalRequestsResponse(proto.Message):
    r"""Response message for list access requests.

    Attributes:
        access_approval_requests (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.AccessApprovalRequest]):
            List of access approval requests
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    access_approval_requests: MutableSequence["AccessApprovalRequest"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="AccessApprovalRequest",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class AccessReason(proto.Message):
    r"""Reason for the access.

    Attributes:
        type_ (google.cloud.cloudcontrolspartner_v1.types.AccessReason.Type):
            Type of access justification.
        detail (str):
            More detail about certain reason types. See
            comments for each type above.
    """

    class Type(proto.Enum):
        r"""Type of access justification.

        Values:
            TYPE_UNSPECIFIED (0):
                Default value for proto, shouldn't be used.
            CUSTOMER_INITIATED_SUPPORT (1):
                Customer made a request or raised an issue that required the
                principal to access customer data. ``detail`` is of the form
                ("#####" is the issue ID):

                - "Feedback Report: #####"
                - "Case Number: #####"
                - "Case ID: #####"
                - "E-PIN Reference: #####"
                - "Google-#####"
                - "T-#####".
            GOOGLE_INITIATED_SERVICE (2):
                The principal accessed customer data in order
                to diagnose or resolve a suspected issue in
                services. Often this access is used to confirm
                that customers are not affected by a suspected
                service issue or to remediate a reversible
                system issue.
            GOOGLE_INITIATED_REVIEW (3):
                Google initiated service for security, fraud,
                abuse, or compliance purposes.
            THIRD_PARTY_DATA_REQUEST (4):
                The principal was compelled to access
                customer data in order to respond to a legal
                third party data request or process, including
                legal processes from customers themselves.
            GOOGLE_RESPONSE_TO_PRODUCTION_ALERT (5):
                The principal accessed customer data in order
                to diagnose or resolve a suspected issue in
                services or a known outage.
            CLOUD_INITIATED_ACCESS (6):
                Similar to 'GOOGLE_INITIATED_SERVICE' or
                'GOOGLE_INITIATED_REVIEW', but with universe agnostic
                naming. The principal accessed customer data in order to
                diagnose or resolve a suspected issue in services or a known
                outage, or for security, fraud, abuse, or compliance review
                purposes.
        """

        TYPE_UNSPECIFIED = 0
        CUSTOMER_INITIATED_SUPPORT = 1
        GOOGLE_INITIATED_SERVICE = 2
        GOOGLE_INITIATED_REVIEW = 3
        THIRD_PARTY_DATA_REQUEST = 4
        GOOGLE_RESPONSE_TO_PRODUCTION_ALERT = 5
        CLOUD_INITIATED_ACCESS = 6

    type_: Type = proto.Field(
        proto.ENUM,
        number=1,
        enum=Type,
    )
    detail: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
