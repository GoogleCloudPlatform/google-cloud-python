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
    package="google.cloud.channel.v1",
    manifest={
        "OperationMetadata",
    },
)


class OperationMetadata(proto.Message):
    r"""Provides contextual information about a
    [google.longrunning.Operation][google.longrunning.Operation].

    Attributes:
        operation_type (google.cloud.channel_v1.types.OperationMetadata.OperationType):
            The RPC that initiated this Long Running
            Operation.
    """

    class OperationType(proto.Enum):
        r"""RPCs that return a Long Running Operation.

        Values:
            OPERATION_TYPE_UNSPECIFIED (0):
                Not used.
            CREATE_ENTITLEMENT (1):
                Long Running Operation was triggered by
                CreateEntitlement.
            CHANGE_RENEWAL_SETTINGS (3):
                Long Running Operation was triggered by
                ChangeRenewalSettings.
            START_PAID_SERVICE (5):
                Long Running Operation was triggered by
                StartPaidService.
            ACTIVATE_ENTITLEMENT (7):
                Long Running Operation was triggered by
                ActivateEntitlement.
            SUSPEND_ENTITLEMENT (8):
                Long Running Operation was triggered by
                SuspendEntitlement.
            CANCEL_ENTITLEMENT (9):
                Long Running Operation was triggered by
                CancelEntitlement.
            TRANSFER_ENTITLEMENTS (10):
                Long Running Operation was triggered by
                TransferEntitlements.
            TRANSFER_ENTITLEMENTS_TO_GOOGLE (11):
                Long Running Operation was triggered by
                TransferEntitlementsToGoogle.
            CHANGE_OFFER (14):
                Long Running Operation was triggered by
                ChangeOffer.
            CHANGE_PARAMETERS (15):
                Long Running Operation was triggered by
                ChangeParameters.
            PROVISION_CLOUD_IDENTITY (16):
                Long Running Operation was triggered by
                ProvisionCloudIdentity.
        """

        OPERATION_TYPE_UNSPECIFIED = 0
        CREATE_ENTITLEMENT = 1
        CHANGE_RENEWAL_SETTINGS = 3
        START_PAID_SERVICE = 5
        ACTIVATE_ENTITLEMENT = 7
        SUSPEND_ENTITLEMENT = 8
        CANCEL_ENTITLEMENT = 9
        TRANSFER_ENTITLEMENTS = 10
        TRANSFER_ENTITLEMENTS_TO_GOOGLE = 11
        CHANGE_OFFER = 14
        CHANGE_PARAMETERS = 15
        PROVISION_CLOUD_IDENTITY = 16

    operation_type: OperationType = proto.Field(
        proto.ENUM,
        number=1,
        enum=OperationType,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
