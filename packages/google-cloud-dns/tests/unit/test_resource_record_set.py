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


class TestResourceRecordSet(unittest.TestCase):
    @staticmethod
    def _get_target_class():
        from google.cloud.dns.resource_record_set import ResourceRecordSet

        return ResourceRecordSet

    def _make_one(self, *args, **kw):
        return self._get_target_class()(*args, **kw)

    def test_ctor(self):
        zone = _Zone()

        rrs = self._make_one(
            "test.example.com", "CNAME", 3600, ["www.example.com"], zone
        )

        self.assertEqual(rrs.name, "test.example.com")
        self.assertEqual(rrs.record_type, "CNAME")
        self.assertEqual(rrs.ttl, 3600)
        self.assertEqual(rrs.rrdatas, ["www.example.com"])
        self.assertIs(rrs.zone, zone)

    def test_from_api_repr_missing_rrdatas(self):
        zone = _Zone()
        klass = self._get_target_class()

        with self.assertRaises(KeyError):
            klass.from_api_repr(
                {"name": "test.example.com", "type": "CNAME", "ttl": 3600}, zone=zone
            )

    def test_from_api_repr_missing_ttl(self):
        zone = _Zone()
        klass = self._get_target_class()

        with self.assertRaises(KeyError):
            klass.from_api_repr(
                {
                    "name": "test.example.com",
                    "type": "CNAME",
                    "rrdatas": ["www.example.com"],
                },
                zone=zone,
            )

    def test_from_api_repr_missing_type(self):
        zone = _Zone()
        klass = self._get_target_class()

        with self.assertRaises(KeyError):
            klass.from_api_repr(
                {
                    "name": "test.example.com",
                    "ttl": 3600,
                    "rrdatas": ["www.example.com"],
                },
                zone=zone,
            )

    def test_from_api_repr_missing_name(self):
        zone = _Zone()
        klass = self._get_target_class()

        with self.assertRaises(KeyError):
            klass.from_api_repr(
                {"type": "CNAME", "ttl": 3600, "rrdatas": ["www.example.com"]},
                zone=zone,
            )

    def test_from_api_repr_bare(self):
        zone = _Zone()
        RESOURCE = {
            "kind": "dns#resourceRecordSet",
            "name": "test.example.com",
            "type": "CNAME",
            "ttl": "3600",
            "rrdatas": ["www.example.com"],
        }
        klass = self._get_target_class()
        rrs = klass.from_api_repr(RESOURCE, zone=zone)
        self.assertEqual(rrs.name, "test.example.com")
        self.assertEqual(rrs.record_type, "CNAME")
        self.assertEqual(rrs.ttl, 3600)
        self.assertEqual(rrs.rrdatas, ["www.example.com"])
        self.assertIs(rrs.zone, zone)


class _Zone(object):
    pass
