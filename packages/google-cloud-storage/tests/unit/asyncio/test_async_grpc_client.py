# Copyright 2025 Google LLC
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

import pytest
from google.api_core import client_info as client_info_lib
from google.api_core import client_options
from google.auth import credentials as auth_credentials
from google.auth.credentials import AnonymousCredentials

from google.cloud.storage import __version__
from google.cloud.storage.asyncio import async_grpc_client


def _make_credentials(spec=None):
    if spec is None:
        return mock.Mock(spec=auth_credentials.Credentials)
    return mock.Mock(spec=spec)


class TestAsyncGrpcClient:
    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_constructor_default_options(self, mock_async_storage_client):
        # Arrange
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        # Act
        async_grpc_client.AsyncGrpcClient(credentials=mock_creds)

        # Assert
        mock_async_storage_client.get_transport_class.assert_called_once_with(
            "grpc_asyncio"
        )
        kwargs = mock_async_storage_client.call_args.kwargs
        client_info = kwargs["client_info"]
        agent_version = f"gcloud-python/{__version__}"
        assert agent_version in client_info.user_agent
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=True,
            credentials=mock_creds,
            options=expected_options,
        )
        mock_channel = mock_transport_cls.create_channel.return_value
        mock_transport_cls.assert_called_once_with(channel=mock_channel)
        mock_transport = mock_transport_cls.return_value
        assert kwargs["transport"] is mock_transport
        assert kwargs["client_options"] is None

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_constructor_with_client_info(self, mock_async_storage_client):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()
        client_info = client_info_lib.ClientInfo(
            client_library_version="1.2.3",
        )

        async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds, client_info=client_info
        )

        agent_version = f"gcloud-python/{__version__}"
        assert agent_version in client_info.user_agent
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=True,
            credentials=mock_creds,
            options=expected_options,
        )

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_constructor_with_quota_project_and_endpoint(
        self, mock_async_storage_client
    ):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        from google.api_core import client_options

        mock_client_options = client_options.ClientOptions(
            api_endpoint="custom-endpoint.com", quota_project_id="my-quota-project"
        )

        async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds, client_options=mock_client_options
        )

        kwargs = mock_async_storage_client.call_args.kwargs
        client_info = kwargs["client_info"]
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="custom-endpoint.com",
            quota_project_id="my-quota-project",
            attempt_direct_path=True,
            credentials=mock_creds,
            options=expected_options,
        )

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_constructor_disables_directpath(self, mock_async_storage_client):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds, attempt_direct_path=False
        )

        kwargs = mock_async_storage_client.call_args.kwargs
        client_info = kwargs["client_info"]
        agent_version = f"gcloud-python/{__version__}"
        assert agent_version in client_info.user_agent
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=False,
            credentials=mock_creds,
            options=expected_options,
        )
        mock_channel = mock_transport_cls.create_channel.return_value
        mock_transport_cls.assert_called_once_with(channel=mock_channel)

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_metrics_properties(self, mock_async_storage_client):
        from google.cloud.storage import _opentelemetry_metrics

        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ):
            client = async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                enable_metrics=True,
                enable_debug_metrics=True,
            )
            assert client.metrics_enabled is True
            assert client.debug_metrics_enabled is True

            client_base_false = async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                enable_metrics=False,
                enable_debug_metrics=True,
            )
            assert client_base_false.metrics_enabled is False
            assert client_base_false.debug_metrics_enabled is True

            client_both_false = async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                enable_metrics=False,
                enable_debug_metrics=False,
            )
            assert client_both_false.metrics_enabled is False
            assert client_both_false.debug_metrics_enabled is False

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=False,
        ):
            client = async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                enable_metrics=True,
                enable_debug_metrics=True,
            )
            assert client.metrics_enabled is False
            assert client.debug_metrics_enabled is False

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_ctor_w_invalid_enable_metrics_raises_type_error(
        self, mock_async_storage_client
    ):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        with pytest.raises(TypeError):
            async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                enable_metrics="true",
            )
        with pytest.raises(TypeError):
            async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                enable_debug_metrics="true",
            )

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_ctor_metrics_defaults_and_env_fallback(self, mock_async_storage_client):
        from google.cloud.storage import _opentelemetry_metrics

        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        with mock.patch.multiple(
            _opentelemetry_metrics,
            HAS_OPENTELEMETRY_METRICS=True,
            _ENABLE_METRICS_DEV_GATE=True,
        ):
            with mock.patch.dict("os.environ", {}, clear=True):
                client = async_grpc_client.AsyncGrpcClient(credentials=mock_creds)
                assert client._enable_metrics is None
                assert client._enable_debug_metrics is None
                assert client.metrics_enabled is False
                assert client.debug_metrics_enabled is False

            with mock.patch.dict(
                "os.environ",
                {
                    "GCP_STORAGE_PYTHON_ENABLE_OTEL_METRICS": "true",
                    "GCP_STORAGE_PYTHON_ENABLE_OTEL_DEBUG_METRICS": "true",
                },
                clear=True,
            ):
                client = async_grpc_client.AsyncGrpcClient(credentials=mock_creds)
                assert client.metrics_enabled is True
                assert client.debug_metrics_enabled is True

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_grpc_client_property(self, mock_grpc_gapic_client):
        # Arrange
        mock_transport_cls = mock.MagicMock()
        mock_grpc_gapic_client.get_transport_class.return_value = mock_transport_cls
        channel_sentinel = mock.sentinel.channel
        mock_transport_cls.create_channel.return_value = channel_sentinel
        mock_transport_instance = mock.sentinel.transport
        mock_transport_cls.return_value = mock_transport_instance

        mock_creds = _make_credentials()
        # Use a real ClientInfo instance instead of a mock to properly test user agent logic
        client_info = client_info_lib.ClientInfo(user_agent="test-user-agent")
        mock_client_options = mock.sentinel.client_options
        mock_attempt_direct_path = mock.sentinel.attempt_direct_path

        # Act
        client = async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds,
            client_info=client_info,
            client_options=mock_client_options,
            attempt_direct_path=mock_attempt_direct_path,
        )
        retrieved_client = client.grpc_client  # This is what is being tested

        # Assert - verify that gcloud-python agent version was added
        agent_version = f"gcloud-python/{__version__}"
        assert agent_version in client_info.user_agent
        # Also verify original user_agent is still there
        assert "test-user-agent" in client_info.user_agent

        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=mock_attempt_direct_path,
            credentials=mock_creds,
            options=expected_options,
        )
        mock_transport_cls.assert_called_once_with(channel=channel_sentinel)
        mock_grpc_gapic_client.assert_called_once_with(
            transport=mock_transport_instance,
            client_info=client_info,
            client_options=mock_client_options,
        )
        assert retrieved_client is mock_grpc_gapic_client.return_value

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    @mock.patch(
        "google.cloud.storage.asyncio.async_grpc_client.grpc.aio.insecure_channel"
    )
    def test_grpc_client_with_anon_creds(
        self, mock_insecure_channel, mock_async_storage_client
    ):
        # Arrange
        mock_channel = mock.MagicMock()
        mock_insecure_channel.return_value = mock_channel

        # Act
        client = async_grpc_client.AsyncGrpcClient(
            client_options=client_options.ClientOptions(
                api_endpoint="my-grpc-endpoint"
            ),
            credentials=AnonymousCredentials(),
        )

        # Assert
        assert client.grpc_client is mock_async_storage_client.return_value
        mock_insecure_channel.assert_called_once_with("my-grpc-endpoint")

        kwargs = mock_async_storage_client.call_args.kwargs
        transport = kwargs["transport"]
        assert isinstance(transport._credentials, AnonymousCredentials)

    def test_grpc_client_with_anon_creds_no_client_options(self):
        # Act & Assert
        message = "Either client_options or `client_option.api_endpoint` is None. Please provide api_endpoint when `AnonymousCredentials` is used "
        with pytest.raises(ValueError, match=message):
            async_grpc_client.AsyncGrpcClient(
                credentials=AnonymousCredentials(),
            )

    def test_grpc_client_with_anon_creds_empty_client_options(self):
        # Act & Assert
        message = "Either client_options or `client_option.api_endpoint` is None. Please provide api_endpoint when `AnonymousCredentials` is used "
        with pytest.raises(ValueError, match=message):
            async_grpc_client.AsyncGrpcClient(
                client_options=client_options.ClientOptions(),
                credentials=AnonymousCredentials(),
            )

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_user_agent_with_custom_client_info(self, mock_async_storage_client):
        """Test that gcloud-python user agent is appended to existing user agent.

        Regression test similar to test__http.py::TestConnection::test_duplicate_user_agent
        """
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        # Create a client_info with an existing user_agent
        client_info = client_info_lib.ClientInfo(user_agent="custom-app/1.0")

        # Act
        async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds,
            client_info=client_info,
        )

        # Assert - verify that gcloud-python version was appended
        agent_version = f"gcloud-python/{__version__}"
        expected_user_agent = f"custom-app/1.0 {agent_version} "
        assert client_info.user_agent == expected_user_agent

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    @pytest.mark.asyncio
    async def test_delete_object(self, mock_async_storage_client):
        # Arrange
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_gapic_client = mock.AsyncMock()
        mock_async_storage_client.return_value = mock_gapic_client

        client = async_grpc_client.AsyncGrpcClient(credentials=_make_credentials())

        bucket_name = "bucket"
        object_name = "object"
        generation = 123
        if_generation_match = 456
        if_generation_not_match = 789
        if_metageneration_match = 111
        if_metageneration_not_match = 222

        # New parameters
        metadata = (("x-goog-api-client", "test-ua"),)
        timeout = 10.0
        retry = mock.Mock()

        # Act
        await client.delete_object(
            bucket_name,
            object_name,
            generation=generation,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            metadata=metadata,
            timeout=timeout,
            retry=retry,
        )

        # Assert
        call_args, call_kwargs = mock_gapic_client.delete_object.call_args
        request = call_kwargs["request"]
        assert request.bucket == "projects/_/buckets/bucket"
        assert request.object == "object"
        assert request.generation == generation
        assert request.if_generation_match == if_generation_match
        assert request.if_generation_not_match == if_generation_not_match
        assert request.if_metageneration_match == if_metageneration_match
        assert request.if_metageneration_not_match == if_metageneration_not_match
        assert call_kwargs["metadata"] == metadata
        assert call_kwargs["timeout"] == timeout
        assert call_kwargs["retry"] == retry

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    @pytest.mark.asyncio
    async def test_get_object(self, mock_async_storage_client):
        # Arrange
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_gapic_client = mock.AsyncMock()
        mock_async_storage_client.return_value = mock_gapic_client

        client = async_grpc_client.AsyncGrpcClient(credentials=_make_credentials())

        bucket_name = "bucket"
        object_name = "object"

        # Act
        await client.get_object(
            bucket_name,
            object_name,
        )

        # Assert
        call_args, call_kwargs = mock_gapic_client.get_object.call_args
        request = call_kwargs["request"]
        assert request.bucket == "projects/_/buckets/bucket"
        assert request.object == "object"
        assert request.soft_deleted is False

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    @pytest.mark.asyncio
    async def test_get_object_with_all_parameters(self, mock_async_storage_client):
        # Arrange
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_gapic_client = mock.AsyncMock()
        mock_async_storage_client.return_value = mock_gapic_client

        client = async_grpc_client.AsyncGrpcClient(credentials=_make_credentials())

        bucket_name = "bucket"
        object_name = "object"
        generation = 123
        if_generation_match = 456
        if_generation_not_match = 789
        if_metageneration_match = 111
        if_metageneration_not_match = 222
        soft_deleted = True

        # New parameters
        metadata = (("x-goog-api-client", "test-ua"),)
        timeout = 10.0
        retry = mock.Mock()

        # Act
        await client.get_object(
            bucket_name,
            object_name,
            generation=generation,
            if_generation_match=if_generation_match,
            if_generation_not_match=if_generation_not_match,
            if_metageneration_match=if_metageneration_match,
            if_metageneration_not_match=if_metageneration_not_match,
            soft_deleted=soft_deleted,
            metadata=metadata,
            timeout=timeout,
            retry=retry,
        )

        # Assert
        call_args, call_kwargs = mock_gapic_client.get_object.call_args
        request = call_kwargs["request"]
        assert request.bucket == "projects/_/buckets/bucket"
        assert request.object == "object"
        assert request.generation == generation
        assert request.if_generation_match == if_generation_match
        assert request.if_generation_not_match == if_generation_not_match
        assert request.if_metageneration_match == if_metageneration_match
        assert request.if_metageneration_not_match == if_metageneration_not_match
        assert request.soft_deleted is True
        assert call_kwargs["metadata"] == metadata
        assert call_kwargs["timeout"] == timeout
        assert call_kwargs["retry"] == retry

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "invalid_metadata, expected_exc",
        [
            ("not-a-sequence", TypeError),
            ([("key_only",)], ValueError),
            ([("too", "many", "items")], ValueError),
            ([(123, "val")], TypeError),
            ([("key", 456)], TypeError),
        ],
    )
    async def test_delete_object_invalid_metadata(self, invalid_metadata, expected_exc):
        client = async_grpc_client.AsyncGrpcClient(credentials=_make_credentials())
        with pytest.raises(expected_exc):
            await client.delete_object("bucket", "object", metadata=invalid_metadata)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "invalid_metadata, expected_exc",
        [
            ("not-a-sequence", TypeError),
            ([("key_only",)], ValueError),
            ([("too", "many", "items")], ValueError),
            ([(123, "val")], TypeError),
            ([("key", 456)], TypeError),
        ],
    )
    async def test_get_object_invalid_metadata(self, invalid_metadata, expected_exc):
        client = async_grpc_client.AsyncGrpcClient(credentials=_make_credentials())
        with pytest.raises(expected_exc):
            await client.get_object("bucket", "object", metadata=invalid_metadata)

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_async_grpc_client_attempt_direct_path_xds_over_interconnect(
        self, mock_async_storage_client
    ):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds,
            attempt_direct_path_xds_over_interconnect=True,
        )

        kwargs = mock_async_storage_client.call_args.kwargs
        client_info = kwargs["client_info"]
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage-direct.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=True,
            attempt_direct_path_xds_over_interconnect=True,
            credentials=mock_creds,
            options=expected_options,
        )

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_create_gapic_client_custom_client_options_with_interconnect(
        self, mock_async_storage_client
    ):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        client_options_obj = client_options.ClientOptions(
            api_endpoint="custom.endpoint.com",
            quota_project_id="my-quota-proj",
        )
        async_grpc_client.AsyncGrpcClient(
            credentials=mock_creds,
            client_options=client_options_obj,
            attempt_direct_path_xds_over_interconnect=True,
        )

        kwargs = mock_async_storage_client.call_args.kwargs
        client_info = kwargs["client_info"]
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="custom.endpoint.com",
            quota_project_id="my-quota-proj",
            attempt_direct_path=True,
            attempt_direct_path_xds_over_interconnect=True,
            credentials=mock_creds,
            options=expected_options,
        )

    @mock.patch("google.cloud._storage_v2.StorageAsyncClient")
    def test_async_grpc_client_interconnect_env_override(
        self, mock_async_storage_client
    ):
        mock_transport_cls = mock.MagicMock()
        mock_async_storage_client.get_transport_class.return_value = mock_transport_cls
        mock_creds = _make_credentials()

        with mock.patch.dict(
            "os.environ",
            {"GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT": "true"},
        ):
            async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                attempt_direct_path=False,
                attempt_direct_path_xds_over_interconnect=False,
            )

        kwargs = mock_async_storage_client.call_args.kwargs
        client_info = kwargs["client_info"]
        primary_user_agent = client_info.to_user_agent()
        expected_options = (("grpc.primary_user_agent", primary_user_agent),)

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage-direct.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=True,
            attempt_direct_path_xds_over_interconnect=True,
            credentials=mock_creds,
            options=expected_options,
        )

        mock_transport_cls.create_channel.reset_mock()
        with mock.patch.dict(
            "os.environ",
            {"GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT": " FALSE "},
        ):
            async_grpc_client.AsyncGrpcClient(
                credentials=mock_creds,
                attempt_direct_path_xds_over_interconnect=True,
            )

        mock_transport_cls.create_channel.assert_called_once_with(
            host="storage.googleapis.com",
            quota_project_id=None,
            attempt_direct_path=True,
            credentials=mock_creds,
            options=expected_options,
        )

        with mock.patch.dict(
            "os.environ",
            {"GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS_OVER_INTERCONNECT": "invalid"},
        ):
            with pytest.raises(ValueError):
                async_grpc_client.AsyncGrpcClient(credentials=mock_creds)
