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

from google.cloud.vectorsearch_v1beta.types import data_object as gcv_data_object

__protobuf__ = proto.module(
    package="google.cloud.vectorsearch.v1beta",
    manifest={
        "CreateDataObjectRequest",
        "BatchCreateDataObjectsRequest",
        "BatchCreateDataObjectsResponse",
        "GetDataObjectRequest",
        "UpdateDataObjectRequest",
        "BatchUpdateDataObjectsRequest",
        "BatchUpdateDataObjectsResponse",
        "DeleteDataObjectRequest",
        "BatchDeleteDataObjectsRequest",
    },
)


class CreateDataObjectRequest(proto.Message):
    r"""Request message for
    [DataObjectService.CreateDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.CreateDataObject].

    Attributes:
        parent (str):
            Required. The resource name of the Collection to create the
            DataObject in. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``
        data_object_id (str):
            Required. The id of the dataObject to create. The id must be
            1-63 characters long, and comply with
            `RFC1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.
            Specifically, it must be 1-63 characters long and match the
            regular expression ``[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?``.
        data_object (google.cloud.vectorsearch_v1beta.types.DataObject):
            Required. The DataObject to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    data_object_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    data_object: gcv_data_object.DataObject = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcv_data_object.DataObject,
    )


class BatchCreateDataObjectsRequest(proto.Message):
    r"""Request message for
    [DataObjectService.BatchCreateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchCreateDataObjects].

    Attributes:
        parent (str):
            Required. The resource name of the Collection to create the
            DataObjects in. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``.
            The parent field in the CreateDataObjectRequest messages
            must match this field.
        requests (MutableSequence[google.cloud.vectorsearch_v1beta.types.CreateDataObjectRequest]):
            Required. The request message specifying the
            resources to create. A maximum of 1000
            DataObjects can be created in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["CreateDataObjectRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="CreateDataObjectRequest",
    )


class BatchCreateDataObjectsResponse(proto.Message):
    r"""Response message for
    [DataObjectService.BatchCreateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchCreateDataObjects].

    Attributes:
        data_objects (MutableSequence[google.cloud.vectorsearch_v1beta.types.DataObject]):
            Output only. DataObjects created.
    """

    data_objects: MutableSequence[gcv_data_object.DataObject] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcv_data_object.DataObject,
    )


class GetDataObjectRequest(proto.Message):
    r"""Request message for
    [DataObjectService.GetDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.GetDataObject].

    Attributes:
        name (str):
            Required. The name of the DataObject resource. Format:
            ``projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateDataObjectRequest(proto.Message):
    r"""Request message for
    [DataObjectService.UpdateDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.UpdateDataObject].

    Attributes:
        data_object (google.cloud.vectorsearch_v1beta.types.DataObject):
            Required. The DataObject which replaces the
            resource on the server.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. The update mask applies to the resource. See
            [google.protobuf.FieldMask][google.protobuf.FieldMask].
    """

    data_object: gcv_data_object.DataObject = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcv_data_object.DataObject,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class BatchUpdateDataObjectsRequest(proto.Message):
    r"""Request message for
    [DataObjectService.BatchUpdateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchUpdateDataObjects].

    Attributes:
        parent (str):
            Required. The resource name of the Collection to update the
            DataObjects in. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``.
            The parent field in the UpdateDataObjectRequest messages
            must match this field.
        requests (MutableSequence[google.cloud.vectorsearch_v1beta.types.UpdateDataObjectRequest]):
            Required. The request message specifying the
            resources to update. A maximum of 1000
            DataObjects can be updated in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["UpdateDataObjectRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="UpdateDataObjectRequest",
    )


class BatchUpdateDataObjectsResponse(proto.Message):
    r"""Response message for
    [DataObjectService.BatchUpdateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchUpdateDataObjects].

    """


class DeleteDataObjectRequest(proto.Message):
    r"""Request message for
    [DataObjectService.DeleteDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.DeleteDataObject].

    Attributes:
        name (str):
            Required. The name of the DataObject resource to be deleted.
            Format:
            ``projects/{project}/locations/{location}/collections/{collection}/dataObjects/{dataObject}``
        etag (str):
            Optional. The current etag of the DataObject.
            If an etag is provided and does not match the
            current etag of the DataObject, deletion will be
            blocked and an ABORTED error will be returned.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    etag: str = proto.Field(
        proto.STRING,
        number=2,
    )


class BatchDeleteDataObjectsRequest(proto.Message):
    r"""Request message for
    [DataObjectService.BatchDeleteDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchDeleteDataObjects].

    Attributes:
        parent (str):
            Required. The resource name of the Collection to delete the
            DataObjects in. Format:
            ``projects/{project}/locations/{location}/collections/{collection}``.
        requests (MutableSequence[google.cloud.vectorsearch_v1beta.types.DeleteDataObjectRequest]):
            Required. The request message specifying the
            resources to delete. A maximum of 1000
            DataObjects can be deleted in a batch.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    requests: MutableSequence["DeleteDataObjectRequest"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="DeleteDataObjectRequest",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
