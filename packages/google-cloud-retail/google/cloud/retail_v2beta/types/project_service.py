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

from google.cloud.retail_v2beta.types import project

__protobuf__ = proto.module(
    package="google.cloud.retail.v2beta",
    manifest={
        "GetAlertConfigRequest",
        "UpdateAlertConfigRequest",
    },
)


class GetAlertConfigRequest(proto.Message):
    r"""Request for
    [ProjectService.GetAlertConfig][google.cloud.retail.v2beta.ProjectService.GetAlertConfig]
    method.

    Attributes:
        name (str):
            Required. Full AlertConfig resource name. Format:
            projects/{project_number}/alertConfig
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateAlertConfigRequest(proto.Message):
    r"""Request for
    [ProjectService.UpdateAlertConfig][google.cloud.retail.v2beta.ProjectService.UpdateAlertConfig]
    method.

    Attributes:
        alert_config (google.cloud.retail_v2beta.types.AlertConfig):
            Required. The
            [AlertConfig][google.cloud.retail.v2beta.AlertConfig] to
            update.

            If the caller does not have permission to update the
            [AlertConfig][google.cloud.retail.v2beta.AlertConfig], then
            a PERMISSION_DENIED error is returned.

            If the [AlertConfig][google.cloud.retail.v2beta.AlertConfig]
            to update does not exist, a NOT_FOUND error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [AlertConfig][google.cloud.retail.v2beta.AlertConfig] to
            update. If not set, all supported fields are updated.
    """

    alert_config: project.AlertConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=project.AlertConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
