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

from google.ads.admanager_v1.types import cdn_config_messages

__protobuf__ = proto.module(
    package="google.ads.admanager.v1",
    manifest={
        "GetCdnConfigRequest",
        "ListCdnConfigsRequest",
        "ListCdnConfigsResponse",
        "CreateCdnConfigRequest",
        "BatchCreateCdnConfigsRequest",
        "BatchCreateCdnConfigsResponse",
        "UpdateCdnConfigRequest",
        "BatchUpdateCdnConfigsRequest",
        "BatchUpdateCdnConfigsResponse",
        "BatchActivateCdnConfigsRequest",
        "BatchActivateCdnConfigsResponse",
        "BatchArchiveCdnConfigsRequest",
        "BatchArchiveCdnConfigsResponse",
    },
)


class GetCdnConfigRequest(proto.Message):
    r"""Request object for ``GetCdnConfig`` method.

    Attributes:
        name (str):
            Required. The resource name of the CdnConfig. Format:
            ``networks/{network_code}/cdnConfigs/{cdn_config_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListCdnConfigsRequest(proto.Message):
    r"""Request object for ``ListCdnConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent, which owns this collection of
            CdnConfigs. Format: ``networks/{network_code}``
        page_size (int):
            Optional. The maximum number of ``CdnConfigs`` to return.
            The service may return fewer than this value. If
            unspecified, at most 50 ``CdnConfigs`` will be returned. The
            maximum value is 1000; values greater than 1000 will be
            coerced to 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListCdnConfigs`` call. Provide this to retrieve the
            subsequent page.

            When paginating, all other parameters provided to
            ``ListCdnConfigs`` must match the call that provided the
            page token.
        filter (str):
            Optional. Expression to filter the response. See syntax
            details at
            https://developers.google.com/ad-manager/api/beta/filters

            **Filterable fields:**

            - ``cdnConfigStatus``
            - ``cdnConfigType``
            - ``displayName``
            - ``name``
            - ``sourceContentConfig.ingestSettings.urlPrefix``
        order_by (str):
            Optional. Expression to specify sorting
            order. See syntax details at
            https://developers.google.com/ad-manager/api/beta/filters#order
        skip (int):
            Optional. Number of individual resources to
            skip while paginating.
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
    skip: int = proto.Field(
        proto.INT32,
        number=6,
    )


class ListCdnConfigsResponse(proto.Message):
    r"""Response object for ``ListCdnConfigsRequest`` containing matching
    ``CdnConfig`` objects.

    Attributes:
        cdn_configs (MutableSequence[google.ads.admanager_v1.types.CdnConfig]):
            The ``CdnConfig`` objects from the specified network.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages.
        total_size (int):
            Total number of ``CdnConfig`` objects. If a filter was
            included in the request, this reflects the total number
            after the filtering is applied.

            ``total_size`` won't be calculated in the response unless it
            has been included in a response field mask. The response
            field mask can be provided to the method by using the URL
            parameter ``$fields`` or ``fields``, or by using the
            HTTP/gRPC header ``X-Goog-FieldMask``.

            For more information, see
            https://developers.google.com/ad-manager/api/beta/field-masks
    """

    @property
    def raw_page(self):
        return self

    cdn_configs: MutableSequence[cdn_config_messages.CdnConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cdn_config_messages.CdnConfig,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    total_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class CreateCdnConfigRequest(proto.Message):
    r"""Request object for ``CreateCdnConfig`` method.

    Attributes:
        parent (str):
            Required. The parent resource where this ``CdnConfig`` will
            be created. Format: ``networks/{network_code}``
        cdn_config (google.ads.admanager_v1.types.CdnConfig):
            Required. The ``CdnConfig`` to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    cdn_config: cdn_config_messages.CdnConfig = proto.Field(
        proto.MESSAGE,
        number=2,
        message=cdn_config_messages.CdnConfig,
    )


class BatchCreateCdnConfigsRequest(proto.Message):
    r"""Request object for ``BatchCreateCdnConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``CdnConfigs`` will be
            created. Format: ``networks/{network_code}`` The parent
            field in the CreateCdnConfigRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.CreateCdnConfigRequest]):
            Required. The ``CdnConfig`` objects to create. A maximum of
            100 objects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateCdnConfigRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateCdnConfigRequest",
    )


class BatchCreateCdnConfigsResponse(proto.Message):
    r"""Response object for ``BatchCreateCdnConfigs`` method.

    Attributes:
        cdn_configs (MutableSequence[google.ads.admanager_v1.types.CdnConfig]):
            The ``CdnConfig`` objects created.
    """

    cdn_configs: MutableSequence[cdn_config_messages.CdnConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cdn_config_messages.CdnConfig,
    )


class UpdateCdnConfigRequest(proto.Message):
    r"""Request object for ``UpdateCdnConfig`` method.

    Attributes:
        cdn_config (google.ads.admanager_v1.types.CdnConfig):
            Required. The ``CdnConfig`` to update.

            The ``CdnConfig``'s ``name`` is used to identify the
            ``CdnConfig`` to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    cdn_config: cdn_config_messages.CdnConfig = proto.Field(
        proto.MESSAGE,
        number=1,
        message=cdn_config_messages.CdnConfig,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateCdnConfigsRequest(proto.Message):
    r"""Request object for ``BatchUpdateCdnConfigs`` method.

    Attributes:
        parent (str):
            Required. The parent resource where ``CdnConfigs`` will be
            updated. Format: ``networks/{network_code}`` The parent
            field in the UpdateCdnConfigRequest must match this field.
        requests (MutableSequence[google.ads.admanager_v1.types.UpdateCdnConfigRequest]):
            Required. The ``CdnConfig`` objects to update. A maximum of
            100 objects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateCdnConfigRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateCdnConfigRequest",
    )


class BatchUpdateCdnConfigsResponse(proto.Message):
    r"""Response object for ``BatchUpdateCdnConfigs`` method.

    Attributes:
        cdn_configs (MutableSequence[google.ads.admanager_v1.types.CdnConfig]):
            The ``CdnConfig`` objects updated.
    """

    cdn_configs: MutableSequence[cdn_config_messages.CdnConfig] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=cdn_config_messages.CdnConfig,
    )


class BatchActivateCdnConfigsRequest(proto.Message):
    r"""Request message to activate ``CdnConfig`` objects.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``CdnConfig`` objects to
            activate. Format:
            ``networks/{network_code}/cdnConfigs/{cdn_config_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchActivateCdnConfigsResponse(proto.Message):
    r"""Response message for ``BatchActivateCdnConfigs`` method."""


class BatchArchiveCdnConfigsRequest(proto.Message):
    r"""Request message to archive ``CdnConfig`` objects.

    Attributes:
        parent (str):
            Required. Format: ``networks/{network_code}``
        names (MutableSequence[str]):
            Required. The resource names of the ``CdnConfig`` objects to
            archive. Format:
            ``networks/{network_code}/cdnConfigs/{cdn_config_id}``
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    names: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )


class BatchArchiveCdnConfigsResponse(proto.Message):
    r"""Response object for ``BatchArchiveCdnConfigs`` method."""


__all__ = tuple(sorted(__protobuf__.manifest))
