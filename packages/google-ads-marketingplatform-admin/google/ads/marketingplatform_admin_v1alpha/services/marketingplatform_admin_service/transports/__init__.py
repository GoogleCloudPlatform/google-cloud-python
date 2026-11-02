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

from .base import MarketingplatformAdminServiceTransport
from .grpc import MarketingplatformAdminServiceGrpcTransport
from .grpc_asyncio import MarketingplatformAdminServiceGrpcAsyncIOTransport
from .rest import (
    MarketingplatformAdminServiceRestInterceptor,
    MarketingplatformAdminServiceRestTransport,
)

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[MarketingplatformAdminServiceTransport]]
_transport_registry["grpc"] = MarketingplatformAdminServiceGrpcTransport
_transport_registry["grpc_asyncio"] = MarketingplatformAdminServiceGrpcAsyncIOTransport
_transport_registry["rest"] = MarketingplatformAdminServiceRestTransport

__all__ = (
    "MarketingplatformAdminServiceTransport",
    "MarketingplatformAdminServiceGrpcTransport",
    "MarketingplatformAdminServiceGrpcAsyncIOTransport",
    "MarketingplatformAdminServiceRestTransport",
    "MarketingplatformAdminServiceRestInterceptor",
)
