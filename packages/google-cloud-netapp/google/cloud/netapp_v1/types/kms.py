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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.netapp.v1",
    manifest={
        "GetKmsConfigRequest",
        "ListKmsConfigsRequest",
        "ListKmsConfigsResponse",
        "CreateKmsConfigRequest",
        "UpdateKmsConfigRequest",
        "DeleteKmsConfigRequest",
        "EncryptVolumesRequest",
        "VerifyKmsConfigRequest",
        "VerifyKmsConfigResponse",
        "KmsConfig",
    },
)


class GetKmsConfigRequest(proto.Message):
    r"""GetKmsConfigRequest gets a KMS Config.

    Attributes:
        name (str):
            Required. Name of the KmsConfig
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListKmsConfigsRequest(proto.Message):
    r"""ListKmsConfigsRequest lists KMS Configs.

    Attributes:
        parent (str):
            Required. Parent value
        page_size (int):
            The maximum number of items to return.
        page_token (str):
            The next_page_token value to use if there are additional
            results to retrieve for this list request.
        order_by (str):
            Sort results. Supported values are "name",
            "name desc" or "" (unsorted).
        filter (str):
            List filter.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListKmsConfigsResponse(proto.Message):
    r"""ListKmsConfigsResponse is the response to a
    ListKmsConfigsRequest.

    Attributes:
        kms_configs (MutableSequence[google.cloud.netapp_v1.types.KmsConfig]):
            The list of KmsConfigs
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    kms_configs: MutableSequence["KmsConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="KmsConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class CreateKmsConfigRequest(proto.Message):
    r"""CreateKmsConfigRequest creates a KMS Config.

    Attributes:
        parent (str):
            Required. Value for parent.
        kms_config_id (str):
            Required. Id of the requesting KmsConfig.
            Must be unique within the parent resource. Must
            contain only letters, numbers and hyphen, with
            the first character a letter, the last a letter
            or a
            number, and a 63 character maximum.
        kms_config (google.cloud.netapp_v1.types.KmsConfig):
            Required. The required parameters to create a
            new KmsConfig.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    kms_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    kms_config: "KmsConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="KmsConfig",
    )


class UpdateKmsConfigRequest(proto.Message):
    r"""UpdateKmsConfigRequest updates a KMS Config.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the KmsConfig resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        kms_config (google.cloud.netapp_v1.types.KmsConfig):
            Required. The KmsConfig being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    kms_config: "KmsConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="KmsConfig",
    )


class DeleteKmsConfigRequest(proto.Message):
    r"""DeleteKmsConfigRequest deletes a KMS Config.

    Attributes:
        name (str):
            Required. Name of the KmsConfig.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class EncryptVolumesRequest(proto.Message):
    r"""EncryptVolumesRequest specifies the KMS config to encrypt
    existing volumes.

    Attributes:
        name (str):
            Required. Name of the KmsConfig.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VerifyKmsConfigRequest(proto.Message):
    r"""VerifyKmsConfigRequest specifies the KMS config to be
    validated.

    Attributes:
        name (str):
            Required. Name of the KMS Config to be
            verified.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class VerifyKmsConfigResponse(proto.Message):
    r"""VerifyKmsConfigResponse contains the information if the
    config is correctly and error message.

    Attributes:
        healthy (bool):
            Output only. If the customer key configured
            correctly to the encrypt volume.
        health_error (str):
            Output only. Error message if config is not
            healthy.
        instructions (str):
            Output only. Instructions for the customers
            to provide the access to the encryption key.
    """

    healthy: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    health_error: str = proto.Field(
        proto.STRING,
        number=2,
    )
    instructions: str = proto.Field(
        proto.STRING,
        number=3,
    )


class KmsConfig(proto.Message):
    r"""KmsConfig is the customer-managed encryption key(CMEK)
    configuration.

    Attributes:
        name (str):
            Identifier. Name of the ``KmsConfig``. Format:
            ``projects/{project}/locations/{location}/kmsConfigs/{kms_config}``
        crypto_key_name (str):
            Required. Customer-managed crypto key resource full name.
            Format:
            ``projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}``
        state (google.cloud.netapp_v1.types.KmsConfig.State):
            Output only. State of the KmsConfig.
        state_details (str):
            Output only. State details of the KmsConfig.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Create time of the KmsConfig.
        description (str):
            Description of the KmsConfig.
        labels (MutableMapping[str, str]):
            Labels as key value pairs
        instructions (str):
            Output only. Instructions to provide the
            access to the customer provided encryption key.
        service_account (str):
            Output only. The Service account which will
            have access to the customer provided encryption
            key.
    """

    class State(proto.Enum):
        r"""The KmsConfig States

        Values:
            STATE_UNSPECIFIED (0):
                Unspecified KmsConfig State
            READY (1):
                KmsConfig State is Ready
            CREATING (2):
                KmsConfig State is Creating
            DELETING (3):
                KmsConfig State is Deleting
            UPDATING (4):
                KmsConfig State is Updating
            IN_USE (5):
                KmsConfig State is In Use.
            ERROR (6):
                KmsConfig State is Error
            KEY_CHECK_PENDING (7):
                KmsConfig State is Pending to verify crypto
                key access.
            KEY_NOT_REACHABLE (8):
                KmsConfig State is Not accessbile by the SDE
                service account to the crypto key.
            DISABLING (9):
                KmsConfig State is Disabling.
            DISABLED (10):
                KmsConfig State is Disabled.
            MIGRATING (11):
                KmsConfig State is Migrating.
                The existing volumes are migrating from SMEK to
                CMEK.
        """

        STATE_UNSPECIFIED = 0
        READY = 1
        CREATING = 2
        DELETING = 3
        UPDATING = 4
        IN_USE = 5
        ERROR = 6
        KEY_CHECK_PENDING = 7
        KEY_NOT_REACHABLE = 8
        DISABLING = 9
        DISABLED = 10
        MIGRATING = 11

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    crypto_key_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=3,
        enum=State,
    )
    state_details: str = proto.Field(
        proto.STRING,
        number=4,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    instructions: str = proto.Field(
        proto.STRING,
        number=8,
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
