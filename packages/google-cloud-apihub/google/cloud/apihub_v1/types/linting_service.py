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

from google.cloud.apihub_v1.types import common_fields

__protobuf__ = proto.module(
    package="google.cloud.apihub.v1",
    manifest={
        "GetStyleGuideRequest",
        "UpdateStyleGuideRequest",
        "GetStyleGuideContentsRequest",
        "LintSpecRequest",
        "StyleGuideContents",
        "StyleGuide",
    },
)


class GetStyleGuideRequest(proto.Message):
    r"""The
    [GetStyleGuide][google.cloud.apihub.v1.LintingService.GetStyleGuide]
    method's request.

    Attributes:
        name (str):
            Required. The name of the spec to retrieve. Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/styleGuide``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateStyleGuideRequest(proto.Message):
    r"""The
    [UpdateStyleGuide][google.cloud.apihub.v1.LintingService.UpdateStyleGuide]
    method's request.

    Attributes:
        style_guide (google.cloud.apihub_v1.types.StyleGuide):
            Required. The Style guide resource to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The list of fields to update.
    """

    style_guide: "StyleGuide" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="StyleGuide",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetStyleGuideContentsRequest(proto.Message):
    r"""The
    [GetStyleGuideContents][google.cloud.apihub.v1.LintingService.GetStyleGuideContents]
    method's request.

    Attributes:
        name (str):
            Required. The name of the StyleGuide whose contents need to
            be retrieved. There is exactly one style guide resource per
            project per location. The expected format is
            ``projects/{project}/locations/{location}/plugins/{plugin}/styleGuide``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class LintSpecRequest(proto.Message):
    r"""The [LintSpec][google.cloud.apihub.v1.LintingService.LintSpec]
    method's request.

    Attributes:
        name (str):
            Required. The name of the spec to be linted. Format:
            ``projects/{project}/locations/{location}/apis/{api}/versions/{version}/specs/{spec}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class StyleGuideContents(proto.Message):
    r"""The style guide contents.

    Attributes:
        contents (bytes):
            Required. The contents of the style guide.
        mime_type (str):
            Required. The mime type of the content.
    """

    contents: bytes = proto.Field(
        proto.BYTES,
        number=1,
    )
    mime_type: str = proto.Field(
        proto.STRING,
        number=2,
    )


class StyleGuide(proto.Message):
    r"""Represents a singleton style guide resource to be used for
    linting Open API specs.

    Attributes:
        name (str):
            Identifier. The name of the style guide.

            Format:
            ``projects/{project}/locations/{location}/plugins/{plugin}/styleGuide``
        linter (google.cloud.apihub_v1.types.Linter):
            Required. Target linter for the style guide.
        contents (google.cloud.apihub_v1.types.StyleGuideContents):
            Required. Input only. The contents of the
            uploaded style guide.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    linter: common_fields.Linter = proto.Field(
        proto.ENUM,
        number=2,
        enum=common_fields.Linter,
    )
    contents: "StyleGuideContents" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="StyleGuideContents",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
