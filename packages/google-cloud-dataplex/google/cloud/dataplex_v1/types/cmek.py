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
    package="google.cloud.dataplex.v1",
    manifest={
        "EncryptionConfig",
        "CreateEncryptionConfigRequest",
        "GetEncryptionConfigRequest",
        "UpdateEncryptionConfigRequest",
        "DeleteEncryptionConfigRequest",
        "ListEncryptionConfigsRequest",
        "ListEncryptionConfigsResponse",
    },
)


class EncryptionConfig(proto.Message):
    r"""A Resource designed to manage encryption configurations for
    customers to support Customer Managed Encryption Keys (CMEK).

    Attributes:
        name (str):
            Identifier. The resource name of the EncryptionConfig.
            Format:
            organizations/{organization}/locations/{location}/encryptionConfigs/{encryption_config}
            Global location is not supported.
        key (str):
            Optional. If a key is chosen, it means that
            the customer is using CMEK. If a key is not
            chosen, it means that the customer is using
            Google managed encryption.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Encryption
            configuration was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the Encryption
            configuration was last updated.
        encryption_state (google.cloud.dataplex_v1.types.EncryptionConfig.EncryptionState):
            Output only. The state of encryption of the
            databases.
        etag (str):
            Etag of the EncryptionConfig. This is a
            strong etag.
        failure_details (google.cloud.dataplex_v1.types.EncryptionConfig.FailureDetails):
            Output only. Details of the failure if
            anything related to Cmek db fails.
        enable_metastore_encryption (bool):
            Optional. Represent the state of CMEK opt-in
            for metastore.
    """

    class EncryptionState(proto.Enum):
        r"""State of encryption of the databases when EncryptionConfig is
        created or updated.

        Values:
            ENCRYPTION_STATE_UNSPECIFIED (0):
                State is not specified.
            ENCRYPTING (1):
                The encryption state of the database when the
                EncryptionConfig is created or updated. If the
                encryption fails, it is retried indefinitely and
                the state is shown as ENCRYPTING.
            COMPLETED (2):
                The encryption of data has completed
                successfully.
            FAILED (3):
                The encryption of data has failed.
                The state is set to FAILED when the encryption
                fails due to reasons like permission issues,
                invalid key etc.
        """

        ENCRYPTION_STATE_UNSPECIFIED = 0
        ENCRYPTING = 1
        COMPLETED = 2
        FAILED = 3

    class FailureDetails(proto.Message):
        r"""Details of the failure if anything related to Cmek db fails.

        Attributes:
            error_code (google.cloud.dataplex_v1.types.EncryptionConfig.FailureDetails.ErrorCode):
                Output only. The error code for the failure.
            error_message (str):
                Output only. The error message will be shown to the user.
                Set only if the error code is REQUIRE_USER_ACTION.
        """

        class ErrorCode(proto.Enum):
            r"""Error code for the failure if anything related to Cmek db
            fails.

            Values:
                UNKNOWN (0):
                    The error code is not specified
                INTERNAL_ERROR (1):
                    Error because of internal server error, will
                    be retried automatically.
                REQUIRE_USER_ACTION (2):
                    User action is required to resolve the error.
            """

            UNKNOWN = 0
            INTERNAL_ERROR = 1
            REQUIRE_USER_ACTION = 2

        error_code: "EncryptionConfig.FailureDetails.ErrorCode" = proto.Field(
            proto.ENUM,
            number=1,
            enum="EncryptionConfig.FailureDetails.ErrorCode",
        )
        error_message: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    key: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    encryption_state: EncryptionState = proto.Field(
        proto.ENUM,
        number=5,
        enum=EncryptionState,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    failure_details: FailureDetails = proto.Field(
        proto.MESSAGE,
        number=7,
        message=FailureDetails,
    )
    enable_metastore_encryption: bool = proto.Field(
        proto.BOOL,
        number=8,
    )


class CreateEncryptionConfigRequest(proto.Message):
    r"""Create EncryptionConfig Request

    Attributes:
        parent (str):
            Required. The location at which the
            EncryptionConfig is to be created.
        encryption_config_id (str):
            Required. The ID of the
            [EncryptionConfig][google.cloud.dataplex.v1.EncryptionConfig]
            to create. Currently, only a value of "default" is
            supported.
        encryption_config (google.cloud.dataplex_v1.types.EncryptionConfig):
            Required. The EncryptionConfig to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    encryption_config_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    encryption_config: "EncryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="EncryptionConfig",
    )


class GetEncryptionConfigRequest(proto.Message):
    r"""Get EncryptionConfig Request

    Attributes:
        name (str):
            Required. The name of the EncryptionConfig to
            fetch.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateEncryptionConfigRequest(proto.Message):
    r"""Update EncryptionConfig Request

    Attributes:
        encryption_config (google.cloud.dataplex_v1.types.EncryptionConfig):
            Required. The EncryptionConfig to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Mask of fields to update.
            The service treats an omitted field mask as an
            implied field mask equivalent to all fields that
            are populated (have a non-empty value).
    """

    encryption_config: "EncryptionConfig" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="EncryptionConfig",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteEncryptionConfigRequest(proto.Message):
    r"""Delete EncryptionConfig Request

    Attributes:
        name (str):
            Required. The name of the EncryptionConfig to
            delete.
        etag (str):
            Optional. Etag of the EncryptionConfig. This
            is a strong etag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListEncryptionConfigsRequest(proto.Message):
    r"""List EncryptionConfigs Request

    Attributes:
        parent (str):
            Required. The location for which the
            EncryptionConfig is to be listed.
        page_size (int):
            Optional. Maximum number of EncryptionConfigs
            to return. The service may return fewer than
            this value. If unspecified, at most 10
            EncryptionConfigs will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListEncryptionConfigs`` call. Provide this to retrieve the
            subsequent page. When paginating, the parameters - filter
            and order_by provided to ``ListEncryptionConfigs`` must
            match the call that provided the page token.
        filter (str):
            Optional. Filter the EncryptionConfigs to be returned. Using
            bare literals: (These values will be matched anywhere it may
            appear in the object's field values)

            - filter=some_value Using fields: (These values will be
              matched only in the specified field)
            - filter=some_field=some_value Supported fields:
            - name, key, create_time, update_time, encryption_state
              Example:
            - filter=name=organizations/123/locations/us-central1/encryptionConfigs/test-config
              conjunctions: (AND, OR, NOT)
            - filter=name=organizations/123/locations/us-central1/encryptionConfigs/test-config
              AND mode=CMEK logical operators: (>, <, >=, <=, !=, =, :),
            - filter=create_time>2024-05-01T00:00:00.000Z
        order_by (str):
            Optional. Order by fields for the result.
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


class ListEncryptionConfigsResponse(proto.Message):
    r"""List EncryptionConfigs Response

    Attributes:
        encryption_configs (MutableSequence[google.cloud.dataplex_v1.types.EncryptionConfig]):
            The list of EncryptionConfigs under the given
            parent location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    encryption_configs: MutableSequence["EncryptionConfig"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="EncryptionConfig",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
