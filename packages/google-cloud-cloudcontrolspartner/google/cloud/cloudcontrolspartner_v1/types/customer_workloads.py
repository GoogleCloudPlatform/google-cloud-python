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

from google.cloud.cloudcontrolspartner_v1.types import (
    completion_state as gcc_completion_state,
)

__protobuf__ = proto.module(
    package="google.cloud.cloudcontrolspartner.v1",
    manifest={
        "Workload",
        "ListWorkloadsRequest",
        "ListWorkloadsResponse",
        "GetWorkloadRequest",
        "WorkloadOnboardingState",
        "WorkloadOnboardingStep",
    },
)


class Workload(proto.Message):
    r"""Contains metadata around the `Workload
    resource <https://cloud.google.com/assured-workloads/docs/reference/rest/Shared.Types/Workload>`__
    in the Assured Workloads API.

    Attributes:
        name (str):
            Identifier. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``
        folder_id (int):
            Output only. Folder id this workload is
            associated with
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time the resource was created.
        folder (str):
            Output only. The name of container folder of
            the assured workload
        workload_onboarding_state (google.cloud.cloudcontrolspartner_v1.types.WorkloadOnboardingState):
            Container for workload onboarding steps.
        is_onboarded (bool):
            Indicates whether a workload is fully
            onboarded.
        key_management_project_id (str):
            The project id of the key management project
            for the workload
        location (str):
            The Google Cloud location of the workload
        partner (google.cloud.cloudcontrolspartner_v1.types.Workload.Partner):
            Partner associated with this workload.
    """

    class Partner(proto.Enum):
        r"""Supported Assured Workloads Partners.

        Values:
            PARTNER_UNSPECIFIED (0):
                Unknown Partner.
            PARTNER_LOCAL_CONTROLS_BY_S3NS (1):
                Enum representing S3NS (Thales) partner.
            PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS (2):
                Enum representing T_SYSTEM (TSI) partner.
            PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT (3):
                Enum representing SIA_MINSAIT (Indra) partner.
            PARTNER_SOVEREIGN_CONTROLS_BY_PSN (4):
                Enum representing PSN (TIM) partner.
            PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT (6):
                Enum representing CNTXT (Kingdom of Saudi
                Arabia) partner.
            PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM (7):
                Enum representing CNXT (Kingdom of Saudi
                Arabia) partner offering without EKM
                provisioning.
        """

        PARTNER_UNSPECIFIED = 0
        PARTNER_LOCAL_CONTROLS_BY_S3NS = 1
        PARTNER_SOVEREIGN_CONTROLS_BY_T_SYSTEMS = 2
        PARTNER_SOVEREIGN_CONTROLS_BY_SIA_MINSAIT = 3
        PARTNER_SOVEREIGN_CONTROLS_BY_PSN = 4
        PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT = 6
        PARTNER_SOVEREIGN_CONTROLS_BY_CNTXT_NO_EKM = 7

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    folder_id: int = proto.Field(
        proto.INT64,
        number=2,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    folder: str = proto.Field(
        proto.STRING,
        number=4,
    )
    workload_onboarding_state: "WorkloadOnboardingState" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="WorkloadOnboardingState",
    )
    is_onboarded: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    key_management_project_id: str = proto.Field(
        proto.STRING,
        number=7,
    )
    location: str = proto.Field(
        proto.STRING,
        number=8,
    )
    partner: Partner = proto.Field(
        proto.ENUM,
        number=9,
        enum=Partner,
    )


class ListWorkloadsRequest(proto.Message):
    r"""Request to list customer workloads.

    Attributes:
        parent (str):
            Required. Parent resource Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}``
        page_size (int):
            The maximum number of workloads to return.
            The service may return fewer than this value. If
            unspecified, at most 500 workloads will be
            returned.
        page_token (str):
            A page token, received from a previous ``ListWorkloads``
            call. Provide this to retrieve the subsequent page.
        filter (str):
            Optional. Filtering results.
        order_by (str):
            Optional. Hint for how to order the results.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class ListWorkloadsResponse(proto.Message):
    r"""Response message for list customer workloads requests.

    Attributes:
        workloads (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.Workload]):
            List of customer workloads
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    workloads: MutableSequence["Workload"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Workload",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetWorkloadRequest(proto.Message):
    r"""Message for getting a customer workload.

    Attributes:
        name (str):
            Required. Format:
            ``organizations/{organization}/locations/{location}/customers/{customer}/workloads/{workload}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class WorkloadOnboardingState(proto.Message):
    r"""Container for workload onboarding steps.

    Attributes:
        onboarding_steps (MutableSequence[google.cloud.cloudcontrolspartner_v1.types.WorkloadOnboardingStep]):
            List of workload onboarding steps.
    """

    onboarding_steps: MutableSequence["WorkloadOnboardingStep"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="WorkloadOnboardingStep",
    )


class WorkloadOnboardingStep(proto.Message):
    r"""Container for workload onboarding information.

    Attributes:
        step (google.cloud.cloudcontrolspartner_v1.types.WorkloadOnboardingStep.Step):
            The onboarding step.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            The starting time of the onboarding step.
        completion_time (google.protobuf.timestamp_pb2.Timestamp):
            The completion time of the onboarding step.
        completion_state (google.cloud.cloudcontrolspartner_v1.types.CompletionState):
            Output only. The completion state of the
            onboarding step.
    """

    class Step(proto.Enum):
        r"""Enum for possible onboarding steps.

        Values:
            STEP_UNSPECIFIED (0):
                Unspecified step.
            EKM_PROVISIONED (1):
                EKM Provisioned step.
            SIGNED_ACCESS_APPROVAL_CONFIGURED (2):
                Signed Access Approval step.
        """

        STEP_UNSPECIFIED = 0
        EKM_PROVISIONED = 1
        SIGNED_ACCESS_APPROVAL_CONFIGURED = 2

    step: Step = proto.Field(
        proto.ENUM,
        number=1,
        enum=Step,
    )
    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    completion_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    completion_state: gcc_completion_state.CompletionState = proto.Field(
        proto.ENUM,
        number=4,
        enum=gcc_completion_state.CompletionState,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
