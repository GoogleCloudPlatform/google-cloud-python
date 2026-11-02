# Copyright 2015 Google LLC
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


class TestChanges(unittest.TestCase):
    PROJECT = "project"
    ZONE_NAME = "example.com"
    CHANGES_NAME = "changeset_id"

    @staticmethod
    def _get_target_class():
        from google.cloud.dns.changes import Changes

        return Changes

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _setUpConstants(self):
        from google.cloud._helpers import _NOW, UTC

        self.WHEN = _NOW().replace(tzinfo=UTC)

    def _make_resource(self):
        from google.cloud._helpers import _datetime_to_rfc3339

        when_str = _datetime_to_rfc3339(self.WHEN)
        return {
            "kind": "dns#change",
            "id": self.CHANGES_NAME,
            "startTime": when_str,
            "status": "done",
            "additions": [
                {
                    "name": "test.example.com",
                    "type": "CNAME",
                    "ttl": "3600",
                    "rrdatas": ["www.example.com"],
                }
            ],
            "deletions": [
                {
                    "name": "test.example.com",
                    "type": "CNAME",
                    "ttl": "86400",
                    "rrdatas": ["other.example.com"],
                }
            ],
        }

    def _verifyResourceProperties(self, changes, resource, zone):
        from google.cloud._helpers import _rfc3339_to_datetime

        self.assertEqual(changes.name, resource["id"])
        started = _rfc3339_to_datetime(resource["startTime"])
        self.assertEqual(changes.started, started)
        self.assertEqual(changes.status, resource["status"])

        r_additions = resource.get("additions", ())
        self.assertEqual(len(changes.additions), len(r_additions))
        for found, expected in zip(changes.additions, r_additions):
            self.assertEqual(found.name, expected["name"])
            self.assertEqual(found.record_type, expected["type"])
            self.assertEqual(found.ttl, int(expected["ttl"]))
            self.assertEqual(found.rrdatas, expected["rrdatas"])
            self.assertIs(found.zone, zone)

        r_deletions = resource.get("deletions", ())
        self.assertEqual(len(changes.deletions), len(r_deletions))
        for found, expected in zip(changes.deletions, r_deletions):
            self.assertEqual(found.name, expected["name"])
            self.assertEqual(found.record_type, expected["type"])
            self.assertEqual(found.ttl, int(expected["ttl"]))
            self.assertEqual(found.rrdatas, expected["rrdatas"])
            self.assertIs(found.zone, zone)

    def test_ctor(self):
        zone = _Zone()

        changes = self._make_one(zone)

        self.assertIs(changes.zone, zone)
        self.assertIsNone(changes.name)
        self.assertIsNone(changes.status)
        self.assertIsNone(changes.started)
        self.assertEqual(list(changes.additions), [])
        self.assertEqual(list(changes.deletions), [])

    def test_from_api_repr_missing_additions_deletions(self):
        self._setUpConstants()
        RESOURCE = self._make_resource()
        del RESOURCE["additions"]
        del RESOURCE["deletions"]
        zone = _Zone()
        klass = self._get_target_class()

        changes = klass.from_api_repr(RESOURCE, zone=zone)

        self._verifyResourceProperties(changes, RESOURCE, zone)

    def test_from_api_repr(self):
        self._setUpConstants()
        RESOURCE = self._make_resource()
        zone = _Zone()
        klass = self._get_target_class()

        changes = klass.from_api_repr(RESOURCE, zone=zone)

        self._verifyResourceProperties(changes, RESOURCE, zone)

    def test_name_setter_bad_value(self):
        zone = _Zone()
        changes = self._make_one(zone)
        with self.assertRaises(ValueError):
            changes.name = 12345

    def test_name_setter(self):
        zone = _Zone()
        changes = self._make_one(zone)
        changes.name = "NAME"
        self.assertEqual(changes.name, "NAME")

    def test_add_record_set_invalid_value(self):
        zone = _Zone()
        changes = self._make_one(zone)

        with self.assertRaises(ValueError):
            changes.add_record_set(object())

    def test_add_record_set(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        zone = _Zone()
        changes = self._make_one(zone)
        rrs = ResourceRecordSet(
            "test.example.com", "CNAME", 3600, ["www.example.com"], zone
        )
        changes.add_record_set(rrs)
        self.assertEqual(list(changes.additions), [rrs])

    def test_delete_record_set_invalid_value(self):
        zone = _Zone()
        changes = self._make_one(zone)

        with self.assertRaises(ValueError):
            changes.delete_record_set(object())

    def test_delete_record_set(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        zone = _Zone()
        changes = self._make_one(zone)
        rrs = ResourceRecordSet(
            "test.example.com", "CNAME", 3600, ["www.example.com"], zone
        )
        changes.delete_record_set(rrs)
        self.assertEqual(list(changes.deletions), [rrs])

    def test_create_wo_additions_or_deletions(self):
        self._setUpConstants()
        RESOURCE = self._make_resource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = _Zone(client)
        changes = self._make_one(zone)

        with self.assertRaises(ValueError):
            changes.create()

        self.assertEqual(len(conn._requested), 0)

    def test_create_w_bound_client(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        self._setUpConstants()
        RESOURCE = self._make_resource()
        PATH = "projects/%s/managedZones/%s/changes" % (self.PROJECT, self.ZONE_NAME)
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = _Zone(client)
        changes = self._make_one(zone)
        changes.add_record_set(
            ResourceRecordSet(
                "test.example.com", "CNAME", 3600, ["www.example.com"], zone
            )
        )
        changes.delete_record_set(
            ResourceRecordSet(
                "test.example.com", "CNAME", 86400, ["other.example.com"], zone
            )
        )

        changes.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        SENT = {"additions": RESOURCE["additions"], "deletions": RESOURCE["deletions"]}
        self.assertEqual(req["data"], SENT)
        self._verifyResourceProperties(changes, RESOURCE, zone)

    def test_create_w_alternate_client(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        self._setUpConstants()
        RESOURCE = self._make_resource()
        PATH = "projects/%s/managedZones/%s/changes" % (self.PROJECT, self.ZONE_NAME)
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = _Zone(client1)
        changes = self._make_one(zone)
        changes.add_record_set(
            ResourceRecordSet(
                "test.example.com", "CNAME", 3600, ["www.example.com"], zone
            )
        )
        changes.delete_record_set(
            ResourceRecordSet(
                "test.example.com", "CNAME", 86400, ["other.example.com"], zone
            )
        )

        changes.create(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        SENT = {"additions": RESOURCE["additions"], "deletions": RESOURCE["deletions"]}
        self.assertEqual(req["data"], SENT)
        self._verifyResourceProperties(changes, RESOURCE, zone)

    def test_exists_miss_w_bound_client(self):
        PATH = "projects/%s/managedZones/%s/changes/%s" % (
            self.PROJECT,
            self.ZONE_NAME,
            self.CHANGES_NAME,
        )
        self._setUpConstants()
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        zone = _Zone(client)
        changes = self._make_one(zone)
        changes.name = self.CHANGES_NAME

        self.assertFalse(changes.exists())

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self.assertEqual(req["query_params"], {"fields": "id"})

    def test_exists_hit_w_alternate_client(self):
        PATH = "projects/%s/managedZones/%s/changes/%s" % (
            self.PROJECT,
            self.ZONE_NAME,
            self.CHANGES_NAME,
        )
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = _Zone(client1)
        changes = self._make_one(zone)
        changes.name = self.CHANGES_NAME

        self.assertTrue(changes.exists(client=client2))

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self.assertEqual(req["query_params"], {"fields": "id"})

    def test_reload_w_bound_client(self):
        PATH = "projects/%s/managedZones/%s/changes/%s" % (
            self.PROJECT,
            self.ZONE_NAME,
            self.CHANGES_NAME,
        )
        self._setUpConstants()
        RESOURCE = self._make_resource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = _Zone(client)
        changes = self._make_one(zone)
        changes.name = self.CHANGES_NAME

        changes.reload()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self._verifyResourceProperties(changes, RESOURCE, zone)

    def test_reload_w_alternate_client(self):
        PATH = "projects/%s/managedZones/%s/changes/%s" % (
            self.PROJECT,
            self.ZONE_NAME,
            self.CHANGES_NAME,
        )
        self._setUpConstants()
        RESOURCE = self._make_resource()
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = _Zone(client1)
        changes = self._make_one(zone)
        changes.name = self.CHANGES_NAME

        changes.reload(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self._verifyResourceProperties(changes, RESOURCE, zone)


class _Zone(object):
    def __init__(
        self, client=None, project=TestChanges.PROJECT, name=TestChanges.ZONE_NAME
    ):
        self._client = client
        self.project = project
        self.name = name


class _Client(object):
    def __init__(self, project="project", connection=None):
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
