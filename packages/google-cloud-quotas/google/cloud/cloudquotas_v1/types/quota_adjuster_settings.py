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
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.api.cloudquotas.v1",
    manifest={
        "GetQuotaAdjusterSettingsRequest",
        "UpdateQuotaAdjusterSettingsRequest",
        "QuotaAdjusterSettings",
    },
)


class GetQuotaAdjusterSettingsRequest(proto.Message):
    r"""Request for getting QuotaAdjusterSettings

    Attributes:
        name (str):
            Required. Identifier. Name of the ``quotaAdjusterSettings``
            configuration. Only a single setting per project is
            supported.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateQuotaAdjusterSettingsRequest(proto.Message):
    r"""Request for updating QuotaAdjusterSettings

    Attributes:
        quota_adjuster_settings (google.cloud.cloudquotas_v1.types.QuotaAdjusterSettings):
            Required. The QuotaAdjusterSettings to
            update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
        validate_only (bool):
            Optional. If set to true, checks the syntax
            of the request but doesn't update the quota
            adjuster settings value. Note that although a
            request can be valid, that doesn't guarantee
            that the request will be fulfilled.
    """

    quota_adjuster_settings: "QuotaAdjusterSettings" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="QuotaAdjusterSettings",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    validate_only: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class QuotaAdjusterSettings(proto.Message):
    r"""The QuotaAdjusterSettings resource defines the settings for
    the Quota Adjuster.

    Attributes:
        name (str):
            Identifier. Name of the configuration, in the formats below:

            - For a project:
              projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings
            - For a folder:
              folders/FOLDER_NUMBER/locations/global/quotaAdjusterSettings
            - For an organization:
              organizations/ORGANIZATION_NUMBER/locations/global/quotaAdjusterSettings
        enablement (google.cloud.cloudquotas_v1.types.QuotaAdjusterSettings.Enablement):
            Optional. The configured value of the
            enablement at the given resource.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The timestamp when the
            QuotaAdjusterSettings resource was last updated.
        etag (str):
            Optional. The current ETag of the
            QuotaAdjusterSettings. If an ETag is provided on
            update and does not match the current server's
            ETag in the QuotaAdjusterSettings, the request
            is blocked and returns an ABORTED error. See
            https://google.aip.dev/134#etags for more
            details on ETags.
        inherited (bool):
            Optional. Indicates whether the setting is
            inherited or explicitly specified.
        inherited_from (str):
            Output only. The resource container from which the setting
            is inherited. This refers to the nearest ancestor with
            enablement set (either ENABLED or DISABLED). The value can
            be an organizations/{organization_id}, folders/{folder_id},
            or can be 'default' if no ancestor exists with enablement
            set. The value will be empty when enablement is directly set
            on this container.
    """

    class Enablement(proto.Enum):
        r"""The enablement status of the quota adjuster.

        Values:
            ENABLEMENT_UNSPECIFIED (0):
                The quota adjuster is in an unknown state.
            ENABLED (2):
                The quota adjuster is enabled.
            DISABLED (3):
                The quota adjuster is disabled.
        """

        ENABLEMENT_UNSPECIFIED = 0
        ENABLED = 2
        DISABLED = 3

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    enablement: Enablement = proto.Field(
        proto.ENUM,
        number=2,
        enum=Enablement,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamp_pb2.Timestamp,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=6,
    )
    inherited: bool = proto.Field(
        proto.BOOL,
        number=7,
    )
    inherited_from: str = proto.Field(
        proto.STRING,
        number=8,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
