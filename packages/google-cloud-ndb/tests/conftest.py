# Copyright 2018 Google LLC
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

"""py.test shared testing configuration.

This defines fixtures (expected to be) shared across different test
modules.
"""

import os
from unittest import mock

import pytest

from google.cloud import environment_vars
from google.cloud.ndb import _eventloop, model, utils
from google.cloud.ndb import context as context_module
from google.cloud.ndb import global_cache as global_cache_module

utils.DEBUG = True


class TestingEventLoop(_eventloop.EventLoop):
    def call_soon(self, callback, *args, **kwargs):
        """For testing, call the callback immediately."""
        callback(*args, **kwargs)


@pytest.fixture(autouse=True)
def reset_state(environ):
    """Reset module and class level runtime state.

    To make sure that each test has the same starting conditions, we reset
    module or class level datastructures that maintain runtime state.

    This resets:

    - ``model.Property._FIND_METHODS_CACHE``
    - ``model.Model._kind_map``
    """
    yield
    model.Property._FIND_METHODS_CACHE.clear()
    model.Model._kind_map.clear()
    global_cache_module._InProcessGlobalCache.cache.clear()


@pytest.fixture
def environ():
    """Copy of ``os.environ``"""
    original = os.environ
    environ_copy = original.copy()
    os.environ = environ_copy
    yield environ_copy
    os.environ = original


@pytest.fixture(autouse=True)
def initialize_environment(request, environ):
    """Set environment variables to default values.

    There are some variables, like ``GOOGLE_APPLICATION_CREDENTIALS``, that we
    want to reset for unit tests but not system tests. This fixture introspects
    the current request, determines whether it's in a unit test, or not, and
    does the right thing.
    """
    if request.module.__name__.startswith("tests.unit"):  # pragma: NO COVER
        environ.pop(environment_vars.GCD_DATASET, None)
        environ.pop(environment_vars.GCD_HOST, None)
        environ.pop("GOOGLE_APPLICATION_CREDENTIALS", None)


@pytest.fixture
def context_factory():
    def context(**kwargs):
        client = mock.Mock(
            project="testing",
            database=None,
            namespace=None,
            spec=("project", "database", "namespace"),
            stub=mock.Mock(spec=()),
        )
        context = context_module.Context(
            client,
            eventloop=TestingEventLoop(),
            datastore_policy=True,
            legacy_data=False,
            **kwargs,
        )
        return context

    return context


@pytest.fixture
def context(context_factory):
    return context_factory()


@pytest.fixture
def in_context(context):
    assert not context_module._state.context
    with context.use():
        yield context
    assert not context_module._state.context


@pytest.fixture
def database():
    return "testdb"


@pytest.fixture
def namespace():
    return "UnitTest"


@pytest.fixture
def client_context(namespace, database):
    from google.cloud import ndb

    client = ndb.Client()
    context_manager = client.context(
        cache_policy=False, legacy_data=False, database=database, namespace=namespace
    )
    with context_manager as context:
        yield context


@pytest.fixture
def global_cache(context):
    assert not context_module._state.context

    cache = global_cache_module._InProcessGlobalCache()
    with context.new(global_cache=cache).use():
        yield cache

    assert not context_module._state.context
