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
    package="google.cloud.chronicle.v1",
    manifest={
        "CreateDataAccessLabelRequest",
        "GetDataAccessLabelRequest",
        "ListDataAccessLabelsRequest",
        "ListDataAccessLabelsResponse",
        "UpdateDataAccessLabelRequest",
        "DeleteDataAccessLabelRequest",
        "CreateDataAccessScopeRequest",
        "GetDataAccessScopeRequest",
        "ListDataAccessScopesRequest",
        "ListDataAccessScopesResponse",
        "UpdateDataAccessScopeRequest",
        "DeleteDataAccessScopeRequest",
        "DataAccessLabel",
        "DataAccessScope",
        "DataAccessLabelReference",
        "IngestionLabel",
    },
)


class CreateDataAccessLabelRequest(proto.Message):
    r"""Request message for CreateDataAccessLabel.

    Attributes:
        parent (str):
            Required. The parent resource where this Data Access Label
            will be created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        data_access_label (google.cloud.chronicle_v1.types.DataAccessLabel):
            Required. Data access label to create.
        data_access_label_id (str):
            Required. The ID to use for the data access
            label, which will become the label's display
            name and the final component of the label's
            resource name. The maximum number of characters
            should be 63. Regex pattern is as per AIP:

            https://google.aip.dev/122#resource-id-segments
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_access_label: "DataAccessLabel" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataAccessLabel",
    )
    data_access_label_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetDataAccessLabelRequest(proto.Message):
    r"""Request message to retrieve a data access label.

    Attributes:
        name (str):
            Required. The ID of the data access label to retrieve.
            Format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessLabels/{data_access_label}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataAccessLabelsRequest(proto.Message):
    r"""Request message for ListDataAccessLabels.

    Attributes:
        parent (str):
            Required. The parent resource where this data access label
            will be created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        page_size (int):
            The maximum number of data access labels to
            return. The service may return fewer than this
            value. If unspecified, at most 100 data access
            labels will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListDataAccessLabelsRequest`` call. Provide this to
            retrieve the subsequent page.
        filter (str):
            Optional. A filter which should follow the guidelines of
            AIP-160. Supports filtering on all fieds of DataAccessLabel
            and all operations as mentioned in
            https://google.aip.dev/160. example filter: "create_time
            greater than "2023-04-21T11:30:00-04:00" OR
            display_name:"-21-1"".
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


class ListDataAccessLabelsResponse(proto.Message):
    r"""Response message for ListDataAccessLabels.

    Attributes:
        data_access_labels (MutableSequence[google.cloud.chronicle_v1.types.DataAccessLabel]):
            List of data access labels.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_access_labels: MutableSequence["DataAccessLabel"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataAccessLabel",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateDataAccessLabelRequest(proto.Message):
    r"""Request message for UpdateDataAccessLabel method.

    Attributes:
        data_access_label (google.cloud.chronicle_v1.types.DataAccessLabel):
            Required. The data access label to update.

            The label's ``name`` field is used to identify the label to
            update. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessLabels/{data_access_label}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. If not included, all fields
            with a non-empty value will be overwritten. Currently, only
            the description and definition fields are supported for
            update; an update call that attempts to update any other
            fields will return INVALID_ARGUMENT.
    """

    data_access_label: "DataAccessLabel" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataAccessLabel",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDataAccessLabelRequest(proto.Message):
    r"""Request message to delete a data access label.

    Attributes:
        name (str):
            Required. The ID of the data access label to delete. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessLabels/{data_access_label}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateDataAccessScopeRequest(proto.Message):
    r"""Request message for CreateDataAccessScope.

    Attributes:
        parent (str):
            Required. The parent resource where this Data Access Scope
            will be created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        data_access_scope (google.cloud.chronicle_v1.types.DataAccessScope):
            Required. Data access scope to create.
        data_access_scope_id (str):
            Required. The user provided scope id which
            will become the last part of the name of the
            scope resource. Needs to be compliant with
            https://google.aip.dev/122
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_access_scope: "DataAccessScope" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataAccessScope",
    )
    data_access_scope_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetDataAccessScopeRequest(proto.Message):
    r"""Request message to retrieve a data access scope.

    Attributes:
        name (str):
            Required. The ID of the data access scope to retrieve.
            Format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{data_access_scope}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDataAccessScopesRequest(proto.Message):
    r"""Request message for ListDataAccessScopes.

    Attributes:
        parent (str):
            Required. The parent resource where this data access scope
            will be created. Format:
            ``projects/{project}/locations/{location}/instances/{instance}``
        page_size (int):
            The maximum number of data access scopes to
            return. The service may return fewer than this
            value. If unspecified, at most 100 data access
            scopes will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            A page token, received from a previous
            ``ListDataAccessScopesRequest`` call. Provide this to
            retrieve the subsequent page.
        filter (str):
            Optional. A filter which should follow the guidelines of
            AIP-160. Supports filtering on all fieds of DataAccessScope
            and all operations as mentioned in
            https://google.aip.dev/160. example filter: "create_time
            greater than "2023-04-21T11:30:00-04:00" OR
            display_name:"-21-1"".
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


class ListDataAccessScopesResponse(proto.Message):
    r"""Response message for ListDataAccessScopes.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_access_scopes (MutableSequence[google.cloud.chronicle_v1.types.DataAccessScope]):
            List of data access scopes.
        global_data_access_scope_granted (bool):
            Whether or not global scope is granted to the
            user.

            This field is a member of `oneof`_ ``_global_data_access_scope_granted``.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_access_scopes: MutableSequence["DataAccessScope"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataAccessScope",
    )
    global_data_access_scope_granted: bool = proto.Field(
        proto.BOOL,
        number=3,
        optional=True,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateDataAccessScopeRequest(proto.Message):
    r"""Request message for UpdateDataAccessScope method.

    Attributes:
        data_access_scope (google.cloud.chronicle_v1.types.DataAccessScope):
            Required. The data access scope to update.

            The scope's ``name`` field is used to identify the scope to
            update. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{data_access_scope}``
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to update. If not included, all fields
            with a non-empty value will be overwritten. Currently, only
            the description, the allowed and denied labels list fields
            are supported for update; an update call that attempts to
            update any other fields will return INVALID_ARGUMENT.
    """

    data_access_scope: "DataAccessScope" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataAccessScope",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteDataAccessScopeRequest(proto.Message):
    r"""Request message to delete a data access scope.

    Attributes:
        name (str):
            Required. The ID of the data access scope to delete. Format:
            ``projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{data_access_scope}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DataAccessLabel(proto.Message):
    r"""A DataAccessLabel is a label on events to define user access
    to data.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        udm_query (str):
            A UDM query over event data.

            This field is a member of `oneof`_ ``definition``.
        name (str):
            The unique resource name of the data access
            label.
        display_name (str):
            Output only. The short name displayed for the
            label as it appears on event data.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data
            access label was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data
            access label was last updated.
        author (str):
            Output only. The user who created the data
            access label.
        last_editor (str):
            Output only. The user who last updated the
            data access label.
        description (str):
            Optional. A description of the data access
            label for a human reader.
    """

    udm_query: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="definition",
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=4,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    author: str = proto.Field(
        proto.STRING,
        number=6,
    )
    last_editor: str = proto.Field(
        proto.STRING,
        number=7,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )


class DataAccessScope(proto.Message):
    r"""A DataAccessScope is a boolean expression of data access
    labels used to restrict access to data for users.

    Attributes:
        name (str):
            Required. The unique full name of the data
            access scope. The name should comply with
            https://google.aip.dev/122 standards.
        allowed_data_access_labels (MutableSequence[google.cloud.chronicle_v1.types.DataAccessLabelReference]):
            Optional. The allowed labels for the scope. Either allow_all
            or allowed_data_access_labels needs to be provided. When
            provided, there has to be at least one label allowed for the
            scope to be valid. The logical operator for evaluation of
            the allowed labels is OR. E.g.: A customer with scope with
            allowed labels A and B will be able to see data with labeled
            with A or B or (A and B).
        denied_data_access_labels (MutableSequence[google.cloud.chronicle_v1.types.DataAccessLabelReference]):
            Optional. The denied labels for the scope.
            The logical operator for evaluation of the
            denied labels is AND. E.g.: A customer with
            scope with denied labels A and B won't be able
            to see data labeled with A and data labeled with
            B and data with labels A and B.
        display_name (str):
            Output only. The name to be used for display
            to customers of the data access scope.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data
            access scope was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which the data
            access scope was last updated.
        author (str):
            Output only. The user who created the data
            access scope.
        last_editor (str):
            Output only. The user who last updated the
            data access scope.
        description (str):
            Optional. A description of the data access
            scope for a human reader.
        allow_all (bool):
            Optional. Whether or not the scope allows all labels,
            allow_all and allowed_data_access_labels are mutually
            exclusive and one of them must be present.
            denied_data_access_labels can still be used along with
            allow_all. When combined with denied_data_access_labels,
            access will be granted to all data that doesn't have labels
            mentioned in denied_data_access_labels. E.g.: A customer
            with scope with denied labels A and B and allow_all will be
            able to see all data except data labeled with A and data
            labeled with B and data with labels A and B.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    allowed_data_access_labels: MutableSequence["DataAccessLabelReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=2,
            message="DataAccessLabelReference",
        )
    )
    denied_data_access_labels: MutableSequence["DataAccessLabelReference"] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=3,
            message="DataAccessLabelReference",
        )
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
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
    author: str = proto.Field(
        proto.STRING,
        number=7,
    )
    last_editor: str = proto.Field(
        proto.STRING,
        number=8,
    )
    description: str = proto.Field(
        proto.STRING,
        number=9,
    )
    allow_all: bool = proto.Field(
        proto.BOOL,
        number=10,
    )


class DataAccessLabelReference(proto.Message):
    r"""Reference object to a data access label.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        data_access_label (str):
            The name of the data access label.

            This field is a member of `oneof`_ ``label``.
        log_type (str):
            The name of the log type.

            This field is a member of `oneof`_ ``label``.
        asset_namespace (str):
            The asset namespace configured in the
            forwarder of the customer's events.

            This field is a member of `oneof`_ ``label``.
        ingestion_label (google.cloud.chronicle_v1.types.IngestionLabel):
            The ingestion label configured in the
            forwarder of the customer's events.

            This field is a member of `oneof`_ ``label``.
        display_name (str):
            Output only. The display name of the label.
            Data access label and log types's name
            will match the display name of the resource.
            The asset namespace will match the namespace
            itself. The ingestion key value pair will match
            the key of the tuple.
    """

    data_access_label: str = proto.Field(
        proto.STRING,
        number=1,
        oneof="label",
    )
    log_type: str = proto.Field(
        proto.STRING,
        number=2,
        oneof="label",
    )
    asset_namespace: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="label",
    )
    ingestion_label: "IngestionLabel" = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="label",
        message="IngestionLabel",
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )


class IngestionLabel(proto.Message):
    r"""Representation of an ingestion label type.

    Attributes:
        ingestion_label_key (str):
            Required. The key of the ingestion label.
            Always required.
        ingestion_label_value (str):
            Optional. The value of the ingestion label.
            Optional. An object with no provided value and
            some key provided would match against the given
            key and ANY value.
    """

    ingestion_label_key: str = proto.Field(
        proto.STRING,
        number=1,
    )
    ingestion_label_value: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
