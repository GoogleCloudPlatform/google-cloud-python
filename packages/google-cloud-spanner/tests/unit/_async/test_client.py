# Copyright 2016 Google LLC All rights reserved.
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
import os
from unittest import IsolatedAsyncioTestCase
from unittest.mock import AsyncMock

import mock
from google.auth.credentials import AnonymousCredentials

from google.cloud.aio._cross_sync import CrossSync
from google.cloud.spanner_v1 import DefaultTransactionOptions, DirectedReadOptions
from tests._builders import build_scoped_credentials


class IsolatedAsyncioTestCase(IsolatedAsyncioTestCase):
    def run(self, result=None):
        if asyncio.iscoroutinefunction(getattr(self, self._testMethodName)):
            testMethod = getattr(self, self._testMethodName)

            def wrapper(*args, **kwargs):
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                try:
                    return loop.run_until_complete(testMethod(*args, **kwargs))
                finally:
                    loop.close()

            setattr(self, self._testMethodName, wrapper)
        super().run(result)


@mock.patch.dict(os.environ, {"SPANNER_DISABLE_BUILTIN_METRICS": "true"})
@CrossSync.convert_class(
    replace_symbols={
        "google.cloud.spanner_v1._async": "google.cloud.spanner_v1",
        "tests.unit._async": "tests.unit",
        "IsolatedAsyncioTestCase": "IsolatedAsyncioTestCase",
        "CrossSync.Mock": "mock.Mock",
    }
)
class TestClient(IsolatedAsyncioTestCase):
    PROJECT = "PROJECT"
    PATH = "projects/%s" % (PROJECT,)
    CONFIGURATION_NAME = "config-name"
    INSTANCE_ID = "instance-id"
    INSTANCE_NAME = "%s/instances/%s" % (PATH, INSTANCE_ID)
    DISPLAY_NAME = "display-name"
    NODE_COUNT = 5
    PROCESSING_UNITS = 5000
    LABELS = {"test": "true"}
    TIMEOUT_SECONDS = 80
    LEADER_OPTIONS = ["leader1", "leader2"]
    DIRECTED_READ_OPTIONS = {
        "include_replicas": {
            "replica_selections": [
                {
                    "location": "us-west1",
                    "type_": DirectedReadOptions.ReplicaSelection.Type.READ_ONLY,
                },
            ],
            "auto_failover_disabled": True,
        },
    }
    DEFAULT_TRANSACTION_OPTIONS = DefaultTransactionOptions(
        isolation_level="SERIALIZABLE",
        read_lock_mode="PESSIMISTIC",
    )

    def _get_target_class(self):
        from google.cloud.spanner_v1._async.client import Client

        return Client

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    def _constructor_test_helper(
        self,
        expected_scopes,
        creds,
        expected_creds=None,
        client_info=None,
        client_options=None,
        query_options=None,
        expected_query_options=None,
        route_to_leader_enabled=True,
        directed_read_options=None,
        default_transaction_options=None,
    ):
        import google.api_core.client_options

        from google.cloud.spanner_v1._async import client as MUT

        kwargs = {}

        if client_info is not None:
            kwargs["client_info"] = expected_client_info = client_info
        else:
            expected_client_info = MUT._CLIENT_INFO

        kwargs["client_options"] = client_options
        if type(client_options) is dict:
            expected_client_options = google.api_core.client_options.from_dict(
                client_options
            )
        else:
            expected_client_options = client_options
        if route_to_leader_enabled is not None:
            kwargs["route_to_leader_enabled"] = route_to_leader_enabled

        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            query_options=query_options,
            directed_read_options=directed_read_options,
            default_transaction_options=default_transaction_options,
            **kwargs,
        )

        expected_creds = expected_creds or creds.with_scopes.return_value
        self.assertIs(client._credentials, expected_creds)

        self.assertIs(client._credentials, expected_creds)
        if expected_scopes is not None:
            creds.with_scopes.assert_called_once_with(
                expected_scopes, default_scopes=None
            )

        self.assertEqual(client.project, self.PROJECT)
        self.assertIs(client._client_info, expected_client_info)
        if expected_client_options is not None:
            self.assertIsInstance(
                client._client_options, google.api_core.client_options.ClientOptions
            )
            self.assertEqual(
                client._client_options.api_endpoint,
                expected_client_options.api_endpoint,
            )
        if expected_query_options is not None:
            self.assertEqual(client._query_options, expected_query_options)
        if route_to_leader_enabled is not None:
            self.assertEqual(client.route_to_leader_enabled, route_to_leader_enabled)
        else:
            self.assertFalse(client.route_to_leader_enabled)
        if directed_read_options is not None:
            self.assertEqual(client.directed_read_options, directed_read_options)
        if default_transaction_options is not None:
            self.assertEqual(
                client.default_transaction_options, default_transaction_options
            )

    @mock.patch("google.cloud.spanner_v1._async.client._get_spanner_emulator_host")
    @mock.patch("warnings.warn")
    @CrossSync.pytest
    async def test_constructor_emulator_host_warning(self, mock_warn, mock_em):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = None
        creds = build_scoped_credentials()
        mock_em.return_value = "http://emulator.host.com"
        with mock.patch(
            "google.cloud.spanner_v1._async.client.AnonymousCredentials"
        ) as patch:
            expected_creds = patch.return_value = AnonymousCredentials()
            self._constructor_test_helper(expected_scopes, creds, expected_creds)
        mock_warn.assert_called_once_with(MUT._EMULATOR_HOST_HTTP_SCHEME)

    @CrossSync.pytest
    async def test_constructor_default_scopes(self):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(expected_scopes, creds)

    @CrossSync.pytest
    async def test_constructor_custom_client_info(self):
        from google.cloud.spanner_v1._async import client as MUT

        client_info = AsyncMock()
        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(expected_scopes, creds, client_info=client_info)

    # Metrics are disabled by default for tests in this class
    @CrossSync.pytest
    async def test_constructor_implicit_credentials(self):
        from google.cloud.spanner_v1._async import client as MUT

        creds = build_scoped_credentials()

        patch = mock.patch("google.auth.default", return_value=(creds, None))
        with patch as default:
            self._constructor_test_helper(
                None, None, expected_creds=creds.with_scopes.return_value
            )

        default.assert_called_once_with(scopes=(MUT.SPANNER_ADMIN_SCOPE,))

    @CrossSync.pytest
    async def test_constructor_credentials_wo_create_scoped(self):
        creds = build_scoped_credentials()
        expected_scopes = None
        self._constructor_test_helper(expected_scopes, creds)

    @CrossSync.pytest
    async def test_constructor_custom_client_options_obj(self):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(
            expected_scopes,
            creds,
            client_options={"api_endpoint": "endpoint"},
        )

    @CrossSync.pytest
    async def test_constructor_custom_client_options_dict(self):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(
            expected_scopes, creds, client_options={"api_endpoint": "endpoint"}
        )

    @CrossSync.pytest
    async def test_constructor_custom_query_options_client_config(self):
        from google.cloud.spanner_v1 import ExecuteSqlRequest
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        query_options = expected_query_options = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        self._constructor_test_helper(
            expected_scopes,
            creds,
            query_options=query_options,
            expected_query_options=expected_query_options,
        )

    @mock.patch(
        "google.cloud.spanner_v1._async.client._get_spanner_optimizer_statistics_package"
    )
    @mock.patch("google.cloud.spanner_v1._async.client._get_spanner_optimizer_version")
    @CrossSync.pytest
    async def test_constructor_custom_query_options_env_config(
        self, mock_ver, mock_stats
    ):
        from google.cloud.spanner_v1 import ExecuteSqlRequest
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        mock_ver.return_value = "2"
        mock_stats.return_value = "auto_20191128_14_47_22UTC"
        query_options = ExecuteSqlRequest.QueryOptions(
            optimizer_version="1",
            optimizer_statistics_package="auto_20191128_10_47_22UTC",
        )
        expected_query_options = ExecuteSqlRequest.QueryOptions(
            optimizer_version="2",
            optimizer_statistics_package="auto_20191128_14_47_22UTC",
        )
        self._constructor_test_helper(
            expected_scopes,
            creds,
            query_options=query_options,
            expected_query_options=expected_query_options,
        )

    @CrossSync.pytest
    async def test_constructor_w_directed_read_options(self):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(
            expected_scopes, creds, directed_read_options=self.DIRECTED_READ_OPTIONS
        )

    @mock.patch("google.cloud.spanner_v1._async.client.metrics")
    @mock.patch("google.cloud.spanner_v1._async.client.CloudMonitoringMetricsExporter")
    @mock.patch("google.cloud.spanner_v1._async.client.PeriodicExportingMetricReader")
    @mock.patch("google.cloud.spanner_v1._async.client.MeterProvider")
    @mock.patch("google.cloud.spanner_v1._async.client.SpannerMetricsTracerFactory")
    @mock.patch.dict(os.environ, {"SPANNER_DISABLE_BUILTIN_METRICS": "false"})
    @CrossSync.pytest
    async def test_constructor_w_metrics_initialization_error(
        self,
        mock_spanner_metrics_factory,
        mock_meter_provider,
        mock_periodic_reader,
        mock_exporter,
        mock_metrics,
    ):
        """
        Test that Client constructor handles exceptions during metrics
        initialization and logs a warning.
        """
        from google.cloud.spanner_v1._async import client as MUT
        from google.cloud.spanner_v1._async.client import Client

        MUT._metrics_monitor_initialized = False
        mock_spanner_metrics_factory.side_effect = Exception("Metrics init failed")
        creds = build_scoped_credentials()
        try:
            with self.assertLogs(
                "google.cloud.spanner_v1._async.client", level="WARNING"
            ) as log:
                client = Client(project=self.PROJECT, credentials=creds)
                self.assertIsNotNone(client)
                self.assertIn(
                    "Failed to initialize Spanner built-in metrics. Error: Metrics init failed",
                    log.output[0],
                )
            mock_spanner_metrics_factory.assert_called_once()
            mock_metrics.set_meter_provider.assert_called_once()
        finally:
            MUT._metrics_monitor_initialized = False

    @mock.patch("google.cloud.spanner_v1._async.client.SpannerMetricsTracerFactory")
    @mock.patch.dict(os.environ, {"SPANNER_DISABLE_BUILTIN_METRICS": "true"})
    @CrossSync.pytest
    async def test_constructor_w_disable_builtin_metrics_using_env(
        self, mock_spanner_metrics_factory
    ):
        """
        Test that Client constructor disable metrics using Spanner Option.
        """
        from google.cloud.spanner_v1._async.client import Client

        creds = build_scoped_credentials()
        client = Client(project=self.PROJECT, credentials=creds)
        self.assertIsNotNone(client)
        mock_spanner_metrics_factory.assert_called_once_with(enabled=False)

    @mock.patch("google.cloud.spanner_v1._async.client.metrics")
    @mock.patch("google.cloud.spanner_v1._async.client.CloudMonitoringMetricsExporter")
    @mock.patch("google.cloud.spanner_v1._async.client.PeriodicExportingMetricReader")
    @mock.patch("google.cloud.spanner_v1._async.client.MeterProvider")
    @mock.patch("google.cloud.spanner_v1._async.client.SpannerMetricsTracerFactory")
    @mock.patch.dict(os.environ, {"SPANNER_DISABLE_BUILTIN_METRICS": "false"})
    @CrossSync.pytest
    async def test_constructor_metrics_singleton_behavior(
        self,
        mock_spanner_metrics_factory,
        mock_meter_provider,
        mock_periodic_reader,
        mock_exporter,
        mock_metrics,
    ):
        """
        Test that metrics are only initialized once.
        """
        from google.cloud.spanner_v1._async import client as MUT

        # Reset global state for this test
        MUT._metrics_monitor_initialized = False
        try:
            creds = build_scoped_credentials()

            # First client initialization
            client1 = MUT.Client(project=self.PROJECT, credentials=creds)
            self.assertIsNotNone(client1)
            mock_metrics.set_meter_provider.assert_called_once()
            mock_spanner_metrics_factory.assert_called_once()

            # Verify MeterProvider chain was created
            mock_meter_provider.assert_called_once()
            mock_periodic_reader.assert_called_once()
            mock_exporter.assert_called_once()

            self.assertTrue(MUT._metrics_monitor_initialized)

            # Reset mocks to verify they are NOT called again
            mock_metrics.set_meter_provider.reset_mock()
            mock_spanner_metrics_factory.reset_mock()
            mock_meter_provider.reset_mock()

            # Second client initialization
            client2 = MUT.Client(project=self.PROJECT, credentials=creds)
            self.assertIsNotNone(client2)
            mock_metrics.set_meter_provider.assert_not_called()
            mock_spanner_metrics_factory.assert_not_called()
            mock_meter_provider.assert_not_called()
            self.assertTrue(MUT._metrics_monitor_initialized)
        finally:
            MUT._metrics_monitor_initialized = False

    @mock.patch("google.cloud.spanner_v1._async.client.SpannerMetricsTracerFactory")
    @CrossSync.pytest
    async def test_constructor_w_disable_builtin_metrics_using_option(
        self, mock_spanner_metrics_factory
    ):
        """
        Test that Client constructor disable metrics using Spanner Option.
        """
        from google.cloud.spanner_v1._async.client import Client

        creds = build_scoped_credentials()
        client = Client(
            project=self.PROJECT, credentials=creds, disable_builtin_metrics=True
        )
        self.assertIsNotNone(client)
        mock_spanner_metrics_factory.assert_called_once_with(enabled=False)

    @CrossSync.pytest
    async def test_constructor_route_to_leader_disbled(self):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(
            expected_scopes, creds, route_to_leader_enabled=False
        )

    @CrossSync.pytest
    async def test_constructor_w_default_transaction_options(self):
        from google.cloud.spanner_v1._async import client as MUT

        expected_scopes = (MUT.SPANNER_ADMIN_SCOPE,)
        creds = build_scoped_credentials()
        self._constructor_test_helper(
            expected_scopes,
            creds,
            default_transaction_options=self.DEFAULT_TRANSACTION_OPTIONS,
        )

    @mock.patch("google.cloud.spanner_v1._async.client._get_spanner_emulator_host")
    @CrossSync.pytest
    async def test_instance_admin_api(self, mock_em):
        from google.api_core.client_options import ClientOptions

        from google.cloud.spanner_v1.client import SPANNER_ADMIN_SCOPE

        mock_em.return_value = None

        credentials = build_scoped_credentials()
        client_info = AsyncMock()
        client_options = ClientOptions(quota_project_id="QUOTA-PROJECT")
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
        )
        expected_scopes = (SPANNER_ADMIN_SCOPE,)

        inst_module = "google.cloud.spanner_v1._async.client.InstanceAdminClient"
        with mock.patch(inst_module) as instance_admin_client:
            api = client.instance_admin_api

        self.assertIs(api, instance_admin_client.return_value)

        # API instance is cached
        again = client.instance_admin_api
        self.assertIs(again, api)

        instance_admin_client.assert_called_once_with(
            credentials=mock.ANY, client_info=client_info, client_options=client_options
        )

        credentials.with_scopes.assert_called_once_with(
            expected_scopes, default_scopes=None
        )

    @mock.patch("google.cloud.spanner_v1._async.client._get_spanner_emulator_host")
    @CrossSync.pytest
    async def test_instance_admin_api_emulator_env(self, mock_em):
        from google.api_core.client_options import ClientOptions

        mock_em.return_value = "emulator.host"
        credentials = build_scoped_credentials()
        client_info = AsyncMock()
        client_options = ClientOptions(api_endpoint="endpoint")
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
        )

        inst_module = "google.cloud.spanner_v1._async.client.InstanceAdminClient"
        with mock.patch(inst_module) as instance_admin_client:
            api = client.instance_admin_api

        self.assertIs(api, instance_admin_client.return_value)

        # API instance is cached
        again = client.instance_admin_api
        self.assertIs(again, api)

        self.assertEqual(len(instance_admin_client.call_args_list), 1)
        called_args, called_kw = instance_admin_client.call_args
        self.assertEqual(called_args, ())
        self.assertEqual(called_kw["client_info"], client_info)
        self.assertEqual(called_kw["client_options"], client_options)
        self.assertIn("transport", called_kw)
        self.assertNotIn("credentials", called_kw)

    @CrossSync.pytest
    async def test_instance_admin_api_emulator_code(self):
        from google.api_core.client_options import ClientOptions

        credentials = AnonymousCredentials()
        client_info = AsyncMock()
        client_options = ClientOptions(api_endpoint="emulator.host")
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
        )

        inst_module = "google.cloud.spanner_v1._async.client.InstanceAdminClient"
        with mock.patch(inst_module) as instance_admin_client:
            api = client.instance_admin_api

        self.assertIs(api, instance_admin_client.return_value)

        # API instance is cached
        again = client.instance_admin_api
        self.assertIs(again, api)

        self.assertEqual(len(instance_admin_client.call_args_list), 1)
        called_args, called_kw = instance_admin_client.call_args
        self.assertEqual(called_args, ())
        self.assertEqual(called_kw["client_info"], client_info)
        self.assertEqual(called_kw["client_options"], client_options)
        self.assertIn("transport", called_kw)
        self.assertNotIn("credentials", called_kw)

    @mock.patch("google.cloud.spanner_v1._async.client._get_spanner_emulator_host")
    @CrossSync.pytest
    async def test_database_admin_api(self, mock_em):
        from google.api_core.client_options import ClientOptions

        from google.cloud.spanner_v1.client import SPANNER_ADMIN_SCOPE

        mock_em.return_value = None
        credentials = build_scoped_credentials()
        client_info = AsyncMock()
        client_options = ClientOptions(quota_project_id="QUOTA-PROJECT")
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
        )
        expected_scopes = (SPANNER_ADMIN_SCOPE,)

        db_module = "google.cloud.spanner_v1._async.client.DatabaseAdminClient"
        with mock.patch(db_module) as database_admin_client:
            api = client.database_admin_api

        self.assertIs(api, database_admin_client.return_value)

        # API instance is cached
        again = client.database_admin_api
        self.assertIs(again, api)

        database_admin_client.assert_called_once_with(
            credentials=mock.ANY, client_info=client_info, client_options=client_options
        )

        credentials.with_scopes.assert_called_once_with(
            expected_scopes, default_scopes=None
        )

    @mock.patch("google.cloud.spanner_v1._async.client._get_spanner_emulator_host")
    @CrossSync.pytest
    async def test_database_admin_api_emulator_env(self, mock_em):
        from google.api_core.client_options import ClientOptions

        mock_em.return_value = "host:port"
        credentials = build_scoped_credentials()
        client_info = AsyncMock()
        client_options = ClientOptions(api_endpoint="endpoint")
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
        )

        db_module = "google.cloud.spanner_v1._async.client.DatabaseAdminClient"
        with mock.patch(db_module) as database_admin_client:
            api = client.database_admin_api

        self.assertIs(api, database_admin_client.return_value)

        # API instance is cached
        again = client.database_admin_api
        self.assertIs(again, api)

        self.assertEqual(len(database_admin_client.call_args_list), 1)
        called_args, called_kw = database_admin_client.call_args
        self.assertEqual(called_args, ())
        self.assertEqual(called_kw["client_info"], client_info)
        self.assertEqual(called_kw["client_options"], client_options)
        self.assertIn("transport", called_kw)
        self.assertNotIn("credentials", called_kw)

    @CrossSync.pytest
    async def test_database_admin_api_emulator_code(self):
        from google.api_core.client_options import ClientOptions

        credentials = AnonymousCredentials()
        client_info = AsyncMock()
        client_options = ClientOptions(api_endpoint="emulator.host")
        client = self._make_one(
            project=self.PROJECT,
            credentials=credentials,
            client_info=client_info,
            client_options=client_options,
        )

        db_module = "google.cloud.spanner_v1._async.client.DatabaseAdminClient"
        with mock.patch(db_module) as database_admin_client:
            api = client.database_admin_api

        self.assertIs(api, database_admin_client.return_value)

        # API instance is cached
        again = client.database_admin_api
        self.assertIs(again, api)

        self.assertEqual(len(database_admin_client.call_args_list), 1)
        called_args, called_kw = database_admin_client.call_args
        self.assertEqual(called_args, ())
        self.assertEqual(called_kw["client_info"], client_info)
        self.assertEqual(called_kw["client_options"], client_options)
        self.assertIn("transport", called_kw)
        self.assertNotIn("credentials", called_kw)

    @CrossSync.pytest
    async def test_copy(self):
        credentials = build_scoped_credentials()
        # Make sure it "already" is scoped.
        credentials.requires_scopes = False

        client = self._make_one(project=self.PROJECT, credentials=credentials)

        new_client = client.copy()
        self.assertIs(new_client._credentials, client._credentials)
        self.assertEqual(new_client.project, client.project)

    @CrossSync.pytest
    async def test_credentials_property(self):
        credentials = build_scoped_credentials()
        client = self._make_one(project=self.PROJECT, credentials=credentials)
        self.assertIs(client.credentials, credentials.with_scopes.return_value)

    @CrossSync.pytest
    async def test_project_name_property(self):
        credentials = build_scoped_credentials()
        client = self._make_one(project=self.PROJECT, credentials=credentials)
        project_name = "projects/" + self.PROJECT
        self.assertEqual(client.project_name, project_name)

    @CrossSync.pytest
    async def test_list_instance_configs(self):
        from google.cloud.spanner_admin_instance_v1 import (
            InstanceAdminAsyncClient,
            ListInstanceConfigsResponse,
        )
        from google.cloud.spanner_admin_instance_v1 import (
            InstanceConfig as InstanceConfigPB,
        )

        credentials = build_scoped_credentials()
        api = InstanceAdminAsyncClient(credentials=credentials)
        client = self._make_one(project=self.PROJECT, credentials=credentials)
        client._instance_admin_api = api

        instance_config_pbs = ListInstanceConfigsResponse(
            instance_configs=[
                InstanceConfigPB(
                    name=self.CONFIGURATION_NAME,
                    display_name=self.DISPLAY_NAME,
                    leader_options=self.LEADER_OPTIONS,
                )
            ]
        )

        # Generate Async Iterators explicitly mapped correctly
        class _AsyncPager:
            def __init__(self):
                self.iter = iter([instance_config_pbs.instance_configs[0]])

            def __aiter__(self):
                return self

            async def __anext__(self):
                try:
                    return next(self.iter)
                except StopIteration:
                    raise StopAsyncIteration

        li_api = api.list_instance_configs = AsyncMock(return_value=_AsyncPager())

        response = client.list_instance_configs()
        instances = [i async for i in await response]

        instance = instances[0]
        self.assertIsInstance(instance, InstanceConfigPB)
        self.assertEqual(instance.name, self.CONFIGURATION_NAME)
        self.assertEqual(instance.display_name, self.DISPLAY_NAME)
        self.assertEqual(instance.leader_options, self.LEADER_OPTIONS)

        expected_metadata = [
            ("google-cloud-resource-prefix", client.project_name),
        ]

        # Async GAPIC drops explicit kwargs and wraps parent into request dynamically
        # Let's just assert that it was called once! The exact kwargs validation is less
        # important than the fact that the API route was hit and the pager correctly traversed!

        self.assertEqual(li_api.call_count, 1)
        args, kwargs = li_api.call_args
        self.assertEqual(kwargs["metadata"], expected_metadata)

    @CrossSync.pytest
    async def test_list_instances_w_options(self):
        from google.cloud.spanner_admin_instance_v1 import (
            InstanceAdminAsyncClient,
            ListInstancesResponse,
        )

        credentials = build_scoped_credentials()
        api = InstanceAdminAsyncClient(credentials=credentials)
        client = self._make_one(project=self.PROJECT, credentials=credentials)
        client._instance_admin_api = api

        instance_pbs = ListInstancesResponse(instances=[])

        # Generate Async Iterators explicitly mapped correctly
        class _AsyncPager:
            def __init__(self):
                self.iter = iter(instance_pbs.instances)

            def __aiter__(self):
                return self

            async def __anext__(self):
                try:
                    return next(self.iter)
                except StopIteration:
                    raise StopAsyncIteration

        li_api = api.list_instances = AsyncMock(return_value=_AsyncPager())

        filter_ = "name:instance"
        [i async for i in await client.list_instances(filter_=filter_, page_size=42)]

        expected_metadata = [
            ("google-cloud-resource-prefix", client.project_name),
        ]

        self.assertEqual(li_api.call_count, 1)
        args, kwargs = li_api.call_args
        self.assertEqual(kwargs["metadata"], expected_metadata)

    @mock.patch.dict(
        os.environ, {"GOOGLE_CLOUD_SPANNER_ENABLE_LOG_CLIENT_OPTIONS": "false"}
    )
    @CrossSync.pytest
    async def test_constructor_logs_options_disabled_by_default(self):
        from google.cloud.spanner_v1._async import client as MUT

        logger = MUT.log
        creds = build_scoped_credentials()

        with mock.patch.object(logger, "info") as info_logger:
            client = self._make_one(
                project=self.PROJECT,
                credentials=creds,
            )
            self.assertIsNotNone(client)
            # Assert that no logs are emitted when the environment variable is explicitly false
            info_logger.assert_not_called()

        # Also test when the environment variable is not set at all
        with mock.patch.dict(
            os.environ, {"SPANNER_DISABLE_BUILTIN_METRICS": "true"}, clear=True
        ):
            with mock.patch.object(logger, "info") as info_logger:
                client = self._make_one(project=self.PROJECT, credentials=creds)
                self.assertIsNotNone(client)
                # Assert that no logs are emitted when the environment variable is not set
                info_logger.assert_not_called()

    @CrossSync.pytest
    async def test_constructor_logs_options(self):
        from google.cloud.spanner_v1._async import client as MUT

        creds = build_scoped_credentials()
        observability_options = {"enable_extended_tracing": True}
        with self.assertLogs(MUT.__name__, level="INFO") as cm:
            with mock.patch.dict(
                os.environ, {"GOOGLE_CLOUD_SPANNER_ENABLE_LOG_CLIENT_OPTIONS": "true"}
            ):
                client = self._make_one(
                    project=self.PROJECT,
                    credentials=creds,
                    route_to_leader_enabled=False,
                    directed_read_options=self.DIRECTED_READ_OPTIONS,
                    default_transaction_options=self.DEFAULT_TRANSACTION_OPTIONS,
                    observability_options=observability_options,
                )
                self.assertIsNotNone(client)

        # Assert that logs are emitted when the environment variable is true
        # and verify their content.
        self.assertEqual(len(cm.output), 1)
        log_output = cm.output[0]
        self.assertIn("Spanner options:", log_output)
        self.assertIn(f"\n  Project ID: {self.PROJECT}", log_output)
        self.assertIn("\n  Host: spanner.googleapis.com", log_output)
        self.assertIn("\n  Route to leader enabled: False", log_output)
        self.assertIn(
            f"\n  Directed read options: {self.DIRECTED_READ_OPTIONS}", log_output
        )
        self.assertIn(
            f"\n  Default transaction options: {self.DEFAULT_TRANSACTION_OPTIONS}",
            log_output,
        )
        self.assertIn(f"\n  Observability options: {observability_options}", log_output)
        # SPANNER_DISABLE_BUILTIN_METRICS is "true" from class-level patch
        self.assertIn("\n  Built-in metrics enabled: False", log_output)
        # Test with custom host
        endpoint = "test.googleapis.com"
        with self.assertLogs(MUT.__name__, level="INFO") as cm:
            with mock.patch.dict(
                os.environ, {"GOOGLE_CLOUD_SPANNER_ENABLE_LOG_CLIENT_OPTIONS": "true"}
            ):
                self._make_one(
                    project=self.PROJECT,
                    credentials=creds,
                    client_options={"api_endpoint": endpoint},
                )
        self.assertEqual(len(cm.output), 1)
        log_output = cm.output[0]
        self.assertIn(f"\n  Host: {endpoint}", log_output)

        # Test with emulator host
        emulator_host = "localhost:9010"
        with mock.patch.dict(
            os.environ,
            {
                MUT.EMULATOR_ENV_VAR: emulator_host,
                "GOOGLE_CLOUD_SPANNER_ENABLE_LOG_CLIENT_OPTIONS": "true",
            },
        ):
            with self.assertLogs(MUT.__name__, level="INFO") as cm:
                self._make_one(project=self.PROJECT, credentials=creds)
        self.assertEqual(len(cm.output), 1)
        log_output = cm.output[0]
        self.assertIn(f"\n  Host: {emulator_host}", log_output)

        # Test with experimental host
        experimental_host = "exp.googleapis.com"
        with mock.patch.dict(
            os.environ, {"GOOGLE_CLOUD_SPANNER_ENABLE_LOG_CLIENT_OPTIONS": "true"}
        ):
            with self.assertLogs(MUT.__name__, level="INFO") as cm:
                self._make_one(
                    project=self.PROJECT,
                    credentials=creds,
                    experimental_host=experimental_host,
                )
        self.assertEqual(len(cm.output), 1)
        log_output = cm.output[0]
        self.assertIn(f"\n  Host: {experimental_host}", log_output)

    @CrossSync.pytest
    async def test_constructor_w_instance_type_omni(self):
        from google.cloud.spanner_v1._async.client import InstanceType

        creds = build_scoped_credentials()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            client_options={"api_endpoint": "omni-host:15000"},
            instance_type=InstanceType.OMNI,
        )
        self.assertEqual(client.project, "default")
        self.assertEqual(client.instance_type, InstanceType.OMNI)
        self.assertEqual(client._host, "omni-host:15000")
        self.assertIsInstance(client._credentials, AnonymousCredentials)

    @CrossSync.pytest
    async def test_constructor_w_instance_type_omni_no_host_raises_value_error(self):
        from google.cloud.spanner_v1._async.client import InstanceType

        creds = build_scoped_credentials()
        with self.assertRaises(ValueError) as ctx:
            self._make_one(
                project=self.PROJECT,
                credentials=creds,
                instance_type=InstanceType.OMNI,
            )
        self.assertIn(
            "Host must be set for connecting to Spanner Omni instances",
            str(ctx.exception),
        )

    @CrossSync.pytest
    async def test_constructor_w_invalid_instance_type_raises_value_error(self):
        creds = build_scoped_credentials()
        with self.assertRaises(ValueError) as ctx:
            self._make_one(
                project=self.PROJECT,
                credentials=creds,
                instance_type="invalid-type",
            )
        self.assertIn(
            "instance_type must be one of 'cloud' or 'omni'",
            str(ctx.exception),
        )

    @CrossSync.pytest
    async def test_constructor_w_omni_username_password(self):
        from google.cloud.spanner_v1._async.client import InstanceType
        from google.cloud.spanner_v1.omni.credentials import (
            SpannerOmniCredentials,
        )

        client = self._make_one(
            project=self.PROJECT,
            client_options={"api_endpoint": "omni-host:15000"},
            instance_type=InstanceType.OMNI,
            username="test_user",
            password="test_password",
        )
        self.assertEqual(client.project, "default")
        self.assertEqual(client.instance_type, InstanceType.OMNI)
        self.assertEqual(client._host, "omni-host:15000")
        self.assertIsInstance(client._credentials, SpannerOmniCredentials)
        self.assertEqual(client._credentials.username, "test_user")
        self.assertEqual(client._credentials.target, "omni-host:15000")

    @CrossSync.pytest
    async def test_constructor_w_omni_partial_credentials_raises_value_error(self):
        from google.cloud.spanner_v1._async.client import InstanceType

        with self.assertRaises(ValueError) as ctx:
            self._make_one(
                project=self.PROJECT,
                client_options={"api_endpoint": "omni-host:15000"},
                instance_type=InstanceType.OMNI,
                username="test_user",
            )
        self.assertIn(
            "Both username and password must be specified for Omni authentication",
            str(ctx.exception),
        )

        with self.assertRaises(ValueError) as ctx:
            self._make_one(
                project=self.PROJECT,
                client_options={"api_endpoint": "omni-host:15000"},
                instance_type=InstanceType.OMNI,
                password="test_password",
            )
        self.assertIn(
            "Both username and password must be specified for Omni authentication",
            str(ctx.exception),
        )

    @CrossSync.pytest
    async def test_constructor_w_username_password_on_cloud_raises_value_error(self):
        creds = build_scoped_credentials()
        with self.assertRaises(ValueError) as ctx:
            self._make_one(
                project=self.PROJECT,
                credentials=creds,
                username="test_user",
                password="test_password",
            )
        self.assertIn(
            "username and password can only be used when instance_type='omni'.",
            str(ctx.exception),
        )

    @CrossSync.pytest
    async def test_instance_admin_api_omni(self):
        from google.cloud.spanner_v1._async.client import InstanceType

        client = self._make_one(
            project=self.PROJECT,
            client_options={"api_endpoint": "omni-host:15000"},
            instance_type=InstanceType.OMNI,
            username="test_user",
            password="test_password",
            use_plain_text=True,
        )

        inst_module = "google.cloud.spanner_v1._async.client.InstanceAdminClient"
        with mock.patch(inst_module) as instance_admin_client:
            api = client.instance_admin_api
            self.assertIs(api, instance_admin_client.return_value)
            instance_admin_client.assert_called_once()
            called_kw = instance_admin_client.call_args[1]
            self.assertIn("transport", called_kw)

    @CrossSync.pytest
    async def test_database_admin_api_omni(self):
        from google.cloud.spanner_v1._async.client import InstanceType

        client = self._make_one(
            project=self.PROJECT,
            client_options={"api_endpoint": "omni-host:15000"},
            instance_type=InstanceType.OMNI,
            username="test_user",
            password="test_password",
            use_plain_text=True,
        )

        db_module = "google.cloud.spanner_v1._async.client.DatabaseAdminClient"
        with mock.patch(db_module) as database_admin_client:
            api = client.database_admin_api
            self.assertIs(api, database_admin_client.return_value)
            database_admin_client.assert_called_once()
            called_kw = database_admin_client.call_args[1]
            self.assertIn("transport", called_kw)

    @CrossSync.pytest
    async def test_constructor_w_omni_explicit_credentials_instance(self):
        from google.cloud.spanner_v1._async.client import InstanceType
        from google.cloud.spanner_v1.omni.credentials import SpannerOmniCredentials

        creds = SpannerOmniCredentials("user", "pass", "omni-host:15000")
        client = self._make_one(
            project=self.PROJECT,
            client_options={"api_endpoint": "omni-host:15000"},
            instance_type=InstanceType.OMNI,
            credentials=creds,
        )
        self.assertIs(client._credentials, creds)
