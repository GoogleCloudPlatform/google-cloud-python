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

from google.cloud.retail_v2beta.types import serving_config as gcr_serving_config

__protobuf__ = proto.module(
    package="google.cloud.retail.v2beta",
    manifest={
        "CreateServingConfigRequest",
        "UpdateServingConfigRequest",
        "DeleteServingConfigRequest",
        "GetServingConfigRequest",
        "ListServingConfigsRequest",
        "ListServingConfigsResponse",
        "AddControlRequest",
        "RemoveControlRequest",
    },
)


class CreateServingConfigRequest(proto.Message):
    r"""Request for CreateServingConfig method.

    Attributes:
        parent (str):
            Required. Full resource name of parent. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}``
        serving_config (google.cloud.retail_v2beta.types.ServingConfig):
            Required. The ServingConfig to create.
        serving_config_id (str):
            Required. The ID to use for the ServingConfig, which will
            become the final component of the ServingConfig's resource
            name.

            This value should be 4-63 characters, and valid characters
            are /[a-z][0-9]-\_/.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serving_config: gcr_serving_config.ServingConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcr_serving_config.ServingConfig,
    )
    serving_config_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateServingConfigRequest(proto.Message):
    r"""Request for UpdateServingConfig method.

    Attributes:
        serving_config (google.cloud.retail_v2beta.types.ServingConfig):
            Required. The ServingConfig to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [ServingConfig][google.cloud.retail.v2beta.ServingConfig] to
            update. The following are NOT supported:

            - [ServingConfig.name][google.cloud.retail.v2beta.ServingConfig.name]

            If not set, all supported fields are updated.
    """

    serving_config: gcr_serving_config.ServingConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_serving_config.ServingConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteServingConfigRequest(proto.Message):
    r"""Request for DeleteServingConfig method.

    Attributes:
        name (str):
            Required. The resource name of the ServingConfig to delete.
            Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class GetServingConfigRequest(proto.Message):
    r"""Request for GetServingConfig method.

    Attributes:
        name (str):
            Required. The resource name of the ServingConfig to get.
            Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListServingConfigsRequest(proto.Message):
    r"""Request for ListServingConfigs method.

    Attributes:
        parent (str):
            Required. The catalog resource name. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}``
        page_size (int):
            Optional. Maximum number of results to
            return. If unspecified, defaults to 100. If a
            value greater than 100 is provided, at most 100
            results are returned.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListServingConfigs`` call. Provide this to retrieve the
            subsequent page.
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


class ListServingConfigsResponse(proto.Message):
    r"""Response for ListServingConfigs method.

    Attributes:
        serving_configs (MutableSequence[google.cloud.retail_v2beta.types.ServingConfig]):
            All the ServingConfigs for a given catalog.
        next_page_token (str):
            Pagination token, if not returned indicates
            the last page.
    """

    @property
    def raw_page(self):
        return self

    serving_configs: MutableSequence[gcr_serving_config.ServingConfig] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcr_serving_config.ServingConfig,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class AddControlRequest(proto.Message):
    r"""Request for AddControl method.

    Attributes:
        serving_config (str):
            Required. The source ServingConfig resource name . Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}``
        control_id (str):
            Required. The id of the control to apply. Assumed to be in
            the same catalog as the serving config - if id is not found
            a NOT_FOUND error is returned.
    """

    serving_config: str = proto.Field(
        proto.STRING,
        number=1,
    )
    control_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


class RemoveControlRequest(proto.Message):
    r"""Request for RemoveControl method.

    Attributes:
        serving_config (str):
            Required. The source ServingConfig resource name . Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}``
        control_id (str):
            Required. The id of the control to apply.
            Assumed to be in the same catalog as the serving
            config.
    """

    serving_config: str = proto.Field(
        proto.STRING,
        number=1,
    )
    control_id: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
