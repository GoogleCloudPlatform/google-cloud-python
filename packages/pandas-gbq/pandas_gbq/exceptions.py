# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


class DatasetCreationError(ValueError):
    """
    Raised when the create dataset method fails
    """


class InvalidColumnOrder(ValueError):
    """
    Raised when the provided column order for output
    results DataFrame does not match the schema
    returned by BigQuery.
    """


class InvalidIndexColumn(ValueError):
    """
    Raised when the provided index column for output
    results DataFrame does not match the schema
    returned by BigQuery.
    """


class InvalidPageToken(ValueError):
    """
    Raised when Google BigQuery fails to return,
    or returns a duplicate page token.
    """


class InvalidSchema(ValueError):
    """
    Raised when the provided DataFrame does
    not match the schema of the destination
    table in BigQuery.
    """

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self) -> str:
        return self._message


class NotFoundException(ValueError):
    """
    Raised when the project_id, table or dataset provided in the query could
    not be found.
    """


class TableCreationError(ValueError):
    """
    Raised when the create table method fails
    """

    def __init__(self, message: str):
        self._message = message

    @property
    def message(self) -> str:
        return self._message


class GenericGBQException(ValueError):
    """
    Raised when an unrecognized Google API Error occurs.
    """


class AccessDenied(ValueError):
    """
    Raised when invalid credentials are provided, or tokens have expired.
    """


class ConversionError(GenericGBQException):
    """
    Raised when there is a problem converting the DataFrame to a format
    required to upload it to BigQuery.
    """


class InvalidPrivateKeyFormat(ValueError):
    """
    Raised when provided private key has invalid format.
    """


class LargeResultsWarning(UserWarning):
    """Raise when results are beyond that recommended for pandas DataFrame."""


class PerformanceWarning(RuntimeWarning):
    """
    Raised when a performance-related feature is requested, but unsupported.

    Such warnings can occur when dependencies for the requested feature
    aren't up-to-date.
    """


class QueryTimeout(ValueError):
    """
    Raised when the query request exceeds the timeoutMs value specified in the
    BigQuery configuration.
    """


def translate_exception(ex):
    # See `BigQuery Troubleshooting Errors
    # <https://cloud.google.com/bigquery/troubleshooting-errors>`__

    message = (
        ex.message.casefold()
        if hasattr(ex, "message") and ex.message is not None
        else ""
    )
    if "cancelled" in message:
        return QueryTimeout("Reason: {0}".format(ex))
    elif "schema does not match" in message:
        error_message = ex.errors[0]["message"]
        return InvalidSchema(f"Reason: {error_message}")
    elif "already exists: table" in message:
        error_message = ex.errors[0]["message"]
        return TableCreationError(f"Reason: {error_message}")
    else:
        return GenericGBQException("Reason: {0}".format(ex))
