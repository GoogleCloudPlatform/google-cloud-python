# Copyright 2016 Google LLC
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

import unittest


class TestMetric(unittest.TestCase):
    PROJECT = "test-project"
    METRIC_NAME = "metric-name"
    FULL_METRIC_NAME = f"projects/{PROJECT}/metrics/{METRIC_NAME}"
    FILTER = "logName:syslog AND severity>=ERROR"
    DESCRIPTION = "DESCRIPTION"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import Metric

        return Metric

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        client = _Client(self.PROJECT)
        metric = self._make_one(self.METRIC_NAME, client=client)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertIsNone(metric.filter_)
        self.assertEqual(metric.description, "")
        self.assertIs(metric.client, client)
        self.assertEqual(metric.project, self.PROJECT)
        self.assertEqual(metric.full_name, self.FULL_METRIC_NAME)
        self.assertEqual(metric.path, f"/{self.FULL_METRIC_NAME}")

    def test_ctor_explicit(self):
        client = _Client(self.PROJECT)
        metric = self._make_one(
            self.METRIC_NAME,
            filter_=self.FILTER,
            client=client,
            description=self.DESCRIPTION,
        )
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, self.DESCRIPTION)
        self.assertIs(metric.client, client)
        self.assertEqual(metric.project, self.PROJECT)
        self.assertEqual(metric.full_name, self.FULL_METRIC_NAME)
        self.assertEqual(metric.path, f"/{self.FULL_METRIC_NAME}")

    def test_from_api_repr_minimal(self):
        client = _Client(project=self.PROJECT)
        RESOURCE = {"name": self.METRIC_NAME, "filter": self.FILTER}
        klass = self._get_target_class()
        metric = klass.from_api_repr(RESOURCE, client=client)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, "")
        self.assertIs(metric._client, client)
        self.assertEqual(metric.project, self.PROJECT)
        self.assertEqual(metric.full_name, self.FULL_METRIC_NAME)

    def test_from_api_repr_w_description(self):
        client = _Client(project=self.PROJECT)
        DESCRIPTION = "DESCRIPTION"
        RESOURCE = {
            "name": self.METRIC_NAME,
            "filter": self.FILTER,
            "description": DESCRIPTION,
        }
        klass = self._get_target_class()
        metric = klass.from_api_repr(RESOURCE, client=client)
        self.assertEqual(metric.name, self.METRIC_NAME)
        self.assertEqual(metric.filter_, self.FILTER)
        self.assertEqual(metric.description, DESCRIPTION)
        self.assertIs(metric._client, client)
        self.assertEqual(metric.project, self.PROJECT)
        self.assertEqual(metric.full_name, self.FULL_METRIC_NAME)

    def test_create_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client)

        metric.create()

        self.assertEqual(
            api._metric_create_called_with,
            (self.PROJECT, self.METRIC_NAME, self.FILTER, ""),
        )

    def test_create_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(
            self.METRIC_NAME,
            filter_=self.FILTER,
            client=client1,
            description=self.DESCRIPTION,
        )

        metric.create(client=client2)

        self.assertEqual(
            api._metric_create_called_with,
            (self.PROJECT, self.METRIC_NAME, self.FILTER, self.DESCRIPTION),
        )

    def test_exists_miss_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client)

        self.assertFalse(metric.exists())

        self.assertEqual(api._metric_get_called_with, (self.PROJECT, self.METRIC_NAME))

    def test_exists_hit_w_alternate_client(self):
        RESOURCE = {"name": self.METRIC_NAME, "filter": self.FILTER}
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.metrics_api = _DummyMetricsAPI()
        api._metric_get_response = RESOURCE
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client1)

        self.assertTrue(metric.exists(client=client2))

        self.assertEqual(api._metric_get_called_with, (self.PROJECT, self.METRIC_NAME))

    def test_reload_w_bound_client(self):
        NEW_FILTER = "logName:syslog AND severity>=INFO"
        RESOURCE = {"name": self.METRIC_NAME, "filter": NEW_FILTER}
        client = _Client(project=self.PROJECT)
        api = client.metrics_api = _DummyMetricsAPI()
        api._metric_get_response = RESOURCE
        metric = self._make_one(
            self.METRIC_NAME,
            filter_=self.FILTER,
            client=client,
            description=self.DESCRIPTION,
        )

        metric.reload()

        self.assertEqual(metric.filter_, NEW_FILTER)
        self.assertEqual(metric.description, "")
        self.assertEqual(api._metric_get_called_with, (self.PROJECT, self.METRIC_NAME))

    def test_reload_w_alternate_client(self):
        NEW_FILTER = "logName:syslog AND severity>=INFO"
        RESOURCE = {
            "name": self.METRIC_NAME,
            "description": self.DESCRIPTION,
            "filter": NEW_FILTER,
        }
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.metrics_api = _DummyMetricsAPI()
        api._metric_get_response = RESOURCE
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client1)

        metric.reload(client=client2)

        self.assertEqual(metric.filter_, NEW_FILTER)
        self.assertEqual(metric.description, self.DESCRIPTION)
        self.assertEqual(api._metric_get_called_with, (self.PROJECT, self.METRIC_NAME))

    def test_update_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client)

        metric.update()

        self.assertEqual(
            api._metric_update_called_with,
            (self.PROJECT, self.METRIC_NAME, self.FILTER, ""),
        )

    def test_update_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(
            self.METRIC_NAME,
            filter_=self.FILTER,
            client=client1,
            description=self.DESCRIPTION,
        )

        metric.update(client=client2)

        self.assertEqual(
            api._metric_update_called_with,
            (self.PROJECT, self.METRIC_NAME, self.FILTER, self.DESCRIPTION),
        )

    def test_delete_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client)

        metric.delete()

        self.assertEqual(
            api._metric_delete_called_with, (self.PROJECT, self.METRIC_NAME)
        )

    def test_delete_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.metrics_api = _DummyMetricsAPI()
        metric = self._make_one(self.METRIC_NAME, filter_=self.FILTER, client=client1)

        metric.delete(client=client2)

        self.assertEqual(
            api._metric_delete_called_with, (self.PROJECT, self.METRIC_NAME)
        )


class _Client(object):
    def __init__(self, project):
        self.project = project


class _DummyMetricsAPI(object):
    def metric_create(self, project, metric_name, filter_, description):
        self._metric_create_called_with = (project, metric_name, filter_, description)

    def metric_get(self, project, metric_name):
        from google.cloud.exceptions import NotFound

        self._metric_get_called_with = (project, metric_name)
        try:
            return self._metric_get_response
        except AttributeError:
            raise NotFound("miss")

    def metric_update(self, project, metric_name, filter_, description):
        self._metric_update_called_with = (project, metric_name, filter_, description)

    def metric_delete(self, project, metric_name):
        self._metric_delete_called_with = (project, metric_name)
