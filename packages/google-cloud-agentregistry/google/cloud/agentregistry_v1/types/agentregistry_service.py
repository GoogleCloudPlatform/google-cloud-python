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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.agentregistry_v1.types import agent, endpoint, mcp_server
from google.cloud.agentregistry_v1.types import binding as gca_binding
from google.cloud.agentregistry_v1.types import service as gca_service

__protobuf__ = proto.module(
    package="google.cloud.agentregistry.v1",
    manifest={
        "ListAgentsRequest",
        "ListAgentsResponse",
        "SearchAgentsRequest",
        "SearchAgentsResponse",
        "GetAgentRequest",
        "ListEndpointsRequest",
        "ListEndpointsResponse",
        "GetEndpointRequest",
        "ListMcpServersRequest",
        "ListMcpServersResponse",
        "SearchMcpServersRequest",
        "SearchMcpServersResponse",
        "GetMcpServerRequest",
        "ListServicesRequest",
        "ListServicesResponse",
        "GetServiceRequest",
        "CreateServiceRequest",
        "FetchAvailableBindingsRequest",
        "FetchAvailableBindingsResponse",
        "UpdateServiceRequest",
        "DeleteServiceRequest",
        "OperationMetadata",
        "ListBindingsRequest",
        "ListBindingsResponse",
        "GetBindingRequest",
        "CreateBindingRequest",
        "UpdateBindingRequest",
        "DeleteBindingRequest",
    },
)


class ListAgentsRequest(proto.Message):
    r"""Message for requesting list of Agents

    Attributes:
        parent (str):
            Required. Parent value for ListAgentsRequest
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListAgentsResponse(proto.Message):
    r"""Message for response to listing Agents

    Attributes:
        agents (MutableSequence[google.cloud.agentregistry_v1.types.Agent]):
            The list of Agents.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    agents: MutableSequence[agent.Agent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=agent.Agent,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchAgentsRequest(proto.Message):
    r"""Message for searching Agents

    Attributes:
        parent (str):
            Required. Parent value for SearchAgentsRequest. Format:
            ``projects/{project}/locations/{location}``.
        search_string (str):
            Optional. Search criteria used to select the Agents to
            return. If no search criteria is specified then all
            accessible Agents will be returned.

            Search expressions can be used to restrict results based
            upon searchable fields, where the operators can be used
            along with the suffix wildcard symbol ``*``. See
            `instructions <https://docs.cloud.google.com/agent-registry/search-agents-and-tools>`__
            for more details.

            Allowed operators: ``=``, ``:``, ``NOT``, ``AND``, ``OR``,
            and ``()``.

            Searchable fields:

            \| Field \| ``=`` \| ``:`` \| ``*`` \| Keyword Search \|
            \|--------------------\|-----\|-----\|-----\|----------------\|
            \| agentId \| Yes \| Yes \| Yes \| Included \| \| name \| No
            \| Yes \| Yes \| Included \| \| displayName \| No \| Yes \|
            Yes \| Included \| \| description \| No \| Yes \| No \|
            Included \| \| skills \| No \| Yes \| No \| Included \| \|
            skills.id \| No \| Yes \| No \| Included \| \| skills.name
            \| No \| Yes \| No \| Included \| \| skills.description \|
            No \| Yes \| No \| Included \| \| skills.tags \| No \| Yes
            \| No \| Included \| \| skills.examples \| No \| Yes \| No
            \| Included \|

            Examples:

            - ``agentId="urn:agent:projects-123:projects:123:locations:us-central1:reasoningEngines:1234"``
              to find the agent with the specified agent ID.
            - ``name:important`` to find agents whose name contains
              ``important`` as a word.
            - ``displayName:works*`` to find agents whose display name
              contains words that start with ``works``.
            - ``skills.tags:test`` to find agents whose skills tags
              contain ``test``.
            - ``planner OR booking`` to find agents whose metadata
              contains the words ``planner`` or ``booking``.
        page_size (int):
            Optional. The maximum number of search results to return per
            page. The page size is capped at ``100``, even if a larger
            value is specified. A negative value will result in an
            ``INVALID_ARGUMENT`` error. If unspecified or set to ``0``,
            a default value of ``20`` will be used. The server may
            return fewer results than requested.
        page_token (str):
            Optional. If present, retrieve the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of all other method parameters, must be
            identical to those in the previous call.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_string: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )


class SearchAgentsResponse(proto.Message):
    r"""Message for response to searching Agents

    Attributes:
        agents (MutableSequence[google.cloud.agentregistry_v1.types.Agent]):
            A list of Agents that match the ``search_string``.
        next_page_token (str):
            If there are more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    agents: MutableSequence[agent.Agent] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=agent.Agent,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetAgentRequest(proto.Message):
    r"""Message for getting a Agent

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListEndpointsRequest(proto.Message):
    r"""Message for requesting list of Endpoints

    Attributes:
        parent (str):
            Required. The project and location to list endpoints in.
            Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. A query string used to filter the list of
            endpoints returned. The filter expression must follow
            AIP-160 syntax.

            Filtering is supported on the ``name``, ``display_name``,
            ``description``, ``version``, and ``interfaces`` fields.

            Some examples:

            - ``name = "projects/p1/locations/l1/endpoints/e1"``
            - ``display_name = "my-endpoint"``
            - ``description = "my-endpoint-description"``
            - ``version = "v1"``
            - ``interfaces.transport = "HTTP_JSON"``
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


class ListEndpointsResponse(proto.Message):
    r"""Message for response to listing Endpoints

    Attributes:
        endpoints (MutableSequence[google.cloud.agentregistry_v1.types.Endpoint]):
            The list of Endpoint resources matching the parent and
            filter criteria in the request. Each Endpoint resource
            follows the format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``.
        next_page_token (str):
            A token identifying a page of results the server should
            return. Used in
            [page_token][google.cloud.agentregistry.v1main.ListEndpointsRequest.page_token].
    """

    @property
    def raw_page(self):
        return self

    endpoints: MutableSequence[endpoint.Endpoint] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=endpoint.Endpoint,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetEndpointRequest(proto.Message):
    r"""Message for getting a Endpoint

    Attributes:
        name (str):
            Required. The name of the endpoint to retrieve. Format:
            ``projects/{project}/locations/{location}/endpoints/{endpoint}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMcpServersRequest(proto.Message):
    r"""Message for requesting list of McpServers

    Attributes:
        parent (str):
            Required. Parent value for ListMcpServersRequest. Format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. Filtering results
        order_by (str):
            Optional. Hint for how to order the results
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


class ListMcpServersResponse(proto.Message):
    r"""Message for response to listing McpServers

    Attributes:
        mcp_servers (MutableSequence[google.cloud.agentregistry_v1.types.McpServer]):
            The list of McpServers.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    mcp_servers: MutableSequence[mcp_server.McpServer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mcp_server.McpServer,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class SearchMcpServersRequest(proto.Message):
    r"""Message for searching MCP Servers

    Attributes:
        parent (str):
            Required. Parent value for SearchMcpServersRequest. Format:
            ``projects/{project}/locations/{location}``.
        search_string (str):
            Optional. Search criteria used to select the MCP Servers to
            return. If no search criteria is specified then all
            accessible MCP Servers will be returned.

            Search expressions can be used to restrict results based
            upon searchable fields, where the operators can be used
            along with the suffix wildcard symbol ``*``. See
            `instructions <https://docs.cloud.google.com/agent-registry/search-agents-and-tools>`__
            for more details.

            Allowed operators: ``=``, ``:``, ``NOT``, ``AND``, ``OR``,
            and ``()``.

            Searchable fields:

            \| Field \| ``=`` \| ``:`` \| ``*`` \| Keyword Search \|
            \|--------------------\|-----\|-----\|-----\|----------------\|
            \| mcpServerId \| Yes \| Yes \| Yes \| Included \| \| name
            \| No \| Yes \| Yes \| Included \| \| displayName \| No \|
            Yes \| Yes \| Included \|

            Examples:

            - ``mcpServerId="urn:mcp:projects-123:projects:123:locations:us-central1:agentregistry:services:service-id"``
              to find the MCP Server with the specified MCP Server ID.
            - ``name:important`` to find MCP Servers whose name contains
              ``important`` as a word.
            - ``displayName:works*`` to find MCP Servers whose display
              name contains words that start with ``works``.
            - ``planner OR booking`` to find MCP Servers whose metadata
              contains the words ``planner`` or ``booking``.
            - ``mcpServerId:service-id AND (displayName:planner OR displayName:booking)``
              to find MCP Servers whose MCP Server ID contains
              ``service-id`` and whose display name contains ``planner``
              or ``booking``.
        page_size (int):
            Optional. The maximum number of search results to return per
            page. The page size is capped at ``100``, even if a larger
            value is specified. A negative value will result in an
            ``INVALID_ARGUMENT`` error. If unspecified or set to ``0``,
            a default value of ``20`` will be used. The server may
            return fewer results than requested.
        page_token (str):
            Optional. If present, retrieve the next batch of results
            from the preceding call to this method. ``page_token`` must
            be the value of ``next_page_token`` from the previous
            response. The values of all other method parameters, must be
            identical to those in the previous call.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    search_string: str = proto.Field(
        proto.STRING,
        number=3,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=6,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=7,
    )


class SearchMcpServersResponse(proto.Message):
    r"""Message for response to searching MCP Servers

    Attributes:
        mcp_servers (MutableSequence[google.cloud.agentregistry_v1.types.McpServer]):
            A list of McpServers that match the ``search_string``.
        next_page_token (str):
            If there are more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
    """

    @property
    def raw_page(self):
        return self

    mcp_servers: MutableSequence[mcp_server.McpServer] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=mcp_server.McpServer,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMcpServerRequest(proto.Message):
    r"""Message for getting a McpServer

    Attributes:
        name (str):
            Required. Name of the resource
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListServicesRequest(proto.Message):
    r"""Message for requesting list of Services

    Attributes:
        parent (str):
            Required. The project and location to list services in.
            Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may
            return fewer items than requested. If
            unspecified, server will pick an appropriate
            default.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. A query string used to filter the list of services
            returned. The filter expression must follow AIP-160 syntax.

            Filtering is supported on the ``name``, ``display_name``,
            ``description``, and ``labels`` fields.

            Some examples:

            - ``name = "projects/p1/locations/l1/services/s1"``
            - ``display_name = "my-service"``
            - ``description : "myservice description"``
            - ``labels.env = "prod"``
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


class ListServicesResponse(proto.Message):
    r"""Message for response to listing Services

    Attributes:
        services (MutableSequence[google.cloud.agentregistry_v1.types.Service]):
            The list of Service resources matching the parent and filter
            criteria in the request. Each Service resource follows the
            format:
            ``projects/{project}/locations/{location}/services/{service}``.
        next_page_token (str):
            A token identifying a page of results the server should
            return. Used in
            [page_token][google.cloud.agentregistry.v1main.ListServicesRequest.page_token].
    """

    @property
    def raw_page(self):
        return self

    services: MutableSequence[gca_service.Service] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_service.Service,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetServiceRequest(proto.Message):
    r"""Message for getting a Service

    Attributes:
        name (str):
            Required. The name of the Service. Format:
            ``projects/{project}/locations/{location}/services/{service}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateServiceRequest(proto.Message):
    r"""Message for creating a Service

    Attributes:
        parent (str):
            Required. The project and location to create the Service in.
            Expected format:
            ``projects/{project}/locations/{location}``.
        service_id (str):
            Required. The ID to use for the service, which will become
            the final component of the service's resource name.

            This value should be 4-63 characters, and valid characters
            are ``/[a-z][0-9]-/``.
        service (google.cloud.agentregistry_v1.types.Service):
            Required. The Service resource that is being created.
            Format:
            ``projects/{project}/locations/{location}/services/{service}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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
    service_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    service: gca_service.Service = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_service.Service,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class FetchAvailableBindingsRequest(proto.Message):
    r"""Message for fetching available Bindings.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        source_identifier (str):
            The identifier of the source Agent. Format:

            - ``urn:agent:{publisher}:{namespace}:{name}``

            This field is a member of `oneof`_ ``source``.
        target_identifier (str):
            Optional. The identifier of the target Agent, MCP Server, or
            Endpoint. Format:

            - ``urn:agent:{publisher}:{namespace}:{name}``
            - ``urn:mcp:{publisher}:{namespace}:{name}``
            - ``urn:endpoint:{publisher}:{namespace}:{name}``

            This field is a member of `oneof`_ ``target``.
        parent (str):
            Required. The parent, in the format
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may return fewer items
            than requested. Page size is 500 if unspecified and is
            capped at ``500`` even if a larger value is given.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
    """

    source_identifier: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="source",
    )
    target_identifier: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="target",
    )
    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=4,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=5,
    )


class FetchAvailableBindingsResponse(proto.Message):
    r"""Message for response to fetching available Bindings.

    Attributes:
        bindings (MutableSequence[google.cloud.agentregistry_v1.types.Binding]):
            The list of Bindings.
        next_page_token (str):
            A token identifying a page of results the
            server should return.
    """

    @property
    def raw_page(self):
        return self

    bindings: MutableSequence[gca_binding.Binding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_binding.Binding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateServiceRequest(proto.Message):
    r"""Message for updating a Service

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Service resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields present in the request will be overwritten.
        service (google.cloud.agentregistry_v1.types.Service):
            Required. The Service resource that is being updated.
            Format:
            ``projects/{project}/locations/{location}/services/{service}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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
    service: gca_service.Service = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gca_service.Service,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteServiceRequest(proto.Message):
    r"""Message for deleting a Service

    Attributes:
        name (str):
            Required. The name of the Service. Format:
            ``projects/{project}/locations/{location}/services/{service}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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
            cancellation of the operation. Operations that have been
            cancelled successfully have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of ``1``,
            corresponding to ``Code.CANCELLED``.
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


class ListBindingsRequest(proto.Message):
    r"""Message for requesting a list of Bindings.

    Attributes:
        parent (str):
            Required. The project and location to list bindings in.
            Expected format:
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. Requested page size. Server may return fewer items
            than requested. Page size is 500 if unspecified and is
            capped at ``500`` even if a larger value is given.
        page_token (str):
            Optional. A token identifying a page of
            results the server should return.
        filter (str):
            Optional. A query string used to filter the
            list of bindings returned. The filter expression
            must follow AIP-160 syntax.
        order_by (str):
            Optional. Hint for how to order the results
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


class ListBindingsResponse(proto.Message):
    r"""Message for response to listing Bindings

    Attributes:
        bindings (MutableSequence[google.cloud.agentregistry_v1.types.Binding]):
            The list of Binding resources matching the parent and filter
            criteria in the request. Each Binding resource follows the
            format:
            ``projects/{project}/locations/{location}/bindings/{binding}``.
        next_page_token (str):
            A token identifying a page of results the server should
            return. Used in
            [page_token][google.cloud.agentregistry.v1main.ListBindingsRequest.page_token].
    """

    @property
    def raw_page(self):
        return self

    bindings: MutableSequence[gca_binding.Binding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gca_binding.Binding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetBindingRequest(proto.Message):
    r"""Message for getting a Binding

    Attributes:
        name (str):
            Required. The name of the Binding. Format:
            ``projects/{project}/locations/{location}/bindings/{binding}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateBindingRequest(proto.Message):
    r"""Message for creating a Binding

    Attributes:
        parent (str):
            Required. The project and location to create the Binding in.
            Expected format:
            ``projects/{project}/locations/{location}``.
        binding_id (str):
            Required. The ID to use for the binding, which will become
            the final component of the binding's resource name.

            This value should be 4-63 characters, and must conform to
            RFC-1034. Specifically, it must match the regular expression
            ``^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$``.
        binding (google.cloud.agentregistry_v1.types.Binding):
            Required. The Binding resource that is being
            created.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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
    binding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    binding: gca_binding.Binding = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gca_binding.Binding,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateBindingRequest(proto.Message):
    r"""Message for updating a Binding

    Attributes:
        binding (google.cloud.agentregistry_v1.types.Binding):
            Required. The Binding resource that is being
            updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the Binding resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields present in the request will be overwritten.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes since the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    binding: gca_binding.Binding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gca_binding.Binding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteBindingRequest(proto.Message):
    r"""Message for deleting a Binding

    Attributes:
        name (str):
            Required. The name of the Binding. Format:
            ``projects/{project}/locations/{location}/bindings/{binding}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID so that if
            you must retry your request, the server will
            know to ignore the request if it has already
            been completed. The server will guarantee that
            for at least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
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
