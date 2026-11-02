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
import logging
from typing import Any

from google.cloud.spannerlib.pool import Pool  # type: ignore[import-untyped]

from . import errors
from .cursor import Cursor

logger = logging.getLogger(__name__)


def check_not_closed(function):
    """`Connection` class methods decorator.

    Raise an exception if the connection is closed.

    :raises: :class:`InterfaceError` if the connection is closed.
    """

    def wrapper(connection, *args, **kwargs):
        if connection._closed:
            raise errors.InterfaceError("Connection is closed")

        return function(connection, *args, **kwargs)

    return wrapper


class Connection:
    """Connection to a Google Cloud Spanner database.

    This class provides a connection to the Spanner database and adheres to
    PEP 249 (Python Database API Specification v2.0).
    """

    def __init__(self, internal_connection: Any):
        """
        Args:
            internal_connection: An instance of
                google.cloud.spannerlib.Connection
        """
        self._internal_conn = internal_connection
        self._closed = False
        self._messages: list[Any] = []

    @property
    def messages(self) -> list[Any]:
        """Return the list of messages sent to the client by the database."""
        return self._messages

    @check_not_closed
    def cursor(self) -> Cursor:
        """Return a new Cursor Object using the connection.

        Returns:
            Cursor: A cursor object.
        """
        return Cursor(self)

    @check_not_closed
    def begin(self) -> None:
        """Begin a new transaction."""
        logger.debug("Beginning transaction")
        try:
            self._internal_conn.begin_transaction()
        except Exception as e:
            raise errors.map_spanner_error(e)

    @check_not_closed
    def commit(self) -> None:
        """Commit any pending transaction to the database.

        This is a no-op if there is no active client transaction.
        """
        logger.debug("Committing transaction")
        try:
            self._internal_conn.commit()
        except Exception as e:
            logger.debug(f"Commit failed {e}")
            raise errors.map_spanner_error(e)

    @check_not_closed
    def rollback(self) -> None:
        """Rollback any pending transaction to the database.

        This is a no-op if there is no active client transaction.
        """
        logger.debug("Rolling back transaction")
        try:
            self._internal_conn.rollback()
        except Exception as e:
            logger.debug(f"Rollback failed {e}")
            raise errors.map_spanner_error(e)

    def close(self) -> None:
        """Close the connection now.

        The connection will be unusable from this point forward; an Error (or
        subclass) exception will be raised if any operation is attempted with
        the connection. The same applies to all cursor objects trying to use
        the connection.
        """
        if self._closed:
            raise errors.InterfaceError("Connection is already closed")

        logger.debug("Closing connection")
        self._internal_conn.close()
        self._closed = True

    def __enter__(self) -> "Connection":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.close()


def connect(connection_string: str) -> Connection:
    logger.debug(f"Connecting to {connection_string}")
    # Create the pool
    pool = Pool.create_pool(connection_string)

    # Create the low-level connection
    internal_conn = pool.create_connection()

    return Connection(internal_conn)
