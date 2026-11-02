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

__protobuf__ = proto.module(
    package="google.cloud.metastore.v1alpha",
    manifest={
        "Federation",
        "BackendMetastore",
        "ListFederationsRequest",
        "ListFederationsResponse",
        "GetFederationRequest",
        "CreateFederationRequest",
        "UpdateFederationRequest",
        "DeleteFederationRequest",
    },
)


class Federation(proto.Message):
    r"""Represents a federation of multiple backend metastores.

    Attributes:
        name (str):
            Immutable. The relative resource name of the federation, of
            the form:
            projects/{project_number}/locations/{location_id}/federations/{federation_id}\`.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metastore
            federation was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the metastore
            federation was last updated.
        labels (MutableMapping[str, str]):
            User-defined labels for the metastore
            federation.
        version (str):
            Immutable. The Apache Hive metastore version
            of the federation. All backend metastore
            versions must be compatible with the federation
            version.
        backend_metastores (MutableMapping[int, google.cloud.metastore_v1alpha.types.BackendMetastore]):
            A map from ``BackendMetastore`` rank to
            ``BackendMetastore``\ s from which the federation service
            serves metadata at query time. The map key represents the
            order in which ``BackendMetastore``\ s should be evaluated
            to resolve database names at query time and should be
            greater than or equal to zero. A ``BackendMetastore`` with a
            lower number will be evaluated before a ``BackendMetastore``
            with a higher number.
        endpoint_uri (str):
            Output only. The federation endpoint.
        state (google.cloud.metastore_v1alpha.types.Federation.State):
            Output only. The current state of the
            federation.
        state_message (str):
            Output only. Additional information about the
            current state of the metastore federation, if
            available.
        uid (str):
            Output only. The globally unique resource
            identifier of the metastore federation.
    """

    class State(proto.Enum):
        r"""The current state of the federation.

        Values:
            STATE_UNSPECIFIED (0):
                The state of the metastore federation is
                unknown.
            CREATING (1):
                The metastore federation is in the process of
                being created.
            ACTIVE (2):
                The metastore federation is running and ready
                to serve queries.
            UPDATING (3):
                The metastore federation is being updated. It
                remains usable but cannot accept additional
                update requests or be deleted at this time.
            DELETING (4):
                The metastore federation is undergoing
                deletion. It cannot be used.
            ERROR (5):
                The metastore federation has encountered an
                error and cannot be used. The metastore
                federation should be deleted.
        """

        STATE_UNSPECIFIED = 0
        CREATING = 1
        ACTIVE = 2
        UPDATING = 3
        DELETING = 4
        ERROR = 5

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
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=4,
    )
    version: str = proto.Field(
        proto.STRING,
        number=5,
    )
    backend_metastores: MutableMapping[int, "BackendMetastore"] = proto.MapField(
        proto.INT32,
        proto.MESSAGE,
        number=6,
        message="BackendMetastore",
    )
    endpoint_uri: str = proto.Field(
        proto.STRING,
        number=7,
    )
    state: State = proto.Field(
        proto.ENUM,
        number=8,
        enum=State,
    )
    state_message: str = proto.Field(
        proto.STRING,
        number=9,
    )
    uid: str = proto.Field(
        proto.STRING,
        number=10,
    )


class BackendMetastore(proto.Message):
    r"""Represents a backend metastore for the federation.

    Attributes:
        name (str):
            The relative resource name of the metastore that is being
            federated. The formats of the relative resource names for
            the currently supported metastores are listed below:

            - BigQuery

              - ``projects/{project_id}``

            - Dataproc Metastore

              - ``projects/{project_id}/locations/{location}/services/{service_id}``
        metastore_type (google.cloud.metastore_v1alpha.types.BackendMetastore.MetastoreType):
            The type of the backend metastore.
    """

    class MetastoreType(proto.Enum):
        r"""The type of the backend metastore.

        Values:
            METASTORE_TYPE_UNSPECIFIED (0):
                The metastore type is not set.
            DATAPLEX (1):
                The backend metastore is Dataplex.
            BIGQUERY (2):
                The backend metastore is BigQuery.
            DATAPROC_METASTORE (3):
                The backend metastore is Dataproc Metastore.
        """

        METASTORE_TYPE_UNSPECIFIED = 0
        DATAPLEX = 1
        BIGQUERY = 2
        DATAPROC_METASTORE = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    metastore_type: MetastoreType = proto.Field(
        proto.ENUM,
        number=2,
        enum=MetastoreType,
    )


class ListFederationsRequest(proto.Message):
    r"""Request message for ListFederations.

    Attributes:
        parent (str):
            Required. The relative resource name of the location of
            metastore federations to list, in the following form:
            ``projects/{project_number}/locations/{location_id}``.
        page_size (int):
            Optional. The maximum number of federations
            to return. The response may contain less than
            the maximum number. If unspecified, no more than
            500 services are returned. The maximum value is
            1000; values above 1000 are changed to 1000.
        page_token (str):
            Optional. A page token, received from a
            previous ListFederationServices call. Provide
            this token to retrieve the subsequent page.

            To retrieve the first page, supply an empty page
            token.

            When paginating, other parameters provided to
            ListFederationServices must match the call that
            provided the page token.
        filter (str):
            Optional. The filter to apply to list
            results.
        order_by (str):
            Optional. Specify the ordering of results as described in
            `Sorting
            Order <https://cloud.google.com/apis/design/design_patterns#sorting_order>`__.
            If not specified, the results will be sorted in the default
            order.
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


class ListFederationsResponse(proto.Message):
    r"""Response message for ListFederations

    Attributes:
        federations (MutableSequence[google.cloud.metastore_v1alpha.types.Federation]):
            The services in the specified location.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    federations: MutableSequence["Federation"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Federation",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetFederationRequest(proto.Message):
    r"""Request message for GetFederation.

    Attributes:
        name (str):
            Required. The relative resource name of the metastore
            federation to retrieve, in the following form:

            ``projects/{project_number}/locations/{location_id}/federations/{federation_id}``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFederationRequest(proto.Message):
    r"""Request message for CreateFederation.

    Attributes:
        parent (str):
            Required. The relative resource name of the location in
            which to create a federation service, in the following form:

            ``projects/{project_number}/locations/{location_id}``.
        federation_id (str):
            Required. The ID of the metastore federation,
            which is used as the final component of the
            metastore federation's name.

            This value must be between 2 and 63 characters
            long inclusive, begin with a letter, end with a
            letter or number, and consist of alpha-numeric
            ASCII characters or hyphens.
        federation (google.cloud.metastore_v1alpha.types.Federation):
            Required. The Metastore Federation to create. The ``name``
            field is ignored. The ID of the created metastore federation
            must be provided in the request's ``federation_id`` field.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    federation_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    federation: "Federation" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Federation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class UpdateFederationRequest(proto.Message):
    r"""Request message for UpdateFederation.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. A field mask used to specify the fields to be
            overwritten in the metastore federation resource by the
            update. Fields specified in the ``update_mask`` are relative
            to the resource (not to the full request). A field is
            overwritten if it is in the mask.
        federation (google.cloud.metastore_v1alpha.types.Federation):
            Required. The metastore federation to update. The server
            only merges fields in the service if they are specified in
            ``update_mask``.

            The metastore federation's ``name`` field is used to
            identify the metastore service to be updated.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    federation: "Federation" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Federation",
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class DeleteFederationRequest(proto.Message):
    r"""Request message for DeleteFederation.

    Attributes:
        name (str):
            Required. The relative resource name of the metastore
            federation to delete, in the following form:

            ``projects/{project_number}/locations/{location_id}/federations/{federation_id}``.
        request_id (str):
            Optional. A request ID. Specify a unique request ID to allow
            the server to ignore the request if it has completed. The
            server will ignore subsequent requests that provide a
            duplicate request ID for at least 60 minutes after the first
            request.

            For example, if an initial request times out, followed by
            another request with the same request ID, the server ignores
            the second request to prevent the creation of duplicate
            commitments.

            The request ID must be a valid
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier#Format>`__
            A zero UUID (00000000-0000-0000-0000-000000000000) is not
            supported.
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
