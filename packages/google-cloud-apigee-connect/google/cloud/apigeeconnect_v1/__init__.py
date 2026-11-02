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

from google.cloud.apigeeconnect_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.apigeeconnect_v1.services.connection_service",
    "google.cloud.apigeeconnect_v1.services.tether",
    "google.cloud.apigeeconnect_v1.types.connection",
    "google.cloud.apigeeconnect_v1.types.tether",
}


from .services.connection_service import (
    ConnectionServiceAsyncClient,
    ConnectionServiceClient,
)
from .services.tether import TetherAsyncClient, TetherClient
from .types.connection import (
    Cluster,
    Connection,
    ListConnectionsRequest,
    ListConnectionsResponse,
)
from .types.tether import (
    Action,
    EgressRequest,
    EgressResponse,
    Header,
    HttpRequest,
    HttpResponse,
    Payload,
    Scheme,
    StreamInfo,
    TetherEndpoint,
    Url,
)

__all__ = (
    "ConnectionServiceAsyncClient",
    "TetherAsyncClient",
    "Action",
    "Cluster",
    "Connection",
    "ConnectionServiceClient",
    "EgressRequest",
    "EgressResponse",
    "Header",
    "HttpRequest",
    "HttpResponse",
    "ListConnectionsRequest",
    "ListConnectionsResponse",
    "Payload",
    "Scheme",
    "StreamInfo",
    "TetherClient",
    "TetherEndpoint",
    "Url",
)

api_core.check_python_version("google.cloud.apigeeconnect_v1")
api_core.check_dependency_versions("google.cloud.apigeeconnect_v1")
