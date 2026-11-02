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
from unittest import mock

import grpc
import pytest
from google.api_core.gapic_v1.client_info import METRICS_METADATA_KEY

from google.cloud.pubsub_v1 import subscriber, types
from google.cloud.pubsub_v1.open_telemetry.context_propagation import (
    OpenTelemetryContextGetter,
)
from google.cloud.pubsub_v1.subscriber import futures
from google.pubsub_v1.services.subscriber import client as subscriber_client
from google.pubsub_v1.services.subscriber.transports.grpc import SubscriberGrpcTransport
from google.pubsub_v1.types import PubsubMessage


# Attempt to use `_thunk` to obtain the underlying grpc channel from
# the intercept channel. Default to obtaining the grpc channel directly
# for backwards compatibility.
# TODO(https://github.com/grpc/grpc/issues/38519): Workaround to obtain a channel
# until a public API is available.
def get_pull_channel(client):
    try:
        return client._transport.pull._thunk("")._channel
    except AttributeError:
        return client._transport.pull._channel


def test_init_default_client_info(creds):
    client = subscriber.Client(credentials=creds)

    installed_version = subscriber.client.__version__
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


def test_init_default_closed_state(creds):
    client = subscriber.Client(credentials=creds)
    assert not client.closed


def test_init_w_custom_transport(creds):
    transport = SubscriberGrpcTransport(credentials=creds)
    client = subscriber.Client(transport=transport)
    assert client._transport is transport


def test_init_w_api_endpoint(creds):
    client_options = {"api_endpoint": "testendpoint.google.com"}
    client = subscriber.Client(client_options=client_options, credentials=creds)

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
    client = subscriber.Client(client_options={}, credentials=creds)
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

    with mock.patch.object(subscriber_client.SubscriberClient, "__init__", init):
        client = subscriber.Client(
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
    monkeypatch.setenv("PUBSUB_EMULATOR_HOST", "/baz/bacon:123")
    # NOTE: When the emulator host is set, a custom channel will be used, so
    #       no credentials (mock ot otherwise) can be passed in.
    client = subscriber.Client()

    # Establish that a gRPC request would attempt to hit the emulator host.
    #
    # Sadly, there seems to be no good way to do this without poking at
    # the private API of gRPC.
    channel = get_pull_channel(client)
    # Behavior to include dns prefix changed in gRPCv1.63
    grpc_major, grpc_minor = [int(part) for part in grpc.__version__.split(".")[0:2]]
    if grpc_major > 1 or (grpc_major == 1 and grpc_minor >= 63):
        _EXPECTED_TARGET = "dns:////baz/bacon:123"
    else:
        _EXPECTED_TARGET = "/baz/bacon:123"
    assert channel.target().decode("utf8") == _EXPECTED_TARGET


def test_class_method_factory():
    patch = mock.patch(
        "google.oauth2.service_account.Credentials.from_service_account_file"
    )

    with patch:
        client = subscriber.Client.from_service_account_file("filename.json")

    assert isinstance(client, subscriber.Client)


@mock.patch(
    "google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager."
    "StreamingPullManager.open",
    autospec=True,
)
def test_subscribe(manager_open, creds):
    client = subscriber.Client(credentials=creds)

    future = client.subscribe("sub_name_a", callback=mock.sentinel.callback)
    assert isinstance(future, futures.StreamingPullFuture)

    manager = future._StreamingPullFuture__manager
    assert manager._subscription == "sub_name_a"
    manager_open.assert_called_once_with(
        mock.ANY,
        callback=mock.sentinel.callback,
        on_callback_error=future.set_exception,
    )


@mock.patch(
    "google.cloud.pubsub_v1.subscriber._protocol.streaming_pull_manager."
    "StreamingPullManager.open",
    autospec=True,
)
def test_subscribe_options(manager_open, creds):
    client = subscriber.Client(credentials=creds)
    flow_control = types.FlowControl(max_bytes=42)
    scheduler = mock.sentinel.scheduler

    future = client.subscribe(
        "sub_name_a",
        callback=mock.sentinel.callback,
        flow_control=flow_control,
        scheduler=scheduler,
        await_callbacks_on_shutdown=mock.sentinel.await_callbacks,
    )
    assert isinstance(future, futures.StreamingPullFuture)

    manager = future._StreamingPullFuture__manager
    assert manager._subscription == "sub_name_a"
    assert manager.flow_control == flow_control
    assert manager._scheduler == scheduler
    assert manager._await_callbacks_on_shutdown is mock.sentinel.await_callbacks
    manager_open.assert_called_once_with(
        mock.ANY,
        callback=mock.sentinel.callback,
        on_callback_error=future.set_exception,
    )


def test_close(creds):
    client = subscriber.Client(credentials=creds)
    patcher = mock.patch.object(client._transport.grpc_channel, "close")

    with patcher as patched_close:
        client.close()

    patched_close.assert_called()
    assert client.closed


def test_closes_channel_as_context_manager(creds):
    client = subscriber.Client(credentials=creds)
    patcher = mock.patch.object(client._transport.grpc_channel, "close")

    with patcher as patched_close:
        with client:
            pass

    patched_close.assert_called()


def test_context_manager_raises_if_closed(creds):
    client = subscriber.Client(credentials=creds)

    with mock.patch.object(client._transport.grpc_channel, "close"):
        client.close()

    expetect_msg = r"(?i).*closed.*cannot.*context manager.*"
    with pytest.raises(RuntimeError, match=expetect_msg):
        with client:
            pass  # pragma: NO COVER


def test_api_property_deprecated(creds):
    client = subscriber.Client(credentials=creds)

    with pytest.warns(DeprecationWarning, match="client.api") as warned:
        client.api

    assert len(warned) == 1
    assert issubclass(warned[0].category, DeprecationWarning)
    warning_msg = str(warned[0].message)
    assert "client.api" in warning_msg


def test_api_property_proxy_to_generated_client(creds):
    client = subscriber.Client(credentials=creds)

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

    # The close() method only exists on the hand-written wrapper class.
    assert hasattr(client, "close")
    assert not hasattr(api_object, "close")


def test_streaming_pull_gapic_monkeypatch(creds):
    client = subscriber.Client(credentials=creds)

    with mock.patch("google.api_core.gapic_v1.method.wrap_method"):
        client.streaming_pull(requests=iter([]))

    transport = client._transport
    assert hasattr(transport.streaming_pull, "_prefetch_first_result_")
    assert not transport.streaming_pull._prefetch_first_result_


def test_sync_pull_warning_if_return_immediately(creds):
    client = subscriber.Client(credentials=creds)
    subscription_path = "projects/foo/subscriptions/bar"

    with (
        mock.patch.object(client._transport, "_wrapped_methods"),
        pytest.warns(
            DeprecationWarning,
            match="The return_immediately flag is deprecated and should be set to False",
        ) as warned,
    ):
        client.pull(subscription=subscription_path, return_immediately=True)

    # Setting the deprecated return_immediately flag to True should emit a warning.
    assert len(warned) == 1
    assert issubclass(warned[0].category, DeprecationWarning)
    warning_msg = str(warned[0].message)
    assert "return_immediately" in warning_msg
    assert "deprecated" in warning_msg


@pytest.mark.asyncio
async def test_sync_pull_warning_if_return_immediately_async(creds):
    from google.pubsub_v1.services.subscriber.async_client import SubscriberAsyncClient

    client = SubscriberAsyncClient(credentials=creds)
    subscription_path = "projects/foo/subscriptions/bar"

    patcher = mock.patch.object(
        type(client.transport.pull),
        "__call__",
        new_callable=mock.AsyncMock,
    )

    with (
        patcher,
        pytest.warns(
            DeprecationWarning,
            match="The return_immediately flag is deprecated and should be set to False",
        ) as warned,
    ):
        await client.pull(subscription=subscription_path, return_immediately=True)

    # Setting the deprecated return_immediately flag to True should emit a warning.
    assert len(warned) == 1
    assert issubclass(warned[0].category, DeprecationWarning)
    warning_msg = str(warned[0].message)
    assert "return_immediately" in warning_msg
    assert "deprecated" in warning_msg


@pytest.mark.parametrize(
    "enable_open_telemetry",
    [
        True,
        False,
    ],
)
def test_opentelemetry_subscriber_setting(creds, enable_open_telemetry):
    options = types.SubscriberOptions(
        enable_open_telemetry_tracing=enable_open_telemetry,
    )
    client = subscriber.Client(credentials=creds, subscriber_options=options)
    assert client.subscriber_options == options
    assert client._open_telemetry_enabled == enable_open_telemetry


def test_opentelemetry_propagator_get():
    message = PubsubMessage(data=b"foo")
    message.attributes["key1"] = "value1"
    message.attributes["googclient_key2"] = "value2"

    assert OpenTelemetryContextGetter().get(message, "key2") == ["value2"]

    assert OpenTelemetryContextGetter().get(message, "key1") is None


def test_opentelemetry_propagator_keys():
    message = PubsubMessage(data=b"foo")
    message.attributes["key1"] = "value1"
    message.attributes["googclient_key2"] = "value2"

    assert sorted(OpenTelemetryContextGetter().keys(message)) == [
        "googclient_key2",
        "key1",
    ]
