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

import datetime

import pytest

import google.cloud.bigquery.schema


def create_field(mode="NULLABLE", type_="IGNORED"):
    return google.cloud.bigquery.schema.SchemaField("test_field", type_, mode=mode)


@pytest.fixture
def mut():
    from google.cloud.bigquery import _helpers

    return _helpers


@pytest.fixture
def object_under_test(mut):
    return mut.SCALAR_QUERY_PARAM_PARSER


def test_timestamp_to_py_w_none_nullable(object_under_test):
    assert object_under_test.timestamp_to_py(None, create_field()) is None


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (
            "2016-12-20 15:58:27.339328+00:00",
            datetime.datetime(
                2016, 12, 20, 15, 58, 27, 339328, tzinfo=datetime.timezone.utc
            ),
        ),
        (
            "2016-12-20 15:58:27+00:00",
            datetime.datetime(2016, 12, 20, 15, 58, 27, tzinfo=datetime.timezone.utc),
        ),
        (
            "2016-12-20T15:58:27.339328+00:00",
            datetime.datetime(
                2016, 12, 20, 15, 58, 27, 339328, tzinfo=datetime.timezone.utc
            ),
        ),
        (
            "2016-12-20T15:58:27+00:00",
            datetime.datetime(2016, 12, 20, 15, 58, 27, tzinfo=datetime.timezone.utc),
        ),
        (
            "2016-12-20 15:58:27.339328Z",
            datetime.datetime(
                2016, 12, 20, 15, 58, 27, 339328, tzinfo=datetime.timezone.utc
            ),
        ),
        (
            "2016-12-20 15:58:27Z",
            datetime.datetime(2016, 12, 20, 15, 58, 27, tzinfo=datetime.timezone.utc),
        ),
        (
            "2016-12-20T15:58:27.339328Z",
            datetime.datetime(
                2016, 12, 20, 15, 58, 27, 339328, tzinfo=datetime.timezone.utc
            ),
        ),
        (
            "2016-12-20T15:58:27Z",
            datetime.datetime(2016, 12, 20, 15, 58, 27, tzinfo=datetime.timezone.utc),
        ),
    ],
)
def test_timestamp_to_py_w_timestamp_valid(object_under_test, value, expected):
    assert object_under_test.timestamp_to_py(value, create_field()) == expected


def test_timestamp_to_py_w_timestamp_invalid(object_under_test):
    with pytest.raises(ValueError):
        object_under_test.timestamp_to_py("definitely-not-a-timestamp", create_field())
