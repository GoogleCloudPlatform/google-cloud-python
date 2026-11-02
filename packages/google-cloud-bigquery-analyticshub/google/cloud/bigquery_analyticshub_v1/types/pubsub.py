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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.bigquery.analyticshub.v1",
    manifest={
        "PubSubSubscription",
        "RetryPolicy",
        "DeadLetterPolicy",
        "ExpirationPolicy",
        "PushConfig",
        "BigQueryConfig",
        "CloudStorageConfig",
        "MessageTransform",
        "JavaScriptUDF",
    },
)


class PubSubSubscription(proto.Message):
    r"""Defines the destination Pub/Sub subscription. If none of
    ``push_config``, ``bigquery_config``, ``cloud_storage_config``,
    ``pubsub_export_config``, or ``pubsublite_export_config`` is set,
    then the subscriber will pull and ack messages using API methods. At
    most one of these fields may be set.

    Attributes:
        name (str):
            Required. Name of the subscription. Format is
            ``projects/{project}/subscriptions/{sub}``.
        push_config (google.cloud.bigquery_analyticshub_v1.types.PushConfig):
            Optional. If push delivery is used with this
            subscription, this field is used to configure
            it.
        bigquery_config (google.cloud.bigquery_analyticshub_v1.types.BigQueryConfig):
            Optional. If delivery to BigQuery is used
            with this subscription, this field is used to
            configure it.
        cloud_storage_config (google.cloud.bigquery_analyticshub_v1.types.CloudStorageConfig):
            Optional. If delivery to Google Cloud Storage
            is used with this subscription, this field is
            used to configure it.
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
        expiration_policy (google.cloud.bigquery_analyticshub_v1.types.ExpirationPolicy):
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
        dead_letter_policy (google.cloud.bigquery_analyticshub_v1.types.DeadLetterPolicy):
            Optional. A policy that specifies the conditions for dead
            lettering messages in this subscription. If
            dead_letter_policy is not set, dead lettering is disabled.

            The Pub/Sub service account associated with this
            subscriptions's parent project (i.e.,
            service-{project_number}@gcp-sa-pubsub.iam.gserviceaccount.com)
            must have permission to Acknowledge() messages on this
            subscription.
        retry_policy (google.cloud.bigquery_analyticshub_v1.types.RetryPolicy):
            Optional. A policy that specifies how Pub/Sub
            retries message delivery for this subscription.

            If not set, the default retry policy is applied.
            This generally implies that messages will be
            retried as soon as possible for healthy
            subscribers. RetryPolicy will be triggered on
            NACKs or acknowledgement deadline exceeded
            events for a given message.
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
              resent before the message's acknowledgement deadline
              expires.
            - An acknowledged message will not be resent to a
              subscriber.

            Note that subscribers may still receive multiple copies of a
            message when ``enable_exactly_once_delivery`` is true if the
            message was published multiple times by a publisher client.
            These copies are considered distinct by Pub/Sub and have
            distinct ``message_id`` values.
        message_transforms (MutableSequence[google.cloud.bigquery_analyticshub_v1.types.MessageTransform]):
            Optional. Transforms to be applied to
            messages before they are delivered to
            subscribers. Transforms are applied in the order
            specified.
        tags (MutableMapping[str, str]):
            Optional. Input only. Immutable. Tag
            keys/values directly bound to this resource. For
            example:

              "123/environment": "production",
              "123/costCenter": "marketing".
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
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

    RetryPolicy will be triggered on NACKs or acknowledgement deadline
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
            of number of NACKs and number of times the acknowledgement
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
        oidc_token (google.cloud.bigquery_analyticshub_v1.types.PushConfig.OidcToken):
            Optional. If specified, Pub/Sub will generate and attach an
            OIDC JWT token as an ``Authorization`` header in the HTTP
            request for every pushed message.

            This field is a member of `oneof`_ ``authentication_method``.
        pubsub_wrapper (google.cloud.bigquery_analyticshub_v1.types.PushConfig.PubsubWrapper):
            Optional. When set, the payload to the push
            endpoint is in the form of the JSON
            representation of a PubsubMessage
            (https://cloud.google.com/pubsub/docs/reference/rpc/google.pubsub.v1#pubsubmessage).

            This field is a member of `oneof`_ ``wrapper``.
        no_wrapper (google.cloud.bigquery_analyticshub_v1.types.PushConfig.NoWrapper):
            Optional. When set, the payload to the push
            endpoint is not wrapped.

            This field is a member of `oneof`_ ``wrapper``.
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
    push_endpoint: str = proto.Field(
        proto.STRING,
        number=1,
    )
    attributes: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
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
            Optional. When true and use_topic_schema is true, any fields
            that are a part of the topic schema that are not part of the
            BigQuery table schema are dropped when writing to BigQuery.
            Otherwise, the schemas must be kept in sync and any messages
            with extra fields are not written and remain in the
            subscription's backlog.
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
    use_table_schema: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    service_account_email: str = proto.Field(
        proto.STRING,
        number=7,
    )


class CloudStorageConfig(proto.Message):
    r"""Configuration for a Cloud Storage subscription.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        text_config (google.cloud.bigquery_analyticshub_v1.types.CloudStorageConfig.TextConfig):
            Optional. If set, message data will be
            written to Cloud Storage in text format.

            This field is a member of `oneof`_ ``output_format``.
        avro_config (google.cloud.bigquery_analyticshub_v1.types.CloudStorageConfig.AvroConfig):
            Optional. If set, message data will be
            written to Cloud Storage in Avro format.

            This field is a member of `oneof`_ ``output_format``.
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
        max_duration (google.protobuf.duration_pb2.Duration):
            Optional. File batching settings. If no max_duration setting
            is specified, a max_duration of 5 minutes will be set by
            default. max_duration is required regardless of whether
            other file batching settings are specified.

            The maximum duration that can elapse before a new Cloud
            Storage file is created. Min 1 minute, max 10 minutes,
            default 5 minutes. May not exceed the subscription's
            acknowledgement deadline.
        max_bytes (int):
            Optional. The maximum bytes that can be written to a Cloud
            Storage file before a new file is created. Min 1 KB, max 10
            GiB. The max_bytes limit may be exceeded in cases where
            messages are larger than the limit.
        max_messages (int):
            Optional. The maximum number of messages that
            can be written to a Cloud Storage file before a
            new file is created. Min 1000 messages.
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
    service_account_email: str = proto.Field(
        proto.STRING,
        number=11,
    )


class MessageTransform(proto.Message):
    r"""All supported message transforms types.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        javascript_udf (google.cloud.bigquery_analyticshub_v1.types.JavaScriptUDF):
            Optional. JavaScript User Defined Function. If multiple
            JavaScriptUDF's are specified on a resource, each must have
            a unique ``function_name``.

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
    enabled: bool = proto.Field(
        proto.BOOL,
        number=3,
    )
    disabled: bool = proto.Field(
        proto.BOOL,
        number=4,
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
                 *   - (required) 'message_id'  : {string}
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


__all__ = tuple(sorted(__protobuf__.manifest))
