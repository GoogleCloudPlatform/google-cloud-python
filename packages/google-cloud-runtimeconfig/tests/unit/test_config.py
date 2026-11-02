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


class TestConfig(unittest.TestCase):
    PROJECT = "PROJECT"
    CONFIG_NAME = "config_name"
    CONFIG_PATH = "projects/%s/configs/%s" % (PROJECT, CONFIG_NAME)

    @staticmethod
    def _get_target_class():
        from google.cloud.runtimeconfig.config import Config

        return Config

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _verifyResourceProperties(self, config, resource):
        from google.cloud.runtimeconfig._helpers import config_name_from_full_name

        if "name" in resource:
            self.assertEqual(config.full_name, resource["name"])
            self.assertEqual(config.name, config_name_from_full_name(resource["name"]))
        if "description" in resource:
            self.assertEqual(config.description, resource["description"])

    def test_ctor(self):
        client = _Client(project=self.PROJECT)
        config = self._make_one(name=self.CONFIG_NAME, client=client)
        self.assertEqual(config.name, self.CONFIG_NAME)
        self.assertEqual(config.project, self.PROJECT)
        self.assertEqual(config.full_name, self.CONFIG_PATH)

    def test_ctor_w_no_name(self):
        client = _Client(project=self.PROJECT)
        config = self._make_one(name=None, client=client)
        with self.assertRaises(ValueError):
            getattr(config, "full_name")

    def test_exists_miss_w_bound_client(self):
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(client=client, name=self.CONFIG_NAME)

        self.assertFalse(config.exists())

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.CONFIG_PATH,))
        self.assertEqual(req["query_params"], {"fields": "name"})

    def test_exists_hit_w_alternate_client(self):
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        config = self._make_one(client=CLIENT1, name=self.CONFIG_NAME)

        self.assertTrue(config.exists(client=CLIENT2))

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.CONFIG_PATH,))
        self.assertEqual(req["query_params"], {"fields": "name"})

    def test_reload_w_empty_resource(self):
        RESOURCE = {}
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        config.reload()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        # Name should not be overwritten if not in the response.
        self.assertEqual(self.CONFIG_NAME, config.name)
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.CONFIG_PATH,))
        self._verifyResourceProperties(config, RESOURCE)

    def test_reload_w_bound_client(self):
        RESOURCE = {"name": self.CONFIG_PATH, "description": "hello"}
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        config.reload()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.CONFIG_PATH,))
        self._verifyResourceProperties(config, RESOURCE)

    def test_reload_w_alternate_client(self):
        RESOURCE = {"name": self.CONFIG_PATH, "description": "hello"}
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        config = self._make_one(name=self.CONFIG_NAME, client=CLIENT1)

        config.reload(client=CLIENT2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (self.CONFIG_PATH,))
        self._verifyResourceProperties(config, RESOURCE)

    def test_variable(self):
        VARIABLE_NAME = "my-variable/abcd"
        VARIABLE_PATH = "%s/variables/%s" % (self.CONFIG_PATH, VARIABLE_NAME)
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        variable = config.variable(VARIABLE_NAME)

        self.assertEqual(variable.name, VARIABLE_NAME)
        self.assertEqual(variable.full_name, VARIABLE_PATH)
        self.assertEqual(len(conn._requested), 0)

    def test_get_variable_w_bound_client(self):
        from google.api_core import datetime_helpers

        VARIABLE_NAME = "my-variable/abcd"
        VARIABLE_PATH = "%s/variables/%s" % (self.CONFIG_PATH, VARIABLE_NAME)
        RESOURCE = {
            "name": VARIABLE_PATH,
            "value": "bXktdmFyaWFibGUtdmFsdWU=",  # base64 my-variable-value
            "updateTime": "2016-04-14T21:21:54.123456789Z",
            "state": "VARIABLE_STATE_UNSPECIFIED",
        }
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        variable = config.get_variable(VARIABLE_NAME)

        self.assertEqual(variable.name, VARIABLE_NAME)
        self.assertEqual(variable.full_name, VARIABLE_PATH)
        DatetimeWithNanoseconds = datetime_helpers.DatetimeWithNanoseconds
        self.assertEqual(
            variable.update_time,
            DatetimeWithNanoseconds.from_rfc3339(RESOURCE["updateTime"]),
        )
        self.assertEqual(variable.state, RESOURCE["state"])

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (VARIABLE_PATH,))

    def test_get_variable_w_notfound(self):
        VARIABLE_NAME = "my-variable/abcd"
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)
        variable = config.get_variable(VARIABLE_NAME)
        self.assertIsNone(variable)

    def test_get_variable_w_alternate_client(self):
        from google.cloud._helpers import _rfc3339_to_datetime

        VARIABLE_NAME = "my-variable/abcd"
        VARIABLE_PATH = "%s/variables/%s" % (self.CONFIG_PATH, VARIABLE_NAME)
        RESOURCE = {
            "name": VARIABLE_PATH,
            "value": "bXktdmFyaWFibGUtdmFsdWU=",  # base64 my-variable-value
            "updateTime": "2016-04-14T21:21:54.5000Z",
            "state": "VARIABLE_STATE_UNSPECIFIED",
        }
        conn1 = _Connection()
        CLIENT1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        CLIENT2 = _Client(project=self.PROJECT, connection=conn2)
        config = self._make_one(client=CLIENT1, name=self.CONFIG_NAME)

        variable = config.get_variable(VARIABLE_NAME, client=CLIENT2)

        self.assertEqual(variable.name, VARIABLE_NAME)
        self.assertEqual(variable.full_name, VARIABLE_PATH)
        self.assertEqual(
            variable.update_time, _rfc3339_to_datetime(RESOURCE["updateTime"])
        )
        self.assertEqual(variable.state, RESOURCE["state"])

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (VARIABLE_PATH,))

    def test_list_variables_empty(self):
        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        iterator = config.list_variables()
        page = next(iterator.pages)
        variables = list(page)
        token = iterator.next_page_token

        self.assertEqual(variables, [])
        self.assertIsNone(token)
        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        PATH = "projects/%s/configs/%s/variables" % (self.PROJECT, self.CONFIG_NAME)
        self.assertEqual(req["path"], "/%s" % (PATH,))

    def test_list_variables_defaults(self):
        from google.cloud._helpers import _rfc3339_to_datetime

        from google.cloud.runtimeconfig.variable import Variable

        VARIABLE_1 = "variable-one"
        VARIABLE_2 = "variable/two"
        PATH = "projects/%s/configs/%s/variables" % (self.PROJECT, self.CONFIG_NAME)
        TOKEN = "TOKEN"
        DATA = {
            "nextPageToken": TOKEN,
            "variables": [
                {
                    "name": "%s/%s" % (PATH, VARIABLE_1),
                    "updateTime": "2016-04-14T21:21:54.5000Z",
                },
                {
                    "name": "%s/%s" % (PATH, VARIABLE_2),
                    "updateTime": "2016-04-21T21:21:54.6000Z",
                },
            ],
        }

        conn = _Connection(DATA)
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        iterator = config.list_variables()
        page = next(iterator.pages)
        variables = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(variables), len(DATA["variables"]))
        for found, expected in zip(variables, DATA["variables"]):
            self.assertIsInstance(found, Variable)
            self.assertEqual(found.full_name, expected["name"])
            self.assertEqual(
                found.update_time, _rfc3339_to_datetime(expected["updateTime"])
            )
        self.assertEqual(token, TOKEN)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (PATH,))
        self.assertNotIn("filter", req["query_params"])

    def test_list_variables_explicit(self):
        from google.cloud._helpers import _rfc3339_to_datetime

        from google.cloud.runtimeconfig.variable import Variable

        VARIABLE_1 = "variable-one"
        VARIABLE_2 = "variable/two"
        PATH = "projects/%s/configs/%s/variables" % (self.PROJECT, self.CONFIG_NAME)
        TOKEN = "TOKEN"
        DATA = {
            "variables": [
                {
                    "name": "%s/%s" % (PATH, VARIABLE_1),
                    "updateTime": "2016-04-14T21:21:54.5000Z",
                },
                {
                    "name": "%s/%s" % (PATH, VARIABLE_2),
                    "updateTime": "2016-04-21T21:21:54.6000Z",
                },
            ]
        }

        conn = _Connection(DATA)
        client = _Client(project=self.PROJECT, connection=conn)
        config = self._make_one(name=self.CONFIG_NAME, client=client)

        iterator = config.list_variables(page_size=3, page_token=TOKEN, client=client)
        page = next(iterator.pages)
        variables = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(variables), len(DATA["variables"]))
        for found, expected in zip(variables, DATA["variables"]):
            self.assertIsInstance(found, Variable)
            self.assertEqual(found.full_name, expected["name"])
            self.assertEqual(
                found.update_time, _rfc3339_to_datetime(expected["updateTime"])
            )
        self.assertIsNone(token)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (PATH,))
        self.assertEqual(req["query_params"], {"pageSize": 3, "pageToken": TOKEN})


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
            return response
