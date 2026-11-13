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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1beta1",
    manifest={
        "EventType",
        "LoadBalancingScheme",
        "ExtensionChain",
        "LbTrafficExtension",
        "ListLbTrafficExtensionsRequest",
        "ListLbTrafficExtensionsResponse",
        "GetLbTrafficExtensionRequest",
        "CreateLbTrafficExtensionRequest",
        "UpdateLbTrafficExtensionRequest",
        "DeleteLbTrafficExtensionRequest",
        "LbRouteExtension",
        "ListLbRouteExtensionsRequest",
        "ListLbRouteExtensionsResponse",
        "GetLbRouteExtensionRequest",
        "CreateLbRouteExtensionRequest",
        "UpdateLbRouteExtensionRequest",
        "DeleteLbRouteExtensionRequest",
        "ExtensionBinding",
        "ListExtensionBindingsRequest",
        "ListExtensionBindingsResponse",
        "GetExtensionBindingRequest",
        "CreateExtensionBindingRequest",
        "UpdateExtensionBindingRequest",
        "DeleteExtensionBindingRequest",
    },
)


class EventType(proto.Enum):
    r"""The part of the request or response for which the extension
    is called.

    Values:
        EVENT_TYPE_UNSPECIFIED (0):
            Unspecified value. Do not use.
        REQUEST_HEADERS (1):
            If included in ``supported_events``, the extension is called
            when the HTTP request headers arrive.
        REQUEST_BODY (2):
            If included in ``supported_events``, the extension is called
            when the HTTP request body arrives.
        RESPONSE_HEADERS (3):
            If included in ``supported_events``, the extension is called
            when the HTTP response headers arrive.
        RESPONSE_BODY (4):
            If included in ``supported_events``, the extension is called
            when the HTTP response body arrives.
        REQUEST_TRAILERS (5):
            If included in ``supported_events``, the extension is called
            when the HTTP request trailers arrives.
        RESPONSE_TRAILERS (6):
            If included in ``supported_events``, the extension is called
            when the HTTP response trailers arrives.
    """

    EVENT_TYPE_UNSPECIFIED = 0
    REQUEST_HEADERS = 1
    REQUEST_BODY = 2
    RESPONSE_HEADERS = 3
    RESPONSE_BODY = 4
    REQUEST_TRAILERS = 5
    RESPONSE_TRAILERS = 6


class LoadBalancingScheme(proto.Enum):
    r"""Load balancing schemes supported by the ``LbTrafficExtension``
    resource and ``LbRouteExtension`` resource. For more information,
    refer to `Choosing a load
    balancer <https://cloud.google.com/load-balancing/docs/backend-service>`__.

    Values:
        LOAD_BALANCING_SCHEME_UNSPECIFIED (0):
            Default value. Do not use.
        INTERNAL_MANAGED (1):
            Signifies that this is used for Internal
            HTTP(S) Load Balancing.
        EXTERNAL_MANAGED (2):
            Signifies that this is used for External
            Managed HTTP(S) Load Balancing.
    """

    LOAD_BALANCING_SCHEME_UNSPECIFIED = 0
    INTERNAL_MANAGED = 1
    EXTERNAL_MANAGED = 2


class ExtensionChain(proto.Message):
    r"""A single extension chain wrapper that contains the match
    conditions and extensions to execute.

    Attributes:
        name (str):
            Required. The name for this extension chain.
            The name is logged as part of the HTTP request
            logs. The name must conform with RFC-1034, is
            restricted to lower-cased letters, numbers and
            hyphens, and can have a maximum length of 63
            characters. Additionally, the first character
            must be a letter and the last a letter or a
            number.
        match_condition (google.cloud.network_services_v1beta1.types.ExtensionChain.MatchCondition):
            Required. Conditions under which this chain
            is invoked for a request.
        extensions (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionChain.Extension]):
            Required. A set of extensions to execute for the matching
            request. At least one extension is required. Up to 3
            extensions can be defined for each extension chain for
            ``LbTrafficExtension`` resource. ``LbRouteExtension`` chains
            are limited to 1 extension per extension chain.
    """

    class MatchCondition(proto.Message):
        r"""Conditions under which this chain is invoked for a request.

        Attributes:
            cel_expression (str):
                Required. A Common Expression Language (CEL) expression that
                is used to match requests for which the extension chain is
                executed.

                For more information, see `CEL matcher language
                reference <https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference>`__.
        """

        cel_expression: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class Extension(proto.Message):
        r"""A single extension in the chain to execute for the matching
        request.

        Attributes:
            name (str):
                Required. The name for this extension.
                The name is logged as part of the HTTP request
                logs. The name must conform with RFC-1034, is
                restricted to lower-cased letters, numbers and
                hyphens, and can have a maximum length of 63
                characters. Additionally, the first character
                must be a letter and the last a letter or a
                number.
            authority (str):
                Optional. The ``:authority`` header in the gRPC request sent
                from Envoy to the extension service. Required for Callout
                extensions.
            service (str):
                Required. The reference to the service that runs the
                extension.

                Currently only callout extensions are supported here.

                To configure a callout extension, ``service`` must be a
                fully-qualified reference to a `backend
                service <https://cloud.google.com/compute/docs/reference/rest/v1/backendServices>`__
                in the format:
                ``https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}``
                or
                ``https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}``.
            supported_events (MutableSequence[google.cloud.network_services_v1beta1.types.EventType]):
                Optional. A set of events during request or response
                processing for which this extension is called. This field is
                required for the ``LbTrafficExtension`` resource. It's not
                relevant for the ``LbRouteExtension`` resource.
            timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the timeout for each
                individual message on the stream. The timeout
                must be between 10-1000 milliseconds. Required
                for Callout extensions.
            fail_open (bool):
                Optional. Determines how the proxy behaves if the call to
                the extension fails or times out.

                When set to ``TRUE``, request or response processing
                continues without error. Any subsequent extensions in the
                extension chain are also executed. When set to ``FALSE`` or
                the default setting of ``FALSE`` is used, one of the
                following happens:

                - If response headers have not been delivered to the
                  downstream client, a generic 500 error is returned to the
                  client. The error response can be tailored by configuring
                  a custom error response in the load balancer.

                - If response headers have been delivered, then the HTTP
                  stream to the downstream client is reset.
            forward_headers (MutableSequence[str]):
                Optional. List of the HTTP headers to forward
                to the extension (from the client or backend).
                If omitted, all headers are sent. Each element
                is a string indicating the header name.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        authority: str = proto.Field(
            proto.STRING,
            number=2,
        )
        service: str = proto.Field(
            proto.STRING,
            number=3,
        )
        supported_events: MutableSequence["EventType"] = proto.RepeatedField(
            proto.ENUM,
            number=4,
            enum="EventType",
        )
        timeout: duration_pb2.Duration = proto.Field(
            proto.MESSAGE,
            number=5,
            message=duration_pb2.Duration,
        )
        fail_open: bool = proto.Field(
            proto.BOOL,
            number=6,
        )
        forward_headers: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=7,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    match_condition: MatchCondition = proto.Field(
        proto.MESSAGE,
        number=2,
        message=MatchCondition,
    )
    extensions: MutableSequence[Extension] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=Extension,
    )


class LbTrafficExtension(proto.Message):
    r"""``LbTrafficExtension`` is a resource that lets the extension service
    modify the headers and payloads of both requests and responses
    without impacting the choice of backend services or any other
    security policies associated with the backend service.

    Attributes:
        name (str):
            Required. Identifier. Name of the ``LbTrafficExtension``
            resource in the following format:
            ``projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A human-readable description of the
            resource.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with the
            ``LbTrafficExtension`` resource.

            The format must comply with `the requirements for
            labels <https://cloud.google.com/compute/docs/labeling-resources#requirements>`__
            for Google Cloud resources.
        forwarding_rules (MutableSequence[str]):
            Required. A list of references to the forwarding rules to
            which this service extension is attached to. At least one
            forwarding rule is required. There can be only one
            ``LBTrafficExtension`` resource per forwarding rule.
        extension_chains (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionChain]):
            Required. A set of ordered extension chains
            that contain the match conditions and extensions
            to execute. Match conditions for each extension
            chain are evaluated in sequence for a given
            request. The first extension chain that has a
            condition that matches the request is executed.
            Any subsequent extension chains do not execute.
            Limited to 5 extension chains per resource.
        load_balancing_scheme (google.cloud.network_services_v1beta1.types.LoadBalancingScheme):
            Required. All backend services and forwarding rules
            referenced by this extension must share the same load
            balancing scheme. Supported values: ``INTERNAL_MANAGED``,
            ``EXTERNAL_MANAGED``. For more information, refer to
            `Choosing a load
            balancer <https://cloud.google.com/load-balancing/docs/backend-service>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    forwarding_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    extension_chains: MutableSequence["ExtensionChain"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ExtensionChain",
    )
    load_balancing_scheme: "LoadBalancingScheme" = proto.Field(
        proto.ENUM,
        number=8,
        enum="LoadBalancingScheme",
    )


class ListLbTrafficExtensionsRequest(proto.Message):
    r"""Message for requesting list of ``LbTrafficExtension`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``LbTrafficExtension`` resources are listed, specified in
            the following format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. The server
            might return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results that the server returns.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
    """

    parent: str = proto.Field(
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListLbTrafficExtensionsResponse(proto.Message):
    r"""Message for response to listing ``LbTrafficExtension`` resources.

    Attributes:
        lb_traffic_extensions (MutableSequence[google.cloud.network_services_v1beta1.types.LbTrafficExtension]):
            The list of ``LbTrafficExtension`` resources.
        next_page_token (str):
            A token identifying a page of results that
            the server returns.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    lb_traffic_extensions: MutableSequence["LbTrafficExtension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LbTrafficExtension",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetLbTrafficExtensionRequest(proto.Message):
    r"""Message for getting a ``LbTrafficExtension`` resource.

    Attributes:
        name (str):
            Required. A name of the ``LbTrafficExtension`` resource to
            get. Must be in the format
            ``projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLbTrafficExtensionRequest(proto.Message):
    r"""Message for creating a ``LbTrafficExtension`` resource.

    Attributes:
        parent (str):
            Required. The parent resource of the ``LbTrafficExtension``
            resource. Must be in the format
            ``projects/{project}/locations/{location}``.
        lb_traffic_extension_id (str):
            Required. User-provided ID of the ``LbTrafficExtension``
            resource to be created.
        lb_traffic_extension (google.cloud.network_services_v1beta1.types.LbTrafficExtension):
            Required. ``LbTrafficExtension`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lb_traffic_extension_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lb_traffic_extension: "LbTrafficExtension" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LbTrafficExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateLbTrafficExtensionRequest(proto.Message):
    r"""Message for updating a ``LbTrafficExtension`` resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Used to specify the fields to be overwritten in
            the ``LbTrafficExtension`` resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If the user does not specify a mask, then
            all fields are overwritten.
        lb_traffic_extension (google.cloud.network_services_v1beta1.types.LbTrafficExtension):
            Required. ``LbTrafficExtension`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    lb_traffic_extension: "LbTrafficExtension" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LbTrafficExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteLbTrafficExtensionRequest(proto.Message):
    r"""Message for deleting a ``LbTrafficExtension`` resource.

    Attributes:
        name (str):
            Required. The name of the ``LbTrafficExtension`` resource to
            delete. Must be in the format
            ``projects/{project}/locations/{location}/lbTrafficExtensions/{lb_traffic_extension}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class LbRouteExtension(proto.Message):
    r"""``LbRouteExtension`` is a resource that lets you control where
    traffic is routed to for a given request.

    Attributes:
        name (str):
            Required. Identifier. Name of the ``LbRouteExtension``
            resource in the following format:
            ``projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A human-readable description of the
            resource.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with the
            ``LbRouteExtension`` resource.

            The format must comply with `the requirements for
            labels <https://cloud.google.com/compute/docs/labeling-resources#requirements>`__
            for Google Cloud resources.
        forwarding_rules (MutableSequence[str]):
            Required. A list of references to the forwarding rules to
            which this service extension is attached to. At least one
            forwarding rule is required. There can be only one
            ``LbRouteExtension`` resource per forwarding rule.
        extension_chains (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionChain]):
            Required. A set of ordered extension chains
            that contain the match conditions and extensions
            to execute. Match conditions for each extension
            chain are evaluated in sequence for a given
            request. The first extension chain that has a
            condition that matches the request is executed.
            Any subsequent extension chains do not execute.
            Limited to 5 extension chains per resource.
        load_balancing_scheme (google.cloud.network_services_v1beta1.types.LoadBalancingScheme):
            Required. All backend services and forwarding rules
            referenced by this extension must share the same load
            balancing scheme. Supported values: ``INTERNAL_MANAGED``,
            ``EXTERNAL_MANAGED``. For more information, refer to
            `Choosing a load
            balancer <https://cloud.google.com/load-balancing/docs/backend-service>`__.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    forwarding_rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )
    extension_chains: MutableSequence["ExtensionChain"] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="ExtensionChain",
    )
    load_balancing_scheme: "LoadBalancingScheme" = proto.Field(
        proto.ENUM,
        number=8,
        enum="LoadBalancingScheme",
    )


class ListLbRouteExtensionsRequest(proto.Message):
    r"""Message for requesting list of ``LbRouteExtension`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``LbRouteExtension`` resources are listed, specified in the
            following format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. The server
            might return fewer items than requested. If
            unspecified, the server picks an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results that the server returns.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
    """

    parent: str = proto.Field(
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
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListLbRouteExtensionsResponse(proto.Message):
    r"""Message for response to listing ``LbRouteExtension`` resources.

    Attributes:
        lb_route_extensions (MutableSequence[google.cloud.network_services_v1beta1.types.LbRouteExtension]):
            The list of ``LbRouteExtension`` resources.
        next_page_token (str):
            A token identifying a page of results that
            the server returns.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    lb_route_extensions: MutableSequence["LbRouteExtension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LbRouteExtension",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetLbRouteExtensionRequest(proto.Message):
    r"""Message for getting a ``LbRouteExtension`` resource.

    Attributes:
        name (str):
            Required. A name of the ``LbRouteExtension`` resource to
            get. Must be in the format
            ``projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLbRouteExtensionRequest(proto.Message):
    r"""Message for creating a ``LbRouteExtension`` resource.

    Attributes:
        parent (str):
            Required. The parent resource of the ``LbRouteExtension``
            resource. Must be in the format
            ``projects/{project}/locations/{location}``.
        lb_route_extension_id (str):
            Required. User-provided ID of the ``LbRouteExtension``
            resource to be created.
        lb_route_extension (google.cloud.network_services_v1beta1.types.LbRouteExtension):
            Required. ``LbRouteExtension`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lb_route_extension_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lb_route_extension: "LbRouteExtension" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LbRouteExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateLbRouteExtensionRequest(proto.Message):
    r"""Message for updating a ``LbRouteExtension`` resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Used to specify the fields to be overwritten in
            the ``LbRouteExtension`` resource by the update. The fields
            specified in the update_mask are relative to the resource,
            not the full request. A field is overwritten if it is in the
            mask. If the user does not specify a mask, then all fields
            are overwritten.
        lb_route_extension (google.cloud.network_services_v1beta1.types.LbRouteExtension):
            Required. ``LbRouteExtension`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    lb_route_extension: "LbRouteExtension" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LbRouteExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteLbRouteExtensionRequest(proto.Message):
    r"""Message for deleting a ``LbRouteExtension`` resource.

    Attributes:
        name (str):
            Required. The name of the ``LbRouteExtension`` resource to
            delete. Must be in the format
            ``projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, ignores the second request. This prevents
            clients from accidentally creating duplicate
            commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ExtensionBinding(proto.Message):
    r"""``ExtensionBinding`` is a resource representing the attachment of an
    extension to a service.

    Attributes:
        name (str):
            Identifier. Name of the ``ExtensionBinding`` resource in the
            following format:
            ``projects/{project}/locations/{location}/extensionBindings/{extension_binding}``.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the resource
            was updated.
        description (str):
            Optional. A human-readable description of the
            resource.
        labels (MutableMapping[str, str]):
            Optional. Set of labels associated with the
            ``ExtensionBinding`` resource.

            The format must comply with `the following
            requirements <https://cloud.google.com/compute/docs/labeling-resources#requirements>`__.
        etag (str):
            Optional. Etag of the resource.
            If provided, it must match the server's etag. If
            the provided etag does not match the server's
            etag, the request will fail with a 409 ABORTED
            error.
        producer_extension (str):
            Required. The name of the extension that this binding should
            attach to target resources.

            Format: For Google-provided extensions, specify the service
            endpoint (see `Model Armor
            integration <https://docs.cloud.google.com/model-armor/integrations>`__)
        target (google.cloud.network_services_v1beta1.types.ExtensionBinding.Target):
            Required. Specifies a target to which this
            ``ExtensionBinding`` should be attached. The target can be
            either a single resource or a scope of resources.
        match_conditions (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition]):
            Optional. A list of match conditions to match
            against the incoming request. The extension will
            be invoked if at least one condition matches the
            request, or if no match conditions are
            specified. Limited to 5 conditions.
        fail_open (bool):
            Optional. Determines the behavior of the extension binding
            when the call to the extension fails or times out. Default
            value is ``FALSE``.

            When set to ``TRUE``, failures of the extension are silently
            ignored.
        producer_metadata (MutableMapping[str, str]):
            Optional. Additional metadata that should be
            passed to the attached extension with each
            request.
        priority (int):
            Optional. Priority of the extension binding.
            Lower numbers indicate higher priority. Priority
            of extension bindings are used to determine the
            order in which extension bindings are applied to
            a request.
    """

    class Target(proto.Message):
        r"""Specifies a list of targets to which this ``ExtensionBinding``
        should attach.

        Attributes:
            resources (MutableSequence[str]):
                Optional. The reference to the target resource, to which
                this binding should attach. Exactly one of ``resources`` or
                ``scope`` must be set.
            scope (google.cloud.network_services_v1beta1.types.ExtensionBinding.Target.Scope):
                Optional. Specifies the scope of resources to which this
                binding should attach. Exactly one of ``resources`` or
                ``scope`` must be set.
        """

        class Scope(proto.Message):
            r"""Specifies the scope of resources to which this binding should
            attach.

            Attributes:
                parent (str):
                    Required. Parent resource name specification, in the format:
                    ``projects/{project_number}``.
                resource_types (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding.Target.Scope.ResourceType]):
                    Required. Type of the resource to which the
                    binding should attach. Limited to 1 resource
                    type.
            """

            class ResourceType(proto.Enum):
                r"""Resource types that should be targeted by the binding.

                Values:
                    RESOURCE_TYPE_UNSPECIFIED (0):
                        Default value. Should not be used.
                    AI_APPLICATION (1):
                        AI Application resources.
                    AGENT_GATEWAY (2):
                        Agent Gateway resources.
                """

                RESOURCE_TYPE_UNSPECIFIED = 0
                AI_APPLICATION = 1
                AGENT_GATEWAY = 2

            parent: str = proto.Field(
                proto.STRING,
                number=1,
            )
            resource_types: MutableSequence[
                "ExtensionBinding.Target.Scope.ResourceType"
            ] = proto.RepeatedField(
                proto.ENUM,
                number=2,
                enum="ExtensionBinding.Target.Scope.ResourceType",
            )

        resources: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=1,
        )
        scope: "ExtensionBinding.Target.Scope" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ExtensionBinding.Target.Scope",
        )

    class MatchCondition(proto.Message):
        r"""Conditions to match against the incoming request.

        Attributes:
            to (google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To):
                Optional. Describes properties of a
                destination of a request. If specified, the
                extension will only be invoked on requests to
                destinations that match the specified criteria.
        """

        class StringMatch(proto.Message):
            r"""Specifies matching logic for string values.

            This message has `oneof`_ fields (mutually exclusive fields).
            For each oneof, at most one member field can be set at the same time.
            Setting any member of the oneof automatically clears all other
            members.

            .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

            Attributes:
                exact (str):
                    Optional. The input string must match exactly the string
                    specified here.

                    Examples:

                    - ``abc`` only matches the value ``abc``.

                    This field is a member of `oneof`_ ``match_pattern``.
                prefix (str):
                    Optional. The input string must have the prefix specified
                    here. Note: empty prefix is not allowed.

                    Examples:

                    - ``abc`` matches the value ``abc.xyz``

                    This field is a member of `oneof`_ ``match_pattern``.
                suffix (str):
                    Optional. The input string must have the suffix specified
                    here. Note: empty prefix is not allowed, please use regex
                    instead.

                    Examples:

                    - ``abc`` matches the value ``xyz.abc``

                    This field is a member of `oneof`_ ``match_pattern``.
                contains (str):
                    Optional. The input string must have the substring specified
                    here. Note: empty contains match is not allowed, please use
                    regex instead.

                    Examples:

                    - ``abc`` matches the value ``xyz.abc.def``

                    This field is a member of `oneof`_ ``match_pattern``.
                ignore_case (bool):
                    Optional. If true, indicates the
                    exact/prefix/suffix/contains matching should be case
                    insensitive. For example, the matcher ``data`` will match
                    both input string ``Data`` and ``data`` if set to true.
            """

            exact: str = proto.Field(
                proto.STRING,
                number=1,
                oneof="match_pattern",
            )
            prefix: str = proto.Field(
                proto.STRING,
                number=2,
                oneof="match_pattern",
            )
            suffix: str = proto.Field(
                proto.STRING,
                number=3,
                oneof="match_pattern",
            )
            contains: str = proto.Field(
                proto.STRING,
                number=4,
                oneof="match_pattern",
            )
            ignore_case: bool = proto.Field(
                proto.BOOL,
                number=5,
            )

        class HeaderMatch(proto.Message):
            r"""Determines how an HTTP header should be matched.

            Attributes:
                name (str):
                    Required. Specifies the name of the header in
                    the request.
                value (google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.StringMatch):
                    Optional. Specifies how the header match will
                    be performed.
            """

            name: str = proto.Field(
                proto.STRING,
                number=1,
            )
            value: "ExtensionBinding.MatchCondition.StringMatch" = proto.Field(
                proto.MESSAGE,
                number=2,
                message="ExtensionBinding.MatchCondition.StringMatch",
            )

        class To(proto.Message):
            r"""Describes properties of one or more destinations of a
            request.

            Attributes:
                destination (google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination):
                    Optional. Describes properties of destination of a request.
                    Within a destination, the match follows AND semantics across
                    fields and OR semantics within a field, i.e. a match occurs
                    when ANY path matches AND ANY header matches and ANY method
                    matches. At least one of destination or not_destination must
                    be specified.
                not_destination (google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination):
                    Optional. Describes the negated properties of the request
                    destination. Extension will not be invoked on requests that
                    match the criteria specified in this field. At least one of
                    destination or not_destination must be specified.
            """

            class Destination(proto.Message):
                r"""Describes properties of a single destination.

                Attributes:
                    header_set (google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.To.Destination.HeaderSet):
                        Optional. A set of HTTP headers to match
                        against. If not specified, requests with any
                        headers are matched.
                    resources (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.StringMatch]):
                        Optional. A list of non-empty strings whose
                        value is matched against the resource to which a
                        request is sent (e.g., an Agent in
                        AiApplication). If not specified, any resource
                        is allowed. If specified, a match occurs if any
                        of the resources matches the resource value in
                        the request. Limited to 5 resources. When
                        matching against resources in the AgentRegistry,
                        use the URNs of the registry resources.
                    hosts (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.StringMatch]):
                        Optional. A list of HTTP Hosts to match
                        against. Limited to 10 hosts. If not specified,
                        any host is allowed. If specified, a match
                        occurs if any of the hosts matches the host
                        value in the request.
                    paths (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.StringMatch]):
                        Optional. A list of paths to match against.
                        Limited to 10 paths. If not specified, any path
                        is allowed.

                        Note that this path match includes the query
                        parameters. For gRPC services, this should be a
                        fully-qualified name of the form
                        /package.service/method.
                """

                class HeaderSet(proto.Message):
                    r"""Describes a set of HTTP headers to match against.

                    Attributes:
                        headers (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding.MatchCondition.HeaderMatch]):
                            Required. A list of headers to match against
                            in http header. If multiple header matches are
                            provided, they will be evaluated as an AND, i.e.
                            all header matches must match for the request to
                            match.
                    """

                    headers: MutableSequence[
                        "ExtensionBinding.MatchCondition.HeaderMatch"
                    ] = proto.RepeatedField(
                        proto.MESSAGE,
                        number=1,
                        message="ExtensionBinding.MatchCondition.HeaderMatch",
                    )

                header_set: "ExtensionBinding.MatchCondition.To.Destination.HeaderSet" = proto.Field(
                    proto.MESSAGE,
                    number=1,
                    message="ExtensionBinding.MatchCondition.To.Destination.HeaderSet",
                )
                resources: MutableSequence[
                    "ExtensionBinding.MatchCondition.StringMatch"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=2,
                    message="ExtensionBinding.MatchCondition.StringMatch",
                )
                hosts: MutableSequence[
                    "ExtensionBinding.MatchCondition.StringMatch"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=3,
                    message="ExtensionBinding.MatchCondition.StringMatch",
                )
                paths: MutableSequence[
                    "ExtensionBinding.MatchCondition.StringMatch"
                ] = proto.RepeatedField(
                    proto.MESSAGE,
                    number=4,
                    message="ExtensionBinding.MatchCondition.StringMatch",
                )

            destination: "ExtensionBinding.MatchCondition.To.Destination" = proto.Field(
                proto.MESSAGE,
                number=1,
                message="ExtensionBinding.MatchCondition.To.Destination",
            )
            not_destination: "ExtensionBinding.MatchCondition.To.Destination" = (
                proto.Field(
                    proto.MESSAGE,
                    number=2,
                    message="ExtensionBinding.MatchCondition.To.Destination",
                )
            )

        to: "ExtensionBinding.MatchCondition.To" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="ExtensionBinding.MatchCondition.To",
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    producer_extension: str = proto.Field(
        proto.STRING,
        number=7,
    )
    target: Target = proto.Field(
        proto.MESSAGE,
        number=8,
        message=Target,
    )
    match_conditions: MutableSequence[MatchCondition] = proto.RepeatedField(
        proto.MESSAGE,
        number=9,
        message=MatchCondition,
    )
    fail_open: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    producer_metadata: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=11,
    )
    priority: int = proto.Field(
        proto.INT32,
        number=12,
    )


class ListExtensionBindingsRequest(proto.Message):
    r"""Request used with the ``ListExtensionBindings`` method.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``ExtensionBinding`` resources should be listed, specified
            in the format ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Maximum number of ``ExtensionBinding`` resources
            to return per call.
        page_token (str):
            Optional. The value returned by the last
            ``ListExtensionBindingsResponse`` Indicates that this is a
            continuation of a prior ``ListExtensionBindings`` call, and
            that the system should return the next page of data.
    """

    parent: str = proto.Field(
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


class ListExtensionBindingsResponse(proto.Message):
    r"""Response returned by the ``ListExtensionBindings`` method.

    Attributes:
        extension_bindings (MutableSequence[google.cloud.network_services_v1beta1.types.ExtensionBinding]):
            List of ``ExtensionBinding`` resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Unordered list. Unreachable resources. Populated when the
            request attempts to list all resources across all supported
            locations, while some locations are temporarily unavailable.
            The resource names are in the format
            ``projects/{project}/locations/{location}/extensionBindings/{extension_binding}``.
    """

    @property
    def raw_page(self):
        return self

    extension_bindings: MutableSequence["ExtensionBinding"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ExtensionBinding",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetExtensionBindingRequest(proto.Message):
    r"""Request used by the ``GetExtensionBinding`` method.

    Attributes:
        name (str):
            Required. A name of the ``ExtensionBinding`` resource to
            get. Must be in the format
            ``projects/{project}/locations/{location}/extensionBindings/{extension_binding}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateExtensionBindingRequest(proto.Message):
    r"""Request used by the ``CreateExtensionBinding`` method.

    Attributes:
        parent (str):
            Required. The parent resource of the ``ExtensionBinding``
            resource. Must be in the format
            ``projects/{project}/locations/{location}``.
        extension_binding_id (str):
            Required. Short name of the ``ExtensionBinding`` resource to
            be created.
        extension_binding (google.cloud.network_services_v1beta1.types.ExtensionBinding):
            Required. ``ExtensionBinding`` resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    extension_binding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    extension_binding: "ExtensionBinding" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="ExtensionBinding",
    )


class UpdateExtensionBindingRequest(proto.Message):
    r"""Request used by the ``UpdateExtensionBinding`` method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the ``ExtensionBinding`` resource by the
            update. The fields specified in the update_mask are relative
            to the resource, not the full request. A field will be
            overwritten if it is in the mask. If the user does not
            provide a mask then all fields will be overwritten.
        extension_binding (google.cloud.network_services_v1beta1.types.ExtensionBinding):
            Required. Updated ``ExtensionBinding`` resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    extension_binding: "ExtensionBinding" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExtensionBinding",
    )


class DeleteExtensionBindingRequest(proto.Message):
    r"""Request used by the ``DeleteExtensionBinding`` method.

    Attributes:
        name (str):
            Required. A name of the ``ExtensionBinding`` resource to
            delete. Must be in the format
            ``projects/{project}/locations/{location}/extensionBindings/{extension_binding}``.
        etag (str):
            Optional. The etag of the ExtensionBinding to
            delete.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
