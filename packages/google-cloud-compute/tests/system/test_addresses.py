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

from google.cloud.compute_v1.services.addresses.client import AddressesClient
from google.cloud.compute_v1.types import Address, InsertAddressRequest
from tests.system.base import TestBase


class TestAddresses(TestBase):
    def setUp(self) -> None:
        super().setUp()
        self.client = AddressesClient(transport="rest")
        self.name = self.get_unique_name("address")
        self.addresses = []

    def tearDown(self) -> None:
        for address in self.addresses:
            self.client.delete_unary(
                project=self.DEFAULT_PROJECT,
                region=self.DEFAULT_REGION,
                address=address,
            )

    def insert_address(self):
        address_res = Address()
        address_res.name = self.name

        request = InsertAddressRequest()
        request.project = self.DEFAULT_PROJECT
        request.region = self.DEFAULT_REGION
        request.address_resource = address_res
        operation = self.client.insert_unary(request)
        self.wait_for_regional_operation(operation.name)
        self.addresses.append(self.name)

    def test_create_read(self):
        self.insert_address()
        address = self.client.get(
            project=self.DEFAULT_PROJECT, region=self.DEFAULT_REGION, address=self.name
        )
        self.assertEqual(getattr(address, "name"), self.name)

    def test_list(self):
        presented = False
        self.insert_address()
        result = self.client.list(
            project=self.DEFAULT_PROJECT, region=self.DEFAULT_REGION
        )
        for item in result:
            if getattr(item, "name") == self.name:
                presented = True
                break
        self.assertTrue(presented)
