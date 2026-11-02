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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.chronicle.v1",
    manifest={
        "DataTableUpdateSource",
        "CreateDataTableRequest",
        "GetDataTableRequest",
        "UpdateDataTableRequest",
        "ListDataTablesRequest",
        "DeleteDataTableRequest",
        "ListDataTablesResponse",
        "CreateDataTableRowRequest",
        "UpdateDataTableRowRequest",
        "ListDataTableRowsRequest",
        "ListDataTableRowsResponse",
        "GetDataTableRowRequest",
        "DeleteDataTableRowRequest",
        "BulkCreateDataTableRowsRequest",
        "BulkCreateDataTableRowsResponse",
        "BulkGetDataTableRowsRequest",
        "BulkGetDataTableRowsResponse",
        "BulkReplaceDataTableRowsRequest",
        "BulkReplaceDataTableRowsResponse",
        "BulkUpdateDataTableRowsRequest",
        "BulkUpdateDataTableRowsResponse",
        "DataTableScopeInfo",
        "DataTable",
        "DataTableRow",
        "DataTableColumnInfo",
        "GetDataTableOperationErrorsRequest",
        "DataTableOperationErrors",
    },
)


class DataTableUpdateSource(proto.Enum):
    r"""DataTableUpdateSource denotes the source that updated the
    data table.

    Values:
        DATA_TABLE_UPDATE_SOURCE_UNSPECIFIED (0):
            The data table is updated by the user.
        USER (1):
            The data table is updated by the user.
        RULE (2):
            The data table is updated by the rule.
        SEARCH (3):
            The data table is updated by the search.
    """

    DATA_TABLE_UPDATE_SOURCE_UNSPECIFIED = 0
    USER = 1
    RULE = 2
    SEARCH = 3


class CreateDataTableRequest(proto.Message):
    r"""A request to create DataTable.

    Attributes:
        parent (str):
            Required. The parent resource where this data
            table will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        data_table (google.cloud.chronicle_v1.types.DataTable):
            Required. The data table being created.
        data_table_id (str):
            Required. The ID to use for the data table.
            This is also the display name for the data
            table. It must satisfy the following
            requirements:

            - Starts with letter.
            - Contains only letters, numbers and underscore.
            - Must be unique and has length < 256.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_table: "DataTable" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataTable",
    )
    data_table_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class GetDataTableRequest(proto.Message):
    r"""A request to get details about a data table.

    Attributes:
        name (str):
            Required. The resource name of the data table to retrieve.
            Format:
            projects/{project}/locations/{location}/instances/{instances}/dataTables/{data_table}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataTableRequest(proto.Message):
    r"""A request to update details of data table.

    Attributes:
        data_table (google.cloud.chronicle_v1.types.DataTable):
            Required. This field is used to identify the datatable to
            update. Format:
            projects/{project}/locations/{locations}/instances/{instance}/dataTables/{data_table}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of metadata fields to update. Currently
            data tables only support updating the ``description``,
            ``row_time_to_live`` and ``scope_info`` fields. When no
            field mask is supplied, all non-empty fields will be
            updated. A field mask of "\*" will update all fields,
            whether empty or not.
    """

    data_table: "DataTable" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataTable",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListDataTablesRequest(proto.Message):
    r"""A request for a list of data tables.

    Attributes:
        parent (str):
            Required. The parent resource where this data
            table will be created. Format:
            projects/{project}/locations/{location}/instances/{instance}
        page_size (int):
            Optional. The maximum number of data tables
            to return. The service may return fewer than
            this value. If unspecified, at most 100 data
            tables will be returned. The maximum value is
            1000; values above 1000 will be coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDataTables`` call. Provide this to retrieve the
            subsequent page. When paginating, all other parameters
            provided to ``ListDataTables`` must match the call that
            provided the page token.
        order_by (str):
            Optional. Configures ordering of DataTables in the response.
            Note: Our implementation currently supports order by
            "create_time asc" only
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteDataTableRequest(proto.Message):
    r"""Request message for deleting data tables.

    Attributes:
        name (str):
            Required. The resource name of the data table to delete.
            Format
            projects/{project}/locations/{location}/instances/{instances}/dataTables/{data_table}
        force (bool):
            Optional. If set to true, any rows under this
            data table will also be deleted. (Otherwise, the
            request will only work if the data table has no
            rows.)
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class ListDataTablesResponse(proto.Message):
    r"""Response message for listing data tables.

    Attributes:
        data_tables (MutableSequence[google.cloud.chronicle_v1.types.DataTable]):
            The list of the data tables returned.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
    """

    @property
    def raw_page(self):
        return self

    data_tables: MutableSequence["DataTable"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTable",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class CreateDataTableRowRequest(proto.Message):
    r"""Request to create data table row.

    Attributes:
        parent (str):
            Required. The resource id of the data table. Format:
            /projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}
        data_table_row (google.cloud.chronicle_v1.types.DataTableRow):
            Required. The data table row to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_table_row: "DataTableRow" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="DataTableRow",
    )


class UpdateDataTableRowRequest(proto.Message):
    r"""Request to update data table row.

    Attributes:
        data_table_row (google.cloud.chronicle_v1.types.DataTableRow):
            Required. Format:
            projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}/dataTableRows/{data_table_row}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update. Currently data table
            rows only support updating the ``values`` field. When no
            field mask is supplied, all non-empty fields will be
            updated. A field mask of "\*" will update all fields,
            whether empty or not.
    """

    data_table_row: "DataTableRow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="DataTableRow",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListDataTableRowsRequest(proto.Message):
    r"""Request to list data table rows.

    Attributes:
        parent (str):
            Required. The resource id of the data table. Format:
            projects/{project}/locations/{locations}/instances/{instance}/dataTables/{data_table}
        page_size (int):
            Optional. The maximum number of data table
            rows to return. The service may return fewer
            than this value. If unspecified, at most 100
            data table rows will be returned. The maximum
            value is 1000; values above 1000 will be coerced
            to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListDataTableRows`` call.
        order_by (str):
            Optional. Configures ordering of DataTables in the response.
            Note: Our implementation currently supports order by
            "create_time asc" only
        filter (str):
            Optional. Filter facilitating search over
            data table rows. This filter performs a
            case-insensitive substring match on the row
            values.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=4,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListDataTableRowsResponse(proto.Message):
    r"""Response message for listing data table rows.

    Attributes:
        data_table_rows (MutableSequence[google.cloud.chronicle_v1.types.DataTableRow]):
            The list of the data table rows returned.
        next_page_token (str):
            Optional. A token, which can be sent as ``page_token`` to
            retrieve the next page. If this field is omitted, there are
            no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    data_table_rows: MutableSequence["DataTableRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTableRow",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetDataTableRowRequest(proto.Message):
    r"""Request to get data table row.

    Attributes:
        name (str):
            Required. The resource name of the data table row i,e
            row_id. Format:
            projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}/dataTableRows/{data_table_row}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DeleteDataTableRowRequest(proto.Message):
    r"""Request to delete data table row.

    Attributes:
        name (str):
            Required. The resource name of the data table row i,e
            row_id. Format:
            projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}/dataTableRows/{data_table_row}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class BulkCreateDataTableRowsRequest(proto.Message):
    r"""Request to create data table rows in bulk.

    Attributes:
        parent (str):
            Required. The resource id of the data table. Format:
            /projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}
        requests (MutableSequence[google.cloud.chronicle_v1.types.CreateDataTableRowRequest]):
            Required. Data table rows to create. A
            maximum of 1000 rows (for sync requests) or 2000
            rows (for async requests) can be created in a
            single request. Total size of the rows should be
            less than 4MB.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateDataTableRowRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateDataTableRowRequest",
    )


class BulkCreateDataTableRowsResponse(proto.Message):
    r"""Response message with created data table rows.

    Attributes:
        data_table_rows (MutableSequence[google.cloud.chronicle_v1.types.DataTableRow]):
            DataTableRows created
    """

    data_table_rows: MutableSequence["DataTableRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTableRow",
    )


class BulkGetDataTableRowsRequest(proto.Message):
    r"""Request to get data table rows in bulk.

    Attributes:
        parent (str):
            Required. The resource id of the data table. Format:
            /projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}
        requests (MutableSequence[google.cloud.chronicle_v1.types.GetDataTableRowRequest]):
            Required. Data table rows to get. At max
            1,000 rows can be there in a request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["GetDataTableRowRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="GetDataTableRowRequest",
    )


class BulkGetDataTableRowsResponse(proto.Message):
    r"""Response message with data table rows.

    Attributes:
        data_table_rows (MutableSequence[google.cloud.chronicle_v1.types.DataTableRow]):
            The requested data table rows.
    """

    data_table_rows: MutableSequence["DataTableRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTableRow",
    )


class BulkReplaceDataTableRowsRequest(proto.Message):
    r"""Request to replace data table rows in bulk.

    Attributes:
        parent (str):
            Required. The resource id of the data table. Format:
            /projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}
        requests (MutableSequence[google.cloud.chronicle_v1.types.CreateDataTableRowRequest]):
            Required. Data table rows to replace the
            existing data table rows. A maximum of 1000 rows
            (for sync requests) or 2000 rows (for async
            requests) can be replaced in a single request.
            Total size of the rows should be less than 4MB.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateDataTableRowRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateDataTableRowRequest",
    )


class BulkReplaceDataTableRowsResponse(proto.Message):
    r"""Response message with data table rows that replaced existing
    data table rows.

    Attributes:
        data_table_rows (MutableSequence[google.cloud.chronicle_v1.types.DataTableRow]):
            DataTableRows that replaced existing data
            table rows
    """

    data_table_rows: MutableSequence["DataTableRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTableRow",
    )


class BulkUpdateDataTableRowsRequest(proto.Message):
    r"""Request to update data table rows in bulk.

    Attributes:
        parent (str):
            Required. The resource id of the data table. Format:
            /projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}
        requests (MutableSequence[google.cloud.chronicle_v1.types.UpdateDataTableRowRequest]):
            Required. Data table rows to update. At max
            1,000 rows (or rows with size less than 2MB) can
            be there in a request.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateDataTableRowRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateDataTableRowRequest",
    )


class BulkUpdateDataTableRowsResponse(proto.Message):
    r"""Response message with updated data table rows.

    Attributes:
        data_table_rows (MutableSequence[google.cloud.chronicle_v1.types.DataTableRow]):
            DataTableRows updated
    """

    data_table_rows: MutableSequence["DataTableRow"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="DataTableRow",
    )


class DataTableScopeInfo(proto.Message):
    r"""DataTableScopeInfo specifies the scope info of the data
    table.

    Attributes:
        data_access_scopes (MutableSequence[str]):
            Required. Contains the list of scope names of the data
            table. If the list is empty, the data table is treated as
            unscoped. The scope names should be full resource names and
            should be of the format:
            "projects/{project}/locations/{location}/instances/{instance}/dataAccessScopes/{scope_name}".
    """

    data_access_scopes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


class DataTable(proto.Message):
    r"""DataTable represents the data table resource.

    Attributes:
        name (str):
            Identifier. The resource name of the data table Format:
            "{project}/locations/{location}/instances/{instance}/dataTables/{data_table}".
        display_name (str):
            Output only. The unique display name of the
            data table.
        description (str):
            Required. A user-provided description of the
            data table.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Table create time
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Table update time
        column_info (MutableSequence[google.cloud.chronicle_v1.types.DataTableColumnInfo]):
            Immutable. Details of all the columns in the
            table
        data_table_uuid (str):
            Output only. Data table unique id
        rules (MutableSequence[str]):
            Output only. The resource names for the
            associated Rules that use this data table.
            Format:

            projects/{project}/locations/{location}/instances/{instance}/rules/{rule}.
            {rule} here refers to the rule id.
        rule_associations_count (int):
            Output only. The count of rules using the
            data table.
        row_time_to_live (str):
            Optional. User-provided TTL of the data
            table.
        approximate_row_count (int):
            Output only. The count of rows in the data
            table.
        scope_info (google.cloud.chronicle_v1.types.DataTableScopeInfo):
            Optional. The scope info of the data table. During data
            table creation, if this field is not set, the data table
            without scopes (an unscoped table) will be created for a
            global user. For a scoped user, this field must be set.
            During data table update, if scope_info is requested to be
            updated, this field must be set.
        update_source (google.cloud.chronicle_v1.types.DataTableUpdateSource):
            Output only. Source of the data table update.
        row_time_to_live_update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Last update time of the TTL of
            the data table.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
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
    column_info: MutableSequence["DataTableColumnInfo"] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="DataTableColumnInfo",
    )
    data_table_uuid: str = proto.Field(
        proto.STRING,
        number=7,
    )
    rules: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    rule_associations_count: int = proto.Field(
        proto.INT32,
        number=9,
    )
    row_time_to_live: str = proto.Field(
        proto.STRING,
        number=10,
    )
    approximate_row_count: int = proto.Field(
        proto.INT64,
        number=11,
    )
    scope_info: "DataTableScopeInfo" = proto.Field(
        proto.MESSAGE,
        number=12,
        message="DataTableScopeInfo",
    )
    update_source: "DataTableUpdateSource" = proto.Field(
        proto.ENUM,
        number=13,
        enum="DataTableUpdateSource",
    )
    row_time_to_live_update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=14,
        message=timestamp_pb2.Timestamp,
    )


class DataTableRow(proto.Message):
    r"""DataTableRow represents a single row in a data table.

    Attributes:
        name (str):
            Identifier. The resource name of the data table Format:
            projects/{project}/locations/{location}/instances/{instance}/dataTables/{data_table}/dataTableRows/{data_table_row}
        values (MutableSequence[str]):
            Required. All column values for a single row.
            The values should be in the same order as the
            columns of the data tables.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. DataTableRow create time
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. DataTableRow update time
        row_time_to_live (str):
            Optional. User-provided TTL of the data table
            row.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    values: MutableSequence[str] = proto.RepeatedField(
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
    row_time_to_live: str = proto.Field(
        proto.STRING,
        number=5,
    )


class DataTableColumnInfo(proto.Message):
    r"""DataTableColumnInfo represents the column metadata of the datatable.
    The column_index represents the ordering of the values in
    DataTableRow.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        mapped_column_path (str):
            Entity proto field path that the column is
            mapped to

            This field is a member of `oneof`_ ``path_or_type``.
        column_type (google.cloud.chronicle_v1.types.DataTableColumnInfo.DataTableColumnType):
            Column type can be STRING, CIDR (Ex-
            10.1.1.0/24), REGEX

            This field is a member of `oneof`_ ``path_or_type``.
        column_index (int):
            Required. Column Index. 0,1,2...
        original_column (str):
            Required. Original column name of the Data
            Table (present in the CSV header in case of
            creation of data tables using file uploads). It
            must satisfy the following requirements:

            - Starts with letter.
            - Contains only letters, numbers and underscore.
            - Must be unique and has length < 256.
        key_column (bool):
            Optional. Whether to include this column in the calculation
            of the row ID. If no columns have key_column = true, all
            columns will be included in the calculation of the row ID.
        repeated_values (bool):
            Optional. Whether the column is a repeated
            values column.
    """

    class DataTableColumnType(proto.Enum):
        r"""DataTableColumnType denotes the type of the column to be
        referenced in the rule.

        Values:
            DATA_TABLE_COLUMN_TYPE_UNSPECIFIED (0):
                The default Data Table Column Type.
            STRING (1):
                Denotes the type of the column as STRING.
            REGEX (2):
                Denotes the type of the column as REGEX.
            CIDR (3):
                Denotes the type of the column as CIDR.
            NUMBER (4):
                Denotes the type of the column as NUMBER
                (includes int and float).
        """

        DATA_TABLE_COLUMN_TYPE_UNSPECIFIED = 0
        STRING = 1
        REGEX = 2
        CIDR = 3
        NUMBER = 4

    mapped_column_path: str = proto.Field(
        proto.STRING,
        number=3,
        oneof="path_or_type",
    )
    column_type: DataTableColumnType = proto.Field(
        proto.ENUM,
        number=4,
        oneof="path_or_type",
        enum=DataTableColumnType,
    )
    column_index: int = proto.Field(
        proto.INT32,
        number=1,
    )
    original_column: str = proto.Field(
        proto.STRING,
        number=2,
    )
    key_column: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    repeated_values: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class GetDataTableOperationErrorsRequest(proto.Message):
    r"""The request message for GetDataTableOperationErrors.

    Attributes:
        name (str):
            Required. Resource name for the data table operation errors.
            Format:
            projects/{project}/locations/{location}/instances/{instance}/dataTableOperationErrors/{data_table_operation_errors}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class DataTableOperationErrors(proto.Message):
    r"""The message containing the errors for a data table operation.

    Attributes:
        name (str):
            Identifier. Resource name for the data table operation
            errors. Format:
            projects/{project}/locations/{location}/instances/{instance}/dataTableOperationErrors/{data_table_operation_errors}
        rpc_errors (MutableSequence[google.rpc.status_pb2.Status]):
            The list of errors. Replaces the deprecated ``errors``
            field.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rpc_errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
