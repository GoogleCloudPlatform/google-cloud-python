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

import pandas
from google.api import metric_pb2, monitored_resource_pb2
from google.api_core import datetime_helpers

from google.cloud import monitoring_v3
from google.cloud.monitoring_v3 import _dataframe

PROJECT = "my-project"

INSTANCE_NAMES = ["instance-1", "instance-2"]
INSTANCE_ZONES = ["us-east1-a", "us-east1-b"]
INSTANCE_IDS = ["1234567890123456789", "9876543210987654321"]

METRIC_TYPE = "compute.googleapis.com/instance/cpu/utilization"
METRIC_LABELS = list({"instance_name": name} for name in INSTANCE_NAMES)

RESOURCE_TYPE = "gce_instance"
RESOURCE_LABELS = list(
    {"project_id": PROJECT, "zone": zone, "instance_id": instance_id}
    for zone, instance_id in zip(INSTANCE_ZONES, INSTANCE_IDS)
)

METRIC_KIND = "GAUGE"
VALUE_TYPE = "DOUBLE"

TIMESTAMPS = [
    "2016-04-06T22:05:00.042Z",
    "2016-04-06T22:05:01.042Z",
    "2016-04-06T22:05:02.042Z",
]

DIMENSIONS = len(TIMESTAMPS), len(INSTANCE_NAMES)
VALUES = list(0.1 * i for i in range(DIMENSIONS[1]))
ARRAY = [VALUES] * DIMENSIONS[0]


def parse_timestamps():
    from google.api_core import datetime_helpers

    return [datetime_helpers.from_rfc3339(t).replace(tzinfo=None) for t in TIMESTAMPS]


def generate_query_results():
    def P(timestamp, value):
        interval = monitoring_v3.TimeInterval()
        interval.start_time = datetime_helpers.from_rfc3339(timestamp).replace(
            tzinfo=None
        )
        interval.end_time = datetime_helpers.from_rfc3339(timestamp).replace(
            tzinfo=None
        )
        return monitoring_v3.Point(interval=interval, value={"double_value": value})

    for metric_labels, resource_labels, value in zip(
        METRIC_LABELS, RESOURCE_LABELS, VALUES
    ):
        yield monitoring_v3.TimeSeries(
            metric=metric_pb2.Metric(type=METRIC_TYPE, labels=metric_labels),
            resource=monitored_resource_pb2.MonitoredResource(
                type=RESOURCE_TYPE, labels=resource_labels
            ),
            metric_kind=METRIC_KIND,
            value_type=VALUE_TYPE,
            points=[P(t, value) for t in TIMESTAMPS],
        )


class Test__build_dataframe(unittest.TestCase):
    def _call_fut(self, *args, **kwargs):
        return _dataframe._build_dataframe(*args, **kwargs)

    def test_both_label_and_labels_illegal(self):
        with self.assertRaises(ValueError):
            self._call_fut([], label="instance_name", labels=["zone"])

    def test_empty_labels_illegal(self):
        with self.assertRaises(ValueError):
            self._call_fut([], labels=[])

    def test_simple_label(self):
        iterable = generate_query_results()
        dataframe = self._call_fut(iterable, label="instance_name")

        self.assertEqual(dataframe.shape, DIMENSIONS)
        self.assertEqual(dataframe.values.tolist(), ARRAY)

        expected_headers = [(instance_name,) for instance_name in INSTANCE_NAMES]
        self.assertEqual(list(dataframe.columns), expected_headers)
        self.assertIsNone(dataframe.columns.name)

        self.assertEqual(list(dataframe.index), parse_timestamps())
        self.assertIsNone(dataframe.index.name)

    def test_multiple_labels(self):
        NAMES = ["resource_type", "instance_id"]

        iterable = generate_query_results()
        dataframe = self._call_fut(iterable, labels=NAMES)

        self.assertEqual(dataframe.shape, DIMENSIONS)
        self.assertEqual(dataframe.values.tolist(), ARRAY)

        expected_headers = [
            (RESOURCE_TYPE, instance_id) for instance_id in INSTANCE_IDS
        ]
        self.assertEqual(list(dataframe.columns), expected_headers)
        self.assertEqual(dataframe.columns.names, NAMES)
        self.assertIsNone(dataframe.columns.name)

        self.assertEqual(list(dataframe.index), parse_timestamps())
        self.assertIsNone(dataframe.index.name)

    def test_multiple_labels_with_just_one(self):
        NAME = "instance_id"
        NAMES = [NAME]

        iterable = generate_query_results()
        dataframe = self._call_fut(iterable, labels=NAMES)

        self.assertEqual(dataframe.shape, DIMENSIONS)
        self.assertEqual(dataframe.values.tolist(), ARRAY)

        expected_headers = [(instance_id,) for instance_id in INSTANCE_IDS]
        self.assertEqual(list(dataframe.columns), expected_headers)
        self.assertEqual(dataframe.columns.names, NAMES)
        self.assertIsNone(dataframe.columns.name)

        self.assertEqual(list(dataframe.index), parse_timestamps())
        self.assertIsNone(dataframe.index.name)

    def test_smart_labels(self):
        NAMES = ["resource_type", "project_id", "zone", "instance_id", "instance_name"]

        iterable = generate_query_results()
        dataframe = self._call_fut(iterable)

        self.assertEqual(dataframe.shape, DIMENSIONS)
        self.assertEqual(dataframe.values.tolist(), ARRAY)

        expected_headers = [
            (RESOURCE_TYPE, PROJECT, zone, instance_id, instance_name)
            for zone, instance_id, instance_name in zip(
                INSTANCE_ZONES, INSTANCE_IDS, INSTANCE_NAMES
            )
        ]
        self.assertEqual(list(dataframe.columns), expected_headers)
        self.assertEqual(dataframe.columns.names, NAMES)
        self.assertIsNone(dataframe.columns.name)

        self.assertEqual(list(dataframe.index), parse_timestamps())
        self.assertIsNone(dataframe.index.name)

    def test_empty_table_simple_label(self):
        dataframe = self._call_fut([], label="instance_name")
        self.assertEqual(dataframe.shape, (0, 0))
        self.assertIsNone(dataframe.columns.name)
        self.assertIsNone(dataframe.index.name)
        self.assertIsInstance(dataframe.index, pandas.DatetimeIndex)

    def test_empty_table_multiple_labels(self):
        NAMES = ["resource_type", "instance_id"]
        dataframe = self._call_fut([], labels=NAMES)
        self.assertEqual(dataframe.shape, (0, 0))
        self.assertEqual(dataframe.columns.names, NAMES)
        self.assertIsNone(dataframe.columns.name)
        self.assertIsNone(dataframe.index.name)
        self.assertIsInstance(dataframe.index, pandas.DatetimeIndex)

    def test_empty_table_multiple_labels_with_just_one(self):
        NAME = "instance_id"
        NAMES = [NAME]
        dataframe = self._call_fut([], labels=NAMES)
        self.assertEqual(dataframe.shape, (0, 0))
        self.assertEqual(dataframe.columns.names, NAMES)
        self.assertIsNone(dataframe.columns.name)
        self.assertIsNone(dataframe.index.name)
        self.assertIsInstance(dataframe.index, pandas.DatetimeIndex)

    def test_empty_table_smart_labels(self):
        NAME = "resource_type"
        NAMES = [NAME]
        dataframe = self._call_fut([])
        self.assertEqual(dataframe.shape, (0, 0))
        self.assertEqual(dataframe.columns.names, NAMES)
        self.assertIsNone(dataframe.columns.name)
        self.assertIsNone(dataframe.index.name)
        self.assertIsInstance(dataframe.index, pandas.DatetimeIndex)


class Test__sorted_resource_labels(unittest.TestCase):
    def _call_fut(self, labels):
        from google.cloud.monitoring_v3._dataframe import _sorted_resource_labels

        return _sorted_resource_labels(labels)

    def test_empty(self):
        self.assertEqual(self._call_fut([]), [])

    def test_sorted(self):
        from google.cloud.monitoring_v3._dataframe import TOP_RESOURCE_LABELS

        EXPECTED = TOP_RESOURCE_LABELS + ("other-1", "other-2")
        self.assertSequenceEqual(self._call_fut(EXPECTED), EXPECTED)

    def test_reversed(self):
        from google.cloud.monitoring_v3._dataframe import TOP_RESOURCE_LABELS

        EXPECTED = TOP_RESOURCE_LABELS + ("other-1", "other-2")
        INPUT = list(reversed(EXPECTED))
        self.assertSequenceEqual(self._call_fut(INPUT), EXPECTED)
