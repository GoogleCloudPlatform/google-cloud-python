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
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.pubsub_v1.types import schema as gp_schema

__protobuf__ = proto.module(
    package="google.pubsub.v1",
    manifest={
        "MessageStoragePolicy",
        "SchemaSettings",
        "IngestionDataSourceSettings",
        "PlatformLogsSettings",
        "IngestionFailureEvent",
        "JavaScriptUDF",
        "Compression",
        "AIInference",
        "MessageTransform",
        "Topic",
        "PubsubMessage",
        "GetTopicRequest",
        "UpdateTopicRequest",
        "PublishRequest",
        "PublishResponse",
        "ListTopicsRequest",
        "ListTopicsResponse",
        "ListTopicSubscriptionsRequest",
        "ListTopicSubscriptionsResponse",
        "ListTopicSnapshotsRequest",
        "ListTopicSnapshotsResponse",
        "DeleteTopicRequest",
        "DetachSubscriptionRequest",
        "DetachSubscriptionResponse",
        "Subscription",
        "RetryPolicy",
        "DeadLetterPolicy",
        "ExpirationPolicy",
        "PushConfig",
        "BigQueryConfig",
        "BigtableConfig",
        "CloudStorageConfig",
        "ReceivedMessage",
        "GetSubscriptionRequest",
        "UpdateSubscriptionRequest",
        "ListSubscriptionsRequest",
        "ListSubscriptionsResponse",
        "DeleteSubscriptionRequest",
        "ModifyPushConfigRequest",
        "PullRequest",
        "PullResponse",
        "ModifyAckDeadlineRequest",
        "AcknowledgeRequest",
        "StreamingPullRequest",
        "StreamingPullResponse",
        "CreateSnapshotRequest",
        "UpdateSnapshotRequest",
        "Snapshot",
        "GetSnapshotRequest",
        "ListSnapshotsRequest",
        "ListSnapshotsResponse",
        "DeleteSnapshotRequest",
        "SeekRequest",
        "SeekResponse",
        "PubsubClientTelemetry",
    },
)


class MessageStoragePolicy(proto.Message):
    r"""A policy constraining the storage of messages published to
    the topic.

    Attributes:
        allowed_persistence_regions (MutableSequence[str]):
            Optional. A list of IDs of Google Cloud
            regions where messages that are published to the
            topic may be persisted in storage. Messages
            published by publishers running in non-allowed
            Google Cloud regions (or running outside of
            Google Cloud altogether) are routed for storage
            in one of the allowed regions. An empty list
            means that no regions are allowed, and is not a
            valid configuration.
        enforce_in_transit (bool):
            Optional. If true, ``allowed_persistence_regions`` is also
            used to enforce in-transit guarantees for messages. That is,
            Pub/Sub will fail Publish operations on this topic and
            subscribe operations on any subscription attached to this
            topic in any region that is not in
            ``allowed_persistence_regions``.
    """

    allowed_persistence_regions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    enforce_in_transit: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class SchemaSettings(proto.Message):
    r"""Settings for validating messages published against a schema.

    Attributes:
        schema (str):
            Required. The name of the schema that messages published
            should be validated against. Format is
            ``projects/{project}/schemas/{schema}``. The value of this
            field will be ``_deleted-schema_`` if the schema has been
            deleted.
        encoding (google.pubsub_v1.types.Encoding):
            Optional. The encoding of messages validated against
            ``schema``.
        first_revision_id (str):
            Optional. The minimum (inclusive) revision allowed for
            validating messages. If empty or not present, allow any
            revision to be validated against last_revision or any
            revision created before.
        last_revision_id (str):
            Optional. The maximum (inclusive) revision allowed for
            validating messages. If empty or not present, allow any
            revision to be validated against first_revision or any
            revision created after.
    """

    schema: str = proto.Field(
        proto.STRING,
        number=1,
    )
    encoding: gp_schema.Encoding = proto.Field(
        proto.ENUM,
        number=2,
        enum=gp_schema.Encoding,
    )
    first_revision_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    last_revision_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class IngestionDataSourceSettings(proto.Message):
    r"""Settings for an ingestion data source on a topic.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        aws_kinesis (google.pubsub_v1.types.IngestionDataSourceSettings.AwsKinesis):
            Optional. Amazon Kinesis Data Streams.

            This field is a member of `oneof`_ ``source``.
        cloud_storage (google.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage):
            Optional. Cloud Storage.

            This field is a member of `oneof`_ ``source``.
        azure_event_hubs (google.pubsub_v1.types.IngestionDataSourceSettings.AzureEventHubs):
            Optional. Azure Event Hubs.

            This field is a member of `oneof`_ ``source``.
        aws_msk (google.pubsub_v1.types.IngestionDataSourceSettings.AwsMsk):
            Optional. Amazon MSK.

            This field is a member of `oneof`_ ``source``.
        confluent_cloud (google.pubsub_v1.types.IngestionDataSourceSettings.ConfluentCloud):
            Optional. Confluent Cloud.

            This field is a member of `oneof`_ ``source``.
        platform_logs_settings (google.pubsub_v1.types.PlatformLogsSettings):
            Optional. Platform Logs settings. If unset,
            no Platform Logs will be generated.
    """

    class AwsKinesis(proto.Message):
        r"""Ingestion settings for Amazon Kinesis Data Streams.

        Attributes:
            state (google.pubsub_v1.types.IngestionDataSourceSettings.AwsKinesis.State):
                Output only. An output-only field that
                indicates the state of the Kinesis ingestion
                source.
            stream_arn (str):
                Required. The Kinesis stream ARN to ingest
                data from.
            consumer_arn (str):
                Required. The Kinesis consumer ARN to used
                for ingestion in Enhanced Fan-Out mode. The
                consumer must be already created and ready to be
                used.
            aws_role_arn (str):
                Required. AWS role ARN to be used for
                Federated Identity authentication with Kinesis.
                Check the Pub/Sub docs for how to set up this
                role and the required permissions that need to
                be attached to it.
            gcp_service_account (str):
                Required. The GCP service account to be used for Federated
                Identity authentication with Kinesis (via a
                ``AssumeRoleWithWebIdentity`` call for the provided role).
                The ``aws_role_arn`` must be set up with
                ``accounts.google.com:sub`` equals to this service account
                number.
        """

        class State(proto.Enum):
            r"""Possible states for ingestion from Amazon Kinesis Data
            Streams.

            Values:
                STATE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ACTIVE (1):
                    Ingestion is active.
                KINESIS_PERMISSION_DENIED (2):
                    Permission denied encountered while consuming data from
                    Kinesis. This can happen if:

                    - The provided ``aws_role_arn`` does not exist or does not
                      have the appropriate permissions attached.
                    - The provided ``aws_role_arn`` is not set up properly for
                      Identity Federation using ``gcp_service_account``.
                    - The Pub/Sub SA is not granted the
                      ``iam.serviceAccounts.getOpenIdToken`` permission on
                      ``gcp_service_account``.
                PUBLISH_PERMISSION_DENIED (3):
                    Permission denied encountered while publishing to the topic.
                    This can happen if the Pub/Sub SA has not been granted the
                    `appropriate publish
                    permissions <https://cloud.google.com/pubsub/docs/access-control#pubsub.publisher>`__
                STREAM_NOT_FOUND (4):
                    The Kinesis stream does not exist.
                CONSUMER_NOT_FOUND (5):
                    The Kinesis consumer does not exist.
                CONFLICTING_REGION_CONSTRAINTS (6):
                    Indicates an error state where the ingestion
                    source cannot be processed because the selected
                    ingestion region is not permitted by the
                    Regional Access Boundary (RAB) restrictions on
                    the project's service account.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            KINESIS_PERMISSION_DENIED = 2
            PUBLISH_PERMISSION_DENIED = 3
            STREAM_NOT_FOUND = 4
            CONSUMER_NOT_FOUND = 5
            CONFLICTING_REGION_CONSTRAINTS = 6

        state: "IngestionDataSourceSettings.AwsKinesis.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="IngestionDataSourceSettings.AwsKinesis.State",
        )
        stream_arn: str = proto.Field(
            proto.STRING,
            number=2,
        )
        consumer_arn: str = proto.Field(
            proto.STRING,
            number=3,
        )
        aws_role_arn: str = proto.Field(
            proto.STRING,
            number=4,
        )
        gcp_service_account: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class CloudStorage(proto.Message):
        r"""Ingestion settings for Cloud Storage.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            state (google.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.State):
                Output only. An output-only field that
                indicates the state of the Cloud Storage
                ingestion source.
            bucket (str):
                Optional. Cloud Storage bucket. The bucket name must be
                without any prefix like "gs://". See the [bucket naming
                requirements]
                (https://cloud.google.com/storage/docs/buckets#naming).
            text_format (google.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.TextFormat):
                Optional. Data from Cloud Storage will be
                interpreted as text.

                This field is a member of `oneof`_ ``input_format``.
            avro_format (google.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.AvroFormat):
                Optional. Data from Cloud Storage will be
                interpreted in Avro format.

                This field is a member of `oneof`_ ``input_format``.
            pubsub_avro_format (google.pubsub_v1.types.IngestionDataSourceSettings.CloudStorage.PubSubAvroFormat):
                Optional. It will be assumed data from Cloud Storage was
                written via `Cloud Storage
                subscriptions <https://cloud.google.com/pubsub/docs/cloudstorage>`__.

                This field is a member of `oneof`_ ``input_format``.
            minimum_object_create_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. Only objects with a larger or equal
                creation timestamp will be ingested.
            match_glob (str):
                Optional. Glob pattern used to match objects that will be
                ingested. If unset, all objects will be ingested. See the
                `supported
                patterns <https://cloud.google.com/storage/docs/json_api/v1/objects/list#list-objects-and-prefixes-using-glob>`__.
        """

        class State(proto.Enum):
            r"""Possible states for ingestion from Cloud Storage.

            Values:
                STATE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ACTIVE (1):
                    Ingestion is active.
                CLOUD_STORAGE_PERMISSION_DENIED (2):
                    Permission denied encountered while calling the Cloud
                    Storage API. This can happen if the Pub/Sub SA has not been
                    granted the `appropriate
                    permissions <https://cloud.google.com/storage/docs/access-control/iam-permissions>`__:

                    - storage.objects.list: to list the objects in a bucket.
                    - storage.objects.get: to read the objects in a bucket.
                    - storage.buckets.get: to verify the bucket exists.
                PUBLISH_PERMISSION_DENIED (3):
                    Permission denied encountered while publishing to the topic.
                    This can happen if the Pub/Sub SA has not been granted the
                    `appropriate publish
                    permissions <https://cloud.google.com/pubsub/docs/access-control#pubsub.publisher>`__
                BUCKET_NOT_FOUND (4):
                    The provided Cloud Storage bucket doesn't
                    exist.
                TOO_MANY_OBJECTS (5):
                    The Cloud Storage bucket has too many
                    objects, ingestion will be paused.
                CONFLICTING_REGION_CONSTRAINTS (8):
                    Indicates an error state where the ingestion
                    source cannot be processed because the selected
                    ingestion region is not permitted by the
                    Regional Access Boundary (RAB) restrictions on
                    the project's service account.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            CLOUD_STORAGE_PERMISSION_DENIED = 2
            PUBLISH_PERMISSION_DENIED = 3
            BUCKET_NOT_FOUND = 4
            TOO_MANY_OBJECTS = 5
            CONFLICTING_REGION_CONSTRAINTS = 8

        class TextFormat(proto.Message):
            r"""Configuration for reading Cloud Storage data in text format. Each
            line of text as specified by the delimiter will be set to the
            ``data`` field of a Pub/Sub message.


            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                delimiter (str):
                    Optional. When unset, '\n' is used.

                    This field is a member of `oneof`_ ``_delimiter``.
            """

            delimiter: str = proto.Field(
                proto.STRING,
                number=1,
                optional=True,
            )

        class AvroFormat(proto.Message):
            r"""Configuration for reading Cloud Storage data in Avro binary format.
            The bytes of each object will be set to the ``data`` field of a
            Pub/Sub message.

            """

        class PubSubAvroFormat(proto.Message):
            r"""Configuration for reading Cloud Storage data written via `Cloud
            Storage
            subscriptions <https://cloud.google.com/pubsub/docs/cloudstorage>`__.
            The data and attributes fields of the originally exported Pub/Sub
            message will be restored when publishing.

            """

        state: "IngestionDataSourceSettings.CloudStorage.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="IngestionDataSourceSettings.CloudStorage.State",
        )
        bucket: str = proto.Field(
            proto.STRING,
            number=2,
        )
        text_format: "IngestionDataSourceSettings.CloudStorage.TextFormat" = (
            proto.Field(
                proto.MESSAGE,
                number=3,
                oneof="input_format",
                message="IngestionDataSourceSettings.CloudStorage.TextFormat",
            )
        )
        avro_format: "IngestionDataSourceSettings.CloudStorage.AvroFormat" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="input_format",
                message="IngestionDataSourceSettings.CloudStorage.AvroFormat",
            )
        )
        pubsub_avro_format: "IngestionDataSourceSettings.CloudStorage.PubSubAvroFormat" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="input_format",
            message="IngestionDataSourceSettings.CloudStorage.PubSubAvroFormat",
        )
        minimum_object_create_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=6,
            message=timestamp_pb2.Timestamp,
        )
        match_glob: str = proto.Field(
            proto.STRING,
            number=9,
        )

    class AzureEventHubs(proto.Message):
        r"""Ingestion settings for Azure Event Hubs.

        Attributes:
            state (google.pubsub_v1.types.IngestionDataSourceSettings.AzureEventHubs.State):
                Output only. An output-only field that
                indicates the state of the Event Hubs ingestion
                source.
            resource_group (str):
                Optional. Name of the resource group within
                the azure subscription.
            namespace (str):
                Optional. The name of the Event Hubs
                namespace.
            event_hub (str):
                Optional. The name of the Event Hub.
            client_id (str):
                Optional. The client id of the Azure
                application that is being used to authenticate
                Pub/Sub.
            tenant_id (str):
                Optional. The tenant id of the Azure
                application that is being used to authenticate
                Pub/Sub.
            subscription_id (str):
                Optional. The Azure subscription id.
            gcp_service_account (str):
                Optional. The GCP service account to be used
                for Federated Identity authentication.
        """

        class State(proto.Enum):
            r"""Possible states for managed ingestion from Event Hubs.

            Values:
                STATE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ACTIVE (1):
                    Ingestion is active.
                EVENT_HUBS_PERMISSION_DENIED (2):
                    Permission denied encountered while consuming data from
                    Event Hubs. This can happen when ``client_id``, or
                    ``tenant_id`` are invalid. Or the right permissions haven't
                    been granted.
                PUBLISH_PERMISSION_DENIED (3):
                    Permission denied encountered while
                    publishing to the topic.
                NAMESPACE_NOT_FOUND (4):
                    The provided Event Hubs namespace couldn't be
                    found.
                EVENT_HUB_NOT_FOUND (5):
                    The provided Event Hub couldn't be found.
                SUBSCRIPTION_NOT_FOUND (6):
                    The provided Event Hubs subscription couldn't
                    be found.
                RESOURCE_GROUP_NOT_FOUND (7):
                    The provided Event Hubs resource group
                    couldn't be found.
                CONFLICTING_REGION_CONSTRAINTS (8):
                    Indicates an error state where the ingestion
                    source cannot be processed because the selected
                    ingestion region is not permitted by the
                    Regional Access Boundary (RAB) restrictions on
                    the project's service account.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            EVENT_HUBS_PERMISSION_DENIED = 2
            PUBLISH_PERMISSION_DENIED = 3
            NAMESPACE_NOT_FOUND = 4
            EVENT_HUB_NOT_FOUND = 5
            SUBSCRIPTION_NOT_FOUND = 6
            RESOURCE_GROUP_NOT_FOUND = 7
            CONFLICTING_REGION_CONSTRAINTS = 8

        state: "IngestionDataSourceSettings.AzureEventHubs.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="IngestionDataSourceSettings.AzureEventHubs.State",
        )
        resource_group: str = proto.Field(
            proto.STRING,
            number=2,
        )
        namespace: str = proto.Field(
            proto.STRING,
            number=3,
        )
        event_hub: str = proto.Field(
            proto.STRING,
            number=4,
        )
        client_id: str = proto.Field(
            proto.STRING,
            number=5,
        )
        tenant_id: str = proto.Field(
            proto.STRING,
            number=6,
        )
        subscription_id: str = proto.Field(
            proto.STRING,
            number=7,
        )
        gcp_service_account: str = proto.Field(
            proto.STRING,
            number=8,
        )

    class AwsMsk(proto.Message):
        r"""Ingestion settings for Amazon MSK.

        Attributes:
            state (google.pubsub_v1.types.IngestionDataSourceSettings.AwsMsk.State):
                Output only. An output-only field that
                indicates the state of the Amazon MSK ingestion
                source.
            cluster_arn (str):
                Required. The Amazon Resource Name (ARN) that
                uniquely identifies the cluster.
            topic (str):
                Required. The name of the topic in the Amazon
                MSK cluster that Pub/Sub will import from.
            aws_role_arn (str):
                Required. AWS role ARN to be used for
                Federated Identity authentication with Amazon
                MSK. Check the Pub/Sub docs for how to set up
                this role and the required permissions that need
                to be attached to it.
            gcp_service_account (str):
                Required. The GCP service account to be used for Federated
                Identity authentication with Amazon MSK (via a
                ``AssumeRoleWithWebIdentity`` call for the provided role).
                The ``aws_role_arn`` must be set up with
                ``accounts.google.com:sub`` equals to this service account
                number.
        """

        class State(proto.Enum):
            r"""Possible states for managed ingestion from Amazon MSK.

            Values:
                STATE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ACTIVE (1):
                    Ingestion is active.
                MSK_PERMISSION_DENIED (2):
                    Permission denied encountered while consuming
                    data from Amazon MSK.
                PUBLISH_PERMISSION_DENIED (3):
                    Permission denied encountered while
                    publishing to the topic.
                CLUSTER_NOT_FOUND (4):
                    The provided MSK cluster wasn't found.
                TOPIC_NOT_FOUND (5):
                    The provided topic wasn't found.
                CONFLICTING_REGION_CONSTRAINTS (6):
                    Indicates an error state where the ingestion
                    source cannot be processed because the selected
                    ingestion region is not permitted by the
                    Regional Access Boundary (RAB) restrictions on
                    the project's service account.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            MSK_PERMISSION_DENIED = 2
            PUBLISH_PERMISSION_DENIED = 3
            CLUSTER_NOT_FOUND = 4
            TOPIC_NOT_FOUND = 5
            CONFLICTING_REGION_CONSTRAINTS = 6

        state: "IngestionDataSourceSettings.AwsMsk.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="IngestionDataSourceSettings.AwsMsk.State",
        )
        cluster_arn: str = proto.Field(
            proto.STRING,
            number=2,
        )
        topic: str = proto.Field(
            proto.STRING,
            number=3,
        )
        aws_role_arn: str = proto.Field(
            proto.STRING,
            number=4,
        )
        gcp_service_account: str = proto.Field(
            proto.STRING,
            number=5,
        )

    class ConfluentCloud(proto.Message):
        r"""Ingestion settings for Confluent Cloud.

        Attributes:
            state (google.pubsub_v1.types.IngestionDataSourceSettings.ConfluentCloud.State):
                Output only. An output-only field that
                indicates the state of the Confluent Cloud
                ingestion source.
            bootstrap_server (str):
                Required. The address of the bootstrap
                server. The format is url:port.
            cluster_id (str):
                Required. The id of the cluster.
            topic (str):
                Required. The name of the topic in the
                Confluent Cloud cluster that Pub/Sub will import
                from.
            identity_pool_id (str):
                Required. The id of the identity pool to be
                used for Federated Identity authentication with
                Confluent Cloud. See
                https://docs.confluent.io/cloud/current/security/authenticate/workload-identities/identity-providers/oauth/identity-pools.html#add-oauth-identity-pools.
            gcp_service_account (str):
                Required. The GCP service account to be used for Federated
                Identity authentication with ``identity_pool_id``.
        """

        class State(proto.Enum):
            r"""Possible states for managed ingestion from Confluent Cloud.

            Values:
                STATE_UNSPECIFIED (0):
                    Default value. This value is unused.
                ACTIVE (1):
                    Ingestion is active.
                CONFLUENT_CLOUD_PERMISSION_DENIED (2):
                    Permission denied encountered while consuming
                    data from Confluent Cloud.
                PUBLISH_PERMISSION_DENIED (3):
                    Permission denied encountered while
                    publishing to the topic.
                UNREACHABLE_BOOTSTRAP_SERVER (4):
                    The provided bootstrap server address is
                    unreachable.
                CLUSTER_NOT_FOUND (5):
                    The provided cluster wasn't found.
                TOPIC_NOT_FOUND (6):
                    The provided topic wasn't found.
                CONFLICTING_REGION_CONSTRAINTS (7):
                    Indicates an error state where the ingestion
                    source cannot be processed because the selected
                    ingestion region is not permitted by the
                    Regional Access Boundary (RAB) restrictions on
                    the project's service account.
            """

            STATE_UNSPECIFIED = 0
            ACTIVE = 1
            CONFLUENT_CLOUD_PERMISSION_DENIED = 2
            PUBLISH_PERMISSION_DENIED = 3
            UNREACHABLE_BOOTSTRAP_SERVER = 4
            CLUSTER_NOT_FOUND = 5
            TOPIC_NOT_FOUND = 6
            CONFLICTING_REGION_CONSTRAINTS = 7

        state: "IngestionDataSourceSettings.ConfluentCloud.State" = proto.Field(
            proto.ENUM,
            number=1,
            enum="IngestionDataSourceSettings.ConfluentCloud.State",
        )
        bootstrap_server: str = proto.Field(
            proto.STRING,
            number=2,
        )
        cluster_id: str = proto.Field(
            proto.STRING,
            number=3,
        )
        topic: str = proto.Field(
            proto.STRING,
            number=4,
        )
        identity_pool_id: str = proto.Field(
            proto.STRING,
            number=5,
        )
        gcp_service_account: str = proto.Field(
            proto.STRING,
            number=6,
        )

    aws_kinesis: AwsKinesis = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="source",
        message=AwsKinesis,
    )
    cloud_storage: CloudStorage = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message=CloudStorage,
    )
    azure_event_hubs: AzureEventHubs = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message=AzureEventHubs,
    )
    aws_msk: AwsMsk = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="source",
        message=AwsMsk,
    )
    confluent_cloud: ConfluentCloud = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="source",
        message=ConfluentCloud,
    )
    platform_logs_settings: "PlatformLogsSettings" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PlatformLogsSettings",
    )


class PlatformLogsSettings(proto.Message):
    r"""Settings for Platform Logs produced by Pub/Sub.

    Attributes:
        severity (google.pubsub_v1.types.PlatformLogsSettings.Severity):
            Optional. The minimum severity level of
            Platform Logs that will be written.
    """

    class Severity(proto.Enum):
        r"""Severity levels of Platform Logs.

        Values:
            SEVERITY_UNSPECIFIED (0):
                Default value. Logs level is unspecified.
                Logs will be disabled.
            DISABLED (1):
                Logs will be disabled.
            DEBUG (2):
                Debug logs and higher-severity logs will be
                written.
            INFO (3):
                Info logs and higher-severity logs will be
                written.
            WARNING (4):
                Warning logs and higher-severity logs will be
                written.
            ERROR (5):
                Only error logs will be written.
        """

        SEVERITY_UNSPECIFIED = 0
        DISABLED = 1
        DEBUG = 2
        INFO = 3
        WARNING = 4
        ERROR = 5

    severity: Severity = proto.Field(
        proto.ENUM,
        number=1,
        enum=Severity,
    )


class IngestionFailureEvent(proto.Message):
    r"""Payload of the Platform Log entry sent when a failure is
    encountered while ingesting.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        topic (str):
            Required. Name of the import topic. Format is:
            projects/{project_name}/topics/{topic_name}.
        error_message (str):
            Required. Error details explaining why
            ingestion to Pub/Sub has failed.
        cloud_storage_failure (google.pubsub_v1.types.IngestionFailureEvent.CloudStorageFailure):
            Optional. Failure when ingesting from Cloud
            Storage.

            This field is a member of `oneof`_ ``failure``.
        aws_msk_failure (google.pubsub_v1.types.IngestionFailureEvent.AwsMskFailureReason):
            Optional. Failure when ingesting from Amazon
            MSK.

            This field is a member of `oneof`_ ``failure``.
        azure_event_hubs_failure (google.pubsub_v1.types.IngestionFailureEvent.AzureEventHubsFailureReason):
            Optional. Failure when ingesting from Azure
            Event Hubs.

            This field is a member of `oneof`_ ``failure``.
        confluent_cloud_failure (google.pubsub_v1.types.IngestionFailureEvent.ConfluentCloudFailureReason):
            Optional. Failure when ingesting from
            Confluent Cloud.

            This field is a member of `oneof`_ ``failure``.
        aws_kinesis_failure (google.pubsub_v1.types.IngestionFailureEvent.AwsKinesisFailureReason):
            Optional. Failure when ingesting from AWS
            Kinesis.

            This field is a member of `oneof`_ ``failure``.
    """

    class ApiViolationReason(proto.Message):
        r"""Specifies the reason why some data may have been left out of the
        desired Pub/Sub message due to the API message limits
        (https://cloud.google.com/pubsub/quotas#resource_limits). For
        example, when the number of attributes is larger than 100, the
        number of attributes is truncated to 100 to respect the limit on the
        attribute count. Other attribute limits are treated similarly. When
        the size of the desired message would've been larger than 10MB, the
        message won't be published at all, and ingestion of the subsequent
        messages will proceed as normal.

        """

    class AvroFailureReason(proto.Message):
        r"""Set when an Avro file is unsupported or its format is not
        valid. When this occurs, one or more Avro objects won't be
        ingested.

        """

    class SchemaViolationReason(proto.Message):
        r"""Set when a Pub/Sub message fails to get published due to a
        schema validation violation.

        """

    class MessageTransformationFailureReason(proto.Message):
        r"""Set when a Pub/Sub message fails to get published due to a
        message transformation error.

        """

    class CloudStorageFailure(proto.Message):
        r"""Failure when ingesting from a Cloud Storage source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            bucket (str):
                Optional. Name of the Cloud Storage bucket
                used for ingestion.
            object_name (str):
                Optional. Name of the Cloud Storage object
                which contained the section that couldn't be
                ingested.
            object_generation (int):
                Optional. Generation of the Cloud Storage
                object which contained the section that couldn't
                be ingested.
            avro_failure_reason (google.pubsub_v1.types.IngestionFailureEvent.AvroFailureReason):
                Optional. Failure encountered when parsing an
                Avro file.

                This field is a member of `oneof`_ ``reason``.
            api_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.ApiViolationReason):
                Optional. The Pub/Sub API limits prevented
                the desired message from being published.

                This field is a member of `oneof`_ ``reason``.
            schema_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.SchemaViolationReason):
                Optional. The Pub/Sub message failed schema
                validation.

                This field is a member of `oneof`_ ``reason``.
            message_transformation_failure_reason (google.pubsub_v1.types.IngestionFailureEvent.MessageTransformationFailureReason):
                Optional. Failure encountered when applying a
                message transformation to the Pub/Sub message.

                This field is a member of `oneof`_ ``reason``.
        """

        bucket: str = proto.Field(
            proto.STRING,
            number=1,
        )
        object_name: str = proto.Field(
            proto.STRING,
            number=2,
        )
        object_generation: int = proto.Field(
            proto.INT64,
            number=3,
        )
        avro_failure_reason: "IngestionFailureEvent.AvroFailureReason" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="reason",
            message="IngestionFailureEvent.AvroFailureReason",
        )
        api_violation_reason: "IngestionFailureEvent.ApiViolationReason" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="reason",
            message="IngestionFailureEvent.ApiViolationReason",
        )
        schema_violation_reason: "IngestionFailureEvent.SchemaViolationReason" = (
            proto.Field(
                proto.MESSAGE,
                number=7,
                oneof="reason",
                message="IngestionFailureEvent.SchemaViolationReason",
            )
        )
        message_transformation_failure_reason: "IngestionFailureEvent.MessageTransformationFailureReason" = proto.Field(
            proto.MESSAGE,
            number=8,
            oneof="reason",
            message="IngestionFailureEvent.MessageTransformationFailureReason",
        )

    class AwsMskFailureReason(proto.Message):
        r"""Failure when ingesting from an Amazon MSK source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            cluster_arn (str):
                Optional. The ARN of the cluster of the topic
                being ingested from.
            kafka_topic (str):
                Optional. The name of the Kafka topic being
                ingested from.
            partition_id (int):
                Optional. The partition ID of the message
                that failed to be ingested.
            offset (int):
                Optional. The offset within the partition of
                the message that failed to be ingested.
            api_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.ApiViolationReason):
                Optional. The Pub/Sub API limits prevented
                the desired message from being published.

                This field is a member of `oneof`_ ``reason``.
            schema_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.SchemaViolationReason):
                Optional. The Pub/Sub message failed schema
                validation.

                This field is a member of `oneof`_ ``reason``.
            message_transformation_failure_reason (google.pubsub_v1.types.IngestionFailureEvent.MessageTransformationFailureReason):
                Optional. Failure encountered when applying a
                message transformation to the Pub/Sub message.

                This field is a member of `oneof`_ ``reason``.
        """

        cluster_arn: str = proto.Field(
            proto.STRING,
            number=1,
        )
        kafka_topic: str = proto.Field(
            proto.STRING,
            number=2,
        )
        partition_id: int = proto.Field(
            proto.INT64,
            number=3,
        )
        offset: int = proto.Field(
            proto.INT64,
            number=4,
        )
        api_violation_reason: "IngestionFailureEvent.ApiViolationReason" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="reason",
            message="IngestionFailureEvent.ApiViolationReason",
        )
        schema_violation_reason: "IngestionFailureEvent.SchemaViolationReason" = (
            proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="reason",
                message="IngestionFailureEvent.SchemaViolationReason",
            )
        )
        message_transformation_failure_reason: "IngestionFailureEvent.MessageTransformationFailureReason" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="reason",
            message="IngestionFailureEvent.MessageTransformationFailureReason",
        )

    class AzureEventHubsFailureReason(proto.Message):
        r"""Failure when ingesting from an Azure Event Hubs source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            namespace (str):
                Optional. The namespace containing the event
                hub being ingested from.
            event_hub (str):
                Optional. The name of the event hub being
                ingested from.
            partition_id (int):
                Optional. The partition ID of the message
                that failed to be ingested.
            offset (int):
                Optional. The offset within the partition of
                the message that failed to be ingested.
            api_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.ApiViolationReason):
                Optional. The Pub/Sub API limits prevented
                the desired message from being published.

                This field is a member of `oneof`_ ``reason``.
            schema_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.SchemaViolationReason):
                Optional. The Pub/Sub message failed schema
                validation.

                This field is a member of `oneof`_ ``reason``.
            message_transformation_failure_reason (google.pubsub_v1.types.IngestionFailureEvent.MessageTransformationFailureReason):
                Optional. Failure encountered when applying a
                message transformation to the Pub/Sub message.

                This field is a member of `oneof`_ ``reason``.
        """

        namespace: str = proto.Field(
            proto.STRING,
            number=1,
        )
        event_hub: str = proto.Field(
            proto.STRING,
            number=2,
        )
        partition_id: int = proto.Field(
            proto.INT64,
            number=3,
        )
        offset: int = proto.Field(
            proto.INT64,
            number=4,
        )
        api_violation_reason: "IngestionFailureEvent.ApiViolationReason" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="reason",
            message="IngestionFailureEvent.ApiViolationReason",
        )
        schema_violation_reason: "IngestionFailureEvent.SchemaViolationReason" = (
            proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="reason",
                message="IngestionFailureEvent.SchemaViolationReason",
            )
        )
        message_transformation_failure_reason: "IngestionFailureEvent.MessageTransformationFailureReason" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="reason",
            message="IngestionFailureEvent.MessageTransformationFailureReason",
        )

    class ConfluentCloudFailureReason(proto.Message):
        r"""Failure when ingesting from a Confluent Cloud source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            cluster_id (str):
                Optional. The cluster ID containing the topic
                being ingested from.
            kafka_topic (str):
                Optional. The name of the Kafka topic being
                ingested from.
            partition_id (int):
                Optional. The partition ID of the message
                that failed to be ingested.
            offset (int):
                Optional. The offset within the partition of
                the message that failed to be ingested.
            api_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.ApiViolationReason):
                Optional. The Pub/Sub API limits prevented
                the desired message from being published.

                This field is a member of `oneof`_ ``reason``.
            schema_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.SchemaViolationReason):
                Optional. The Pub/Sub message failed schema
                validation.

                This field is a member of `oneof`_ ``reason``.
            message_transformation_failure_reason (google.pubsub_v1.types.IngestionFailureEvent.MessageTransformationFailureReason):
                Optional. Failure encountered when applying a
                message transformation to the Pub/Sub message.

                This field is a member of `oneof`_ ``reason``.
        """

        cluster_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        kafka_topic: str = proto.Field(
            proto.STRING,
            number=2,
        )
        partition_id: int = proto.Field(
            proto.INT64,
            number=3,
        )
        offset: int = proto.Field(
            proto.INT64,
            number=4,
        )
        api_violation_reason: "IngestionFailureEvent.ApiViolationReason" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="reason",
            message="IngestionFailureEvent.ApiViolationReason",
        )
        schema_violation_reason: "IngestionFailureEvent.SchemaViolationReason" = (
            proto.Field(
                proto.MESSAGE,
                number=6,
                oneof="reason",
                message="IngestionFailureEvent.SchemaViolationReason",
            )
        )
        message_transformation_failure_reason: "IngestionFailureEvent.MessageTransformationFailureReason" = proto.Field(
            proto.MESSAGE,
            number=7,
            oneof="reason",
            message="IngestionFailureEvent.MessageTransformationFailureReason",
        )

    class AwsKinesisFailureReason(proto.Message):
        r"""Failure when ingesting from an AWS Kinesis source.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            stream_arn (str):
                Optional. The stream ARN of the Kinesis
                stream being ingested from.
            partition_key (str):
                Optional. The partition key of the message
                that failed to be ingested.
            sequence_number (str):
                Optional. The sequence number of the message
                that failed to be ingested.
            schema_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.SchemaViolationReason):
                Optional. The Pub/Sub message failed schema
                validation.

                This field is a member of `oneof`_ ``reason``.
            message_transformation_failure_reason (google.pubsub_v1.types.IngestionFailureEvent.MessageTransformationFailureReason):
                Optional. Failure encountered when applying a
                message transformation to the Pub/Sub message.

                This field is a member of `oneof`_ ``reason``.
            api_violation_reason (google.pubsub_v1.types.IngestionFailureEvent.ApiViolationReason):
                Optional. The message failed to be published
                due to an API violation. This is only set when
                the size of the data field of the Kinesis record
                is zero.

                This field is a member of `oneof`_ ``reason``.
        """

        stream_arn: str = proto.Field(
            proto.STRING,
            number=1,
        )
        partition_key: str = proto.Field(
            proto.STRING,
            number=2,
        )
        sequence_number: str = proto.Field(
            proto.STRING,
            number=3,
        )
        schema_violation_reason: "IngestionFailureEvent.SchemaViolationReason" = (
            proto.Field(
                proto.MESSAGE,
                number=4,
                oneof="reason",
                message="IngestionFailureEvent.SchemaViolationReason",
            )
        )
        message_transformation_failure_reason: "IngestionFailureEvent.MessageTransformationFailureReason" = proto.Field(
            proto.MESSAGE,
            number=5,
            oneof="reason",
            message="IngestionFailureEvent.MessageTransformationFailureReason",
        )
        api_violation_reason: "IngestionFailureEvent.ApiViolationReason" = proto.Field(
            proto.MESSAGE,
            number=6,
            oneof="reason",
            message="IngestionFailureEvent.ApiViolationReason",
        )

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    error_message: str = proto.Field(
        proto.STRING,
        number=2,
    )
    cloud_storage_failure: CloudStorageFailure = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="failure",
        message=CloudStorageFailure,
    )
    aws_msk_failure: AwsMskFailureReason = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="failure",
        message=AwsMskFailureReason,
    )
    azure_event_hubs_failure: AzureEventHubsFailureReason = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="failure",
        message=AzureEventHubsFailureReason,
    )
    confluent_cloud_failure: ConfluentCloudFailureReason = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="failure",
        message=ConfluentCloudFailureReason,
    )
    aws_kinesis_failure: AwsKinesisFailureReason = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="failure",
        message=AwsKinesisFailureReason,
    )


class JavaScriptUDF(proto.Message):
    r"""User-defined JavaScript function that can transform or filter
    a Pub/Sub message.

    Attributes:
        function_name (str):
            Required. Name of the JavasScript function
            that should applied to Pub/Sub messages.
        code (str):
            Required. JavaScript code that contains a function
            ``function_name`` with the below signature:

            ::

                 /**
                 * Transforms a Pub/Sub message.

                 * @return {(Object<string, (string | Object<string, string>)>|null)} - To
                 * filter a message, return `null`. To transform a message return a map
                 * with the following keys:
                 *   - (required) 'data' : {string}
                 *   - (optional) 'attributes' : {Object<string, string>}
                 * Returning empty `attributes` will remove all attributes from the
                 * message.
                 *
                 * @param  {(Object<string, (string | Object<string, string>)>} Pub/Sub
                 * message. Keys:
                 *   - (required) 'data' : {string}
                 *   - (required) 'attributes' : {Object<string, string>}
                 *
                 * @param  {Object<string, any>} metadata - Pub/Sub message metadata.
                 * Keys:
                 *   - (optional) 'message_id'  : {string}
                 *   - (optional) 'publish_time': {string} YYYY-MM-DDTHH:MM:SSZ format
                 *   - (optional) 'ordering_key': {string}
                 */

                 function <function_name>(message, metadata) {
                 }
    """

    function_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Compression(proto.Message):
    r"""Configuration for compressing/decompressing message data
    using a user-specified compression algorithm.

    Attributes:
        compression_algorithm (google.pubsub_v1.types.Compression.CompressionAlgorithm):
            Required. Specifies the compression algorithm
            to use.
        compression_mode (google.pubsub_v1.types.Compression.CompressionMode):
            Required. Specifies whether to compress or
            decompress the message.
    """

    class CompressionAlgorithm(proto.Enum):
        r"""The compression algorithm to use.

        Values:
            COMPRESSION_ALGORITHM_UNSPECIFIED (0):
                Unspecified algorithm.
            ZLIB (1):
                ZLIB compression.
        """

        COMPRESSION_ALGORITHM_UNSPECIFIED = 0
        ZLIB = 1

    class CompressionMode(proto.Enum):
        r"""The mode of the compression SMT.

        Values:
            COMPRESSION_MODE_UNSPECIFIED (0):
                Unspecified mode.
            COMPRESS (1):
                Compress.
            DECOMPRESS (2):
                Decompress.
        """

        COMPRESSION_MODE_UNSPECIFIED = 0
        COMPRESS = 1
        DECOMPRESS = 2

    compression_algorithm: CompressionAlgorithm = proto.Field(
        proto.ENUM,
        number=1,
        enum=CompressionAlgorithm,
    )
    compression_mode: CompressionMode = proto.Field(
        proto.ENUM,
        number=2,
        enum=CompressionMode,
    )


class AIInference(proto.Message):
    r"""Configuration for making inference requests against Vertex AI
    models.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        endpoint (str):
            Required. An endpoint to a Vertex AI model of the form
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
            or
            ``projects/{project}/locations/{location}/publishers/{publisher}/models/{model}``.
            Vertex AI API requests will be sent to this endpoint.
        unstructured_inference (google.pubsub_v1.types.AIInference.UnstructuredInference):
            Optional. Requests and responses can be any
            arbitrary JSON object.

            This field is a member of `oneof`_ ``inference_mode``.
        service_account_email (str):
            Optional. The service account to use to make prediction
            requests against endpoints. The resource creator or updater
            that specifies this field must have
            ``iam.serviceAccounts.actAs`` permission on the service
            account. If not specified, the Pub/Sub `service
            agent <https://cloud.google.com/iam/docs/service-agents>`__,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com,
            is used.
    """

    class UnstructuredInference(proto.Message):
        r"""Configuration for making inferences using arbitrary JSON
        payloads.

        Attributes:
            parameters (google.protobuf.struct_pb2.Struct):
                Optional. A parameters object to be included
                in each inference request. The parameters object
                is combined with the data field of the Pub/Sub
                message to form the inference request.
        """

        parameters: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=1,
            message=struct_pb2.Struct,
        )

    endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    unstructured_inference: UnstructuredInference = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="inference_mode",
        message=UnstructuredInference,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=3,
    )


class MessageTransform(proto.Message):
    r"""All supported message transforms types.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        javascript_udf (google.pubsub_v1.types.JavaScriptUDF):
            Optional. JavaScript User Defined Function. If multiple
            JavaScriptUDF's are specified on a resource, each must have
            a unique ``function_name``.

            This field is a member of `oneof`_ ``transform``.
        compression (google.pubsub_v1.types.Compression):
            Optional. Compression/Decompression.

            This field is a member of `oneof`_ ``transform``.
        ai_inference (google.pubsub_v1.types.AIInference):
            Optional. AI Inference. Specifies the Vertex
            AI endpoint that inference requests built from
            the Pub/Sub message data and provided parameters
            will be sent to.

            This field is a member of `oneof`_ ``transform``.
        enabled (bool):
            Optional. This field is deprecated, use the ``disabled``
            field to disable transforms.
        disabled (bool):
            Optional. If true, the transform is disabled and will not be
            applied to messages. Defaults to ``false``.
    """

    javascript_udf: "JavaScriptUDF" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="transform",
        message="JavaScriptUDF",
    )
    compression: "Compression" = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="transform",
        message="Compression",
    )
    ai_inference: "AIInference" = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="transform",
        message="AIInference",
    )
    enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class Topic(proto.Message):
    r"""A topic resource.

    Attributes:
        name (str):
            Required. Identifier. The name of the topic. It must have
            the format ``"projects/{project}/topics/{topic}"``.
            ``{topic}`` must start with a letter, and contain only
            letters (``[A-Za-z]``), numbers (``[0-9]``), dashes (``-``),
            underscores (``_``), periods (``.``), tildes (``~``), plus
            (``+``) or percent signs (``%``). It must be between 3 and
            255 characters in length, and it must not start with
            ``"goog"``.
        labels (MutableMapping[str, str]):
            Optional. See [Creating and managing labels]
            (https://cloud.google.com/pubsub/docs/labels).
        message_storage_policy (google.pubsub_v1.types.MessageStoragePolicy):
            Optional. Policy constraining the set of
            Google Cloud Platform regions where messages
            published to the topic may be stored. If not
            present, then no constraints are in effect.
        kms_key_name (str):
            Optional. The resource name of the Cloud KMS CryptoKey to be
            used to protect access to messages published on this topic.

            The expected format is
            ``projects/*/locations/*/keyRings/*/cryptoKeys/*``.
        schema_settings (google.pubsub_v1.types.SchemaSettings):
            Optional. Settings for validating messages
            published against a schema.
        satisfies_pzs (bool):
            Optional. Reserved for future use. This field
            is set only in responses from the server; it is
            ignored if it is set in any requests.
        message_retention_duration (google.protobuf.duration_pb2.Duration):
            Optional. Indicates the minimum duration to retain a message
            after it is published to the topic. If this field is set,
            messages published to the topic in the last
            ``message_retention_duration`` are always available to
            subscribers. For instance, it allows any attached
            subscription to `seek to a
            timestamp <https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time>`__
            that is up to ``message_retention_duration`` in the past. If
            this field is not set, message retention is controlled by
            settings on individual subscriptions. Cannot be more than 31
            days or less than 10 minutes.
        state (google.pubsub_v1.types.Topic.State):
            Output only. An output-only field indicating
            the state of the topic.
        ingestion_data_source_settings (google.pubsub_v1.types.IngestionDataSourceSettings):
            Optional. Settings for ingestion from a data
            source into this topic.
        message_transforms (MutableSequence[google.pubsub_v1.types.MessageTransform]):
            Optional. Transforms to be applied to
            messages published to the topic. Transforms are
            applied in the order specified.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag keys/values directly
            bound to this resource. For example: "123/environment":
            "production", "123/costCenter": "marketing" See
            https://{$universe.dns_names.final_documentation_domain}/pubsub/docs/tags
            for more information on using tags with Pub/Sub resources.
    """

    class State(proto.Enum):
        r"""The state of the topic.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The topic does not have any persistent
                errors.
            INGESTION_RESOURCE_ERROR (2):
                Ingestion from the data source has
                encountered a permanent error. See the more
                detailed error state in the corresponding
                ingestion source configuration.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        INGESTION_RESOURCE_ERROR = 2

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    message_storage_policy: "MessageStoragePolicy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="MessageStoragePolicy",
    )
    kms_key_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    schema_settings: "SchemaSettings" = proto.Field(
        proto.MESSAGE,
        number=6,
        message="SchemaSettings",
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    message_retention_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    ingestion_data_source_settings: "IngestionDataSourceSettings" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="IngestionDataSourceSettings",
    )
    message_transforms: MutableSequence["MessageTransform"] = proto.RepeatedField(
        proto.MESSAGE,
        number=13,
        message="MessageTransform",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=14,
    )


class PubsubMessage(proto.Message):
    r"""A message that is published by publishers and consumed by
    subscribers. The message must contain either a non-empty data field
    or at least one attribute. Note that client libraries represent this
    object differently depending on the language. See the corresponding
    `client library
    documentation <https://cloud.google.com/pubsub/docs/reference/libraries>`__
    for more information. See [quotas and limits]
    (https://cloud.google.com/pubsub/quotas) for more information about
    message limits.

    Attributes:
        data (bytes):
            Optional. The message data field. If this
            field is empty, the message must contain at
            least one attribute.
        attributes (MutableMapping[str, str]):
            Optional. Attributes for this message. If
            this field is empty, the message must contain
            non-empty data. This can be used to filter
            messages on the subscription.
        message_id (str):
            ID of this message, assigned by the server when the message
            is published. Guaranteed to be unique within the topic. This
            value may be read by a subscriber that receives a
            ``PubsubMessage`` via a ``Pull`` call or a push delivery. It
            must not be populated by the publisher in a ``Publish``
            call.
        publish_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the message was published, populated by
            the server when it receives the ``Publish`` call. It must
            not be populated by the publisher in a ``Publish`` call.
        ordering_key (str):
            Optional. If non-empty, identifies related messages for
            which publish order should be respected. If a
            ``Subscription`` has ``enable_message_ordering`` set to
            ``true``, messages published with the same non-empty
            ``ordering_key`` value will be delivered to subscribers in
            the order in which they are received by the Pub/Sub system.
            All ``PubsubMessage``\ s published in a given
            ``PublishRequest`` must specify the same ``ordering_key``
            value. For more information, see `ordering
            messages <https://cloud.google.com/pubsub/docs/ordering>`__.
    """

    data: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    message_id: str = proto.Field(
        proto.STRING,
        number=3,
    )
    publish_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    ordering_key: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetTopicRequest(proto.Message):
    r"""Request for the GetTopic method.

    Attributes:
        topic (str):
            Required. The name of the topic to get. Format is
            ``projects/{project}/topics/{topic}``.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTopicRequest(proto.Message):
    r"""Request for the UpdateTopic method.

    Attributes:
        topic (google.pubsub_v1.types.Topic):
            Required. The updated topic object.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Indicates which fields in the provided topic to
            update. Must be specified and non-empty. Note that if
            ``update_mask`` contains "message_storage_policy" but the
            ``message_storage_policy`` is not set in the ``topic``
            provided above, then the updated value is determined by the
            policy configured at the project or organization level.
    """

    topic: "Topic" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Topic",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class PublishRequest(proto.Message):
    r"""Request for the Publish method.

    Attributes:
        topic (str):
            Required. The messages in the request will be published on
            this topic. Format is ``projects/{project}/topics/{topic}``.
        messages (MutableSequence[google.pubsub_v1.types.PubsubMessage]):
            Required. The messages to publish.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    messages: MutableSequence["PubsubMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="PubsubMessage",
    )


class PublishResponse(proto.Message):
    r"""Response for the ``Publish`` method.

    Attributes:
        message_ids (MutableSequence[str]):
            Optional. The server-assigned ID of each
            published message, in the same order as the
            messages in the request. IDs are guaranteed to
            be unique within the topic.
    """

    message_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class ListTopicsRequest(proto.Message):
    r"""Request for the ``ListTopics`` method.

    Attributes:
        project (str):
            Required. The name of the project in which to list topics.
            Format is ``projects/{project-id}``.
        page_size (int):
            Optional. Maximum number of topics to return.
        page_token (str):
            Optional. The value returned by the last
            ``ListTopicsResponse``; indicates that this is a
            continuation of a prior ``ListTopics`` call, and that the
            system should return the next page of data.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListTopicsResponse(proto.Message):
    r"""Response for the ``ListTopics`` method.

    Attributes:
        topics (MutableSequence[google.pubsub_v1.types.Topic]):
            Optional. The resulting topics.
        next_page_token (str):
            Optional. If not empty, indicates that there may be more
            topics that match the request; this value should be passed
            in a new ``ListTopicsRequest``.
    """

    @property
    def raw_page(self):
        return self

    topics: MutableSequence["Topic"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Topic",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTopicSubscriptionsRequest(proto.Message):
    r"""Request for the ``ListTopicSubscriptions`` method.

    Attributes:
        topic (str):
            Required. The name of the topic that subscriptions are
            attached to. Format is
            ``projects/{project}/topics/{topic}``.
        page_size (int):
            Optional. Maximum number of subscription
            names to return.
        page_token (str):
            Optional. The value returned by the last
            ``ListTopicSubscriptionsResponse``; indicates that this is a
            continuation of a prior ``ListTopicSubscriptions`` call, and
            that the system should return the next page of data.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListTopicSubscriptionsResponse(proto.Message):
    r"""Response for the ``ListTopicSubscriptions`` method.

    Attributes:
        subscriptions (MutableSequence[str]):
            Optional. The names of subscriptions attached
            to the topic specified in the request.
        next_page_token (str):
            Optional. If not empty, indicates that there may be more
            subscriptions that match the request; this value should be
            passed in a new ``ListTopicSubscriptionsRequest`` to get
            more subscriptions.
    """

    @property
    def raw_page(self):
        return self

    subscriptions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListTopicSnapshotsRequest(proto.Message):
    r"""Request for the ``ListTopicSnapshots`` method.

    Attributes:
        topic (str):
            Required. The name of the topic that snapshots are attached
            to. Format is ``projects/{project}/topics/{topic}``.
        page_size (int):
            Optional. Maximum number of snapshot names to
            return.
        page_token (str):
            Optional. The value returned by the last
            ``ListTopicSnapshotsResponse``; indicates that this is a
            continuation of a prior ``ListTopicSnapshots`` call, and
            that the system should return the next page of data.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListTopicSnapshotsResponse(proto.Message):
    r"""Response for the ``ListTopicSnapshots`` method.

    Attributes:
        snapshots (MutableSequence[str]):
            Optional. The names of the snapshots that
            match the request.
        next_page_token (str):
            Optional. If not empty, indicates that there may be more
            snapshots that match the request; this value should be
            passed in a new ``ListTopicSnapshotsRequest`` to get more
            snapshots.
    """

    @property
    def raw_page(self):
        return self

    snapshots: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteTopicRequest(proto.Message):
    r"""Request for the ``DeleteTopic`` method.

    Attributes:
        topic (str):
            Required. Name of the topic to delete. Format is
            ``projects/{project}/topics/{topic}``.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DetachSubscriptionRequest(proto.Message):
    r"""Request for the DetachSubscription method.

    Attributes:
        subscription (str):
            Required. The subscription to detach. Format is
            ``projects/{project}/subscriptions/{subscription}``.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DetachSubscriptionResponse(proto.Message):
    r"""Response for the DetachSubscription method.
    Reserved for future use.

    """


class Subscription(proto.Message):
    r"""A subscription resource. If none of ``push_config``,
    ``bigquery_config``, ``cloud_storage_config``, or
    ``bigtable_config`` is set, then the subscriber will pull and ack
    messages using API methods. At most one of these fields may be set.

    Attributes:
        name (str):
            Required. Identifier. The name of the subscription. It must
            have the format
            ``"projects/{project}/subscriptions/{subscription}"``.
            ``{subscription}`` must start with a letter, and contain
            only letters (``[A-Za-z]``), numbers (``[0-9]``), dashes
            (``-``), underscores (``_``), periods (``.``), tildes
            (``~``), plus (``+``) or percent signs (``%``). It must be
            between 3 and 255 characters in length, and it must not
            start with ``"goog"``.
        topic (str):
            Required. The name of the topic from which this subscription
            is receiving messages. Format is
            ``projects/{project}/topics/{topic}``. The value of this
            field will be ``_deleted-topic_`` if the topic has been
            deleted.
        push_config (google.pubsub_v1.types.PushConfig):
            Optional. If push delivery is used with this
            subscription, this field is used to configure
            it.
        bigquery_config (google.pubsub_v1.types.BigQueryConfig):
            Optional. If delivery to BigQuery is used
            with this subscription, this field is used to
            configure it.
        cloud_storage_config (google.pubsub_v1.types.CloudStorageConfig):
            Optional. If delivery to Google Cloud Storage
            is used with this subscription, this field is
            used to configure it.
        bigtable_config (google.pubsub_v1.types.BigtableConfig):
            Optional. If delivery to Bigtable is used
            with this subscription, this field is used to
            configure it.
        ack_deadline_seconds (int):
            Optional. The approximate amount of time (on a best-effort
            basis) Pub/Sub waits for the subscriber to acknowledge
            receipt before resending the message. In the interval after
            the message is delivered and before it is acknowledged, it
            is considered to be *outstanding*. During that time period,
            the message will not be redelivered (on a best-effort
            basis).

            For pull subscriptions, this value is used as the initial
            value for the ack deadline. To override this value for a
            given message, call ``ModifyAckDeadline`` with the
            corresponding ``ack_id`` if using non-streaming pull or send
            the ``ack_id`` in a ``StreamingModifyAckDeadlineRequest`` if
            using streaming pull. The minimum custom deadline you can
            specify is 10 seconds. The maximum custom deadline you can
            specify is 600 seconds (10 minutes). If this parameter is 0,
            a default value of 10 seconds is used.

            For push delivery, this value is also used to set the
            request timeout for the call to the push endpoint.

            If the subscriber never acknowledges the message, the
            Pub/Sub system will eventually redeliver the message.
        retain_acked_messages (bool):
            Optional. Indicates whether to retain acknowledged messages.
            If true, then messages are not expunged from the
            subscription's backlog, even if they are acknowledged, until
            they fall out of the ``message_retention_duration`` window.
            This must be true if you would like to [``Seek`` to a
            timestamp]
            (https://cloud.google.com/pubsub/docs/replay-overview#seek_to_a_time)
            in the past to replay previously-acknowledged messages.
        message_retention_duration (google.protobuf.duration_pb2.Duration):
            Optional. How long to retain unacknowledged messages in the
            subscription's backlog, from the moment a message is
            published. If ``retain_acked_messages`` is true, then this
            also configures the retention of acknowledged messages, and
            thus configures how far back in time a ``Seek`` can be done.
            Defaults to 7 days. Cannot be more than 31 days or less than
            10 minutes.
        labels (MutableMapping[str, str]):
            Optional. See `Creating and managing
            labels <https://cloud.google.com/pubsub/docs/labels>`__.
        enable_message_ordering (bool):
            Optional. If true, messages published with the same
            ``ordering_key`` in ``PubsubMessage`` will be delivered to
            the subscribers in the order in which they are received by
            the Pub/Sub system. Otherwise, they may be delivered in any
            order.
        expiration_policy (google.pubsub_v1.types.ExpirationPolicy):
            Optional. A policy that specifies the conditions for this
            subscription's expiration. A subscription is considered
            active as long as any connected subscriber is successfully
            consuming messages from the subscription or is issuing
            operations on the subscription. If ``expiration_policy`` is
            not set, a *default policy* with ``ttl`` of 31 days will be
            used. The minimum allowed value for
            ``expiration_policy.ttl`` is 1 day. If ``expiration_policy``
            is set, but ``expiration_policy.ttl`` is not set, the
            subscription never expires.
        filter (str):
            Optional. An expression written in the Pub/Sub `filter
            language <https://cloud.google.com/pubsub/docs/filtering>`__.
            If non-empty, then only ``PubsubMessage``\ s whose
            ``attributes`` field matches the filter are delivered on
            this subscription. If empty, then no messages are filtered
            out.
        dead_letter_policy (google.pubsub_v1.types.DeadLetterPolicy):
            Optional. A policy that specifies the conditions for dead
            lettering messages in this subscription. If
            dead_letter_policy is not set, dead lettering is disabled.

            The Pub/Sub service account associated with this
            subscriptions's parent project (i.e.,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com)
            must have permission to Acknowledge() messages on this
            subscription.
        retry_policy (google.pubsub_v1.types.RetryPolicy):
            Optional. A policy that specifies how Pub/Sub
            retries message delivery for this subscription.

            If not set, the default retry policy is applied.
            This generally implies that messages will be
            retried as soon as possible for healthy
            subscribers. RetryPolicy will be triggered on
            NACKs or acknowledgment deadline exceeded events
            for a given message.
        detached (bool):
            Optional. Indicates whether the subscription is detached
            from its topic. Detached subscriptions don't receive
            messages from their topic and don't retain any backlog.
            ``Pull`` and ``StreamingPull`` requests will return
            FAILED_PRECONDITION. If the subscription is a push
            subscription, pushes to the endpoint will not be made.
        enable_exactly_once_delivery (bool):
            Optional. If true, Pub/Sub provides the following guarantees
            for the delivery of a message with a given value of
            ``message_id`` on this subscription:

            - The message sent to a subscriber is guaranteed not to be
              resent before the message's acknowledgment deadline
              expires.
            - An acknowledged message will not be resent to a
              subscriber.

            Note that subscribers may still receive multiple copies of a
            message when ``enable_exactly_once_delivery`` is true if the
            message was published multiple times by a publisher client.
            These copies are considered distinct by Pub/Sub and have
            distinct ``message_id`` values.
        topic_message_retention_duration (google.protobuf.duration_pb2.Duration):
            Output only. Indicates the minimum duration for which a
            message is retained after it is published to the
            subscription's topic. If this field is set, messages
            published to the subscription's topic in the last
            ``topic_message_retention_duration`` are always available to
            subscribers. See the ``message_retention_duration`` field in
            ``Topic``. This field is set only in responses from the
            server; it is ignored if it is set in any requests.
        state (google.pubsub_v1.types.Subscription.State):
            Output only. An output-only field indicating
            whether or not the subscription can receive
            messages.
        analytics_hub_subscription_info (google.pubsub_v1.types.Subscription.AnalyticsHubSubscriptionInfo):
            Output only. Information about the associated
            Analytics Hub subscription. Only set if the
            subscription is created by Analytics Hub.
        message_transforms (MutableSequence[google.pubsub_v1.types.MessageTransform]):
            Optional. Transforms to be applied to
            messages before they are delivered to
            subscribers. Transforms are applied in the order
            specified.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag keys/values directly
            bound to this resource. For example: "123/environment":
            "production", "123/costCenter": "marketing" See
            https://{$universe.dns_names.final_documentation_domain}/pubsub/docs/tags
            for more information on using tags with Pub/Sub resources.
    """

    class State(proto.Enum):
        r"""Possible states for a subscription.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The subscription can actively receive
                messages
            RESOURCE_ERROR (2):
                The subscription cannot receive messages
                because of an error with the resource to which
                it pushes messages. See the more detailed error
                state in the corresponding configuration.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        RESOURCE_ERROR = 2

    class AnalyticsHubSubscriptionInfo(proto.Message):
        r"""Information about an associated `Analytics Hub
        subscription <https://cloud.google.com/bigquery/docs/analytics-hub-manage-subscriptions>`__.

        Attributes:
            listing (str):
                Optional. The name of the associated Analytics Hub listing
                resource. Pattern:
                "projects/{project}/locations/{location}/dataExchanges/{data_exchange}/listings/{listing}".
            subscription (str):
                Optional. The name of the associated
                Analytics Hub subscription resource. Pattern:

                "projects/{project}/locations/{location}/subscriptions/{subscription}".
        """

        listing: str = proto.Field(
            proto.STRING,
            number=1,
        )
        subscription: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    topic: str = proto.Field(
        proto.STRING,
        number=2,
    )
    push_config: "PushConfig" = proto.Field(
        proto.MESSAGE,
        number=4,
        message="PushConfig",
    )
    bigquery_config: "BigQueryConfig" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="BigQueryConfig",
    )
    cloud_storage_config: "CloudStorageConfig" = proto.Field(
        proto.MESSAGE,
        number=22,
        message="CloudStorageConfig",
    )
    bigtable_config: "BigtableConfig" = proto.Field(
        proto.MESSAGE,
        number=27,
        message="BigtableConfig",
    )
    ack_deadline_seconds: int = proto.Field(
        proto.INT32,
        number=5,
    )
    retain_acked_messages: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    message_retention_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=8,
        message=duration_pb2.Duration,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=9,
    )
    enable_message_ordering: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    expiration_policy: "ExpirationPolicy" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="ExpirationPolicy",
    )
    filter: str = proto.Field(
        proto.STRING,
        number=12,
    )
    dead_letter_policy: "DeadLetterPolicy" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="DeadLetterPolicy",
    )
    retry_policy: "RetryPolicy" = proto.Field(
        proto.MESSAGE,
        number=14,
        message="RetryPolicy",
    )
    detached: bool = proto.Field(
        proto.BOOL,
        number=15,
    )
    enable_exactly_once_delivery: bool = proto.Field(
        proto.BOOL,
        number=16,
    )
    topic_message_retention_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=17,
        message=duration_pb2.Duration,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=19,
        enum=State,
    )
    analytics_hub_subscription_info: AnalyticsHubSubscriptionInfo = proto.Field(
        proto.MESSAGE,
        number=23,
        message=AnalyticsHubSubscriptionInfo,
    )
    message_transforms: MutableSequence["MessageTransform"] = proto.RepeatedField(
        proto.MESSAGE,
        number=25,
        message="MessageTransform",
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=26,
    )


class RetryPolicy(proto.Message):
    r"""A policy that specifies how Pub/Sub retries message delivery.

    Retry delay will be exponential based on provided minimum and
    maximum backoffs. https://en.wikipedia.org/wiki/Exponential_backoff.

    RetryPolicy will be triggered on NACKs or acknowledgment deadline
    exceeded events for a given message.

    Retry Policy is implemented on a best effort basis. At times, the
    delay between consecutive deliveries may not match the
    configuration. That is, delay can be more or less than configured
    backoff.

    Attributes:
        minimum_backoff (google.protobuf.duration_pb2.Duration):
            Optional. The minimum delay between
            consecutive deliveries of a given message. Value
            should be between 0 and 600 seconds. Defaults to
            10 seconds.
        maximum_backoff (google.protobuf.duration_pb2.Duration):
            Optional. The maximum delay between
            consecutive deliveries of a given message. Value
            should be between 0 and 600 seconds. Defaults to
            600 seconds.
    """

    minimum_backoff: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )
    maximum_backoff: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=2,
        message=duration_pb2.Duration,
    )


class DeadLetterPolicy(proto.Message):
    r"""Dead lettering is done on a best effort basis. The same
    message might be dead lettered multiple times.

    If validation on any of the fields fails at subscription
    creation/updation, the create/update subscription request will
    fail.

    Attributes:
        dead_letter_topic (str):
            Optional. The name of the topic to which dead letter
            messages should be published. Format is
            ``projects/{project}/topics/{topic}``.The Pub/Sub service
            account associated with the enclosing subscription's parent
            project (i.e.,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com)
            must have permission to Publish() to this topic.

            The operation will fail if the topic does not exist. Users
            should ensure that there is a subscription attached to this
            topic since messages published to a topic with no
            subscriptions are lost.
        max_delivery_attempts (int):
            Optional. The maximum number of delivery attempts for any
            message. The value must be between 5 and 100.

            The number of delivery attempts is defined as 1 + (the sum
            of number of NACKs and number of times the acknowledgment
            deadline has been exceeded for the message).

            A NACK is any call to ModifyAckDeadline with a 0 deadline.
            Note that client libraries may automatically extend
            ack_deadlines.

            This field will be honored on a best effort basis.

            If this parameter is 0, a default value of 5 is used.
    """

    dead_letter_topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    max_delivery_attempts: int = proto.Field(
        proto.INT32,
        number=2,
    )


class ExpirationPolicy(proto.Message):
    r"""A policy that specifies the conditions for resource
    expiration (i.e., automatic resource deletion).

    Attributes:
        ttl (google.protobuf.duration_pb2.Duration):
            Optional. Specifies the "time-to-live" duration for an
            associated resource. The resource expires if it is not
            active for a period of ``ttl``. The definition of "activity"
            depends on the type of the associated resource. The minimum
            and maximum allowed values for ``ttl`` depend on the type of
            the associated resource, as well. If ``ttl`` is not set, the
            associated resource never expires.
    """

    ttl: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=1,
        message=duration_pb2.Duration,
    )


class PushConfig(proto.Message):
    r"""Configuration for a push delivery endpoint.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        push_endpoint (str):
            Optional. A URL locating the endpoint to which messages
            should be pushed. For example, a Webhook endpoint might use
            ``https://example.com/push``.
        attributes (MutableMapping[str, str]):
            Optional. Endpoint configuration attributes that can be used
            to control different aspects of the message delivery.

            The only currently supported attribute is
            ``x-goog-version``, which you can use to change the format
            of the pushed message. This attribute indicates the version
            of the data expected by the endpoint. This controls the
            shape of the pushed message (i.e., its fields and metadata).

            If not present during the ``CreateSubscription`` call, it
            will default to the version of the Pub/Sub API used to make
            such call. If not present in a ``ModifyPushConfig`` call,
            its value will not be changed. ``GetSubscription`` calls
            will always return a valid version, even if the subscription
            was created without this attribute.

            The only supported values for the ``x-goog-version``
            attribute are:

            - ``v1beta1``: uses the push format defined in the v1beta1
              Pub/Sub API.
            - ``v1`` or ``v1beta2``: uses the push format defined in the
              v1 Pub/Sub API.

            For example: ``attributes { "x-goog-version": "v1" }``
        oidc_token (google.pubsub_v1.types.PushConfig.OidcToken):
            Optional. If specified, Pub/Sub will generate and attach an
            OIDC JWT token as an ``Authorization`` header in the HTTP
            request for every pushed message.

            This field is a member of `oneof`_ ``authentication_method``.
        pubsub_wrapper (google.pubsub_v1.types.PushConfig.PubsubWrapper):
            Optional. When set, the payload to the push
            endpoint is in the form of the JSON
            representation of a PubsubMessage
            (https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage).

            This field is a member of `oneof`_ ``wrapper``.
        no_wrapper (google.pubsub_v1.types.PushConfig.NoWrapper):
            Optional. When set, the payload to the push
            endpoint is not wrapped.

            This field is a member of `oneof`_ ``wrapper``.
    """

    class OidcToken(proto.Message):
        r"""Contains information needed for generating an `OpenID Connect
        token <https://developers.google.com/identity/protocols/OpenIDConnect>`__.

        Attributes:
            service_account_email (str):
                Optional. `Service account
                email <https://cloud.google.com/iam/docs/service-accounts>`__
                used for generating the OIDC token. For more information on
                setting up authentication, see `Push
                subscriptions <https://cloud.google.com/pubsub/docs/push>`__.
            audience (str):
                Optional. Audience to be used when generating
                OIDC token. The audience claim identifies the
                recipients that the JWT is intended for. The
                audience value is a single case-sensitive
                string. Having multiple values (array) for the
                audience field is not supported. More info about
                the OIDC JWT token audience here:

                https://tools.ietf.org/html/rfc7519#section-4.1.3
                Note: if not specified, the Push endpoint URL
                will be used.
        """

        service_account_email: str = proto.Field(
            proto.STRING,
            number=1,
        )
        audience: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class PubsubWrapper(proto.Message):
        r"""The payload to the push endpoint is in the form of the JSON
        representation of a PubsubMessage
        (https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage).

        """

    class NoWrapper(proto.Message):
        r"""Sets the ``data`` field as the HTTP body for delivery.

        Attributes:
            write_metadata (bool):
                Optional. When true, writes the Pub/Sub message metadata to
                ``x-goog-pubsub-<KEY>:<VAL>`` headers of the HTTP request.
                Writes the Pub/Sub message attributes to ``<KEY>:<VAL>``
                headers of the HTTP request.
        """

        write_metadata: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    push_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    oidc_token: OidcToken = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="authentication_method",
        message=OidcToken,
    )
    pubsub_wrapper: PubsubWrapper = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="wrapper",
        message=PubsubWrapper,
    )
    no_wrapper: NoWrapper = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="wrapper",
        message=NoWrapper,
    )


class BigQueryConfig(proto.Message):
    r"""Configuration for a BigQuery subscription.

    Attributes:
        table (str):
            Optional. The name of the table to which to
            write data, of the form
            {projectId}.{datasetId}.{tableId}
        use_topic_schema (bool):
            Optional. When true, use the topic's schema as the columns
            to write to in BigQuery, if it exists. ``use_topic_schema``
            and ``use_table_schema`` cannot be enabled at the same time.
        write_metadata (bool):
            Optional. When true, write the subscription name,
            message_id, publish_time, attributes, and ordering_key to
            additional columns in the table. The subscription name,
            message_id, and publish_time fields are put in their own
            columns while all other message properties (other than data)
            are written to a JSON object in the attributes column.
        drop_unknown_fields (bool):
            Optional. If true and ``use_topic_schema`` is true, drops
            any fields that are part of the topic schema that are not
            part of the BigQuery table schema when writing to BigQuery.
            Otherwise, the schemas must be kept in sync and any messages
            with extra fields are not written and remain in the
            subscription's backlog. If true and ``use_table_schema`` is
            true, drops any fields in the message that are not part of
            the BigQuery table schema when writing to BigQuery.
            Otherwise, the write to BigQuery will fail.
        state (google.pubsub_v1.types.BigQueryConfig.State):
            Output only. An output-only field that
            indicates whether or not the subscription can
            receive messages.
        use_table_schema (bool):
            Optional. When true, use the BigQuery table's schema as the
            columns to write to in BigQuery. ``use_table_schema`` and
            ``use_topic_schema`` cannot be enabled at the same time.
        service_account_email (str):
            Optional. The service account to use to write to BigQuery.
            The subscription creator or updater that specifies this
            field must have ``iam.serviceAccounts.actAs`` permission on
            the service account. If not specified, the Pub/Sub `service
            agent <https://cloud.google.com/iam/docs/service-agents>`__,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com,
            is used.
    """

    class State(proto.Enum):
        r"""Possible states for a BigQuery subscription.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The subscription can actively send messages
                to BigQuery
            PERMISSION_DENIED (2):
                Cannot write to the BigQuery table because of permission
                denied errors. This can happen if

                - Pub/Sub SA has not been granted the `appropriate BigQuery
                  IAM
                  permissions <https://cloud.google.com/pubsub/docs/create-subscription#assign_bigquery_service_account>`__
                - bigquery.googleapis.com API is not enabled for the project
                  (`instructions <https://cloud.google.com/service-usage/docs/enable-disable>`__)
            NOT_FOUND (3):
                Cannot write to the BigQuery table because it
                does not exist.
            SCHEMA_MISMATCH (4):
                Cannot write to the BigQuery table due to a
                schema mismatch.
            IN_TRANSIT_LOCATION_RESTRICTION (5):
                Cannot write to the destination because enforce_in_transit
                is set to true and the destination locations are not in the
                allowed regions.
            VERTEX_AI_LOCATION_RESTRICTION (6):
                Cannot write to the BigQuery table because the table is not
                in the same location as where Vertex AI models used in
                ``message_transform``\ s are deployed.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        PERMISSION_DENIED = 2
        NOT_FOUND = 3
        SCHEMA_MISMATCH = 4
        IN_TRANSIT_LOCATION_RESTRICTION = 5
        VERTEX_AI_LOCATION_RESTRICTION = 6

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    use_topic_schema: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    write_metadata: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    drop_unknown_fields: bool = proto.Field(
        proto.BOOL,
        number=4,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=5,
        enum=State,
    )
    use_table_schema: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=7,
    )


class BigtableConfig(proto.Message):
    r"""Configuration for a Bigtable subscription, which will write a
    Pub/Sub message to a Bigtable row. See the ColumnFamilyMapping
    documentation below for details on how the row keys and columns
    will be written.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        table (str):
            Optional. The unique name of the table to write messages to.

            Values are of the form
            ``projects/<project>/instances/<instance>/tables/<table>``.
        app_profile_id (str):
            Optional. The app profile to use for the
            Bigtable writes. If not specified, the "default"
            application profile will be used. The app
            profile must use single-cluster routing.
        service_account_email (str):
            Optional. The service account to use to write to Bigtable.
            The subscription creator or updater that specifies this
            field must have ``iam.serviceAccounts.actAs`` permission on
            the service account. If not specified, the Pub/Sub `service
            agent <https://cloud.google.com/iam/docs/service-agents>`__,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com,
            is used.
        write_metadata (bool):
            Optional. When true, write the subscription name,
            message_id, publish_time, attributes, and ordering_key to
            additional columns in the table under the pubsub_metadata
            column family. The subscription name, message_id, and
            publish_time fields are put in their own columns while all
            other message properties (other than data) are written to a
            JSON object in the attributes column.
        column_family_mapping (google.pubsub_v1.types.BigtableConfig.ColumnFamilyMapping):
            Optional. Configuration that allows writing
            row keys and/or columns based on fields in the
            input message. The input message format must be
            JSON if this field is set.

            This field is a member of `oneof`_ ``message_mapping``.
        state (google.pubsub_v1.types.BigtableConfig.State):
            Output only. An output-only field that
            indicates whether or not the subscription can
            receive messages.
    """

    class State(proto.Enum):
        r"""Possible states for a Bigtable subscription.
        Note: more states could be added in the future. Please code
        accordingly.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The subscription can actively send messages
                to Bigtable.
            NOT_FOUND (2):
                Unused in the current implementation.
                Placeholder for future use.
            APP_PROFILE_MISCONFIGURED (3):
                Unused in the current implementation.
                Placeholder for future use.
            PERMISSION_DENIED (4):
                Cannot write to Bigtable because of permission denied
                errors. This can happen if:

                - The Bigtable instance, table, or app profile does not
                  exist.
                - The Pub/Sub service agent has not been granted the
                  `appropriate Bigtable IAM permission
                  bigtable.tables.mutateRows <{$universe.dns_names.final_documentation_domain}/bigtable/docs/access-control#permissions>`__
                - The bigtable.googleapis.com API is not enabled for the
                  project
                  (`instructions <{$universe.dns_names.final_documentation_domain}/service-usage/docs/enable-disable>`__)
            SCHEMA_MISMATCH (5):
                Cannot write to Bigtable because of a missing column family
                (``data``), or if there is no structured row key for the
                subscription name + message ID, if because the app profile
                is not configured for single-cluster routing.
            IN_TRANSIT_LOCATION_RESTRICTION (6):
                Cannot write to the destination because enforce_in_transit
                is set to true and the destination locations are not in the
                allowed regions.
            VERTEX_AI_LOCATION_RESTRICTION (7):
                Cannot write to Bigtable because the table is not in the
                same location as where Vertex AI models used in
                ``message_transform``\ s are deployed.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        NOT_FOUND = 2
        APP_PROFILE_MISCONFIGURED = 3
        PERMISSION_DENIED = 4
        SCHEMA_MISMATCH = 5
        IN_TRANSIT_LOCATION_RESTRICTION = 6
        VERTEX_AI_LOCATION_RESTRICTION = 7

    class ColumnFamilyMapping(proto.Message):
        r"""Configuration for writing a Pub/Sub message to a Bigtable row with a
        user-defined key and writing to column families.

        If this field is set:

        - The subscription messages must be formatted as JSON.
        - The row key mapping is configured in the ``key_definition``
          section.
        - The top-level fields will be written either:

          - By default, they will be written to the ``data`` column family
            with the field name as the column qualifier.
          - But if the field name matches an existing column family (except
            for the default ``data`` column), then that field will be
            written to that column family, either as a scalar or its next
            level nested fields if it's a JSON object.

        - The cell timestamp will be the message publish timestamp.

        If the field is not set, the default behavior is to write:

        - row key: subscription name, message ID hash, and message ID
          delimited by ``#``.
        - columns: message bytes written to a single column family ``data``
          with an empty-string column qualifier.
        - cell timestamp: the message publish timestamp.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            row_key_schema (google.pubsub_v1.types.BigtableConfig.ColumnFamilyMapping.RowKeySchema):
                Optional. If set, the row key is constructed from the field
                names of the table's structured row key
                ({$universe.dns_names.final_documentation_domain}/bigtable/docs/manage-row-key-schemas).
                Note that if the field is nullable in the structured row
                key, then it need not be present in the message; null will
                be used instead.

                This field is a member of `oneof`_ ``key_definition``.
            delimited_key (google.pubsub_v1.types.BigtableConfig.ColumnFamilyMapping.DelimitedKey):
                Optional. If set, the row key is constructed
                from the given key fields and delimiter. All key
                fields must be present in the message;
                otherwise, the message remains in the
                subscription backlog.

                This field is a member of `oneof`_ ``key_definition``.
        """

        class RowKeySchema(proto.Message):
            r"""Row key definition that reads the input message fields based on the
            field names of the table's structured row key
            ({$universe.dns_names.final_documentation_domain}/bigtable/docs/manage-row-key-schemas).
            Note that if the field is nullable in the structured row key, then
            it need not be present in the message; null will be used instead.

            """

        class DelimitedKey(proto.Message):
            r"""Row key definition based on fields from the message.

            Attributes:
                key_fields (MutableSequence[str]):
                    Required. The key fields to construct from
                    the row key. The fields must be present in the
                    message as a top-level field, i.e. JSON path
                    expressions will not traverse into nested
                    objects.
                delimiter (bytes):
                    Optional. Byte sequence used to delimit
                    concatenated fields. Must be specified if
                    multiple key fields are used. The delimiter must
                    contain at least 1 character and at most 50
                    characters.
            """

            key_fields: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )
            delimiter: bytes = proto.Field(
                proto.BYTES,
                number=2,
            )

        row_key_schema: "BigtableConfig.ColumnFamilyMapping.RowKeySchema" = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="key_definition",
            message="BigtableConfig.ColumnFamilyMapping.RowKeySchema",
        )
        delimited_key: "BigtableConfig.ColumnFamilyMapping.DelimitedKey" = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="key_definition",
            message="BigtableConfig.ColumnFamilyMapping.DelimitedKey",
        )

    table: str = proto.Field(
        proto.STRING,
        number=1,
    )
    app_profile_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=3,
    )
    write_metadata: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    column_family_mapping: ColumnFamilyMapping = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="message_mapping",
        message=ColumnFamilyMapping,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=4,
        enum=State,
    )


class CloudStorageConfig(proto.Message):
    r"""Configuration for a Cloud Storage subscription.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        bucket (str):
            Required. User-provided name for the Cloud Storage bucket.
            The bucket must be created by the user. The bucket name must
            be without any prefix like "gs://". See the [bucket naming
            requirements]
            (https://cloud.google.com/storage/docs/buckets#naming).
        filename_prefix (str):
            Optional. User-provided prefix for Cloud Storage filename.
            See the `object naming
            requirements <https://cloud.google.com/storage/docs/objects#naming>`__.
        filename_suffix (str):
            Optional. User-provided suffix for Cloud Storage filename.
            See the `object naming
            requirements <https://cloud.google.com/storage/docs/objects#naming>`__.
            Must not end in "/".
        filename_datetime_format (str):
            Optional. User-provided format string specifying how to
            represent datetimes in Cloud Storage filenames. See the
            `datetime format
            guidance <https://cloud.google.com/pubsub/docs/create-cloudstorage-subscription#file_names>`__.
        text_config (google.pubsub_v1.types.CloudStorageConfig.TextConfig):
            Optional. If set, message data will be
            written to Cloud Storage in text format.

            This field is a member of `oneof`_ ``output_format``.
        avro_config (google.pubsub_v1.types.CloudStorageConfig.AvroConfig):
            Optional. If set, message data will be
            written to Cloud Storage in Avro format.

            This field is a member of `oneof`_ ``output_format``.
        max_duration (google.protobuf.duration_pb2.Duration):
            Optional. The maximum duration that can
            elapse before a new Cloud Storage file is
            created. Min 1 minute, max 10 minutes, default 5
            minutes. May not exceed the subscription's
            acknowledgment deadline.
        max_bytes (int):
            Optional. The maximum bytes that can be written to a Cloud
            Storage file before a new file is created. Min 1 KB, max 10
            GiB. The max_bytes limit may be exceeded in cases where
            messages are larger than the limit.
        max_messages (int):
            Optional. The maximum number of messages that
            can be written to a Cloud Storage file before a
            new file is created. Min 1000 messages.
        state (google.pubsub_v1.types.CloudStorageConfig.State):
            Output only. An output-only field that
            indicates whether or not the subscription can
            receive messages.
        service_account_email (str):
            Optional. The service account to use to write to Cloud
            Storage. The subscription creator or updater that specifies
            this field must have ``iam.serviceAccounts.actAs``
            permission on the service account. If not specified, the
            Pub/Sub `service
            agent <https://cloud.google.com/iam/docs/service-agents>`__,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com,
            is used.
    """

    class State(proto.Enum):
        r"""Possible states for a Cloud Storage subscription.

        Values:
            STATE_UNSPECIFIED (0):
                Default value. This value is unused.
            ACTIVE (1):
                The subscription can actively send messages
                to Cloud Storage.
            PERMISSION_DENIED (2):
                Cannot write to the Cloud Storage bucket
                because of permission denied errors.
            NOT_FOUND (3):
                Cannot write to the Cloud Storage bucket
                because it does not exist.
            IN_TRANSIT_LOCATION_RESTRICTION (4):
                Cannot write to the destination because enforce_in_transit
                is set to true and the destination locations are not in the
                allowed regions.
            SCHEMA_MISMATCH (5):
                Cannot write to the Cloud Storage bucket due
                to an incompatibility between the topic schema
                and subscription settings.
            VERTEX_AI_LOCATION_RESTRICTION (6):
                Cannot write to the Cloud Storage bucket because the bucket
                is not in the same location as where Vertex AI models used
                in ``message_transform``\ s are deployed.
        """

        STATE_UNSPECIFIED = 0
        ACTIVE = 1
        PERMISSION_DENIED = 2
        NOT_FOUND = 3
        IN_TRANSIT_LOCATION_RESTRICTION = 4
        SCHEMA_MISMATCH = 5
        VERTEX_AI_LOCATION_RESTRICTION = 6

    class TextConfig(proto.Message):
        r"""Configuration for writing message data in text format.
        Message payloads will be written to files as raw text, separated
        by a newline.

        """

    class AvroConfig(proto.Message):
        r"""Configuration for writing message data in Avro format.
        Message payloads and metadata will be written to files as an
        Avro binary.

        Attributes:
            write_metadata (bool):
                Optional. When true, write the subscription name,
                message_id, publish_time, attributes, and ordering_key as
                additional fields in the output. The subscription name,
                message_id, and publish_time fields are put in their own
                fields while all other message properties other than data
                (for example, an ordering_key, if present) are added as
                entries in the attributes map.
            use_topic_schema (bool):
                Optional. When true, the output Cloud Storage
                file will be serialized using the topic schema,
                if it exists.
        """

        write_metadata: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        use_topic_schema: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    bucket: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filename_prefix: str = proto.Field(
        proto.STRING,
        number=2,
    )
    filename_suffix: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filename_datetime_format: str = proto.Field(
        proto.STRING,
        number=10,
    )
    text_config: TextConfig = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="output_format",
        message=TextConfig,
    )
    avro_config: AvroConfig = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="output_format",
        message=AvroConfig,
    )
    max_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=6,
        message=duration_pb2.Duration,
    )
    max_bytes: int = proto.Field(
        proto.INT64,
        number=7,
    )
    max_messages: int = proto.Field(
        proto.INT64,
        number=8,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=9,
        enum=State,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=11,
    )


class ReceivedMessage(proto.Message):
    r"""A message and its corresponding acknowledgment ID.

    Attributes:
        ack_id (str):
            Optional. This ID can be used to acknowledge
            the received message.
        message (google.pubsub_v1.types.PubsubMessage):
            Optional. The message.
        delivery_attempt (int):
            Optional. The approximate number of times that Pub/Sub has
            attempted to deliver the associated message to a subscriber.

            More precisely, this is 1 + (number of NACKs) + (number of
            ack_deadline exceeds) for this message.

            A NACK is any call to ModifyAckDeadline with a 0 deadline.
            An ack_deadline exceeds event is whenever a message is not
            acknowledged within ack_deadline. Note that ack_deadline is
            initially Subscription.ackDeadlineSeconds, but may get
            extended automatically by the client library.

            Upon the first delivery of a given message,
            ``delivery_attempt`` will have a value of 1. The value is
            calculated at best effort and is approximate.

            If a DeadLetterPolicy is not set on the subscription, this
            will be 0.
    """

    ack_id: str = proto.Field(
        proto.STRING,
        number=1,
    )
    message: "PubsubMessage" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PubsubMessage",
    )
    delivery_attempt: int = proto.Field(
        proto.INT32,
        number=3,
    )


class GetSubscriptionRequest(proto.Message):
    r"""Request for the GetSubscription method.

    Attributes:
        subscription (str):
            Required. The name of the subscription to get. Format is
            ``projects/{project}/subscriptions/{sub}``.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateSubscriptionRequest(proto.Message):
    r"""Request for the UpdateSubscription method.

    Attributes:
        subscription (google.pubsub_v1.types.Subscription):
            Required. The updated subscription object.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Indicates which fields in the
            provided subscription to update. Must be
            specified and non-empty.
    """

    subscription: "Subscription" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Subscription",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListSubscriptionsRequest(proto.Message):
    r"""Request for the ``ListSubscriptions`` method.

    Attributes:
        project (str):
            Required. The name of the project in which to list
            subscriptions. Format is ``projects/{project-id}``.
        page_size (int):
            Optional. Maximum number of subscriptions to
            return.
        page_token (str):
            Optional. The value returned by the last
            ``ListSubscriptionsResponse``; indicates that this is a
            continuation of a prior ``ListSubscriptions`` call, and that
            the system should return the next page of data.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSubscriptionsResponse(proto.Message):
    r"""Response for the ``ListSubscriptions`` method.

    Attributes:
        subscriptions (MutableSequence[google.pubsub_v1.types.Subscription]):
            Optional. The subscriptions that match the
            request.
        next_page_token (str):
            Optional. If not empty, indicates that there may be more
            subscriptions that match the request; this value should be
            passed in a new ``ListSubscriptionsRequest`` to get more
            subscriptions.
    """

    @property
    def raw_page(self):
        return self

    subscriptions: MutableSequence["Subscription"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Subscription",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteSubscriptionRequest(proto.Message):
    r"""Request for the DeleteSubscription method.

    Attributes:
        subscription (str):
            Required. The subscription to delete. Format is
            ``projects/{project}/subscriptions/{sub}``.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ModifyPushConfigRequest(proto.Message):
    r"""Request for the ModifyPushConfig method.

    Attributes:
        subscription (str):
            Required. The name of the subscription. Format is
            ``projects/{project}/subscriptions/{sub}``.
        push_config (google.pubsub_v1.types.PushConfig):
            Required. The push configuration for future deliveries.

            An empty ``pushConfig`` indicates that the Pub/Sub system
            should stop pushing messages from the given subscription and
            allow messages to be pulled and acknowledged - effectively
            pausing the subscription if ``Pull`` or ``StreamingPull`` is
            not called.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    push_config: "PushConfig" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PushConfig",
    )


class PullRequest(proto.Message):
    r"""Request for the ``Pull`` method.

    Attributes:
        subscription (str):
            Required. The subscription from which messages should be
            pulled. Format is
            ``projects/{project}/subscriptions/{sub}``.
        return_immediately (bool):
            Optional. If this field set to true, the system will respond
            immediately even if it there are no messages available to
            return in the ``Pull`` response. Otherwise, the system may
            wait (for a bounded amount of time) until at least one
            message is available, rather than returning no messages.
            Warning: setting this field to ``true`` is discouraged
            because it adversely impacts the performance of ``Pull``
            operations. We recommend that users do not set this field.
        max_messages (int):
            Required. The maximum number of messages to
            return for this request. Must be a positive
            integer. The Pub/Sub system may return fewer
            than the number specified.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    return_immediately: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    max_messages: int = proto.Field(
        proto.INT32,
        number=3,
    )


class PullResponse(proto.Message):
    r"""Response for the ``Pull`` method.

    Attributes:
        received_messages (MutableSequence[google.pubsub_v1.types.ReceivedMessage]):
            Optional. Received Pub/Sub messages. The list will be empty
            if there are no more messages available in the backlog, or
            if no messages could be returned before the request timeout.
            For JSON, the response can be entirely empty. The Pub/Sub
            system may return fewer than the ``maxMessages`` requested
            even if there are more messages available in the backlog.
    """

    received_messages: MutableSequence["ReceivedMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReceivedMessage",
    )


class ModifyAckDeadlineRequest(proto.Message):
    r"""Request for the ModifyAckDeadline method.

    Attributes:
        subscription (str):
            Required. The name of the subscription. Format is
            ``projects/{project}/subscriptions/{sub}``.
        ack_ids (MutableSequence[str]):
            Required. List of acknowledgment IDs.
        ack_deadline_seconds (int):
            Required. The new ack deadline with respect to the time this
            request was sent to the Pub/Sub system. For example, if the
            value is 10, the new ack deadline will expire 10 seconds
            after the ``ModifyAckDeadline`` call was made. Specifying
            zero might immediately make the message available for
            delivery to another subscriber client. This typically
            results in an increase in the rate of message redeliveries
            (that is, duplicates). The minimum deadline you can specify
            is 0 seconds. The maximum deadline you can specify in a
            single request is 600 seconds (10 minutes).
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ack_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    ack_deadline_seconds: int = proto.Field(
        proto.INT32,
        number=3,
    )


class AcknowledgeRequest(proto.Message):
    r"""Request for the Acknowledge method.

    Attributes:
        subscription (str):
            Required. The subscription whose message is being
            acknowledged. Format is
            ``projects/{project}/subscriptions/{sub}``.
        ack_ids (MutableSequence[str]):
            Required. The acknowledgment ID for the messages being
            acknowledged that was returned by the Pub/Sub system in the
            ``Pull`` response. Must not be empty.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ack_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class StreamingPullRequest(proto.Message):
    r"""Request for the ``StreamingPull`` streaming RPC method. This request
    is used to establish the initial stream as well as to stream
    acknowledgments and ack deadline modifications from the client to
    the server.

    Attributes:
        subscription (str):
            Required. The subscription for which to initialize the new
            stream. This must be provided in the first request on the
            stream, and must not be set in subsequent requests from
            client to server. Format is
            ``projects/{project}/subscriptions/{sub}``.
        ack_ids (MutableSequence[str]):
            Optional. List of acknowledgment IDs for acknowledging
            previously received messages (received on this stream or a
            different stream). If an ack ID has expired, the
            corresponding message may be redelivered later.
            Acknowledging a message more than once will not result in an
            error. If the acknowledgment ID is malformed, the stream
            will be aborted with status ``INVALID_ARGUMENT``.
        modify_deadline_seconds (MutableSequence[int]):
            Optional. The list of new ack deadlines for the IDs listed
            in ``modify_deadline_ack_ids``. The size of this list must
            be the same as the size of ``modify_deadline_ack_ids``. If
            it differs the stream will be aborted with
            ``INVALID_ARGUMENT``. Each element in this list is applied
            to the element in the same position in
            ``modify_deadline_ack_ids``. The new ack deadline is with
            respect to the time this request was sent to the Pub/Sub
            system. Must be >= 0. For example, if the value is 10, the
            new ack deadline will expire 10 seconds after this request
            is received. If the value is 0, the message is immediately
            made available for another streaming or non-streaming pull
            request. If the value is < 0 (an error), the stream will be
            aborted with status ``INVALID_ARGUMENT``.
        modify_deadline_ack_ids (MutableSequence[str]):
            Optional. List of acknowledgment IDs whose deadline will be
            modified based on the corresponding element in
            ``modify_deadline_seconds``. This field can be used to
            indicate that more time is needed to process a message by
            the subscriber, or to make the message available for
            redelivery if the processing was interrupted.
        stream_ack_deadline_seconds (int):
            Required. The ack deadline to use for the
            stream. This must be provided in the first
            request on the stream, but it can also be
            updated on subsequent requests from client to
            server. The minimum deadline you can specify is
            10 seconds. The maximum deadline you can specify
            is 600 seconds (10 minutes).
        client_id (str):
            Optional. A unique identifier that is used to distinguish
            client instances from each other. Only needs to be provided
            on the initial request. When a stream disconnects and
            reconnects for the same stream, the client_id should be set
            to the same value so that state associated with the old
            stream can be transferred to the new stream. The same
            client_id should not be used for different client instances.
        max_outstanding_messages (int):
            Optional. Flow control settings for the maximum number of
            outstanding messages. When there are
            ``max_outstanding_messages`` currently sent to the streaming
            pull client that have not yet been acked or nacked, the
            server stops sending more messages. The sending of messages
            resumes once the number of outstanding messages is less than
            this value. If the value is <= 0, there is no limit to the
            number of outstanding messages. This property can only be
            set on the initial StreamingPullRequest. If it is set on a
            subsequent request, the stream will be aborted with status
            ``INVALID_ARGUMENT``.
        max_outstanding_bytes (int):
            Optional. Flow control settings for the maximum number of
            outstanding bytes. When there are ``max_outstanding_bytes``
            or more worth of messages currently sent to the streaming
            pull client that have not yet been acked or nacked, the
            server will stop sending more messages. The sending of
            messages resumes once the number of outstanding bytes is
            less than this value. If the value is <= 0, there is no
            limit to the number of outstanding bytes. This property can
            only be set on the initial StreamingPullRequest. If it is
            set on a subsequent request, the stream will be aborted with
            status ``INVALID_ARGUMENT``.
        protocol_version (int):
            Optional. The protocol version used by the client. This
            property can only be set on the initial
            StreamingPullRequest. If it is set on a subsequent request,
            the stream will be aborted with status ``INVALID_ARGUMENT``.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ack_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    modify_deadline_seconds: MutableSequence[int] = proto.RepeatedField(
        proto.INT32,
        number=3,
    )
    modify_deadline_ack_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    stream_ack_deadline_seconds: int = proto.Field(
        proto.INT32,
        number=5,
    )
    client_id: str = proto.Field(
        proto.STRING,
        number=6,
    )
    max_outstanding_messages: int = proto.Field(
        proto.INT64,
        number=7,
    )
    max_outstanding_bytes: int = proto.Field(
        proto.INT64,
        number=8,
    )
    protocol_version: int = proto.Field(
        proto.INT64,
        number=10,
    )


class StreamingPullResponse(proto.Message):
    r"""Response for the ``StreamingPull`` method. This response is used to
    stream messages from the server to the client.

    Attributes:
        received_messages (MutableSequence[google.pubsub_v1.types.ReceivedMessage]):
            Optional. Received Pub/Sub messages.
        acknowledge_confirmation (google.pubsub_v1.types.StreamingPullResponse.AcknowledgeConfirmation):
            Optional. This field will only be set if
            ``enable_exactly_once_delivery`` is set to ``true`` and is
            not guaranteed to be populated.
        modify_ack_deadline_confirmation (google.pubsub_v1.types.StreamingPullResponse.ModifyAckDeadlineConfirmation):
            Optional. This field will only be set if
            ``enable_exactly_once_delivery`` is set to ``true`` and is
            not guaranteed to be populated.
        subscription_properties (google.pubsub_v1.types.StreamingPullResponse.SubscriptionProperties):
            Optional. Properties associated with this
            subscription.
    """

    class AcknowledgeConfirmation(proto.Message):
        r"""Acknowledgment IDs sent in one or more previous requests to
        acknowledge a previously received message.

        Attributes:
            ack_ids (MutableSequence[str]):
                Optional. Successfully processed
                acknowledgment IDs.
            invalid_ack_ids (MutableSequence[str]):
                Optional. List of acknowledgment IDs that
                were malformed or whose acknowledgment deadline
                has expired.
            unordered_ack_ids (MutableSequence[str]):
                Optional. List of acknowledgment IDs that
                were out of order.
            temporary_failed_ack_ids (MutableSequence[str]):
                Optional. List of acknowledgment IDs that
                failed processing with temporary issues.
        """

        ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        invalid_ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        unordered_ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )
        temporary_failed_ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=4,
        )

    class ModifyAckDeadlineConfirmation(proto.Message):
        r"""Acknowledgment IDs sent in one or more previous requests to
        modify the deadline for a specific message.

        Attributes:
            ack_ids (MutableSequence[str]):
                Optional. Successfully processed
                acknowledgment IDs.
            invalid_ack_ids (MutableSequence[str]):
                Optional. List of acknowledgment IDs that
                were malformed or whose acknowledgment deadline
                has expired.
            temporary_failed_ack_ids (MutableSequence[str]):
                Optional. List of acknowledgment IDs that
                failed processing with temporary issues.
        """

        ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        invalid_ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
        )
        temporary_failed_ack_ids: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=3,
        )

    class SubscriptionProperties(proto.Message):
        r"""Subscription properties sent as part of the response.

        Attributes:
            exactly_once_delivery_enabled (bool):
                Optional. True iff exactly once delivery is
                enabled for this subscription.
            message_ordering_enabled (bool):
                Optional. True iff message ordering is
                enabled for this subscription.
        """

        exactly_once_delivery_enabled: bool = proto.Field(
            proto.BOOL,
            number=1,
        )
        message_ordering_enabled: bool = proto.Field(
            proto.BOOL,
            number=2,
        )

    received_messages: MutableSequence["ReceivedMessage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ReceivedMessage",
    )
    acknowledge_confirmation: AcknowledgeConfirmation = proto.Field(
        proto.MESSAGE,
        number=5,
        message=AcknowledgeConfirmation,
    )
    modify_ack_deadline_confirmation: ModifyAckDeadlineConfirmation = proto.Field(
        proto.MESSAGE,
        number=3,
        message=ModifyAckDeadlineConfirmation,
    )
    subscription_properties: SubscriptionProperties = proto.Field(
        proto.MESSAGE,
        number=4,
        message=SubscriptionProperties,
    )


class CreateSnapshotRequest(proto.Message):
    r"""Request for the ``CreateSnapshot`` method.

    Attributes:
        name (str):
            Required. User-provided name for this snapshot. If the name
            is not provided in the request, the server will assign a
            random name for this snapshot on the same project as the
            subscription. Note that for REST API requests, you must
            specify a name. See the `resource name
            rules <https://cloud.google.com/pubsub/docs/pubsub-basics#resource_names>`__.
            Format is ``projects/{project}/snapshots/{snap}``.
        subscription (str):
            Required. The subscription whose backlog the snapshot
            retains. Specifically, the created snapshot is guaranteed to
            retain: (a) The existing backlog on the subscription. More
            precisely, this is defined as the messages in the
            subscription's backlog that are unacknowledged upon the
            successful completion of the ``CreateSnapshot`` request; as
            well as: (b) Any messages published to the subscription's
            topic following the successful completion of the
            CreateSnapshot request. Format is
            ``projects/{project}/subscriptions/{sub}``.
        labels (MutableMapping[str, str]):
            Optional. See `Creating and managing
            labels <https://cloud.google.com/pubsub/docs/labels>`__.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag keys/values directly
            bound to this resource. For example: "123/environment":
            "production", "123/costCenter": "marketing" See
            https://{$universe.dns_names.final_documentation_domain}/pubsub/docs/tags
            for more information on using tags with Pub/Sub resources.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subscription: str = proto.Field(
        proto.STRING,
        number=2,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=3,
    )
    tags: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class UpdateSnapshotRequest(proto.Message):
    r"""Request for the UpdateSnapshot method.

    Attributes:
        snapshot (google.pubsub_v1.types.Snapshot):
            Required. The updated snapshot object.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Indicates which fields in the
            provided snapshot to update. Must be specified
            and non-empty.
    """

    snapshot: "Snapshot" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Snapshot",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class Snapshot(proto.Message):
    r"""A snapshot resource. Snapshots are used in
    `Seek <https://cloud.google.com/pubsub/docs/replay-overview>`__
    operations, which allow you to manage message acknowledgments in
    bulk. That is, you can set the acknowledgment state of messages in
    an existing subscription to the state captured by a snapshot.

    Attributes:
        name (str):
            Optional. The name of the snapshot.
        topic (str):
            Optional. The name of the topic from which
            this snapshot is retaining messages.
        expire_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The snapshot is guaranteed to exist up until this
            time. A newly-created snapshot expires no later than 7 days
            from the time of its creation. Its exact lifetime is
            determined at creation by the existing backlog in the source
            subscription. Specifically, the lifetime of the snapshot is
            ``7 days - (age of oldest unacked message in the subscription)``.
            For example, consider a subscription whose oldest unacked
            message is 3 days old. If a snapshot is created from this
            subscription, the snapshot -- which will always capture this
            3-day-old backlog as long as the snapshot exists -- will
            expire in 4 days. The service will refuse to create a
            snapshot that would expire in less than 1 hour after
            creation.
        labels (MutableMapping[str, str]):
            Optional. See [Creating and managing labels]
            (https://cloud.google.com/pubsub/docs/labels).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    topic: str = proto.Field(
        proto.STRING,
        number=2,
    )
    expire_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )


class GetSnapshotRequest(proto.Message):
    r"""Request for the GetSnapshot method.

    Attributes:
        snapshot (str):
            Required. The name of the snapshot to get. Format is
            ``projects/{project}/snapshots/{snap}``.
    """

    snapshot: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListSnapshotsRequest(proto.Message):
    r"""Request for the ``ListSnapshots`` method.

    Attributes:
        project (str):
            Required. The name of the project in which to list
            snapshots. Format is ``projects/{project-id}``.
        page_size (int):
            Optional. Maximum number of snapshots to
            return.
        page_token (str):
            Optional. The value returned by the last
            ``ListSnapshotsResponse``; indicates that this is a
            continuation of a prior ``ListSnapshots`` call, and that the
            system should return the next page of data.
    """

    project: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ListSnapshotsResponse(proto.Message):
    r"""Response for the ``ListSnapshots`` method.

    Attributes:
        snapshots (MutableSequence[google.pubsub_v1.types.Snapshot]):
            Optional. The resulting snapshots.
        next_page_token (str):
            Optional. If not empty, indicates that there may be more
            snapshot that match the request; this value should be passed
            in a new ``ListSnapshotsRequest``.
    """

    @property
    def raw_page(self):
        return self

    snapshots: MutableSequence["Snapshot"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Snapshot",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DeleteSnapshotRequest(proto.Message):
    r"""Request for the ``DeleteSnapshot`` method.

    Attributes:
        snapshot (str):
            Required. The name of the snapshot to delete. Format is
            ``projects/{project}/snapshots/{snap}``.
    """

    snapshot: str = proto.Field(
        proto.STRING,
        number=1,
    )


class SeekRequest(proto.Message):
    r"""Request for the ``Seek`` method.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        subscription (str):
            Required. The subscription to affect.
        time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time to seek to. Messages retained in the
            subscription that were published before this time are marked
            as acknowledged, and messages retained in the subscription
            that were published after this time are marked as
            unacknowledged. Note that this operation affects only those
            messages retained in the subscription (configured by the
            combination of ``message_retention_duration`` and
            ``retain_acked_messages``). For example, if ``time``
            corresponds to a point before the message retention window
            (or to a point before the system's notion of the
            subscription creation time), only retained messages will be
            marked as unacknowledged, and already-expunged messages will
            not be restored.

            This field is a member of `oneof`_ ``target``.
        snapshot (str):
            Optional. The snapshot to seek to. The snapshot's topic must
            be the same as that of the provided subscription. Format is
            ``projects/{project}/snapshots/{snap}``.

            This field is a member of `oneof`_ ``target``.
    """

    subscription: str = proto.Field(
        proto.STRING,
        number=1,
    )
    time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="target",
        message=timestamp_pb2.Timestamp,
    )
    snapshot: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="target",
    )


class SeekResponse(proto.Message):
    r"""Response for the ``Seek`` method (this response is empty)."""


class PubsubClientTelemetry(proto.Message):
    r"""Client-side telemetry about Pub/Sub requests, useful for debugging
    purposes. If the client opts to provide this information, it will be
    passed as a serialized proto in the
    ``x-goog-pubsub-client-telemetry`` header.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        publish_operation (google.pubsub_v1.types.PubsubClientTelemetry.PublishOperation):
            Optional. Telemetry about a ``Publish`` operation.

            This field is a member of `oneof`_ ``operation``.
    """

    class PublishOperation(proto.Message):
        r"""Telemetry about a ``Publish`` operation which may or may not be
        common across individual RPCs.

        Attributes:
            hedged_attempt_count (int):
                Optional. If the publisher client is using
                publish hedging, provides the attempt count for
                the hedge (starting at 1). A value of 0
                indicates that the request was not hedged.
            publish_start_time (google.protobuf.timestamp_pb2.Timestamp):
                Optional. Time at which the ``publish()`` call was initiated
                in the client library, meaning across all RPC retry
                attempts, see `grpc
                retries <https://grpc.io/docs/guides/retry/>`__. Provides a
                sense of the end-to-end publish duration from the client
                perspective, across retries.
        """

        hedged_attempt_count: int = proto.Field(
            proto.INT32,
            number=1,
        )
        publish_start_time: timestamp_pb2.Timestamp = proto.Field(
            proto.MESSAGE,
            number=2,
            message=timestamp_pb2.Timestamp,
        )

    publish_operation: PublishOperation = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="operation",
        message=PublishOperation,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
