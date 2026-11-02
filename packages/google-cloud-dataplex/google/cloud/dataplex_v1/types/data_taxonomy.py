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

from google.cloud.dataplex_v1.types import security

__protobuf__ = proto.module(
    package="google.cloud.dataplex.v1",
    manifest={
        "DataTaxonomy",
        "DataAttribute",
        "DataAttributeBinding",
        "CreateDataTaxonomyRequest",
        "UpdateDataTaxonomyRequest",
        "GetDataTaxonomyRequest",
        "ListDataTaxonomiesRequest",
        "ListDataTaxonomiesResponse",
        "DeleteDataTaxonomyRequest",
        "CreateDataAttributeRequest",
        "UpdateDataAttributeRequest",
        "GetDataAttributeRequest",
        "ListDataAttributesRequest",
        "ListDataAttributesResponse",
        "DeleteDataAttributeRequest",
        "CreateDataAttributeBindingRequest",
        "UpdateDataAttributeBindingRequest",
        "GetDataAttributeBindingRequest",
        "ListDataAttributeBindingsRequest",
        "ListDataAttributeBindingsResponse",
        "DeleteDataAttributeBindingRequest",
    },
)


class DataTaxonomy(proto.Message):
    r"""DataTaxonomy represents a set of hierarchical DataAttributes
    resources, grouped with a common theme Eg:
    'SensitiveDataTaxonomy' can have attributes to manage PII data.
    It is defined at project level.

    Attributes:
        name (str):
            Output only. The relative resource name of the DataTaxonomy,
            of the form:
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}.
        uid (str):
            Output only. System generated globally unique
            ID for the dataTaxonomy. This ID will be
            different if the DataTaxonomy is deleted and
            re-created with the same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the DataTaxonomy
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the DataTaxonomy
            was last updated.
        description (str):
            Optional. Description of the DataTaxonomy.
        display_name (str):
            Optional. User friendly display name.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            DataTaxonomy.
        attribute_count (int):
            Output only. The number of attributes in the
            DataTaxonomy.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        class_count (int):
            Output only. The number of classes in the
            DataTaxonomy.
    """

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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )
    attribute_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    class_count: int = proto.Field(
        proto.INT32,
        number=11,
    )


class DataAttribute(proto.Message):
    r"""Denotes one dataAttribute in a dataTaxonomy, for example, PII.
    DataAttribute resources can be defined in a hierarchy. A single
    dataAttribute resource can contain specs of multiple types

    ::

       PII
         - ResourceAccessSpec :
                       - readers :foo@bar.com
         - DataAccessSpec :
                       - readers :bar@foo.com

    Attributes:
        name (str):
            Output only. The relative resource name of the
            dataAttribute, of the form:
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}.
        uid (str):
            Output only. System generated globally unique
            ID for the DataAttribute. This ID will be
            different if the DataAttribute is deleted and
            re-created with the same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the DataAttribute
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the DataAttribute
            was last updated.
        description (str):
            Optional. Description of the DataAttribute.
        display_name (str):
            Optional. User friendly display name.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            DataAttribute.
        parent_id (str):
            Optional. The ID of the parent DataAttribute resource,
            should belong to the same data taxonomy. Circular dependency
            in parent chain is not valid. Maximum depth of the hierarchy
            allowed is 4. [a -> b -> c -> d -> e, depth = 4]
        attribute_count (int):
            Output only. The number of child attributes
            present for this attribute.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding.
        resource_access_spec (google.cloud.dataplex_v1.types.ResourceAccessSpec):
            Optional. Specified when applied to a
            resource (eg: Cloud Storage bucket, BigQuery
            dataset, BigQuery table).
        data_access_spec (google.cloud.dataplex_v1.types.DataAccessSpec):
            Optional. Specified when applied to data
            stored on the resource (eg: rows, columns in
            BigQuery Tables).
    """

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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    parent_id: str = proto.Field(
        proto.STRING,
        number=8,
    )
    attribute_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=10,
    )
    resource_access_spec: security.ResourceAccessSpec = proto.Field(
        proto.MESSAGE,
        number=100,
        message=security.ResourceAccessSpec,
    )
    data_access_spec: security.DataAccessSpec = proto.Field(
        proto.MESSAGE,
        number=101,
        message=security.DataAccessSpec,
    )


class DataAttributeBinding(proto.Message):
    r"""DataAttributeBinding represents binding of attributes to
    resources. Eg: Bind 'CustomerInfo' entity with 'PII' attribute.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            Output only. The relative resource name of the Data
            Attribute Binding, of the form:
            projects/{project_number}/locations/{location}/dataAttributeBindings/{data_attribute_binding_id}
        uid (str):
            Output only. System generated globally unique
            ID for the DataAttributeBinding. This ID will be
            different if the DataAttributeBinding is deleted
            and re-created with the same name.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the
            DataAttributeBinding was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the
            DataAttributeBinding was last updated.
        description (str):
            Optional. Description of the
            DataAttributeBinding.
        display_name (str):
            Optional. User friendly display name.
        labels (MutableMapping[str, str]):
            Optional. User-defined labels for the
            DataAttributeBinding.
        etag (str):
            This checksum is computed by the server based
            on the value of other fields, and may be sent on
            update and delete requests to ensure the client
            has an up-to-date value before proceeding. Etags
            must be used when calling the
            DeleteDataAttributeBinding and the
            UpdateDataAttributeBinding method.
        resource (str):
            Optional. Immutable. The resource name of the resource that
            is associated to attributes. Presently, only entity resource
            is supported in the form:
            projects/{project}/locations/{location}/lakes/{lake}/zones/{zone}/entities/{entity_id}
            Must belong in the same project and region as the attribute
            binding, and there can only exist one active binding for a
            resource.

            This field is a member of `oneof`_ ``resource_reference``.
        attributes (MutableSequence[str]):
            Optional. List of attributes to be associated with the
            resource, provided in the form:
            projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        paths (MutableSequence[google.cloud.dataplex_v1.types.DataAttributeBinding.Path]):
            Optional. The list of paths for items within
            the associated resource (eg. columns and
            partitions within a table) along with attribute
            bindings.
    """

    class Path(proto.Message):
        r"""Represents a subresource of the given resource, and
        associated bindings with it. Currently supported subresources
        are column and partition schema fields within a table.

        Attributes:
            name (str):
                Required. The name identifier of the path.
                Nested columns should be of the form:
                'address.city'.
            attributes (MutableSequence[str]):
                Optional. List of attributes to be associated with the path
                of the resource, provided in the form:
                projects/{project}/locations/{location}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        attributes: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=2,
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
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=8,
    )
    resource: str = proto.Field(
        proto.STRING,
        number=100,
        oneof="resource_reference",
    )
    attributes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=110,
    )
    paths: MutableSequence[Path] = proto.RepeatedField(
        proto.MESSAGE,
        number=120,
        message=Path,
    )


class CreateDataTaxonomyRequest(proto.Message):
    r"""Create DataTaxonomy request.

    Attributes:
        parent (str):

        data_taxonomy_id (str):
            Required. DataTaxonomy identifier.

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the Project.
        data_taxonomy (google.cloud.dataplex_v1.types.DataTaxonomy):
            Required. DataTaxonomy resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_taxonomy_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_taxonomy: "DataTaxonomy" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataTaxonomy",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateDataTaxonomyRequest(proto.Message):
    r"""Update DataTaxonomy request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        data_taxonomy (google.cloud.dataplex_v1.types.DataTaxonomy):
            Required. Only fields specified in ``update_mask`` are
            updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    data_taxonomy: "DataTaxonomy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataTaxonomy",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetDataTaxonomyRequest(proto.Message):
    r"""Get DataTaxonomy request.

    Attributes:
        name (str):

    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataTaxonomiesRequest(proto.Message):
    r"""List DataTaxonomies request.

    Attributes:
        parent (str):
            Required. The resource name of the DataTaxonomy location, of
            the form: projects/{project_number}/locations/{location_id}
            where ``location_id`` refers to a Google Cloud region.
        page_size (int):
            Optional. Maximum number of DataTaxonomies to
            return. The service may return fewer than this
            value. If unspecified, at most 10 DataTaxonomies
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListDataTaxonomies`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListDataTaxonomies`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter request.
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


class ListDataTaxonomiesResponse(proto.Message):
    r"""List DataTaxonomies response.

    Attributes:
        data_taxonomies (MutableSequence[google.cloud.dataplex_v1.types.DataTaxonomy]):
            DataTaxonomies under the given parent
            location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    data_taxonomies: MutableSequence["DataTaxonomy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTaxonomy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteDataTaxonomyRequest(proto.Message):
    r"""Delete DataTaxonomy request.

    Attributes:
        name (str):
            Required. The resource name of the DataTaxonomy:
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}
        etag (str):
            Optional. If the client provided etag value
            does not match the current etag value,the
            DeleteDataTaxonomy method returns an ABORTED
            error.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDataAttributeRequest(proto.Message):
    r"""Create DataAttribute request.

    Attributes:
        parent (str):
            Required. The resource name of the parent data taxonomy
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}
        data_attribute_id (str):
            Required. DataAttribute identifier.

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the DataTaxonomy.
        data_attribute (google.cloud.dataplex_v1.types.DataAttribute):
            Required. DataAttribute resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_attribute_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_attribute: "DataAttribute" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataAttribute",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateDataAttributeRequest(proto.Message):
    r"""Update DataAttribute request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        data_attribute (google.cloud.dataplex_v1.types.DataAttribute):
            Required. Only fields specified in ``update_mask`` are
            updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    data_attribute: "DataAttribute" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataAttribute",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetDataAttributeRequest(proto.Message):
    r"""Get DataAttribute request.

    Attributes:
        name (str):
            Required. The resource name of the dataAttribute:
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataAttributesRequest(proto.Message):
    r"""List DataAttributes request.

    Attributes:
        parent (str):
            Required. The resource name of the DataTaxonomy:
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{data_taxonomy_id}
        page_size (int):
            Optional. Maximum number of DataAttributes to
            return. The service may return fewer than this
            value. If unspecified, at most 10 dataAttributes
            will be returned. The maximum value is 1000;
            values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListDataAttributes`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListDataAttributes`` must match the call that
            provided the page token.
        filter (str):
            Optional. Filter request.
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


class ListDataAttributesResponse(proto.Message):
    r"""List DataAttributes response.

    Attributes:
        data_attributes (MutableSequence[google.cloud.dataplex_v1.types.DataAttribute]):
            DataAttributes under the given parent
            DataTaxonomy.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    data_attributes: MutableSequence["DataAttribute"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataAttribute",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteDataAttributeRequest(proto.Message):
    r"""Delete DataAttribute request.

    Attributes:
        name (str):
            Required. The resource name of the DataAttribute:
            projects/{project_number}/locations/{location_id}/dataTaxonomies/{dataTaxonomy}/attributes/{data_attribute_id}
        etag (str):
            Optional. If the client provided etag value
            does not match the current etag value, the
            DeleteDataAttribute method returns an ABORTED
            error response.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDataAttributeBindingRequest(proto.Message):
    r"""Create DataAttributeBinding request.

    Attributes:
        parent (str):
            Required. The resource name of the parent data taxonomy
            projects/{project_number}/locations/{location_id}
        data_attribute_binding_id (str):
            Required. DataAttributeBinding identifier.

            - Must contain only lowercase letters, numbers and hyphens.
            - Must start with a letter.
            - Must be between 1-63 characters.
            - Must end with a number or a letter.
            - Must be unique within the Location.
        data_attribute_binding (google.cloud.dataplex_v1.types.DataAttributeBinding):
            Required. DataAttributeBinding resource.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_attribute_binding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_attribute_binding: "DataAttributeBinding" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="DataAttributeBinding",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=4,
    )


class UpdateDataAttributeBindingRequest(proto.Message):
    r"""Update DataAttributeBinding request.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        data_attribute_binding (google.cloud.dataplex_v1.types.DataAttributeBinding):
            Required. Only fields specified in ``update_mask`` are
            updated.
        validate_only (bool):
            Optional. Only validate the request, but do
            not perform mutations. The default is false.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    data_attribute_binding: "DataAttributeBinding" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataAttributeBinding",
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class GetDataAttributeBindingRequest(proto.Message):
    r"""Get DataAttributeBinding request.

    Attributes:
        name (str):
            Required. The resource name of the DataAttributeBinding:
            projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataAttributeBindingsRequest(proto.Message):
    r"""List DataAttributeBindings request.

    Attributes:
        parent (str):
            Required. The resource name of the Location:
            projects/{project_number}/locations/{location_id}
        page_size (int):
            Optional. Maximum number of
            DataAttributeBindings to return. The service may
            return fewer than this value. If unspecified, at
            most 10 DataAttributeBindings will be returned.
            The maximum value is 1000; values above 1000
            will be coerced to 1000.
        page_token (str):
            Optional. Page token received from a previous
            ``ListDataAttributeBindings`` call. Provide this to retrieve
            the subsequent page. When paginating, all other parameters
            provided to ``ListDataAttributeBindings`` must match the
            call that provided the page token.
        filter (str):
            Optional. Filter request.
            Filter using resource:
            filter=resource:"resource-name" Filter using
            attribute: filter=attributes:"attribute-name"
            Filter using attribute in paths list:

            filter=paths.attributes:"attribute-name".
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


class ListDataAttributeBindingsResponse(proto.Message):
    r"""List DataAttributeBindings response.

    Attributes:
        data_attribute_bindings (MutableSequence[google.cloud.dataplex_v1.types.DataAttributeBinding]):
            DataAttributeBindings under the given parent
            Location.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
        unreachable_locations (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    data_attribute_bindings: MutableSequence["DataAttributeBinding"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="DataAttributeBinding",
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable_locations: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class DeleteDataAttributeBindingRequest(proto.Message):
    r"""Delete DataAttributeBinding request.

    Attributes:
        name (str):
            Required. The resource name of the DataAttributeBinding:
            projects/{project_number}/locations/{location_id}/dataAttributeBindings/{data_attribute_binding_id}
        etag (str):
            Required. If the client provided etag value
            does not match the current etag value, the
            DeleteDataAttributeBindingRequest method returns
            an ABORTED error response. Etags must be used
            when calling the DeleteDataAttributeBinding.
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
