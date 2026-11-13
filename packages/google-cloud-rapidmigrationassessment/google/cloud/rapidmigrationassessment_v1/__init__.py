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

from google.cloud.rapidmigrationassessment_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.cloud.rapidmigrationassessment_v1.services.rapid_migration_assessment",
    "google.cloud.rapidmigrationassessment_v1.types.api_entities",
    "google.cloud.rapidmigrationassessment_v1.types.rapidmigrationassessment",
}


from .services.rapid_migration_assessment import (
    RapidMigrationAssessmentAsyncClient,
    RapidMigrationAssessmentClient,
)
from .types.api_entities import Annotation, Collector, GuestOsScan, VSphereScan
from .types.rapidmigrationassessment import (
    CreateAnnotationRequest,
    CreateCollectorRequest,
    DeleteCollectorRequest,
    GetAnnotationRequest,
    GetCollectorRequest,
    ListCollectorsRequest,
    ListCollectorsResponse,
    OperationMetadata,
    PauseCollectorRequest,
    RegisterCollectorRequest,
    ResumeCollectorRequest,
    UpdateCollectorRequest,
)

__all__ = (
    "RapidMigrationAssessmentAsyncClient",
    "Annotation",
    "Collector",
    "CreateAnnotationRequest",
    "CreateCollectorRequest",
    "DeleteCollectorRequest",
    "GetAnnotationRequest",
    "GetCollectorRequest",
    "GuestOsScan",
    "ListCollectorsRequest",
    "ListCollectorsResponse",
    "OperationMetadata",
    "PauseCollectorRequest",
    "RapidMigrationAssessmentClient",
    "RegisterCollectorRequest",
    "ResumeCollectorRequest",
    "UpdateCollectorRequest",
    "VSphereScan",
)

api_core.check_python_version("google.cloud.rapidmigrationassessment_v1")
api_core.check_dependency_versions("google.cloud.rapidmigrationassessment_v1")
