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
    package="google.cloud.retail.v2beta",
    manifest={
        "AlertConfig",
    },
)


class AlertConfig(proto.Message):
    r"""Project level alert config.

    Attributes:
        name (str):
            Required. Immutable. The name of the AlertConfig singleton
            resource. Format: projects/\*/alertConfig
        alert_policies (MutableSequence[google.cloud.retail_v2beta.types.AlertConfig.AlertPolicy]):
            Alert policies for a customer. They must be unique by
            [AlertPolicy.alert_group]
    """

    class AlertPolicy(proto.Message):
        r"""Alert policy for a customer.

        Attributes:
            alert_group (str):
                The feature that provides alerting capability. Supported
                value:

                - ``search-data-quality`` for retail search customers.
                - ``conv-data-quality`` for retail conversation customers.
            enroll_status (google.cloud.retail_v2beta.types.AlertConfig.AlertPolicy.EnrollStatus):
                The enrollment status of a customer.
            recipients (MutableSequence[google.cloud.retail_v2beta.types.AlertConfig.AlertPolicy.Recipient]):
                Recipients for the alert policy.
                One alert policy should not exceed 20
                recipients.
        """

        class EnrollStatus(proto.Enum):
            r"""The enrollment status enum for alert policy.

            Values:
                ENROLL_STATUS_UNSPECIFIED (0):
                    Default value. Used for customers who have
                    not responded to the alert policy.
                ENROLLED (1):
                    Customer is enrolled in this policy.
                DECLINED (2):
                    Customer declined this policy.
            """

            ENROLL_STATUS_UNSPECIFIED = 0
            ENROLLED = 1
            DECLINED = 2

        class Recipient(proto.Message):
            r"""Recipient contact information.

            Attributes:
                email_address (str):
                    Email address of the recipient.
            """

            email_address: str = proto.Field(
                proto.STRING,
                number=1,
            )

        alert_group: str = proto.Field(
            proto.STRING,
            number=1,
        )
        enroll_status: "AlertConfig.AlertPolicy.EnrollStatus" = proto.Field(
            proto.ENUM,
            number=2,
            enum="AlertConfig.AlertPolicy.EnrollStatus",
        )
        recipients: MutableSequence["AlertConfig.AlertPolicy.Recipient"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="AlertConfig.AlertPolicy.Recipient",
            )
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    alert_policies: MutableSequence[AlertPolicy] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AlertPolicy,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
