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
    package="google.cloud.networksecurity.v1alpha1",
    manifest={
        "UrlList",
        "ListUrlListsRequest",
        "ListUrlListsResponse",
        "GetUrlListRequest",
        "CreateUrlListRequest",
        "UpdateUrlListRequest",
        "DeleteUrlListRequest",
    },
)


class UrlList(proto.Message):
    r"""UrlList proto helps users to set reusable, independently
    manageable lists of hosts, host patterns, URLs, URL patterns.

    Attributes:
        name (str):
            Required. Name of the resource provided by the user. Name is
            of the form
            projects/{project}/locations/{location}/urlLists/{url_list}
            url_list should match the
            pattern:(^\ `a-z <[a-z0-9-]{0,61}[a-z0-9]>`__?$).
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the security policy
            was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Time when the security policy
            was updated.
        description (str):
            Optional. Free-text description of the
            resource.
        values (MutableSequence[str]):
            Required. FQDNs and URLs.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=3,
        message=timestamp_pb2.Timestamp,
    )
    description: str = proto.Field(
        proto.STRING,
        number=4,
    )
    values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class ListUrlListsRequest(proto.Message):
    r"""Request used by the ListUrlList method.

    Attributes:
        parent (str):
            Required. The project and location from which the UrlLists
            should be listed, specified in the format
            ``projects/{project}/locations/{location}``.
        page_size (int):
            Maximum number of UrlLists to return per
            call.
        page_token (str):
            The value returned by the last ``ListUrlListsResponse``
            Indicates that this is a continuation of a prior
            ``ListUrlLists`` call, and that the system should return the
            next page of data.
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


class ListUrlListsResponse(proto.Message):
    r"""Response returned by the ListUrlLists method.

    Attributes:
        url_lists (MutableSequence[google.cloud.network_security_v1alpha1.types.UrlList]):
            List of UrlList resources.
        next_page_token (str):
            If there might be more results than those appearing in this
            response, then ``next_page_token`` is included. To get the
            next set of results, call this method again using the value
            of ``next_page_token`` as ``page_token``.
        unreachable (MutableSequence[str]):
            Locations that could not be reached.
    """

    @property
    def raw_page(self):
        return self

    url_lists: MutableSequence["UrlList"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="UrlList",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetUrlListRequest(proto.Message):
    r"""Request used by the GetUrlList method.

    Attributes:
        name (str):
            Required. A name of the UrlList to get. Must be in the
            format ``projects/*/locations/{location}/urlLists/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateUrlListRequest(proto.Message):
    r"""Request used by the CreateUrlList method.

    Attributes:
        parent (str):
            Required. The parent resource of the UrlList. Must be in the
            format ``projects/*/locations/{location}``.
        url_list_id (str):
            Required. Short name of the UrlList resource to be created.
            This value should be 1-63 characters long, containing only
            letters, numbers, hyphens, and underscores, and should not
            start with a number. E.g. "url_list".
        url_list (google.cloud.network_security_v1alpha1.types.UrlList):
            Required. UrlList resource to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    url_list_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    url_list: "UrlList" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="UrlList",
    )


class UpdateUrlListRequest(proto.Message):
    r"""Request used by UpdateUrlList method.

    Attributes:
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Optional. Field mask is used to specify the fields to be
            overwritten in the UrlList resource by the update. The
            fields specified in the update_mask are relative to the
            resource, not the full request. A field will be overwritten
            if it is in the mask. If the user does not provide a mask
            then all fields will be overwritten.
        url_list (google.cloud.network_security_v1alpha1.types.UrlList):
            Required. Updated UrlList resource.
    """

    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=1,
        message=field_mask_pb2.FieldMask,
    )
    url_list: "UrlList" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="UrlList",
    )


class DeleteUrlListRequest(proto.Message):
    r"""Request used by the DeleteUrlList method.

    Attributes:
        name (str):
            Required. A name of the UrlList to delete. Must be in the
            format ``projects/*/locations/{location}/urlLists/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
