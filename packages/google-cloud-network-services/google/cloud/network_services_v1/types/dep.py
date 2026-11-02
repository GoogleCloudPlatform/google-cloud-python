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

__protobuf__ = proto.module(
    package="google.cloud.networkservices.v1",
    manifest={
        "EventType",
        "LoadBalancingScheme",
        "WireFormat",
        "BodySendMode",
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
        "LbEdgeExtension",
        "ListLbEdgeExtensionsRequest",
        "ListLbEdgeExtensionsResponse",
        "GetLbEdgeExtensionRequest",
        "CreateLbEdgeExtensionRequest",
        "UpdateLbEdgeExtensionRequest",
        "DeleteLbEdgeExtensionRequest",
        "AuthzExtension",
        "ListAuthzExtensionsRequest",
        "ListAuthzExtensionsResponse",
        "GetAuthzExtensionRequest",
        "CreateAuthzExtensionRequest",
        "UpdateAuthzExtensionRequest",
        "DeleteAuthzExtensionRequest",
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
    r"""Load balancing schemes supported by the ``LbTrafficExtension``,
    ``LbRouteExtension``, and ``LbEdgeExtension`` resources. For more
    information, refer to `Backend services
    overview <https://cloud.google.com/load-balancing/docs/backend-service>`__.

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


class WireFormat(proto.Enum):
    r"""The format of communication supported by the extension.

    Values:
        WIRE_FORMAT_UNSPECIFIED (0):
            Not specified.
        EXT_PROC_GRPC (1):
            The extension service uses ext_proc gRPC API over a gRPC
            stream. This is the default value if the wire format is not
            specified. The backend service for the extension must use
            HTTP2 or H2C as the protocol. All ``supported_events`` for a
            client request are sent as part of the same gRPC stream.
        EXT_AUTHZ_GRPC (3):
            The extension service uses Envoy's ``ext_authz`` gRPC API.
            The backend service for the extension must use HTTP2 or H2C
            as the protocol. ``EXT_AUTHZ_GRPC`` is only supported for
            regional ``AuthzExtension`` resources.
    """

    WIRE_FORMAT_UNSPECIFIED = 0
    EXT_PROC_GRPC = 1
    EXT_AUTHZ_GRPC = 3


class BodySendMode(proto.Enum):
    r"""The send mode for body processing.

    Values:
        BODY_SEND_MODE_UNSPECIFIED (0):
            Default value. Do not use.
        BODY_SEND_MODE_STREAMED (1):
            Calls to the extension are executed in the
            streamed mode. Subsequent chunks will be sent
            only after the previous chunks have been
            processed.

            The content of the body chunks is sent one way
            to the extension. Extension may send modified
            chunks back.

            This is the default value if the processing mode
            is not specified.
        BODY_SEND_MODE_FULL_DUPLEX_STREAMED (2):
            Calls are executed in the full duplex mode. Subsequent
            chunks will be sent for processing without waiting for the
            response for the previous chunk or for the response for
            ``REQUEST_HEADERS`` event.

            Extension can freely modify or chunk the body contents. If
            the extension doesn't send the body contents back, the next
            extension in the chain or the upstream will receive an empty
            body.
    """

    BODY_SEND_MODE_UNSPECIFIED = 0
    BODY_SEND_MODE_STREAMED = 1
    BODY_SEND_MODE_FULL_DUPLEX_STREAMED = 2


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
        match_condition (google.cloud.network_services_v1.types.ExtensionChain.MatchCondition):
            Required. Conditions under which this chain
            is invoked for a request.
        extensions (MutableSequence[google.cloud.network_services_v1.types.ExtensionChain.Extension]):
            Required. A set of extensions to execute for the matching
            request. At least one extension is required. Up to 3
            extensions can be defined for each extension chain for
            ``LbTrafficExtension`` resource. ``LbRouteExtension`` and
            ``LbEdgeExtension`` chains are limited to 1 extension per
            extension chain.
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
                Optional. The name for this extension.
                The name is logged as part of the HTTP request
                logs. The name must conform with RFC-1034, is
                restricted to lower-cased letters, numbers and
                hyphens, and can have a maximum length of 63
                characters. Additionally, the first character
                must be a letter and the last a letter or a
                number.

                This field is required except for
                AuthzExtension.
            authority (str):
                Optional. The ``:authority`` header in the gRPC request sent
                from Envoy to the extension service. Required for Callout
                extensions.

                This field is not supported for plugin extensions. Setting
                it results in a validation error.
            service (str):
                Required. The reference to the service that runs the
                extension.

                To configure a callout extension, ``service`` must be a
                fully-qualified reference to a `backend
                service <https://cloud.google.com/compute/docs/reference/rest/v1/backendServices>`__
                in the format:
                ``https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}``
                or
                ``https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}``.

                To configure a plugin extension, ``service`` must be a
                reference to a ```WasmPlugin``
                resource <https://cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.wasmPlugins>`__
                in the format:
                ``projects/{project}/locations/{location}/wasmPlugins/{plugin}``
                or
                ``//networkservices.googleapis.com/projects/{project}/locations/{location}/wasmPlugins/{wasmPlugin}``.

                Plugin extensions are currently supported for the
                ``LbTrafficExtension``, the ``LbRouteExtension``, and the
                ``LbEdgeExtension`` resources.
            supported_events (MutableSequence[google.cloud.network_services_v1.types.EventType]):
                Optional. A set of events during request or response
                processing for which this extension is called.

                For the ``LbTrafficExtension`` resource, this field is
                required.

                For the ``LbRouteExtension`` resource, this field is
                optional. If unspecified, ``REQUEST_HEADERS`` event is
                assumed as supported.

                For the ``LbEdgeExtension`` resource, this field is required
                and must only contain ``REQUEST_HEADERS`` event.

                For the ``AuthzExtension`` resource, this field is optional.
                ``REQUEST_HEADERS`` is the only supported event. If
                unspecified, ``REQUEST_HEADERS`` event is assumed as
                supported.
            timeout (google.protobuf.duration_pb2.Duration):
                Optional. Specifies the timeout for each individual message
                on the stream. The timeout must be between ``10``-``10000``
                milliseconds. Required for callout extensions.

                This field is not supported for plugin extensions. Setting
                it results in a validation error.
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
            forward_attributes (MutableSequence[str]):
                Optional. List of the Envoy attributes to forward to the
                extension server. The attributes provided here are included
                as part of the ``ProcessingRequest.attributes`` field (of
                type ``map<string, google.protobuf.Struct>``), where the
                keys are the attribute names. Refer to the
                `documentation <https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference#attributes>`__
                for the names of attributes that can be forwarded. If
                omitted, no attributes are sent. Each element is a string
                indicating the attribute name.
            metadata (google.protobuf.struct_pb2.Struct):
                Optional. The metadata provided here is included as part of
                the ``metadata_context`` (of type
                ``google.protobuf.Struct``) in the ``ProcessingRequest``
                message sent to the extension server.

                For ``AuthzExtension`` resources, the metadata is available
                under the namespace
                ``com.google.authz_extension.<resource_name>``. For other
                types of extensions, the metadata is available under the
                namespace
                ``com.google.<extension_type>.<resource_name>.<extension_chain_name>.<extension_name>``.
                For example:
                ``com.google.lb_traffic_extension.lbtrafficextension1.chain1.ext1``.

                The following variables are supported in the metadata:

                ``{forwarding_rule_id}`` - substituted with the forwarding
                rule's fully qualified resource name.

                This field must not be set for plugin extensions. Setting it
                results in a validation error.

                You can set metadata at either the resource level or the
                extension level. The extension level metadata is recommended
                because you can pass a different set of metadata through
                each extension to the backend.

                This field is subject to following limitations:

                - The total size of the metadata must be less than 1KiB.
                - The total number of keys in the metadata must be less than
                  16.
                - The length of each key must be less than 64 characters.
                - The length of each value must be less than 1024
                  characters.
                - All values must be strings.
            request_body_send_mode (google.cloud.network_services_v1.types.BodySendMode):
                Optional. Configures the send mode for request body
                processing.

                The field can only be set if ``supported_events`` includes
                ``REQUEST_BODY``. If ``supported_events`` includes
                ``REQUEST_BODY``, but ``request_body_send_mode`` is unset,
                the default value ``STREAMED`` is used.

                When this field is set to ``FULL_DUPLEX_STREAMED``,
                ``supported_events`` must include both ``REQUEST_BODY`` and
                ``REQUEST_TRAILERS``.

                This field can be set only for ``LbTrafficExtension`` and
                ``LbRouteExtension`` resources, and only when the
                ``service`` field of the extension points to a
                ``BackendService``. Only ``FULL_DUPLEX_STREAMED`` mode is
                supported for ``LbRouteExtension`` resources.
            response_body_send_mode (google.cloud.network_services_v1.types.BodySendMode):
                Optional. Configures the send mode for response processing.
                If unspecified, the default value ``STREAMED`` is used.

                The field can only be set if ``supported_events`` includes
                ``RESPONSE_BODY``. If ``supported_events`` includes
                ``RESPONSE_BODY``, but ``response_body_send_mode`` is unset,
                the default value ``STREAMED`` is used.

                When this field is set to ``FULL_DUPLEX_STREAMED``,
                ``supported_events`` must include both ``RESPONSE_BODY`` and
                ``RESPONSE_TRAILERS``.

                This field can be set only for ``LbTrafficExtension``
                resources, and only when the ``service`` field of the
                extension points to a ``BackendService``.
            observability_mode (bool):
                Optional. When set to ``true``, the calls to the extension
                backend are performed asynchronously, without pausing the
                processing of the ongoing request. In this mode, only
                ``STREAMED`` (default) body processing is supported.
                Responses, if any, are ignored.

                Supported by regional ``LbTrafficExtension`` and
                ``LbRouteExtension`` resources.
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
        forward_attributes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=8,
        )
        metadata: struct_pb2.Struct = proto.Field(
            proto.MESSAGE,
            number=9,
            message=struct_pb2.Struct,
        )
        request_body_send_mode: "BodySendMode" = proto.Field(
            proto.ENUM,
            number=14,
            enum="BodySendMode",
        )
        response_body_send_mode: "BodySendMode" = proto.Field(
            proto.ENUM,
            number=15,
            enum="BodySendMode",
        )
        observability_mode: bool = proto.Field(
            proto.BOOL,
            number=16,
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
            Optional. A list of references to the forwarding rules to
            which this service extension is attached. At least one
            forwarding rule is required. Only one ``LbTrafficExtension``
            resource can be associated with a forwarding rule.
        extension_chains (MutableSequence[google.cloud.network_services_v1.types.ExtensionChain]):
            Required. A set of ordered extension chains
            that contain the match conditions and extensions
            to execute. Match conditions for each extension
            chain are evaluated in sequence for a given
            request. The first extension chain that has a
            condition that matches the request is executed.
            Any subsequent extension chains do not execute.
            Limited to 5 extension chains per resource.
        load_balancing_scheme (google.cloud.network_services_v1.types.LoadBalancingScheme):
            Required. All backend services and forwarding rules
            referenced by this extension must share the same load
            balancing scheme. Supported values: ``INTERNAL_MANAGED`` and
            ``EXTERNAL_MANAGED``. For more information, refer to
            `Backend services
            overview <https://cloud.google.com/load-balancing/docs/backend-service>`__.
        metadata (google.protobuf.struct_pb2.Struct):
            Optional. The metadata provided here is included as part of
            the ``metadata_context`` (of type
            ``google.protobuf.Struct``) in the ``ProcessingRequest``
            message sent to the extension server.

            The metadata applies to all extensions in all extensions
            chains in this resource.

            The metadata is available under the key
            ``com.google.lb_traffic_extension.<resource_name>``.

            The following variables are supported in the metadata:

            ``{forwarding_rule_id}`` - substituted with the forwarding
            rule's fully qualified resource name.

            This field must not be set if at least one of the extension
            chains contains plugin extensions. Setting it results in a
            validation error.

            You can set metadata at either the resource level or the
            extension level. The extension level metadata is recommended
            because you can pass a different set of metadata through
            each extension to the backend.
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
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )


class ListLbTrafficExtensionsRequest(proto.Message):
    r"""Message for requesting list of ``LbTrafficExtension`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``LbTrafficExtension`` resources are listed. These values
            are specified in the following format:
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
            Optional. Hint about how to order the
            results.
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
        lb_traffic_extensions (MutableSequence[google.cloud.network_services_v1.types.LbTrafficExtension]):
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
        lb_traffic_extension (google.cloud.network_services_v1.types.LbTrafficExtension):
            Required. ``LbTrafficExtension`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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
            Optional. Used to specify the fields to be overwritten in
            the ``LbTrafficExtension`` resource by the update. The
            fields specified in the ``update_mask`` are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If the user does not specify a mask, then
            all fields are overwritten.
        lb_traffic_extension (google.cloud.network_services_v1.types.LbTrafficExtension):
            Required. ``LbTrafficExtension`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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
            completed. The server guarantees that for 60
            minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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
            which this service extension is attached. At least one
            forwarding rule is required. Only one ``LbRouteExtension``
            resource can be associated with a forwarding rule.
        extension_chains (MutableSequence[google.cloud.network_services_v1.types.ExtensionChain]):
            Required. A set of ordered extension chains
            that contain the match conditions and extensions
            to execute. Match conditions for each extension
            chain are evaluated in sequence for a given
            request. The first extension chain that has a
            condition that matches the request is executed.
            Any subsequent extension chains do not execute.
            Limited to 5 extension chains per resource.
        load_balancing_scheme (google.cloud.network_services_v1.types.LoadBalancingScheme):
            Required. All backend services and forwarding rules
            referenced by this extension must share the same load
            balancing scheme. Supported values: ``INTERNAL_MANAGED``,
            ``EXTERNAL_MANAGED``. For more information, refer to
            `Backend services
            overview <https://cloud.google.com/load-balancing/docs/backend-service>`__.
        metadata (google.protobuf.struct_pb2.Struct):
            Optional. The metadata provided here is included as part of
            the ``metadata_context`` (of type
            ``google.protobuf.Struct``) in the ``ProcessingRequest``
            message sent to the extension server.

            The metadata applies to all extensions in all extensions
            chains in this resource.

            The metadata is available under the key
            ``com.google.lb_route_extension.<resource_name>``.

            The following variables are supported in the metadata:

            ``{forwarding_rule_id}`` - substituted with the forwarding
            rule's fully qualified resource name.

            This field must not be set if at least one of the extension
            chains contains plugin extensions. Setting it results in a
            validation error.

            You can set metadata at either the resource level or the
            extension level. The extension level metadata is recommended
            because you can pass a different set of metadata through
            each extension to the backend.
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
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=10,
        message=struct_pb2.Struct,
    )


class ListLbRouteExtensionsRequest(proto.Message):
    r"""Message for requesting list of ``LbRouteExtension`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``LbRouteExtension`` resources are listed. These values are
            specified in the following format:
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
            Optional. Hint about how to order the
            results.
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
        lb_route_extensions (MutableSequence[google.cloud.network_services_v1.types.LbRouteExtension]):
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
        lb_route_extension (google.cloud.network_services_v1.types.LbRouteExtension):
            Required. ``LbRouteExtension`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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
            Optional. Used to specify the fields to be overwritten in
            the ``LbRouteExtension`` resource by the update. The fields
            specified in the ``update_mask`` are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If the user does not specify a mask, then
            all fields are overwritten.
        lb_route_extension (google.cloud.network_services_v1.types.LbRouteExtension):
            Required. ``LbRouteExtension`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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
            completed. The server guarantees that for 60
            minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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


class LbEdgeExtension(proto.Message):
    r"""``LbEdgeExtension`` is a resource that lets the extension service
    influence the selection of backend services and Cloud CDN cache keys
    by modifying request headers.

    Attributes:
        name (str):
            Required. Identifier. Name of the ``LbEdgeExtension``
            resource in the following format:
            ``projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}``.
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
            ``LbEdgeExtension`` resource.

            The format must comply with `the requirements for
            labels <https://cloud.google.com/compute/docs/labeling-resources#requirements>`__
            for Google Cloud resources.
        forwarding_rules (MutableSequence[str]):
            Required. A list of references to the forwarding rules to
            which this service extension is attached. At least one
            forwarding rule is required. Only one ``LbEdgeExtension``
            resource can be associated with a forwarding rule.
        extension_chains (MutableSequence[google.cloud.network_services_v1.types.ExtensionChain]):
            Required. A set of ordered extension chains
            that contain the match conditions and extensions
            to execute. Match conditions for each extension
            chain are evaluated in sequence for a given
            request. The first extension chain that has a
            condition that matches the request is executed.
            Any subsequent extension chains do not execute.
            Limited to 5 extension chains per resource.
        load_balancing_scheme (google.cloud.network_services_v1.types.LoadBalancingScheme):
            Required. All forwarding rules referenced by this extension
            must share the same load balancing scheme. Supported values:
            ``EXTERNAL_MANAGED``.
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
        number=6,
        message="ExtensionChain",
    )
    load_balancing_scheme: "LoadBalancingScheme" = proto.Field(
        proto.ENUM,
        number=7,
        enum="LoadBalancingScheme",
    )


class ListLbEdgeExtensionsRequest(proto.Message):
    r"""Message for requesting list of ``LbEdgeExtension`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``LbEdgeExtension`` resources are listed. These values are
            specified in the following format:
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
            Optional. Hint about how to order the
            results.
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


class ListLbEdgeExtensionsResponse(proto.Message):
    r"""Message for response to listing ``LbEdgeExtension`` resources.

    Attributes:
        lb_edge_extensions (MutableSequence[google.cloud.network_services_v1.types.LbEdgeExtension]):
            The list of ``LbEdgeExtension`` resources.
        next_page_token (str):
            A token identifying a page of results that
            the server returns.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    lb_edge_extensions: MutableSequence["LbEdgeExtension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="LbEdgeExtension",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetLbEdgeExtensionRequest(proto.Message):
    r"""Message for getting a ``LbEdgeExtension`` resource.

    Attributes:
        name (str):
            Required. A name of the ``LbEdgeExtension`` resource to get.
            Must be in the format
            ``projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateLbEdgeExtensionRequest(proto.Message):
    r"""Message for creating a ``LbEdgeExtension`` resource.

    Attributes:
        parent (str):
            Required. The parent resource of the ``LbEdgeExtension``
            resource. Must be in the format
            ``projects/{project}/locations/{location}``.
        lb_edge_extension_id (str):
            Required. User-provided ID of the ``LbEdgeExtension``
            resource to be created.
        lb_edge_extension (google.cloud.network_services_v1.types.LbEdgeExtension):
            Required. ``LbEdgeExtension`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    lb_edge_extension_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    lb_edge_extension: "LbEdgeExtension" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="LbEdgeExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateLbEdgeExtensionRequest(proto.Message):
    r"""Message for updating a ``LbEdgeExtension`` resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Used to specify the fields to be overwritten in
            the ``LbEdgeExtension`` resource by the update. The fields
            specified in the ``update_mask`` are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If the user does not specify a mask, then
            all fields are overwritten.
        lb_edge_extension (google.cloud.network_services_v1.types.LbEdgeExtension):
            Required. ``LbEdgeExtension`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    lb_edge_extension: "LbEdgeExtension" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="LbEdgeExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteLbEdgeExtensionRequest(proto.Message):
    r"""Message for deleting a ``LbEdgeExtension`` resource.

    Attributes:
        name (str):
            Required. The name of the ``LbEdgeExtension`` resource to
            delete. Must be in the format
            ``projects/{project}/locations/{location}/lbEdgeExtensions/{lb_edge_extension}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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


class AuthzExtension(proto.Message):
    r"""``AuthzExtension`` is a resource that allows traffic forwarding to a
    callout backend service to make an authorization decision.

    Attributes:
        name (str):
            Required. Identifier. Name of the ``AuthzExtension``
            resource in the following format:
            ``projects/{project}/locations/{location}/authzExtensions/{authz_extension}``.
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
            ``AuthzExtension`` resource.

            The format must comply with `the requirements for
            labels </compute/docs/labeling-resources#requirements>`__
            for Google Cloud resources.
        load_balancing_scheme (google.cloud.network_services_v1.types.LoadBalancingScheme):
            Optional. All backend services and forwarding rules
            referenced by this extension must share the same load
            balancing scheme. Supported values: ``INTERNAL_MANAGED``,
            ``EXTERNAL_MANAGED``. Can be omitted for AuthzExtensions
            that do not reference a backend service. For more
            information, refer to `Backend services
            overview <https://cloud.google.com/load-balancing/docs/backend-service>`__.
        authority (str):
            Optional. The ``:authority`` header in the gRPC request sent
            from Envoy to the extension service. It is required when the
            ``service`` field points to a backend service or a wasm
            plugin.
        service (str):
            Required. The reference to the service that runs the
            extension.

            To configure a callout extension, ``service`` must be a
            fully-qualified reference to a `backend
            service <https://cloud.google.com/compute/docs/reference/rest/v1/backendServices>`__
            in the format:
            ``https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/backendServices/{backendService}``
            or
            ``https://www.googleapis.com/compute/v1/projects/{project}/global/backendServices/{backendService}``.
        timeout (google.protobuf.duration_pb2.Duration):
            Required. Specifies the timeout for each
            individual message on the stream. The timeout
            must be between 10-10000 milliseconds.
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
        metadata (google.protobuf.struct_pb2.Struct):
            Optional. The metadata provided here is included as part of
            the ``metadata_context`` (of type
            ``google.protobuf.Struct``) in the ``ProcessingRequest``
            message sent to the extension server. The metadata is
            available under the namespace
            ``com.google.authz_extension.<resource_name>``. The
            following variables are supported in the metadata Struct:

            ``{forwarding_rule_id}`` - substituted with the forwarding
            rule's fully qualified resource name.
        forward_headers (MutableSequence[str]):
            Optional. List of the HTTP headers to forward
            to the extension (from the client). If omitted,
            all headers are sent. Each element is a string
            indicating the header name.
        forward_attributes (MutableSequence[str]):
            Optional. List of the Envoy attributes to forward to the
            extension server. The attributes provided here are included
            as part of the ``ProcessingRequest.attributes`` field (of
            type ``map<string, google.protobuf.Struct>``), where the
            keys are the attribute names. Refer to the
            `documentation <https://cloud.google.com/service-extensions/docs/cel-matcher-language-reference#attributes>`__
            for the names of attributes that can be forwarded. If
            omitted, no attributes are sent. Each element is a string
            indicating the attribute name.
        wire_format (google.cloud.network_services_v1.types.WireFormat):
            Optional. The format of communication supported by the
            callout extension. This field is supported only for regional
            ``AuthzExtension`` resources. If not specified, the default
            value ``EXT_PROC_GRPC`` is used. Global ``AuthzExtension``
            resources use the ``EXT_PROC_GRPC`` wire format.
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
        number=4,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    load_balancing_scheme: "LoadBalancingScheme" = proto.Field(
        proto.ENUM,
        number=6,
        enum="LoadBalancingScheme",
    )
    authority: str = proto.Field(
        proto.STRING,
        number=7,
    )
    service: str = proto.Field(
        proto.STRING,
        number=8,
    )
    timeout: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=9,
        message=duration_pb2.Duration,
    )
    fail_open: bool = proto.Field(
        proto.BOOL,
        number=10,
    )
    metadata: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=11,
        message=struct_pb2.Struct,
    )
    forward_headers: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=12,
    )
    forward_attributes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )
    wire_format: "WireFormat" = proto.Field(
        proto.ENUM,
        number=14,
        enum="WireFormat",
    )


class ListAuthzExtensionsRequest(proto.Message):
    r"""Message for requesting list of ``AuthzExtension`` resources.

    Attributes:
        parent (str):
            Required. The project and location from which the
            ``AuthzExtension`` resources are listed. These values are
            specified in the following format:
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
            Optional. Hint about how to order the
            results.
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


class ListAuthzExtensionsResponse(proto.Message):
    r"""Message for response to listing ``AuthzExtension`` resources.

    Attributes:
        authz_extensions (MutableSequence[google.cloud.network_services_v1.types.AuthzExtension]):
            The list of ``AuthzExtension`` resources.
        next_page_token (str):
            A token identifying a page of results that
            the server returns.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    authz_extensions: MutableSequence["AuthzExtension"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AuthzExtension",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetAuthzExtensionRequest(proto.Message):
    r"""Message for getting a ``AuthzExtension`` resource.

    Attributes:
        name (str):
            Required. A name of the ``AuthzExtension`` resource to get.
            Must be in the format
            ``projects/{project}/locations/{location}/authzExtensions/{authz_extension}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateAuthzExtensionRequest(proto.Message):
    r"""Message for creating a ``AuthzExtension`` resource.

    Attributes:
        parent (str):
            Required. The parent resource of the ``AuthzExtension``
            resource. Must be in the format
            ``projects/{project}/locations/{location}``.
        authz_extension_id (str):
            Required. User-provided ID of the ``AuthzExtension``
            resource to be created.
        authz_extension (google.cloud.network_services_v1.types.AuthzExtension):
            Required. ``AuthzExtension`` resource to be created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    authz_extension_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    authz_extension: "AuthzExtension" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AuthzExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateAuthzExtensionRequest(proto.Message):
    r"""Message for updating a ``AuthzExtension`` resource.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Used to specify the fields to be overwritten in
            the ``AuthzExtension`` resource by the update. The fields
            specified in the ``update_mask`` are relative to the
            resource, not the full request. A field is overwritten if it
            is in the mask. If the user does not specify a mask, then
            all fields are overwritten.
        authz_extension (google.cloud.network_services_v1.types.AuthzExtension):
            Required. ``AuthzExtension`` resource being updated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    authz_extension: "AuthzExtension" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="AuthzExtension",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteAuthzExtensionRequest(proto.Message):
    r"""Message for deleting a ``AuthzExtension`` resource.

    Attributes:
        name (str):
            Required. The name of the ``AuthzExtension`` resource to
            delete. Must be in the format
            ``projects/{project}/locations/{location}/authzExtensions/{authz_extension}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server can
            ignore the request if it has already been
            completed. The server guarantees that for 60
            minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server ignores the second request This
            prevents clients from accidentally creating
            duplicate commitments.

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


__all__ = tuple(sorted(__protobuf__.manifest))
