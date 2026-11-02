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

import google.protobuf.any_pb2 as any_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.channel.v1",
    manifest={
        "EduData",
        "CloudIdentityInfo",
        "Value",
        "AdminUser",
    },
)


class EduData(proto.Message):
    r"""Required Edu Attributes

    Attributes:
        institute_type (google.cloud.channel_v1.types.EduData.InstituteType):
            Designated institute type of customer.
        institute_size (google.cloud.channel_v1.types.EduData.InstituteSize):
            Size of the institute.
        website (str):
            Web address for the edu customer's
            institution.
    """

    class InstituteType(proto.Enum):
        r"""Enum to specify the institute type.

        Values:
            INSTITUTE_TYPE_UNSPECIFIED (0):
                Not used.
            K12 (1):
                Elementary/Secondary Schools & Districts
            UNIVERSITY (2):
                Higher Education Universities & Colleges
        """

        INSTITUTE_TYPE_UNSPECIFIED = 0
        K12 = 1
        UNIVERSITY = 2

    class InstituteSize(proto.Enum):
        r"""Number of students and staff the institute has.

        Values:
            INSTITUTE_SIZE_UNSPECIFIED (0):
                Not used.
            SIZE_1_100 (1):
                1 - 100
            SIZE_101_500 (2):
                101 - 500
            SIZE_501_1000 (3):
                501 - 1,000
            SIZE_1001_2000 (4):
                1,001 - 2,000
            SIZE_2001_5000 (5):
                2,001 - 5,000
            SIZE_5001_10000 (6):
                5,001 - 10,000
            SIZE_10001_OR_MORE (7):
                10,001 +
        """

        INSTITUTE_SIZE_UNSPECIFIED = 0
        SIZE_1_100 = 1
        SIZE_101_500 = 2
        SIZE_501_1000 = 3
        SIZE_1001_2000 = 4
        SIZE_2001_5000 = 5
        SIZE_5001_10000 = 6
        SIZE_10001_OR_MORE = 7

    institute_type: InstituteType = proto.Field(
        proto.ENUM,
        number=1,
        enum=InstituteType,
    )
    institute_size: InstituteSize = proto.Field(
        proto.ENUM,
        number=2,
        enum=InstituteSize,
    )
    website: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CloudIdentityInfo(proto.Message):
    r"""Cloud Identity information for the Cloud Channel Customer.

    Attributes:
        customer_type (google.cloud.channel_v1.types.CloudIdentityInfo.CustomerType):
            CustomerType indicates verification type
            needed for using services.
        primary_domain (str):
            Output only. The primary domain name.
        is_domain_verified (bool):
            Output only. Whether the domain is verified. This field is
            not returned for a Customer's cloud_identity_info resource.
            Partners can use the domains.get() method of the Workspace
            SDK's Directory API, or listen to the
            PRIMARY_DOMAIN_VERIFIED Pub/Sub event in to track domain
            verification of their resolve Workspace customers.
        alternate_email (str):
            The alternate email.
        phone_number (str):
            Phone number associated with the Cloud
            Identity.
        language_code (str):
            Language code.
        admin_console_uri (str):
            Output only. URI of Customer's Admin console
            dashboard.
        edu_data (google.cloud.channel_v1.types.EduData):
            Edu information about the customer.
    """

    class CustomerType(proto.Enum):
        r"""CustomerType of the customer

        Values:
            CUSTOMER_TYPE_UNSPECIFIED (0):
                Not used.
            DOMAIN (1):
                Domain-owning customer which needs domain
                verification to use services.
            TEAM (2):
                Team customer which needs email verification
                to use services.
        """

        CUSTOMER_TYPE_UNSPECIFIED = 0
        DOMAIN = 1
        TEAM = 2

    customer_type: CustomerType = proto.Field(
        proto.ENUM,
        number=1,
        enum=CustomerType,
    )
    primary_domain: str = proto.Field(
        proto.STRING,
        number=9,
    )
    is_domain_verified: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    alternate_email: str = proto.Field(
        proto.STRING,
        number=6,
    )
    phone_number: str = proto.Field(
        proto.STRING,
        number=7,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=8,
    )
    admin_console_uri: str = proto.Field(
        proto.STRING,
        number=10,
    )
    edu_data: "EduData" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="EduData",
    )


class Value(proto.Message):
    r"""Data type and value of a parameter.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        int64_value (int):
            Represents an int64 value.

            This field is a member of `oneof`_ ``kind``.
        string_value (str):
            Represents a string value.

            This field is a member of `oneof`_ ``kind``.
        double_value (float):
            Represents a double value.

            This field is a member of `oneof`_ ``kind``.
        proto_value (google.protobuf.any_pb2.Any):
            Represents an 'Any' proto value.

            This field is a member of `oneof`_ ``kind``.
        bool_value (bool):
            Represents a boolean value.

            This field is a member of `oneof`_ ``kind``.
    """

    int64_value: int = proto.Field(
        proto.INT64,
        number=1,
        oneof="kind",
    )
    string_value: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="kind",
    )
    double_value: float = proto.Field(
        proto.DOUBLE,
        number=3,
        oneof="kind",
    )
    proto_value: any_pb2.Any = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="kind",
        message=any_pb2.Any,
    )
    bool_value: bool = proto.Field(
        proto.BOOL,
        number=5,
        oneof="kind",
    )


class AdminUser(proto.Message):
    r"""Information needed to create an Admin User for Google
    Workspace.

    Attributes:
        email (str):
            Primary email of the admin user.
        given_name (str):
            Given name of the admin user.
        family_name (str):
            Family name of the admin user.
    """

    email: str = proto.Field(
        proto.STRING,
        number=1,
    )
    given_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    family_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
