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


class TestVariable(unittest.TestCase):
    PROJECT = "PROJECT"
    CONFIG_NAME = "config_name"
    VARIABLE_NAME = "variable_name"
    PATH = "projects/%s/configs/%s/variables/%s" % (PROJECT, CONFIG_NAME, VARIABLE_NAME)

    @staticmethod
    def _get_target_class():
        from google.cloud.runtimeconfig.variable import Variable

        return Variable

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _verifyResourceProperties(self, variable, resource):
        import base64

        from google.api_core import datetime_helpers

        if "name" in resource:
            self.assertEqual(variable.full_name, resource["name"])

        if "value" in resource:
            self.assertEqual(variable.value, base64.b64decode(resource["value"]))
        else:
            self.assertIsNone(variable.value)

        if "text" in resource:
            self.assertEqual(variable.text, resource["text"])
        else:
            self.assertIsNone(variable.text)

        if "state" in resource:
            self.assertEqual(variable.state, resource["state"])

        if "updateTime" in resource:
            self.assertEqual(
                variable.update_time,
                datetime_helpers.DatetimeWithNanoseconds.from_rfc3339(
                    resource["updateTime"]
                ),
            )
        else:
            self.assertIsNone(variable.update_time)

    def test_ctor(self):
        from google.cloud.runtimeconfig.config import Config
        from google.cloud.runtimeconfig.variable import STATE_UNSPECIFIED

        client = _Client(project=self.PROJECT)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=self.VARIABLE_NAME, config=config)
        self.assertEqual(variable.name, self.VARIABLE_NAME)
        self.assertEqual(variable.full_name, self.PATH)
        self.assertEqual(variable.path, "/%s" % (self.PATH,))
        self.assertEqual(variable.state, STATE_UNSPECIFIED)
        self.assertIs(variable.client, client)

    def test_ctor_w_no_name(self):
        from google.cloud.runtimeconfig.config import Config

        client = _Client(project=self.PROJECT)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=None, config=config)
        with self.assertRaises(ValueError):
            getattr(variable, "full_name")

    def test_exists_miss_w_bound_client(self):
        from google.cloud.runtimeconfig.config import Config

        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=self.VARIABLE_NAME, config=config)

        self.assertFalse(variable.exists())

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.PATH,))
        self.assertEqual(req["query_params"], {"fields": "name"})

    def test_exists_hit_w_alternate_client(self):
        from google.cloud.runtimeconfig.config import Config

        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        CONFIG1 = Config(name=self.CONFIG_NAME, client=CLIENT1)
        conn2 = _Connection({})
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        variable = self._make_one(name=self.VARIABLE_NAME, config=CONFIG1)

        self.assertTrue(variable.exists(client=CLIENT2))

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.PATH,))
        self.assertEqual(req["query_params"], {"fields": "name"})

    def test_create_no_data(self):
        from google.cloud.runtimeconfig.config import Config
        from google.cloud.runtimeconfig.exceptions import Error

        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.variable(self.VARIABLE_NAME)
        with self.assertRaises(Error) as ctx:
            variable.create()
        self.assertEqual("No text or value set.", str(ctx.exception))

    def test_create_conflict(self):
        from google.cloud.exceptions import Conflict

        from google.cloud.runtimeconfig.config import Config

        conn = _Connection(Conflict("test"))
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.variable(self.VARIABLE_NAME)
        variable.text = "foo"
        self.assertFalse(variable.create())

    def test_create_text(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {
            "name": self.PATH,
            "text": "foo",
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "UPDATED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.variable(self.VARIABLE_NAME)
        variable.text = "foo"
        result = variable.create()
        self.assertTrue(result)
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(
            req["path"],
            "/projects/%s/configs/%s/variables" % (self.PROJECT, self.CONFIG_NAME),
        )
        self._verifyResourceProperties(variable, RESOURCE)

    def test_create_value(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {
            "name": self.PATH,
            "value": "bXktdmFyaWFibGUtdmFsdWU=",  # base64 my-variable-value
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "UPDATED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.variable(self.VARIABLE_NAME)
        variable.value = b"my-variable-value"
        result = variable.create()
        self.assertTrue(result)
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(
            req["path"],
            "/projects/%s/configs/%s/variables" % (self.PROJECT, self.CONFIG_NAME),
        )
        self._verifyResourceProperties(variable, RESOURCE)

    def test_update_text_conflict(self):
        from google.cloud.runtimeconfig.config import Config
        from google.cloud.runtimeconfig.exceptions import Error

        RESOURCE = {
            "name": self.PATH,
            "value": "bXktdmFyaWFibGUtdmFsdWU=",  # base64 my-variable-value
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "UPDATED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.get_variable(self.VARIABLE_NAME)
        with self.assertRaises(Error) as ctx:
            variable.text = "bar"
        self.assertEqual("Value and text are mutually exclusive.", str(ctx.exception))

    def test_update_value_conflict(self):
        from google.cloud.runtimeconfig.config import Config
        from google.cloud.runtimeconfig.exceptions import Error

        RESOURCE = {
            "name": self.PATH,
            "text": "foo",
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "UPDATED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.get_variable(self.VARIABLE_NAME)
        with self.assertRaises(Error) as ctx:
            variable.value = b"bar"
        self.assertEqual("Value and text are mutually exclusive.", str(ctx.exception))

    def test_update_not_found(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {
            "name": self.PATH,
            "text": "foo",
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "UPDATED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.get_variable(self.VARIABLE_NAME)
        self.assertFalse(variable.update())

    def test_update_text(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {
            "name": self.PATH,
            "text": "foo",
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "UPDATED",
        }
        RESOURCE_UPD = RESOURCE.copy()
        RESOURCE_UPD["text"] = "bar"
        conn = _Connection(RESOURCE, RESOURCE_UPD)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = config.get_variable(self.VARIABLE_NAME)
        variable.text = "bar"
        result = variable.update()
        self.assertTrue(result)
        self.assertEqual(len(conn._requested), 2)
        req = conn._requested[1]
        self.assertEqual(req["method"], "PUT")
        self.assertEqual(req["path"], "/%s" % self.PATH)
        self._verifyResourceProperties(variable, RESOURCE_UPD)

    def test_reload_w_bound_client(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {
            "name": self.PATH,
            "value": "bXktdmFyaWFibGUtdmFsdWU=",  # base64 my-variable-value
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "VARIABLE_STATE_UNSPECIFIED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=self.VARIABLE_NAME, config=config)

        variable.reload()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.PATH,))
        self._verifyResourceProperties(variable, RESOURCE)

    def test_reload_w_empty_resource(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {}
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=self.VARIABLE_NAME, config=config)

        variable.reload()

        # Name should not be overwritten.
        self.assertEqual(self.VARIABLE_NAME, variable.name)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.PATH,))
        self._verifyResourceProperties(variable, RESOURCE)

    def test_reload_w_alternate_client(self):
        from google.cloud.runtimeconfig.config import Config

        RESOURCE = {
            "name": self.PATH,
            "value": "bXktdmFyaWFibGUtdmFsdWU=",  # base64 my-variable-value
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "VARIABLE_STATE_UNSPECIFIED",
        }
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        CONFIG1 = Config(name=self.CONFIG_NAME, client=CLIENT1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        variable = self._make_one(name=self.VARIABLE_NAME, config=CONFIG1)

        variable.reload(client=CLIENT2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.PATH,))
        self._verifyResourceProperties(variable, RESOURCE)

    def test_with_microseconds(self):
        from google.cloud.runtimeconfig.config import Config

        resource = {"updateTime": "2016-04-14T21:21:54.123456Z"}
        conn = _Connection(resource)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=self.VARIABLE_NAME, config=config)
        variable.reload(client=client)
        self._verifyResourceProperties(variable, resource)

    def test_with_nanoseconds(self):
        from google.cloud.runtimeconfig.config import Config

        resource = {"updateTime": "2016-04-14T21:21:54.123456789Z"}
        conn = _Connection(resource)
        client = _Client(project=self.PROJECT, connection=conn)
        config = Config(name=self.CONFIG_NAME, client=client)
        variable = self._make_one(name=self.VARIABLE_NAME, config=config)
        variable.reload(client=client)
        self._verifyResourceProperties(variable, resource)


class _Client(object):
    _connection = None

    def __init__(self, project, connection=None):
        self.project = project
        self._connection = connection


class _Connection(object):
    def __init__(self, *responses):
        self._responses = responses
        self._requested = []

    def api_request(self, **kw):
        from google.cloud.exceptions import NotFound

        self._requested.append(kw)

        try:
            response, self._responses = self._responses[0], self._responses[1:]
        except IndexError:
            raise NotFound("miss")
        else:
            if issubclass(type(response), Exception):
                raise response
            return response
