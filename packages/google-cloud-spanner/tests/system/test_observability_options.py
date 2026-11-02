# Copyright 2024 Google LLC All rights reserved.
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

import pytest
from google.api_core.exceptions import Aborted
from google.auth.credentials import AnonymousCredentials
from google.rpc import code_pb2
from mock import PropertyMock, patch

from google.cloud.spanner_v1 import Client
from google.cloud.spanner_v1.database_sessions_manager import TransactionType
from google.cloud.spanner_v1.session import Session

from .._helpers import is_multiplexed_enabled
from . import _helpers

HAS_OTEL_INSTALLED = False

try:
    from opentelemetry import trace
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )
    from opentelemetry.sdk.trace.sampling import ALWAYS_ON

    HAS_OTEL_INSTALLED = True
except ImportError:
    pass


@pytest.mark.skipif(
    not HAS_OTEL_INSTALLED, reason="OpenTelemetry is necessary to test traces."
)
@pytest.mark.skipif(
    not _helpers.USE_EMULATOR, reason="Emulator is necessary to test traces."
)
def test_observability_options_propagation():
    PROJECT = _helpers.EMULATOR_PROJECT
    CONFIGURATION_NAME = "config-name"
    INSTANCE_ID = _helpers.INSTANCE_ID
    DISPLAY_NAME = "display-name"
    DATABASE_ID = _helpers.unique_id("temp_db")
    NODE_COUNT = 5
    LABELS = {"test": "true"}

    def test_propagation(enable_extended_tracing):
        global_tracer_provider = TracerProvider(sampler=ALWAYS_ON)
        trace.set_tracer_provider(global_tracer_provider)
        global_trace_exporter = InMemorySpanExporter()
        global_tracer_provider.add_span_processor(
            SimpleSpanProcessor(global_trace_exporter)
        )

        inject_tracer_provider = TracerProvider(sampler=ALWAYS_ON)
        inject_trace_exporter = InMemorySpanExporter()
        inject_tracer_provider.add_span_processor(
            SimpleSpanProcessor(inject_trace_exporter)
        )
        observability_options = dict(
            tracer_provider=inject_tracer_provider,
            enable_extended_tracing=enable_extended_tracing,
        )
        client = Client(
            project=PROJECT,
            observability_options=observability_options,
            credentials=_make_credentials(),
        )

        instance = client.instance(
            INSTANCE_ID,
            CONFIGURATION_NAME,
            display_name=DISPLAY_NAME,
            node_count=NODE_COUNT,
            labels=LABELS,
        )

        try:
            instance.create()
        except Exception:
            pass

        db = instance.database(DATABASE_ID)
        try:
            db.create()
        except Exception:
            pass

        assert db.observability_options == observability_options
        with db.snapshot() as snapshot:
            res = snapshot.execute_sql("SELECT 1")
            for val in res:
                _ = val

        from_global_spans = global_trace_exporter.get_finished_spans()
        target_spans = inject_trace_exporter.get_finished_spans()
        from_inject_spans = sorted(target_spans, key=lambda v1: v1.start_time)
        assert (
            len(from_global_spans) == 0
        )  # "Expecting no spans from the global trace exporter"
        assert (
            len(from_inject_spans) >= 2
        )  # "Expecting at least 2 spans from the injected trace exporter"
        gotNames = [span.name for span in from_inject_spans]

        # Check if multiplexed sessions are enabled
        multiplexed_enabled = is_multiplexed_enabled(TransactionType.READ_ONLY)

        # Determine expected session span name based on multiplexed sessions
        expected_session_span_name = (
            "CloudSpanner.CreateMultiplexedSession"
            if multiplexed_enabled
            else "CloudSpanner.CreateSession"
        )

        wantNames = [
            expected_session_span_name,
            "CloudSpanner.Snapshot.execute_sql",
        ]
        assert gotNames == wantNames

        # Check for conformance of enable_extended_tracing
        lastSpan = from_inject_spans[len(from_inject_spans) - 1]
        wantAnnotatedSQL = "SELECT 1"
        if not enable_extended_tracing:
            wantAnnotatedSQL = None
        assert (
            lastSpan.attributes.get("db.statement", None) == wantAnnotatedSQL
        )  # "Mismatch in annotated sql"

        try:
            db.delete()
            instance.delete()
        except Exception:
            pass

    # Test the respective options for enable_extended_tracing
    test_propagation(True)
    test_propagation(False)


def create_db_trace_exporter():
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )
    from opentelemetry.sdk.trace.sampling import ALWAYS_ON

    PROJECT = _helpers.EMULATOR_PROJECT
    CONFIGURATION_NAME = "config-name"
    INSTANCE_ID = _helpers.INSTANCE_ID
    DISPLAY_NAME = "display-name"
    DATABASE_ID = _helpers.unique_id("temp_db")
    NODE_COUNT = 5
    LABELS = {"test": "true"}

    tracer_provider = TracerProvider(sampler=ALWAYS_ON)
    trace_exporter = InMemorySpanExporter()
    tracer_provider.add_span_processor(SimpleSpanProcessor(trace_exporter))
    observability_options = dict(
        tracer_provider=tracer_provider,
        enable_extended_tracing=True,
    )

    client = Client(
        project=PROJECT,
        observability_options=observability_options,
        credentials=AnonymousCredentials(),
    )

    instance = client.instance(
        INSTANCE_ID,
        CONFIGURATION_NAME,
        display_name=DISPLAY_NAME,
        node_count=NODE_COUNT,
        labels=LABELS,
    )

    try:
        instance.create()
    except Exception:
        pass

    db = instance.database(DATABASE_ID)
    try:
        db.create()
    except Exception:
        pass

    return db, trace_exporter


@pytest.mark.skipif(
    not _helpers.USE_EMULATOR,
    reason="Emulator needed to run this test",
)
@pytest.mark.skipif(
    not HAS_OTEL_INSTALLED,
    reason="Tracing requires OpenTelemetry",
)
@patch.object(Session, "session_id", new_callable=PropertyMock)
def test_transaction_abort_then_retry_spans(mock_session_id):
    from opentelemetry.trace.status import StatusCode

    mock_session_id.return_value = session_id = "session-id"
    multiplexed = is_multiplexed_enabled(TransactionType.READ_WRITE)

    db, trace_exporter = create_db_trace_exporter()

    counters = dict(aborted=0)

    def select_in_txn(txn):
        results = txn.execute_sql("SELECT 1")
        for row in results:
            _ = row

        if counters["aborted"] == 0:
            counters["aborted"] = 1
            raise Aborted(
                "Thrown from ClientInterceptor for testing",
                errors=[_helpers.FauxCall(code_pb2.ABORTED)],
            )

    db.run_in_transaction(select_in_txn)

    got_statuses, got_events = finished_spans_statuses(trace_exporter)

    # Check for the series of events
    if multiplexed:
        # With multiplexed sessions, there are no pool-related events
        want_events = [
            ("Creating Session", {}),
            ("Using session", {"id": session_id, "multiplexed": multiplexed}),
            (
                "Transaction was aborted in user operation, retrying",
                {"delay_seconds": "EPHEMERAL", "cause": "EPHEMERAL", "attempt": 1},
            ),
            ("Returning session", {"id": session_id, "multiplexed": multiplexed}),
            ("Starting Commit", {}),
            ("Commit Done", {}),
        ]
    else:
        # With regular sessions, include pool-related events
        want_events = [
            ("Acquiring session", {"kind": "BurstyPool"}),
            ("Waiting for a session to become available", {"kind": "BurstyPool"}),
            ("No sessions available in pool. Creating session", {"kind": "BurstyPool"}),
            ("Creating Session", {}),
            ("Using session", {"id": session_id, "multiplexed": multiplexed}),
            (
                "Transaction was aborted in user operation, retrying",
                {"delay_seconds": "EPHEMERAL", "cause": "EPHEMERAL", "attempt": 1},
            ),
            ("Returning session", {"id": session_id, "multiplexed": multiplexed}),
            ("Starting Commit", {}),
            ("Commit Done", {}),
        ]
    assert got_events == want_events

    # Check for the statues.
    codes = StatusCode
    if multiplexed:
        # With multiplexed sessions, the session span name is different
        want_statuses = [
            ("CloudSpanner.Database.run_in_transaction", codes.OK, None),
            ("CloudSpanner.CreateMultiplexedSession", codes.OK, None),
            ("CloudSpanner.Transaction.execute_sql", codes.OK, None),
            ("CloudSpanner.Transaction.execute_sql", codes.OK, None),
            ("CloudSpanner.Transaction.commit", codes.OK, None),
        ]
    else:
        # With regular sessions
        want_statuses = [
            ("CloudSpanner.Database.run_in_transaction", codes.OK, None),
            ("CloudSpanner.CreateSession", codes.OK, None),
            ("CloudSpanner.Transaction.execute_sql", codes.OK, None),
            ("CloudSpanner.Transaction.execute_sql", codes.OK, None),
            ("CloudSpanner.Transaction.commit", codes.OK, None),
        ]
    assert got_statuses == want_statuses


def finished_spans_statuses(trace_exporter):
    span_list = trace_exporter.get_finished_spans()
    # Sort the spans by their start time in the hierarchy.
    span_list = sorted(span_list, key=lambda span: span.start_time)

    got_events = []
    got_statuses = []

    # Some event attributes are noisy/highly ephemeral
    # and can't be directly compared against.
    imprecise_event_attributes = ["exception.stacktrace", "delay_seconds", "cause"]
    for span in span_list:
        got_statuses.append(
            (span.name, span.status.status_code, span.status.description)
        )

        for event in span.events:
            evt_attributes = event.attributes.copy()
            for attr_name in imprecise_event_attributes:
                if attr_name in evt_attributes:
                    evt_attributes[attr_name] = "EPHEMERAL"

            got_events.append((event.name, evt_attributes))

    return got_statuses, got_events


@pytest.mark.skipif(
    not _helpers.USE_EMULATOR,
    reason="Emulator needed to run this tests",
)
@pytest.mark.skipif(
    not HAS_OTEL_INSTALLED,
    reason="Tracing requires OpenTelemetry",
)
def test_transaction_update_implicit_begin_nested_inside_commit():
    # Tests to ensure that transaction.commit() without a began transaction
    # has transaction.begin() inlined and nested under the commit span.
    from google.auth.credentials import AnonymousCredentials
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )
    from opentelemetry.sdk.trace.sampling import ALWAYS_ON

    PROJECT = _helpers.EMULATOR_PROJECT
    CONFIGURATION_NAME = "config-name"
    INSTANCE_ID = _helpers.INSTANCE_ID
    DISPLAY_NAME = "display-name"
    DATABASE_ID = _helpers.unique_id("temp_db")
    NODE_COUNT = 5
    LABELS = {"test": "true"}

    def tx_update(txn):
        txn.insert(
            "Singers",
            columns=["SingerId", "FirstName"],
            values=[["1", "Bryan"], ["2", "Slash"]],
        )

    tracer_provider = TracerProvider(sampler=ALWAYS_ON)
    trace_exporter = InMemorySpanExporter()
    tracer_provider.add_span_processor(SimpleSpanProcessor(trace_exporter))
    observability_options = dict(
        tracer_provider=tracer_provider,
        enable_extended_tracing=True,
    )

    client = Client(
        project=PROJECT,
        observability_options=observability_options,
        credentials=AnonymousCredentials(),
    )

    instance = client.instance(
        INSTANCE_ID,
        CONFIGURATION_NAME,
        display_name=DISPLAY_NAME,
        node_count=NODE_COUNT,
        labels=LABELS,
    )

    try:
        instance.create()
    except Exception:
        pass

    db = instance.database(DATABASE_ID)
    try:
        db._ddl_statements = [
            """CREATE TABLE Singers (
            SingerId     INT64 NOT NULL,
            FirstName    STRING(1024),
            LastName     STRING(1024),
            SingerInfo   BYTES(MAX),
            FullName   STRING(2048) AS (
                ARRAY_TO_STRING([FirstName, LastName], " ")
            ) STORED
            ) PRIMARY KEY (SingerId)""",
            """CREATE TABLE Albums (
                SingerId     INT64 NOT NULL,
                AlbumId      INT64 NOT NULL,
                AlbumTitle   STRING(MAX),
                MarketingBudget INT64,
            ) PRIMARY KEY (SingerId, AlbumId),
            INTERLEAVE IN PARENT Singers ON DELETE CASCADE""",
        ]
        db.create()
    except Exception:
        pass

    try:
        db.run_in_transaction(tx_update)
    except Exception:
        pass

    span_list = trace_exporter.get_finished_spans()
    # Sort the spans by their start time in the hierarchy.
    span_list = sorted(span_list, key=lambda span: span.start_time)
    got_span_names = [span.name for span in span_list]

    # Check if multiplexed sessions are enabled for read-write transactions
    multiplexed_enabled = is_multiplexed_enabled(TransactionType.READ_WRITE)

    # Determine expected session span name based on multiplexed sessions
    expected_session_span_name = (
        "CloudSpanner.CreateMultiplexedSession"
        if multiplexed_enabled
        else "CloudSpanner.CreateSession"
    )

    want_span_names = [
        "CloudSpanner.Database.run_in_transaction",
        expected_session_span_name,
        "CloudSpanner.Transaction.commit",
        "CloudSpanner.Transaction.begin",
    ]

    assert got_span_names == want_span_names

    # Our object is to ensure that .begin() is a child of .commit()
    span_tx_begin = span_list[-1]
    span_tx_commit = span_list[-2]
    assert span_tx_begin.parent.span_id == span_tx_commit.context.span_id


@pytest.mark.skipif(
    not _helpers.USE_EMULATOR,
    reason="Emulator needed to run this test",
)
@pytest.mark.skipif(
    not HAS_OTEL_INSTALLED,
    reason="Tracing requires OpenTelemetry",
)
def test_database_partitioned_error():
    from opentelemetry.trace.status import StatusCode

    db, trace_exporter = create_db_trace_exporter()

    try:
        db.execute_partitioned_dml("UPDATE NonExistent SET name = 'foo' WHERE id > 1")
    except Exception:
        pass

    got_statuses, got_events = finished_spans_statuses(trace_exporter)
    multiplexed_enabled = is_multiplexed_enabled(TransactionType.PARTITIONED)

    if multiplexed_enabled:
        expected_event_names = [
            "Creating Session",
            "Using session",
            "Starting BeginTransaction",
            "Returning session",
            "exception",
            "exception",
        ]
        assert len(got_events) == len(expected_event_names)
        for i, expected_name in enumerate(expected_event_names):
            assert got_events[i][0] == expected_name

        assert got_events[1][1]["multiplexed"] is True

        assert got_events[3][1]["multiplexed"] is True

        for i in [4, 5]:
            assert (
                got_events[i][1]["exception.type"]
                == "google.api_core.exceptions.InvalidArgument"
            )
            assert (
                "Table not found: NonExistent" in got_events[i][1]["exception.message"]
            )
    else:
        expected_event_names = [
            "Acquiring session",
            "Waiting for a session to become available",
            "No sessions available in pool. Creating session",
            "Creating Session",
            "Using session",
            "Starting BeginTransaction",
            "Returning session",
            "exception",
            "exception",
        ]

        assert len(got_events) == len(expected_event_names)
        for i, expected_name in enumerate(expected_event_names):
            assert got_events[i][0] == expected_name

        assert got_events[0][1]["kind"] == "BurstyPool"
        assert got_events[1][1]["kind"] == "BurstyPool"
        assert got_events[2][1]["kind"] == "BurstyPool"

        assert got_events[4][1]["multiplexed"] is False

        assert got_events[6][1]["multiplexed"] is False

        for i in [7, 8]:
            assert (
                got_events[i][1]["exception.type"]
                == "google.api_core.exceptions.InvalidArgument"
            )
            assert (
                "Table not found: NonExistent" in got_events[i][1]["exception.message"]
            )

    codes = StatusCode

    expected_session_span_name = (
        "CloudSpanner.CreateMultiplexedSession"
        if multiplexed_enabled
        else "CloudSpanner.CreateSession"
    )
    expected_error_prefix = "InvalidArgument: 400 Table not found: NonExistent [at 1:8]\nUPDATE NonExistent SET name = 'foo' WHERE id > 1\n       ^"

    # Check the statuses - error messages may include request_id suffix
    assert len(got_statuses) == 3

    # First status: execute_partitioned_pdml with error
    assert got_statuses[0][0] == "CloudSpanner.Database.execute_partitioned_pdml"
    assert got_statuses[0][1] == codes.ERROR
    assert got_statuses[0][2].startswith(expected_error_prefix)

    # Second status: session creation OK
    assert got_statuses[1] == (expected_session_span_name, codes.OK, None)

    # Third status: ExecuteStreamingSql with error
    assert got_statuses[2][0] == "CloudSpanner.ExecuteStreamingSql"
    assert got_statuses[2][1] == codes.ERROR
    assert got_statuses[2][2].startswith(expected_error_prefix)


def _make_credentials():
    from google.auth.credentials import AnonymousCredentials

    return AnonymousCredentials()
