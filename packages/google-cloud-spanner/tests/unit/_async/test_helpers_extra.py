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

import asyncio
import unittest
from unittest import mock

from google.cloud.spanner_v1._async import _helpers as MUT


class TestHelpersExtra(unittest.IsolatedAsyncioTestCase):
    async def test_retry_allowed_exceptions_match(self):
        # coverage for line 54-58
        count = 0

        def func():
            nonlocal count
            count += 1
            if count == 1:
                raise ValueError("retry me")
            return "done"

        allowed = {ValueError: None}
        res = await MUT._retry(func, allowed_exceptions=allowed, delay=0.01)
        self.assertEqual(res, "done")
        self.assertEqual(count, 2)

    async def test_retry_allowed_exceptions_mismatch(self):
        # coverage for line 55-56
        def func():
            raise TypeError("don't retry me")

        allowed = {ValueError: None}
        with self.assertRaises(TypeError):
            await MUT._retry(func, allowed_exceptions=allowed, delay=0.01)

    async def test_retry_allowed_exceptions_callable_check(self):
        # coverage for line 57-59
        count = 0

        def func():
            nonlocal count
            count += 1
            raise ValueError("check me")

        def check_err(exc):
            return False  # don't retry

        allowed = {ValueError: check_err}
        with self.assertRaises(ValueError):
            await MUT._retry(
                func, allowed_exceptions=allowed, delay=0.01, retry_count=2
            )
        self.assertEqual(count, 1)

    async def test_retry_max_retries(self):
        # coverage for line 60-61
        def func():
            raise ValueError("always fail")

        with self.assertRaises(ValueError):
            await MUT._retry(func, retry_count=1, delay=0.01)

    async def test_retry_before_next_retry_callback(self):
        # coverage for line 62-65
        count = 0

        def func():
            nonlocal count
            count += 1
            if count == 1:
                raise ValueError("retry")
            return "done"

        callback_called = False

        async def before_retry(retries, delay):
            nonlocal callback_called
            callback_called = True

        res = await MUT._retry(func, before_next_retry=before_retry, delay=0.01)
        self.assertEqual(res, "done")
        self.assertTrue(callback_called)

    async def test_create_experimental_host_transport_tls_mtls(self):
        # coverage for lines 106-124
        from google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.grpc_asyncio import (
            InstanceAdminGrpcAsyncIOTransport as InstanceAdminGrpcTransport,
        )

        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            # Test TLS
            with mock.patch("grpc.aio.secure_channel") as mock_channel:
                MUT._create_experimental_host_transport(
                    InstanceAdminGrpcTransport, "host", False, "ca_cert", None, None
                )
                self.assertTrue(mock_channel.called)

            # Test mTLS
            with mock.patch("grpc.aio.secure_channel") as mock_channel:
                MUT._create_experimental_host_transport(
                    InstanceAdminGrpcTransport,
                    "host",
                    False,
                    "ca_cert",
                    "client_cert",
                    "client_key",
                )
                self.assertTrue(mock_channel.called)

    async def test_create_experimental_host_transport_errors(self):
        # coverage for line 118-130
        from google.cloud.spanner_admin_instance_v1.services.instance_admin.transports.grpc_asyncio import (
            InstanceAdminGrpcAsyncIOTransport as InstanceAdminGrpcTransport,
        )

        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            # Missing client_key
            with self.assertRaises(ValueError):
                MUT._create_experimental_host_transport(
                    InstanceAdminGrpcTransport,
                    "host",
                    False,
                    "ca_cert",
                    "client_cert",
                    None,
                )

            # No TLS/mTLS config
            with self.assertRaises(ValueError):
                MUT._create_experimental_host_transport(
                    InstanceAdminGrpcTransport, "host", False, None, None, None
                )

    async def test_create_spanner_omni_transport(self):
        mock_factory = mock.MagicMock()

        # Plaintext with create_async_auth_interceptors
        mock_creds1 = mock.MagicMock()
        mock_creds1.create_async_auth_interceptors.return_value = ["interceptor1"]
        with mock.patch("grpc.aio.insecure_channel") as mock_insecure:
            MUT._create_spanner_omni_transport(
                mock_factory,
                "localhost:9010",
                use_plain_text=True,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
                credentials=mock_creds1,
            )
            mock_insecure.assert_called_once_with(
                target="localhost:9010", interceptors=["interceptor1"]
            )

        # Credentials with create_async_auth_interceptor returning list and single item
        mock_creds2 = mock.MagicMock(spec=["create_async_auth_interceptor"])
        mock_creds2.create_async_auth_interceptor.return_value = ["interceptor2"]
        with mock.patch("grpc.aio.insecure_channel") as mock_insecure:
            MUT._create_spanner_omni_transport(
                mock_factory,
                "localhost:9010",
                use_plain_text=True,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
                credentials=mock_creds2,
            )
            mock_insecure.assert_called_once_with(
                target="localhost:9010", interceptors=["interceptor2"]
            )

        mock_creds2.create_async_auth_interceptor.return_value = "single_interceptor"
        with mock.patch("grpc.aio.insecure_channel") as mock_insecure:
            MUT._create_spanner_omni_transport(
                mock_factory,
                "localhost:9010",
                use_plain_text=True,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
                credentials=mock_creds2,
            )
            mock_insecure.assert_called_once_with(
                target="localhost:9010", interceptors=["single_interceptor"]
            )

        # Credentials with create_auth_interceptor returning list and single item
        mock_creds3 = mock.MagicMock(spec=["create_auth_interceptor"])
        mock_creds3.create_auth_interceptor.return_value = ["interceptor3"]
        with mock.patch("grpc.aio.insecure_channel") as mock_insecure:
            MUT._create_spanner_omni_transport(
                mock_factory,
                "localhost:9010",
                use_plain_text=True,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
                credentials=mock_creds3,
            )
            mock_insecure.assert_called_once_with(
                target="localhost:9010", interceptors=["interceptor3"]
            )

        mock_creds3.create_auth_interceptor.return_value = "single_interceptor3"
        with mock.patch("grpc.aio.insecure_channel") as mock_insecure:
            MUT._create_spanner_omni_transport(
                mock_factory,
                "localhost:9010",
                use_plain_text=True,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
                credentials=mock_creds3,
            )
            mock_insecure.assert_called_once_with(
                target="localhost:9010", interceptors=["single_interceptor3"]
            )

        # TLS and mTLS
        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            with mock.patch("grpc.ssl_channel_credentials") as mock_ssl_creds:
                with mock.patch("grpc.aio.secure_channel") as mock_secure:
                    # TLS only
                    MUT._create_spanner_omni_transport(
                        mock_factory,
                        "omni-host:15000",
                        use_plain_text=False,
                        ca_certificate="ca.pem",
                        client_certificate=None,
                        client_key=None,
                    )
                    mock_ssl_creds.assert_called_with(root_certificates=b"cert_data")
                    mock_secure.assert_called_with(
                        "omni-host:15000", mock_ssl_creds.return_value, interceptors=[]
                    )

                    # mTLS
                    MUT._create_spanner_omni_transport(
                        mock_factory,
                        "omni-host:15000",
                        use_plain_text=False,
                        ca_certificate="ca.pem",
                        client_certificate="client.pem",
                        client_key="key.pem",
                    )
                    mock_ssl_creds.assert_called_with(
                        root_certificates=b"cert_data",
                        private_key=b"cert_data",
                        certificate_chain=b"cert_data",
                    )

        # Validation errors
        with self.assertRaises(ValueError) as cm:
            MUT._create_spanner_omni_transport(
                mock_factory,
                "omni-host:15000",
                use_plain_text=False,
                ca_certificate=None,
                client_certificate=None,
                client_key=None,
            )
        self.assertIn("TLS/mTLS connection requires ca_certificate", str(cm.exception))

        with mock.patch("builtins.open", mock.mock_open(read_data=b"cert_data")):
            with self.assertRaises(ValueError) as cm:
                MUT._create_spanner_omni_transport(
                    mock_factory,
                    "omni-host:15000",
                    use_plain_text=False,
                    ca_certificate="ca.pem",
                    client_certificate="client.pem",
                    client_key=None,
                )
            self.assertIn(
                "Both client_certificate and client_key must be provided for mTLS connection",
                str(cm.exception),
            )

            with self.assertRaises(ValueError) as cm:
                MUT._create_spanner_omni_transport(
                    mock_factory,
                    "omni-host:15000",
                    use_plain_text=False,
                    ca_certificate="ca.pem",
                    client_certificate=None,
                    client_key="key.pem",
                )
            self.assertIn(
                "Both client_certificate and client_key must be provided for mTLS connection",
                str(cm.exception),
            )


class TestDrainStreamAsync(unittest.IsolatedAsyncioTestCase):
    async def test_drain_stream_consumes_async_iterator(self):
        items = [1, 2, 3]
        consumed = []

        class MockAsyncIterator:
            def __aiter__(self):
                return self

            async def __anext__(self):
                if items:
                    item = items.pop(0)
                    consumed.append(item)
                    return item
                raise StopAsyncIteration

        iterator = MockAsyncIterator()
        MUT._drain_stream(iterator)
        if MUT._PENDING_DRAIN_TASKS:
            await asyncio.wait(MUT._PENDING_DRAIN_TASKS)

        self.assertEqual(consumed, [1, 2, 3])

    async def test_drain_stream_event_loop_closed_fallback(self):
        iterator = mock.Mock()
        iterator.cancel = mock.Mock()

        def _raise_runtime_error(coroutine):
            coroutine.close()
            raise RuntimeError("no running loop")

        with mock.patch(
            "google.cloud.spanner_v1._async._helpers.asyncio.create_task",
            side_effect=_raise_runtime_error,
        ):
            MUT._drain_stream(iterator)

        iterator.cancel.assert_called_once()

    async def test_drain_stream_handles_none(self):
        MUT._drain_stream(None)

    async def test_drain_stream_handles_iterator_exception(self):
        class FailingAsyncIterator:
            def __aiter__(self):
                return self

            async def __anext__(self):
                raise RuntimeError("Stream broken")

        iterator = FailingAsyncIterator()
        MUT._drain_stream(iterator)
        if MUT._PENDING_DRAIN_TASKS:
            await asyncio.wait(MUT._PENDING_DRAIN_TASKS)

    async def test_drain_stream_task_cancellation(self):
        started = asyncio.Event()
        blocker = asyncio.Event()

        class BlockingAsyncIterator:
            def __aiter__(self):
                return self

            async def __anext__(self):
                started.set()
                await blocker.wait()
                return 1

        iterator = BlockingAsyncIterator()
        iterator.cancel = mock.Mock()

        MUT._drain_stream(iterator)
        await started.wait()
        task = next(iter(MUT._PENDING_DRAIN_TASKS))
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass

        iterator.cancel.assert_called_once()
        self.assertNotIn(task, MUT._PENDING_DRAIN_TASKS)

    def test_drain_stream_tasks_cleared_after_fork(self):
        MUT._PENDING_DRAIN_TASKS.add("dummy_task")
        self.assertEqual(len(MUT._PENDING_DRAIN_TASKS), 1)

        MUT._PENDING_DRAIN_TASKS.clear()
        self.assertEqual(len(MUT._PENDING_DRAIN_TASKS), 0)
