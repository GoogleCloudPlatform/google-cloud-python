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
import proto  # type: ignore

from google.cloud.managedkafka_v1.types import resources

__protobuf__ = proto.module(
    package="google.cloud.managedkafka.v1",
    manifest={
        "GetConnectClusterRequest",
        "CreateConnectClusterRequest",
        "UpdateConnectClusterRequest",
        "DeleteConnectClusterRequest",
        "ListConnectClustersRequest",
        "ListConnectClustersResponse",
        "GetConnectorRequest",
        "CreateConnectorRequest",
        "UpdateConnectorRequest",
        "DeleteConnectorRequest",
        "ListConnectorsRequest",
        "ListConnectorsResponse",
        "PauseConnectorRequest",
        "PauseConnectorResponse",
        "ResumeConnectorRequest",
        "ResumeConnectorResponse",
        "RestartConnectorRequest",
        "RestartConnectorResponse",
        "StopConnectorRequest",
        "StopConnectorResponse",
    },
)


class GetConnectClusterRequest(proto.Message):
    r"""Request for GetConnectCluster.

    Attributes:
        name (str):
            Required. The name of the Kafka Connect cluster whose
            configuration to return. Structured like
            ``projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConnectClusterRequest(proto.Message):
    r"""Request for CreateConnectCluster.

    Attributes:
        parent (str):
            Required. The parent project/location in which to create the
            Kafka Connect cluster. Structured like
            ``projects/{project}/locations/{location}/``.
        connect_cluster_id (str):
            Required. The ID to use for the Connect cluster, which will
            become the final component of the cluster's name. The ID
            must be 1-63 characters long, and match the regular
            expression ``[a-z]([-a-z0-9]*[a-z0-9])?`` to comply with RFC
            1035.

            This value is structured like: ``my-cluster-id``.
        connect_cluster (google.cloud.managedkafka_v1.types.ConnectCluster):
            Required. Configuration of the Kafka Connect cluster to
            create. Its ``name`` field is ignored.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID to avoid
            duplication of requests. If a request times out
            or fails, retrying with the same ID allows the
            server to recognize the previous attempt. For at
            least 60 minutes, the server ignores duplicate
            requests bearing the same ID.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID within 60 minutes of the last request, the
            server checks if an original operation with the
            same request ID was received. If so, the server
            ignores the second request.

            The request ID must be a valid UUID. A zero UUID
            is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connect_cluster_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connect_cluster: resources.ConnectCluster = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.ConnectCluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateConnectClusterRequest(proto.Message):
    r"""Request for UpdateConnectCluster.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the cluster resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The mask is required and a value of \*
            will update all fields.
        connect_cluster (google.cloud.managedkafka_v1.types.ConnectCluster):
            Required. The Kafka Connect cluster to update. Its ``name``
            field must be populated.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID to avoid
            duplication of requests. If a request times out
            or fails, retrying with the same ID allows the
            server to recognize the previous attempt. For at
            least 60 minutes, the server ignores duplicate
            requests bearing the same ID.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID within 60 minutes of the last request, the
            server checks if an original operation with the
            same request ID was received. If so, the server
            ignores the second request.

            The request ID must be a valid UUID. A zero UUID
            is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    connect_cluster: resources.ConnectCluster = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.ConnectCluster,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteConnectClusterRequest(proto.Message):
    r"""Request for DeleteConnectCluster.

    Attributes:
        name (str):
            Required. The name of the Kafka Connect cluster to delete.
            Structured like
            ``projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}``.
        request_id (str):
            Optional. An optional request ID to identify
            requests. Specify a unique request ID to avoid
            duplication of requests. If a request times out
            or fails, retrying with the same ID allows the
            server to recognize the previous attempt. For at
            least 60 minutes, the server ignores duplicate
            requests bearing the same ID.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID within 60 minutes of the last request, the
            server checks if an original operation with the
            same request ID was received. If so, the server
            ignores the second request.

            The request ID must be a valid UUID. A zero UUID
            is not supported
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


class ListConnectClustersRequest(proto.Message):
    r"""Request for ListConnectClusters.

    Attributes:
        parent (str):
            Required. The parent project/location whose Connect clusters
            are to be listed. Structured like
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Optional. The maximum number of Connect
            clusters to return. The service may return fewer
            than this value. If unspecified, server will
            pick an appropriate default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListConnectClusters`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListConnectClusters`` must match the call that provided
            the page token.
        filter (str):
            Optional. Filter expression for the result.
        order_by (str):
            Optional. Order by fields for the result.
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


class ListConnectClustersResponse(proto.Message):
    r"""Response for ListConnectClusters.

    Attributes:
        connect_clusters (MutableSequence[google.cloud.managedkafka_v1.types.ConnectCluster]):
            The list of Connect clusters in the requested
            parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page of results. If this field is omitted, there are no
            more results.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    connect_clusters: MutableSequence[resources.ConnectCluster] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.ConnectCluster,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetConnectorRequest(proto.Message):
    r"""Request for GetConnector.

    Attributes:
        name (str):
            Required. The name of the connector whose
            configuration to return. Structured like:

            projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateConnectorRequest(proto.Message):
    r"""Request for CreateConnector.

    Attributes:
        parent (str):
            Required. The parent Connect cluster in which to create the
            connector. Structured like
            ``projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}``.
        connector_id (str):
            Required. The ID to use for the connector, which will become
            the final component of the connector's name. The ID must be
            1-63 characters long, and match the regular expression
            ``[a-z]([-a-z0-9]*[a-z0-9])?`` to comply with RFC 1035.

            This value is structured like: ``my-connector-id``.
        connector (google.cloud.managedkafka_v1.types.Connector):
            Required. The connector to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    connector_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    connector: resources.Connector = proto.Field(
        proto.MESSAGE,
        number=3,
        message=resources.Connector,
    )


class UpdateConnectorRequest(proto.Message):
    r"""Request for UpdateConnector.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Field mask is used to specify the fields to be
            overwritten in the cluster resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. The mask is required and a value of \*
            will update all fields.
        connector (google.cloud.managedkafka_v1.types.Connector):
            Required. The connector to update. Its ``name`` field must
            be populated.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    connector: resources.Connector = proto.Field(
        proto.MESSAGE,
        number=2,
        message=resources.Connector,
    )


class DeleteConnectorRequest(proto.Message):
    r"""Request for DeleteConnector.

    Attributes:
        name (str):
            Required. The name of the connector to
            delete. Structured like:

            projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListConnectorsRequest(proto.Message):
    r"""Request for ListConnectors.

    Attributes:
        parent (str):
            Required. The parent Connect cluster whose connectors are to
            be listed. Structured like
            ``projects/{project}/locations/{location}/connectClusters/{connect_cluster_id}``.
        page_size (int):
            Optional. The maximum number of connectors to
            return. The service may return fewer than this
            value. If unspecified, server will pick an
            appropriate default.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListConnectors`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListConnectors`` must match the call that provided the
            page token.
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


class ListConnectorsResponse(proto.Message):
    r"""Response for ListConnectors.

    Attributes:
        connectors (MutableSequence[google.cloud.managedkafka_v1.types.Connector]):
            The list of connectors in the requested
            parent.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page of results. If this field is omitted, there are no
            more results.
    """

    @property
    def raw_page(self):
        return self

    connectors: MutableSequence[resources.Connector] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=resources.Connector,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class PauseConnectorRequest(proto.Message):
    r"""Request for PauseConnector.

    Attributes:
        name (str):
            Required. The name of the connector to pause.
            Structured like:

            projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PauseConnectorResponse(proto.Message):
    r"""Response for PauseConnector."""


class ResumeConnectorRequest(proto.Message):
    r"""Request for ResumeConnector.

    Attributes:
        name (str):
            Required. The name of the connector to pause.
            Structured like:

            projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeConnectorResponse(proto.Message):
    r"""Response for ResumeConnector."""


class RestartConnectorRequest(proto.Message):
    r"""Request for RestartConnector.

    Attributes:
        name (str):
            Required. The name of the connector to
            restart. Structured like:

            projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class RestartConnectorResponse(proto.Message):
    r"""Response for RestartConnector."""


class StopConnectorRequest(proto.Message):
    r"""Request for StopConnector.

    Attributes:
        name (str):
            Required. The name of the connector to stop.
            Structured like:

            projects/{project}/locations/{location}/connectClusters/{connectCluster}/connectors/{connector}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StopConnectorResponse(proto.Message):
    r"""Response for StopConnector."""


__all__ = tuple(sorted(__protobuf__.manifest))
