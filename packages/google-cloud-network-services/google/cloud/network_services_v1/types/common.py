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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "EnvoyHeaders",
        "OperationMetadata",
        "TrafficPortSelector",
        "EndpointMatcher",
    },
)


class EnvoyHeaders(proto.Enum):
    r"""EnvoyHeader configuration for Mesh and Gateway

    Values:
        ENVOY_HEADERS_UNSPECIFIED (0):
            Defaults to NONE.
        NONE (1):
            Suppress envoy debug headers.
        DEBUG_HEADERS (2):
            Envoy will insert default internal debug
            headers into upstream requests:
            x-envoy-attempt-count, x-envoy-is-timeout-retry,
            x-envoy-expected-rq-timeout-ms,
            x-envoy-original-path,
            x-envoy-upstream-stream-duration-ms
    """

    ENVOY_HEADERS_UNSPECIFIED = 0
    NONE = 1
    DEBUG_HEADERS = 2


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_message (str):
            Output only. Human-readable status of the
            operation, if any.
        requested_cancellation (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_message: str = proto.Field(
        proto.STRING,
        number=5,
    )
    requested_cancellation: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


class TrafficPortSelector(proto.Message):
    r"""Specification of a port-based selector.

    Attributes:
        ports (MutableSequence[str]):
            Optional. A list of ports. Can be port numbers or port range
            (example, [80-90] specifies all ports from 80 to 90,
            including 80 and 90) or named ports or \* to specify all
            ports. If the list is empty, all ports are selected.
    """

    ports: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class EndpointMatcher(proto.Message):
    r"""A definition of a matcher that selects endpoints to which the
    policies should be applied.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        metadata_label_matcher (google.cloud.network_services_v1.types.EndpointMatcher.MetadataLabelMatcher):
            The matcher is based on node metadata
            presented by xDS clients.

            This field is a member of `oneof`_ ``matcher_type``.
    """

    class MetadataLabelMatcher(proto.Message):
        r"""The matcher that is based on node metadata presented by xDS
        clients.

        Attributes:
            metadata_label_match_criteria (google.cloud.network_services_v1.types.EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria):
                Specifies how matching should be done.

                Supported values are: MATCH_ANY: At least one of the Labels
                specified in the matcher should match the metadata presented
                by xDS client. MATCH_ALL: The metadata presented by the xDS
                client should contain all of the labels specified here.

                The selection is determined based on the best match. For
                example, suppose there are three EndpointPolicy resources
                P1, P2 and P3 and if P1 has a the matcher as MATCH_ANY <A:1,
                B:1>, P2 has MATCH_ALL <A:1,B:1>, and P3 has MATCH_ALL
                <A:1,B:1,C:1>.

                If a client with label <A:1> connects, the config from P1
                will be selected.

                If a client with label <A:1,B:1> connects, the config from
                P2 will be selected.

                If a client with label <A:1,B:1,C:1> connects, the config
                from P3 will be selected.

                If there is more than one best match, (for example, if a
                config P4 with selector <A:1,D:1> exists and if a client
                with label <A:1,B:1,D:1> connects), pick up the one with
                older creation time.
            metadata_labels (MutableSequence[google.cloud.network_services_v1.types.EndpointMatcher.MetadataLabelMatcher.MetadataLabels]):
                The list of label value pairs that must match labels in the
                provided metadata based on filterMatchCriteria This list can
                have at most 64 entries. The list can be empty if the match
                criteria is MATCH_ANY, to specify a wildcard match (i.e this
                matches any client).
        """

        class MetadataLabelMatchCriteria(proto.Enum):
            r"""Possible criteria values that define logic of how matching is
            made.

            Values:
                METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED (0):
                    Default value. Should not be used.
                MATCH_ANY (1):
                    At least one of the Labels specified in the
                    matcher should match the metadata presented by
                    xDS client.
                MATCH_ALL (2):
                    The metadata presented by the xDS client
                    should contain all of the labels specified here.
            """

            METADATA_LABEL_MATCH_CRITERIA_UNSPECIFIED = 0
            MATCH_ANY = 1
            MATCH_ALL = 2

        class MetadataLabels(proto.Message):
            r"""Defines a name-pair value for a single label.

            Attributes:
                label_name (str):
                    Required. Label name presented as key in xDS
                    Node Metadata.
                label_value (str):
                    Required. Label value presented as value
                    corresponding to the above key, in xDS Node
                    Metadata.
            """

            label_name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            label_value: str = proto.Field(
                proto.STRING,
                number=2,
            )

        metadata_label_match_criteria: "EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria" = proto.Field(
            proto.ENUM,
            number=1,
            enum="EndpointMatcher.MetadataLabelMatcher.MetadataLabelMatchCriteria",
        )
        metadata_labels: MutableSequence[
            "EndpointMatcher.MetadataLabelMatcher.MetadataLabels"
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="EndpointMatcher.MetadataLabelMatcher.MetadataLabels",
        )

    metadata_label_matcher: MetadataLabelMatcher = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="matcher_type",
        message=MetadataLabelMatcher,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
