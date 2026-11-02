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

from google.cloud.compute_v1.services.instance_group_managers.client import (
    InstanceGroupManagersClient,
)
from google.cloud.compute_v1.services.instance_templates.client import (
    InstanceTemplatesClient,
)
from google.cloud.compute_v1.services.instances.client import InstancesClient
from google.cloud.compute_v1.types import (
    AttachedDisk,
    AttachedDiskInitializeParams,
    InsertInstanceRequest,
    Instance,
    InstanceGroupManager,
    InstanceTemplate,
    NetworkInterface,
)
from tests.system.base import TestBase


class TestInstanceGroups(TestBase):
    def setUp(self):
        super().setUp()
        self.instances = []
        self.igms = []
        self.templates = []
        self.inst_client = InstancesClient(transport="rest")
        self.name = self.get_unique_name("instance")
        self.igm_client = InstanceGroupManagersClient()
        self.template_client = InstanceTemplatesClient()

    def tearDown(self) -> None:
        for igm in self.igms:
            op = self.igm_client.delete_unary(
                project=self.DEFAULT_PROJECT,
                zone=self.DEFAULT_ZONE,
                instance_group_manager=igm,
            )
            self.wait_for_zonal_operation(op.name)
        for instance in self.instances:
            op = self.inst_client.delete_unary(
                project=self.DEFAULT_PROJECT, zone=self.DEFAULT_ZONE, instance=instance
            )
        for template in self.templates:
            op = self.template_client.delete_unary(
                project=self.DEFAULT_PROJECT, instance_template=template
            )

    def test_instance_group_resize(self):
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
        operation = self.inst_client.insert_unary(request=request)
        self.wait_for_zonal_operation(operation.name)
        self.instances.append(self.name)

        template_name = self.get_unique_name("template")
        igm_name = self.get_unique_name("igm")

        instance = operation.target_link

        template_resource = InstanceTemplate(
            name=template_name, source_instance=instance
        )
        operation = self.template_client.insert_unary(
            project=self.DEFAULT_PROJECT, instance_template_resource=template_resource
        )
        self.wait_for_global_operation(operation.name)
        self.templates.append(template_name)
        template = operation.target_link

        igm_resource = InstanceGroupManager(
            base_instance_name="gapicinst",
            instance_template=template,
            name=igm_name,
            target_size=0,
        )
        operation = self.igm_client.insert_unary(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance_group_manager_resource=igm_resource,
        )
        self.wait_for_zonal_operation(operation.name)
        self.igms.append(igm_name)

        instance_group = self.igm_client.get(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance_group_manager=igm_name,
        )
        self.assertEqual(instance_group.target_size, 0)

        resize_op = self.igm_client.resize_unary(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            size=1,
            instance_group_manager=igm_name,
        )
        self.wait_for_zonal_operation(resize_op.name)

        instance_group = self.igm_client.get(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance_group_manager=igm_name,
        )
        self.assertEqual(instance_group.target_size, 1)

        resize_0_op = self.igm_client.resize_unary(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            size=0,
            instance_group_manager=igm_name,
        )
        self.wait_for_zonal_operation(resize_0_op.name)
        igm = self.igm_client.get(
            project=self.DEFAULT_PROJECT,
            zone=self.DEFAULT_ZONE,
            instance_group_manager=igm_name,
        )
        self.assertEqual(igm.target_size, 0)
