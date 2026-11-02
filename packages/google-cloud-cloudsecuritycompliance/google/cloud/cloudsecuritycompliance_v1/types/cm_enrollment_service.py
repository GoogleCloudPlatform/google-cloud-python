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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.cloudsecuritycompliance.v1",
    manifest={
        "UpdateCmEnrollmentRequest",
        "CalculateEffectiveCmEnrollmentRequest",
        "CmEnrollment",
        "CalculateEffectiveCmEnrollmentResponse",
        "AuditConfig",
    },
)


class UpdateCmEnrollmentRequest(proto.Message):
    r"""The request message for [UpdateCmEnrollment][].

    Attributes:
        cm_enrollment (google.cloud.cloudsecuritycompliance_v1.types.CmEnrollment):
            Required. The Compliance Manager enrollment to update. The
            ``name`` field is used to identify the settings that you
            want to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields that you want to
            update.
    """

    cm_enrollment: "CmEnrollment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CmEnrollment",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class CalculateEffectiveCmEnrollmentRequest(proto.Message):
    r"""The request message for [CalculateEffectiveCmEnrollment][].

    Attributes:
        name (str):
            Required. The name of the Compliance Manager enrollment to
            calculate.

            Supported formats are the following:

            - ``organizations/{organization_id}/locations/{location}/cmEnrollment``
            - ``folders/{folder_id}/locations/{location}/cmEnrollment``
            - ``projects/{project_id}/locations/{location}/cmEnrollment``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CmEnrollment(proto.Message):
    r"""The settings for Compliance Manager at a specific resource
    scope.=

    Attributes:
        name (str):
            Identifier. The name of the Compliance Manager enrollment.

            Supported formats are the following:

            - ``organizations/{organization_id}/locations/{location}/cmEnrollment``
            - ``folders/{folder_id}/locations/{location}/cmEnrollment``
            - ``projects/{project_id}/locations/{location}/cmEnrollment``
        enrolled (bool):
            Optional. Whether the resource is enrolled in
            Compliance Manager. This setting is inherited by
            all descendants.
        audit_config (google.cloud.cloudsecuritycompliance_v1.types.AuditConfig):
            Optional. The audit configuration for
            Compliance Manager. If set at a scope, this
            configuration overrides any inherited audit
            configuration.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enrolled: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    audit_config: "AuditConfig" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AuditConfig",
    )


class CalculateEffectiveCmEnrollmentResponse(proto.Message):
    r"""The response message for [CalculateEffectiveCmEnrollment][].

    Attributes:
        cm_enrollment (google.cloud.cloudsecuritycompliance_v1.types.CmEnrollment):
            The effective Compliance Manager enrollment
            for the resource.
    """

    cm_enrollment: "CmEnrollment" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="CmEnrollment",
    )


class AuditConfig(proto.Message):
    r"""The audit configuration for Compliance Manager.

    Attributes:
        destinations (MutableSequence[google.cloud.cloudsecuritycompliance_v1.types.AuditConfig.CmEligibleDestination]):
            Required. The list of destinations that can
            be selected for uploading audit reports to.
    """

    class CmEligibleDestination(proto.Message):
        r"""The destination details where audit reports are
        uploaded.


        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            gcs_bucket (str):
                The Cloud Storage bucket where audit reports and evidences
                can be uploaded. The format is ``gs://{bucket_name}``.

                This field is a member of `oneof`_ ``cm_eligible_destinations``.
        """

        gcs_bucket: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="cm_eligible_destinations",
        )

    destinations: MutableSequence[CmEligibleDestination] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=CmEligibleDestination,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
