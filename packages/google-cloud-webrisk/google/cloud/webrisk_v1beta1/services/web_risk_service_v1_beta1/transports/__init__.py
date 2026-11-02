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

from .base import WebRiskServiceV1Beta1Transport
from .grpc import WebRiskServiceV1Beta1GrpcTransport
from .grpc_asyncio import WebRiskServiceV1Beta1GrpcAsyncIOTransport
from .rest import (
    WebRiskServiceV1Beta1RestInterceptor,
    WebRiskServiceV1Beta1RestTransport,
)

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[WebRiskServiceV1Beta1Transport]]
_transport_registry["grpc"] = WebRiskServiceV1Beta1GrpcTransport
_transport_registry["grpc_asyncio"] = WebRiskServiceV1Beta1GrpcAsyncIOTransport
_transport_registry["rest"] = WebRiskServiceV1Beta1RestTransport

__all__ = (
    "WebRiskServiceV1Beta1Transport",
    "WebRiskServiceV1Beta1GrpcTransport",
    "WebRiskServiceV1Beta1GrpcAsyncIOTransport",
    "WebRiskServiceV1Beta1RestTransport",
    "WebRiskServiceV1Beta1RestInterceptor",
)
