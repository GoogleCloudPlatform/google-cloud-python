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

from .base import WorkflowsServiceV2BetaTransport
from .grpc import WorkflowsServiceV2BetaGrpcTransport
from .grpc_asyncio import WorkflowsServiceV2BetaGrpcAsyncIOTransport
from .rest import (
    WorkflowsServiceV2BetaRestInterceptor,
    WorkflowsServiceV2BetaRestTransport,
)

# Compile a registry of transports.
_transport_registry = OrderedDict()  # type: Dict[str, Type[WorkflowsServiceV2BetaTransport]]
_transport_registry["grpc"] = WorkflowsServiceV2BetaGrpcTransport
_transport_registry["grpc_asyncio"] = WorkflowsServiceV2BetaGrpcAsyncIOTransport
_transport_registry["rest"] = WorkflowsServiceV2BetaRestTransport

__all__ = (
    "WorkflowsServiceV2BetaTransport",
    "WorkflowsServiceV2BetaGrpcTransport",
    "WorkflowsServiceV2BetaGrpcAsyncIOTransport",
    "WorkflowsServiceV2BetaRestTransport",
    "WorkflowsServiceV2BetaRestInterceptor",
)
