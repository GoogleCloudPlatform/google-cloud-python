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

from .base import CloudProductRegistryReadServiceTransport
from .grpc import CloudProductRegistryReadServiceGrpcTransport
from .grpc_asyncio import CloudProductRegistryReadServiceGrpcAsyncIOTransport
from .rest import (
    CloudProductRegistryReadServiceRestInterceptor,
    CloudProductRegistryReadServiceRestTransport,
)

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[CloudProductRegistryReadServiceTransport]]
_transport_registry["grpc"] = CloudProductRegistryReadServiceGrpcTransport
_transport_registry["grpc_asyncio"] = (
    CloudProductRegistryReadServiceGrpcAsyncIOTransport
)
_transport_registry["rest"] = CloudProductRegistryReadServiceRestTransport

__all__ = (
    "CloudProductRegistryReadServiceTransport",
    "CloudProductRegistryReadServiceGrpcTransport",
    "CloudProductRegistryReadServiceGrpcAsyncIOTransport",
    "CloudProductRegistryReadServiceRestTransport",
    "CloudProductRegistryReadServiceRestInterceptor",
)
