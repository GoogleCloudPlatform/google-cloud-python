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

from google.pubsub_v1 import gapic_version as package_version

__version__ = package_version.__version__

# PEP 0810: Explicit Lazy Imports
# Python 3.15+ natively intercepts and defers these imports.
# Developers can disable this behavior and force eager imports.
# For more information, see:
# https://docs.python.org/3.15/library/sys.html#sys.set_lazy_imports_filter
# Older Python versions safely ignore this variable.
__lazy_modules__ = {
    "google.pubsub_v1.services.publisher",
    "google.pubsub_v1.services.schema_service",
    "google.pubsub_v1.services.subscriber",
    "google.pubsub_v1.types.pubsub",
    "google.pubsub_v1.types.schema",
}


from .services.publisher import PublisherAsyncClient, PublisherClient
from .services.schema_service import SchemaServiceAsyncClient, SchemaServiceClient
from .services.subscriber import SubscriberAsyncClient, SubscriberClient
from .types.pubsub import (
    AcknowledgeRequest,
    AIInference,
    BigQueryConfig,
    BigtableConfig,
    CloudStorageConfig,
    Compression,
    CreateSnapshotRequest,
    DeadLetterPolicy,
    DeleteSnapshotRequest,
    DeleteSubscriptionRequest,
    DeleteTopicRequest,
    DetachSubscriptionRequest,
    DetachSubscriptionResponse,
    ExpirationPolicy,
    GetSnapshotRequest,
    GetSubscriptionRequest,
    GetTopicRequest,
    IngestionDataSourceSettings,
    IngestionFailureEvent,
    JavaScriptUDF,
    ListSnapshotsRequest,
    ListSnapshotsResponse,
    ListSubscriptionsRequest,
    ListSubscriptionsResponse,
    ListTopicSnapshotsRequest,
    ListTopicSnapshotsResponse,
    ListTopicsRequest,
    ListTopicsResponse,
    ListTopicSubscriptionsRequest,
    ListTopicSubscriptionsResponse,
    MessageStoragePolicy,
    MessageTransform,
    ModifyAckDeadlineRequest,
    ModifyPushConfigRequest,
    PlatformLogsSettings,
    PublishRequest,
    PublishResponse,
    PubsubClientTelemetry,
    PubsubMessage,
    PullRequest,
    PullResponse,
    PushConfig,
    ReceivedMessage,
    RetryPolicy,
    SchemaSettings,
    SeekRequest,
    SeekResponse,
    Snapshot,
    StreamingPullRequest,
    StreamingPullResponse,
    Subscription,
    Topic,
    UpdateSnapshotRequest,
    UpdateSubscriptionRequest,
    UpdateTopicRequest,
)
from .types.schema import (
    CommitSchemaRequest,
    CompiledProtoSchema,
    CreateSchemaRequest,
    DeleteSchemaRequest,
    DeleteSchemaRevisionRequest,
    Encoding,
    GetSchemaRequest,
    ListSchemaRevisionsRequest,
    ListSchemaRevisionsResponse,
    ListSchemasRequest,
    ListSchemasResponse,
    RollbackSchemaRequest,
    Schema,
    SchemaView,
    ValidateMessageRequest,
    ValidateMessageResponse,
    ValidateSchemaRequest,
    ValidateSchemaResponse,
)

__all__ = (
    "PublisherAsyncClient",
    "SchemaServiceAsyncClient",
    "SubscriberAsyncClient",
    "AIInference",
    "AcknowledgeRequest",
    "BigQueryConfig",
    "BigtableConfig",
    "CloudStorageConfig",
    "CommitSchemaRequest",
    "CompiledProtoSchema",
    "Compression",
    "CreateSchemaRequest",
    "CreateSnapshotRequest",
    "DeadLetterPolicy",
    "DeleteSchemaRequest",
    "DeleteSchemaRevisionRequest",
    "DeleteSnapshotRequest",
    "DeleteSubscriptionRequest",
    "DeleteTopicRequest",
    "DetachSubscriptionRequest",
    "DetachSubscriptionResponse",
    "Encoding",
    "ExpirationPolicy",
    "GetSchemaRequest",
    "GetSnapshotRequest",
    "GetSubscriptionRequest",
    "GetTopicRequest",
    "IngestionDataSourceSettings",
    "IngestionFailureEvent",
    "JavaScriptUDF",
    "ListSchemaRevisionsRequest",
    "ListSchemaRevisionsResponse",
    "ListSchemasRequest",
    "ListSchemasResponse",
    "ListSnapshotsRequest",
    "ListSnapshotsResponse",
    "ListSubscriptionsRequest",
    "ListSubscriptionsResponse",
    "ListTopicSnapshotsRequest",
    "ListTopicSnapshotsResponse",
    "ListTopicSubscriptionsRequest",
    "ListTopicSubscriptionsResponse",
    "ListTopicsRequest",
    "ListTopicsResponse",
    "MessageStoragePolicy",
    "MessageTransform",
    "ModifyAckDeadlineRequest",
    "ModifyPushConfigRequest",
    "PlatformLogsSettings",
    "PublishRequest",
    "PublishResponse",
    "PublisherClient",
    "PubsubClientTelemetry",
    "PubsubMessage",
    "PullRequest",
    "PullResponse",
    "PushConfig",
    "ReceivedMessage",
    "RetryPolicy",
    "RollbackSchemaRequest",
    "Schema",
    "SchemaServiceClient",
    "SchemaSettings",
    "SchemaView",
    "SeekRequest",
    "SeekResponse",
    "Snapshot",
    "StreamingPullRequest",
    "StreamingPullResponse",
    "SubscriberClient",
    "Subscription",
    "Topic",
    "UpdateSnapshotRequest",
    "UpdateSubscriptionRequest",
    "UpdateTopicRequest",
    "ValidateMessageRequest",
    "ValidateMessageResponse",
    "ValidateSchemaRequest",
    "ValidateSchemaResponse",
)

api_core.check_python_version("google.pubsub_v1")
api_core.check_dependency_versions("google.pubsub_v1")
