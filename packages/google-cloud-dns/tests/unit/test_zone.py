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


class TestManagedZone(unittest.TestCase):
    PROJECT = "project"
    ZONE_NAME = "zone-name"
    DESCRIPTION = "ZONE DESCRIPTION"
    DNS_NAME = "test.example.com"

    @staticmethod
    def _get_target_class():
        from google.cloud.dns.zone import ManagedZone

        return ManagedZone

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def _setUpConstants(self):
        import datetime

        from google.cloud._helpers import UTC

        year = 2015
        month = 7
        day = 24
        hour = 19
        minute = 53
        seconds = 19
        micros = 6000

        self.WHEN_STR = "%d-%02d-%02dT%02d:%02d:%02d.%06dZ" % (
            year,
            month,
            day,
            hour,
            minute,
            seconds,
            micros,
        )
        self.WHEN = datetime.datetime(
            year, month, day, hour, minute, seconds, micros, tzinfo=UTC
        )
        self.ZONE_ID = 12345

    def _make_resource(self):
        self._setUpConstants()
        return {
            "name": self.ZONE_NAME,
            "dnsName": self.DNS_NAME,
            "description": self.DESCRIPTION,
            "id": self.ZONE_ID,
            "creationTime": self.WHEN_STR,
            "nameServers": [
                "ns-cloud1.googledomains.com",
                "ns-cloud2.googledomains.com",
            ],
        }

    def _verifyReadonlyResourceProperties(self, zone, resource):
        self.assertEqual(zone.zone_id, resource.get("id"))

        if "creationTime" in resource:
            self.assertEqual(zone.created, self.WHEN)
        else:
            self.assertIsNone(zone.created)

        if "nameServers" in resource:
            self.assertEqual(zone.name_servers, resource["nameServers"])
        else:
            self.assertIsNone(zone.name_servers)

    def _verifyResourceProperties(self, zone, resource):
        self._verifyReadonlyResourceProperties(zone, resource)

        self.assertEqual(zone.name, resource.get("name"))
        self.assertEqual(zone.dns_name, resource.get("dnsName"))
        self.assertEqual(zone.description, resource.get("description"))
        self.assertEqual(zone.zone_id, resource.get("id"))
        self.assertEqual(zone.name_server_set, resource.get("nameServerSet"))

    def test_ctor_defaults(self):
        zone = self._make_one(self.ZONE_NAME)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertIsNone(zone.dns_name)
        self.assertIsNone(zone._client)

        with self.assertRaises(AttributeError):
            (zone.project)

        with self.assertRaises(AttributeError):
            (zone.path)

        self.assertIsNone(zone.zone_id)
        self.assertIsNone(zone.created)
        self.assertIsNone(zone.description)

    def test_ctor_wo_description(self):
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertEqual(zone.dns_name, self.DNS_NAME)
        self.assertIs(zone._client, client)
        self.assertEqual(zone.project, client.project)
        self.assertEqual(
            zone.path, "/projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        )
        self.assertIsNone(zone.zone_id)
        self.assertIsNone(zone.created)
        self.assertEqual(zone.description, self.DNS_NAME)

    def test_ctor_explicit(self):
        DESCRIPTION = "DESCRIPTION"
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client, DESCRIPTION)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertEqual(zone.dns_name, self.DNS_NAME)
        self.assertIs(zone._client, client)
        self.assertEqual(zone.project, client.project)
        self.assertEqual(
            zone.path, "/projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        )
        self.assertIsNone(zone.zone_id)
        self.assertIsNone(zone.created)
        self.assertEqual(zone.description, DESCRIPTION)

    def test_from_api_repr_missing_identity(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = {}
        klass = self._get_target_class()
        with self.assertRaises(KeyError):
            klass.from_api_repr(RESOURCE, client=client)

    def test_from_api_repr_bare(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = {"name": self.ZONE_NAME, "dnsName": self.DNS_NAME}
        klass = self._get_target_class()
        zone = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(zone._client, client)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_from_api_repr_w_properties(self):
        self._setUpConstants()
        client = _Client(self.PROJECT)
        RESOURCE = self._make_resource()
        klass = self._get_target_class()
        zone = klass.from_api_repr(RESOURCE, client=client)
        self.assertIs(zone._client, client)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_description_setter_bad_value(self):
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        with self.assertRaises(ValueError):
            zone.description = 12345

    def test_description_setter(self):
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        zone.description = "DESCRIPTION"
        self.assertEqual(zone.description, "DESCRIPTION")

    def test_name_server_set_setter_bad_value(self):
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        with self.assertRaises(ValueError):
            zone.name_server_set = 12345

    def test_name_server_set_setter(self):
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        zone.name_server_set = "NAME_SERVER_SET"
        self.assertEqual(zone.name_server_set, "NAME_SERVER_SET")

    def test_resource_record_set(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        RRS_NAME = "other.example.com"
        RRS_TYPE = "CNAME"
        TTL = 3600
        RRDATAS = ["www.example.com"]
        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        rrs = zone.resource_record_set(RRS_NAME, RRS_TYPE, TTL, RRDATAS)
        self.assertIsInstance(rrs, ResourceRecordSet)
        self.assertEqual(rrs.name, RRS_NAME)
        self.assertEqual(rrs.record_type, RRS_TYPE)
        self.assertEqual(rrs.ttl, TTL)
        self.assertEqual(rrs.rrdatas, RRDATAS)
        self.assertIs(rrs.zone, zone)

    def test_changes(self):
        from google.cloud.dns.changes import Changes

        client = _Client(self.PROJECT)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)
        changes = zone.changes()
        self.assertIsInstance(changes, Changes)
        self.assertIs(changes.zone, zone)

    def test_create_w_bound_client(self):
        PATH = "projects/%s/managedZones" % self.PROJECT
        RESOURCE = self._make_resource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)

        zone.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        SENT = {
            "name": self.ZONE_NAME,
            "dnsName": self.DNS_NAME,
            "description": self.DNS_NAME,
        }
        self.assertEqual(req["data"], SENT)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_create_w_alternate_client(self):
        PATH = "projects/%s/managedZones" % self.PROJECT
        DESCRIPTION = "DESCRIPTION"
        NAME_SERVER_SET = "NAME_SERVER_SET"
        RESOURCE = self._make_resource()
        RESOURCE["nameServerSet"] = NAME_SERVER_SET
        RESOURCE["description"] = DESCRIPTION
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client1)
        zone.name_server_set = NAME_SERVER_SET
        zone.description = DESCRIPTION

        zone.create(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        SENT = {
            "name": self.ZONE_NAME,
            "dnsName": self.DNS_NAME,
            "nameServerSet": NAME_SERVER_SET,
            "description": DESCRIPTION,
        }
        self.assertEqual(req["data"], SENT)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_create_wo_dns_name_or_description(self):
        from google.cloud.exceptions import BadRequest

        PATH = "projects/%s/managedZones" % self.PROJECT

        _requested = []

        def _api_request(**kw):
            _requested.append(kw)
            raise BadRequest("missing dns_name / description")

        conn = _Connection()
        conn.api_request = _api_request
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, client=client)

        with self.assertRaises(BadRequest):
            zone.create()

        self.assertEqual(len(_requested), 1)
        req = _requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        SENT = {"name": self.ZONE_NAME}
        self.assertEqual(req["data"], SENT)

    def test_create_w_missing_output_properties(self):
        # In the wild, the resource returned from 'zone.create' sometimes
        # lacks 'creationTime' / 'lastModifiedTime'
        PATH = "projects/%s/managedZones" % (self.PROJECT,)
        RESOURCE = self._make_resource()
        del RESOURCE["creationTime"]
        del RESOURCE["id"]
        del RESOURCE["nameServers"]
        self.WHEN = None
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)

        zone.create()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "POST")
        self.assertEqual(req["path"], "/%s" % PATH)
        SENT = {
            "name": self.ZONE_NAME,
            "dnsName": self.DNS_NAME,
            "description": self.DNS_NAME,
        }
        self.assertEqual(req["data"], SENT)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_exists_miss_w_bound_client(self):
        PATH = "projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        conn = _Connection()
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)

        self.assertFalse(zone.exists())

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_exists_hit_w_alternate_client(self):
        PATH = "projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client1)

        self.assertTrue(zone.exists(client=client2))

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_reload_w_bound_client(self):
        PATH = "projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        RESOURCE = self._make_resource()
        conn = _Connection(RESOURCE)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, client=client)

        zone.reload()

        self.assertEqual(zone.dns_name, self.DNS_NAME)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_reload_w_alternate_client(self):
        PATH = "projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        RESOURCE = self._make_resource()
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(RESOURCE)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client1)

        zone.reload(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self._verifyResourceProperties(zone, RESOURCE)

    def test_delete_w_bound_client(self):
        PATH = "projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        conn = _Connection({})
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)

        zone.delete()

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "DELETE")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_delete_w_alternate_client(self):
        PATH = "projects/%s/managedZones/%s" % (self.PROJECT, self.ZONE_NAME)
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection({})
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client1)

        zone.delete(client=client2)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "DELETE")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_list_resource_record_sets_defaults(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        PATH = "projects/%s/managedZones/%s/rrsets" % (self.PROJECT, self.ZONE_NAME)
        TOKEN = "TOKEN"
        NAME_1 = "www.example.com"
        TYPE_1 = "A"
        TTL_1 = "86400"
        RRDATAS_1 = ["123.45.67.89"]
        NAME_2 = "alias.example.com"
        TYPE_2 = "CNAME"
        TTL_2 = "3600"
        RRDATAS_2 = ["www.example.com"]
        DATA = {
            "nextPageToken": TOKEN,
            "rrsets": [
                {
                    "kind": "dns#resourceRecordSet",
                    "name": NAME_1,
                    "type": TYPE_1,
                    "ttl": TTL_1,
                    "rrdatas": RRDATAS_1,
                },
                {
                    "kind": "dns#resourceRecordSet",
                    "name": NAME_2,
                    "type": TYPE_2,
                    "ttl": TTL_2,
                    "rrdatas": RRDATAS_2,
                },
            ],
        }
        conn = _Connection(DATA)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)

        iterator = zone.list_resource_record_sets()
        self.assertIs(zone, iterator.zone)
        page = next(iterator.pages)
        rrsets = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(rrsets), len(DATA["rrsets"]))
        for found, expected in zip(rrsets, DATA["rrsets"]):
            self.assertIsInstance(found, ResourceRecordSet)
            self.assertEqual(found.name, expected["name"])
            self.assertEqual(found.record_type, expected["type"])
            self.assertEqual(found.ttl, int(expected["ttl"]))
            self.assertEqual(found.rrdatas, expected["rrdatas"])
        self.assertEqual(token, TOKEN)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_list_resource_record_sets_explicit(self):
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        PATH = "projects/%s/managedZones/%s/rrsets" % (self.PROJECT, self.ZONE_NAME)
        TOKEN = "TOKEN"
        NAME_1 = "www.example.com"
        TYPE_1 = "A"
        TTL_1 = "86400"
        RRDATAS_1 = ["123.45.67.89"]
        NAME_2 = "alias.example.com"
        TYPE_2 = "CNAME"
        TTL_2 = "3600"
        RRDATAS_2 = ["www.example.com"]
        DATA = {
            "rrsets": [
                {
                    "kind": "dns#resourceRecordSet",
                    "name": NAME_1,
                    "type": TYPE_1,
                    "ttl": TTL_1,
                    "rrdatas": RRDATAS_1,
                },
                {
                    "kind": "dns#resourceRecordSet",
                    "name": NAME_2,
                    "type": TYPE_2,
                    "ttl": TTL_2,
                    "rrdatas": RRDATAS_2,
                },
            ]
        }
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(DATA)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client1)

        iterator = zone.list_resource_record_sets(
            max_results=3, page_token=TOKEN, client=client2
        )
        self.assertIs(zone, iterator.zone)
        page = next(iterator.pages)
        rrsets = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(rrsets), len(DATA["rrsets"]))
        for found, expected in zip(rrsets, DATA["rrsets"]):
            self.assertIsInstance(found, ResourceRecordSet)
            self.assertEqual(found.name, expected["name"])
            self.assertEqual(found.record_type, expected["type"])
            self.assertEqual(found.ttl, int(expected["ttl"]))
            self.assertEqual(found.rrdatas, expected["rrdatas"])
        self.assertIsNone(token)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self.assertEqual(req["query_params"], {"maxResults": 3, "pageToken": TOKEN})

    def _get_changes(self, token, changes_name):
        from google.cloud._helpers import _datetime_to_rfc3339

        name_1 = "www.example.com"
        type_1 = "A"
        ttl_1 = "86400"
        rrdatas_1 = ["123.45.67.89"]
        name_2 = "alias.example.com"
        type_2 = "CNAME"
        ttl_2 = "3600"
        rrdatas_2 = ["www.example.com"]
        result = {
            "changes": [
                {
                    "kind": "dns#change",
                    "id": changes_name,
                    "status": "pending",
                    "startTime": _datetime_to_rfc3339(self.WHEN),
                    "additions": [
                        {
                            "kind": "dns#resourceRecordSet",
                            "name": name_1,
                            "type": type_1,
                            "ttl": ttl_1,
                            "rrdatas": rrdatas_1,
                        }
                    ],
                    "deletions": [
                        {
                            "kind": "dns#change",
                            "name": name_2,
                            "type": type_2,
                            "ttl": ttl_2,
                            "rrdatas": rrdatas_2,
                        }
                    ],
                }
            ]
        }
        if token is not None:
            result["nextPageToken"] = token
        return result

    def test_list_changes_defaults(self):
        from google.cloud.dns.changes import Changes
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        self._setUpConstants()
        path = "projects/%s/managedZones/%s/changes" % (self.PROJECT, self.ZONE_NAME)
        token = "TOKEN"
        changes_name = "changeset_id"
        data = self._get_changes(token, changes_name)

        conn = _Connection(data)
        client = _Client(project=self.PROJECT, connection=conn)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client)

        iterator = zone.list_changes()
        self.assertIs(zone, iterator.zone)
        page = next(iterator.pages)
        changes = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(changes), len(data["changes"]))
        for found, expected in zip(changes, data["changes"]):
            self.assertIsInstance(found, Changes)
            self.assertEqual(found.name, changes_name)
            self.assertEqual(found.status, "pending")
            self.assertEqual(found.started, self.WHEN)

            self.assertEqual(len(found.additions), len(expected["additions"]))
            for found_rr, expected_rr in zip(found.additions, expected["additions"]):
                self.assertIsInstance(found_rr, ResourceRecordSet)
                self.assertEqual(found_rr.name, expected_rr["name"])
                self.assertEqual(found_rr.record_type, expected_rr["type"])
                self.assertEqual(found_rr.ttl, int(expected_rr["ttl"]))
                self.assertEqual(found_rr.rrdatas, expected_rr["rrdatas"])

            self.assertEqual(len(found.deletions), len(expected["deletions"]))
            for found_rr, expected_rr in zip(found.deletions, expected["deletions"]):
                self.assertIsInstance(found_rr, ResourceRecordSet)
                self.assertEqual(found_rr.name, expected_rr["name"])
                self.assertEqual(found_rr.record_type, expected_rr["type"])
                self.assertEqual(found_rr.ttl, int(expected_rr["ttl"]))
                self.assertEqual(found_rr.rrdatas, expected_rr["rrdatas"])

        self.assertEqual(token, token)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (path,))

    def test_list_changes_explicit(self):
        from google.cloud.dns.changes import Changes
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        self._setUpConstants()
        path = "projects/%s/managedZones/%s/changes" % (self.PROJECT, self.ZONE_NAME)
        changes_name = "changeset_id"
        data = self._get_changes(None, changes_name)
        conn1 = _Connection()
        client1 = _Client(project=self.PROJECT, connection=conn1)
        conn2 = _Connection(data)
        client2 = _Client(project=self.PROJECT, connection=conn2)
        zone = self._make_one(self.ZONE_NAME, self.DNS_NAME, client1)

        page_token = "TOKEN"
        iterator = zone.list_changes(
            max_results=3, page_token=page_token, client=client2
        )
        self.assertIs(zone, iterator.zone)
        page = next(iterator.pages)
        changes = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(changes), len(data["changes"]))
        for found, expected in zip(changes, data["changes"]):
            self.assertIsInstance(found, Changes)
            self.assertEqual(found.name, changes_name)
            self.assertEqual(found.status, "pending")
            self.assertEqual(found.started, self.WHEN)

            self.assertEqual(len(found.additions), len(expected["additions"]))
            for found_rr, expected_rr in zip(found.additions, expected["additions"]):
                self.assertIsInstance(found_rr, ResourceRecordSet)
                self.assertEqual(found_rr.name, expected_rr["name"])
                self.assertEqual(found_rr.record_type, expected_rr["type"])
                self.assertEqual(found_rr.ttl, int(expected_rr["ttl"]))
                self.assertEqual(found_rr.rrdatas, expected_rr["rrdatas"])

            self.assertEqual(len(found.deletions), len(expected["deletions"]))
            for found_rr, expected_rr in zip(found.deletions, expected["deletions"]):
                self.assertIsInstance(found_rr, ResourceRecordSet)
                self.assertEqual(found_rr.name, expected_rr["name"])
                self.assertEqual(found_rr.record_type, expected_rr["type"])
                self.assertEqual(found_rr.ttl, int(expected_rr["ttl"]))
                self.assertEqual(found_rr.rrdatas, expected_rr["rrdatas"])

        self.assertIsNone(token)

        self.assertEqual(len(conn1._requested), 0)
        self.assertEqual(len(conn2._requested), 1)
        req = conn2._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % (path,))
        self.assertEqual(
            req["query_params"], {"maxResults": 3, "pageToken": page_token}
        )


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
