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

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.sql.v1",
    manifest={
        "SqlUsersDeleteRequest",
        "SqlUsersGetRequest",
        "SqlUsersInsertRequest",
        "SqlUsersListRequest",
        "SqlUsersUpdateRequest",
        "UserPasswordValidationPolicy",
        "PasswordStatus",
        "User",
        "SqlServerUserDetails",
        "UsersListResponse",
    },
)


class SqlUsersDeleteRequest(proto.Message):
    r"""

    Attributes:
        host (str):
            Host of the user in the instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        name (str):
            Name of the user in the instance.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    host: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SqlUsersGetRequest(proto.Message):
    r"""Request message for Users Get RPC

    Attributes:
        instance (str):
            Database instance ID. This does not include
            the project ID.
        name (str):
            User of the instance.
        project (str):
            Project ID of the project that contains the
            instance.
        host (str):
            Host of a user of the instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )
    host: str = proto.Field(
        proto.STRING,
        number=4,
    )
    location: str = proto.Field(
        proto.STRING,
        number=5,
    )


class SqlUsersInsertRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        body (google.cloud.sqladmin_v1.types.User):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    body: "User" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="User",
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlUsersListRequest(proto.Message):
    r"""

    Attributes:
        instance (str):
            Database instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    location: str = proto.Field(
        proto.STRING,
        number=3,
    )


class SqlUsersUpdateRequest(proto.Message):
    r"""

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        host (str):
            Optional. Host of the user in the instance.
        instance (str):
            Database instance ID. This does not include
            the project ID.
        name (str):
            Name of the user in the instance.
        project (str):
            Project ID of the project that contains the
            instance.
        database_roles (MutableSequence[str]):
            Optional. List of database roles to grant to the user.
            body.database_roles will be ignored for update request.
        revoke_existing_roles (bool):
            Optional. Specifies whether to revoke existing roles that
            are not present in the ``database_roles`` field. If
            ``false`` or unset, the database roles specified in
            ``database_roles`` are added to the user's existing roles.

            This field is a member of `oneof`_ ``_revoke_existing_roles``.
        server_roles (MutableSequence[str]):
            Optional. The server roles to grant to the SQL Server login.
            Existing server roles will not be revoked if
            revoke_existing_roles is false. body.server_roles will be
            ignored for update request.
        revoke_existing_server_roles (bool):
            Optional. Specifies whether to revoke existing roles that
            are not present in the ``server_roles`` field. If ``false``
            or unset, the server roles specified in ``server_roles`` are
            added to the user's existing server roles.

            This field is a member of `oneof`_ ``_revoke_existing_server_roles``.
        body (google.cloud.sqladmin_v1.types.User):

        location (str):
            Optional. Region of the Cloud SQL instance.
    """

    host: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    project: str = proto.Field(
        proto.STRING,
        number=4,
    )
    database_roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    revoke_existing_roles: bool = proto.Field(
        proto.BOOL,
        number=6,
        optional=True,
    )
    server_roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=7,
    )
    revoke_existing_server_roles: bool = proto.Field(
        proto.BOOL,
        number=8,
        optional=True,
    )
    body: "User" = proto.Field(
        proto.MESSAGE,
        number=100,
        message="User",
    )
    location: str = proto.Field(
        proto.STRING,
        number=9,
    )


class UserPasswordValidationPolicy(proto.Message):
    r"""User level password validation policy.

    Attributes:
        allowed_failed_attempts (int):
            Number of failed login attempts allowed
            before user get locked.
        password_expiration_duration (google.protobuf.duration_pb2.Duration):
            Expiration duration after password is
            updated.
        enable_failed_attempts_check (bool):
            If true, failed login attempts check will be
            enabled.
        status (google.cloud.sqladmin_v1.types.PasswordStatus):
            Output only. Read-only password status.
        enable_password_verification (bool):
            If true, the user must specify the current
            password before changing the password. This flag
            is supported only for MySQL.
    """

    allowed_failed_attempts: int = proto.Field(
        proto.INT32,
        number=1,
    )
    password_expiration_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )
    enable_failed_attempts_check: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    status: "PasswordStatus" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PasswordStatus",
    )
    enable_password_verification: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


class PasswordStatus(proto.Message):
    r"""Read-only password status.

    Attributes:
        locked (bool):
            If true, user does not have login privileges.
        password_expiration_time (google.protobuf.timestamp_pb2.Timestamp):
            The expiration time of the current password.
    """

    locked: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    password_expiration_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class User(proto.Message):
    r"""A Cloud SQL user resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#user``.
        password (str):
            The password for the user.
        etag (str):
            This field is deprecated and will be removed
            from a future version of the API.
        name (str):
            The name of the user in the Cloud SQL instance. Can be
            omitted for ``update`` because it is already specified in
            the URL.
        host (str):
            Optional. The host from which the user can connect. For
            ``insert`` operations, host defaults to an empty string. For
            ``update`` operations, host is specified as part of the
            request URL. The host name cannot be updated after
            insertion. For a MySQL instance, it's required; for a
            PostgreSQL or SQL Server instance, it's optional.
        instance (str):
            The name of the Cloud SQL instance. This does not include
            the project ID. Can be omitted for ``update`` because it is
            already specified on the URL.
        project (str):
            The project ID of the project containing the Cloud SQL
            database. The Google apps domain is prefixed if applicable.
            Can be omitted for ``update`` because it is already
            specified on the URL.
        type_ (google.cloud.sqladmin_v1.types.User.SqlUserType):
            The user type. It determines the method to
            authenticate the user during login. The default
            is the database's built-in user type.
        sqlserver_user_details (google.cloud.sqladmin_v1.types.SqlServerUserDetails):

            This field is a member of `oneof`_ ``user_details``.
        iam_email (str):
            Optional. The full email for an IAM user. For
            normal database users, this will not be filled.
            Only applicable to MySQL database users.
        password_policy (google.cloud.sqladmin_v1.types.UserPasswordValidationPolicy):
            User level password validation policy.
        dual_password_type (google.cloud.sqladmin_v1.types.User.DualPasswordType):
            Dual password status for the user.

            This field is a member of `oneof`_ ``_dual_password_type``.
        iam_status (google.cloud.sqladmin_v1.types.User.IamStatus):
            Indicates if a group is active or inactive
            for IAM database authentication.

            This field is a member of `oneof`_ ``_iam_status``.
        database_roles (MutableSequence[str]):
            Optional. Role memberships of the user
        server_roles (MutableSequence[str]):
            Optional. The server roles for the SQL Server
            login.
    """

    class SqlUserType(proto.Enum):
        r"""The user type.

        Values:
            BUILT_IN (0):
                The database's built-in user type.
            CLOUD_IAM_USER (1):
                Cloud IAM user.
            CLOUD_IAM_SERVICE_ACCOUNT (2):
                Cloud IAM service account.
            CLOUD_IAM_GROUP (3):
                Cloud IAM group. Not used for login.
            CLOUD_IAM_GROUP_USER (4):
                Read-only. Login for a user that belongs to
                the Cloud IAM group.
            CLOUD_IAM_GROUP_SERVICE_ACCOUNT (5):
                Read-only. Login for a service account that
                belongs to the Cloud IAM group.
            CLOUD_IAM_WORKFORCE_IDENTITY (6):
                Cloud IAM workforce identity managed by
                Workforce Identity Federation.
            ENTRAID_USER (7):
                Microsoft Entra ID user.
            ACTIVE_DIRECTORY_USER (8):
                Active Directory user.
        """

        BUILT_IN = 0
        CLOUD_IAM_USER = 1
        CLOUD_IAM_SERVICE_ACCOUNT = 2
        CLOUD_IAM_GROUP = 3
        CLOUD_IAM_GROUP_USER = 4
        CLOUD_IAM_GROUP_SERVICE_ACCOUNT = 5
        CLOUD_IAM_WORKFORCE_IDENTITY = 6
        ENTRAID_USER = 7
        ACTIVE_DIRECTORY_USER = 8

    class DualPasswordType(proto.Enum):
        r"""The type of retained password.

        Values:
            DUAL_PASSWORD_TYPE_UNSPECIFIED (0):
                The default value.
            NO_MODIFY_DUAL_PASSWORD (1):
                Do not update the user's dual password
                status.
            NO_DUAL_PASSWORD (2):
                No dual password usable for connecting using
                this user.
            DUAL_PASSWORD (3):
                Dual password usable for connecting using
                this user.
        """

        DUAL_PASSWORD_TYPE_UNSPECIFIED = 0
        NO_MODIFY_DUAL_PASSWORD = 1
        NO_DUAL_PASSWORD = 2
        DUAL_PASSWORD = 3

    class IamStatus(proto.Enum):
        r"""Indicates if a group is available for IAM database
        authentication.

        Values:
            IAM_STATUS_UNSPECIFIED (0):
                The default value for users that are not of type
                CLOUD_IAM_GROUP. Only CLOUD_IAM_GROUP users will be inactive
                or active. Users with an IamStatus of IAM_STATUS_UNSPECIFIED
                will not display whether they are active or inactive as that
                is not applicable to them.
            INACTIVE (1):
                INACTIVE indicates a group is not available
                for IAM database authentication.
            ACTIVE (2):
                ACTIVE indicates a group is available for IAM
                database authentication.
        """

        IAM_STATUS_UNSPECIFIED = 0
        INACTIVE = 1
        ACTIVE = 2

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    password: str = proto.Field(
        proto.STRING,
        number=2,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=3,
    )
    name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    host: str = proto.Field(
        proto.STRING,
        number=5,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=6,
    )
    project: str = proto.Field(
        proto.STRING,
        number=7,
    )
    type_: SqlUserType = proto.Field(
        proto.ENUM,
        number=8,
        enum=SqlUserType,
    )
    sqlserver_user_details: "SqlServerUserDetails" = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="user_details",
        message="SqlServerUserDetails",
    )
    iam_email: str = proto.Field(
        proto.STRING,
        number=11,
    )
    password_policy: "UserPasswordValidationPolicy" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="UserPasswordValidationPolicy",
    )
    dual_password_type: DualPasswordType = proto.Field(
        proto.ENUM,
        number=13,
        optional=True,
        enum=DualPasswordType,
    )
    iam_status: IamStatus = proto.Field(
        proto.ENUM,
        number=14,
        optional=True,
        enum=IamStatus,
    )
    database_roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=15,
    )
    server_roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=16,
    )


class SqlServerUserDetails(proto.Message):
    r"""Represents a Sql Server user on the Cloud SQL instance.

    Attributes:
        disabled (bool):
            Indicates if the user has been disabled.
        server_roles (MutableSequence[str]):
            Indicates the server roles for this user.
    """

    disabled: bool = proto.Field(
        proto.BOOL,
        number=1,
    )
    server_roles: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class UsersListResponse(proto.Message):
    r"""User list response.

    Attributes:
        kind (str):
            This is always ``sql#usersList``.
        items (MutableSequence[google.cloud.sqladmin_v1.types.User]):
            List of user resources in the instance.
        next_page_token (str):
            Unused.
    """

    @property
    def raw_page(self):
        return self

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    items: MutableSequence["User"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="User",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
