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
from collections import OrderedDict
from typing import Dict, Type

from .base import SqlBackupRunsServiceTransport
from .grpc import SqlBackupRunsServiceGrpcTransport
from .grpc_asyncio import SqlBackupRunsServiceGrpcAsyncIOTransport
from .rest import SqlBackupRunsServiceRestInterceptor, SqlBackupRunsServiceRestTransport

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[SqlBackupRunsServiceTransport]]
_transport_registry["grpc"] = SqlBackupRunsServiceGrpcTransport
_transport_registry["grpc_asyncio"] = SqlBackupRunsServiceGrpcAsyncIOTransport
_transport_registry["rest"] = SqlBackupRunsServiceRestTransport

__all__ = (
    "SqlBackupRunsServiceTransport",
    "SqlBackupRunsServiceGrpcTransport",
    "SqlBackupRunsServiceGrpcAsyncIOTransport",
    "SqlBackupRunsServiceRestTransport",
    "SqlBackupRunsServiceRestInterceptor",
)
