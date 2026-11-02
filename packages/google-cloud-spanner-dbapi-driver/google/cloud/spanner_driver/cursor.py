#  Copyright 2026 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import base64
import datetime
import logging
import uuid
from enum import Enum
from typing import TYPE_CHECKING, Any, Iterable

from google.cloud.spanner_v1 import (
    ExecuteBatchDmlRequest,
    ExecuteSqlRequest,
    Type,
    TypeCode,
)

from . import errors
from .types import _type_code_to_dbapi_type

if TYPE_CHECKING:
    from .connection import Connection

logger = logging.getLogger(__name__)


def check_not_closed(function):
    """`Cursor` class methods decorator.

    Raise an exception if the cursor is closed.

    :raises: :class:`InterfaceError` if the cursor is closed.
    """

    def wrapper(cursor, *args, **kwargs):
        if cursor._closed:
            raise errors.InterfaceError("Cursor is closed")

        return function(cursor, *args, **kwargs)

    return wrapper


class FetchScope(Enum):
    FETCH_ONE = 1
    FETCH_MANY = 2
    FETCH_ALL = 3


class Cursor:
    """Cursor object for the Google Cloud Spanner database.

    This class lets you use a cursor to interact with the database.
    """

    def __init__(self, connection: "Connection"):
        self._connection = connection
        self._rows: Any = None  # Holds the google.cloud.spannerlib.rows.Rows object
        self._closed = False
        self.arraysize = 1
        self._rowcount = -1

    @property
    def description(self) -> tuple[tuple[Any, ...], ...] | None:
        """
        This read-only attribute is a sequence of 7-item sequences.

        Each of these sequences contains information describing one result
        column:
        - name
        - type_code
        - display_size
        - internal_size
        - precision
        - scale
        - null_ok

        The first two items (name and type_code) are mandatory, the other
        five are optional and are set to None if no meaningful values can be
        provided.

        This attribute will be None for operations that do not return rows or
        if the cursor has not had an operation invoked via the .execute*()
        method yet.
        """
        logger.debug("Fetching description for cursor")
        if not self._rows:
            return None

        try:
            metadata = self._rows.metadata()
            if not metadata or not metadata.row_type:
                return None

            desc = []
            for field in metadata.row_type.fields:
                desc.append(
                    (
                        field.name,
                        _type_code_to_dbapi_type(field.type.code),
                        None,  # display_size
                        None,  # internal_size
                        None,  # precision
                        None,  # scale
                        True,  # null_ok
                    )
                )
            return tuple(desc)
        except Exception as e:
            logger.warning("Could not determine cursor description: %s", e)
            return None

    @property
    def rowcount(self) -> int:
        """
        This read-only attribute specifies the number of rows that the last
        .execute*() produced (for DQL statements like 'select') or affected
        (for DML statements like 'update' or 'insert').

        The attribute is -1 in case no .execute*() has been performed on the
        cursor or the rowcount of the last operation cannot be determined by
        the interface.
        """
        return self._rowcount

    def _prepare_params(
        self, parameters: dict[str, Any] | list[Any] | tuple[Any] | None = None
    ) -> tuple[dict[str, Any] | None, dict[str, Type] | None]:
        """
        Prepares parameters for Spanner execution

        Args:
            parameters: A dictionary (for named parameters/GoogleSQL)
                        or a list/tuple
                        (for positional parameters/PostgreSQL).

        Returns:
            A tuple containing:
            - converted_params: Dictionary of parameters with values
            converted for Spanner (e.g. ints to strings).
            - param_types: Dictionary mapping parameter names to
            their Spanner Type.
        """
        if not parameters:
            return {}, {}

        converted_params: dict[str, Any] = {}
        param_types = {}

        # Normalize input to an iterable of (key, value)
        iterator: Iterable[tuple[str, Any]]
        if isinstance(parameters, (list, tuple)):
            # PostgreSQL Dialect: Positional parameters $1, $2... are
            # mapped to P1, P2...
            iterator = ((f"P{i}", val) for i, val in enumerate(parameters, 1))
        elif isinstance(parameters, dict):
            # GoogleSQL Dialect: Named parameters @name are mapped directly.
            iterator = parameters.items()
        else:
            raise errors.ProgrammingError(
                f"Parameters must be a dict, list, or tuple, not {type(parameters).__name__}"
            )

        for key, value in iterator:
            if value is None:
                converted_params[key] = None
                continue
            # Note: check bool before int, as bool is a subclass of int
            if isinstance(value, bool):
                converted_params[key] = value
                param_types[key] = Type(code=TypeCode.BOOL)
            elif isinstance(value, int):
                # Spanner expects INT64 as strings to preserve precision
                # in JSON
                converted_params[key] = str(value)
                param_types[key] = Type(code=TypeCode.INT64)
            elif isinstance(value, float):
                converted_params[key] = value
                param_types[key] = Type(code=TypeCode.FLOAT64)
            elif isinstance(value, bytes):
                converted_params[key] = value
                param_types[key] = Type(code=TypeCode.BYTES)
            elif isinstance(value, uuid.UUID):
                # Convert UUID to string as requested
                converted_params[key] = str(value)
                # Use STRING type for UUIDs (unless specific UUID type is
                # required/supported by your backend version)
                param_types[key] = Type(code=TypeCode.STRING)
            elif isinstance(value, datetime.datetime):
                # Convert Datetime to string (RFC 3339 format is standard
                # for str(datetime))
                converted_params[key] = str(value)
                param_types[key] = Type(code=TypeCode.TIMESTAMP)
            elif isinstance(value, datetime.date):
                converted_params[key] = str(value)
                param_types[key] = Type(code=TypeCode.DATE)
            else:
                # Fallback for strings and other types
                converted_params[key] = value
                # For strings, we can explicitly set the type or let it default.
                if isinstance(value, str):
                    param_types[key] = Type(code=TypeCode.STRING)

        return converted_params, param_types

    @check_not_closed
    def execute(
        self,
        operation: str,
        parameters: dict[str, Any] | list[Any] | tuple[Any] | None = None,
    ) -> None:
        """Prepare and execute a database operation (query or command).

        Parameters may be provided as sequence or mapping and will be bound to
        variables in the operation. Variables are specified in a
        database-specific notation (see the module's paramstyle attribute for
        details).

        Args:
            operation (str): The SQL statement to execute.
            parameters (dict | list | tuple, optional): parameters to bind.
        """
        logger.debug(f"Executing operation: {operation}")

        request = ExecuteSqlRequest(sql=operation)
        params, _ = self._prepare_params(parameters)
        request.params = params  # type: ignore[assignment]

        try:
            self._rows = self._connection._internal_conn.execute(request)

            if self.description:
                self._rowcount = -1
            else:
                update_count = self._rows.update_count()
                if update_count != -1:
                    self._rowcount = update_count
                self._rows.close()
                self._rows = None

        except Exception as e:
            raise errors.map_spanner_error(e) from e

    @check_not_closed
    def executemany(
        self,
        operation: str,
        seq_of_parameters: (list[dict[str, Any]] | list[list[Any]] | list[tuple[Any]]),
    ) -> None:
        """Prepare a database operation (query or command) and then execute it
        against all parameter sequences or mappings found in the sequence
        seq_of_parameters.

        Args:
            operation (str): The SQL statement to execute.
            seq_of_parameters (list): A list of parameter sequences/mappings.
        """
        logger.debug(f"Executing batch operation: {operation}")

        request = ExecuteBatchDmlRequest()

        for parameters in seq_of_parameters:
            statement = ExecuteBatchDmlRequest.Statement(sql=operation)
            params, _ = self._prepare_params(parameters)
            statement.params = params  # type: ignore[assignment]

            request.statements.append(statement)

        try:
            response = self._connection._internal_conn.execute_batch(request)
            total_rowcount = 0
            for result_set in response.result_sets:
                if result_set.stats.row_count_exact != -1:
                    total_rowcount += result_set.stats.row_count_exact
                elif result_set.stats.row_count_lower_bound != -1:
                    total_rowcount += result_set.stats.row_count_lower_bound
            self._rowcount = total_rowcount

        except Exception as e:
            raise errors.map_spanner_error(e) from e

    def _convert_value(self, value: Any, field_type: Any) -> Any:
        kind = value.WhichOneof("kind")
        if kind == "null_value":
            return None
        if kind == "bool_value":
            return value.bool_value
        if kind == "number_value":
            return value.number_value
        if kind == "string_value":
            code = field_type.code
            val = value.string_value
            if code == TypeCode.INT64:
                return int(val)
            if code == TypeCode.BYTES or code == TypeCode.PROTO:
                return base64.b64decode(val)
            return val
        if kind == "list_value":
            return [
                self._convert_value(v, field_type.array_element_type)
                for v in value.list_value.values
            ]
        # Fallback for complex types (structs) not fully mapped yet
        return value

    def _convert_row(self, row: Any) -> tuple[Any, ...]:
        metadata = self._rows.metadata()
        fields = metadata.row_type.fields
        converted = []
        for i, value in enumerate(row.values):
            converted.append(self._convert_value(value, fields[i].type))
        return tuple(converted)

    def _fetch(
        self, scope: FetchScope, size: int | None = None
    ) -> list[tuple[Any, ...]]:
        if not self._rows:
            raise errors.ProgrammingError("No result set available")
        try:
            rows = []
            if scope == FetchScope.FETCH_ONE:
                try:
                    row = self._rows.next()
                    if row is not None:
                        rows.append(self._convert_row(row))
                except StopIteration:
                    pass
            elif scope == FetchScope.FETCH_MANY:
                # size is guaranteed to be int if scope is FETCH_MANY and
                # called from fetchmany but might be None if internal logic
                # changes, strict check would satisfy type checker
                limit = size if size is not None else self.arraysize
                for _ in range(limit):
                    try:
                        row = self._rows.next()
                        if row is None:
                            break
                        rows.append(self._convert_row(row))
                    except StopIteration:
                        break
            elif scope == FetchScope.FETCH_ALL:
                while True:
                    try:
                        row = self._rows.next()
                        if row is None:
                            break
                        rows.append(self._convert_row(row))
                    except StopIteration:
                        break
        except Exception as e:
            raise errors.map_spanner_error(e) from e

        return rows

    @check_not_closed
    def fetchone(self) -> tuple[Any, ...] | None:
        """Fetch the next row of a query result set, returning a single
        sequence, or None when no more data is available.

        Returns:
            tuple | None: A row of data or None.
        """
        logger.debug("Fetching one row")
        rows = self._fetch(FetchScope.FETCH_ONE)
        if not rows:
            return None
        return rows[0]

    @check_not_closed
    def fetchmany(self, size: int | None = None) -> list[tuple[Any, ...]]:
        """Fetch the next set of rows of a query result, returning a sequence
        of sequences (e.g. a list of tuples). An empty sequence is returned
        when no more rows are available.

        The number of rows to fetch per call is specified by the parameter. If
        it is not given, the cursor's arraysize determines the number of rows
        to be fetched.

        Args:
            size (int, optional): The number of rows to fetch.

        Returns:
            list[tuple]: A list of rows.
        """
        logger.debug("Fetching many rows")
        if size is None:
            size = self.arraysize
        return self._fetch(FetchScope.FETCH_MANY, size)

    @check_not_closed
    def fetchall(self) -> list[tuple[Any, ...]]:
        """Fetch all (remaining) rows of a query result, returning them as a
        sequence of sequences (e.g. a list of tuples).

        Returns:
            list[tuple]: A list of rows.
        """
        logger.debug("Fetching all rows")
        return self._fetch(FetchScope.FETCH_ALL)

    def close(self) -> None:
        """Close the cursor now.

        The cursor will be unusable from this point forward; an Error (or
        subclass) exception will be raised if any operation is attempted with
        the cursor.
        """
        logger.debug("Closing cursor")
        self._closed = True
        if self._rows:
            self._rows.close()

    @check_not_closed
    def nextset(self) -> bool | None:
        """Skip to the next available set of results."""
        logger.debug("Fetching next set of results")
        if not self._rows:
            return None

        try:
            next_metadata = self._rows.next_result_set()
            if next_metadata:
                return True
            return None
        except Exception as e:
            logger.warning("Could not determine next set of results: %s", e)
            return None

    def __enter__(self) -> "Cursor":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()

    def __iter__(self) -> "Cursor":
        return self

    def __next__(self) -> tuple[Any, ...]:
        row = self.fetchone()
        if row is None:
            raise StopIteration
        return row

    @check_not_closed
    def setinputsizes(self, sizes: list[Any]) -> None:
        """Predefine memory areas for parameters.
        This operation is a no-op implementation.
        """
        logger.debug("NO-OP: Setting input sizes")
        pass

    @check_not_closed
    def setoutputsize(self, size: int, column: int | None = None) -> None:
        """Set a column buffer size.
        This operation is a no-op implementation.
        """
        logger.debug("NO-OP: Setting output size")
        pass

    @check_not_closed
    def callproc(
        self, procname: str, parameters: list[Any] | tuple[Any] | None = None
    ) -> None:
        """Call a stored database procedure with the given name.

        This method is not supported by Spanner.
        """
        logger.debug("NO-OP: Calling stored procedure")
        raise errors.NotSupportedError("Stored procedures are not supported.")
