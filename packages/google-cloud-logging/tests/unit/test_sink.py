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


class TestSink(unittest.TestCase):
    PROJECT = "test-project"
    PROJECT_PATH = f"projects/{PROJECT}"
    SINK_NAME = "sink-name"
    FULL_NAME = f"projects/{PROJECT}/sinks/{SINK_NAME}"
    FILTER = "logName:syslog AND severity>=INFO"
    DESTINATION_URI = "faux.googleapis.com/destination"
    WRITER_IDENTITY = "serviceAccount:project-123@example.com"

    @staticmethod
    def _get_target_class():
        from google.cloud.logging import Sink

        return Sink

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        client = _Client(self.PROJECT)
        sink = self._make_one(self.SINK_NAME, client=client)
        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertIsNone(sink.filter_)
        self.assertIsNone(sink.destination)
        self.assertIs(sink.client, client)
        self.assertEqual(sink.parent, self.PROJECT_PATH)
        self.assertEqual(sink.full_name, self.FULL_NAME)
        self.assertEqual(sink.path, f"/{self.FULL_NAME}")

    def test_ctor_explicit(self):
        client = _Client(self.PROJECT)
        parent = "folders/testFolder"
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            parent=parent,
            destination=self.DESTINATION_URI,
            client=client,
        )
        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIs(sink.client, client)
        self.assertEqual(sink.parent, parent)
        self.assertEqual(sink.full_name, f"{parent}/sinks/{self.SINK_NAME}")
        self.assertEqual(sink.path, f"/{parent}/sinks/{self.SINK_NAME}")

    def test_from_api_repr_minimal(self):
        client = _Client(project=self.PROJECT)

        RESOURCE = {"name": self.SINK_NAME, "destination": self.DESTINATION_URI}
        klass = self._get_target_class()
        sink = klass.from_api_repr(RESOURCE, client=client)
        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertIsNone(sink.filter_)
        self.assertIsNone(sink.writer_identity)
        self.assertIs(sink._client, client)
        self.assertEqual(sink.parent, self.PROJECT_PATH)
        self.assertEqual(sink.full_name, self.FULL_NAME)

    def test_from_api_repr_full(self):
        client = _Client(project=self.PROJECT)
        parent = "organizations/my_organization"
        RESOURCE = {
            "name": self.SINK_NAME,
            "destination": self.DESTINATION_URI,
            "filter": self.FILTER,
            "writerIdentity": self.WRITER_IDENTITY,
        }
        klass = self._get_target_class()
        sink = klass.from_api_repr(RESOURCE, client=client, parent=parent)
        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertEqual(sink.writer_identity, self.WRITER_IDENTITY)
        self.assertIs(sink._client, client)
        self.assertEqual(sink.parent, parent)
        self.assertEqual(sink.full_name, f"{parent}/sinks/{self.SINK_NAME}")

    def test_create_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.sinks_api = _DummySinksAPI()
        api._sink_create_response = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
            "writerIdentity": self.WRITER_IDENTITY,
        }
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client,
        )

        sink.create()

        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertEqual(sink.writer_identity, self.WRITER_IDENTITY)
        self.assertEqual(
            api._sink_create_called_with,
            (
                self.PROJECT_PATH,
                self.SINK_NAME,
                self.FILTER,
                self.DESTINATION_URI,
                False,
            ),
        )

    def test_create_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client1,
        )
        api = client2.sinks_api = _DummySinksAPI()
        api._sink_create_response = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
            "writerIdentity": self.WRITER_IDENTITY,
        }

        sink.create(client=client2, unique_writer_identity=True)

        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertEqual(sink.writer_identity, self.WRITER_IDENTITY)
        self.assertEqual(
            api._sink_create_called_with,
            (
                self.PROJECT_PATH,
                self.SINK_NAME,
                self.FILTER,
                self.DESTINATION_URI,
                True,
            ),
        )

    def test_exists_miss_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.sinks_api = _DummySinksAPI()
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client,
        )

        self.assertFalse(sink.exists())

        self.assertEqual(api._sink_get_called_with, (self.FULL_NAME))

    def test_exists_hit_w_alternate_client(self):
        RESOURCE = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
        }
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.sinks_api = _DummySinksAPI()
        api._sink_get_response = RESOURCE
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client1,
        )

        self.assertTrue(sink.exists(client=client2))

        self.assertEqual(api._sink_get_called_with, (self.FULL_NAME))

    def test_reload_w_bound_client(self):
        NEW_DESTINATION_URI = "faux.googleapis.com/other"
        RESOURCE = {"name": self.SINK_NAME, "destination": NEW_DESTINATION_URI}
        client = _Client(project=self.PROJECT)
        api = client.sinks_api = _DummySinksAPI()
        api._sink_get_response = RESOURCE
        sink = self._make_one(self.SINK_NAME, client=client)

        sink.reload()

        self.assertEqual(sink.destination, NEW_DESTINATION_URI)
        self.assertIsNone(sink.filter_)
        self.assertIsNone(sink.writer_identity)
        self.assertEqual(api._sink_get_called_with, (self.FULL_NAME))

    def test_reload_w_alternate_client(self):
        NEW_FILTER = "logName:syslog AND severity>=INFO"
        NEW_DESTINATION_URI = "faux.googleapis.com/other"
        RESOURCE = {
            "name": self.SINK_NAME,
            "filter": NEW_FILTER,
            "destination": NEW_DESTINATION_URI,
            "writerIdentity": self.WRITER_IDENTITY,
        }
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.sinks_api = _DummySinksAPI()
        api._sink_get_response = RESOURCE
        sink = self._make_one(self.SINK_NAME, client=client1)

        sink.reload(client=client2)

        self.assertEqual(sink.destination, NEW_DESTINATION_URI)
        self.assertEqual(sink.filter_, NEW_FILTER)
        self.assertEqual(sink.writer_identity, self.WRITER_IDENTITY)
        self.assertEqual(api._sink_get_called_with, (self.FULL_NAME))

    def test_update_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.sinks_api = _DummySinksAPI()
        api._sink_update_response = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
            "writerIdentity": self.WRITER_IDENTITY,
        }
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client,
        )

        sink.update()

        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertEqual(sink.writer_identity, self.WRITER_IDENTITY)
        self.assertEqual(
            api._sink_update_called_with,
            (self.FULL_NAME, self.FILTER, self.DESTINATION_URI, False),
        )

    def test_update_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.sinks_api = _DummySinksAPI()
        api._sink_update_response = {
            "name": self.SINK_NAME,
            "filter": self.FILTER,
            "destination": self.DESTINATION_URI,
            "writerIdentity": self.WRITER_IDENTITY,
        }
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client1,
        )

        sink.update(client=client2, unique_writer_identity=True)

        self.assertEqual(sink.name, self.SINK_NAME)
        self.assertEqual(sink.filter_, self.FILTER)
        self.assertEqual(sink.destination, self.DESTINATION_URI)
        self.assertEqual(sink.writer_identity, self.WRITER_IDENTITY)
        self.assertEqual(
            api._sink_update_called_with,
            (self.FULL_NAME, self.FILTER, self.DESTINATION_URI, True),
        )

    def test_delete_w_bound_client(self):
        client = _Client(project=self.PROJECT)
        api = client.sinks_api = _DummySinksAPI()
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client,
        )

        sink.delete()

        self.assertEqual(api._sink_delete_called_with, (self.FULL_NAME))

    def test_delete_w_alternate_client(self):
        client1 = _Client(project=self.PROJECT)
        client2 = _Client(project=self.PROJECT)
        api = client2.sinks_api = _DummySinksAPI()
        sink = self._make_one(
            self.SINK_NAME,
            filter_=self.FILTER,
            destination=self.DESTINATION_URI,
            client=client1,
        )

        sink.delete(client=client2)

        self.assertEqual(api._sink_delete_called_with, (self.FULL_NAME))


class _Client(object):
    def __init__(self, project):
        self.project = project


class _DummySinksAPI(object):
    def sink_create(
        self, parent, sink_name, filter_, destination, *, unique_writer_identity=False
    ):
        self._sink_create_called_with = (
            parent,
            sink_name,
            filter_,
            destination,
            unique_writer_identity,
        )
        return self._sink_create_response

    def sink_get(self, sink_name):
        from google.cloud.exceptions import NotFound

        self._sink_get_called_with = sink_name
        try:
            return self._sink_get_response
        except AttributeError:
            raise NotFound("miss")

    def sink_update(
        self, sink_name, filter_, destination, *, unique_writer_identity=False
    ):
        self._sink_update_called_with = (
            sink_name,
            filter_,
            destination,
            unique_writer_identity,
        )
        return self._sink_update_response

    def sink_delete(self, sink_name):
        self._sink_delete_called_with = sink_name
