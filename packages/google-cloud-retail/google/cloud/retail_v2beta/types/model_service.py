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

from google.cloud.retail_v2beta.types import model as gcr_model

__protobuf__ = proto.module(
    package="google.cloud.retail.v2beta",
    manifest={
        "CreateModelRequest",
        "UpdateModelRequest",
        "GetModelRequest",
        "PauseModelRequest",
        "ResumeModelRequest",
        "ListModelsRequest",
        "DeleteModelRequest",
        "ListModelsResponse",
        "TuneModelRequest",
        "CreateModelMetadata",
        "TuneModelMetadata",
        "TuneModelResponse",
    },
)


class CreateModelRequest(proto.Message):
    r"""Request for creating a model.

    Attributes:
        parent (str):
            Required. The parent resource under which to create the
            model. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}``
        model (google.cloud.retail_v2beta.types.Model):
            Required. The payload of the
            [Model][google.cloud.retail.v2beta.Model] to create.
        dry_run (bool):
            Optional. Whether to run a dry run to
            validate the request (without actually creating
            the model).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    model: gcr_model.Model = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcr_model.Model,
    )
    dry_run: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateModelRequest(proto.Message):
    r"""Request for updating an existing model.

    Attributes:
        model (google.cloud.retail_v2beta.types.Model):
            Required. The body of the updated
            [Model][google.cloud.retail.v2beta.Model].
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Indicates which fields in the
            provided 'model' to update. If not set, by
            default updates all fields.
    """

    model: gcr_model.Model = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcr_model.Model,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetModelRequest(proto.Message):
    r"""Request for getting a model.

    Attributes:
        name (str):
            Required. The resource name of the
            [Model][google.cloud.retail.v2beta.Model] to get. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog}/models/{model_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class PauseModelRequest(proto.Message):
    r"""Request for pausing training of a model.

    Attributes:
        name (str):
            Required. The name of the model to pause. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ResumeModelRequest(proto.Message):
    r"""Request for resuming training of a model.

    Attributes:
        name (str):
            Required. The name of the model to resume. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListModelsRequest(proto.Message):
    r"""Request for listing models associated with a resource.

    Attributes:
        parent (str):
            Required. The parent for which to list models. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}``
        page_size (int):
            Optional. Maximum number of results to
            return. If unspecified, defaults to 50. Max
            allowed value is 1000.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListModels`` call. Provide this to retrieve the subsequent
            page.
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


class DeleteModelRequest(proto.Message):
    r"""Request for deleting a model.

    Attributes:
        name (str):
            Required. The resource name of the
            [Model][google.cloud.retail.v2beta.Model] to delete. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListModelsResponse(proto.Message):
    r"""Response to a ListModelRequest.

    Attributes:
        models (MutableSequence[google.cloud.retail_v2beta.types.Model]):
            List of Models.
        next_page_token (str):
            Pagination token, if not returned indicates
            the last page.
    """

    @property
    def raw_page(self):
        return self

    models: MutableSequence[gcr_model.Model] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcr_model.Model,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TuneModelRequest(proto.Message):
    r"""Request to manually start a tuning process now (instead of
    waiting for the periodically scheduled tuning to happen).

    Attributes:
        name (str):
            Required. The resource name of the model to tune. Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateModelMetadata(proto.Message):
    r"""Metadata associated with a create operation.

    Attributes:
        model (str):
            The resource name of the model that this create applies to.
            Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TuneModelMetadata(proto.Message):
    r"""Metadata associated with a tune operation.

    Attributes:
        model (str):
            The resource name of the model that this tune applies to.
            Format:
            ``projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/models/{model_id}``
    """

    model: str = proto.Field(
        proto.STRING,
        number=1,
    )


class TuneModelResponse(proto.Message):
    r"""Response associated with a tune operation."""


__all__ = tuple(sorted(__protobuf__.manifest))
