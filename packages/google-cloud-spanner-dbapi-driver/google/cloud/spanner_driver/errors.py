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
"""
Spanner Python Driver Errors.

DBAPI-defined Exceptions are defined in the following hierarchy::

    Exceptions
    |__Warning
    |__Error
       |__InterfaceError
       |__DatabaseError
          |__DataError
          |__OperationalError
          |__IntegrityError
          |__InternalError
          |__ProgrammingError
          |__NotSupportedError

"""

from typing import Any, Sequence

from google.api_core.exceptions import GoogleAPICallError


class Warning(Exception):
    """Important DB API warning."""

    pass


class Error(Exception):
    """The base class for all the DB API exceptions.

    Does not include :class:`Warning`.
    """

    def _is_error_cause_instance_of_google_api_exception(self) -> bool:
        return isinstance(self.__cause__, GoogleAPICallError)

    @property
    def reason(self) -> str | None:
        """The reason of the error.
        Reference:
            https://cloud.google.com/apis/design/errors#error_info
        Returns:
            Union[str, None]: An optional string containing reason of the error.
        """
        return (
            self.__cause__.reason
            if isinstance(self.__cause__, GoogleAPICallError)
            else None
        )

    @property
    def domain(self) -> str | None:
        """The logical grouping to which the "reason" belongs.
        Reference:
            https://cloud.google.com/apis/design/errors#error_info
        Returns:
            Union[str, None]: An optional string containing a logical grouping
            to which the "reason" belongs.
        """
        return (
            self.__cause__.domain
            if isinstance(self.__cause__, GoogleAPICallError)
            else None
        )

    @property
    def metadata(self) -> dict[str, str] | None:
        """Additional structured details about this error.
        Reference:
            https://cloud.google.com/apis/design/errors#error_info
        Returns:
            Union[Dict[str, str], None]: An optional object containing
            structured details about the error.
        """
        return (
            self.__cause__.metadata
            if isinstance(self.__cause__, GoogleAPICallError)
            else None
        )

    @property
    def details(self) -> Sequence[Any] | None:
        """Information contained in google.rpc.status.details.
        Reference:
            https://cloud.google.com/apis/design/errors#error_model
            https://cloud.google.com/apis/design/errors#error_details
        Returns:
            Sequence[Any]: A list of structured objects from
            error_details.proto
        """
        return (
            self.__cause__.details
            if isinstance(self.__cause__, GoogleAPICallError)
            else None
        )


class InterfaceError(Error):
    """
    Error related to the database interface
    rather than the database itself.
    """

    pass


class DatabaseError(Error):
    """Error related to the database."""

    pass


class DataError(DatabaseError):
    """
    Error due to problems with the processed data like
    division by zero, numeric value out of range, etc.
    """

    pass


class OperationalError(DatabaseError):
    """
    Error related to the database's operation, e.g. an
    unexpected disconnect, the data source name is not
    found, a transaction could not be processed, a
    memory allocation error, etc.
    """

    pass


class IntegrityError(DatabaseError):
    """
    Error for cases of relational integrity of the database
    is affected, e.g. a foreign key check fails.
    """

    pass


class InternalError(DatabaseError):
    """
    Internal database error, e.g. the cursor is not valid
    anymore, the transaction is out of sync, etc.
    """

    pass


class ProgrammingError(DatabaseError):
    """
    Programming error, e.g. table not found or already
    exists, syntax error in the SQL statement, wrong
    number of parameters specified, etc.
    """

    pass


class NotSupportedError(DatabaseError):
    """
    Error for case of a method or database API not
    supported by the database was used.
    """

    pass


def map_spanner_error(error: Exception) -> Error:
    """Map SpannerLibError or GoogleAPICallError to DB API 2.0 errors."""
    from google.api_core import exceptions
    from google.cloud.spannerlib.internal.errors import (  # type: ignore[import-untyped]
        SpannerLibError,
    )

    match error:
        # Handle SpannerLibError by matching on the internal
        # error_code attribute
        case SpannerLibError(error_code=code):
            match code:
                # 3 - INVALID_ARGUMENT
                # 5 - NOT_FOUND
                case 3 | 5:
                    return ProgrammingError(error)
                # 6 - ALREADY_EXISTS
                case 6:
                    return IntegrityError(error)
                # 11 - OUT_OF_RANGE
                case 11:
                    return DataError(error)
                # 1 - CANCELLED
                # 4 - DEADLINE_EXCEEDED
                # 7 - PERMISSION_DENIED
                # 9 - FAILED_PRECONDITION
                # 10 - ABORTED
                # 14 - INTERNAL
                # 16 - UNAUTHENTICATED
                case 1 | 4 | 7 | 9 | 10 | 14 | 16:
                    return OperationalError(error)
                # 13 - INTERNAL
                case 13:
                    return InternalError(error)
                case _:
                    return DatabaseError(error)

        # Handle standard api_core exceptions
        case exceptions.InvalidArgument() | exceptions.NotFound():
            return ProgrammingError(error)
        case exceptions.AlreadyExists():
            return IntegrityError(error)
        case exceptions.OutOfRange():
            return DataError(error)
        case (
            exceptions.FailedPrecondition()
            | exceptions.Unauthenticated()
            | exceptions.PermissionDenied()
            | exceptions.DeadlineExceeded()
            | exceptions.ServiceUnavailable()
            | exceptions.Aborted()
            | exceptions.Cancelled()
        ):
            return OperationalError(error)
        case exceptions.InternalServerError():
            return InternalError(error)
        case _:
            return DatabaseError(error)
