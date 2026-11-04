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

from google.cloud.discoveryengine_v1.types import data_connector as gcd_data_connector

__protobuf__ = proto.module(
    package="google.cloud.discoveryengine.v1",
    manifest={
        "SetUpDataConnectorRequest",
        "SetUpDataConnectorMetadata",
        "GetDataConnectorRequest",
        "UpdateDataConnectorRequest",
    },
)


class SetUpDataConnectorRequest(proto.Message):
    r"""Request for
    [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
    method.

    Attributes:
        parent (str):
            Required. The parent of
            [Collection][google.cloud.discoveryengine.v1.Collection], in
            the format of ``projects/{project}/locations/{location}``.
        collection_id (str):
            Required. The ID to use for the
            [Collection][google.cloud.discoveryengine.v1.Collection],
            which will become the final component of the
            [Collection][google.cloud.discoveryengine.v1.Collection]'s
            resource name. A new
            [Collection][google.cloud.discoveryengine.v1.Collection] is
            created as part of the
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            setup.
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            is a singleton resource under
            [Collection][google.cloud.discoveryengine.v1.Collection],
            managing all
            [DataStore][google.cloud.discoveryengine.v1.DataStore]s of
            the
            [Collection][google.cloud.discoveryengine.v1.Collection].

            Should conform to
            `RFC-1034 <https://tools.ietf.org/html/rfc1034>`__ standard
            with a length limit of 63 characters. Otherwise, an
            ``INVALID_ARGUMENT`` error is returned.
        collection_display_name (str):
            Required. The display name of the
            [Collection][google.cloud.discoveryengine.v1.Collection].

            Should be human readable, used to display collections in the
            Console Dashboard. UTF-8 encoded string with limit of 1024
            characters.
        data_connector (google.cloud.discoveryengine_v1.types.DataConnector):
            Required. The
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            to initialize in the newly created
            [Collection][google.cloud.discoveryengine.v1.Collection].
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    collection_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    collection_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    data_connector: gcd_data_connector.DataConnector = proto.Field(
        proto.MESSAGE,
        number=4,
        message=gcd_data_connector.DataConnector,
    )


class SetUpDataConnectorMetadata(proto.Message):
    r"""Metadata for
    [DataConnectorService.SetUpDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector]
    method.

    """


class GetDataConnectorRequest(proto.Message):
    r"""Request for
    [DataConnectorService.GetDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector]
    method.

    Attributes:
        name (str):
            Required. Full resource name of
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector],
            such as
            ``projects/{project}/locations/{location}/collections/{collection_id}/dataConnector``.

            If the caller does not have permission to access the
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector],
            regardless of whether or not it exists, a
            ``PERMISSION_DENIED`` error is returned.

            If the requested
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            does not exist, a ``NOT_FOUND`` error is returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataConnectorRequest(proto.Message):
    r"""Request message for
    [DataConnectorService.UpdateDataConnector][google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector]
    method.

    Attributes:
        data_connector (google.cloud.discoveryengine_v1.types.DataConnector):
            Required. The
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            to update.

            If the caller does not have permission to update the
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector],
            regardless of whether or not it exists, a
            ``PERMISSION_DENIED`` error is returned.

            If the
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            does not exist, a ``NOT_FOUND`` error is returned.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Indicates which fields in the provided
            [DataConnector][google.cloud.discoveryengine.v1.DataConnector]
            to update.

            Supported field paths include:

            - ``refresh_interval``
            - ``params``
            - ``auto_run_disabled``
            - ``action_config``
            - ``action_config.action_params``
            - ``action_config.service_name``
            - ``destination_configs``
            - ``blocking_reasons``
            - ``sync_mode``
            - ``incremental_sync_disabled``
            - ``incremental_refresh_interval``
            - ``data_protection_policy``

            Note: Support for these fields may vary depending on the
            connector type. For example, not all connectors support
            ``destination_configs``.

            If an unsupported or unknown field path is provided, the
            request will return an ``INVALID_ARGUMENT`` error.
    """

    data_connector: gcd_data_connector.DataConnector = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcd_data_connector.DataConnector,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
