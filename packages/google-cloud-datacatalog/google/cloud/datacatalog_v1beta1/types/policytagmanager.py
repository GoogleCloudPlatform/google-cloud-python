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

from google.cloud.datacatalog_v1beta1.types import common, timestamps

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1beta1",
    manifest={
        "Taxonomy",
        "PolicyTag",
        "CreateTaxonomyRequest",
        "DeleteTaxonomyRequest",
        "UpdateTaxonomyRequest",
        "ListTaxonomiesRequest",
        "ListTaxonomiesResponse",
        "GetTaxonomyRequest",
        "CreatePolicyTagRequest",
        "DeletePolicyTagRequest",
        "UpdatePolicyTagRequest",
        "ListPolicyTagsRequest",
        "ListPolicyTagsResponse",
        "GetPolicyTagRequest",
    },
)


class Taxonomy(proto.Message):
    r"""A taxonomy is a collection of policy tags that classify data along a
    common axis. For instance a data *sensitivity* taxonomy could
    contain policy tags denoting PII such as age, zipcode, and SSN. A
    data *origin* taxonomy could contain policy tags to distinguish user
    data, employee data, partner data, public data.

    Attributes:
        name (str):
            Identifier. Resource name of this taxonomy, whose format is:
            "projects/{project_number}/locations/{location_id}/taxonomies/{id}".
        display_name (str):
            Required. User defined name of this taxonomy.
            It must: contain only unicode letters, numbers,
            underscores, dashes and spaces; not start or end
            with spaces; and be at most 200 bytes long when
            encoded in UTF-8.

            The taxonomy display name must be unique within
            an organization.
        description (str):
            Optional. Description of this taxonomy. It
            must: contain only unicode characters, tabs,
            newlines, carriage returns and page breaks; and
            be at most 2000 bytes long when encoded in
            UTF-8. If not set, defaults to an empty
            description.
        policy_tag_count (int):
            Output only. Number of policy tags contained
            in this taxonomy.
        taxonomy_timestamps (google.cloud.datacatalog_v1beta1.types.SystemTimestamps):
            Output only. Timestamps about this taxonomy. Only
            create_time and update_time are used.
        activated_policy_types (MutableSequence[google.cloud.datacatalog_v1beta1.types.Taxonomy.PolicyType]):
            Optional. A list of policy types that are
            activated for this taxonomy. If not set,
            defaults to an empty list.
        service (google.cloud.datacatalog_v1beta1.types.Taxonomy.Service):
            Output only. Identity of the service which
            owns the Taxonomy. This field is only populated
            when the taxonomy is created by a Google Cloud
            service. Currently only 'DATAPLEX' is supported.
    """

    class PolicyType(proto.Enum):
        r"""Defines policy types where policy tag can be used for.

        Values:
            POLICY_TYPE_UNSPECIFIED (0):
                Unspecified policy type.
            FINE_GRAINED_ACCESS_CONTROL (1):
                Fine grained access control policy, which
                enables access control on tagged resources.
        """

        POLICY_TYPE_UNSPECIFIED = 0
        FINE_GRAINED_ACCESS_CONTROL = 1

    class Service(proto.Message):
        r"""The source system of the Taxonomy.

        Attributes:
            name (google.cloud.datacatalog_v1beta1.types.ManagingSystem):
                The Google Cloud service name.
            identity (str):
                The service agent for the service.
        """

        name: common.ManagingSystem = proto.Field(
            proto.ENUM,
            number=1,
            enum=common.ManagingSystem,
        )
        identity: str = proto.Field(
            proto.STRING,
            number=2,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    policy_tag_count: int = proto.Field(
        proto.INT32,
        number=4,
    )
    taxonomy_timestamps: timestamps.SystemTimestamps = proto.Field(
        proto.MESSAGE,
        number=5,
        message=timestamps.SystemTimestamps,
    )
    activated_policy_types: MutableSequence[PolicyType] = proto.RepeatedField(
        proto.ENUM,
        number=6,
        enum=PolicyType,
    )
    service: Service = proto.Field(
        proto.MESSAGE,
        number=7,
        message=Service,
    )


class PolicyTag(proto.Message):
    r"""Denotes one policy tag in a taxonomy (e.g. ssn). Policy Tags
    can be defined in a hierarchy. For example, consider the
    following hierarchy:

    Geolocation -&gt; (LatLong, City, ZipCode). PolicyTag
    "Geolocation" contains three child policy tags: "LatLong",
    "City", and "ZipCode".

    Attributes:
        name (str):
            Identifier. Resource name of this policy tag, whose format
            is:
            "projects/{project_number}/locations/{location_id}/taxonomies/{taxonomy_id}/policyTags/{id}".
        display_name (str):
            Required. User defined name of this policy
            tag. It must: be unique within the parent
            taxonomy; contain only unicode letters, numbers,
            underscores, dashes and spaces; not start or end
            with spaces; and be at most 200 bytes long when
            encoded in UTF-8.
        description (str):
            Description of this policy tag. It must:
            contain only unicode characters, tabs, newlines,
            carriage returns and page breaks; and be at most
            2000 bytes long when encoded in UTF-8. If not
            set, defaults to an empty description. If not
            set, defaults to an empty description.
        parent_policy_tag (str):
            Resource name of this policy tag's parent
            policy tag (e.g. for the "LatLong" policy tag in
            the example above, this field contains the
            resource name of the "Geolocation" policy tag).
            If empty, it means this policy tag is a top
            level policy tag (e.g. this field is empty for
            the "Geolocation" policy tag in the example
            above). If not set, defaults to an empty string.
        child_policy_tags (MutableSequence[str]):
            Output only. Resource names of child policy
            tags of this policy tag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=2,
    )
    description: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent_policy_tag: str = proto.Field(
        proto.STRING,
        number=4,
    )
    child_policy_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=5,
    )


class CreateTaxonomyRequest(proto.Message):
    r"""Request message for
    [CreateTaxonomy][google.cloud.datacatalog.v1beta1.PolicyTagManager.CreateTaxonomy].

    Attributes:
        parent (str):
            Required. Resource name of the project that
            the taxonomy will belong to.
        taxonomy (google.cloud.datacatalog_v1beta1.types.Taxonomy):
            The taxonomy to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    taxonomy: "Taxonomy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Taxonomy",
    )


class DeleteTaxonomyRequest(proto.Message):
    r"""Request message for
    [DeleteTaxonomy][google.cloud.datacatalog.v1beta1.PolicyTagManager.DeleteTaxonomy].

    Attributes:
        name (str):
            Required. Resource name of the taxonomy to be
            deleted. All policy tags in this taxonomy will
            also be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateTaxonomyRequest(proto.Message):
    r"""Request message for
    [UpdateTaxonomy][google.cloud.datacatalog.v1beta1.PolicyTagManager.UpdateTaxonomy].

    Attributes:
        taxonomy (google.cloud.datacatalog_v1beta1.types.Taxonomy):
            The taxonomy to update. Only description, display_name, and
            activated policy types can be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource. For the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If not set, defaults to all of the fields that are allowed
            to update.
    """

    taxonomy: "Taxonomy" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Taxonomy",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListTaxonomiesRequest(proto.Message):
    r"""Request message for
    [ListTaxonomies][google.cloud.datacatalog.v1beta1.PolicyTagManager.ListTaxonomies].

    Attributes:
        parent (str):
            Required. Resource name of the project to
            list the taxonomies of.
        page_size (int):
            The maximum number of items to return. Must
            be a value between 1 and 1000. If not set,
            defaults to 50.
        page_token (str):
            The next_page_token value returned from a previous list
            request, if any. If not set, defaults to an empty string.
        filter (str):
            Supported field for filter is 'service' and
            value is 'dataplex'. Eg: service=dataplex.
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


class ListTaxonomiesResponse(proto.Message):
    r"""Response message for
    [ListTaxonomies][google.cloud.datacatalog.v1beta1.PolicyTagManager.ListTaxonomies].

    Attributes:
        taxonomies (MutableSequence[google.cloud.datacatalog_v1beta1.types.Taxonomy]):
            Taxonomies that the project contains.
        next_page_token (str):
            Token used to retrieve the next page of
            results, or empty if there are no more results
            in the list.
    """

    @property
    def raw_page(self):
        return self

    taxonomies: MutableSequence["Taxonomy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Taxonomy",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetTaxonomyRequest(proto.Message):
    r"""Request message for
    [GetTaxonomy][google.cloud.datacatalog.v1beta1.PolicyTagManager.GetTaxonomy].

    Attributes:
        name (str):
            Required. Resource name of the requested
            taxonomy.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreatePolicyTagRequest(proto.Message):
    r"""Request message for
    [CreatePolicyTag][google.cloud.datacatalog.v1beta1.PolicyTagManager.CreatePolicyTag].

    Attributes:
        parent (str):
            Required. Resource name of the taxonomy that
            the policy tag will belong to.
        policy_tag (google.cloud.datacatalog_v1beta1.types.PolicyTag):
            The policy tag to be created.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    policy_tag: "PolicyTag" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="PolicyTag",
    )


class DeletePolicyTagRequest(proto.Message):
    r"""Request message for
    [DeletePolicyTag][google.cloud.datacatalog.v1beta1.PolicyTagManager.DeletePolicyTag].

    Attributes:
        name (str):
            Required. Resource name of the policy tag to
            be deleted. All of its descendant policy tags
            will also be deleted.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdatePolicyTagRequest(proto.Message):
    r"""Request message for
    [UpdatePolicyTag][google.cloud.datacatalog.v1beta1.PolicyTagManager.UpdatePolicyTag].

    Attributes:
        policy_tag (google.cloud.datacatalog_v1beta1.types.PolicyTag):
            The policy tag to update. Only the description,
            display_name, and parent_policy_tag fields can be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            The update mask applies to the resource. Only display_name,
            description and parent_policy_tag can be updated and thus
            can be listed in the mask. If update_mask is not provided,
            all allowed fields (i.e. display_name, description and
            parent) will be updated. For more information including the
            ``FieldMask`` definition, see
            https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
            If not set, defaults to all of the fields that are allowed
            to update.
    """

    policy_tag: "PolicyTag" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="PolicyTag",
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class ListPolicyTagsRequest(proto.Message):
    r"""Request message for
    [ListPolicyTags][google.cloud.datacatalog.v1beta1.PolicyTagManager.ListPolicyTags].

    Attributes:
        parent (str):
            Required. Resource name of the taxonomy to
            list the policy tags of.
        page_size (int):
            The maximum number of items to return. Must
            be a value between 1 and 1000. If not set,
            defaults to 50.
        page_token (str):
            The next_page_token value returned from a previous List
            request, if any. If not set, defaults to an empty string.
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


class ListPolicyTagsResponse(proto.Message):
    r"""Response message for
    [ListPolicyTags][google.cloud.datacatalog.v1beta1.PolicyTagManager.ListPolicyTags].

    Attributes:
        policy_tags (MutableSequence[google.cloud.datacatalog_v1beta1.types.PolicyTag]):
            The policy tags that are in the requested
            taxonomy.
        next_page_token (str):
            Token used to retrieve the next page of
            results, or empty if there are no more results
            in the list.
    """

    @property
    def raw_page(self):
        return self

    policy_tags: MutableSequence["PolicyTag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="PolicyTag",
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetPolicyTagRequest(proto.Message):
    r"""Request message for
    [GetPolicyTag][google.cloud.datacatalog.v1beta1.PolicyTagManager.GetPolicyTag].

    Attributes:
        name (str):
            Required. Resource name of the requested
            policy tag.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
