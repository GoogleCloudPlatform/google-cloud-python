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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.code_pb2 as code_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.eventarc_v1.types import network_config as gce_network_config

__protobuf__ = proto.module(
    package="google.cloud.eventarc.v1",
    manifest={
        "Trigger",
        "EventFilter",
        "StateCondition",
        "Destination",
        "Transport",
        "CloudRun",
        "GKE",
        "Pubsub",
        "HttpEndpoint",
    },
)


class Trigger(proto.Message):
    r"""A representation of the trigger resource.

    Attributes:
        name (str):
            Required. The resource name of the trigger. Must be unique
            within the location of the project and must be in
            ``projects/{project}/locations/{location}/triggers/{trigger}``
            format.
        uid (str):
            Output only. Server-assigned unique
            identifier for the trigger. The value is a UUID4
            string and guaranteed to remain unchanged until
            the resource is deleted.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The creation time.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The last-modified time.
        event_filters (MutableSequence[google.cloud.eventarc_v1.types.EventFilter]):
            Required. Unordered list. The list of filters
            that applies to event attributes. Only events
            that match all the provided filters are sent to
            the destination.
        service_account (str):
            Optional. The IAM service account email associated with the
            trigger. The service account represents the identity of the
            trigger.

            The ``iam.serviceAccounts.actAs`` permission must be granted
            on the service account to allow a principal to impersonate
            the service account. For more information, see the `Roles
            and permissions </eventarc/docs/all-roles-permissions>`__
            page specific to the trigger destination.
        destination (google.cloud.eventarc_v1.types.Destination):
            Required. Destination specifies where the
            events should be sent to.
        transport (google.cloud.eventarc_v1.types.Transport):
            Optional. To deliver messages, Eventarc might
            use other Google Cloud products as a transport
            intermediary. This field contains a reference to
            that transport intermediary. This information
            can be used for debugging purposes.
        labels (MutableMapping[str, str]):
            Optional. User labels attached to the
            triggers that can be used to group resources.
        channel (str):
            Optional. The name of the channel associated with the
            trigger in
            ``projects/{project}/locations/{location}/channels/{channel}``
            format. You must provide a channel to receive events from
            Eventarc SaaS partners.
        conditions (MutableMapping[str, google.cloud.eventarc_v1.types.StateCondition]):
            Output only. The reason(s) why a trigger is
            in FAILED state.
        event_data_content_type (str):
            Optional. EventDataContentType specifies the type of payload
            in MIME format that is expected from the CloudEvent data
            field. This is set to ``application/json`` if the value is
            not defined.
        satisfies_pzs (bool):
            Output only. Whether or not this Trigger
            satisfies the requirements of physical zone
            separation
        retry_policy (google.cloud.eventarc_v1.types.Trigger.RetryPolicy):
            Optional. The retry policy to use in the
            Trigger.
            If unset, event delivery will be retried for up
            to 24 hours by default:

            https://cloud.google.com/eventarc/docs/retry-events
        etag (str):
            Output only. This checksum is computed by the
            server based on the value of other fields, and
            might be sent only on create requests to ensure
            that the client has an up-to-date value before
            proceeding.
    """

    class RetryPolicy(proto.Message):
        r"""The retry policy configuration for the Trigger.

        Can only be set with Cloud Run destinations.

        Attributes:
            max_attempts (int):
                Optional. The maximum number of delivery
                attempts for any message. The only valid value
                is 1.
        """

        max_attempts: int = proto.Field(
            proto.INT32,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    event_filters: MutableSequence["EventFilter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=8,
        message="EventFilter",
    )
    service_account: str = proto.Field(
        proto.STRING,
        number=9,
    )
    destination: "Destination" = proto.Field(
        proto.MESSAGE,
        number=10,
        message="Destination",
    )
    transport: "Transport" = proto.Field(
        proto.MESSAGE,
        number=11,
        message="Transport",
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    channel: str = proto.Field(
        proto.STRING,
        number=13,
    )
    conditions: MutableMapping[str, "StateCondition"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=15,
        message="StateCondition",
    )
    event_data_content_type: str = proto.Field(
        proto.STRING,
        number=16,
    )
    satisfies_pzs: bool = proto.Field(
        proto.BOOL,
        number=19,
    )
    retry_policy: RetryPolicy = proto.Field(
        proto.MESSAGE,
        number=20,
        message=RetryPolicy,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=99,
    )


class EventFilter(proto.Message):
    r"""Filters events based on exact matches on the CloudEvents
    attributes.

    Attributes:
        attribute (str):
            Required. The name of a CloudEvents attribute. Currently,
            only a subset of attributes are supported for filtering. You
            can `retrieve a specific provider's supported event
            types </eventarc/docs/list-providers#describe-provider>`__.

            All triggers MUST provide a filter for the 'type' attribute.
        value (str):
            Required. The value for the attribute.
        operator (str):
            Optional. The operator used for matching the events with the
            value of the filter. If not specified, only events that have
            an exact key-value pair specified in the filter are matched.
            The allowed values are ``path_pattern`` and
            ``match-path-pattern``. ``path_pattern`` is only allowed for
            GCFv1 triggers.
    """

    attribute: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: str = proto.Field(
        proto.STRING,
        number=2,
    )
    operator: str = proto.Field(
        proto.STRING,
        number=3,
    )


class StateCondition(proto.Message):
    r"""A condition that is part of the trigger state computation.

    Attributes:
        code (google.rpc.code_pb2.Code):
            The canonical code of the condition.
        message (str):
            Human-readable message.
    """

    code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    message: str = proto.Field(
        proto.STRING,
        number=2,
    )


class Destination(proto.Message):
    r"""Represents a target of an invocation over HTTP.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        cloud_run (google.cloud.eventarc_v1.types.CloudRun):
            Cloud Run fully-managed resource that
            receives the events. The resource should be in
            the same project as the trigger.

            This field is a member of `oneof`_ ``descriptor``.
        cloud_function (str):
            The Cloud Function resource name. Cloud Functions V1 and V2
            are supported. Format:
            ``projects/{project}/locations/{location}/functions/{function}``

            This is a read-only field. Creating Cloud Functions V1/V2
            triggers is only supported via the Cloud Functions product.
            An error will be returned if the user sets this value.

            This field is a member of `oneof`_ ``descriptor``.
        gke (google.cloud.eventarc_v1.types.GKE):
            A GKE service capable of receiving events.
            The service should be running in the same
            project as the trigger.

            This field is a member of `oneof`_ ``descriptor``.
        workflow (str):
            The resource name of the Workflow whose Executions are
            triggered by the events. The Workflow resource should be
            deployed in the same project as the trigger. Format:
            ``projects/{project}/locations/{location}/workflows/{workflow}``

            This field is a member of `oneof`_ ``descriptor``.
        http_endpoint (google.cloud.eventarc_v1.types.HttpEndpoint):
            An HTTP endpoint destination described by an
            URI.

            This field is a member of `oneof`_ ``descriptor``.
        network_config (google.cloud.eventarc_v1.types.NetworkConfig):
            Optional. Network config is used to configure
            how Eventarc resolves and connect to a
            destination. This should only be used with
            HttpEndpoint destination type.
    """

    cloud_run: "CloudRun" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="descriptor",
        message="CloudRun",
    )
    cloud_function: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="descriptor",
    )
    gke: "GKE" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="descriptor",
        message="GKE",
    )
    workflow: str = proto.Field(
        proto.STRING,
        number=4,
        oneof="descriptor",
    )
    http_endpoint: "HttpEndpoint" = proto.Field(
        proto.MESSAGE,
        number=5,
        oneof="descriptor",
        message="HttpEndpoint",
    )
    network_config: gce_network_config.NetworkConfig = proto.Field(
        proto.MESSAGE,
        number=6,
        message=gce_network_config.NetworkConfig,
    )


class Transport(proto.Message):
    r"""Represents the transport intermediaries created for the
    trigger to deliver events.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        pubsub (google.cloud.eventarc_v1.types.Pubsub):
            The Pub/Sub topic and subscription used by
            Eventarc as a transport intermediary.

            This field is a member of `oneof`_ ``intermediary``.
    """

    pubsub: "Pubsub" = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="intermediary",
        message="Pubsub",
    )


class CloudRun(proto.Message):
    r"""Represents a Cloud Run destination.

    Attributes:
        service (str):
            Required. The name of the Cloud Run service
            being addressed. See
            https://cloud.google.com/run/docs/reference/rest/v1/namespaces.services.

            Only services located in the same project as the
            trigger object can be addressed.
        path (str):
            Optional. The relative path on the Cloud Run
            service the events should be sent to.

            The value must conform to the definition of a
            URI path segment (section 3.3 of RFC2396).
            Examples: "/route", "route", "route/subroute".
        region (str):
            Required. The region the Cloud Run service is
            deployed in.
    """

    service: str = proto.Field(
        proto.STRING,
        number=1,
    )
    path: str = proto.Field(
        proto.STRING,
        number=2,
    )
    region: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GKE(proto.Message):
    r"""Represents a GKE destination.

    Attributes:
        cluster (str):
            Required. The name of the cluster the GKE
            service is running in. The cluster must be
            running in the same project as the trigger being
            created.
        location (str):
            Required. The name of the Google Compute
            Engine in which the cluster resides, which can
            either be compute zone (for example,
            us-central1-a) for the zonal clusters or region
            (for example, us-central1) for regional
            clusters.
        namespace (str):
            Required. The namespace the GKE service is
            running in.
        service (str):
            Required. Name of the GKE service.
        path (str):
            Optional. The relative path on the GKE
            service the events should be sent to.

            The value must conform to the definition of a
            URI path segment (section 3.3 of RFC2396).
            Examples: "/route", "route", "route/subroute".
    """

    cluster: str = proto.Field(
        proto.STRING,
        number=1,
    )
    location: str = proto.Field(
        proto.STRING,
        number=2,
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=3,
    )
    service: str = proto.Field(
        proto.STRING,
        number=4,
    )
    path: str = proto.Field(
        proto.STRING,
        number=5,
    )


class Pubsub(proto.Message):
    r"""Represents a Pub/Sub transport.

    Attributes:
        topic (str):
            Optional. The name of the Pub/Sub topic created and managed
            by Eventarc as a transport for the event delivery. Format:
            ``projects/{PROJECT_ID}/topics/{TOPIC_NAME}``.

            You can set an existing topic for triggers of the type
            ``google.cloud.pubsub.topic.v1.messagePublished``. The topic
            you provide here is not deleted by Eventarc at trigger
            deletion.
        subscription (str):
            Output only. The name of the Pub/Sub subscription created
            and managed by Eventarc as a transport for the event
            delivery. Format:
            ``projects/{PROJECT_ID}/subscriptions/{SUBSCRIPTION_NAME}``.
    """

    topic: str = proto.Field(
        proto.STRING,
        number=1,
    )
    subscription: str = proto.Field(
        proto.STRING,
        number=2,
    )


class HttpEndpoint(proto.Message):
    r"""Represents a HTTP endpoint destination.

    Attributes:
        uri (str):
            Required. The URI of the HTTP endpoint.

            The value must be a RFC2396 URI string. Examples:
            ``http://10.10.10.8:80/route``,
            ``http://svc.us-central1.p.local:8080/``. Only HTTP and
            HTTPS protocols are supported. The host can be either a
            static IP addressable from the VPC specified by the network
            config, or an internal DNS hostname of the service
            resolvable via Cloud DNS.
    """

    uri: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
