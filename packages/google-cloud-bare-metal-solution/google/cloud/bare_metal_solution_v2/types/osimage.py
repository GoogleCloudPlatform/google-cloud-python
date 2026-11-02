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

import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.baremetalsolution.v2",
    manifest={
        "OSImage",
        "ListOSImagesRequest",
        "ListOSImagesResponse",
    },
)


class OSImage(proto.Message):
    r"""Operation System image.

    Attributes:
        name (str):
            Output only. OS Image's unique name.
        code (str):
            OS Image code.
        description (str):
            OS Image description.
        applicable_instance_types (MutableSequence[str]):
            Instance types this image is applicable to. `Available
            types <https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations>`__
        supported_network_templates (MutableSequence[str]):
            Network templates that can be used with this
            OS Image.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    code: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    applicable_instance_types: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=4,
    )
    supported_network_templates: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class ListOSImagesRequest(proto.Message):
    r"""Request for getting all available OS images.

    Attributes:
        parent (str):
            Required. Parent value for
            ListProvisioningQuotasRequest.
        page_size (int):
            Requested page size. The server might return fewer items
            than requested. If unspecified, server will pick an
            appropriate default. Notice that page_size field is not
            supported and won't be respected in the API request for now,
            will be updated when pagination is supported.
        page_token (str):
            A token identifying a page of results from
            the server.
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


class ListOSImagesResponse(proto.Message):
    r"""Request for getting all available OS images.

    Attributes:
        os_images (MutableSequence[google.cloud.bare_metal_solution_v2.types.OSImage]):
            The OS images available.
        next_page_token (str):
            Token to retrieve the next page of results,
            or empty if there are no more results in the
            list.
    """

    @property
    def raw_page(self):
        return self

    os_images: MutableSequence["OSImage"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="OSImage",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
