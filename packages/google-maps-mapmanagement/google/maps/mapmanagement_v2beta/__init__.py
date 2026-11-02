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

from google.maps.mapmanagement_v2beta import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.maps.mapmanagement_v2beta.services.map_management",
    "google.maps.mapmanagement_v2beta.types.map_management_service",
}


from .services.map_management import MapManagementAsyncClient, MapManagementClient
from .types.map_management_service import (
    CreateMapConfigRequest,
    CreateMapContextConfigRequest,
    CreateStyleConfigRequest,
    DeleteMapConfigRequest,
    DeleteMapContextConfigRequest,
    DeleteStyleConfigRequest,
    GetMapConfigRequest,
    GetMapContextConfigRequest,
    GetStyleConfigRequest,
    ListMapConfigsRequest,
    ListMapConfigsResponse,
    ListMapContextConfigsRequest,
    ListMapContextConfigsResponse,
    ListStyleConfigsRequest,
    ListStyleConfigsResponse,
    MapConfig,
    MapContextConfig,
    MapFeatures,
    MapRenderingType,
    StyleConfig,
    StyleConfigView,
    UpdateMapConfigRequest,
    UpdateMapContextConfigRequest,
    UpdateStyleConfigRequest,
)

__all__ = (
    "MapManagementAsyncClient",
    "CreateMapConfigRequest",
    "CreateMapContextConfigRequest",
    "CreateStyleConfigRequest",
    "DeleteMapConfigRequest",
    "DeleteMapContextConfigRequest",
    "DeleteStyleConfigRequest",
    "GetMapConfigRequest",
    "GetMapContextConfigRequest",
    "GetStyleConfigRequest",
    "ListMapConfigsRequest",
    "ListMapConfigsResponse",
    "ListMapContextConfigsRequest",
    "ListMapContextConfigsResponse",
    "ListStyleConfigsRequest",
    "ListStyleConfigsResponse",
    "MapConfig",
    "MapContextConfig",
    "MapFeatures",
    "MapManagementClient",
    "MapRenderingType",
    "StyleConfig",
    "StyleConfigView",
    "UpdateMapConfigRequest",
    "UpdateMapContextConfigRequest",
    "UpdateStyleConfigRequest",
)

api_core.check_python_version("google.maps.mapmanagement_v2beta")
api_core.check_dependency_versions("google.maps.mapmanagement_v2beta")
