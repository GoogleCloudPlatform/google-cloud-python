# -*- coding: utf-8 -*-
#
# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

ENDPOINT = "https://some.endpoint"
CONNECTION = "connection_string"
MAX_BATCHING_ROWS = 50
USER_DEFINED_CONTEXT = {
    "foo": "bar",
}


@pytest.fixture
def target_class():
    from google.cloud.bigquery.routine import RemoteFunctionOptions

    return RemoteFunctionOptions


def test_ctor(target_class):
    options = target_class(
        endpoint=ENDPOINT,
        connection=CONNECTION,
        max_batching_rows=MAX_BATCHING_ROWS,
        user_defined_context=USER_DEFINED_CONTEXT,
    )
    assert options.endpoint == ENDPOINT
    assert options.connection == CONNECTION
    assert options.max_batching_rows == MAX_BATCHING_ROWS
    assert options.user_defined_context == USER_DEFINED_CONTEXT


def test_empty_ctor(target_class):
    options = target_class()
    assert options._properties == {}
    options = target_class(_properties=None)
    assert options._properties == {}
    options = target_class(_properties={})
    assert options._properties == {}


def test_ctor_bad_context(target_class):
    with pytest.raises(ValueError, match="value must be dictionary"):
        target_class(user_defined_context=[1, 2, 3, 4])


def test_from_api_repr(target_class):
    resource = {
        "endpoint": ENDPOINT,
        "connection": CONNECTION,
        "maxBatchingRows": MAX_BATCHING_ROWS,
        "userDefinedContext": USER_DEFINED_CONTEXT,
        "someRandomField": "someValue",
    }
    options = target_class.from_api_repr(resource)
    assert options.endpoint == ENDPOINT
    assert options.connection == CONNECTION
    assert options.max_batching_rows == MAX_BATCHING_ROWS
    assert options.user_defined_context == USER_DEFINED_CONTEXT
    assert options._properties["someRandomField"] == "someValue"


def test_from_api_repr_w_minimal_resource(target_class):
    resource = {}
    options = target_class.from_api_repr(resource)
    assert options.endpoint is None
    assert options.connection is None
    assert options.max_batching_rows is None
    assert options.user_defined_context is None


def test_from_api_repr_w_unknown_fields(target_class):
    resource = {"thisFieldIsNotInTheProto": "just ignore me"}
    options = target_class.from_api_repr(resource)
    assert options._properties is resource


def test_eq(target_class):
    options = target_class(
        endpoint=ENDPOINT,
        connection=CONNECTION,
        max_batching_rows=MAX_BATCHING_ROWS,
        user_defined_context=USER_DEFINED_CONTEXT,
    )
    other_options = target_class(
        endpoint=ENDPOINT,
        connection=CONNECTION,
        max_batching_rows=MAX_BATCHING_ROWS,
        user_defined_context=USER_DEFINED_CONTEXT,
    )
    assert options == other_options
    assert not (options != other_options)

    empty_options = target_class()
    assert not (options == empty_options)
    assert options != empty_options

    notanarg = object()
    assert not (options == notanarg)
    assert options != notanarg


def test_repr(target_class):
    options = target_class(
        endpoint=ENDPOINT,
        connection=CONNECTION,
        max_batching_rows=MAX_BATCHING_ROWS,
        user_defined_context=USER_DEFINED_CONTEXT,
    )
    actual_repr = repr(options)
    assert actual_repr == (
        "RemoteFunctionOptions(connection='connection_string', endpoint='https://some.endpoint', max_batching_rows=50, user_defined_context={'foo': 'bar'})"
    )
