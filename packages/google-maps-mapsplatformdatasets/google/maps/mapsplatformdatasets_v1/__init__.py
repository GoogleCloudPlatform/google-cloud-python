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

from google.maps.mapsplatformdatasets_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.maps.mapsplatformdatasets_v1.services.maps_platform_datasets",
    "google.maps.mapsplatformdatasets_v1.types.data_source",
    "google.maps.mapsplatformdatasets_v1.types.dataset",
    "google.maps.mapsplatformdatasets_v1.types.maps_platform_datasets",
    "google.maps.mapsplatformdatasets_v1.types.maps_platform_datasets_service",
}


from .services.maps_platform_datasets import (
    MapsPlatformDatasetsAsyncClient,
    MapsPlatformDatasetsClient,
)
from .types.data_source import FileFormat, GcsSource, LocalFileSource
from .types.dataset import Dataset, Status, Usage
from .types.maps_platform_datasets import (
    CreateDatasetRequest,
    DeleteDatasetRequest,
    FetchDatasetErrorsRequest,
    FetchDatasetErrorsResponse,
    GetDatasetRequest,
    ListDatasetsRequest,
    ListDatasetsResponse,
    UpdateDatasetMetadataRequest,
)

__all__ = (
    "MapsPlatformDatasetsAsyncClient",
    "CreateDatasetRequest",
    "Dataset",
    "DeleteDatasetRequest",
    "FetchDatasetErrorsRequest",
    "FetchDatasetErrorsResponse",
    "FileFormat",
    "GcsSource",
    "GetDatasetRequest",
    "ListDatasetsRequest",
    "ListDatasetsResponse",
    "LocalFileSource",
    "MapsPlatformDatasetsClient",
    "Status",
    "UpdateDatasetMetadataRequest",
    "Usage",
)

api_core.check_python_version("google.maps.mapsplatformdatasets_v1")
api_core.check_dependency_versions("google.maps.mapsplatformdatasets_v1")
