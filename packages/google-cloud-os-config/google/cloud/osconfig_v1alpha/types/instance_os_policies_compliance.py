# -*- coding: utf-8 -*-
# Copyright 2026 Google LLC
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
#
from __future__ import annotations

from typing import MutableMapping, MutableSequence

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.osconfig_v1alpha.types import config_common

__protobuf__ = proto.module(
    package="google.cloud.osconfig.v1alpha",
    manifest={
        "InstanceOSPoliciesCompliance",
        "GetInstanceOSPoliciesComplianceRequest",
        "ListInstanceOSPoliciesCompliancesRequest",
        "ListInstanceOSPoliciesCompliancesResponse",
    },
)


class InstanceOSPoliciesCompliance(proto.Message):
    r"""This API resource represents the OS policies compliance data for a
    Compute Engine virtual machine (VM) instance at a given point in
    time.

    A Compute Engine VM can have multiple OS policy assignments, and
    each assignment can have multiple OS policies. As a result, multiple
    OS policies could be applied to a single VM.

    You can use this API resource to determine both the compliance state
    of your VM as well as the compliance state of an individual OS
    policy.

    For more information, see `View
    compliance <https://cloud.google.com/compute/docs/os-configuration-management/view-compliance>`__.

    Attributes:
        name (str):
            Output only. The ``InstanceOSPoliciesCompliance`` API
            resource name.

            Format:
            ``projects/{project_number}/locations/{location}/instanceOSPoliciesCompliances/{instance_id}``
        instance (str):
            Output only. The Compute Engine VM instance
            name.
        state (google.cloud.osconfig_v1alpha.types.OSPolicyComplianceState):
            Output only. Compliance state of the VM.
        detailed_state (str):
            Output only. Detailed compliance state of the VM. This field
            is populated only when compliance state is ``UNKNOWN``.

            It may contain one of the following values:

            - ``no-compliance-data``: Compliance data is not available
              for this VM.
            - ``no-agent-detected``: OS Config agent is not detected for
              this VM.
            - ``config-not-supported-by-agent``: The version of the OS
              Config agent running on this VM does not support
              configuration management.
            - ``inactive``: VM is not running.
            - ``internal-service-errors``: There were internal service
              errors encountered while enforcing compliance.
            - ``agent-errors``: OS config agent encountered errors while
              enforcing compliance.
        detailed_state_reason (str):
            Output only. The reason for the ``detailed_state`` of the VM
            (if any).
        os_policy_compliances (MutableSequence[google.cloud.osconfig_v1alpha.types.InstanceOSPoliciesCompliance.OSPolicyCompliance]):
            Output only. Compliance data for each ``OSPolicy`` that is
            applied to the VM.
        last_compliance_check_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Timestamp of the last compliance
            check for the VM.
        last_compliance_run_id (str):
            Output only. Unique identifier for the last
            compliance run. This id will be logged by the OS
            config agent during a compliance run and can be
            used for debugging and tracing purpose.
    """

    class OSPolicyCompliance(proto.Message):
        r"""Compliance data for an OS policy

        Attributes:
            os_policy_id (str):
                The OS policy id
            os_policy_assignment (str):
                Reference to the ``OSPolicyAssignment`` API resource that
                the ``OSPolicy`` belongs to.

                Format:
                ``projects/{project_number}/locations/{location}/osPolicyAssignments/{os_policy_assignment_id@revision_id}``
            state (google.cloud.osconfig_v1alpha.types.OSPolicyComplianceState):
                Compliance state of the OS policy.
            os_policy_resource_compliances (MutableSequence[google.cloud.osconfig_v1alpha.types.OSPolicyResourceCompliance]):
                Compliance data for each ``OSPolicyResource`` that is
                applied to the VM.
        """

        os_policy_id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        os_policy_assignment: str = proto.Field(
            proto.STRING,
            number=2,
        )
        state: config_common.OSPolicyComplianceState = proto.Field(
            proto.ENUM,
            number=4,
            enum=config_common.OSPolicyComplianceState,
        )
        os_policy_resource_compliances: MutableSequence[
            config_common.OSPolicyResourceCompliance
        ] = proto.RepeatedField(
            proto.MESSAGE,
            number=5,
            message=config_common.OSPolicyResourceCompliance,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    instance: str = proto.Field(
        proto.STRING,
        number=2,
    )
    state: config_common.OSPolicyComplianceState = proto.Field(
        proto.ENUM,
        number=3,
        enum=config_common.OSPolicyComplianceState,
    )
    detailed_state: str = proto.Field(
        proto.STRING,
        number=4,
    )
    detailed_state_reason: str = proto.Field(
        proto.STRING,
        number=5,
    )
    os_policy_compliances: MutableSequence[OSPolicyCompliance] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=OSPolicyCompliance,
    )
    last_compliance_check_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    last_compliance_run_id: str = proto.Field(
        proto.STRING,
        number=8,
    )


class GetInstanceOSPoliciesComplianceRequest(proto.Message):
    r"""A request message for getting OS policies compliance data for
    the given Compute Engine VM instance.

    Attributes:
        name (str):
            Required. API resource name for instance OS policies
            compliance resource.

            Format:
            ``projects/{project}/locations/{location}/instanceOSPoliciesCompliances/{instance}``

            For ``{project}``, either Compute Engine project-number or
            project-id can be provided. For ``{instance}``, either
            Compute Engine VM instance-id or instance-name can be
            provided.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListInstanceOSPoliciesCompliancesRequest(proto.Message):
    r"""A request message for listing OS policies compliance data for
    all Compute Engine VMs in the given location.

    Attributes:
        parent (str):
            Required. The parent resource name.

            Format: ``projects/{project}/locations/{location}``

            For ``{project}``, either Compute Engine project-number or
            project-id can be provided.
        page_size (int):
            The maximum number of results to return.
        page_token (str):
            A pagination token returned from a previous call to
            ``ListInstanceOSPoliciesCompliances`` that indicates where
            this listing should continue from.
        filter (str):
            If provided, this field specifies the criteria that must be
            met by a ``InstanceOSPoliciesCompliance`` API resource to be
            included in the response.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListInstanceOSPoliciesCompliancesResponse(proto.Message):
    r"""A response message for listing OS policies compliance data
    for all Compute Engine VMs in the given location.

    Attributes:
        instance_os_policies_compliances (MutableSequence[google.cloud.osconfig_v1alpha.types.InstanceOSPoliciesCompliance]):
            List of instance OS policies compliance
            objects.
        next_page_token (str):
            The pagination token to retrieve the next
            page of instance OS policies compliance objects.
    """

    @property
    def raw_page(self):
        return self

    instance_os_policies_compliances: MutableSequence[
        "InstanceOSPoliciesCompliance"
    ] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="InstanceOSPoliciesCompliance",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
