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
    package="google.cloud.oracledatabase.v1",
    manifest={
        "DatabaseConnection",
        "CreateDatabaseConnectionRequest",
        "DeleteDatabaseConnectionRequest",
        "ListDatabaseConnectionsRequest",
        "ListDatabaseConnectionsResponse",
        "GetDatabaseConnectionRequest",
        "UpdateDatabaseConnectionRequest",
        "TestDatabaseConnectionRequest",
        "TestDatabaseConnectionResponse",
    },
)


class DatabaseConnection(proto.Message):
    r"""Represents DatabaseConnection resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        wallet_secret_version (str):
            Optional. Optional: The resource name of the GCP Secret
            Manager secret version containing base64 encoded content of
            the Oracle Wallet ZIP file required for mTLS/TLS
            connections. Format:
            projects/{project}/secrets/{secret_id}/versions/{version_id}
            The service's Per-Product Per-Project Service Account (P4SA)
            must have the 'secretmanager.secretAccessor' permission on
            this secret.

            This field is a member of `oneof`_ ``wallet_source``.
        odb_network (str):
            Optional. Immutable. For Oracle
            Database@Google cloud resources. Format:
            projects/{project}/locations/{location}/odbNetworks/{odbNetwork}

            This field is a member of `oneof`_ ``network_configuration``.
        name (str):
            Identifier. The resource name of the DatabaseConnection.
            Format:
            projects/{project}/locations/{location}/databaseConnections/{database_connection}
        display_name (str):
            Optional. Immutable. User-friendly display
            name for the connection.
        username (str):
            Optional. Immutable. The default database
            username to use for connections.
        password_secret_version (str):
            Optional. The resource name of the GCP Secret Manager secret
            version containing the password for the specified username.
            Format:
            projects/{project}/secrets/{secret_id}/versions/{version_id}
            The service's Per-Product Per-Project Service Account (P4SA)
            must have the 'secretmanager.secretAccessor' permission on
            this secret.
        connection_string (str):
            Required. Immutable. Oracle Easy Connect or TNS connection
            string. Example:
            "your-db-host.example.com:1521/YOUR_SERVICE_NAME".
        state (google.cloud.oracledatabase_v1.types.DatabaseConnection.State):
            Output only. The current state of the
            connection.
        labels (MutableMapping[str, str]):
            Optional. Optional: Labels as key-value pairs
            to organize the resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The create time of the resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The update time of the resource.
        lifecycle_details (str):
            Output only. Additional information about the
            current state of the connection.
    """

    class State(proto.Enum):
        r"""States of the DatabaseConnection resource.

        Values:
            STATE_UNSPECIFIED (0):
                Default unspecified value.
            CREATING (1):
                Indicates that the resource is in a creating
                state.
            ACTIVE (2):
                Indicates that the resource is in an active
                state.
            FAILED (3):
                Indicates that the resource is in a failed
                state.
            DELETING (4):
                Indicates that the resource is in a deleting
                state.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        FAILED = 3
        DELETING = 4

    wallet_secret_version: str = proto.Field(
        proto.STRING,
        number=6,
        oneof="wallet_source",
    )
    odb_network: str = proto.Field(
        proto.STRING,
        number=7,
        oneof="network_configuration",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    username: str = proto.Field(
        proto.STRING,
        number=3,
    )
    password_secret_version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    connection_string: str = proto.Field(
        proto.STRING,
        number=5,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=10,
        enum=State,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=13,
        message=timestamp_pb2.Timestamp,
    )
    lifecycle_details: str = proto.Field(
        proto.STRING,
        number=14,
    )


class CreateDatabaseConnectionRequest(proto.Message):
    r"""The request for ``DatabaseConnection.Create``.

    Attributes:
        parent (str):
            Required. The parent value for the
            DatabaseConnection in the following format:
            projects/{project}/locations/{location}.
        database_connection_id (str):
            Required. The ID of the DatabaseConnection to create. This
            value is restricted to
            (^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$) and must be a
            maximum of 63 characters in length. The value must start
            with a letter and end with a letter or a number.
        database_connection (google.cloud.oracledatabase_v1.types.DatabaseConnection):
            Required. Details of the DatabaseConnection
            instance to create.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    database_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    database_connection: "DatabaseConnection" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DatabaseConnection",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteDatabaseConnectionRequest(proto.Message):
    r"""The request for ``DatabaseConnection.Delete``.

    Attributes:
        name (str):
            Required. The name of the resource in the following format:
            projects/{project}/locations/{location}/databaseConnections/{database_connection}.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListDatabaseConnectionsRequest(proto.Message):
    r"""The request for ``DatabaseConnection.List``.

    Attributes:
        parent (str):
            Required. The parent value for the
            DatabaseConnection in the following format:
            projects/{project}/locations/{location}.
        page_size (int):
            Optional. The maximum number of items to
            return. If unspecified, at most 50
            DatabaseConnections will be returned. The
            maximum value is 1000; values above 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. An expression for filtering the
            results of the request.
        order_by (str):
            Optional. An expression for ordering the
            results of the request.
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


class ListDatabaseConnectionsResponse(proto.Message):
    r"""The response for ``DatabaseConnection.List``.

    Attributes:
        database_connections (MutableSequence[google.cloud.oracledatabase_v1.types.DatabaseConnection]):
            The list of DatabaseConnections.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unreachable locations when listing resources
            across all locations using wildcard location
            '-'.
    """

    @property
    def raw_page(self):
        return self

    database_connections: MutableSequence["DatabaseConnection"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DatabaseConnection",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetDatabaseConnectionRequest(proto.Message):
    r"""The request for ``DatabaseConnection.Get``.

    Attributes:
        name (str):
            Required. The name of the DatabaseConnection in the
            following format:
            projects/{project}/locations/{location}/databaseConnections/{database_connection}.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDatabaseConnectionRequest(proto.Message):
    r"""The request for ``DatabaseConnection.Update``.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. A mask specifying which fields in
            the DatabaseConnection should be updated. A
            field specified in the mask is overwritten. If a
            mask isn't provided then all the fields in the
            DatabaseConnection are overwritten.
        database_connection (google.cloud.oracledatabase_v1.types.DatabaseConnection):
            Required. The resource being updated.
        request_id (str):
            Optional. An optional ID to identify the
            request. This value is used to identify
            duplicate requests. If you make a request with
            the same request ID and the original request is
            still in progress or completed, the server
            ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    database_connection: "DatabaseConnection" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DatabaseConnection",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class TestDatabaseConnectionRequest(proto.Message):
    r"""Request message for ``DatabaseConnection.TestDatabaseConnection``.

    Attributes:
        name (str):
            Required. The name of the DatabaseConnection to test.
            Format:
            projects/{project}/locations/{location}/databaseConnections/{database_connection}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TestDatabaseConnectionResponse(proto.Message):
    r"""Response message for ``DatabaseConnection.TestDatabaseConnection``.

    Attributes:
        success (bool):
            Whether the test connection was successful.
        error_message (str):
            Error message if the test connection failed.
    """

    success: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
