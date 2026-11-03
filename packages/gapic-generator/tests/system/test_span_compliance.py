# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Telemetry Semantic Compliance Verification Suite.

This module implements a spec-driven, matrix-governed verification engine for OpenTelemetry
tracing across Google Cloud Client Libraries (GAPIC), evaluated live against the GAPIC Showcase daemon.

Architectural Overview:
-----------------------
Rather than hardcoding dozens of repetitive test functions with fragile assertions, this suite
operates as a data-driven test engine governed by a Single Source of Truth (SSOT):
`telemetry_requirements_matrix.csv`.

The matrix adheres strictly to Tidy Data guidelines:
- Each row defines a single test evaluating a single target span (identified by `Tier` and `Attempt`).
- Each column holds a single atomic variable (no multi-tier or multi-attempt cell grammars).

The engine operates across five distinct phases:

1. Specification Matrix (`telemetry_requirements_matrix.csv`):
   Defines the contract for observability test rows across transports (gRPC, REST),
   span tiers (T3 Logical Client vs. T4 Wire Attempt), attempt indices, error scenarios, and retries.

2. Scenario Execution & Span Capture (`execute_scenario`):
   Instantiates isolated Showcase clients configured with in-memory OpenTelemetry tracer
   providers and dispatches live requests (unary echo calls, stateful multi-step retry sequences)
   against the Showcase test daemon.

3. Hierarchy Classification:
   Partitions captured finished spans by parentage:
   - Root Spans (parent is None): Represents the outer logical RPC call (T3 Tier).
   - Child Spans (parent is not None): Represents physical wire attempts (T4 Tier).
   Selects the span under test using the row's `Tier` and `Attempt` index.

4. Validators (`assert_span_matches_row`):
   Validates each cell against the target span, checking:
   span names, kinds, status codes, string attributes (with wildcard prefix support),
   integer attributes, substring status messages, resend counts, and parent-child span linkage.

5. Diagnostic Archival (`RAW_SPANS_CATALOG` & `dump_raw_spans` fixture):
   Serializes every captured span in full JSON format to `raw_spans_output.json`, enabling
   offline auditability and regression post-mortems without re-running the live server.
"""

from __future__ import annotations

import contextlib
import csv
import json
import time
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any

import pytest

try:
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )

    HAS_OPENTELEMETRY = True
except ImportError:
    HAS_OPENTELEMETRY = False

if not HAS_OPENTELEMETRY:
    pytest.skip("OpenTelemetry is not installed", allow_module_level=True)

try:
    from google.api_core import _observability

    HAS_TIER3_TRACING = hasattr(_observability, "_TraceContext")
except ImportError:
    HAS_TIER3_TRACING = False

if not HAS_TIER3_TRACING:
    pytest.skip(
        "Installed google-api-core lacks Tier 3 OpenTelemetry tracing",
        allow_module_level=True,
    )

import requests.exceptions
from google import showcase
from google.api_core import exceptions
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.protobuf import duration_pb2
from google.rpc import code_pb2, status_pb2
from google.showcase import (
    AttemptSequenceRequest,
    CreateSequenceRequest,
    EchoClient,
    Sequence,
    SequenceServiceClient,
)

try:
    from . import conftest
except (ImportError, ValueError):
    import conftest


# ---------------------------------------------------------------------------
# Test Harness Performance & Tuning Knobs
# ---------------------------------------------------------------------------
# These constants govern execution timing and timeout budgets during test runs.
# They are intentionally separated from the telemetry specification itself:
# while production defaults use exponential backoffs and multi-second retry windows,
# test scenarios require ultra-fast, deterministic execution to keep the CI suite snappy
# without flaking under high concurrency.
# Use a negative deadline (-1.0s) for gRPC so C-core immediately expires the call
# locally with DEADLINE_EXCEEDED without writing a near-zero `grpc-timeout` header
# to the wire (which can race with the Go Showcase server sending HTTP/2 RST_STREAM CANCEL).
GRPC_CLIENT_TIMEOUT_SECONDS = -1.0
REST_CLIENT_TIMEOUT_SECONDS = 0.2
CLIENT_TIMEOUT_SECONDS = {
    "grpc": GRPC_CLIENT_TIMEOUT_SECONDS,
    "rest": REST_CLIENT_TIMEOUT_SECONDS,
}
SERVER_BLOCK_DELAY_SECONDS = 2
FAST_RETRY_BACKOFF_SECONDS = 0.01
# Setting multiplier to 1.0 enforces constant/linear polling intervals, bypassing
# exponential backoff delay calculation during retry loops:
CONSTANT_BACKOFF_MULTIPLIER = 1.0
EXHAUSTION_DEADLINE_SECONDS = 0.1
GENEROUS_RECOVERY_DEADLINE_SECONDS = 5.0
# Deterministic number of wire attempts executed for retry exhaustion scenarios:
EXHAUSTED_RETRY_ATTEMPTS = 2


# ---------------------------------------------------------------------------
# CSV Matrix Loader & Diagnostic Archival
# ---------------------------------------------------------------------------

CSV_PATH = Path(__file__).parent / "telemetry_requirements_matrix.csv"


def load_feature_matrix() -> dict[str, dict[str, str]]:
    """Loads and indexes the Single Source of Truth CSV requirements matrix.

    Returns:
        A dictionary mapping Feature ID (e.g. 'F1.2', 'F3.1b') to its dictionary
        of column names and string specifications.
    """
    with open(CSV_PATH, mode="r", encoding="utf-8") as f:
        return {r["Feature ID"]: r for r in csv.DictReader(f)}


FEATURE_MATRIX = load_feature_matrix()
RAW_SPANS_CATALOG: dict[str, Any] = {}


# ---------------------------------------------------------------------------
# Test Fixture
# ---------------------------------------------------------------------------


@pytest.fixture
def span_exporter(monkeypatch):
    """Provides an isolated OpenTelemetry in-memory span exporter and provider.

    Lifecycle:
        1. Instantiates an InMemorySpanExporter coupled to a SimpleSpanProcessor.
        2. Sets the SDK tracing feature flag ('GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED=true')
           via pytest's monkeypatch fixture to guarantee process-level isolation without
           polluting global environment state.
        3. Yields the (exporter, provider) pair to the test body.
        4. Clears all buffered spans on teardown to prevent state leakage between tests.

    Args:
        monkeypatch: Pytest fixture for thread-safe environment variable management.

    Yields:
        tuple[InMemorySpanExporter, TracerProvider]: The span collector and provider.
    """
    exporter = InMemorySpanExporter()
    provider = TracerProvider()
    provider.add_span_processor(SimpleSpanProcessor(exporter))
    monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "true")

    yield exporter, provider
    exporter.clear()


# ---------------------------------------------------------------------------
# RPC Invocation Runners & Client Construction
# ---------------------------------------------------------------------------


def construct_observability_client(
    client_class,
    transport: str,
    client_options: ClientOptions | None = None,
    use_mtls: bool = False,
):
    """Factory helper to instantiate GAPIC Showcase clients with test harness defaults.

    This function encapsulates client instantiation by supplying `use_mtls=False`
    by default (the standard for local Showcase daemon testing) while forwarding
    transport configuration and OpenTelemetry client_options.

    Design Note:
        Rather than modifying the shared system test fixture helper (`conftest.construct_client`),
        wrapping it locally insulates this compliance suite with zero blast radius on existing
        Showcase tests.

    Args:
        client_class: The GAPIC client class to instantiate (e.g. EchoClient).
        transport: Target transport name ('grpc' or 'rest').
        client_options: Optional ClientOptions containing the TracerProvider.
        use_mtls: Whether to enable mTLS (defaults to False).

    Returns:
        An instantiated, ready-to-call Showcase client instance.
    """
    return conftest.construct_client(
        client_class,
        use_mtls=use_mtls,
        transport_name=transport,
        client_options=client_options,
    )


def run_echo_call(client: EchoClient, scenario: str, transport: str) -> None:
    """Executes unary RPC requests against an injected EchoClient.

    This runner exercises the three standard unary RPC lifecycle scenarios:
    - 'Happy Path' / 'Tracing Off': Dispatches a successful unary EchoRequest.
    - 'Server Failure': Injects a non-retryable INVALID_ARGUMENT gRPC status on the
      Showcase server, expecting an immediate InvalidArgument or BadRequest exception.
    - 'Client Timeout': Enforces a transport-appropriate client-side timeout
      (`CLIENT_TIMEOUT_SECONDS[transport]`) with retries disabled, expecting a
      DeadlineExceeded or Timeout exception.

    Args:
        client: The instantiated EchoClient (injected by `execute_scenario`).
        scenario: The scenario name string from the CSV matrix row.
        transport: Normalized transport string ('grpc' or 'rest') derived from the CSV matrix row.
    """
    if scenario in ("Happy Path", "Tracing Off"):
        client.echo(showcase.EchoRequest(content="hello"))
    elif scenario == "Server Failure":
        with pytest.raises((exceptions.InvalidArgument, exceptions.BadRequest)):
            client.echo(
                showcase.EchoRequest(
                    error=status_pb2.Status(
                        code=code_pb2.INVALID_ARGUMENT,
                        message="Simulated unretryable invalid argument error.",
                    )
                )
            )
    elif scenario == "Client Timeout":
        with pytest.raises(
            (
                exceptions.DeadlineExceeded,
                requests.exceptions.Timeout,
            )
        ):
            client.block(
                showcase.BlockRequest(
                    response_delay=duration_pb2.Duration(
                        seconds=SERVER_BLOCK_DELAY_SECONDS
                    ),
                ),
                timeout=CLIENT_TIMEOUT_SECONDS[transport],
                retry=None,
            )


def run_sequence_retry_call(
    client: SequenceServiceClient,
    scenario: str,
    exporter: InMemorySpanExporter,
):
    """Executes stateful retry sequence requests against an injected SequenceServiceClient.

    The Showcase SequenceService allows configuring a server-side queue of pre-programmed
    responses that return sequentially across consecutive attempt RPCs.

    Execution Flow:
    1. Pre-programs a deterministic 2-response sequence queue via `create_sequence`:
       - 'Retries Exhausted': Configures 2 UNAVAILABLE ('Persistent outage') responses
         and an `on_error` hook that sleeps past `EXHAUSTION_DEADLINE_SECONDS` upon the
         2nd failure, guaranteeing that `Retry` genuinely raises `exceptions.RetryError`
         (`RetryFailureReason.TIMEOUT`) after exactly 2 wire attempts.
       - 'Retry Recovery': Configures 1 UNAVAILABLE ('Temporary glitch') response
         followed by 1 OK response, guaranteeing 2 wire attempts that recover.
    2. Flushes the in-memory span exporter (`exporter.clear()`).
       CRITICAL: The `create_sequence` setup call emits its own OpenTelemetry spans!
       Purging the exporter ensures that downstream assertions strictly evaluate spans emitted
       by the target `attempt_sequence` call.
    3. Invokes `attempt_sequence` with a fast Retry policy.

    Args:
        client: The instantiated SequenceServiceClient (injected by `execute_scenario`).
        scenario: The scenario name string from the CSV matrix row.
        exporter: The active span exporter used to purge pre-flight setup spans.
    """
    is_exhaust = scenario == "Retries Exhausted"

    if is_exhaust:
        responses = [
            Sequence.Response(
                status=status_pb2.Status(
                    code=code_pb2.UNAVAILABLE,
                    message="Persistent outage",
                )
            )
        ] * EXHAUSTED_RETRY_ATTEMPTS
        attempts_seen = 0

        def on_error(_exc: Exception) -> None:
            nonlocal attempts_seen
            attempts_seen += 1
            if attempts_seen >= EXHAUSTED_RETRY_ATTEMPTS:
                time.sleep(EXHAUSTION_DEADLINE_SECONDS)

        deadline = EXHAUSTION_DEADLINE_SECONDS
        expectation = pytest.raises(exceptions.RetryError)
    else:
        responses = [
            Sequence.Response(
                status=status_pb2.Status(
                    code=code_pb2.UNAVAILABLE,
                    message="Temporary glitch",
                )
            ),
            Sequence.Response(status=status_pb2.Status(code=code_pb2.OK)),
        ]
        on_error = None
        deadline = GENEROUS_RECOVERY_DEADLINE_SECONDS
        expectation = contextlib.nullcontext()

    # Step 1: Pre-program response sequence on the Showcase daemon
    seq = client.create_sequence(
        CreateSequenceRequest(sequence=Sequence(responses=responses))
    )

    # Step 2: Flush setup RPC spans so assertions evaluate only attempt_sequence
    exporter.clear()

    # Step 3: Configure fast retry policy and execute sequence attempts
    retry_policy = retries.Retry(
        predicate=retries.if_exception_type(exceptions.ServiceUnavailable),
        initial=FAST_RETRY_BACKOFF_SECONDS,
        maximum=FAST_RETRY_BACKOFF_SECONDS,
        multiplier=CONSTANT_BACKOFF_MULTIPLIER,
        deadline=deadline,
        on_error=on_error,
    )

    with expectation:
        client.attempt_sequence(
            AttemptSequenceRequest(name=seq.name),
            retry=retry_policy,
        )


def execute_scenario(
    scenario: str,
    transport_str: str,
    provider: TracerProvider,
    exporter: InMemorySpanExporter,
    monkeypatch: pytest.MonkeyPatch,
):
    """High-level scenario dispatcher and Dependency Injection (DI) coordinator.

    Responsibilities:
    1. Normalizes transport strings ('grpc' vs 'rest').
    2. Injects the TracerProvider into `ClientOptions` (or unsets it for 'Tracing Off').
    3. Handles scenario-specific environment configuration via `monkeypatch`.
    4. Instantiates the appropriate client class (`EchoClient` vs `SequenceServiceClient`).
    5. Dispatches execution to the corresponding runner (`run_echo_call` or `run_sequence_retry_call`).

    Args:
        scenario: The scenario column value from the CSV matrix row.
        transport_str: The transport column value ('gRPC' or 'HTTP/REST').
        provider: The active OpenTelemetry TracerProvider.
        exporter: The active InMemorySpanExporter.
        monkeypatch: Pytest monkeypatch fixture for environment variable scoping.
    """
    transport = "grpc" if "grpc" in transport_str.lower() else "rest"
    client_options = ClientOptions(tracer_provider=provider)

    if scenario == "Tracing Off":
        monkeypatch.setenv("GOOGLE_SDK_EXPERIMENTAL_PYTHON_TRACING_ENABLED", "false")
        client_options = ClientOptions()

    if scenario in ("Happy Path", "Server Failure", "Client Timeout", "Tracing Off"):
        client = construct_observability_client(EchoClient, transport, client_options)
        run_echo_call(client, scenario, transport)
    else:
        client = construct_observability_client(
            SequenceServiceClient, transport, client_options
        )
        run_sequence_retry_call(client, scenario, exporter)


# ---------------------------------------------------------------------------
# Validators & Assertion Engine
# ---------------------------------------------------------------------------

# OpenTelemetry attributes validated as strings
STRING_ATTRIBUTES = [
    "rpc.system.name",
    "rpc.method",
    "rpc.response.status_code",
    "http.request.method",
    "url.domain",
    "url.template",
    "server.address",
    "error.type",
]

# OpenTelemetry attributes validated as exact integer types
INTEGER_ATTRIBUTES = [
    "http.response.status_code",
    "rpc.grpc.status_code",
    "server.port",
]


def _clean_cell(raw_val: str | None) -> str:
    """Normalizes a raw CSV cell string into a trimmed value or 'N/A'."""
    if raw_val is None:
        return "N/A"
    cleaned = raw_val.strip()
    return cleaned if cleaned else "N/A"


def _match_int(attr: str, actual: Any, expected: str):
    """Validates that an attribute matches the expected integer value."""
    assert actual == int(expected), (
        f"Attribute {attr}: expected {expected}, got {actual}"
    )


def _assert_attribute(
    span,
    attr: str,
    raw_expected: str | None,
    comparator=None,
):
    """Universal triage helper for single-attribute validation against a matrix cell.

    This helper standardizes attribute verification across all sub-validators:
    - 'N/A': Skips assertion (attribute is irrelevant or not applicable to this scenario).
    - 'NOT SET': Enforces negative assertion, verifying the key is completely absent
      from `span.attributes`.
    - Present values: Asserts presence, then applies either a custom comparator callback
      (e.g. for wildcard prefixes or integer parsing) or default strict equality.

    Args:
        span: The OpenTelemetry ReadableSpan instance being evaluated.
        attr: The attribute name key (e.g. 'rpc.system.name').
        raw_expected: The raw string value from the CSV row cell.
        comparator: Optional callable `comparator(attr, actual, expected)` for custom validation.
    """
    expected = _clean_cell(raw_expected)
    if expected == "N/A":
        return

    if expected == "NOT SET":
        assert attr not in span.attributes, (
            f"Attribute {attr} should NOT be set, found: {span.attributes.get(attr)}"
        )
        return

    actual = span.attributes.get(attr)
    assert actual is not None, f"Attribute {attr} missing, expected '{expected}'"

    if comparator:
        comparator(attr, actual, expected)
    else:
        assert actual == expected, (
            f"Attribute {attr}: expected '{expected}', got '{actual}'"
        )


def _assert_span_metadata(span, row: dict[str, str]):
    """Validates top-level span header fields (Name, Kind, and Status Code).

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
    """
    metadata_fields = (
        ("Span Name", span.name, "Span name"),
        ("Span Kind", span.kind.name, "Span kind"),
        ("Span Status", span.status.status_code.name, "Span status"),
    )
    for col, actual, label in metadata_fields:
        expected = _clean_cell(row.get(col))
        if expected != "N/A":
            assert actual == expected, (
                f"{label} mismatch: expected '{expected}', got '{actual}'"
            )


def _assert_string_attributes(span, row: dict[str, str]):
    """Validates string OpenTelemetry attributes with wildcard prefix support.

    Supports wildcard templates in the matrix (e.g. 'http://localhost:7469/v1beta1/echo:echo/*')
    by checking `startswith` when an expected value ends with '/*'.

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
    """

    def _match_string(attr: str, actual: Any, expected: str):
        if expected.endswith("/*"):
            prefix = expected[:-1]
            assert str(actual).startswith(prefix), (
                f"Attribute {attr}: expected prefix '{prefix}', got '{actual}'"
            )
        else:
            assert actual == expected, (
                f"Attribute {attr}: expected '{expected}', got '{actual}'"
            )

    for attr in STRING_ATTRIBUTES:
        _assert_attribute(
            span,
            attr,
            row.get(attr),
            comparator=_match_string,
        )


def _assert_integer_attributes(span, row: dict[str, str]):
    """Validates integer OpenTelemetry attributes (e.g. status codes, ports).

    Enforces strict integer type conversion to prevent false positives where string
    values might accidentally pass comparison.

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
    """
    for attr in INTEGER_ATTRIBUTES:
        _assert_attribute(
            span,
            attr,
            row.get(attr),
            comparator=_match_int,
        )


def _assert_status_message(span, row: dict[str, str]):
    """Validates status.message via exact string equality.

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
    """

    def _match_message(attr: str, actual: Any, expected: str):
        assert str(actual) == expected, (
            f"Attribute {attr}: expected '{expected}', got '{actual}'"
        )

    _assert_attribute(
        span,
        "status.message",
        row.get("status.message"),
        comparator=_match_message,
    )


def _assert_resend_count(span, row: dict[str, str]):
    """Validates retry resend counts across HTTP and gRPC attribute variations.

    Protocol Discrepancies Handled:
    - HTTP / REST spans record resend counts under `http.request.resend_count`.
    - gRPC spans record resend counts under `gcp.grpc.resend_count`.

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
    """
    attr = (
        "gcp.grpc.resend_count"
        if "grpc" in row["Transport"].lower()
        else "http.request.resend_count"
    )
    _assert_attribute(span, attr, row.get("resend_count"), comparator=_match_int)


def _assert_parent_span_id(span, row: dict[str, str], t3_spans: list[Any]):
    """Validates span parentage against the `parent_span_id` column.

    Supported Values:
    - 'None (Root)': Verifies the span is a root span (`span.parent is None`).
    - 'T3.span_id': Verifies the child span links directly to the captured T3 root span ID.

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
        t3_spans: List of captured root (T3) spans in the current trace.
    """
    expected_parent = _clean_cell(row.get("parent_span_id"))
    if expected_parent == "None (Root)":
        assert span.parent is None, (
            f"Expected root span (parent=None), got parent={span.parent}"
        )
    elif expected_parent == "T3.span_id":
        assert len(t3_spans) == 1, (
            f"Expected 1 T3 root span for parent linkage check, got {len(t3_spans)}"
        )
        assert span.parent is not None, "Expected child span to have a parent"
        assert span.parent.span_id == t3_spans[0].context.span_id, (
            f"Parent span_id mismatch: expected {t3_spans[0].context.span_id}, "
            f"got {span.parent.span_id}"
        )
    elif expected_parent != "N/A":
        pytest.fail(f"Unsupported parent_span_id value in matrix: {expected_parent!r}")


def _assert_t3_t4_inheritance(span, row: Mapping[str, str], t4_spans: Sequence[Any]):
    """Validates cross-tier attribute inheritance from child T4 spans to the parent T3 span.

    Enforces Test Plan requirements:
    - `url.template` on HTTP T3 is populated from the first T4 span (`T4_1`).
    - `http.response.status_code`, `error.type`, and `status.message` on HTTP T3 are
      consistent with / inherited from the last T4 span when present on that T4 span.

    Args:
        span: The OpenTelemetry ReadableSpan being validated.
        row: The CSV requirements dictionary for this feature.
        t4_spans: List of captured child (T4) spans in the current trace.
    """
    if row.get("Tier") != "T3" or not t4_spans:
        return

    first_t4 = t4_spans[0]
    if "url.template" in first_t4.attributes:
        assert span.attributes.get("url.template") == first_t4.attributes.get(
            "url.template"
        ), (
            "T3 url.template must be inherited from the first T4 span: T3="
            f"{span.attributes.get('url.template')!r} != "
            f"T4_1={first_t4.attributes.get('url.template')!r}"
        )

    last_t4 = t4_spans[-1]
    for inherited_attr in ("http.response.status_code", "error.type", "status.message"):
        if inherited_attr in last_t4.attributes:
            assert span.attributes.get(inherited_attr) == last_t4.attributes.get(
                inherited_attr
            ), (
                f"T3 {inherited_attr} must match the last T4 span: T3="
                f"{span.attributes.get(inherited_attr)!r} != "
                f"T4_last={last_t4.attributes.get(inherited_attr)!r}"
            )


def assert_span_matches_row(
    span,
    row: Mapping[str, str],
    t3_spans: Sequence[Any],
    t4_spans: Sequence[Any] | None = None,
):
    """Master validator delegating single-span verification across specialized sub-validators.

    Coordinates verification of:
    1. Top-level Span Metadata (Name, Kind, Status)
    2. String Attributes (System, Method, URL, Error Type)
    3. Integer Attributes (HTTP / gRPC Status Codes, Port)
    4. Status Error Message (Exact string equality)
    5. Retry Resend Count (Protocol-aware retry progression)
    6. Parent Span ID Hierarchy Invariant
    7. Cross-tier T3/T4 Attribute Inheritance

    Args:
        span: The OpenTelemetry ReadableSpan instance being checked.
        row: The CSV requirements dictionary for this feature.
        t3_spans: Captured T3 root spans used to validate parent-child linkage.
        t4_spans: Captured T4 child spans used to validate cross-tier inheritance.
    """
    _assert_span_metadata(span, row)
    _assert_string_attributes(span, row)
    _assert_integer_attributes(span, row)
    _assert_status_message(span, row)
    _assert_resend_count(span, row)
    _assert_parent_span_id(span, row, t3_spans)
    if t4_spans is not None:
        _assert_t3_t4_inheritance(span, row, t4_spans)


# ---------------------------------------------------------------------------
# Parametrized Test Runner (Tidy Matrix: 1 Row = 1 Span Assertion)
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("feature_id", "row"),
    [
        pytest.param(
            fid,
            row,
            id=f"{fid}_{row['Feature Name'].replace(' ', '_')}",
        )
        for fid, row in FEATURE_MATRIX.items()
    ],
)
def test_feature(feature_id: str, row: dict[str, str], span_exporter, monkeypatch):
    """Executes a single observability scenario and validates its target span against a tidy matrix row.

    Test Lifecycle:
    ---------------
    1. Execute Scenario:
       Invokes `execute_scenario` to dispatch unary or retry requests to the live Showcase server.
    2. Capture Spans:
       Retrieves all finished spans from the in-memory exporter and archives them into
       `RAW_SPANS_CATALOG` for diagnostic output.
    3. Handle 'Tracing Off':
       If the row specifies 'Span Count = 0', asserts that zero spans were produced.
    4. Span Partitioning & Target Selection:
       Partitions captured spans into root spans (`parent is None`, representing T3)
       and child spans (`parent is not None`, representing T4), verifies the expected
       tier span count, and selects the single target span at `Attempt`.
    5. Evaluate Target Span:
       Validates the target span's metadata, attributes, and parentage against the row.

    Args:
        feature_id: Unique matrix identifier (e.g. 'F1.2', 'F3.1b').
        row: The CSV requirements dictionary for this feature.
        span_exporter: Isolated test fixture yielding (exporter, provider).
        monkeypatch: Pytest environment variable isolation fixture.
    """
    exporter, provider = span_exporter

    # Phase 1: Execute physical scenario against Showcase daemon
    execute_scenario(row["Scenario"], row["Transport"], provider, exporter, monkeypatch)
    spans = exporter.get_finished_spans()

    # Phase 2: Archive raw spans in memory for end-of-session JSON diagnostic dump
    RAW_SPANS_CATALOG[feature_id] = [json.loads(s.to_json()) for s in spans]

    # Phase 3: Verify Tracing Off scenarios emit zero telemetry
    expected_count = int(row["Span Count"])
    if expected_count == 0:
        assert len(spans) == 0, f"Expected 0 spans for {feature_id}, found {len(spans)}"
        return

    # Phase 4: Partition captured spans into Root (T3) and Child (T4) attempts
    t3_spans = [s for s in spans if s.parent is None]
    t4_spans = [s for s in spans if s.parent is not None]

    tier = row["Tier"]
    assert tier in ("T3", "T4"), f"Unsupported Tier {tier!r} for {feature_id}"
    tier_spans = t3_spans if tier == "T3" else t4_spans
    assert len(tier_spans) == expected_count, (
        f"Expected {expected_count} {tier} spans for {feature_id}, got {len(tier_spans)}"
    )

    # Phase 5: Select the target span by Attempt index and validate all columns
    attempt_idx = int(row["Attempt"])
    assert 0 <= attempt_idx < len(tier_spans), (
        f"Attempt index {attempt_idx} out of bounds for {feature_id} "
        f"(captured {len(tier_spans)} {tier} spans)"
    )
    target_span = tier_spans[attempt_idx]
    with conftest.skip_on_core_mismatch():
        assert_span_matches_row(target_span, row, t3_spans, t4_spans)


# ---------------------------------------------------------------------------
# Session Teardown: Raw Spans Archival
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session", autouse=True)
def dump_raw_spans():
    """Serializes all captured raw spans to raw_spans_output.json upon session completion.

    This autouse session fixture runs after all tests complete, writing an immutable
    diagnostic artifact showing every span's exact attributes, timing, and hierarchy
    ready for upload by CI.
    """
    yield
    if RAW_SPANS_CATALOG:
        output_path = Path(__file__).parent / "raw_spans_output.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(RAW_SPANS_CATALOG, f, indent=2)
