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

import mock


def _make_credentials():
    import google.auth.credentials

    return mock.Mock(spec=google.auth.credentials.Credentials)


class TestClient(unittest.TestCase):
    PROJECT = "PROJECT"
    ZONE_NAME = "zone-name"

    @staticmethod
    def _get_target_class():
        from google.cloud.dns.client import Client

        return Client

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor_defaults(self):
        from google.api_core.client_info import ClientInfo

        from google.cloud.dns._http import Connection

        creds = _make_credentials()
        http = object()
        client = self._make_one(project=self.PROJECT, credentials=creds, _http=http)
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertIsInstance(client._connection._client_info, ClientInfo)
        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )

    def test_ctor_w_client_info(self):
        from google.api_core.client_info import ClientInfo

        from google.cloud.dns._http import Connection

        client_info = ClientInfo()

        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT, credentials=creds, _http=http, client_info=client_info
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertIs(client._connection._client_info, client_info)

    def test_ctor_w_empty_client_options_object(self):
        from google.api_core.client_info import ClientInfo
        from google.api_core.client_options import ClientOptions

        from google.cloud.dns._http import Connection

        creds = _make_credentials()
        http = object()
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=ClientOptions(),
        )
        self.assertIsInstance(client._connection, Connection)
        self.assertIs(client._connection.credentials, creds)
        self.assertIs(client._connection.http, http)
        self.assertIsInstance(client._connection._client_info, ClientInfo)
        self.assertEqual(
            client._connection.API_BASE_URL, client._connection.DEFAULT_API_ENDPOINT
        )

    def test_ctor_w_client_options_object(self):
        from google.api_core.client_options import ClientOptions

        api_endpoint = "https://foo-dns.googleapis.com"
        creds = _make_credentials()
        http = object()
        client_options = ClientOptions(api_endpoint=api_endpoint)
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=client_options,
        )
        self.assertEqual(client._connection.API_BASE_URL, api_endpoint)

    def test_ctor_w_client_options_dict(self):
        api_endpoint = "https://foo-dns.googleapis.com"
        creds = _make_credentials()
        http = object()
        client_options = {"api_endpoint": api_endpoint}
        client = self._make_one(
            project=self.PROJECT,
            credentials=creds,
            _http=http,
            client_options=client_options,
        )
        self.assertEqual(client._connection.API_BASE_URL, api_endpoint)

    def test_quotas_defaults(self):
        PATH = "projects/%s" % (self.PROJECT,)
        MANAGED_ZONES = 1234
        RRS_PER_RRSET = 23
        RRSETS_PER_ZONE = 345
        RRSET_ADDITIONS = 456
        RRSET_DELETIONS = 567
        TOTAL_SIZE = 67890
        DATA = {
            "quota": {
                "managedZones": MANAGED_ZONES,
                "resourceRecordsPerRrset": RRS_PER_RRSET,
                "rrsetsPerManagedZone": RRSETS_PER_ZONE,
                "rrsetAdditionsPerChange": RRSET_ADDITIONS,
                "rrsetDeletionsPerChange": RRSET_DELETIONS,
                "totalRrdataSizePerChange": TOTAL_SIZE,
            }
        }
        CONVERTED = {key: int(value) for key, value in DATA["quota"].items()}
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = _Connection(DATA)

        quotas = client.quotas()

        self.assertEqual(quotas, CONVERTED)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_quotas_w_kind_key(self):
        PATH = "projects/%s" % (self.PROJECT,)
        MANAGED_ZONES = 1234
        RRS_PER_RRSET = 23
        RRSETS_PER_ZONE = 345
        RRSET_ADDITIONS = 456
        RRSET_DELETIONS = 567
        TOTAL_SIZE = 67890
        DATA = {
            "quota": {
                "managedZones": MANAGED_ZONES,
                "resourceRecordsPerRrset": RRS_PER_RRSET,
                "rrsetsPerManagedZone": RRSETS_PER_ZONE,
                "rrsetAdditionsPerChange": RRSET_ADDITIONS,
                "rrsetDeletionsPerChange": RRSET_DELETIONS,
                "totalRrdataSizePerChange": TOTAL_SIZE,
                "whitelistedKeySpecs": [
                    {
                        "keyType": "keySigning",
                        "algorithm": "rsasha512",
                        "keyLength": 2048,
                    }
                ],
            }
        }
        CONVERTED = DATA["quota"]
        WITH_KIND = {"quota": DATA["quota"].copy()}
        WITH_KIND["quota"]["kind"] = "dns#quota"
        WITH_KIND["quota"]["whitelistedKeySpecs"][0]["kind"] = "dns#dnsKeySpec"
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = _Connection(WITH_KIND)

        quotas = client.quotas()

        self.assertEqual(quotas, CONVERTED)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_list_zones_defaults(self):
        from google.cloud.dns.zone import ManagedZone

        ID_1 = "123"
        ZONE_1 = "zone_one"
        DNS_1 = "one.example.com"
        ID_2 = "234"
        ZONE_2 = "zone_two"
        DNS_2 = "two.example.com"
        PATH = "projects/%s/managedZones" % (self.PROJECT,)
        TOKEN = "TOKEN"
        DATA = {
            "nextPageToken": TOKEN,
            "managedZones": [
                {
                    "kind": "dns#managedZone",
                    "id": ID_1,
                    "name": ZONE_1,
                    "dnsName": DNS_1,
                },
                {
                    "kind": "dns#managedZone",
                    "id": ID_2,
                    "name": ZONE_2,
                    "dnsName": DNS_2,
                },
            ],
        }
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = _Connection(DATA)

        iterator = client.list_zones()
        page = next(iterator.pages)
        zones = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(zones), len(DATA["managedZones"]))
        for found, expected in zip(zones, DATA["managedZones"]):
            self.assertIsInstance(found, ManagedZone)
            self.assertEqual(found.zone_id, expected["id"])
            self.assertEqual(found.name, expected["name"])
            self.assertEqual(found.dns_name, expected["dnsName"])
        self.assertEqual(token, TOKEN)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)

    def test_list_zones_explicit(self):
        from google.cloud.dns.zone import ManagedZone

        ID_1 = "123"
        ZONE_1 = "zone_one"
        DNS_1 = "one.example.com"
        ID_2 = "234"
        ZONE_2 = "zone_two"
        DNS_2 = "two.example.com"
        PATH = "projects/%s/managedZones" % (self.PROJECT,)
        TOKEN = "TOKEN"
        DATA = {
            "managedZones": [
                {
                    "kind": "dns#managedZone",
                    "id": ID_1,
                    "name": ZONE_1,
                    "dnsName": DNS_1,
                },
                {
                    "kind": "dns#managedZone",
                    "id": ID_2,
                    "name": ZONE_2,
                    "dnsName": DNS_2,
                },
            ]
        }
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        conn = client._connection = _Connection(DATA)

        iterator = client.list_zones(max_results=3, page_token=TOKEN)
        page = next(iterator.pages)
        zones = list(page)
        token = iterator.next_page_token

        self.assertEqual(len(zones), len(DATA["managedZones"]))
        for found, expected in zip(zones, DATA["managedZones"]):
            self.assertIsInstance(found, ManagedZone)
            self.assertEqual(found.zone_id, expected["id"])
            self.assertEqual(found.name, expected["name"])
            self.assertEqual(found.dns_name, expected["dnsName"])
        self.assertIsNone(token)

        self.assertEqual(len(conn._requested), 1)
        req = conn._requested[0]
        self.assertEqual(req["method"], "GET")
        self.assertEqual(req["path"], "/%s" % PATH)
        self.assertEqual(req["query_params"], {"maxResults": 3, "pageToken": TOKEN})

    def test_zone_explicit(self):
        from google.cloud.dns.zone import ManagedZone

        DESCRIPTION = "DESCRIPTION"
        DNS_NAME = "test.example.com"
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        zone = client.zone(self.ZONE_NAME, DNS_NAME, DESCRIPTION)
        self.assertIsInstance(zone, ManagedZone)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertEqual(zone.dns_name, DNS_NAME)
        self.assertEqual(zone.description, DESCRIPTION)
        self.assertIs(zone._client, client)

    def test_zone_w_dns_name_wo_description(self):
        from google.cloud.dns.zone import ManagedZone

        DNS_NAME = "test.example.com"
        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        zone = client.zone(self.ZONE_NAME, DNS_NAME)
        self.assertIsInstance(zone, ManagedZone)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertEqual(zone.dns_name, DNS_NAME)
        self.assertEqual(zone.description, DNS_NAME)
        self.assertIs(zone._client, client)

    def test_zone_wo_dns_name(self):
        from google.cloud.dns.zone import ManagedZone

        creds = _make_credentials()
        client = self._make_one(self.PROJECT, creds)
        zone = client.zone(self.ZONE_NAME)
        self.assertIsInstance(zone, ManagedZone)
        self.assertEqual(zone.name, self.ZONE_NAME)
        self.assertIsNone(zone.dns_name)
        self.assertIsNone(zone.description)
        self.assertIs(zone._client, client)


class _Connection(object):
    def __init__(self, *responses):
        self._responses = responses
        self._requested = []

    def api_request(self, **kw):
        self._requested.append(kw)
        response, self._responses = self._responses[0], self._responses[1:]
        return response
