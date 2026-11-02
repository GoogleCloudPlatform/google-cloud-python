# Copyright 2025 Google LLC All rights reserved.
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
import inspect
from datetime import datetime
from logging import Logger
from typing import Mapping

from google.auth.credentials import Credentials, Scoped
from google.cloud._helpers import _datetime_to_pb_timestamp
from mock import create_autospec

from google.cloud.aio._cross_sync import CrossSync
from google.cloud.spanner_dbapi import Connection
from google.cloud.spanner_v1 import SpannerAsyncClient, SpannerClient
from google.cloud.spanner_v1._async.client import Client as AsyncClient
from google.cloud.spanner_v1._async.database import Database as AsyncDatabase
from google.cloud.spanner_v1._async.instance import Instance as AsyncInstance
from google.cloud.spanner_v1._async.session import Session as AsyncSession
from google.cloud.spanner_v1.client import Client
from google.cloud.spanner_v1.database import Database
from google.cloud.spanner_v1.instance import Instance
from google.cloud.spanner_v1.session import Session
from google.cloud.spanner_v1.transaction import Transaction
from google.cloud.spanner_v1.types import CommitResponse as CommitResponsePB
from google.cloud.spanner_v1.types import (
    MultiplexedSessionPrecommitToken as PrecommitTokenPB,
)
from google.cloud.spanner_v1.types import Session as SessionPB
from google.cloud.spanner_v1.types import Transaction as TransactionPB

# Default values used to populate required or expected attributes.
# Tests should not depend on them: if a test requires a specific
# identifier or name, it should set it explicitly.
_PROJECT_ID = "default-project-id"
_INSTANCE_ID = "default-instance-id"
_DATABASE_ID = "default-database-id"
_SESSION_ID = "default-session-id"

_PROJECT_NAME = "projects/" + _PROJECT_ID
_INSTANCE_NAME = _PROJECT_NAME + "/instances/" + _INSTANCE_ID
_DATABASE_NAME = _INSTANCE_NAME + "/databases/" + _DATABASE_ID
_SESSION_NAME = _DATABASE_NAME + "/sessions/" + _SESSION_ID

_TRANSACTION_ID = b"default-transaction-id"
_PRECOMMIT_TOKEN = b"default-precommit-token"
_SEQUENCE_NUMBER = -1
_TIMESTAMP = _datetime_to_pb_timestamp(datetime.now())

# Protocol buffers
# ----------------


def build_commit_response_pb(**kwargs) -> CommitResponsePB:
    """Builds and returns a commit response protocol buffer for testing using the given arguments.
    If an expected argument is not provided, a default value will be used."""

    if "commit_timestamp" not in kwargs:
        kwargs["commit_timestamp"] = _TIMESTAMP

    return CommitResponsePB(**kwargs)


def build_precommit_token_pb(**kwargs) -> PrecommitTokenPB:
    """Builds and returns a multiplexed session precommit token protocol buffer for
    testing using the given arguments. If an expected argument is not provided, a
    default value will be used."""

    if "precommit_token" not in kwargs:
        kwargs["precommit_token"] = _PRECOMMIT_TOKEN

    if "seq_num" not in kwargs:
        kwargs["seq_num"] = _SEQUENCE_NUMBER

    return PrecommitTokenPB(**kwargs)


def build_session_pb(**kwargs) -> SessionPB:
    """Builds and returns a session protocol buffer for testing using the given arguments.
    If an expected argument is not provided, a default value will be used."""

    if "name" not in kwargs:
        kwargs["name"] = _SESSION_NAME

    return SessionPB(**kwargs)


def build_transaction_pb(**kwargs) -> TransactionPB:
    """Builds and returns a transaction protocol buffer for testing using the given arguments..
    If an expected argument is not provided, a default value will be used."""

    if "id" not in kwargs:
        kwargs["id"] = _TRANSACTION_ID

    return TransactionPB(**kwargs)


# Client classes
# --------------


def _is_async_test_caller():
    # Check if the caller is in an async test directory
    for frame in inspect.stack():
        module = inspect.getmodule(frame[0])
        if module:
            filename = getattr(module, "__file__", "")
            if filename and "tests/unit/_async" in filename:
                return True
            if "_async" in module.__name__:
                return True
    return False


def build_client(**kwargs: Mapping) -> Client:
    """Builds and returns a client for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    if "project" not in kwargs:
        kwargs["project"] = _PROJECT_ID

    if "credentials" not in kwargs:
        kwargs["credentials"] = build_scoped_credentials()

    is_async = CrossSync.is_async
    if is_async and not _is_async_test_caller():
        is_async = False

    cls = AsyncClient if is_async else Client
    return cls(**kwargs)


def build_connection(**kwargs: Mapping) -> Connection:
    """Builds and returns a connection for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    if "instance" not in kwargs:
        kwargs["instance"] = build_instance()

    if "database" not in kwargs:
        kwargs["database"] = build_database(instance=kwargs["instance"])

    return Connection(**kwargs)


def build_database(**kwargs: Mapping) -> Database:
    """Builds and returns a database for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    if "database_id" not in kwargs:
        kwargs["database_id"] = _DATABASE_ID

    if "logger" not in kwargs:
        kwargs["logger"] = build_logger()

    if "instance" not in kwargs:
        kwargs["instance"] = build_instance()

    is_async = CrossSync.is_async
    if is_async and not _is_async_test_caller():
        is_async = False

    cls = AsyncDatabase if is_async else Database
    database = cls(**kwargs)
    database._spanner_api = build_spanner_api()

    if not is_async:
        database._pool.bind(database)

    return database


def build_instance(**kwargs: Mapping) -> Instance:
    """Builds and returns an instance for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    if "instance_id" not in kwargs:
        kwargs["instance_id"] = _INSTANCE_ID

    if "client" not in kwargs:
        kwargs["client"] = build_client()

    is_async = CrossSync.is_async
    if is_async and not _is_async_test_caller():
        is_async = False

    cls = AsyncInstance if is_async else Instance
    return cls(**kwargs)


def build_session(**kwargs: Mapping) -> Session:
    """Builds and returns a session for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    if "database" not in kwargs:
        kwargs["database"] = build_database()

    is_async = CrossSync.is_async
    if is_async and not _is_async_test_caller():
        is_async = False

    cls = AsyncSession if is_async else Session
    return cls(**kwargs)


def build_snapshot(**kwargs):
    """Builds and returns a snapshot for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    session = kwargs.pop("session", build_session())

    # Ensure session exists.
    if session.session_id is None:
        session._session_id = _SESSION_ID

    return session.snapshot(**kwargs)


def build_transaction(session=None) -> Transaction:
    """Builds and returns a transaction for testing using the given arguments.
    If a required argument is not provided, a default value will be used."""

    session = session or build_session()

    # Ensure session exists.
    if session.session_id is None:
        session._session_id = _SESSION_ID

    return session.transaction()


# Other classes
# -------------


def build_logger() -> Logger:
    """Builds and returns a logger for testing."""

    return create_autospec(Logger, instance=True)


def build_scoped_credentials() -> Credentials:
    """Builds and returns a mock scoped credentials for testing."""

    class _ScopedCredentials(Credentials, Scoped):
        pass

    return create_autospec(spec=_ScopedCredentials, instance=True)


def build_spanner_api() -> SpannerClient:
    """Builds and returns a mock Spanner Client API for testing using the given arguments.
    Commonly used methods are mocked to return default values."""

    is_async = CrossSync.is_async
    if is_async and not _is_async_test_caller():
        is_async = False

    cls = SpannerAsyncClient if is_async else SpannerClient
    api = create_autospec(cls, instance=True)

    # Mock API calls with default return values.
    api.begin_transaction.return_value = build_transaction_pb()
    api.commit.return_value = build_commit_response_pb()
    api.create_session.return_value = build_session_pb()

    return api
