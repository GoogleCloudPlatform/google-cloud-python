from os import getenv
from unittest import IsolatedAsyncioTestCase

try:
    import mock
except ImportError:
    import unittest.mock as mock

from google.cloud.spanner_v1 import gapic_version
from google.cloud.spanner_v1.database_sessions_manager import TransactionType

LIB_VERSION = gapic_version.__version__

try:
    from opentelemetry import trace
    from opentelemetry.resourcedetector.gcp_resource_detector import (  # noqa: F401
        GoogleCloudResourceDetector,
    )
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import SimpleSpanProcessor
    from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
        InMemorySpanExporter,
    )
    from opentelemetry.sdk.trace.sampling import TraceIdRatioBased
    from opentelemetry.trace.status import StatusCode

    trace.set_tracer_provider(TracerProvider(sampler=TraceIdRatioBased(1.0)))

    HAS_OPENTELEMETRY_INSTALLED = True
except ImportError:
    HAS_OPENTELEMETRY_INSTALLED = False

    StatusCode = mock.Mock()

_TEST_OT_EXPORTER = None
_TEST_OT_PROVIDER_INITIALIZED = False


def is_multiplexed_enabled(transaction_type: TransactionType) -> bool:
    """Returns whether multiplexed sessions are enabled for the given transaction type."""

    env_var = "GOOGLE_CLOUD_SPANNER_MULTIPLEXED_SESSIONS"
    env_var_partitioned = "GOOGLE_CLOUD_SPANNER_MULTIPLEXED_SESSIONS_PARTITIONED_OPS"
    env_var_read_write = "GOOGLE_CLOUD_SPANNER_MULTIPLEXED_SESSIONS_FOR_RW"

    def _getenv(val: str) -> bool:
        return getenv(val, "true").lower().strip() != "false"

    if transaction_type is TransactionType.READ_ONLY:
        return _getenv(env_var)
    elif transaction_type is TransactionType.PARTITIONED:
        return _getenv(env_var) and _getenv(env_var_partitioned)
    else:
        return _getenv(env_var) and _getenv(env_var_read_write)


def get_test_ot_exporter():
    global _TEST_OT_EXPORTER

    if _TEST_OT_EXPORTER is None:
        _TEST_OT_EXPORTER = InMemorySpanExporter()
    return _TEST_OT_EXPORTER


def enrich_with_otel_scope(attrs):
    """
    This helper enriches attrs with OTEL_SCOPE_NAME and OTEL_SCOPE_VERSION
    for the purpose of avoiding cumbersome duplicated imports.
    """
    if HAS_OPENTELEMETRY_INSTALLED:
        attrs["otel.scope.name"] = "cloud.google.com/python/spanner"
        attrs["otel.scope.version"] = LIB_VERSION

    return attrs


def use_test_ot_exporter():
    global _TEST_OT_PROVIDER_INITIALIZED

    if _TEST_OT_PROVIDER_INITIALIZED:
        return

    provider = trace.get_tracer_provider()
    if not hasattr(provider, "add_span_processor"):
        return
    provider.add_span_processor(SimpleSpanProcessor(get_test_ot_exporter()))
    _TEST_OT_PROVIDER_INITIALIZED = True


class OpenTelemetryBase(IsolatedAsyncioTestCase):
    @classmethod
    def setUpClass(cls):
        if HAS_OPENTELEMETRY_INSTALLED:
            use_test_ot_exporter()
            cls.ot_exporter = get_test_ot_exporter()

    def setUp(self):
        super().setUp()
        if HAS_OPENTELEMETRY_INSTALLED:
            self.ot_exporter.clear()

    def tearDown(self):
        if HAS_OPENTELEMETRY_INSTALLED:
            self.ot_exporter.clear()

    def assertNoSpans(self):
        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = self.get_finished_spans()
            self.assertEqual(len(span_list), 0)

    def assertSpanAttributes(
        self, name, status=StatusCode.OK, attributes=None, span=None
    ):
        if HAS_OPENTELEMETRY_INSTALLED:
            if not span:
                span_list = self.get_finished_spans()
                self.assertEqual(len(span_list) > 0, True)
                span = span_list[0]

            self.assertEqual(span.name, name)
            self.assertEqual(span.status.status_code, status)
            self.assertEqual(dict(span.attributes), attributes)

    def assertSpanEvents(self, name, wantEventNames=[], span=None):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        if not span:
            span_list = self.ot_exporter.get_finished_spans()
            self.assertEqual(len(span_list) > 0, True)
            span = span_list[0]

        self.assertEqual(span.name, name)
        actualEventNames = []
        for event in span.events:
            actualEventNames.append(event.name)
        self.assertEqual(actualEventNames, wantEventNames)

    def assertSpanNames(self, want_span_names):
        if not HAS_OPENTELEMETRY_INSTALLED:
            return

        span_list = self.get_finished_spans()
        got_span_names = [span.name for span in span_list]
        self.assertEqual(got_span_names, want_span_names)

    def get_finished_spans(self):
        if HAS_OPENTELEMETRY_INSTALLED:
            span_list = list(
                filter(
                    lambda span: span and span.name,
                    self.ot_exporter.get_finished_spans(),
                )
            )
            # Sort the spans by their start time in the hierarchy.
            return sorted(span_list, key=lambda span: span.start_time)
        else:
            return []

    def reset(self):
        self.tearDown()

    def finished_spans_events_statuses(self):
        span_list = self.get_finished_spans()
        # Some event attributes are noisy/highly ephemeral
        # and can't be directly compared against.
        got_all_events = []
        imprecise_event_attributes = ["exception.stacktrace", "delay_seconds", "cause"]
        for span in span_list:
            for event in span.events:
                evt_attributes = event.attributes.copy()
                for attr_name in imprecise_event_attributes:
                    if attr_name in evt_attributes:
                        evt_attributes[attr_name] = "EPHEMERAL"

                got_all_events.append((event.name, evt_attributes))

        return got_all_events
