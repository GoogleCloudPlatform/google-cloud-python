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


import time

import google.api_core.exceptions
import google.protobuf

from google.cloud.compute_v1.services.firewalls.client import FirewallsClient
from google.cloud.compute_v1.services.instances.client import InstancesClient
from google.cloud.compute_v1.types import (
    Allowed,
    AttachedDisk,
    AttachedDiskInitializeParams,
    Firewall,
    InsertInstanceRequest,
    Instance,
    NetworkInterface,
    ShieldedInstanceConfig,
)
from tests.system.base import TestBase

PROTOBUF_VERSION = google.protobuf.__version__


class TestComputeSmoke(TestBase):
    def setUp(self) -> None:
        super().setUp()
        self.client = InstancesClient(transport="rest")
        self.name = self.get_unique_name("instance")
        self.instances = []

    def tearDown(self) -> None:
        for instance in self.instances:
            self.client.delete_unary(
                project=self.DEFAULT_PROJECT, zone=self.DEFAULT_ZONE, instance=instance
            )

    def test_insert_instance(self):
        self.insert_instance()
        self.assert_instance()

    def test_aggregated_list(self):
        presented = False
        self.insert_instance()
        result = self.client.aggregated_list(project=self.DEFAULT_PROJECT)
        instances = getattr(result.get("zones/" + self.DEFAULT_ZONE), "instances")
        for item in instances:
            if getattr(item, "name") == self.name:
                presented = True
                break
        self.assertTrue(presented)

    def test_client_error(self):
        with self.assertRaises(expected_exception=ValueError):
            self.client.get(instance=self.name, zone=self.DEFAULT_ZONE)

    def test_api_error(self):
        with self.assertRaises(expected_exception=google.api_core.exceptions.NotFound):
            self.client.get(
                project=self.DEFAULT_PROJECT,
                zone=self.DEFAULT_ZONE,
                instance="nonexistent9999123412314",
            )

    def test_zero_values(self):
        with self.assertRaises(expected_exception=TypeError) as ex:
            self.client.get(instance=self.name, zone=0)
        self.assertIn(
            ("bad argument type for built-in operation"),
            str(ex.exception.args),
        )

    def test_patch(self):
        self.insert_instance()
        instance = self.get_instance()
        self.assertEqual(instance.shielded_instance_config.enable_secure_boot, False)
        op = self.client.stop_unary(
            project=self.DEFAULT_PROJECT, zone=self.DEFAULT_ZONE, instance=self.name
        )
        self.wait_for_zonal_operation(op.name)

        timeout = time.time() + 120  # it takes some time for instance to stop
        while True:
            if time.time() > timeout:
                self.fail("Instance was not stopped")
            instance = self.get_instance()
            if instance.status == "TERMINATED":
                break
            else:
                time.sleep(10)

        resource = ShieldedInstanceConfig()
        resource.enable_secure_boot = True
        op = self.client.update_shielded_instance_config_unary(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance=self.name,
            shielded_instance_config_resource=resource,
        )
        self.wait_for_zonal_operation(op.name)
        patched_instance = self.get_instance()
        self.assertEqual(
            patched_instance.shielded_instance_config.enable_secure_boot, True
        )

    def test_list(self):
        presented = False
        self.insert_instance()
        result = self.client.list(project=self.DEFAULT_PROJECT, zone=self.DEFAULT_ZONE)
        for item in result:
            if getattr(item, "name") == self.name:
                presented = True
                break
        self.assertTrue(presented)

    def test_update_description_empty(self):
        self.insert_instance()
        instance = self.get_instance()
        self.assertEqual(instance.description, "test")
        self.assertEqual(instance.scheduling.min_node_cpus, 0)
        instance.description = ""
        update_op = self.client.update_unary(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance=self.name,
            instance_resource=instance,
        )
        self.wait_for_zonal_operation(update_op.name)
        fetched = self.get_instance()
        self.assertEqual(fetched.description, "")
        self.assertEqual(fetched.scheduling.min_node_cpus, 0)

    def test_update_description_non_ascii(self):
        self.insert_instance()
        instance = self.get_instance()
        self.assertEqual(instance.description, "test")
        instance.description = "тест"
        update_op = self.client.update_unary(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance=self.name,
            instance_resource=instance,
        )
        self.wait_for_zonal_operation(update_op.name)
        fetched = self.get_instance()
        self.assertEqual(fetched.description, "тест")

    def get_instance(self):
        return self.client.get(
            project=self.DEFAULT_PROJECT, zone=self.DEFAULT_ZONE, instance=self.name
        )

    def assert_instance(self):
        instance = self.get_instance()
        self.assertEqual(getattr(instance, "name"), self.name)
        self.assertEqual(len(getattr(instance, "network_interfaces")), 1)
        self.assertEqual(len(getattr(instance, "disks")), 1)

    def insert_instance(self):
        initialize_params = AttachedDiskInitializeParams(source_image=self.DISK_IMAGE)
        disk = AttachedDisk(
            auto_delete=True,
            boot=True,
            type_="PERSISTENT",
            initialize_params=initialize_params,
        )
        network_interface = NetworkInterface(name="default")
        instance = Instance(
            name=self.name,
            description="test",
            disks=[disk],
            machine_type=self.MACHINE_TYPE,
            network_interfaces=[network_interface],
        )

        request = InsertInstanceRequest(
            zone=self.DEFAULT_ZONE,
            project=self.DEFAULT_PROJECT,
            instance_resource=instance,
        )
        operation = self.client.insert_unary(request=request)
        self.wait_for_zonal_operation(operation.name)
        self.instances.append(self.name)


class TestComputeFirewalls(TestBase):
    def setUp(self):
        super().setUp()

    def test_capital_letter_field(self):
        # we want to test a field like "IPProtocol"
        name = self.get_unique_name("firewall")
        client = FirewallsClient()
        firewall = Firewall(
            name=name,
            source_ranges=["0.0.0.0/0"],
            allowed=[Allowed(I_p_protocol="tcp", ports=["80"])],
        )
        op = client.insert_unary(
            project=self.DEFAULT_PROJECT, firewall_resource=firewall
        )
        try:
            self.wait_for_global_operation(op.name)

            fetched = client.get(project=self.DEFAULT_PROJECT, firewall=name)
            self.assertEqual(fetched.allowed[0].I_p_protocol, "tcp")
            self.assertEqual(fetched.allowed[0].ports, ["80"])
        finally:
            client.delete_unary(project=self.DEFAULT_PROJECT, firewall=name)
