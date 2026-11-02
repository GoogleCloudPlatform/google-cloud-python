# Copyright 2017, Google LLC All rights reserved.
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

from __future__ import absolute_import, division

import inspect
import math
import time
from typing import Any, Callable, TypeVar, cast
from unittest import mock

import grpc
import pytest
from flaky import flaky
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.gapic_v1.client_info import METRICS_METADATA_KEY
from google.api_core.timeout import ConstantTimeout
from opentelemetry import trace

from google.cloud.pubsub_v1 import publisher, types
from google.cloud.pubsub_v1.open_telemetry.context_propagation import (
    OpenTelemetryContextSetter,
)
from google.cloud.pubsub_v1.open_telemetry.publish_message_wrapper import (
    PublishMessageWrapper,
)
from google.cloud.pubsub_v1.publisher import exceptions
from google.cloud.pubsub_v1.publisher._sequencer import ordered_sequencer
from google.pubsub_v1 import types as gapic_types
from google.pubsub_v1.services.publisher import client as publisher_client
from google.pubsub_v1.services.publisher.transports.grpc import PublisherGrpcTransport

C = TypeVar("C", bound=Callable[..., Any])
typed_flaky = cast(Callable[[C], C], flaky(max_runs=5, min_passes=1))


# Attempt to use `_thunk` to obtain the underlying grpc channel from
# the intercept channel. Default to obtaining the grpc channel directly
# for backwards compatibility.
# TODO(https://github.com/grpc/grpc/issues/38519): Workaround to obtain a channel
# until a public API is available.
def get_publish_channel(client):
    try:
        return client._transport.publish._thunk("")._channel
    except AttributeError:
        return client._transport.publish._channel


def _assert_retries_equal(retry, retry2):
    # Retry instances cannot be directly compared, because their predicates are
    # different instances of the same function. We thus manually compare their other
    # attributes, and then heuristically compare their predicates.
    for attr in ("_deadline", "_initial", "_maximum", "_multiplier"):
        assert getattr(retry, attr) == getattr(retry2, attr)

    pred = retry._predicate
    pred2 = retry2._predicate
    assert inspect.getsource(pred) == inspect.getsource(pred2)
    assert inspect.getclosurevars(pred) == inspect.getclosurevars(pred2)


def test_api_property_deprecated(creds):
    client = publisher.Client(credentials=creds)

    with pytest.warns(DeprecationWarning, match="client.api") as warned:
        client.api

    assert len(warned) == 1
    assert issubclass(warned[0].category, DeprecationWarning)
    warning_msg = str(warned[0].message)
    assert "client.api" in warning_msg


def test_api_property_proxy_to_generated_client(creds):
    client = publisher.Client(credentials=creds)

    with pytest.warns(DeprecationWarning, match="client.api"):
        api_object = client.api

    # Not a perfect check, but we are satisficed if the returned API object indeed
    # contains all methods of the generated class.
    superclass_attrs = (attr for attr in dir(type(client).__mro__[1]))
    assert all(
        hasattr(api_object, attr)
        for attr in superclass_attrs
        if callable(getattr(client, attr))
    )

    # The resume_publish() method only exists on the hand-written wrapper class.
    assert hasattr(client, "resume_publish")
    assert not hasattr(api_object, "resume_publish")


def test_init(creds):
    client = publisher.Client(credentials=creds)

    # A plain client should have a batch settings object containing the defaults.
    assert client.batch_settings.max_bytes == 1 * 1000 * 1000
    assert client.batch_settings.max_latency == 0.01
    assert client.batch_settings.max_messages == 100


def test_init_default_client_info(creds):
    client = publisher.Client(credentials=creds)

    installed_version = publisher.client.__version__
    expected_client_info = f"gccl/{installed_version}"

    for wrapped_method in client.transport._wrapped_methods.values():
        # Handle internal changes in google-api-core _GapicCallable
        metadata = getattr(
            wrapped_method,
            "_metadata",
            getattr(wrapped_method, "_default_metadata", []),
        )
        user_agent = next(
            (
                header_value
                for header, header_value in metadata
                if header == METRICS_METADATA_KEY
            ),
            None,  # pragma: NO COVER
        )
        assert user_agent is not None
        assert expected_client_info in user_agent


def test_init_w_custom_transport(creds):
    transport = PublisherGrpcTransport(credentials=creds)
    client = publisher.Client(transport=transport)

    # A plain client should have a transport and a batch settings object, which should
    # contain the defaults.
    assert isinstance(client, publisher_client.PublisherClient)
    assert client._transport is transport
    assert client.batch_settings.max_bytes == 1 * 1000 * 1000
    assert client.batch_settings.max_latency == 0.01
    assert client.batch_settings.max_messages == 100


@pytest.mark.parametrize(
    "enable_open_telemetry",
    [
        True,
        False,
    ],
)
@typed_flaky
def test_open_telemetry_publisher_options(creds, enable_open_telemetry):
    client = publisher.Client(
        publisher_options=types.PublisherOptions(
            enable_open_telemetry_tracing=enable_open_telemetry
        ),
        credentials=creds,
    )
    assert client._open_telemetry_enabled == enable_open_telemetry


def test_opentelemetry_context_setter():
    msg = gapic_types.PubsubMessage(data=b"foo")
    OpenTelemetryContextSetter().set(carrier=msg, key="key", value="bar")

    assert "googclient_key" in msg.attributes.keys()


def test_opentelemetry_context_propagation(creds, span_exporter):
    TOPIC = "projects/projectID/topics/topicID"
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(
            enable_open_telemetry_tracing=True,
        ),
    )

    message_mock = mock.Mock(spec=publisher.flow_controller.FlowController.add)
    client._flow_controller.add = message_mock
    client.publish(TOPIC, b"data")

    message_mock.assert_called_once()
    args = message_mock.call_args.args
    assert len(args) == 1
    assert "googclient_traceparent" in args[0].attributes


@pytest.mark.parametrize(
    "enable_open_telemetry",
    [
        True,
        False,
    ],
)
def test_opentelemetry_publisher_batching_exception(
    creds, span_exporter, enable_open_telemetry
):
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(
            enable_open_telemetry_tracing=enable_open_telemetry,
        ),
    )

    # Throw an exception when sequencer.publish() is called
    sequencer = mock.Mock(spec=ordered_sequencer.OrderedSequencer)
    sequencer.publish = mock.Mock(side_effect=RuntimeError("some error"))
    client._get_or_create_sequencer = mock.Mock(return_value=sequencer)

    TOPIC = "projects/projectID/topics/topicID"
    with pytest.raises(RuntimeError):
        client.publish(TOPIC, b"message")

    spans = span_exporter.get_finished_spans()

    if enable_open_telemetry:
        # Span 1: Publisher Flow Control span
        # Span 2: Publisher Batching span
        # Span 3: Create Publish span
        assert len(spans) == 3

        flow_control_span, batching_span, create_span = spans

        # Verify batching span contents.
        assert batching_span.name == "publisher batching"
        assert batching_span.kind == trace.SpanKind.INTERNAL
        assert batching_span.parent.span_id == create_span.get_span_context().span_id

        # Verify exception recorded by the publisher batching span.
        assert batching_span.status.status_code == trace.StatusCode.ERROR
        assert len(batching_span.events) == 1
        assert batching_span.events[0].name == "exception"

        # Verify exception recorded by the publisher create span.
        assert create_span.status.status_code == trace.StatusCode.ERROR
        assert len(create_span.events) == 2
        assert create_span.events[0].name == "publish start"
        assert create_span.events[1].name == "exception"

        # Verify the finished flow control span.
        assert flow_control_span.name == "publisher flow control"
        assert len(flow_control_span.events) == 0
    else:
        assert len(spans) == 0


def test_opentelemetry_flow_control_exception(creds, span_exporter):
    publisher_options = types.PublisherOptions(
        flow_control=types.PublishFlowControl(
            message_limit=10,
            byte_limit=150,
            limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
        ),
        enable_open_telemetry_tracing=True,
    )
    client = publisher.Client(credentials=creds, publisher_options=publisher_options)

    mock_batch = mock.Mock(spec=client._batch_class)
    topic = "projects/projectID/topics/topicID"
    client._set_batch(topic, mock_batch)

    future1 = client.publish(topic, b"a" * 60)
    future2 = client.publish(topic, b"b" * 100)

    future1.result()  # no error, still within flow control limits
    with pytest.raises(exceptions.FlowControlLimitError):
        future2.result()

    spans = span_exporter.get_finished_spans()

    # Find the spans related to the second, failing publish call.
    # We first find the failed flow control span.
    failed_fc_span = None
    for span in spans:
        if (
            span.name == "publisher flow control"
            and span.status.status_code == trace.StatusCode.ERROR
        ):
            failed_fc_span = span
            break

    # Next, we find the corresponding 'create' span.
    # Crucially, to prevent matching late-arriving or concurrent publish spans from other tests
    # (e.g. background batch/sequencer threads from previous tests executing late),
    # we filter for the 'topicID create' span that shares the EXACT same trace ID.
    failed_create_span = None
    if failed_fc_span:
        for span in spans:
            if (
                span.name == "topicID create"
                and span.context.trace_id == failed_fc_span.context.trace_id
            ):
                failed_create_span = span
                break

    assert failed_create_span is not None, "Failed 'topicID create' span not found"
    assert failed_fc_span is not None, "Failed 'publisher flow control' span not found"

    # Verify failed flow control span values.
    assert failed_fc_span.kind == trace.SpanKind.INTERNAL
    assert (
        failed_fc_span.parent.span_id == failed_create_span.get_span_context().span_id
    )
    assert len(failed_fc_span.events) == 1
    assert failed_fc_span.events[0].name == "exception"

    # Verify finished publish create span values
    assert failed_create_span.status.status_code == trace.StatusCode.ERROR
    assert len(failed_create_span.events) >= 1  # Should have at least 'publish start'
    assert failed_create_span.events[0].name == "publish start"
    # Check for exception event
    has_exception_event = any(
        event.name == "exception" for event in failed_create_span.events
    )
    assert has_exception_event, "Exception event not found in failed create span"


def test_opentelemetry_publish(creds, span_exporter):
    TOPIC = "projects/projectID/topics/topicID"
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(
            enable_open_telemetry_tracing=True,
        ),
    )

    client.publish(TOPIC, b"message")
    spans = span_exporter.get_finished_spans()

    # Publisher Flow control and batching spans would be ended in the
    # publish() function and are deterministically expected to be in the
    # list of exported spans. The Publish Create span and Publish RPC span
    # are run async and end at a non-deterministic time. Hence,
    # asserting that we have atleast two spans(flow control and batching span)
    assert len(spans) >= 2
    flow_control_span = None
    batching_span = None
    for span in spans:
        if span.name == "publisher flow control":
            flow_control_span = span
            assert flow_control_span.kind == trace.SpanKind.INTERNAL
            assert flow_control_span.parent is not None
        if span.name == "publisher batching":
            batching_span = span
            assert batching_span.kind == trace.SpanKind.INTERNAL
            assert batching_span.parent is not None

    assert flow_control_span is not None
    assert batching_span is not None


def test_init_w_api_endpoint(creds):
    client_options = {"api_endpoint": "testendpoint.google.com"}
    client = publisher.Client(client_options=client_options, credentials=creds)

    # Behavior to include dns prefix changed in gRPCv1.63
    grpc_major, grpc_minor = [int(part) for part in grpc.__version__.split(".")[0:2]]
    if grpc_major > 1 or (grpc_major == 1 and grpc_minor >= 63):
        _EXPECTED_TARGET = "dns:///testendpoint.google.com:443"
    else:
        _EXPECTED_TARGET = "testendpoint.google.com:443"
    assert (client._transport.grpc_channel._channel.target()).decode(
        "utf-8"
    ) == _EXPECTED_TARGET


def test_init_w_empty_client_options(creds):
    client = publisher.Client(client_options={}, credentials=creds)
    # Behavior to include dns prefix changed in gRPCv1.63
    grpc_major, grpc_minor = [int(part) for part in grpc.__version__.split(".")[0:2]]
    if grpc_major > 1 or (grpc_major == 1 and grpc_minor >= 63):
        _EXPECTED_TARGET = "dns:///pubsub.googleapis.com:443"
    else:
        _EXPECTED_TARGET = "pubsub.googleapis.com:443"
    assert (client._transport.grpc_channel._channel.target()).decode(
        "utf-8"
    ) == _EXPECTED_TARGET


def test_init_client_options_pass_through():
    mock_ssl_creds = grpc.ssl_channel_credentials()

    def init(self, *args, **kwargs):
        self.kwargs = kwargs
        self._transport = mock.Mock()
        self._transport._host = "testendpoint.google.com"
        self._transport._ssl_channel_credentials = mock_ssl_creds

    with mock.patch.object(publisher_client.PublisherClient, "__init__", init):
        client = publisher.Client(
            client_options={
                "quota_project_id": "42",
                "scopes": [],
                "credentials_file": "file.json",
            }
        )
        client_options = client.kwargs["client_options"]
        assert client_options.get("quota_project_id") == "42"
        assert client_options.get("scopes") == []
        assert client_options.get("credentials_file") == "file.json"
        assert client.target == "testendpoint.google.com"
        assert client.transport._ssl_channel_credentials == mock_ssl_creds


def test_init_emulator(monkeypatch):
    monkeypatch.setenv("PUBSUB_EMULATOR_HOST", "/foo/bar:123")
    # NOTE: When the emulator host is set, a custom channel will be used, so
    #       no credentials (mock ot otherwise) can be passed in.
    client = publisher.Client()

    # Establish that a gRPC request would attempt to hit the emulator host.
    #
    # Sadly, there seems to be no good way to do this without poking at
    # the private API of gRPC.
    channel = get_publish_channel(client)
    # Behavior to include dns prefix changed in gRPCv1.63
    grpc_major, grpc_minor = [int(part) for part in grpc.__version__.split(".")[0:2]]
    if grpc_major > 1 or (grpc_major == 1 and grpc_minor >= 63):
        _EXPECTED_TARGET = "dns:////foo/bar:123"
    else:
        _EXPECTED_TARGET = "/foo/bar:123"
    assert channel.target().decode("utf8") == _EXPECTED_TARGET


def test_message_ordering_enabled(creds):
    client = publisher.Client(credentials=creds)
    assert not client._enable_message_ordering

    client = publisher.Client(
        publisher_options=types.PublisherOptions(enable_message_ordering=True),
        credentials=creds,
    )
    assert client._enable_message_ordering


def test_publish(creds):
    client = publisher.Client(credentials=creds)

    future1 = mock.sentinel.future1
    future2 = mock.sentinel.future2
    future1.add_done_callback = mock.Mock(spec=["__call__"])
    future2.add_done_callback = mock.Mock(spec=["__call__"])

    # Use a mock in lieu of the actual batch class.
    batch = mock.Mock(spec=client._batch_class)

    # Set the mock up to claim indiscriminately that it accepts all messages.
    batch.publish.side_effect = (future1, future2)

    topic = "topic/path"
    client._set_batch(topic, batch)

    # Begin publishing.
    future1 = client.publish(topic, b"spam")
    future2 = client.publish(topic, b"foo", bar="baz")

    assert future1 is mock.sentinel.future1
    assert future2 is mock.sentinel.future2

    # Check mock.
    batch.publish.assert_has_calls(
        [
            mock.call(
                PublishMessageWrapper(
                    message=gapic_types.PubsubMessage(data=b"spam"),
                )
            ),
            mock.call(
                PublishMessageWrapper(
                    message=gapic_types.PubsubMessage(
                        data=b"foo", attributes={"bar": "baz"}
                    )
                )
            ),
        ]
    )


def test_publish_error_exceeding_flow_control_limits(creds):
    publisher_options = types.PublisherOptions(
        flow_control=types.PublishFlowControl(
            message_limit=10,
            byte_limit=150,
            limit_exceeded_behavior=types.LimitExceededBehavior.ERROR,
        )
    )
    client = publisher.Client(credentials=creds, publisher_options=publisher_options)

    mock_batch = mock.Mock(spec=client._batch_class)
    topic = "topic/path"
    client._set_batch(topic, mock_batch)

    future1 = client.publish(topic, b"a" * 100)
    future2 = client.publish(topic, b"b" * 100)

    future1.result()  # no error, still within flow control limits
    with pytest.raises(exceptions.FlowControlLimitError):
        future2.result()


def test_publish_data_not_bytestring_error(creds):
    client = publisher.Client(credentials=creds)
    topic = "topic/path"
    with pytest.raises(TypeError):
        client.publish(topic, "This is a text string.")
    with pytest.raises(TypeError):
        client.publish(topic, 42)


def test_publish_message_ordering_not_enabled_error(creds):
    client = publisher.Client(credentials=creds)
    topic = "topic/path"
    with pytest.raises(ValueError):
        client.publish(topic, b"bytestring body", ordering_key="ABC")


def test_publish_empty_ordering_key_when_message_ordering_enabled(creds):
    client = publisher.Client(
        publisher_options=types.PublisherOptions(enable_message_ordering=True),
        credentials=creds,
    )
    topic = "topic/path"
    assert client.publish(topic, b"bytestring body", ordering_key="") is not None


def test_publish_with_ordering_key_uses_extended_retry_deadline(creds):
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(enable_message_ordering=True),
    )

    # Use mocks in lieu of the actual batch class.
    batch = mock.Mock(spec=client._batch_class)
    future = mock.sentinel.future
    future.add_done_callback = mock.Mock(spec=["__call__"])
    batch.publish.return_value = future

    topic = "topic/path"
    client._set_batch(topic, batch)

    # Actually mock the batch class now.
    batch_class = mock.Mock(spec=(), return_value=batch)
    client._set_batch_class(batch_class)

    # Publish a message with custom retry settings.
    custom_retry = retries.Retry(
        initial=1,
        maximum=20,
        multiplier=3.3,
        deadline=999,
        predicate=retries.if_exception_type(TimeoutError, KeyboardInterrupt),
    )
    future = client.publish(topic, b"foo", ordering_key="first", retry=custom_retry)
    assert future is mock.sentinel.future

    # Check the retry settings used for the batch.
    batch_class.assert_called_once()
    _, kwargs = batch_class.call_args

    batch_commit_retry = kwargs["commit_retry"]
    expected_retry = custom_retry.with_deadline(2.0**32)
    _assert_retries_equal(batch_commit_retry, expected_retry)

    batch_commit_timeout = kwargs["commit_timeout"]
    expected_timeout = 2.0**32
    assert batch_commit_timeout == pytest.approx(expected_timeout)


def test_publish_with_ordering_key_with_no_retry(creds):
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(enable_message_ordering=True),
    )

    # Use mocks in lieu of the actual batch class.
    batch = mock.Mock(spec=client._batch_class)
    future = mock.sentinel.future
    future.add_done_callback = mock.Mock(spec=["__call__"])
    batch.publish.return_value = future

    topic = "topic/path"
    client._set_batch(topic, batch)

    # Actually mock the batch class now.
    batch_class = mock.Mock(spec=(), return_value=batch)
    client._set_batch_class(batch_class)

    future = client.publish(topic, b"foo", ordering_key="first", retry=None)
    assert future is mock.sentinel.future

    # Check the retry settings used for the batch.
    batch_class.assert_called_once()


def test_publish_attrs_bytestring(creds):
    client = publisher.Client(credentials=creds)

    # Use a mock in lieu of the actual batch class.
    batch = mock.Mock(spec=client._batch_class)
    # Set the mock up to claim indiscriminately that it accepts all messages.

    topic = "topic/path"
    client._set_batch(topic, batch)

    # Begin publishing.
    future = client.publish(topic, b"foo", bar=b"baz")

    assert future is batch.publish.return_value

    # The attributes should have been sent as text.
    batch.publish.assert_called_once_with(
        PublishMessageWrapper(
            message=gapic_types.PubsubMessage(data=b"foo", attributes={"bar": "baz"})
        )
    )


def test_publish_new_batch_needed(creds):
    client = publisher.Client(credentials=creds)

    # Use mocks in lieu of the actual batch class.
    batch1 = mock.Mock(spec=client._batch_class)
    batch2 = mock.Mock(spec=client._batch_class)

    # Set the first mock up to claim indiscriminately that it rejects all
    # messages and the second accepts all.
    future = mock.sentinel.future
    future.add_done_callback = mock.Mock(spec=["__call__"])
    batch1.publish.return_value = None
    batch2.publish.return_value = future

    topic = "topic/path"
    client._set_batch(topic, batch1)

    # Actually mock the batch class now.
    batch_class = mock.Mock(spec=(), return_value=batch2)
    client._set_batch_class(batch_class)

    # Publish a message.
    future = client.publish(topic, b"foo", bar=b"baz")
    assert future is mock.sentinel.future

    call_args = batch_class.call_args

    # Check the mocks.
    batch_class.assert_called_once_with(
        client=mock.ANY,
        topic=topic,
        settings=client.batch_settings,
        batch_done_callback=None,
        commit_when_full=True,
        commit_retry=gapic_v1.method.DEFAULT,
        commit_timeout=mock.ANY,
    )
    commit_timeout_arg = call_args[1]["commit_timeout"]
    assert isinstance(commit_timeout_arg, ConstantTimeout)
    assert math.isclose(commit_timeout_arg._timeout, 60) is True

    message_pb = gapic_types.PubsubMessage(data=b"foo", attributes={"bar": "baz"})
    wrapper = PublishMessageWrapper(message=message_pb)
    batch1.publish.assert_called_once_with(wrapper)
    batch2.publish.assert_called_once_with(wrapper)


def test_publish_attrs_type_error(creds):
    client = publisher.Client(credentials=creds)
    topic = "topic/path"
    with pytest.raises(TypeError):
        client.publish(topic, b"foo", answer=42)


def test_publish_custom_retry_overrides_configured_retry(creds):
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(retry=mock.sentinel.publish_retry),
    )

    topic = "topic/path"
    client._flow_controller = mock.Mock()
    fake_sequencer = mock.Mock()
    client._get_or_create_sequencer = mock.Mock(return_value=fake_sequencer)
    client.publish(topic, b"hello!", retry=mock.sentinel.custom_retry)

    fake_sequencer.publish.assert_called_once_with(
        wrapper=mock.ANY, retry=mock.sentinel.custom_retry, timeout=mock.ANY
    )
    message = fake_sequencer.publish.call_args.kwargs["wrapper"].message
    assert message.data == b"hello!"


def test_publish_custom_timeout_overrides_configured_timeout(creds):
    client = publisher.Client(
        credentials=creds,
        publisher_options=types.PublisherOptions(timeout=mock.sentinel.publish_timeout),
    )

    topic = "topic/path"
    client._flow_controller = mock.Mock()
    fake_sequencer = mock.Mock()
    client._get_or_create_sequencer = mock.Mock(return_value=fake_sequencer)
    client.publish(topic, b"hello!", timeout=mock.sentinel.custom_timeout)

    fake_sequencer.publish.assert_called_once_with(
        wrapper=mock.ANY, retry=mock.ANY, timeout=mock.sentinel.custom_timeout
    )
    message = fake_sequencer.publish.call_args.kwargs["wrapper"].message
    assert message.data == b"hello!"


def test_stop(creds):
    client = publisher.Client(credentials=creds)

    batch1 = mock.Mock(spec=client._batch_class)
    topic = "topic/path"
    client._set_batch(topic, batch1)

    client.stop()

    assert batch1.commit.call_count == 1

    with pytest.raises(RuntimeError):
        client.publish("topic1", b"msg2")

    with pytest.raises(RuntimeError):
        client.resume_publish("topic", "ord_key")

    with pytest.raises(RuntimeError):
        client.stop()


def test_gapic_instance_method(creds):
    client = publisher.Client(credentials=creds)

    topic = gapic_types.Topic(name="projects/foo/topics/bar")
    with mock.patch.object(client, "create_topic") as patched:
        client.create_topic(topic)

    assert patched.call_count == 1
    _, args, _ = patched.mock_calls[0]
    assert args[0] == gapic_types.Topic(name="projects/foo/topics/bar")


def test_gapic_class_method_on_class():
    answer = publisher.Client.topic_path("foo", "bar")
    assert answer == "projects/foo/topics/bar"


def test_class_method_factory():
    patch = mock.patch(
        "google.oauth2.service_account.Credentials.from_service_account_file"
    )

    with patch:
        client = publisher.Client.from_service_account_file("filename.json")

    assert isinstance(client, publisher.Client)


def test_gapic_class_method_on_instance(creds):
    client = publisher.Client(credentials=creds)
    answer = client.topic_path("foo", "bar")
    assert answer == "projects/foo/topics/bar"


def test_commit_thread_created_on_publish(creds):
    # Max latency is not infinite so a commit thread is created.
    batch_settings = types.BatchSettings(max_latency=600)
    client = publisher.Client(batch_settings=batch_settings, credentials=creds)

    with mock.patch.object(
        client, "_start_commit_thread", autospec=True
    ) as _start_commit_thread:
        # First publish should create a commit thread.
        assert client.publish("topic", b"bytestring body", ordering_key="") is not None
        _start_commit_thread.assert_called_once()

        # Since _start_commit_thread is a mock, no actual thread has been
        # created, so let's put a sentinel there to mimic real behavior.
        client._commit_thread = mock.Mock()

        # Second publish should not create a commit thread since one (the mock)
        # already exists.
        assert client.publish("topic", b"bytestring body", ordering_key="") is not None
        # Call count should remain 1.
        _start_commit_thread.assert_called_once()


def test_commit_thread_not_created_on_publish_if_max_latency_is_inf(creds):
    # Max latency is infinite so a commit thread is not created.
    batch_settings = types.BatchSettings(max_latency=float("inf"))
    client = publisher.Client(batch_settings=batch_settings, credentials=creds)

    assert client.publish("topic", b"bytestring body", ordering_key="") is not None
    assert client._commit_thread is None


def test_wait_and_commit_sequencers(creds):
    # Max latency is infinite so a commit thread is not created.
    # We don't want a commit thread to interfere with this test.
    batch_settings = types.BatchSettings(max_latency=float("inf"))
    client = publisher.Client(batch_settings=batch_settings, credentials=creds)

    # Mock out time so no sleep is actually done.
    with mock.patch.object(time, "sleep"):
        with mock.patch.object(client, "_commit_sequencers") as _commit_sequencers:
            assert (
                client.publish("topic", b"bytestring body", ordering_key="") is not None
            )
            # Call _wait_and_commit_sequencers to simulate what would happen if a
            # commit thread actually ran.
            client._wait_and_commit_sequencers()
            assert _commit_sequencers.call_count == 1


def test_stopped_client_does_not_commit_sequencers(creds):
    # Max latency is infinite so a commit thread is not created.
    # We don't want a commit thread to interfere with this test.
    batch_settings = types.BatchSettings(max_latency=float("inf"))
    client = publisher.Client(batch_settings=batch_settings, credentials=creds)

    # Mock out time so no sleep is actually done.
    with mock.patch.object(time, "sleep"):
        with mock.patch.object(client, "_commit_sequencers") as _commit_sequencers:
            assert (
                client.publish("topic", b"bytestring body", ordering_key="") is not None
            )

            client.stop()

            # Call _wait_and_commit_sequencers to simulate what would happen if a
            # commit thread actually ran after the client was stopped.
            client._wait_and_commit_sequencers()
            # Should not be called since Client is stopped.
            assert _commit_sequencers.call_count == 0


def test_publish_with_ordering_key(creds):
    publisher_options = types.PublisherOptions(enable_message_ordering=True)
    client = publisher.Client(publisher_options=publisher_options, credentials=creds)

    # Use a mock in lieu of the actual batch class.
    batch = mock.Mock(spec=client._batch_class)

    # Set the mock up to claim indiscriminately that it accepts all messages.
    future1 = mock.sentinel.future1
    future2 = mock.sentinel.future2
    future1.add_done_callback = mock.Mock(spec=["__call__"])
    future2.add_done_callback = mock.Mock(spec=["__call__"])

    batch.publish.side_effect = (future1, future2)

    topic = "topic/path"
    ordering_key = "k1"
    client._set_batch(topic, batch, ordering_key=ordering_key)

    # Begin publishing.
    future1 = client.publish(topic, b"spam", ordering_key=ordering_key)
    future2 = client.publish(topic, b"foo", bar="baz", ordering_key=ordering_key)

    assert future1 is mock.sentinel.future1
    assert future2 is mock.sentinel.future2

    # Check mock.
    batch.publish.assert_has_calls(
        [
            mock.call(
                PublishMessageWrapper(
                    message=gapic_types.PubsubMessage(data=b"spam", ordering_key="k1")
                ),
            ),
            mock.call(
                PublishMessageWrapper(
                    message=gapic_types.PubsubMessage(
                        data=b"foo", attributes={"bar": "baz"}, ordering_key="k1"
                    )
                )
            ),
        ]
    )


def test_ordered_sequencer_cleaned_up(creds):
    # Max latency is infinite so a commit thread is not created.
    # We don't want a commit thread to interfere with this test.
    batch_settings = types.BatchSettings(max_latency=float("inf"))
    publisher_options = types.PublisherOptions(enable_message_ordering=True)
    client = publisher.Client(
        batch_settings=batch_settings,
        publisher_options=publisher_options,
        credentials=creds,
    )

    topic = "topic"
    ordering_key = "ord_key"
    sequencer = mock.Mock(spec=ordered_sequencer.OrderedSequencer)
    sequencer.is_finished.return_value = False
    client._set_sequencer(topic=topic, sequencer=sequencer, ordering_key=ordering_key)

    assert len(client._sequencers) == 1
    # 'sequencer' is not finished yet so don't remove it.
    client._commit_sequencers()
    assert len(client._sequencers) == 1

    sequencer.is_finished.return_value = True
    # 'sequencer' is finished so remove it.
    client._commit_sequencers()
    assert len(client._sequencers) == 0


def test_resume_publish(creds):
    publisher_options = types.PublisherOptions(enable_message_ordering=True)
    client = publisher.Client(publisher_options=publisher_options, credentials=creds)

    topic = "topic"
    ordering_key = "ord_key"
    sequencer = mock.Mock(spec=ordered_sequencer.OrderedSequencer)
    client._set_sequencer(topic=topic, sequencer=sequencer, ordering_key=ordering_key)

    client.resume_publish(topic, ordering_key)
    sequencer.unpause.assert_called_once()


def test_resume_publish_no_sequencer_found(creds):
    publisher_options = types.PublisherOptions(enable_message_ordering=True)
    client = publisher.Client(publisher_options=publisher_options, credentials=creds)

    # Check no exception is thrown if a sequencer with the (topic, ordering_key)
    # pair does not exist.
    client.resume_publish("topic", "ord_key")


def test_resume_publish_ordering_keys_not_enabled(creds):
    publisher_options = types.PublisherOptions(enable_message_ordering=False)
    client = publisher.Client(publisher_options=publisher_options, credentials=creds)

    # Throw on calling resume_publish() when enable_message_ordering is False.
    with pytest.raises(ValueError):
        client.resume_publish("topic", "ord_key")
