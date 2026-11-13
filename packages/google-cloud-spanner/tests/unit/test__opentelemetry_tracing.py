import mock

try:
    from opentelemetry import trace as trace_api
    from opentelemetry.trace.status import StatusCode
except ImportError:
    pass

from google.api_core.exceptions import GoogleAPICallError

from google.cloud.spanner_v1 import _opentelemetry_tracing
from google.cloud.spanner_v1._helpers import GOOGLE_CLOUD_REGION_GLOBAL
from tests._helpers import LIB_VERSION, OpenTelemetryBase, enrich_with_otel_scope


def _make_rpc_error(error_cls, trailing_metadata=None):
    import grpc

    grpc_error = mock.create_autospec(grpc.Call, instance=True)
    grpc_error.trailing_metadata.return_value = trailing_metadata
    return error_cls("error", errors=(grpc_error,))


def _make_session():
    from google.cloud.spanner_v1.session import Session

    session = mock.Mock(autospec=Session, instance=True)
    # Set a string name to allow concatenation
    session._database.name = "projects/p/instances/i/databases/d"
    return session


class TestTracing(OpenTelemetryBase):
    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_trace_call(self, mock_region):
        extra_attributes = {
            "attribute1": "value1",
            # Since our database is mocked, we have to override the db.instance parameter so it is a string
            "db.instance": "database_name",
        }

        expected_attributes = enrich_with_otel_scope(
            {
                "db.type": "spanner",
                "db.url": "spanner.googleapis.com",
                "net.host.name": "spanner.googleapis.com",
                "cloud.region": GOOGLE_CLOUD_REGION_GLOBAL,
                "gcp.client.service": "spanner",
                "gcp.client.version": LIB_VERSION,
                "gcp.client.repo": "googleapis/python-spanner",
                "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX
                + "projects/p/instances/i/databases/d",
            }
        )
        expected_attributes.update(extra_attributes)

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.Test", _make_session(), extra_attributes
        ) as span:
            span.set_attribute("after_setup_attribute", 1)

        expected_attributes["after_setup_attribute"] = 1

        span_list = self.ot_exporter.get_finished_spans()
        self.assertEqual(len(span_list), 1)

        span = span_list[0]
        self.assertEqual(span.kind, trace_api.SpanKind.CLIENT)
        self.assertEqual(span.attributes, expected_attributes)
        self.assertEqual(span.name, "CloudSpanner.Test")
        self.assertEqual(span.status.status_code, StatusCode.OK)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_trace_error(self, mock_region):
        extra_attributes = {"db.instance": "database_name"}

        expected_attributes = enrich_with_otel_scope(
            {
                "db.type": "spanner",
                "db.url": "spanner.googleapis.com",
                "net.host.name": "spanner.googleapis.com",
                "cloud.region": GOOGLE_CLOUD_REGION_GLOBAL,
                "gcp.client.service": "spanner",
                "gcp.client.version": LIB_VERSION,
                "gcp.client.repo": "googleapis/python-spanner",
                "gcp.resource.name": _opentelemetry_tracing.GCP_RESOURCE_NAME_PREFIX
                + "projects/p/instances/i/databases/d",
            }
        )
        expected_attributes.update(extra_attributes)

        with self.assertRaises(GoogleAPICallError):
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.Test", _make_session(), extra_attributes
            ) as span:
                from google.api_core.exceptions import InvalidArgument

                raise _make_rpc_error(InvalidArgument)

        span_list = self.ot_exporter.get_finished_spans()
        self.assertEqual(len(span_list), 1)
        span = span_list[0]
        self.assertEqual(span.kind, trace_api.SpanKind.CLIENT)
        self.assertEqual(dict(span.attributes), expected_attributes)
        self.assertEqual(span.name, "CloudSpanner.Test")
        self.assertEqual(span.status.status_code, StatusCode.ERROR)

    def test_trace_grpc_error(self):
        extra_attributes = {"db.instance": "database_name"}

        expected_attributes = enrich_with_otel_scope(
            {
                "db.type": "spanner",
                "db.url": "spanner.googleapis.com:443",
                "net.host.name": "spanner.googleapis.com:443",
            }
        )
        expected_attributes.update(extra_attributes)

        with self.assertRaises(GoogleAPICallError):
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.Test", _make_session(), extra_attributes
            ) as span:
                from google.api_core.exceptions import DataLoss

                raise DataLoss("error")

        span_list = self.ot_exporter.get_finished_spans()
        self.assertEqual(len(span_list), 1)
        span = span_list[0]
        self.assertEqual(span.status.status_code, StatusCode.ERROR)

    def test_trace_codeless_error(self):
        extra_attributes = {"db.instance": "database_name"}

        expected_attributes = enrich_with_otel_scope(
            {
                "db.type": "spanner",
                "db.url": "spanner.googleapis.com:443",
                "net.host.name": "spanner.googleapis.com:443",
            }
        )
        expected_attributes.update(extra_attributes)

        with self.assertRaises(GoogleAPICallError):
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.Test", _make_session(), extra_attributes
            ) as span:
                raise GoogleAPICallError("error")

        span_list = self.ot_exporter.get_finished_spans()
        self.assertEqual(len(span_list), 1)
        span = span_list[0]
        self.assertEqual(span.status.status_code, StatusCode.ERROR)

    def test_trace_call_terminal_span_status_ALWAYS_ON_sampler(self):
        # Verify that we don't unconditionally set the terminal span status to
        # SpanStatus.OK per https://github.com/googleapis/python-spanner/issues/1246
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
        from opentelemetry.sdk.trace.sampling import ALWAYS_ON
        from opentelemetry.trace.status import Status, StatusCode

        tracer_provider = TracerProvider(sampler=ALWAYS_ON)
        trace_exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(trace_exporter))
        observability_options = dict(tracer_provider=tracer_provider)

        session = _make_session()
        with _opentelemetry_tracing.trace_call(
            "VerifyTerminalSpanStatus",
            session,
            observability_options=observability_options,
        ) as span:
            span.set_status(Status(StatusCode.ERROR, "Our error exhibit"))

        span_list = trace_exporter.get_finished_spans()
        got_statuses = []

        for span in span_list:
            got_statuses.append(
                (span.name, span.status.status_code, span.status.description)
            )

        want_statuses = [
            ("VerifyTerminalSpanStatus", StatusCode.ERROR, "Our error exhibit"),
        ]
        assert got_statuses == want_statuses

    def test_trace_call_terminal_span_status_ALWAYS_OFF_sampler(self):
        # Verify that we get the correct status even when using the ALWAYS_OFF
        # sampler which produces the NonRecordingSpan per
        # https://github.com/googleapis/python-spanner/issues/1286
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )
        from opentelemetry.sdk.trace.sampling import ALWAYS_OFF

        tracer_provider = TracerProvider(sampler=ALWAYS_OFF)
        trace_exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(trace_exporter))
        observability_options = dict(tracer_provider=tracer_provider)

        session = _make_session()
        used_span = None
        with _opentelemetry_tracing.trace_call(
            "VerifyWithNonRecordingSpan",
            session,
            observability_options=observability_options,
        ) as span:
            used_span = span

        assert type(used_span).__name__ == "NonRecordingSpan"
        span_list = list(trace_exporter.get_finished_spans())
        assert span_list == []

    def test_is_tracer_noop(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.trace import NoOpTracer, ProxyTracer

        self.assertTrue(_opentelemetry_tracing._is_tracer_noop(None))
        self.assertTrue(_opentelemetry_tracing._is_tracer_noop(NoOpTracer()))

        # ProxyTracer with uninitialized real tracer delegates to NoOpTracer
        with mock.patch("opentelemetry.trace._TRACER_PROVIDER", None):
            proxy_tracer_noop = ProxyTracer("test_mod")
            self.assertTrue(_opentelemetry_tracing._is_tracer_noop(proxy_tracer_noop))

        # Real SDK tracer is not no-op
        sdk_provider = TracerProvider()
        sdk_tracer = sdk_provider.get_tracer("test_mod")
        self.assertFalse(_opentelemetry_tracing._is_tracer_noop(sdk_tracer))

        # ProxyTracer with real tracer attached is not no-op
        proxy_tracer_active = ProxyTracer("test_mod")
        proxy_tracer_active._real_tracer = sdk_tracer
        self.assertFalse(_opentelemetry_tracing._is_tracer_noop(proxy_tracer_active))

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_trace_call_noop_tracer_provider_short_circuits(self, mock_region):
        session = _make_session()
        session._last_use_time = None
        observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestNoOp",
            session,
            extra_attributes={"db.statement": "SELECT 1"},
            observability_options=observability_options,
        ) as span:
            self.assertFalse(span.is_recording())
            self.assertEqual(span, trace_api.INVALID_SPAN)

        mock_region.assert_not_called()
        self.assertIsNotNone(session._last_use_time)

    @mock.patch(
        "google.cloud.spanner_v1._opentelemetry_tracing._get_cloud_region",
        return_value="global",
    )
    def test_trace_call_noop_with_ambient_span(self, mock_region):
        from opentelemetry.context import attach, detach

        ambient_context = trace_api.SpanContext(
            trace_id=0x12345678123456781234567812345678,
            span_id=0x1234567812345678,
            is_remote=False,
        )
        ambient_span = trace_api.NonRecordingSpan(ambient_context)
        token = attach(trace_api.set_span_in_context(ambient_span))

        try:
            observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())
            session = _make_session()

            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.TestAmbient",
                session,
                observability_options=observability_options,
            ) as span:
                self.assertFalse(span.is_recording())
                # Active span in context is the child span, masking the ambient span
                self.assertEqual(_opentelemetry_tracing.get_current_span(), span)
                self.assertNotEqual(span, trace_api.INVALID_SPAN)
                self.assertEqual(
                    span.get_span_context().trace_id, ambient_context.trace_id
                )

            mock_region.assert_not_called()
        finally:
            detach(token)

    def test_trace_call_noop_with_invalid_ambient_span(self):
        from opentelemetry.context import attach, detach

        invalid_ambient = trace_api.NonRecordingSpan(trace_api.INVALID_SPAN_CONTEXT)
        token = attach(trace_api.set_span_in_context(invalid_ambient))

        try:
            observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.TestInvalidAmbient",
                _make_session(),
                observability_options=observability_options,
            ) as span:
                self.assertFalse(span.is_recording())
                self.assertEqual(span, trace_api.INVALID_SPAN)
        finally:
            detach(token)

    def test_trace_call_noop_does_not_pollute_ambient_span(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )

        exporter = InMemorySpanExporter()
        provider = TracerProvider()
        provider.add_span_processor(SimpleSpanProcessor(exporter))
        ambient_tracer = provider.get_tracer("ambient_app")

        with ambient_tracer.start_as_current_span("ambient_request"):
            observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.IsolatedCall",
                session=None,
                observability_options=observability_options,
            ):
                current = _opentelemetry_tracing.get_current_span()
                _opentelemetry_tracing.add_span_event(current, "internal_event")
                current.set_attribute("internal_attr", "internal_val")

        finished_spans = exporter.get_finished_spans()
        self.assertEqual(len(finished_spans), 1)
        parent_span = finished_spans[0]
        self.assertNotIn("internal_attr", parent_span.attributes)
        self.assertEqual(len(parent_span.events), 0)

    def test_trace_call_noop_provider_end_to_end_tracing(self):
        observability_options = dict(
            tracer_provider=trace_api.NoOpTracerProvider(),
            enable_end_to_end_tracing=True,
        )
        metadata = []
        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestE2E",
            _make_session(),
            observability_options=observability_options,
            metadata=metadata,
        ) as span:
            self.assertFalse(span.is_recording())

        self.assertTrue(
            any(item[0] == "x-goog-spanner-end-to-end-tracing" for item in metadata)
        )

    def test_trace_call_noop_fast_path_exception(self):
        observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())

        with self.assertRaises(ValueError):
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.TestError",
                _make_session(),
                observability_options=observability_options,
            ):
                raise ValueError("Test error in fast path")

    def test_trace_call_dict_subclass_observability_options(self):
        from collections import UserDict

        observability_options = UserDict(
            {"tracer_provider": trace_api.NoOpTracerProvider()}
        )
        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestUserDict",
            _make_session(),
            observability_options=observability_options,
        ) as span:
            self.assertEqual(span, trace_api.INVALID_SPAN)

    def test_trace_call_head_sampler_receives_attributes(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.sampling import (
            Decision,
            Sampler,
            SamplingResult,
        )

        class AttributeCapturingSampler(Sampler):
            def __init__(self):
                self.captured_attributes = None

            def should_sample(
                self,
                parent_context,
                trace_id,
                name,
                kind=None,
                attributes=None,
                links=None,
                trace_state=None,
            ):
                self.captured_attributes = dict(attributes) if attributes else {}
                return SamplingResult(Decision.RECORD_AND_SAMPLE)

            def get_description(self):
                return "AttributeCapturingSampler"

        sampler = AttributeCapturingSampler()
        tracer_provider = TracerProvider(sampler=sampler)
        observability_options = dict(
            tracer_provider=tracer_provider,
            db_name="projects/p/instances/i/databases/custom_db",
        )

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestSampler",
            _make_session(),
            extra_attributes={"custom.attr": "value1"},
            observability_options=observability_options,
        ):
            pass

        self.assertIsNotNone(sampler.captured_attributes)
        self.assertEqual(sampler.captured_attributes.get("db.type"), "spanner")
        self.assertEqual(
            sampler.captured_attributes.get("db.instance"),
            "projects/p/instances/i/databases/custom_db",
        )
        self.assertEqual(sampler.captured_attributes.get("custom.attr"), "value1")

    def test_trace_call_span_processor_on_start_receives_attributes(self):
        from opentelemetry.sdk.trace import SpanProcessor, TracerProvider

        class AttributeCapturingProcessor(SpanProcessor):
            def __init__(self):
                self.started_attributes = None

            def on_start(self, span, parent_context=None):
                self.started_attributes = (
                    dict(span.attributes) if span.attributes else {}
                )

            def on_end(self, span):
                pass

        processor = AttributeCapturingProcessor()
        tracer_provider = TracerProvider()
        tracer_provider.add_span_processor(processor)
        observability_options = dict(tracer_provider=tracer_provider)

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestProcessor",
            _make_session(),
            extra_attributes={"on_start.attr": "value2"},
            observability_options=observability_options,
        ):
            pass

        self.assertIsNotNone(processor.started_attributes)
        self.assertEqual(processor.started_attributes.get("db.type"), "spanner")
        self.assertEqual(processor.started_attributes.get("on_start.attr"), "value2")

    def test_trace_call_request_options_and_disabled_extended_tracing(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )

        class DummyRequestOptions:
            request_tag = "test-tag"

        tracer_provider = TracerProvider()
        exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(exporter))

        observability_options = dict(
            tracer_provider=tracer_provider,
            enable_extended_tracing=False,
            enable_end_to_end_tracing=True,
        )
        metadata = []

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestOptions",
            _make_session(),
            extra_attributes={
                "db.statement": "SELECT 1",
                "request_options": DummyRequestOptions(),
            },
            observability_options=observability_options,
            metadata=metadata,
        ):
            pass

        spans = exporter.get_finished_spans()
        self.assertEqual(len(spans), 1)
        self.assertEqual(spans[0].attributes.get("request.tag"), "test-tag")
        self.assertNotIn("db.statement", spans[0].attributes)
        self.assertTrue(
            any(item[0] == "x-goog-spanner-end-to-end-tracing" for item in metadata)
        )

    def test_trace_call_noop_with_ambient_span_and_e2e_tracing(self):
        from opentelemetry.context import attach, detach

        ambient_context = trace_api.SpanContext(
            trace_id=0x12345678123456781234567812345678,
            span_id=0x1234567812345678,
            is_remote=False,
        )
        ambient_span = trace_api.NonRecordingSpan(ambient_context)
        token = attach(trace_api.set_span_in_context(ambient_span))

        try:
            metadata = []
            observability_options = dict(
                tracer_provider=trace_api.NoOpTracerProvider(),
                enable_end_to_end_tracing=True,
            )
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.TestAmbientE2E",
                _make_session(),
                observability_options=observability_options,
                metadata=metadata,
            ):
                pass
            self.assertTrue(
                any(item[0] == "x-goog-spanner-end-to-end-tracing" for item in metadata)
            )
        finally:
            detach(token)

    @mock.patch.object(
        _opentelemetry_tracing, "end_to_end_tracing_globally_enabled", True
    )
    def test_trace_call_global_e2e_tracing_enabled(self):
        observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())
        metadata = []
        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestGlobalE2E",
            _make_session(),
            observability_options=observability_options,
            metadata=metadata,
        ):
            pass
        self.assertTrue(
            any(item[0] == "x-goog-spanner-end-to-end-tracing" for item in metadata)
        )

    @mock.patch.object(
        _opentelemetry_tracing, "extended_tracing_globally_disabled", True
    )
    def test_trace_call_global_extended_tracing_disabled(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )

        tracer_provider = TracerProvider()
        exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(exporter))
        observability_options = dict(tracer_provider=tracer_provider)

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestGlobalExtendedDisabled",
            _make_session(),
            extra_attributes={"db.statement": "SELECT 1"},
            observability_options=observability_options,
        ):
            pass

        spans = exporter.get_finished_spans()
        self.assertEqual(len(spans), 1)
        self.assertNotIn("db.statement", spans[0].attributes)

    def test_trace_call_default_production_unconfigured_without_session(self):
        with mock.patch("opentelemetry.trace._TRACER_PROVIDER", None):
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.TestDefaultNoSession", session=None
            ) as span:
                self.assertEqual(span, trace_api.INVALID_SPAN)

    def test_trace_call_active_without_session_database(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )

        tracer_provider = TracerProvider()
        exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(exporter))
        observability_options = dict(tracer_provider=tracer_provider)

        # Session is None
        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestNoSessionActive",
            session=None,
            observability_options=observability_options,
        ):
            pass

        spans = exporter.get_finished_spans()
        self.assertEqual(len(spans), 1)
        self.assertEqual(spans[0].attributes.get("db.instance"), "")

    def test_trace_call_active_request_options_without_tag(self):
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )

        class UntaggedRequestOptions:
            request_tag = None

        tracer_provider = TracerProvider()
        exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(exporter))
        observability_options = dict(tracer_provider=tracer_provider)

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestUntaggedOptions",
            _make_session(),
            extra_attributes={"request_options": UntaggedRequestOptions()},
            observability_options=observability_options,
        ):
            pass

        spans = exporter.get_finished_spans()
        self.assertEqual(len(spans), 1)
        self.assertNotIn("request.tag", spans[0].attributes)

    def test_trace_call_noop_with_ambient_span_exception(self):
        from opentelemetry.context import attach, detach

        ambient_context = trace_api.SpanContext(
            trace_id=0x12345678123456781234567812345678,
            span_id=0x1234567812345678,
            is_remote=False,
        )
        ambient_span = trace_api.NonRecordingSpan(ambient_context)
        token = attach(trace_api.set_span_in_context(ambient_span))

        try:
            observability_options = dict(tracer_provider=trace_api.NoOpTracerProvider())
            with self.assertRaises(RuntimeError):
                with _opentelemetry_tracing.trace_call(
                    "CloudSpanner.TestAmbientError",
                    _make_session(),
                    observability_options=observability_options,
                ):
                    raise RuntimeError("Error with ambient span")
        finally:
            detach(token)

    def test_add_span_event(self):
        span = mock.Mock()
        _opentelemetry_tracing.add_span_event(span, "test_event", {"attr": "val"})
        span.add_event.assert_called_once_with("test_event", {"attr": "val"})

    @mock.patch("google.cloud.spanner_v1.metrics.metrics_capture.MetricsCapture")
    def test_trace_call_does_not_invoke_metrics_capture(self, mock_metrics_capture):
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import SimpleSpanProcessor
        from opentelemetry.sdk.trace.export.in_memory_span_exporter import (
            InMemorySpanExporter,
        )

        # 1. No-op path (no ambient span)
        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestNoOpSpan",
            _make_session(),
            observability_options={"tracer_provider": trace.NoOpTracerProvider()},
        ) as noop_span:
            self.assertIs(noop_span, trace.INVALID_SPAN)
        mock_metrics_capture.assert_not_called()

        # 2. No-op path with ambient valid span context (sub-branch 1a)
        valid_span_context = trace.SpanContext(
            trace_id=0x12345678123456781234567812345678,
            span_id=0x1234567812345678,
            is_remote=False,
            trace_flags=trace.TraceFlags(trace.TraceFlags.SAMPLED),
        )
        ambient_span = trace.NonRecordingSpan(valid_span_context)
        with trace.use_span(ambient_span):
            with _opentelemetry_tracing.trace_call(
                "CloudSpanner.TestNoOpSpanWithAmbient",
                _make_session(),
                observability_options={"tracer_provider": trace.NoOpTracerProvider()},
            ) as child_span:
                self.assertIsInstance(child_span, trace.NonRecordingSpan)
        mock_metrics_capture.assert_not_called()

        # 3. Active span path
        tracer_provider = TracerProvider()
        exporter = InMemorySpanExporter()
        tracer_provider.add_span_processor(SimpleSpanProcessor(exporter))
        observability_options = dict(tracer_provider=tracer_provider)

        with _opentelemetry_tracing.trace_call(
            "CloudSpanner.TestActiveSpan",
            _make_session(),
            observability_options=observability_options,
        ):
            pass
        mock_metrics_capture.assert_not_called()
