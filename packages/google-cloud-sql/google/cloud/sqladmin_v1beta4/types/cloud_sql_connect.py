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

from google.cloud.sqladmin_v1beta4.types import cloud_sql_resources

__protobuf__ = proto.module(
    package="google.cloud.sql.v1beta4",
    manifest={
        "GetConnectSettingsRequest",
        "ResolveConnectSettingsRequest",
        "ConnectSettings",
        "GenerateEphemeralCertRequest",
        "GenerateEphemeralCertResponse",
    },
)


class GetConnectSettingsRequest(proto.Message):
    r"""Connect settings retrieval request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Optional snapshot read timestamp to
            trade freshness for performance.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )


class ResolveConnectSettingsRequest(proto.Message):
    r"""Connect settings retrieval request.

    Attributes:
        dns_name (str):
            Required. Cloud SQL instance ID. This does
            not include the project ID.
        location (str):
            Required. The region of the instance.
    """

    dns_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ConnectSettings(proto.Message):
    r"""Connect settings retrieval response.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        kind (str):
            This is always ``sql#connectSettings``.
        server_ca_cert (google.cloud.sqladmin_v1beta4.types.SslCert):
            SSL configuration.
        ip_addresses (MutableSequence[google.cloud.sqladmin_v1beta4.types.IpMapping]):
            The assigned IP addresses for the instance.
        region (str):
            The cloud region for the instance. e.g. ``us-central1``,
            ``europe-west1``. The region cannot be changed after
            instance creation.
        database_version (google.cloud.sqladmin_v1beta4.types.SqlDatabaseVersion):
            The database engine type and version. The
            ``databaseVersion`` field cannot be changed after instance
            creation. MySQL instances: ``MYSQL_8_0``, ``MYSQL_5_7``
            (default), or ``MYSQL_5_6``. PostgreSQL instances:
            ``POSTGRES_9_6``, ``POSTGRES_10``, ``POSTGRES_11`` or
            ``POSTGRES_12`` (default), ``POSTGRES_13``, or
            ``POSTGRES_14``. SQL Server instances:
            ``SQLSERVER_2017_STANDARD`` (default),
            ``SQLSERVER_2017_ENTERPRISE``, ``SQLSERVER_2017_EXPRESS``,
            ``SQLSERVER_2017_WEB``, ``SQLSERVER_2019_STANDARD``,
            ``SQLSERVER_2019_ENTERPRISE``, ``SQLSERVER_2019_EXPRESS``,
            or ``SQLSERVER_2019_WEB``.
        backend_type (google.cloud.sqladmin_v1beta4.types.SqlBackendType):
            ``SECOND_GEN``: Cloud SQL database instance. ``EXTERNAL``: A
            database server that is not managed by Google. This property
            is read-only; use the ``tier`` property in the ``settings``
            object to determine the database type.
        psc_enabled (bool):
            Whether PSC connectivity is enabled for this
            instance.
        dns_name (str):
            The dns name of the instance.
        server_ca_mode (google.cloud.sqladmin_v1beta4.types.ConnectSettings.CaMode):
            Specify what type of CA is used for the
            server certificate.
        custom_subject_alternative_names (MutableSequence[str]):
            Custom subject alternative names for the
            server certificate.
        dns_names (MutableSequence[google.cloud.sqladmin_v1beta4.types.DnsNameMapping]):
            Output only. The list of DNS names used by
            this instance.
        node_count (int):
            The number of read pool nodes in a read pool.

            This field is a member of `oneof`_ ``_node_count``.
        nodes (MutableSequence[google.cloud.sqladmin_v1beta4.types.ConnectSettings.ConnectPoolNodeConfig]):
            Output only. Entries containing information
            about each read pool node of the read pool.
        mdx_protocol_support (MutableSequence[google.cloud.sqladmin_v1beta4.types.ConnectSettings.MdxProtocolSupport]):
            Optional. Output only. mdx_protocol_support controls how the
            client uses metadata exchange when connecting to the
            instance. The values in the list representing parts of the
            MDX protocol that are supported by this instance. When the
            list is empty, the instance does not support MDX, so the
            client must not send an MDX request. The default is empty.
        connection_name (str):
            Optional. Output only. Connection name of the
            Cloud SQL instance used in connection strings,
            in the format project:region:instance.
    """

    class CaMode(proto.Enum):
        r"""Various Certificate Authority (CA) modes for certificate
        signing.

        Values:
            CA_MODE_UNSPECIFIED (0):
                CA mode is unspecified. It is effectively the same as
                ``GOOGLE_MANAGED_INTERNAL_CA``.
            GOOGLE_MANAGED_INTERNAL_CA (1):
                Google-managed self-signed internal CA.
            GOOGLE_MANAGED_CAS_CA (2):
                Google-managed regional CA part of root CA
                hierarchy hosted on Google Cloud's Certificate
                Authority Service (CAS).
            CUSTOMER_MANAGED_CAS_CA (3):
                Customer-managed CA hosted on Google Cloud's
                Certificate Authority Service (CAS).
        """

        CA_MODE_UNSPECIFIED = 0
        GOOGLE_MANAGED_INTERNAL_CA = 1
        GOOGLE_MANAGED_CAS_CA = 2
        CUSTOMER_MANAGED_CAS_CA = 3

    class MdxProtocolSupport(proto.Enum):
        r"""MdxProtocolSupport describes parts of the MDX protocol
        supported by this instance.

        Values:
            MDX_PROTOCOL_SUPPORT_UNSPECIFIED (0):
                Not specified.
            CLIENT_PROTOCOL_TYPE (1):
                Client should send the client protocol type
                in the MDX request.
        """

        MDX_PROTOCOL_SUPPORT_UNSPECIFIED = 0
        CLIENT_PROTOCOL_TYPE = 1

    class ConnectPoolNodeConfig(proto.Message):
        r"""Details of a single read pool node of a read pool.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            name (str):
                Output only. The name of the read pool node.
                Doesn't include the project ID.

                This field is a member of `oneof`_ ``_name``.
            ip_addresses (MutableSequence[google.cloud.sqladmin_v1beta4.types.IpMapping]):
                Output only. Mappings containing IP addresses
                that can be used to connect to the read pool
                node.
            dns_name (str):
                Output only. The DNS name of the read pool
                node.

                This field is a member of `oneof`_ ``_dns_name``.
            dns_names (MutableSequence[google.cloud.sqladmin_v1beta4.types.DnsNameMapping]):
                Output only. The list of DNS names used by
                this read pool node.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
            optional=True,
        )
        ip_addresses: MutableSequence[cloud_sql_resources.IpMapping] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message=cloud_sql_resources.IpMapping,
            )
        )
        dns_name: str = proto.Field(
            proto.STRING,
            number=3,
            optional=True,
        )
        dns_names: MutableSequence[cloud_sql_resources.DnsNameMapping] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=4,
                message=cloud_sql_resources.DnsNameMapping,
            )
        )

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    server_ca_cert: cloud_sql_resources.SslCert = proto.Field(
        proto.MESSAGE,
        number=2,
        message=cloud_sql_resources.SslCert,
    )
    ip_addresses: MutableSequence[cloud_sql_resources.IpMapping] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=cloud_sql_resources.IpMapping,
    )
    region: str = proto.Field(
        proto.STRING,
        number=4,
    )
    database_version: cloud_sql_resources.SqlDatabaseVersion = proto.Field(
        proto.ENUM,
        number=31,
        enum=cloud_sql_resources.SqlDatabaseVersion,
    )
    backend_type: cloud_sql_resources.SqlBackendType = proto.Field(
        proto.ENUM,
        number=32,
        enum=cloud_sql_resources.SqlBackendType,
    )
    psc_enabled: bool = proto.Field(
        proto.BOOL,
        number=33,
    )
    dns_name: str = proto.Field(
        proto.STRING,
        number=34,
    )
    server_ca_mode: CaMode = proto.Field(
        proto.ENUM,
        number=35,
        enum=CaMode,
    )
    custom_subject_alternative_names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=37,
    )
    dns_names: MutableSequence[cloud_sql_resources.DnsNameMapping] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=38,
            message=cloud_sql_resources.DnsNameMapping,
        )
    )
    node_count: int = proto.Field(
        proto.INT32,
        number=63,
        optional=True,
    )
    nodes: MutableSequence[ConnectPoolNodeConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=64,
        message=ConnectPoolNodeConfig,
    )
    mdx_protocol_support: MutableSequence[MdxProtocolSupport] = proto.RepeatedField(
        proto.ENUM,
        number=39,
        enum=MdxProtocolSupport,
    )
    connection_name: str = proto.Field(
        proto.STRING,
        number=40,
    )


class GenerateEphemeralCertRequest(proto.Message):
    r"""Ephemeral certificate creation request.

    Attributes:
        instance (str):
            Cloud SQL instance ID. This does not include
            the project ID.
        project (str):
            Project ID of the project that contains the
            instance.
        public_key (str):
            PEM encoded public key to include in the
            signed certificate.
        access_token (str):
            Optional. Access token to include in the
            signed certificate.
        read_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. Optional snapshot read timestamp to
            trade freshness for performance.
        valid_duration (google.protobuf.duration_pb2.Duration):
            Optional. If set, it will contain the cert
            valid duration.
    """

    instance: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    public_key: str = proto.Field(
        proto.STRING,
        number=3,
    )
    access_token: str = proto.Field(
        proto.STRING,
        number=4,
    )
    read_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    valid_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=12,
        message=duration_pb2.Duration,
    )


class GenerateEphemeralCertResponse(proto.Message):
    r"""Ephemeral certificate creation request.

    Attributes:
        ephemeral_cert (google.cloud.sqladmin_v1beta4.types.SslCert):
            Generated cert
    """

    ephemeral_cert: cloud_sql_resources.SslCert = proto.Field(
        proto.MESSAGE,
        number=1,
        message=cloud_sql_resources.SslCert,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
