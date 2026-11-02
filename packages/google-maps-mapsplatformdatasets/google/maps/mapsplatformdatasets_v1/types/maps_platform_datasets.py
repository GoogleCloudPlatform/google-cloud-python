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
import google.rpc.status_pb2 as status_pb2  # type: ignore
import proto  # type: ignore

from google.maps.mapsplatformdatasets_v1.types import dataset as gmm_dataset

__protobuf__ = proto.module(
    package="google.maps.mapsplatformdatasets.v1",
    manifest={
        "CreateDatasetRequest",
        "UpdateDatasetMetadataRequest",
        "GetDatasetRequest",
        "ListDatasetsRequest",
        "ListDatasetsResponse",
        "FetchDatasetErrorsRequest",
        "FetchDatasetErrorsResponse",
        "DeleteDatasetRequest",
    },
)


class CreateDatasetRequest(proto.Message):
    r"""Request to create a maps dataset.

    Attributes:
        parent (str):
            Required. Parent project that will own the
            dataset. Format: projects/{project}
        dataset (google.maps.mapsplatformdatasets_v1.types.Dataset):
            Required. The dataset version to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    dataset: gmm_dataset.Dataset = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gmm_dataset.Dataset,
    )


class UpdateDatasetMetadataRequest(proto.Message):
    r"""Request to update the metadata fields of the dataset.

    Attributes:
        dataset (google.maps.mapsplatformdatasets_v1.types.Dataset):
            Required. Resource name of the dataset to update. Format:
            projects/{project}/datasets/{dataset_id}
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The list of fields to be updated.

            The value "\*" is used for full replacement (default).
    """

    dataset: gmm_dataset.Dataset = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gmm_dataset.Dataset,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class GetDatasetRequest(proto.Message):
    r"""Request to get the specified dataset.

    Attributes:
        name (str):
            Required. Resource name. Format:
            projects/{project}/datasets/{dataset_id}

            Can also fetch some special versions by appending "@" and a
            tag. Format: projects/{project}/datasets/{dataset_id}@{tag}

            Tag "active": The info of the latest completed version will
            be included, and NOT_FOUND if the dataset does not have one.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListDatasetsRequest(proto.Message):
    r"""Request to list datasets for the project.

    Attributes:
        parent (str):
            Required. The name of the project to list all
            the datasets for. Format: projects/{project}
        page_size (int):
            The maximum number of datasets to return per
            page.
            If unspecified (or zero), all datasets will be
            returned.
        page_token (str):
            The page token, received from a previous
            ListDatasets call. Provide this to retrieve the
            subsequent page.
        tag (str):
            The tag that specifies the desired version
            for each dataset.
            Note that when pagination is also specified,
            some filtering can happen after pagination,
            which may cause the response to contain fewer
            datasets than the page size, even if it's not
            the last page.

            Tag "active": Each dataset in the response will
            include the info of its latest completed
            version, and the dataset will be skipped if it
            does not have one.
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
    tag: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListDatasetsResponse(proto.Message):
    r"""Response object of ListDatasets.

    Attributes:
        datasets (MutableSequence[google.maps.mapsplatformdatasets_v1.types.Dataset]):
            All the datasets for the project.
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page.

            If this field is omitted, there are no subsequent pages.
    """

    @property
    def raw_page(self):
        return self

    datasets: MutableSequence[gmm_dataset.Dataset] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gmm_dataset.Dataset,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class FetchDatasetErrorsRequest(proto.Message):
    r"""Request to list detailed errors belonging to a dataset.

    Attributes:
        dataset (str):
            Required. The name of the dataset to list all the errors
            for. Format: projects/{project}/datasets/{dataset_id}
        page_size (int):
            The maximum number of errors to return per
            page.
            The maximum value is 500; values above 500 will
            be capped to 500.

            If unspecified, at most 50 errors will be
            returned.
        page_token (str):
            The page token, received from a previous
            ListDatasetErrors call. Provide this to retrieve
            the subsequent page.
    """

    dataset: str = proto.Field(
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


class FetchDatasetErrorsResponse(proto.Message):
    r"""Response object of FetchDatasetErrors.

    Attributes:
        next_page_token (str):
            A token that can be sent as ``page_token`` to retrieve the
            next page.

            If this field is omitted, there are no subsequent pages.
        errors (MutableSequence[google.rpc.status_pb2.Status]):
            The errors associated with a dataset.
    """

    @property
    def raw_page(self):
        return self

    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    errors: MutableSequence[status_pb2.Status] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=status_pb2.Status,
    )


class DeleteDatasetRequest(proto.Message):
    r"""Request to delete a dataset.

    Attributes:
        name (str):
            Required. The name of the dataset to delete. Format:
            projects/{project}/datasets/{dataset_id}
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
