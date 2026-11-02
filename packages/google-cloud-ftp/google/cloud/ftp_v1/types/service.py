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
    package="google.cloud.ftp.v1",
    manifest={
        "ServerView",
        "UserView",
        "ExternalServerConfig",
        "InternalServerConfig",
        "ServerCredential",
        "Server",
        "ListServersRequest",
        "ListServersResponse",
        "GetServerRequest",
        "CreateServerRequest",
        "UpdateServerRequest",
        "DeleteServerRequest",
        "StorageDirectoryMapping",
        "User",
        "ListUsersRequest",
        "ListUsersResponse",
        "GetUserRequest",
        "CreateUserRequest",
        "UpdateUserRequest",
        "DeleteUserRequest",
        "StartServerRequest",
        "StopServerRequest",
        "UserCredential",
        "OperationMetadata",
    },
)


class ServerView(proto.Enum):
    r"""View for Server resource.

    Values:
        SERVER_VIEW_UNSPECIFIED (0):
            Default value. Equivalent to SERVER_VIEW_BASIC.
        SERVER_VIEW_BASIC (1):
            Basic view. Excludes heavy configurations (internal_config,
            external_config, google_managed_server_credential).
        SERVER_VIEW_FULL (2):
            Full view. Includes all fields.
    """

    SERVER_VIEW_UNSPECIFIED = 0
    SERVER_VIEW_BASIC = 1
    SERVER_VIEW_FULL = 2


class UserView(proto.Enum):
    r"""View for User resource.

    Values:
        USER_VIEW_UNSPECIFIED (0):
            Default value. Equivalent to USER_VIEW_BASIC.
        USER_VIEW_BASIC (1):
            Basic view. Excludes heavy configurations (user_credentials,
            storage_directory_mappings).
        USER_VIEW_FULL (2):
            Full view. Includes all fields.
    """

    USER_VIEW_UNSPECIFIED = 0
    USER_VIEW_BASIC = 1
    USER_VIEW_FULL = 2


class ExternalServerConfig(proto.Message):
    r"""Configuration for external server.

    Attributes:
        ip_address (str):
            Output only. IP address of the LB via which
            clients will connect.
        allowed_cidr_blocks (MutableSequence[str]):
            Optional. List of CIDR blocks that are
            allowed to access the Server. A CIDR range
            consists of an IP Address and a prefix length to
            construct the subnet mask. By default, the
            prefix length is 32 (i.e. matches a single IP
            address). For now, only IPV4 addresses are
            supported. Examples: "203.0.113.0/24" -
            matches with the IP addresses in the range
            203.0.113.0 - 203.0.113.255. "0.0.0.0/0" -
            matches against any IP address. This field must
            contain at least one entry if the access type is
            EXTERNAL. The number of allowed CIDR blocks
            cannot exceed 500. Example: 192.168.0.0/16
    """

    ip_address: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allowed_cidr_blocks: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class InternalServerConfig(proto.Message):
    r"""Configuration for private server accessible via PSC.

    Attributes:
        service_attachment (str):
            Output only. The resource name of the service attachment.
            Format:
            ``projects/{project}/regions/{region}/serviceAttachments/{service_attachment}``
        consumer_accept_list (MutableSequence[google.cloud.ftp_v1.types.InternalServerConfig.AllowedConsumer]):
            Required. A list of projects that are
            permitted to connect. At least one project is
            required in the allow list.
        consumer_reject_list (MutableSequence[google.cloud.ftp_v1.types.InternalServerConfig.DeniedConsumer]):
            Optional. A list of projects that are denied connection.
            Format: "projects/sample_project_id" or
            "projects/1234567890" Projects in this list will be denied
            access, even if they are included in the ``allow_list``. If
            this list is empty, no projects are explicitly rejected.
        psc_endpoints (MutableSequence[google.cloud.ftp_v1.types.InternalServerConfig.PscEndpoint]):
            Output only. Details of endpoints created by
            the customer.
    """

    class AllowedConsumer(proto.Message):
        r"""A consumer project or network that is permitted to connect to
        the server via PSC.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            project (str):
                The project ID or number of the consumer project. Must be in
                the format: ``projects/{project}``.

                This field is a member of `oneof`_ ``consumer_type``.
            connection_limit (int):
                Required. The connection limit for the
                consumer. Value must be greater than 0.
        """

        project: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="consumer_type",
        )
        connection_limit: int = proto.Field(
            proto.INT64,
            number=2,
        )

    class DeniedConsumer(proto.Message):
        r"""A consumer project or network that is denied to connect to
        the server via PSC.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            project (str):
                The project ID or number of the consumer project. Must be in
                the format: ``projects/{project}``.

                This field is a member of `oneof`_ ``consumer_type``.
        """

        project: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="consumer_type",
        )

    class PscEndpoint(proto.Message):
        r"""Details of PSC endpoint created by customer.

        Attributes:
            endpoint (str):
                Output only. This is a Resource name for Private Service
                Connect endpoint. Format:
                ``projects/{project}/regions/{region}/forwardingRules/{forwarding_rule}``
            network (str):
                Output only. The consumer network. Format:
                ``projects/{project}/locations/{location}/networks/{network}``
            status (str):
                Output only. The status of the connected
                endpoint.
        """

        endpoint: str = proto.Field(
            proto.STRING,
            number=1,
        )
        network: str = proto.Field(
            proto.STRING,
            number=2,
        )
        status: str = proto.Field(
            proto.STRING,
            number=3,
        )

    service_attachment: str = proto.Field(
        proto.STRING,
        number=1,
    )
    consumer_accept_list: MutableSequence[AllowedConsumer] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=AllowedConsumer,
    )
    consumer_reject_list: MutableSequence[DeniedConsumer] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=DeniedConsumer,
    )
    psc_endpoints: MutableSequence[PscEndpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=PscEndpoint,
    )


class ServerCredential(proto.Message):
    r"""Represents credentials of an FTP Server.

    Attributes:
        fingerprint (str):
            Output only. The fingerprint is a hash of the
            public key, and is displayed when clients access
            the server for the first time to verify the
            server's identity.
        asymmetric_algorithm (str):
            Output only. Asymmetric algorithm used by the
            public key. Possible values (can be expanded in
            future):

            - ssh-ed25519
    """

    fingerprint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asymmetric_algorithm: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Server(proto.Message):
    r"""Message describing Server object

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        external_config (google.cloud.ftp_v1.types.ExternalServerConfig):
            Configuration for external access.

            This field is a member of `oneof`_ ``access_config``.
        internal_config (google.cloud.ftp_v1.types.InternalServerConfig):
            Configuration for internal access.

            This field is a member of `oneof`_ ``access_config``.
        name (str):
            Identifier. name of resource
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        display_name (str):
            Optional. Display name of the Server
        access_type (google.cloud.ftp_v1.types.Server.AccessType):
            Required. The access type of the Server.
        state (google.cloud.ftp_v1.types.Server.State):
            Output only. The state of the server.
        google_managed_server_credential (google.cloud.ftp_v1.types.ServerCredential):
            Output only. Credentials of the FTP Server.
        service_agent (str):
            Output only. Service agent used to access the
            customer bucket.
    """

    class AccessType(proto.Enum):
        r"""The access type of the Server.

        Values:
            ACCESS_TYPE_UNSPECIFIED (0):
                Default value. This value is unused.
            EXTERNAL (1):
                Server is assigned a public IP.
            INTERNAL (2):
                Server is assigned an internal IP.
        """

        ACCESS_TYPE_UNSPECIFIED = 0
        EXTERNAL = 1
        INTERNAL = 2

    class State(proto.Enum):
        r"""Tracks Server status.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            CREATING (1):
                Server is being created.
            STARTING (2):
                Server is starting.
            ACTIVE (3):
                Server is ready to be used.
            STOPPING (4):
                Server is stopping.
            STOPPED (5):
                Server is stopped.
            DELETING (6):
                Server is being deleted.
            ERROR (7):
                Server is in error state.
            UPDATING (8):
                Server is being updated.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        STARTING = 2
        ACTIVE = 3
        STOPPING = 4
        STOPPED = 5
        DELETING = 6
        ERROR = 7
        UPDATING = 8

    external_config: "ExternalServerConfig" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="access_config",
        message="ExternalServerConfig",
    )
    internal_config: "InternalServerConfig" = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="access_config",
        message="InternalServerConfig",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    access_type: AccessType = proto.Field(
        proto.ENUM,
        number=6,
        enum=AccessType,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    google_managed_server_credential: "ServerCredential" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="ServerCredential",
    )
    service_agent: str = proto.Field(
        proto.STRING,
        number=11,
    )


class ListServersRequest(proto.Message):
    r"""Message for requesting list of Servers

    Attributes:
        parent (str):
            Required. Parent value for ListServersRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
        view (google.cloud.ftp_v1.types.ServerView):
            Optional. The view of the Server resource to
            return.
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
    view: "ServerView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="ServerView",
    )


class ListServersResponse(proto.Message):
    r"""Message for response to listing Servers

    Attributes:
        servers (MutableSequence[google.cloud.ftp_v1.types.Server]):
            The list of Server
        next_page_token (str):
            A token identifying a page of results the
            server should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    servers: MutableSequence["Server"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Server",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetServerRequest(proto.Message):
    r"""Message for getting a Server

    Attributes:
        name (str):
            Required. Name of the resource
        view (google.cloud.ftp_v1.types.ServerView):
            Optional. The view of the Server resource to
            return.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "ServerView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="ServerView",
    )


class CreateServerRequest(proto.Message):
    r"""Message for creating a Server

    Attributes:
        parent (str):
            Required. Value for parent.
        server_id (str):
            Required. A unique ID for the server. Must
            start with a lowercase letter, and end with a
            lowercase letter or number. Can contain
            lowercase letters, numbers, and hyphens. Maximum
            length is 30 characters.
        server (google.cloud.ftp_v1.types.Server):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    server_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    server: "Server" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Server",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateServerRequest(proto.Message):
    r"""Message for updating a Server

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Server resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields present in the request will be overwritten.
        server (google.cloud.ftp_v1.types.Server):
            Required. The resource being updated
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    server: "Server" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Server",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServerRequest(proto.Message):
    r"""Message for deleting a Server
    Note: Cascading delete is not supported. Any nested User
    resources under this Server must be deleted before the Server
    itself can be deleted. Attempting to delete a Server with active
    User resources will result in an error.

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StorageDirectoryMapping(proto.Message):
    r"""Mapping of backing Cloud Storage path to the directory where the
    user lands in the SFTP server. If directory is not specified, it'll
    default to '/'.

    Eg 1 - (bucket_name: bucket, bucket_prefix: path1/path2, directory:
    /abc/def/username)

    The user will land at /abcd/def/username, and the view there will
    match that of /bucket/path1/path2. The user will not be aware of
    Cloud Storage prefix '/bucket/path1' and there will be no such
    directory in the view.

    Eg 2 - (bucket_name: bucket, bucket_prefix: path1/path2, directory:
    '')

    The user will land at '/', and the view there will match that of
    /bucket/path1/path2. The user will not be aware of Cloud Storage
    prefix '/bucket/path1/path2' and there will be no such directory in
    the view.

    Attributes:
        bucket (str):
            Required. Name of the bucket.
        bucket_prefix (str):
            Optional. Prefix inside the bucket.
        directory (str):
            Required. Directory where the user lands in
            the SFTP server.
        permission (google.cloud.ftp_v1.types.StorageDirectoryMapping.Permission):
            Required. Permission to the bucket.
    """

    class Permission(proto.Enum):
        r"""Tracks read/write access to the bucket.

        Values:
            PERMISSION_UNSPECIFIED (0):
                Permission unspecified.
            READ_ONLY (1):
                Read only permission.
            READ_WRITE (2):
                Read write permission.
        """

        PERMISSION_UNSPECIFIED = 0
        READ_ONLY = 1
        READ_WRITE = 2

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    bucket_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    directory: str = proto.Field(
        proto.STRING,
        number=3,
    )
    permission: Permission = proto.Field(
        proto.ENUM,
        number=4,
        enum=Permission,
    )


class User(proto.Message):
    r"""Message describing User object

    Attributes:
        name (str):
            Identifier. User-friendly name via which User
            will be identified.
            projects/{project}/locations/{location}/servers/{server}/users/{user}
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Create time stamp
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. [Output only] Update time stamp
        labels (MutableMapping[str, str]):
            Optional. Labels as key value pairs
        username (str):
            Output only. [Output only] The username of the user.
        customer_service_account (str):
            Required. Service account in customer project
            attached to this SFTP User.
        state (google.cloud.ftp_v1.types.User.State):
            Output only. Tracks user creation.
        user_credentials (MutableSequence[google.cloud.ftp_v1.types.UserCredential]):
            Required. User credential for the user.
            The maximum number of user credentials is 10.
        storage_directory_mappings (MutableSequence[google.cloud.ftp_v1.types.StorageDirectoryMapping]):
            Required. Mapping of Cloud Storage buckets to
            directories where the user will land in the SFTP
            server.
    """

    class State(proto.Enum):
        r"""Tracks user creation.

        Values:
            STATE_UNSPECIFIED (0):
                State unspecified.
            CREATING (1):
                User is being created.
            ACTIVE (2):
                User is ready to be used.
            ERROR (3):
                User creation failed.
            UPDATING (4):
                The resource is being updated.
            DELETING (5):
                The resource is being deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        ERROR = 3
        UPDATING = 4
        DELETING = 5

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    username: str = proto.Field(
        proto.STRING,
        number=5,
    )
    customer_service_account: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    user_credentials: MutableSequence["UserCredential"] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message="UserCredential",
    )
    storage_directory_mappings: MutableSequence["StorageDirectoryMapping"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message="StorageDirectoryMapping",
        )
    )


class ListUsersRequest(proto.Message):
    r"""Message for requesting list of Users

    Attributes:
        parent (str):
            Required. Parent value for ListUsersRequest
        page_size (int):
            Optional. Requested page size. User may
            return fewer items than requested. The maximum
            value is 1000; The default value is 50 if the
            field is omitted (or set to 0).
        page_token (str):
            Optional. A token identifying a page of
            results the user should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
        view (google.cloud.ftp_v1.types.UserView):
            Optional. The view of the User resource to
            return.
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
    view: "UserView" = proto.Field(
        proto.ENUM,
        number=6,
        enum="UserView",
    )


class ListUsersResponse(proto.Message):
    r"""Message for response to listing Users

    Attributes:
        users (MutableSequence[google.cloud.ftp_v1.types.User]):
            The list of User
        next_page_token (str):
            A token identifying a page of results the
            user should return.
        unreachable (MutableSequence[str]):
            Unordered list. Locations that could not be
            reached.
    """

    @property
    def raw_page(self):
        return self

    users: MutableSequence["User"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="User",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetUserRequest(proto.Message):
    r"""Message for getting a User

    Attributes:
        name (str):
            Required. Name of the resource
        view (google.cloud.ftp_v1.types.UserView):
            Optional. The view of the User resource to
            return.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    view: "UserView" = proto.Field(
        proto.ENUM,
        number=2,
        enum="UserView",
    )


class CreateUserRequest(proto.Message):
    r"""Message for creating a User

    Attributes:
        parent (str):
            Required. Value for parent.
        user_id (str):
            Required. A unique user ID for the SFTP user.
            The user ID must start with a lowercase letter
            and can include lowercase letters, numbers, or
            hyphens.
        user (google.cloud.ftp_v1.types.User):
            Required. The resource being created
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

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
    user_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    user: "User" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="User",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateUserRequest(proto.Message):
    r"""Message for updating a User

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the User resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field will be overwritten if it is
            in the mask. If the user does not provide a mask then all
            fields present in the request will be overwritten.
        user (google.cloud.ftp_v1.types.User):
            Required. The resource being updated
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    user: "User" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="User",
    )


class DeleteUserRequest(proto.Message):
    r"""Message for deleting a User

    Attributes:
        name (str):
            Required. Name of the resource
        force (bool):
            Optional. If set to true, the request will
            force the deletion of the User.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class StartServerRequest(proto.Message):
    r"""Request message for starting a Server.

    Attributes:
        name (str):
            Required. Name of the resource Format:
            ``projects/{project}/locations/{location}/servers/{server}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StopServerRequest(proto.Message):
    r"""Request message for stopping a Server.

    Attributes:
        name (str):
            Required. Name of the resource. Format:
            ``projects/{project}/locations/{location}/servers/{server}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UserCredential(proto.Message):
    r"""Message describing UserCredential object

    Attributes:
        credential_name (str):
            Required. Name of the user credential.
        credential_type (google.cloud.ftp_v1.types.UserCredential.Type):
            Required. Type of credential.
        ssh_public_key_body (str):
            Optional. SSH public key body in OpenSSH
            format. Example: "ssh-rsa
            AAAAB3NzaC1yc2EAAAADAQABAAABAQ...".
    """

    class Type(proto.Enum):
        r"""Type of credential.

        Values:
            TYPE_UNSPECIFIED (0):
                Type unspecified.
            PUBLIC_KEY (1):
                Public key credential.
        """

        TYPE_UNSPECIFIED = 0
        PUBLIC_KEY = 1

    credential_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    credential_type: Type = proto.Field(
        proto.ENUM,
        number=2,
        enum=Type,
    )
    ssh_public_key_body: str = proto.Field(
        proto.STRING,
        number=3,
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
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
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


__all__ = tuple(sorted(__protobuf__.manifest))
