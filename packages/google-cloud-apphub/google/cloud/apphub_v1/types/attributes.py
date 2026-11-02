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
    package="google.cloud.apphub.v1",
    manifest={
        "Attributes",
        "Criticality",
        "Environment",
        "ContactInfo",
    },
)


class Attributes(proto.Message):
    r"""Consumer provided attributes.

    Attributes:
        criticality (google.cloud.apphub_v1.types.Criticality):
            Optional. User-defined criticality
            information.
        environment (google.cloud.apphub_v1.types.Environment):
            Optional. User-defined environment
            information.
        developer_owners (MutableSequence[google.cloud.apphub_v1.types.ContactInfo]):
            Optional. Developer team that owns
            development and coding.
        operator_owners (MutableSequence[google.cloud.apphub_v1.types.ContactInfo]):
            Optional. Operator team that ensures runtime
            and operations.
        business_owners (MutableSequence[google.cloud.apphub_v1.types.ContactInfo]):
            Optional. Business team that ensures user
            needs are met and value is delivered
    """

    criticality: "Criticality" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Criticality",
    )
    environment: "Environment" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Environment",
    )
    developer_owners: MutableSequence["ContactInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="ContactInfo",
    )
    operator_owners: MutableSequence["ContactInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="ContactInfo",
    )
    business_owners: MutableSequence["ContactInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=5,
        message="ContactInfo",
    )


class Criticality(proto.Message):
    r"""Criticality of the Application, Service, or Workload

    Attributes:
        type_ (google.cloud.apphub_v1.types.Criticality.Type):
            Required. Criticality Type.
    """

    class Type(proto.Enum):
        r"""Criticality Type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            MISSION_CRITICAL (1):
                Mission critical service, application or
                workload.
            HIGH (2):
                High impact.
            MEDIUM (3):
                Medium impact.
            LOW (4):
                Low impact.
        """

        TYPE_UNSPECIFIED = 0
        MISSION_CRITICAL = 1
        HIGH = 2
        MEDIUM = 3
        LOW = 4

    type_: Type = proto.Field(
        proto.ENUM,
        number=3,
        enum=Type,
    )


class Environment(proto.Message):
    r"""Environment of the Application, Service, or Workload

    Attributes:
        type_ (google.cloud.apphub_v1.types.Environment.Type):
            Required. Environment Type.
    """

    class Type(proto.Enum):
        r"""Environment Type.

        Values:
            TYPE_UNSPECIFIED (0):
                Unspecified type.
            PRODUCTION (1):
                Production environment.
            STAGING (2):
                Staging environment.
            TEST (3):
                Test environment.
            DEVELOPMENT (4):
                Development environment.
        """

        TYPE_UNSPECIFIED = 0
        PRODUCTION = 1
        STAGING = 2
        TEST = 3
        DEVELOPMENT = 4

    type_: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )


class ContactInfo(proto.Message):
    r"""Contact information of stakeholders.

    Attributes:
        display_name (str):
            Optional. Contact's name.
            Can have a maximum length of 63 characters.
        email (str):
            Required. Email address of the contacts.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    email: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
