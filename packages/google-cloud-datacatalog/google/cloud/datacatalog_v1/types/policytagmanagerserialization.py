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

from google.cloud.datacatalog_v1.types import policytagmanager

__protobuf__ = proto.module(
    package="google.cloud.datacatalog.v1",
    manifest={
        "SerializedTaxonomy",
        "SerializedPolicyTag",
        "ReplaceTaxonomyRequest",
        "ImportTaxonomiesRequest",
        "InlineSource",
        "CrossRegionalSource",
        "ImportTaxonomiesResponse",
        "ExportTaxonomiesRequest",
        "ExportTaxonomiesResponse",
    },
)


class SerializedTaxonomy(proto.Message):
    r"""A nested protocol buffer that represents a taxonomy and the
    hierarchy of its policy tags. Used for taxonomy replacement,
    import, and export.

    Attributes:
        display_name (str):
            Required. Display name of the taxonomy. At
            most 200 bytes when encoded in UTF-8.
        description (str):
            Description of the serialized taxonomy. At
            most 2000 bytes when encoded in UTF-8. If not
            set, defaults to an empty description.
        policy_tags (MutableSequence[google.cloud.datacatalog_v1.types.SerializedPolicyTag]):
            Top level policy tags associated with the
            taxonomy, if any.
        activated_policy_types (MutableSequence[google.cloud.datacatalog_v1.types.Taxonomy.PolicyType]):
            A list of policy types that are activated per
            taxonomy.
    """

    display_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    description: str = proto.Field(
        proto.STRING,
        number=2,
    )
    policy_tags: MutableSequence["SerializedPolicyTag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="SerializedPolicyTag",
    )
    activated_policy_types: MutableSequence[policytagmanager.Taxonomy.PolicyType] = (
        proto.RepeatedField(
            proto.ENUM,
            number=4,
            enum=policytagmanager.Taxonomy.PolicyType,
        )
    )


class SerializedPolicyTag(proto.Message):
    r"""A nested protocol buffer that represents a policy tag and all
    its descendants.

    Attributes:
        policy_tag (str):
            Resource name of the policy tag.

            This field is ignored when calling ``ImportTaxonomies``.
        display_name (str):
            Required. Display name of the policy tag. At
            most 200 bytes when encoded in UTF-8.
        description (str):
            Description of the serialized policy tag. At
            most 2000 bytes when encoded in UTF-8. If not
            set, defaults to an empty description.
        child_policy_tags (MutableSequence[google.cloud.datacatalog_v1.types.SerializedPolicyTag]):
            Children of the policy tag, if any.
    """

    policy_tag: str = proto.Field(
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
    child_policy_tags: MutableSequence["SerializedPolicyTag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message="SerializedPolicyTag",
    )


class ReplaceTaxonomyRequest(proto.Message):
    r"""Request message for
    [ReplaceTaxonomy][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ReplaceTaxonomy].

    Attributes:
        name (str):
            Required. Resource name of the taxonomy to
            update.
        serialized_taxonomy (google.cloud.datacatalog_v1.types.SerializedTaxonomy):
            Required. Taxonomy to update along with its
            child policy tags.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    serialized_taxonomy: "SerializedTaxonomy" = proto.Field(
        proto.MESSAGE,
        number=2,
        message="SerializedTaxonomy",
    )


class ImportTaxonomiesRequest(proto.Message):
    r"""Request message for
    [ImportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ImportTaxonomies].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Resource name of project that the
            imported taxonomies will belong to.
        inline_source (google.cloud.datacatalog_v1.types.InlineSource):
            Inline source taxonomy to import.

            This field is a member of `oneof`_ ``source``.
        cross_regional_source (google.cloud.datacatalog_v1.types.CrossRegionalSource):
            Cross-regional source taxonomy to import.

            This field is a member of `oneof`_ ``source``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    inline_source: "InlineSource" = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="source",
        message="InlineSource",
    )
    cross_regional_source: "CrossRegionalSource" = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="source",
        message="CrossRegionalSource",
    )


class InlineSource(proto.Message):
    r"""Inline source containing taxonomies to import.

    Attributes:
        taxonomies (MutableSequence[google.cloud.datacatalog_v1.types.SerializedTaxonomy]):
            Required. Taxonomies to import.
    """

    taxonomies: MutableSequence["SerializedTaxonomy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SerializedTaxonomy",
    )


class CrossRegionalSource(proto.Message):
    r"""Cross-regional source used to import an existing taxonomy
    into a different region.

    Attributes:
        taxonomy (str):
            Required. The resource name of the source
            taxonomy to import.
    """

    taxonomy: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ImportTaxonomiesResponse(proto.Message):
    r"""Response message for
    [ImportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ImportTaxonomies].

    Attributes:
        taxonomies (MutableSequence[google.cloud.datacatalog_v1.types.Taxonomy]):
            Imported taxonomies.
    """

    taxonomies: MutableSequence[policytagmanager.Taxonomy] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=policytagmanager.Taxonomy,
    )


class ExportTaxonomiesRequest(proto.Message):
    r"""Request message for
    [ExportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ExportTaxonomies].


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        parent (str):
            Required. Resource name of the project that
            the exported taxonomies belong to.
        taxonomies (MutableSequence[str]):
            Required. Resource names of the taxonomies to
            export.
        serialized_taxonomies (bool):
            Serialized export taxonomies that contain all
            the policy tags as nested protocol buffers.

            This field is a member of `oneof`_ ``destination``.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    taxonomies: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    serialized_taxonomies: bool = proto.Field(
        proto.BOOL,
        number=3,
        oneof="destination",
    )


class ExportTaxonomiesResponse(proto.Message):
    r"""Response message for
    [ExportTaxonomies][google.cloud.datacatalog.v1.PolicyTagManagerSerialization.ExportTaxonomies].

    Attributes:
        taxonomies (MutableSequence[google.cloud.datacatalog_v1.types.SerializedTaxonomy]):
            List of taxonomies and policy tags as nested
            protocol buffers.
    """

    taxonomies: MutableSequence["SerializedTaxonomy"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SerializedTaxonomy",
    )


__all__ = tuple(sorted(__protobuf__.manifest))
