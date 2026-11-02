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
from google.cloud.storagebatchoperations_v1 import gapic_version as package_version

import google.api_core as api_core

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
"google.cloud.storagebatchoperations_v1.services.storage_batch_operations",
"google.cloud.storagebatchoperations_v1.types.storage_batch_operations",
"google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types",
}


from .services.storage_batch_operations import StorageBatchOperationsClient
from .services.storage_batch_operations import StorageBatchOperationsAsyncClient

from .types.storage_batch_operations import CancelJobRequest
from .types.storage_batch_operations import CancelJobResponse
from .types.storage_batch_operations import CreateJobRequest
from .types.storage_batch_operations import DeleteJobRequest
from .types.storage_batch_operations import GetBucketOperationRequest
from .types.storage_batch_operations import GetJobRequest
from .types.storage_batch_operations import ListBucketOperationsRequest
from .types.storage_batch_operations import ListBucketOperationsResponse
from .types.storage_batch_operations import ListJobsRequest
from .types.storage_batch_operations import ListJobsResponse
from .types.storage_batch_operations import OperationMetadata
from .types.storage_batch_operations_types import BucketList
from .types.storage_batch_operations_types import BucketOperation
from .types.storage_batch_operations_types import Counters
from .types.storage_batch_operations_types import CustomContextUpdates
from .types.storage_batch_operations_types import DeleteObject
from .types.storage_batch_operations_types import ErrorLogEntry
from .types.storage_batch_operations_types import ErrorSummary
from .types.storage_batch_operations_types import Job
from .types.storage_batch_operations_types import LoggingConfig
from .types.storage_batch_operations_types import Manifest
from .types.storage_batch_operations_types import ObjectCustomContextPayload
from .types.storage_batch_operations_types import ObjectRetention
from .types.storage_batch_operations_types import PrefixList
from .types.storage_batch_operations_types import PutMetadata
from .types.storage_batch_operations_types import PutObjectHold
from .types.storage_batch_operations_types import RewriteObject
from .types.storage_batch_operations_types import UpdateObjectCustomContext

__all__ = (
    'StorageBatchOperationsAsyncClient',
'BucketList',
'BucketOperation',
'CancelJobRequest',
'CancelJobResponse',
'Counters',
'CreateJobRequest',
'CustomContextUpdates',
'DeleteJobRequest',
'DeleteObject',
'ErrorLogEntry',
'ErrorSummary',
'GetBucketOperationRequest',
'GetJobRequest',
'Job',
'ListBucketOperationsRequest',
'ListBucketOperationsResponse',
'ListJobsRequest',
'ListJobsResponse',
'LoggingConfig',
'Manifest',
'ObjectCustomContextPayload',
'ObjectRetention',
'OperationMetadata',
'PrefixList',
'PutMetadata',
'PutObjectHold',
'RewriteObject',
'StorageBatchOperationsClient',
'UpdateObjectCustomContext',
)

api_core.check_python_version("google.cloud.storagebatchoperations_v1")
api_core.check_dependency_versions("google.cloud.storagebatchoperations_v1")
