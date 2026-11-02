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

import unittest


class TestIPFilterHelpers(unittest.TestCase):
    @staticmethod
    def _get_public_network_source_class():
        from google.cloud.storage.ip_filter import PublicNetworkSource

        return PublicNetworkSource

    @staticmethod
    def _get_vpc_network_source_class():
        from google.cloud.storage.ip_filter import VpcNetworkSource

        return VpcNetworkSource

    @staticmethod
    def _get_ip_filter_class():
        from google.cloud.storage.ip_filter import IPFilter

        return IPFilter

    def test_public_network_source_serialization(self):
        pns_class = self._get_public_network_source_class()
        pns = pns_class(allowed_ip_cidr_ranges=["1.2.3.4/32"])
        resource = pns._to_api_resource()
        self.assertEqual(resource, {"allowedIpCidrRanges": ["1.2.3.4/32"]})

    def test_vpc_network_source_serialization(self):
        vns_class = self._get_vpc_network_source_class()
        vns = vns_class(
            network="projects/p/global/networks/n",
            allowed_ip_cidr_ranges=["10.0.0.0/8"],
        )
        resource = vns._to_api_resource()
        self.assertEqual(
            resource,
            {
                "network": "projects/p/global/networks/n",
                "allowedIpCidrRanges": ["10.0.0.0/8"],
            },
        )

    def test_ip_filter_full_serialization(self):
        ip_filter_class = self._get_ip_filter_class()
        pns_class = self._get_public_network_source_class()
        vns_class = self._get_vpc_network_source_class()

        ip_filter = ip_filter_class()
        ip_filter.mode = "Enabled"
        ip_filter.public_network_source = pns_class(
            allowed_ip_cidr_ranges=["1.2.3.4/32"]
        )
        ip_filter.vpc_network_sources.append(
            vns_class(
                network="projects/p/global/networks/n",
                allowed_ip_cidr_ranges=["10.0.0.0/8"],
            )
        )
        ip_filter.allow_all_service_agent_access = True

        resource = ip_filter._to_api_resource()
        expected = {
            "mode": "Enabled",
            "publicNetworkSource": {"allowedIpCidrRanges": ["1.2.3.4/32"]},
            "vpcNetworkSources": [
                {
                    "network": "projects/p/global/networks/n",
                    "allowedIpCidrRanges": ["10.0.0.0/8"],
                }
            ],
            "allowAllServiceAgentAccess": True,
        }
        self.assertEqual(resource, expected)

    def test_ip_filter_deserialization(self):
        ip_filter_class = self._get_ip_filter_class()
        resource = {
            "mode": "Enabled",
            "publicNetworkSource": {"allowedIpCidrRanges": ["1.2.3.4/32"]},
            "allowAllServiceAgentAccess": False,
        }

        ip_filter = ip_filter_class._from_api_resource(resource)

        self.assertEqual(ip_filter.mode, "Enabled")
        self.assertIsNotNone(ip_filter.public_network_source)
        self.assertEqual(
            ip_filter.public_network_source.allowed_ip_cidr_ranges, ["1.2.3.4/32"]
        )
        self.assertEqual(ip_filter.vpc_network_sources, [])
        self.assertIs(ip_filter.allow_all_service_agent_access, False)
