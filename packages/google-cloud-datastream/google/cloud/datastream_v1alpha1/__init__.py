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
import google.api_core as api_core

from google.cloud.datastream_v1alpha1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.datastream_v1alpha1.services.datastream",
    "google.cloud.datastream_v1alpha1.types.datastream",
    "google.cloud.datastream_v1alpha1.types.datastream_resources",
}


from .services.datastream import DatastreamAsyncClient, DatastreamClient
from .types.datastream import (
    CreateConnectionProfileRequest,
    CreatePrivateConnectionRequest,
    CreateRouteRequest,
    CreateStreamRequest,
    DeleteConnectionProfileRequest,
    DeletePrivateConnectionRequest,
    DeleteRouteRequest,
    DeleteStreamRequest,
    DiscoverConnectionProfileRequest,
    DiscoverConnectionProfileResponse,
    FetchErrorsRequest,
    FetchErrorsResponse,
    FetchStaticIpsRequest,
    FetchStaticIpsResponse,
    GetConnectionProfileRequest,
    GetPrivateConnectionRequest,
    GetRouteRequest,
    GetStreamRequest,
    ListConnectionProfilesRequest,
    ListConnectionProfilesResponse,
    ListPrivateConnectionsRequest,
    ListPrivateConnectionsResponse,
    ListRoutesRequest,
    ListRoutesResponse,
    ListStreamsRequest,
    ListStreamsResponse,
    OperationMetadata,
    UpdateConnectionProfileRequest,
    UpdateStreamRequest,
)
from .types.datastream_resources import (
    AvroFileFormat,
    ConnectionProfile,
    DestinationConfig,
    Error,
    ForwardSshTunnelConnectivity,
    GcsDestinationConfig,
    GcsFileFormat,
    GcsProfile,
    JsonFileFormat,
    MysqlColumn,
    MysqlDatabase,
    MysqlProfile,
    MysqlRdbms,
    MysqlSourceConfig,
    MysqlSslConfig,
    MysqlTable,
    NoConnectivitySettings,
    OracleColumn,
    OracleProfile,
    OracleRdbms,
    OracleSchema,
    OracleSourceConfig,
    OracleTable,
    PrivateConnection,
    PrivateConnectivity,
    Route,
    SchemaFileFormat,
    SourceConfig,
    StaticServiceIpConnectivity,
    Stream,
    Validation,
    ValidationMessage,
    ValidationResult,
    VpcPeeringConfig,
)

__all__ = (
    "DatastreamAsyncClient",
    "AvroFileFormat",
    "ConnectionProfile",
    "CreateConnectionProfileRequest",
    "CreatePrivateConnectionRequest",
    "CreateRouteRequest",
    "CreateStreamRequest",
    "DatastreamClient",
    "DeleteConnectionProfileRequest",
    "DeletePrivateConnectionRequest",
    "DeleteRouteRequest",
    "DeleteStreamRequest",
    "DestinationConfig",
    "DiscoverConnectionProfileRequest",
    "DiscoverConnectionProfileResponse",
    "Error",
    "FetchErrorsRequest",
    "FetchErrorsResponse",
    "FetchStaticIpsRequest",
    "FetchStaticIpsResponse",
    "ForwardSshTunnelConnectivity",
    "GcsDestinationConfig",
    "GcsFileFormat",
    "GcsProfile",
    "GetConnectionProfileRequest",
    "GetPrivateConnectionRequest",
    "GetRouteRequest",
    "GetStreamRequest",
    "JsonFileFormat",
    "ListConnectionProfilesRequest",
    "ListConnectionProfilesResponse",
    "ListPrivateConnectionsRequest",
    "ListPrivateConnectionsResponse",
    "ListRoutesRequest",
    "ListRoutesResponse",
    "ListStreamsRequest",
    "ListStreamsResponse",
    "MysqlColumn",
    "MysqlDatabase",
    "MysqlProfile",
    "MysqlRdbms",
    "MysqlSourceConfig",
    "MysqlSslConfig",
    "MysqlTable",
    "NoConnectivitySettings",
    "OperationMetadata",
    "OracleColumn",
    "OracleProfile",
    "OracleRdbms",
    "OracleSchema",
    "OracleSourceConfig",
    "OracleTable",
    "PrivateConnection",
    "PrivateConnectivity",
    "Route",
    "SchemaFileFormat",
    "SourceConfig",
    "StaticServiceIpConnectivity",
    "Stream",
    "UpdateConnectionProfileRequest",
    "UpdateStreamRequest",
    "Validation",
    "ValidationMessage",
    "ValidationResult",
    "VpcPeeringConfig",
)

api_core.check_python_version("google.cloud.datastream_v1alpha1")
api_core.check_dependency_versions("google.cloud.datastream_v1alpha1")
