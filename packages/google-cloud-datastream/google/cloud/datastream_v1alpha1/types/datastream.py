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

from google.cloud.datastream_v1alpha1.types import datastream_resources

__protobuf__ = proto.module(
    package="google.cloud.datastream.v1alpha1",
    manifest={
        "DiscoverConnectionProfileRequest",
        "DiscoverConnectionProfileResponse",
        "FetchStaticIpsRequest",
        "FetchStaticIpsResponse",
        "FetchErrorsRequest",
        "FetchErrorsResponse",
        "ListConnectionProfilesRequest",
        "ListConnectionProfilesResponse",
        "GetConnectionProfileRequest",
        "CreateConnectionProfileRequest",
        "UpdateConnectionProfileRequest",
        "DeleteConnectionProfileRequest",
        "ListStreamsRequest",
        "ListStreamsResponse",
        "GetStreamRequest",
        "CreateStreamRequest",
        "UpdateStreamRequest",
        "DeleteStreamRequest",
        "OperationMetadata",
        "CreatePrivateConnectionRequest",
        "ListPrivateConnectionsRequest",
        "ListPrivateConnectionsResponse",
        "DeletePrivateConnectionRequest",
        "GetPrivateConnectionRequest",
        "CreateRouteRequest",
        "ListRoutesRequest",
        "ListRoutesResponse",
        "DeleteRouteRequest",
        "GetRouteRequest",
    },
)


class DiscoverConnectionProfileRequest(proto.Message):
    r"""Request message for 'discover' ConnectionProfile request.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. The parent resource of the ConnectionProfile type.
            Must be in the format ``projects/*/locations/*``.
        connection_profile (google.cloud.datastream_v1alpha1.types.ConnectionProfile):
            An ad-hoc ConnectionProfile configuration.

            This field is a member of `oneof`_ ``target``.
        connection_profile_name (str):
            A reference to an existing ConnectionProfile.

            This field is a member of `oneof`_ ``target``.
        recursive (bool):
            Whether to retrieve the full hierarchy of
            data objects (TRUE) or only the current level
            (FALSE).

            This field is a member of `oneof`_ ``depth``.
        recursion_depth (int):
            The number of hierarchy levels below the
            current level to be retrieved.

            This field is a member of `oneof`_ ``depth``.
        oracle_rdbms (google.cloud.datastream_v1alpha1.types.OracleRdbms):
            Oracle RDBMS to enrich with child data
            objects and metadata.

            This field is a member of `oneof`_ ``data_object``.
        mysql_rdbms (google.cloud.datastream_v1alpha1.types.MysqlRdbms):
            MySQL RDBMS to enrich with child data objects
            and metadata.

            This field is a member of `oneof`_ ``data_object``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_profile: datastream_resources.ConnectionProfile = proto.Field(
        proto.MESSAGE,
        number=200,
        oneof="target",
        message=datastream_resources.ConnectionProfile,
    )
    connection_profile_name: str = proto.Field(
        proto.STRING,
        number=201,
        oneof="target",
    )
    recursive: bool = proto.Field(
        proto.BOOL,
        number=3,
        oneof="depth",
    )
    recursion_depth: int = proto.Field(
        proto.INT32,
        number=4,
        oneof="depth",
    )
    oracle_rdbms: datastream_resources.OracleRdbms = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="data_object",
        message=datastream_resources.OracleRdbms,
    )
    mysql_rdbms: datastream_resources.MysqlRdbms = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="data_object",
        message=datastream_resources.MysqlRdbms,
    )


class DiscoverConnectionProfileResponse(proto.Message):
    r"""

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        oracle_rdbms (google.cloud.datastream_v1alpha1.types.OracleRdbms):
            Enriched Oracle RDBMS object.

            This field is a member of `oneof`_ ``data_object``.
        mysql_rdbms (google.cloud.datastream_v1alpha1.types.MysqlRdbms):
            Enriched MySQL RDBMS object.

            This field is a member of `oneof`_ ``data_object``.
    """

    oracle_rdbms: datastream_resources.OracleRdbms = proto.Field(
        proto.MESSAGE,
        number=100,
        oneof="data_object",
        message=datastream_resources.OracleRdbms,
    )
    mysql_rdbms: datastream_resources.MysqlRdbms = proto.Field(
        proto.MESSAGE,
        number=101,
        oneof="data_object",
        message=datastream_resources.MysqlRdbms,
    )


class FetchStaticIpsRequest(proto.Message):
    r"""Request message for 'FetchStaticIps' request.

    Attributes:
        name (str):
            Required. The name resource of the Response type. Must be in
            the format ``projects/*/locations/*``.
        page_size (int):
            Maximum number of Ips to return, will likely
            not be specified.
        page_token (str):
            A page token, received from a previous ``ListStaticIps``
            call. will likely not be specified.
    """

    name: str = proto.Field(
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


class FetchStaticIpsResponse(proto.Message):
    r"""Response message for a 'FetchStaticIps' response.

    Attributes:
        static_ips (MutableSequence[str]):
            list of static ips by account
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    static_ips: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchErrorsRequest(proto.Message):
    r"""Request message for 'FetchErrors' request.

    Attributes:
        stream (str):
            Name of the Stream resource for which to
            fetch any errors.
    """

    stream: str = proto.Field(
        proto.STRING,
        number=1,
    )


class FetchErrorsResponse(proto.Message):
    r"""Response message for a 'FetchErrors' response.

    Attributes:
        errors (MutableSequence[google.cloud.datastream_v1alpha1.types.Error]):
            The list of errors on the Stream.
    """

    errors: MutableSequence[datastream_resources.Error] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=datastream_resources.Error,
    )


class ListConnectionProfilesRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of connection profiles.
        page_size (int):
            Maximum number of connection profiles to
            return. If unspecified, at most 50 connection
            profiles will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Page token received from a previous
            ``ListConnectionProfiles`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListConnectionProfiles`` must match the call that provided
            the page token.
        filter (str):
            Filter request.
        order_by (str):
            Order by fields for the result.
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


class ListConnectionProfilesResponse(proto.Message):
    r"""

    Attributes:
        connection_profiles (MutableSequence[google.cloud.datastream_v1alpha1.types.ConnectionProfile]):
            List of connection profiles.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    connection_profiles: MutableSequence[datastream_resources.ConnectionProfile] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=datastream_resources.ConnectionProfile,
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


class GetConnectionProfileRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the connection profile
            resource to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConnectionProfileRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of ConnectionProfiles.
        connection_profile_id (str):
            Required. The connection profile identifier.
        connection_profile (google.cloud.datastream_v1alpha1.types.ConnectionProfile):
            Required. The connection profile resource to
            create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connection_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connection_profile: datastream_resources.ConnectionProfile = proto.Field(
        proto.MESSAGE,
        number=3,
        message=datastream_resources.ConnectionProfile,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateConnectionProfileRequest(proto.Message):
    r"""

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ConnectionProfile resource by the update.
            The fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        connection_profile (google.cloud.datastream_v1alpha1.types.ConnectionProfile):
            Required. The ConnectionProfile to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    connection_profile: datastream_resources.ConnectionProfile = proto.Field(
        proto.MESSAGE,
        number=2,
        message=datastream_resources.ConnectionProfile,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteConnectionProfileRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the connection profile
            resource to delete.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

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


class ListStreamsRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of streams.
        page_size (int):
            Maximum number of streams to return.
            If unspecified, at most 50 streams will  be
            returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
        page_token (str):
            Page token received from a previous ``ListStreams`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListStreams`` must match the call that provided the page
            token.
        filter (str):
            Filter request.
        order_by (str):
            Order by fields for the result.
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


class ListStreamsResponse(proto.Message):
    r"""

    Attributes:
        streams (MutableSequence[google.cloud.datastream_v1alpha1.types.Stream]):
            List of streams
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    streams: MutableSequence[datastream_resources.Stream] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=datastream_resources.Stream,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetStreamRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the stream resource to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateStreamRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of streams.
        stream_id (str):
            Required. The stream identifier.
        stream (google.cloud.datastream_v1alpha1.types.Stream):
            Required. The stream resource to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. Only validate the stream, but do
            not create any resources. The default is false.
        force (bool):
            Optional. Create the stream without
            validating it.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    stream_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    stream: datastream_resources.Stream = proto.Field(
        proto.MESSAGE,
        number=3,
        message=datastream_resources.Stream,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class UpdateStreamRequest(proto.Message):
    r"""

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the stream resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields will be overwritten.
        stream (google.cloud.datastream_v1alpha1.types.Stream):
            Required. The stream resource to update.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        validate_only (bool):
            Optional. Only validate the stream with the
            changes, without actually updating it. The
            default is false.
        force (bool):
            Optional. Execute the update without
            validating it.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    stream: datastream_resources.Stream = proto.Field(
        proto.MESSAGE,
        number=2,
        message=datastream_resources.Stream,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class DeleteStreamRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the stream resource to
            delete.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

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


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
        validation_result (google.cloud.datastream_v1alpha1.types.ValidationResult):
            Output only. Results of executed validations
            if there are any.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )
    validation_result: datastream_resources.ValidationResult = proto.Field(
        proto.MESSAGE,
        number=8,
        message=datastream_resources.ValidationResult,
    )


class CreatePrivateConnectionRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of PrivateConnections.
        private_connection_id (str):
            Required. The private connectivity
            identifier.
        private_connection (google.cloud.datastream_v1alpha1.types.PrivateConnection):
            Required. The Private Connectivity resource
            to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    private_connection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    private_connection: datastream_resources.PrivateConnection = proto.Field(
        proto.MESSAGE,
        number=3,
        message=datastream_resources.PrivateConnection,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListPrivateConnectionsRequest(proto.Message):
    r"""

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of private connectivity configurations.
        page_size (int):
            Maximum number of private connectivity
            configurations to return. If unspecified, at
            most 50 private connectivity configurations that
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Page token received from a previous
            ``ListPrivateConnections`` call. Provide this to retrieve
            the subsequent page.

            When paginating, all other parameters provided to
            ``ListPrivateConnections`` must match the call that provided
            the page token.
        filter (str):
            Filter request.
        order_by (str):
            Order by fields for the result.
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


class ListPrivateConnectionsResponse(proto.Message):
    r"""

    Attributes:
        private_connections (MutableSequence[google.cloud.datastream_v1alpha1.types.PrivateConnection]):
            List of private connectivity configurations.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    private_connections: MutableSequence[datastream_resources.PrivateConnection] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=datastream_resources.PrivateConnection,
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


class DeletePrivateConnectionRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the private
            connectivity configuration to delete.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any child routes
            that belong to this PrivateConnection will also
            be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetPrivateConnectionRequest(proto.Message):
    r"""

    Attributes:
        name (str):
            Required. The name of the  private
            connectivity configuration to get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateRouteRequest(proto.Message):
    r"""route creation request

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of Routes.
        route_id (str):
            Required. The Route identifier.
        route (google.cloud.datastream_v1alpha1.types.Route):
            Required. The Route resource to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    route_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    route: datastream_resources.Route = proto.Field(
        proto.MESSAGE,
        number=3,
        message=datastream_resources.Route,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListRoutesRequest(proto.Message):
    r"""route list request

    Attributes:
        parent (str):
            Required. The parent that owns the collection
            of Routess.
        page_size (int):
            Maximum number of Routes to return. The
            service may return fewer than this value. If
            unspecified, at most 50 Routes will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Page token received from a previous ``ListRoutes`` call.
            Provide this to retrieve the subsequent page.

            When paginating, all other parameters provided to
            ``ListRoutes`` must match the call that provided the page
            token.
        filter (str):
            Filter request.
        order_by (str):
            Order by fields for the result.
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


class ListRoutesResponse(proto.Message):
    r"""route list response

    Attributes:
        routes (MutableSequence[google.cloud.datastream_v1alpha1.types.Route]):
            List of Routes.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    routes: MutableSequence[datastream_resources.Route] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=datastream_resources.Route,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteRouteRequest(proto.Message):
    r"""route deletion request

    Attributes:
        name (str):
            Required. The name of the Route resource to
            delete.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

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


class GetRouteRequest(proto.Message):
    r"""route get request

    Attributes:
        name (str):
            Required. The name of the Route resource to
            get.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
