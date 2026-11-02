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

from __future__ import absolute_import

import datetime
import unittest
from unittest import mock

import google.auth.credentials as ga_credentials
import grpc

from google.cloud import monitoring_v3 as monitoring_v3
from google.cloud.monitoring_v3 import MetricServiceClient
from google.cloud.monitoring_v3.services.metric_service.transports import (
    MetricServiceGrpcTransport,
)

PROJECT = "my-project"

METRIC_TYPE = "compute.googleapis.com/instance/uptime"
METRIC_LABELS = {"instance_name": "instance-1"}
METRIC_LABELS2 = {"instance_name": "instance-2"}

RESOURCE_TYPE = "gce_instance"
RESOURCE_LABELS = {
    "project_id": "my-project",
    "zone": "us-east1-a",
    "instance_id": "1234567890123456789",
}
RESOURCE_LABELS2 = {
    "project_id": "my-project",
    "zone": "us-east1-b",
    "instance_id": "9876543210987654321",
}

METRIC_KIND = "DELTA"
VALUE_TYPE = "DOUBLE"

TS0 = datetime.datetime(2016, 4, 6, 22, 5, 0, 42)
TS1 = datetime.datetime(2016, 4, 6, 22, 5, 1, 42)
TS2 = datetime.datetime(2016, 4, 6, 22, 5, 2, 42)


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response

    # This method is required; otherwise we see `AttributeError: 'MultiCallableStub' object has no attribute 'with_call'`
    # See https://github.com/grpc/grpc/blob/b53f4055a93fb98601c75dcefaa8f3665167e6cf/src/python/grpcio/grpc/_interceptor.py#L315
    # for the specific location in gRPC code which expects this method.
    def with_call(
        self,
        request,
        timeout=None,
        metadata=None,
        credentials=None,
        wait_for_ready=None,
        compression=None,
    ):
        self.channel_stub.requests.append((self.method, request))
        mock_call = None  # Actual type is grpc.Call but using None since `with_call` is not needed for tests
        response = self.channel_stub.responses.pop()
        if response:
            return (response, mock_call)


class ChannelStub(grpc.Channel):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.responses = [
            monitoring_v3.ListTimeSeriesResponse(**response) for response in responses
        ]
        self.requests = []

    # The method signature should be compatible with this code
    # https://github.com/grpc/grpc/blob/b53f4055a93fb98601c75dcefaa8f3665167e6cf/src/python/grpcio/grpc/_interceptor.py#L696-L701
    # where arguments `method`, `request_serializer`, `response_deserializer` and `_registered_method` are supported
    def unary_unary(
        self,
        method,
        request_serializer=None,
        response_deserializer=None,
        _registered_method=None,
    ):
        return MultiCallableStub(method, self)

    def subscribe(self, callback, try_to_connect=False):
        """grpc.Channel.subscribe implementation."""
        pass

    def unary_stream(
        self,
        method,
        request_serializer=None,
        response_deserializer=None,
    ):
        """grpc.Channel.unary_stream implementation."""
        return self._stub_for_method(method)

    def stream_unary(
        self,
        method,
        request_serializer=None,
        response_deserializer=None,
    ):
        """grpc.Channel.stream_unary implementation."""
        return self._stub_for_method(method)

    def stream_stream(
        self,
        method,
        request_serializer=None,
        response_deserializer=None,
    ):
        """grpc.Channel.stream_stream implementation."""
        return self._stub_for_method(method)

    def unsubscribe(self, callback):
        """grpc.Channel.unsubscribe implementation."""
        pass

    def close(self):
        """grpc.Channel.close implementation."""
        pass


class TestQuery(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.monitoring_v3.query import Query

        return Query

    def _make_one(self, *args, **kwargs):
        return self._get_target_class()(*args, **kwargs)

    @staticmethod
    def _make_interval(end_time, start_time=None):
        interval = monitoring_v3.TimeInterval(end_time=end_time, start_time=start_time)
        return interval

    @staticmethod
    def _create_client(channel=None):
        if channel is None:
            channel = ChannelStub()
        transport = MetricServiceGrpcTransport(
            channel=channel, credentials=ga_credentials.AnonymousCredentials()
        )
        return MetricServiceClient(transport=transport)

    def test_constructor_minimal(self):
        client = self._create_client()
        query = self._make_one(client, PROJECT)

        self.assertEqual(query._client, client)
        self.assertEqual(
            query._filter.metric_type, self._get_target_class().DEFAULT_METRIC_TYPE
        )

        self.assertIsNone(query._start_time)
        self.assertIsNone(query._end_time)

        self.assertEqual(query._per_series_aligner, 0)
        self.assertEqual(query._alignment_period_seconds, 0)
        self.assertEqual(query._cross_series_reducer, 0)
        self.assertEqual(query._group_by_fields, ())

    def test_constructor_maximal(self):
        T1 = datetime.datetime(2016, 4, 7, 2, 30, 30)
        DAYS, HOURS, MINUTES = 1, 2, 3
        T0 = T1 - datetime.timedelta(days=DAYS, hours=HOURS, minutes=MINUTES)

        client = self._create_client()
        query = self._make_one(
            client,
            PROJECT,
            METRIC_TYPE,
            end_time=T1,
            days=DAYS,
            hours=HOURS,
            minutes=MINUTES,
        )

        self.assertEqual(query._client, client)
        self.assertEqual(query._filter.metric_type, METRIC_TYPE)

        self.assertEqual(query._start_time, T0)
        self.assertEqual(query._end_time, T1)

        self.assertEqual(query._per_series_aligner, 0)
        self.assertEqual(query._alignment_period_seconds, 0)
        self.assertEqual(query._cross_series_reducer, 0)
        self.assertEqual(query._group_by_fields, ())

    def test_constructor_default_end_time(self):
        MINUTES = 5
        NOW = datetime.datetime(2016, 4, 7, 2, 30, 30)
        T0 = datetime.datetime(2016, 4, 7, 2, 25, 0)
        T1 = datetime.datetime(2016, 4, 7, 2, 30, 0)

        client = self._create_client()
        with mock.patch("google.cloud.monitoring_v3.query._UTCNOW", new=lambda: NOW):
            query = self._make_one(client, PROJECT, METRIC_TYPE, minutes=MINUTES)

        self.assertEqual(query._start_time, T0)
        self.assertEqual(query._end_time, T1)

    def test_constructor_nonzero_duration_illegal(self):
        T1 = datetime.datetime(2016, 4, 7, 2, 30, 30)
        client = self._create_client()
        with self.assertRaises(ValueError):
            self._make_one(client, PROJECT, METRIC_TYPE, end_time=T1)

    def test_execution_without_interval_illegal(self):
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        with self.assertRaises(ValueError):
            list(query)

    def test_metric_type(self):
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        self.assertEqual(query.metric_type, METRIC_TYPE)

    def test_filter(self):
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        expected = 'metric.type = "{type}"'.format(type=METRIC_TYPE)
        self.assertEqual(query.filter, expected)

    def test_filter_by_group(self):
        GROUP = "1234567"
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_group(GROUP)
        expected = ('metric.type = "{type}" AND group.id = "{group}"').format(
            type=METRIC_TYPE, group=GROUP
        )
        self.assertEqual(query.filter, expected)

    def test_filter_by_projects(self):
        PROJECT1, PROJECT2 = "project-1", "project-2"
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_projects(PROJECT1, PROJECT2)
        expected = (
            'metric.type = "{type}"'
            ' AND project = "{project1}" OR project = "{project2}"'
        ).format(type=METRIC_TYPE, project1=PROJECT1, project2=PROJECT2)
        self.assertEqual(query.filter, expected)

    def test_filter_by_resources(self):
        ZONE_PREFIX = "europe-"
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_resources(zone_prefix=ZONE_PREFIX)
        expected = (
            'metric.type = "{type}" AND resource.label.zone = starts_with("{prefix}")'
        ).format(type=METRIC_TYPE, prefix=ZONE_PREFIX)
        self.assertEqual(query.filter, expected)

    def test_filter_by_metrics(self):
        INSTANCE = "my-instance"
        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_metrics(instance_name=INSTANCE)
        expected = (
            'metric.type = "{type}" AND metric.label.instance_name = "{instance}"'
        ).format(type=METRIC_TYPE, instance=INSTANCE)
        self.assertEqual(query.filter, expected)

    def test_request_parameters_minimal(self):
        T1 = datetime.datetime(2016, 4, 7, 2, 30, 0)

        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_interval(end_time=T1)
        actual = query._build_query_params()
        expected = {
            "name": "projects/{}".format(PROJECT),
            "filter": 'metric.type = "{type}"'.format(type=METRIC_TYPE),
            "interval": self._make_interval(T1),
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        }
        self.assertEqual(actual, expected)

    def test_request_parameters_maximal(self):
        T0 = datetime.datetime(2016, 4, 7, 2, 0, 0)
        T1 = datetime.datetime(2016, 4, 7, 2, 30, 0)

        ALIGNER = "ALIGN_DELTA"
        MINUTES, SECONDS, PERIOD_IN_SECONDS = 1, 30, 90

        REDUCER = "REDUCE_MEAN"
        FIELD1, FIELD2 = "resource.zone", "metric.instance_name"

        PAGE_SIZE = 100

        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_interval(start_time=T0, end_time=T1)
        query = query.align(ALIGNER, minutes=MINUTES, seconds=SECONDS)
        query = query.reduce(REDUCER, FIELD1, FIELD2)
        actual = query._build_query_params(headers_only=True, page_size=PAGE_SIZE)
        expected = {
            "name": "projects/%s" % PROJECT,
            "filter": 'metric.type = "{type}"'.format(type=METRIC_TYPE),
            "interval": self._make_interval(T1, T0),
            "aggregation": monitoring_v3.Aggregation(
                per_series_aligner=ALIGNER,
                alignment_period={"seconds": PERIOD_IN_SECONDS},
                cross_series_reducer=REDUCER,
                group_by_fields=[FIELD1, FIELD2],
            ),
            "view": monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.HEADERS,
            "page_size": PAGE_SIZE,
        }
        self.assertEqual(actual, expected)

    def test_iteration(self):
        T0 = datetime.datetime(2016, 4, 6, 22, 5, 0)
        T1 = datetime.datetime(2016, 4, 6, 22, 10, 0)

        INTERVAL1 = self._make_interval(TS1, TS0)
        INTERVAL2 = self._make_interval(TS2, TS1)

        VALUE1 = 60  # seconds
        VALUE2 = 60.001  # seconds

        # Currently cannot create from a list of dict for repeated fields due to
        # https://github.com/googleapis/proto-plus-python/issues/135
        POINT1 = monitoring_v3.Point(
            {"interval": INTERVAL2, "value": {"double_value": VALUE1}}
        )
        POINT2 = monitoring_v3.Point(
            {"interval": INTERVAL1, "value": {"double_value": VALUE1}}
        )
        POINT3 = monitoring_v3.Point(
            {"interval": INTERVAL2, "value": {"double_value": VALUE2}}
        )
        POINT4 = monitoring_v3.Point(
            {"interval": INTERVAL1, "value": {"double_value": VALUE2}}
        )
        SERIES1 = monitoring_v3.TimeSeries(
            {
                "metric": {"type": METRIC_TYPE, "labels": METRIC_LABELS},
                "resource": {"type": RESOURCE_TYPE, "labels": RESOURCE_LABELS},
                "metric_kind": METRIC_KIND,
                "value_type": VALUE_TYPE,
                "points": [POINT1, POINT2],
            }
        )
        SERIES2 = monitoring_v3.TimeSeries(
            {
                "metric": {"type": METRIC_TYPE, "labels": METRIC_LABELS2},
                "resource": {"type": RESOURCE_TYPE, "labels": RESOURCE_LABELS2},
                "metric_kind": METRIC_KIND,
                "value_type": VALUE_TYPE,
                "points": [POINT3, POINT4],
            }
        )

        RESPONSE = {"time_series": [SERIES1, SERIES2], "next_page_token": ""}

        channel = ChannelStub(responses=[RESPONSE])
        client = self._create_client(channel)
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_interval(start_time=T0, end_time=T1)
        response = list(query)

        self.assertEqual(len(response), 2)
        series1, series2 = response

        self.assertEqual(series1.metric.labels, METRIC_LABELS)
        self.assertEqual(series2.metric.labels, METRIC_LABELS2)
        self.assertEqual(series1.resource.labels, RESOURCE_LABELS)
        self.assertEqual(series2.resource.labels, RESOURCE_LABELS2)

        self.assertEqual(
            [p.value.double_value for p in series1.points], [VALUE1, VALUE1]
        )
        self.assertEqual(
            [p.value.double_value for p in series2.points], [VALUE2, VALUE2]
        )
        self.assertEqual([p.interval for p in series1.points], [INTERVAL2, INTERVAL1])
        self.assertEqual([p.interval for p in series2.points], [INTERVAL2, INTERVAL1])

        expected_request = monitoring_v3.ListTimeSeriesRequest(
            name="projects/" + PROJECT,
            filter='metric.type = "{type}"'.format(type=METRIC_TYPE),
            interval=self._make_interval(T1, T0),
            view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.FULL,
        )
        request = channel.requests[0][1]
        self.assertEqual(request, expected_request)

    def test_iteration_empty(self):
        T0 = datetime.datetime(2016, 4, 6, 22, 5, 0)
        T1 = datetime.datetime(2016, 4, 6, 22, 10, 0)

        client = self._create_client()
        query = self._make_one(client, PROJECT, METRIC_TYPE)

        with mock.patch.object(
            type(client._transport.list_time_series), "__call__"
        ) as call:
            call.return_value = monitoring_v3.ListTimeSeriesResponse()
            query = query.select_interval(start_time=T0, end_time=T1)
            response = list(query)

            self.assertEqual(len(response), 0)

    def test_iteration_headers_only(self):
        T0 = datetime.datetime(2016, 4, 6, 22, 5, 0)
        T1 = datetime.datetime(2016, 4, 6, 22, 10, 0)

        SERIES1 = {
            "metric": {"type": METRIC_TYPE, "labels": METRIC_LABELS},
            "resource": {"type": RESOURCE_TYPE, "labels": RESOURCE_LABELS},
            "metric_kind": METRIC_KIND,
            "value_type": VALUE_TYPE,
        }
        SERIES2 = {
            "metric": {"type": METRIC_TYPE, "labels": METRIC_LABELS2},
            "resource": {"type": RESOURCE_TYPE, "labels": RESOURCE_LABELS2},
            "metric_kind": METRIC_KIND,
            "value_type": VALUE_TYPE,
        }

        RESPONSE = {"time_series": [SERIES1, SERIES2], "next_page_token": ""}

        channel = ChannelStub(responses=[RESPONSE])
        client = self._create_client(channel)
        query = self._make_one(client, PROJECT, METRIC_TYPE)
        query = query.select_interval(start_time=T0, end_time=T1)

        # add a temporal alignment to test that "aggregation" query params is
        # correctly processed
        query = query.align(monitoring_v3.Aggregation.Aligner.ALIGN_MAX, seconds=3600)
        response = list(query.iter(headers_only=True))

        self.assertEqual(len(response), 2)
        series1, series2 = response

        self.assertEqual(series1.metric.labels, METRIC_LABELS)
        self.assertEqual(series2.metric.labels, METRIC_LABELS2)
        self.assertEqual(series1.resource.labels, RESOURCE_LABELS)
        self.assertEqual(series2.resource.labels, RESOURCE_LABELS2)

        self.assertFalse(len(series1.points))
        self.assertFalse(len(series2.points))

        expected_request = monitoring_v3.ListTimeSeriesRequest(
            name="projects/" + PROJECT,
            filter='metric.type = "{type}"'.format(type=METRIC_TYPE),
            interval=self._make_interval(T1, T0),
            view=monitoring_v3.ListTimeSeriesRequest.TimeSeriesView.HEADERS,
            aggregation=monitoring_v3.Aggregation(
                per_series_aligner=monitoring_v3.Aggregation.Aligner.ALIGN_MAX,
                alignment_period={"seconds": 3600},
            ),
        )
        request = channel.requests[0][1]
        self.assertEqual(request, expected_request)


class Test_Filter(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.monitoring_v3.query import _Filter

        return _Filter

    def _make_one(self, metric_type):
        return self._get_target_class()(metric_type)

    def test_minimal(self):
        obj = self._make_one(METRIC_TYPE)
        expected = 'metric.type = "{type}"'.format(type=METRIC_TYPE)
        self.assertEqual(str(obj), expected)

    def test_maximal(self):
        obj = self._make_one(METRIC_TYPE)
        obj.group_id = "1234567"
        obj.projects = "project-1", "project-2"
        obj.select_resources(resource_type="some-resource", resource_label="foo")
        obj.select_metrics(metric_label_prefix="bar-")

        expected = (
            'metric.type = "{type}"'
            ' AND group.id = "1234567"'
            ' AND project = "project-1" OR project = "project-2"'
            ' AND resource.label.resource_label = "foo"'
            ' AND resource.type = "some-resource"'
            ' AND metric.label.metric_label = starts_with("bar-")'
        ).format(type=METRIC_TYPE)

        self.assertEqual(str(obj), expected)


class Test__build_label_filter(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        from google.cloud.monitoring_v3.query import _build_label_filter

        return _build_label_filter(*args, **kwargs)

    def test_no_labels(self):
        self.assertEqual(self._call_fut("resource"), "")

    def test_label_is_none(self):
        self.assertEqual(self._call_fut("resource", foo=None), "")

    def test_metric_labels(self):
        actual = self._call_fut(
            "metric", alpha_prefix="a-", beta_gamma_suffix="-b", delta_epsilon="xyz"
        )
        expected = (
            'metric.label.alpha = starts_with("a-")'
            ' AND metric.label.beta_gamma = ends_with("-b")'
            ' AND metric.label.delta_epsilon = "xyz"'
        )
        self.assertEqual(actual, expected)

    def test_metric_label_response_code_not_equal(self):
        actual = self._call_fut("metric", response_code_notequal=200)
        expected = "metric.label.response_code != 200"
        self.assertEqual(actual, expected)

    def test_metric_label_response_code_greater_less(self):
        actual = self._call_fut(
            "metric", response_code_greater=500, response_code_less=600
        )
        expected = (
            "metric.label.response_code < 600 AND metric.label.response_code > 500"
        )
        self.assertEqual(actual, expected)

    def test_metric_label_response_code_greater_less_equal(self):
        actual = self._call_fut(
            "metric", response_code_greaterequal=500, response_code_lessequal=600
        )
        expected = (
            "metric.label.response_code <= 600 AND metric.label.response_code >= 500"
        )
        self.assertEqual(actual, expected)

    def test_resource_labels(self):
        actual = self._call_fut(
            "resource", alpha_prefix="a-", beta_gamma_suffix="-b", delta_epsilon="xyz"
        )
        expected = (
            'resource.label.alpha = starts_with("a-")'
            ' AND resource.label.beta_gamma = ends_with("-b")'
            ' AND resource.label.delta_epsilon = "xyz"'
        )
        self.assertEqual(actual, expected)

    def test_raw_label_filters(self):
        actual = self._call_fut(
            "resource",
            'resource.label.alpha = starts_with("a-")',
            'resource.label.beta_gamma = ends_with("-b")',
            'resource.label.delta_epsilon = "xyz"',
        )
        expected = (
            'resource.label.alpha = starts_with("a-")'
            ' AND resource.label.beta_gamma = ends_with("-b")'
            ' AND resource.label.delta_epsilon = "xyz"'
        )
        self.assertEqual(actual, expected)

    def test_resource_type(self):
        actual = self._call_fut("resource", resource_type="foo")
        expected = 'resource.type = "foo"'
        self.assertEqual(actual, expected)

    def test_resource_type_prefix(self):
        actual = self._call_fut("resource", resource_type_prefix="foo-")
        expected = 'resource.type = starts_with("foo-")'
        self.assertEqual(actual, expected)

    def test_resource_type_suffix(self):
        actual = self._call_fut("resource", resource_type_suffix="-foo")
        expected = 'resource.type = ends_with("-foo")'
        self.assertEqual(actual, expected)
