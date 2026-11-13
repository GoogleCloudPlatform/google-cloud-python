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

from google.cloud.discoveryengine_v1.types import widget_config as gcd_widget_config

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1",
    manifest={
        "GetWidgetConfigRequest",
        "UpdateWidgetConfigRequest",
    },
)


class GetWidgetConfigRequest(proto.Message):
    r"""Request for
    [WidgetConfigService.GetWidgetConfig][google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig]
    method.

    Attributes:
        name (str):
            Required. Full WidgetConfig resource name. Format:
            ``projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/widgetConfigs/{widget_config_id}``
        accept_cache (bool):
            Optional. Whether it's acceptable to load the
            widget config from cache. If set to true, recent
            changes on widget configs may take a few minutes
            to reflect on the end user's view. It's
            recommended to set to true for maturely
            developed widgets, as it improves widget
            performance. Set to false to see changes
            reflected in prod right away, if your widget is
            under development.
        get_widget_config_request_option (google.cloud.discoveryengine_v1.types.GetWidgetConfigRequest.GetWidgetConfigRequestOption):
            Optional. Options for GetWidgetConfigRequest.
        language_code (str):
            Optional. BCP-47 language tag (e.g. "en", "fr-CA"). Used to
            localize human-readable strings in the response, such as the
            model selector ``display_name`` / ``description`` on
            ``WidgetConfig.UiSettings.ModelConfigInfo``. Empty / unset
            falls back to the default language (English).
        model_info_view (google.cloud.discoveryengine_v1.types.ModelInfoView):
            Optional. Selects which view of
            ``WidgetConfig.UiSettings.ModelConfigInfo`` the backend
            computes. ``ADMIN`` is set by the Cloud Console admin
            "Feature Management" page to receive the admin-surfaced
            model set with ``ResolvedModel.admin_view`` populated;
            ``END_USER_MOBILE`` is set by the Gemini Enterprise mobile
            app to receive the mobile model set; unset /
            ``END_USER_WEB`` returns the end-user web selector.
    """

    class GetWidgetConfigRequestOption(proto.Message):
        r"""Options for GetWidgetConfigRequest.

        Attributes:
            turn_off_collection_components (bool):
                Optional. Whether to turn off collection_components in
                WidgetConfig to reduce latency and data transmission.
        """

        turn_off_collection_components: bool = proto.Field(
            proto.BOOL,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    accept_cache: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    get_widget_config_request_option: GetWidgetConfigRequestOption = proto.Field(
        proto.MESSAGE,
        number=3,
        message=GetWidgetConfigRequestOption,
    )
    language_code: str = proto.Field(
        proto.STRING,
        number=4,
    )
    model_info_view: gcd_widget_config.ModelInfoView = proto.Field(
        proto.ENUM,
        number=5,
        enum=gcd_widget_config.ModelInfoView,
    )


class UpdateWidgetConfigRequest(proto.Message):
    r"""Request for
    [WidgetConfigService.UpdateWidgetConfig][google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig]
    method.

    Attributes:
        widget_config (google.cloud.discoveryengine_v1.types.WidgetConfig):
            Required. The
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig]
            to update.

            If the caller does not have permission to update the
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig],
            then a PERMISSION_DENIED error is returned.

            If the
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig]
            to update does not exist, a NOT_FOUND error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [WidgetConfig][google.cloud.discoveryengine.v1.WidgetConfig]
            to update. The following are the only supported fields:

            - [WidgetConfig.enable_autocomplete][google.cloud.discoveryengine.v1.WidgetConfig.enable_autocomplete]

            If not set, all supported fields are updated.
    """

    widget_config: gcd_widget_config.WidgetConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_widget_config.WidgetConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
