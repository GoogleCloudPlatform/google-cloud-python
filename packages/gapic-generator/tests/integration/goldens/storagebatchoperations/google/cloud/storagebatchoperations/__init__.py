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
from google.cloud.storagebatchoperations import gapic_version as package_version

__version__ = package_version.__version__


from google.cloud.storagebatchoperations_v1.services.storage_batch_operations.client import StorageBatchOperationsClient
from google.cloud.storagebatchoperations_v1.services.storage_batch_operations.async_client import StorageBatchOperationsAsyncClient

from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import CancelJobRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import CancelJobResponse
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import CreateJobRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import DeleteJobRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import GetBucketOperationRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import GetJobRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import ListBucketOperationsRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import ListBucketOperationsResponse
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import ListJobsRequest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import ListJobsResponse
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations import OperationMetadata
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import BucketList
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import BucketOperation
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import Counters
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import CustomContextUpdates
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import DeleteObject
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import ErrorLogEntry
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import ErrorSummary
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import Job
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import LoggingConfig
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import Manifest
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import ObjectCustomContextPayload
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import ObjectRetention
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import PrefixList
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import PutMetadata
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import PutObjectHold
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import RewriteObject
from google.cloud.storagebatchoperations_v1.types.storage_batch_operations_types import UpdateObjectCustomContext

__all__ = ('StorageBatchOperationsClient',
    'StorageBatchOperationsAsyncClient',
    'CancelJobRequest',
    'CancelJobResponse',
    'CreateJobRequest',
    'DeleteJobRequest',
    'GetBucketOperationRequest',
    'GetJobRequest',
    'ListBucketOperationsRequest',
    'ListBucketOperationsResponse',
    'ListJobsRequest',
    'ListJobsResponse',
    'OperationMetadata',
    'BucketList',
    'BucketOperation',
    'Counters',
    'CustomContextUpdates',
    'DeleteObject',
    'ErrorLogEntry',
    'ErrorSummary',
    'Job',
    'LoggingConfig',
    'Manifest',
    'ObjectCustomContextPayload',
    'ObjectRetention',
    'PrefixList',
    'PutMetadata',
    'PutObjectHold',
    'RewriteObject',
    'UpdateObjectCustomContext',
)
