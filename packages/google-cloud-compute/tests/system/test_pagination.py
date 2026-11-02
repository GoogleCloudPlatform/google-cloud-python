# Copyright 2021 Google LLC
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

import collections

from google.cloud.compute_v1.services.accelerator_types.client import (
    AcceleratorTypesClient,
)
from google.cloud.compute_v1.services.zones.client import ZonesClient
from google.cloud.compute_v1.types import (
    AggregatedListAcceleratorTypesRequest,
    ListZonesRequest,
)
from tests.system.base import TestBase


class TestComputePagination(TestBase):
    def setUp(self) -> None:
        super().setUp()
        self.client = ZonesClient()

    def test_max_results(self):
        request = ListZonesRequest()
        request.max_results = 1
        request.project = self.DEFAULT_PROJECT
        result = self.client.list(request=request)
        self.assertEqual(len(getattr(result, "items")), 1)

    def test_next_page_token(self):
        request = ListZonesRequest()
        request.max_results = 1
        request.project = self.DEFAULT_PROJECT
        result = self.client.list(request=request)

        token_request = ListZonesRequest()
        token_request.max_results = 1
        token_request.project = self.DEFAULT_PROJECT
        token_request.page_token = getattr(result, "next_page_token")
        token_result = self.client.list(request=token_request)
        self.assertNotEqual(getattr(result, "items"), getattr(token_result, "items"))

    def test_filter(self):
        request = ListZonesRequest()
        request.project = self.DEFAULT_PROJECT
        request.filter = "name = us-central1-a"
        result = self.client.list(request=request)
        description = getattr(getattr(result, "items")[0], "description")
        self.assertEqual(len(getattr(result, "items")), 1)
        self.assertEqual(description, "us-central1-a")

    def test_auto_paging(self):
        request = ListZonesRequest()
        request.max_results = 1
        request.project = self.DEFAULT_PROJECT
        request.filter = "name = us-*"
        result = self.client.list(request=request)
        presented = False
        for item in result:
            desc = getattr(item, "description")
            if desc == self.DEFAULT_ZONE:
                presented = True
                break
        self.assertTrue(presented)


class TestPaginationAggregatedList(TestBase):
    def setUp(self) -> None:
        super().setUp()

    def test_auto_paging_map_response(self):
        client = AcceleratorTypesClient()
        request = AggregatedListAcceleratorTypesRequest(
            project=self.DEFAULT_PROJECT, max_results=100
        )
        result = client.aggregated_list(request=request)
        zone_acc_types = collections.defaultdict(list)
        for zone, types in result:
            zone_acc_types[zone].extend(at.name for at in types.accelerator_types)
        default_zone = "zones/" + self.DEFAULT_ZONE
        self.assertIn("nvidia-tesla-t4", zone_acc_types[default_zone])
