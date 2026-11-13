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
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.oracledatabase.v1",
    manifest={
        "ExecuteSqlRequest",
        "SqlParameter",
        "ExecuteSqlResponse",
        "SqlResult",
        "ExecuteSqlMetadata",
    },
)


class ExecuteSqlRequest(proto.Message):
    r"""The request for ``DatabaseConnection.ExecuteSql``.

    Attributes:
        name (str):
            Required. The name of the DatabaseConnection in the
            following format:
            projects/{project}/locations/{location}/databaseConnections/{database_connection}.
        sql_statement (str):
            Required. The SQL statement to execute.
        params (MutableSequence[google.cloud.oracledatabase_v1.types.SqlParameter]):
            Optional. Optional: Bind variables (parameters) to be used
            with the SQL statement. Supports named bind variables (e.g.,
            :dept_id, :status in Oracle SQL) or positional parameters
            (:1, :2).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    sql_statement: str = proto.Field(
        proto.STRING,
        number=2,
    )
    params: MutableSequence["SqlParameter"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SqlParameter",
    )


class SqlParameter(proto.Message):
    r"""Represents a bind variable (parameter) for SQL execution.

    Attributes:
        name (str):
            Optional. The name of the SQL bind parameter
            (excluding the leading colon, e.g. "id"). If
            omitted, parameters bind positionally based on
            their order in the list.
        value (google.protobuf.struct_pb2.Value):
            Required. Use protobuf.Value so clients can
            pass ints, bools, and strings natively.
        type_name (str):
            Optional. Optional: Datatype hint for the
            parameter (e.g., "VARCHAR2", "NUMBER", "DATE",
            "TIMESTAMP"). If omitted, the Oracle driver will
            infer the type from the value string.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    value: struct_pb2.Value = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Value,
    )
    type_name: str = proto.Field(
        proto.STRING,
        number=3,
    )


class ExecuteSqlResponse(proto.Message):
    r"""Execute a SQL statement response.

    Attributes:
        sql_results (MutableSequence[google.cloud.oracledatabase_v1.types.SqlResult]):
            SqlResult represents the results for the
            execution of sql statements.
        metadata (google.cloud.oracledatabase_v1.types.ExecuteSqlMetadata):
            Any additional metadata information regarding
            the execution of the sql statement.
    """

    sql_results: MutableSequence["SqlResult"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SqlResult",
    )
    metadata: "ExecuteSqlMetadata" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="ExecuteSqlMetadata",
    )


class SqlResult(proto.Message):
    r"""SqlResult represents the result for the execution of a sql
    statement.

    Attributes:
        columns (MutableSequence[google.cloud.oracledatabase_v1.types.SqlResult.Column]):
            List of columns included in the result,
            including data type.
        rows (MutableSequence[google.cloud.oracledatabase_v1.types.SqlResult.Row]):
            Rows returned by the SQL statement.
    """

    class Column(proto.Message):
        r"""Contains the name and datatype of a column in a SQL Result.

        Attributes:
            name (str):
                Required. Name of the column.
            type_ (str):
                Required. Database-specific type name (e.g.,
                "VARCHAR2(255)", "NUMBER", "DATE", "CLOB")
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        type_: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class Row(proto.Message):
        r"""A single row from a sql result.

        Attributes:
            values (MutableSequence[google.cloud.oracledatabase_v1.types.SqlResult.Value]):
                List of values in a row of sql result.
        """

        values: MutableSequence["SqlResult.Value"] = proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message="SqlResult.Value",
        )

    class Value(proto.Message):
        r"""A single value in a row from a sql result.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            value (str):
                The cell value represented in string format.
                Timestamps should be converted using RFC3339Nano
                format.
            null_value (bool):
                Set to true if the cell value is NULL.

                This field is a member of `oneof`_ ``_null_value``.
        """

        value: str = proto.Field(
            proto.STRING,
            number=1,
        )
        null_value: bool = proto.Field(
            proto.BOOL,
            number=2,
            optional=True,
        )

    columns: MutableSequence[Column] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=Column,
    )
    rows: MutableSequence[Row] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message=Row,
    )


class ExecuteSqlMetadata(proto.Message):
    r"""Any additional metadata information regarding the execution
    of the SQL

    Attributes:
        message (str):
            Message related to SQL execution. This field
            can be used to convey size limit related
            message.
        partial_result (bool):
            Set to true if SQL returned a result set
            larger than the acceptable response size limits
            and the result was truncated.
        execution_duration (google.protobuf.duration_pb2.Duration):
            The time duration taken to execute the sql
            statement.
        status (google.cloud.oracledatabase_v1.types.ExecuteSqlMetadata.Status):
            Output only. Status of SQL execution.
    """

    class Status(proto.Enum):
        r"""Status contains all valid statuses a SQL execution can end up
        in.

        Values:
            STATUS_UNSPECIFIED (0):
                Default value. Not returned by the service.
            OK (1):
                No error during SQL execution i.e. All SQL
                statements ran to completion. The "message" will
                be empty.
            PARTIAL (2):
                Same as OK, except indicates that only partial results were
                returned. The "message" field will contain details on why
                results were truncated. ``partial_result`` is true if and
                only if ``status`` is ``PARTIAL``.
            ERROR (3):
                The database returned an error while executing the SQL
                statement. ``message`` contains the error text returned by
                Oracle. ``sql_results`` is empty. The statement runs in
                autocommit mode; which changes are committed or rolled back
                follows Oracle Database behavior. Authentication failures,
                database availability errors, network errors, and timeouts
                are returned as API errors (AIP-193), not as ERROR.
        """

        STATUS_UNSPECIFIED = 0
        OK = 1
        PARTIAL = 2
        ERROR = 3

    message: str = proto.Field(
        proto.STRING,
        number=1,
    )
    partial_result: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    execution_duration: duration_pb2.Duration = proto.Field(
        proto.MESSAGE,
        number=3,
        message=duration_pb2.Duration,
    )
    status: Status = proto.Field(
        proto.ENUM,
        number=4,
        enum=Status,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
