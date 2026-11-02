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

import google.cloud.orgpolicy.v1.orgpolicy_pb2 as orgpolicy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.identity.accesscontextmanager.v1.access_level_pb2 as access_level_pb2  # type: ignore
import google.identity.accesscontextmanager.v1.access_policy_pb2 as access_policy_pb2  # type: ignore
import google.identity.accesscontextmanager.v1.service_perimeter_pb2 as service_perimeter_pb2  # type: ignore
import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.code_pb2 as code_pb2  # type: ignore
import proto  # type: ignore
from google.cloud.osconfig_v1.types import inventory

from google.cloud.asset_v1.types import asset_enrichment_resourceowners

__protobuf__ = proto.module(
    package="google.cloud.asset.v1",
    manifest={
        "TemporalAsset",
        "TimeWindow",
        "AssetEnrichment",
        "Asset",
        "Resource",
        "RelatedAssets",
        "RelationshipAttributes",
        "RelatedAsset",
        "Tag",
        "EffectiveTagDetails",
        "ResourceSearchResult",
        "VersionedResource",
        "AttachedResource",
        "RelatedResources",
        "RelatedResource",
        "IamPolicySearchResult",
        "IamPolicyAnalysisState",
        "ConditionEvaluation",
        "IamPolicyAnalysisResult",
    },
)


class TemporalAsset(proto.Message):
    r"""An asset in Google Cloud and its temporal metadata, including
    the time window when it was observed and its status during that
    window.

    Attributes:
        window (google.cloud.asset_v1.types.TimeWindow):
            The time window when the asset data and state
            was observed.
        deleted (bool):
            Whether the asset has been deleted or not.
        asset (google.cloud.asset_v1.types.Asset):
            An asset in Google Cloud.
        prior_asset_state (google.cloud.asset_v1.types.TemporalAsset.PriorAssetState):
            State of prior_asset.
        prior_asset (google.cloud.asset_v1.types.Asset):
            Prior copy of the asset. Populated if prior_asset_state is
            PRESENT. Currently this is only set for responses in
            Real-Time Feed.
    """

    class PriorAssetState(proto.Enum):
        r"""State of prior asset.

        Values:
            PRIOR_ASSET_STATE_UNSPECIFIED (0):
                prior_asset is not applicable for the current asset.
            PRESENT (1):
                prior_asset is populated correctly.
            INVALID (2):
                Failed to set prior_asset.
            DOES_NOT_EXIST (3):
                Current asset is the first known state.
            DELETED (4):
                prior_asset is a deletion.
        """

        PRIOR_ASSET_STATE_UNSPECIFIED = 0
        PRESENT = 1
        INVALID = 2
        DOES_NOT_EXIST = 3
        DELETED = 4

    window: "TimeWindow" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TimeWindow",
    )
    deleted: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Asset",
    )
    prior_asset_state: PriorAssetState = proto.Field(
        proto.ENUM,
        number=4,
        enum=PriorAssetState,
    )
    prior_asset: "Asset" = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Asset",
    )


class TimeWindow(proto.Message):
    r"""A time window specified by its ``start_time`` and ``end_time``.

    Attributes:
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Start time of the time window (exclusive).
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            End time of the time window (inclusive). If
            not specified, the current timestamp is used
            instead.
    """

    start_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )


class AssetEnrichment(proto.Message):
    r"""The enhanced metadata information for a resource.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        resource_owners (google.cloud.asset_v1.types.ResourceOwners):
            The resource owners for a resource.

            Note that this field only contains the members
            that have "roles/owner" role in the resource's
            IAM Policy.

            This field is a member of `oneof`_ ``EnrichmentData``.
    """

    resource_owners: asset_enrichment_resourceowners.ResourceOwners = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="EnrichmentData",
        message=asset_enrichment_resourceowners.ResourceOwners,
    )


class Asset(proto.Message):
    r"""An asset in Google Cloud. An asset can be any resource in the Google
    Cloud `resource
    hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
    a resource outside the Google Cloud resource hierarchy (such as
    Google Kubernetes Engine clusters and objects), or a policy (e.g.
    IAM policy), or a relationship (e.g. an INSTANCE_TO_INSTANCEGROUP
    relationship). See `Supported asset
    types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
    for more information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update timestamp of an asset. update_time is
            updated when create/update/delete operation is performed.
        name (str):
            The full name of the asset. Example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``

            See `Resource
            names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.
        asset_type (str):
            The type of the asset. Example:
            ``compute.googleapis.com/Disk``

            See `Supported asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
            for more information.
        resource (google.cloud.asset_v1.types.Resource):
            A representation of the resource.
        iam_policy (google.iam.v1.policy_pb2.Policy):
            A representation of the IAM policy set on a Google Cloud
            resource. There can be a maximum of one IAM policy set on
            any given resource. In addition, IAM policies inherit their
            granted access scope from any policies set on parent
            resources in the resource hierarchy. Therefore, the
            effectively policy is the union of both the policy set on
            this resource and each policy set on all of the resource's
            ancestry resource levels in the hierarchy. See `this
            topic <https://cloud.google.com/iam/help/allow-policies/inheritance>`__
            for more information.
        org_policy (MutableSequence[google.cloud.orgpolicy.v1.orgpolicy_pb2.Policy]):
            A representation of an `organization
            policy <https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy>`__.
            There can be more than one organization policy with
            different constraints set on a given resource.
        access_policy (google.identity.accesscontextmanager.v1.access_policy_pb2.AccessPolicy):
            Also refer to the `access policy user
            guide <https://cloud.google.com/access-context-manager/docs/overview#access-policies>`__.

            This field is a member of `oneof`_ ``access_context_policy``.
        access_level (google.identity.accesscontextmanager.v1.access_level_pb2.AccessLevel):
            Also refer to the `access level user
            guide <https://cloud.google.com/access-context-manager/docs/overview#access-levels>`__.

            This field is a member of `oneof`_ ``access_context_policy``.
        service_perimeter (google.identity.accesscontextmanager.v1.service_perimeter_pb2.ServicePerimeter):
            Also refer to the `service perimeter user
            guide <https://cloud.google.com/vpc-service-controls/docs/overview>`__.

            This field is a member of `oneof`_ ``access_context_policy``.
        os_inventory (google.cloud.osconfig_v1.types.Inventory):
            A representation of runtime OS Inventory information. See
            `this
            topic <https://cloud.google.com/compute/docs/instances/os-inventory-management>`__
            for more information.
        related_assets (google.cloud.asset_v1.types.RelatedAssets):
            DEPRECATED. This field only presents for the
            purpose of backward-compatibility. The server
            will never generate responses with this field.
            The related assets of the asset of one
            relationship type. One asset only represents one
            type of relationship.
        related_asset (google.cloud.asset_v1.types.RelatedAsset):
            One related asset of the current asset.
        ancestors (MutableSequence[str]):
            The ancestry path of an asset in Google Cloud `resource
            hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
            represented as a list of relative resource names. An
            ancestry path starts with the closest ancestor in the
            hierarchy and ends at root. If the asset is a project,
            folder, or organization, the ancestry path starts from the
            asset itself.

            Example:
            ``["projects/123456789", "folders/5432", "organizations/1234"]``
    """

    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource: "Resource" = proto.Field(
        proto.MESSAGE,
        number=3,
        message="Resource",
    )
    iam_policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=4,
        message=policy_pb2.Policy,
    )
    org_policy: MutableSequence[orgpolicy_pb2.Policy] = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message=orgpolicy_pb2.Policy,
    )
    access_policy: access_policy_pb2.AccessPolicy = proto.Field(
        proto.MESSAGE,
        number=7,
        oneof="access_context_policy",
        message=access_policy_pb2.AccessPolicy,
    )
    access_level: access_level_pb2.AccessLevel = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="access_context_policy",
        message=access_level_pb2.AccessLevel,
    )
    service_perimeter: service_perimeter_pb2.ServicePerimeter = proto.Field(
        proto.MESSAGE,
        number=9,
        oneof="access_context_policy",
        message=service_perimeter_pb2.ServicePerimeter,
    )
    os_inventory: inventory.Inventory = proto.Field(
        proto.MESSAGE,
        number=12,
        message=inventory.Inventory,
    )
    related_assets: "RelatedAssets" = proto.Field(
        proto.MESSAGE,
        number=13,
        message="RelatedAssets",
    )
    related_asset: "RelatedAsset" = proto.Field(
        proto.MESSAGE,
        number=15,
        message="RelatedAsset",
    )
    ancestors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )


class Resource(proto.Message):
    r"""A representation of a Google Cloud resource.

    Attributes:
        version (str):
            The API version. Example: ``v1``
        discovery_document_uri (str):
            The URL of the discovery document containing the resource's
            JSON schema. Example:
            ``https://www.googleapis.com/discovery/v1/apis/compute/v1/rest``

            This value is unspecified for resources that do not have an
            API based on a discovery document, such as Cloud Bigtable.
        discovery_name (str):
            The JSON schema name listed in the discovery document.
            Example: ``Project``

            This value is unspecified for resources that do not have an
            API based on a discovery document, such as Cloud Bigtable.
        resource_url (str):
            The REST URL for accessing the resource. An HTTP ``GET``
            request using this URL returns the resource itself. Example:
            ``https://cloudresourcemanager.googleapis.com/v1/projects/my-project-123``

            This value is unspecified for resources without a REST API.
        parent (str):
            The full name of the immediate parent of this resource. See
            `Resource
            Names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.

            For Google Cloud assets, this value is the parent resource
            defined in the `IAM policy
            hierarchy <https://cloud.google.com/iam/docs/overview#policy_hierarchy>`__.
            Example:
            ``//cloudresourcemanager.googleapis.com/projects/my_project_123``
        data (google.protobuf.struct_pb2.Struct):
            The content of the resource, in which some
            sensitive fields are removed and may not be
            present.
        location (str):
            The location of the resource in Google Cloud,
            such as its zone and region. For more
            information, see
            https://cloud.google.com/about/locations/.
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    discovery_document_uri: str = proto.Field(
        proto.STRING,
        number=2,
    )
    discovery_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    resource_url: str = proto.Field(
        proto.STRING,
        number=4,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=5,
    )
    data: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=6,
        message=struct_pb2.Struct,
    )
    location: str = proto.Field(
        proto.STRING,
        number=8,
    )


class RelatedAssets(proto.Message):
    r"""DEPRECATED. This message only presents for the purpose of
    backward-compatibility. The server will never populate this message
    in responses. The detailed related assets with the
    ``relationship_type``.

    Attributes:
        relationship_attributes (google.cloud.asset_v1.types.RelationshipAttributes):
            The detailed relationship attributes.
        assets (MutableSequence[google.cloud.asset_v1.types.RelatedAsset]):
            The peer resources of the relationship.
    """

    relationship_attributes: "RelationshipAttributes" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="RelationshipAttributes",
    )
    assets: MutableSequence["RelatedAsset"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="RelatedAsset",
    )


class RelationshipAttributes(proto.Message):
    r"""DEPRECATED. This message only presents for the purpose of
    backward-compatibility. The server will never populate this message
    in responses. The relationship attributes which include ``type``,
    ``source_resource_type``, ``target_resource_type`` and ``action``.

    Attributes:
        type_ (str):
            The unique identifier of the relationship type. Example:
            ``INSTANCE_TO_INSTANCEGROUP``
        source_resource_type (str):
            The source asset type. Example:
            ``compute.googleapis.com/Instance``
        target_resource_type (str):
            The target asset type. Example:
            ``compute.googleapis.com/Disk``
        action (str):
            The detail of the relationship, e.g. ``contains``,
            ``attaches``
    """

    type_: str = proto.Field(
        proto.STRING,
        number=4,
    )
    source_resource_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    target_resource_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    action: str = proto.Field(
        proto.STRING,
        number=3,
    )


class RelatedAsset(proto.Message):
    r"""An asset identifier in Google Cloud which contains its name, type
    and ancestors. An asset can be any resource in the Google Cloud
    `resource
    hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
    a resource outside the Google Cloud resource hierarchy (such as
    Google Kubernetes Engine clusters and objects), or a policy (e.g.
    IAM policy). See `Supported asset
    types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
    for more information.

    Attributes:
        asset (str):
            The full name of the asset. Example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``

            See `Resource
            names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.
        asset_type (str):
            The type of the asset. Example:
            ``compute.googleapis.com/Disk``

            See `Supported asset
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
            for more information.
        ancestors (MutableSequence[str]):
            The ancestors of an asset in Google Cloud `resource
            hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
            represented as a list of relative resource names. An
            ancestry path starts with the closest ancestor in the
            hierarchy and ends at root.

            Example:
            ``["projects/123456789", "folders/5432", "organizations/1234"]``
        relationship_type (str):
            The unique identifier of the relationship type. Example:
            ``INSTANCE_TO_INSTANCEGROUP``
    """

    asset: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    ancestors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    relationship_type: str = proto.Field(
        proto.STRING,
        number=4,
    )


class Tag(proto.Message):
    r"""The key and value for a
    `tag <https://cloud.google.com/resource-manager/docs/tags/tags-overview>`__.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        tag_key (str):
            TagKey namespaced name, in the format of
            {ORG_ID}/{TAG_KEY_SHORT_NAME}.

            This field is a member of `oneof`_ ``_tag_key``.
        tag_key_id (str):
            TagKey ID, in the format of tagKeys/{TAG_KEY_ID}.

            This field is a member of `oneof`_ ``_tag_key_id``.
        tag_value (str):
            TagValue namespaced name, in the format of
            {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}.

            This field is a member of `oneof`_ ``_tag_value``.
        tag_value_id (str):
            TagValue ID, in the format of tagValues/{TAG_VALUE_ID}.

            This field is a member of `oneof`_ ``_tag_value_id``.
    """

    tag_key: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    tag_key_id: str = proto.Field(
        proto.STRING,
        number=2,
        optional=True,
    )
    tag_value: str = proto.Field(
        proto.STRING,
        number=3,
        optional=True,
    )
    tag_value_id: str = proto.Field(
        proto.STRING,
        number=4,
        optional=True,
    )


class EffectiveTagDetails(proto.Message):
    r"""The effective tags and the ancestor resources from which they
    were inherited.


    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        attached_resource (str):
            The `full resource
            name <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            of the ancestor from which
            [effective_tags][google.cloud.asset.v1.EffectiveTagDetails.effective_tags]
            are inherited, according to `tag
            inheritance <https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance>`__.

            This field is a member of `oneof`_ ``_attached_resource``.
        effective_tags (MutableSequence[google.cloud.asset_v1.types.Tag]):
            The effective tags inherited from the
            [attached_resource][google.cloud.asset.v1.EffectiveTagDetails.attached_resource].
            Note that tags with the same key but different values may
            attach to resources at a different hierarchy levels. The
            lower hierarchy tag value will overwrite the higher
            hierarchy tag value of the same tag key. In this case, the
            tag value at the higher hierarchy level will be removed. For
            more information, see `tag
            inheritance <https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance>`__.
    """

    attached_resource: str = proto.Field(
        proto.STRING,
        number=1,
        optional=True,
    )
    effective_tags: MutableSequence["Tag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=2,
        message="Tag",
    )


class ResourceSearchResult(proto.Message):
    r"""A result of Resource Search, containing information of a
    cloud resource.

    Attributes:
        name (str):
            The full resource name of this resource. Example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
            See `Cloud Asset Inventory Resource Name
            Format <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            for more information.

            To search against the ``name``:

            - Use a field query. Example: ``name:instance1``
            - Use a free text query. Example: ``instance1``
        asset_type (str):
            The type of this resource. Example:
            ``compute.googleapis.com/Disk``.

            To search against the ``asset_type``:

            - Specify the ``asset_type`` field in your search request.
        project (str):
            The project that this resource belongs to, in the form of
            projects/{PROJECT_NUMBER}. This field is available when the
            resource belongs to a project.

            To search against ``project``:

            - Use a field query. Example: ``project:12345``
            - Use a free text query. Example: ``12345``
            - Specify the ``scope`` field as this project in your search
              request.
        folders (MutableSequence[str]):
            The folder(s) that this resource belongs to, in the form of
            folders/{FOLDER_NUMBER}. This field is available when the
            resource belongs to one or more folders.

            To search against ``folders``:

            - Use a field query. Example: ``folders:(123 OR 456)``
            - Use a free text query. Example: ``123``
            - Specify the ``scope`` field as this folder in your search
              request.
        organization (str):
            The organization that this resource belongs to, in the form
            of organizations/{ORGANIZATION_NUMBER}. This field is
            available when the resource belongs to an organization.

            To search against ``organization``:

            - Use a field query. Example: ``organization:123``
            - Use a free text query. Example: ``123``
            - Specify the ``scope`` field as this organization in your
              search request.
        display_name (str):
            The display name of this resource. This field is available
            only when the resource's Protobuf contains it.

            To search against the ``display_name``:

            - Use a field query. Example: ``displayName:"My Instance"``
            - Use a free text query. Example: ``"My Instance"``
        description (str):
            One or more paragraphs of text description of this resource.
            Maximum length could be up to 1M bytes. This field is
            available only when the resource's Protobuf contains it.

            To search against the ``description``:

            - Use a field query. Example:
              ``description:"important instance"``
            - Use a free text query. Example: ``"important instance"``
        location (str):
            Location can be ``global``, regional like ``us-east1``, or
            zonal like ``us-west1-b``. This field is available only when
            the resource's Protobuf contains it.

            To search against the ``location``:

            - Use a field query. Example: ``location:us-west*``
            - Use a free text query. Example: ``us-west*``
        labels (MutableMapping[str, str]):
            User labels associated with this resource. See `Labelling
            and grouping Google Cloud
            resources <https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources>`__
            for more information. This field is available only when the
            resource's Protobuf contains it.

            To search against the ``labels``:

            - Use a field query:

              - query on any label's key or value. Example:
                ``labels:prod``
              - query by a given label. Example: ``labels.env:prod``
              - query by a given label's existence. Example:
                ``labels.env:*``

            - Use a free text query. Example: ``prod``
        network_tags (MutableSequence[str]):
            Network tags associated with this resource. Like labels,
            network tags are a type of annotations used to group Google
            Cloud resources. See `Labelling Google Cloud
            resources <https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources>`__
            for more information. This field is available only when the
            resource's Protobuf contains it.

            To search against the ``network_tags``:

            - Use a field query. Example: ``networkTags:internal``
            - Use a free text query. Example: ``internal``
        kms_key (str):
            The Cloud KMS
            `CryptoKey <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys>`__
            name or
            `CryptoKeyVersion <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions>`__
            name.

            This field only presents for the purpose of backward
            compatibility. Use the ``kms_keys`` field to retrieve Cloud
            KMS key information. This field is available only when the
            resource's Protobuf contains it and will only be populated
            for `these resource
            types <https://cloud.google.com/asset-inventory/docs/legacy-field-names#resource_types_with_the_to_be_deprecated_kmskey_field>`__
            for backward compatible purposes.

            To search against the ``kms_key``:

            - Use a field query. Example: ``kmsKey:key``
            - Use a free text query. Example: ``key``
        kms_keys (MutableSequence[str]):
            The Cloud KMS
            `CryptoKey <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys>`__
            names or
            `CryptoKeyVersion <https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions>`__
            names. This field is available only when the resource's
            Protobuf contains it.

            To search against the ``kms_keys``:

            - Use a field query. Example: ``kmsKeys:key``
            - Use a free text query. Example: ``key``
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The create timestamp of this resource, at which the resource
            was created. The granularity is in seconds. Timestamp.nanos
            will always be 0. This field is available only when the
            resource's Protobuf contains it.

            To search against ``create_time``:

            - Use a field query.

              - value in seconds since unix epoch. Example:
                ``createTime > 1609459200``
              - value in date string. Example:
                ``createTime > 2021-01-01``
              - value in date-time string (must be quoted). Example:
                ``createTime > "2021-01-01T00:00:00"``
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The last update timestamp of this resource, at which the
            resource was last modified or deleted. The granularity is in
            seconds. Timestamp.nanos will always be 0. This field is
            available only when the resource's Protobuf contains it.

            To search against ``update_time``:

            - Use a field query.

              - value in seconds since unix epoch. Example:
                ``updateTime < 1609459200``
              - value in date string. Example:
                ``updateTime < 2021-01-01``
              - value in date-time string (must be quoted). Example:
                ``updateTime < "2021-01-01T00:00:00"``
        state (str):
            The state of this resource. Different resources types have
            different state definitions that are mapped from various
            fields of different resource types. This field is available
            only when the resource's Protobuf contains it.

            Example: If the resource is an instance provided by Compute
            Engine, its state will include PROVISIONING, STAGING,
            RUNNING, STOPPING, SUSPENDING, SUSPENDED, REPAIRING, and
            TERMINATED. See ``status`` definition in `API
            Reference <https://cloud.google.com/compute/docs/reference/rest/v1/instances>`__.
            If the resource is a project provided by Resource Manager,
            its state will include LIFECYCLE_STATE_UNSPECIFIED, ACTIVE,
            DELETE_REQUESTED and DELETE_IN_PROGRESS. See
            ``lifecycleState`` definition in `API
            Reference <https://cloud.google.com/resource-manager/reference/rest/v1/projects>`__.

            To search against the ``state``:

            - Use a field query. Example: ``state:RUNNING``
            - Use a free text query. Example: ``RUNNING``
        additional_attributes (google.protobuf.struct_pb2.Struct):
            The additional searchable attributes of this resource. The
            attributes may vary from one resource type to another.
            Examples: ``projectId`` for Project, ``dnsName`` for DNS
            ManagedZone. This field contains a subset of the resource
            metadata fields that are returned by the List or Get APIs
            provided by the corresponding Google Cloud service (e.g.,
            Compute Engine). see `API references and supported
            searchable
            attributes <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
            to see which fields are included.

            You can search values of these fields through free text
            search. However, you should not consume the field
            programically as the field names and values may change as
            the Google Cloud service updates to a new incompatible API
            version.

            To search against the ``additional_attributes``:

            - Use a free text query to match the attributes values.
              Example: to search
              ``additional_attributes = { dnsName: "foobar" }``, you can
              issue a query ``foobar``.
        parent_full_resource_name (str):
            The full resource name of this resource's parent, if it has
            one. To search against the ``parent_full_resource_name``:

            - Use a field query. Example:
              ``parentFullResourceName:"project-name"``
            - Use a free text query. Example: ``project-name``
        versioned_resources (MutableSequence[google.cloud.asset_v1.types.VersionedResource]):
            Versioned resource representations of this resource. This is
            repeated because there could be multiple versions of
            resource representations during version migration.

            This ``versioned_resources`` field is not searchable. Some
            attributes of the resource representations are exposed in
            ``additional_attributes`` field, so as to allow users to
            search on them.
        attached_resources (MutableSequence[google.cloud.asset_v1.types.AttachedResource]):
            Attached resources of this resource. For example, an
            OSConfig Inventory is an attached resource of a Compute
            Instance. This field is repeated because a resource could
            have multiple attached resources.

            This ``attached_resources`` field is not searchable. Some
            attributes of the attached resources are exposed in
            ``additional_attributes`` field, so as to allow users to
            search on them.
        relationships (MutableMapping[str, google.cloud.asset_v1.types.RelatedResources]):
            A map of related resources of this resource, keyed by the
            relationship type. A relationship type is in the format of
            {SourceType}\ *{ACTION}*\ {DestType}. Example:
            ``DISK_TO_INSTANCE``, ``DISK_TO_NETWORK``,
            ``INSTANCE_TO_INSTANCEGROUP``. See `supported relationship
            types <https://cloud.google.com/asset-inventory/docs/supported-asset-types#supported_relationship_types>`__.
        tag_keys (MutableSequence[str]):
            This field is only present for the purpose of backward
            compatibility. Use the ``tags`` field instead.

            TagKey namespaced names, in the format of
            {ORG_ID}/{TAG_KEY_SHORT_NAME}. To search against the
            ``tagKeys``:

            - Use a field query. Example:

              - ``tagKeys:"123456789/env*"``
              - ``tagKeys="123456789/env"``
              - ``tagKeys:"env"``

            - Use a free text query. Example:

              - ``env``
        tag_values (MutableSequence[str]):
            This field is only present for the purpose of backward
            compatibility. Use the ``tags`` field instead.

            TagValue namespaced names, in the format of
            {ORG_ID}/{TAG_KEY_SHORT_NAME}/{TAG_VALUE_SHORT_NAME}. To
            search against the ``tagValues``:

            - Use a field query. Example:

              - ``tagValues:"env"``
              - ``tagValues:"env/prod"``
              - ``tagValues:"123456789/env/prod*"``
              - ``tagValues="123456789/env/prod"``

            - Use a free text query. Example:

              - ``prod``
        tag_value_ids (MutableSequence[str]):
            This field is only present for the purpose of backward
            compatibility. Use the ``tags`` field instead.

            TagValue IDs, in the format of tagValues/{TAG_VALUE_ID}. To
            search against the ``tagValueIds``:

            - Use a field query. Example:

              - ``tagValueIds="tagValues/456"``

            - Use a free text query. Example:

              - ``456``
        tags (MutableSequence[google.cloud.asset_v1.types.Tag]):
            The tags directly attached to this resource.

            To search against the ``tags``:

            - Use a field query. Example:

              - ``tagKeys:"123456789/env*"``
              - ``tagKeys="123456789/env"``
              - ``tagKeys:"env"``
              - ``tagKeyIds="tagKeys/123"``
              - ``tagValues:"env"``
              - ``tagValues:"env/prod"``
              - ``tagValues:"123456789/env/prod*"``
              - ``tagValues="123456789/env/prod"``
              - ``tagValueIds="tagValues/456"``

            - Use a free text query. Example:

              - ``env/prod``
        effective_tags (MutableSequence[google.cloud.asset_v1.types.EffectiveTagDetails]):
            The effective tags on this resource. All of the tags that
            are both attached to and inherited by a resource are
            collectively called the effective tags. For more
            information, see `tag
            inheritance <https://cloud.google.com/resource-manager/docs/tags/tags-overview#inheritance>`__.

            To search against the ``effective_tags``:

            - Use a field query. Example:

              - ``effectiveTagKeys:"123456789/env*"``
              - ``effectiveTagKeys="123456789/env"``
              - ``effectiveTagKeys:"env"``
              - ``effectiveTagKeyIds="tagKeys/123"``
              - ``effectiveTagValues:"env"``
              - ``effectiveTagValues:"env/prod"``
              - ``effectiveTagValues:"123456789/env/prod*"``
              - ``effectiveTagValues="123456789/env/prod"``
              - ``effectiveTagValueIds="tagValues/456"``
        enrichments (MutableSequence[google.cloud.asset_v1.types.AssetEnrichment]):
            Enrichments of the asset. Currently supported enrichment
            types with SearchAllResources API:

            - RESOURCE_OWNERS

            The corresponding read masks in order to get the enrichment:

            - enrichments.resource_owners

            The corresponding required permissions:

            - cloudasset.assets.searchEnrichmentResourceOwners

            Example query to get resource owner enrichment:

            ::

                 scope: "projects/my-project"
                 query: "name: my-project"
                 assetTypes: "cloudresourcemanager.googleapis.com/Project"
                 readMask: {
                    paths: "asset_type"
                    paths: "name"
                    paths: "enrichments.resource_owners"
                 }
        parent_asset_type (str):
            The type of this resource's immediate parent, if there is
            one.

            To search against the ``parent_asset_type``:

            - Use a field query. Example:
              ``parentAssetType:"cloudresourcemanager.googleapis.com/Project"``
            - Use a free text query. Example:
              ``cloudresourcemanager.googleapis.com/Project``
        scc_security_marks (MutableMapping[str, str]):
            The actual content of Security Command Center security marks
            associated with the asset.

            To search against SCC SecurityMarks field:

            - Use a field query:

              - query by a given key value pair. Example:
                ``sccSecurityMarks.foo=bar``
              - query by a given key's existence. Example:
                ``sccSecurityMarks.foo:*``
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )
    folders: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=17,
    )
    organization: str = proto.Field(
        proto.STRING,
        number=18,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    location: str = proto.Field(
        proto.STRING,
        number=6,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=7,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=8,
    )
    kms_key: str = proto.Field(
        proto.STRING,
        number=10,
    )
    kms_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=28,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=12,
        message=timestamp_pb2.Timestamp,
    )
    state: str = proto.Field(
        proto.STRING,
        number=13,
    )
    additional_attributes: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=9,
        message=struct_pb2.Struct,
    )
    parent_full_resource_name: str = proto.Field(
        proto.STRING,
        number=19,
    )
    versioned_resources: MutableSequence["VersionedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=16,
        message="VersionedResource",
    )
    attached_resources: MutableSequence["AttachedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=20,
        message="AttachedResource",
    )
    relationships: MutableMapping[str, "RelatedResources"] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=21,
        message="RelatedResources",
    )
    tag_keys: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=23,
    )
    tag_values: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=25,
    )
    tag_value_ids: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=26,
    )
    tags: MutableSequence["Tag"] = proto.RepeatedField(
        proto.MESSAGE,
        number=29,
        message="Tag",
    )
    effective_tags: MutableSequence["EffectiveTagDetails"] = proto.RepeatedField(
        proto.MESSAGE,
        number=30,
        message="EffectiveTagDetails",
    )
    enrichments: MutableSequence["AssetEnrichment"] = proto.RepeatedField(
        proto.MESSAGE,
        number=31,
        message="AssetEnrichment",
    )
    parent_asset_type: str = proto.Field(
        proto.STRING,
        number=103,
    )
    scc_security_marks: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=32,
    )


class VersionedResource(proto.Message):
    r"""Resource representation as defined by the corresponding
    service providing the resource for a given API version.

    Attributes:
        version (str):
            API version of the resource.

            Example: If the resource is an instance provided by Compute
            Engine v1 API as defined in
            ``https://cloud.google.com/compute/docs/reference/rest/v1/instances``,
            version will be "v1".
        resource (google.protobuf.struct_pb2.Struct):
            JSON representation of the resource as defined by the
            corresponding service providing this resource.

            Example: If the resource is an instance provided by Compute
            Engine, this field will contain the JSON representation of
            the instance as defined by Compute Engine:
            ``https://cloud.google.com/compute/docs/reference/rest/v1/instances``.

            You can find the resource definition for each supported
            resource type in this table:
            ``https://cloud.google.com/asset-inventory/docs/supported-asset-types``
    """

    version: str = proto.Field(
        proto.STRING,
        number=1,
    )
    resource: struct_pb2.Struct = proto.Field(
        proto.MESSAGE,
        number=2,
        message=struct_pb2.Struct,
    )


class AttachedResource(proto.Message):
    r"""Attached resource representation, which is defined by the
    corresponding service provider. It represents an attached
    resource's payload.

    Attributes:
        asset_type (str):
            The type of this attached resource.

            Example: ``osconfig.googleapis.com/Inventory``

            You can find the supported attached asset types of each
            resource in this table:
            ``https://cloud.google.com/asset-inventory/docs/supported-asset-types``
        versioned_resources (MutableSequence[google.cloud.asset_v1.types.VersionedResource]):
            Versioned resource representations of this
            attached resource. This is repeated because
            there could be multiple versions of the attached
            resource representations during version
            migration.
    """

    asset_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    versioned_resources: MutableSequence["VersionedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message="VersionedResource",
    )


class RelatedResources(proto.Message):
    r"""The related resources of the primary resource.

    Attributes:
        related_resources (MutableSequence[google.cloud.asset_v1.types.RelatedResource]):
            The detailed related resources of the primary
            resource.
    """

    related_resources: MutableSequence["RelatedResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="RelatedResource",
    )


class RelatedResource(proto.Message):
    r"""The detailed related resource.

    Attributes:
        asset_type (str):
            The type of the asset. Example:
            ``compute.googleapis.com/Instance``
        full_resource_name (str):
            The full resource name of the related resource. Example:
            ``//compute.googleapis.com/projects/my_proj_123/zones/instance/instance123``
    """

    asset_type: str = proto.Field(
        proto.STRING,
        number=1,
    )
    full_resource_name: str = proto.Field(
        proto.STRING,
        number=2,
    )


class IamPolicySearchResult(proto.Message):
    r"""A result of IAM Policy search, containing information of an
    IAM policy.

    Attributes:
        resource (str):
            The full resource name of the resource associated with this
            IAM policy. Example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
            See `Cloud Asset Inventory Resource Name
            Format <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            for more information.

            To search against the ``resource``:

            - use a field query. Example: ``resource:organizations/123``
        asset_type (str):
            The type of the resource associated with this IAM policy.
            Example: ``compute.googleapis.com/Disk``.

            To search against the ``asset_type``:

            - specify the ``asset_types`` field in your search request.
        project (str):
            The project that the associated Google Cloud resource
            belongs to, in the form of projects/{PROJECT_NUMBER}. If an
            IAM policy is set on a resource (like VM instance, Cloud
            Storage bucket), the project field will indicate the project
            that contains the resource. If an IAM policy is set on a
            folder or organization, this field will be empty.

            To search against the ``project``:

            - specify the ``scope`` field as this project in your search
              request.
        folders (MutableSequence[str]):
            The folder(s) that the IAM policy belongs to, in the form of
            folders/{FOLDER_NUMBER}. This field is available when the
            IAM policy belongs to one or more folders.

            To search against ``folders``:

            - use a field query. Example: ``folders:(123 OR 456)``
            - use a free text query. Example: ``123``
            - specify the ``scope`` field as this folder in your search
              request.
        organization (str):
            The organization that the IAM policy belongs to, in the form
            of organizations/{ORGANIZATION_NUMBER}. This field is
            available when the IAM policy belongs to an organization.

            To search against ``organization``:

            - use a field query. Example: ``organization:123``
            - use a free text query. Example: ``123``
            - specify the ``scope`` field as this organization in your
              search request.
        policy (google.iam.v1.policy_pb2.Policy):
            The IAM policy directly set on the given resource. Note that
            the original IAM policy can contain multiple bindings. This
            only contains the bindings that match the given query. For
            queries that don't contain a constrain on policies (e.g., an
            empty query), this contains all the bindings.

            To search against the ``policy`` bindings:

            - use a field query:

              - query by the policy contained members. Example:
                ``policy:amy@gmail.com``
              - query by the policy contained roles. Example:
                ``policy:roles/compute.admin``
              - query by the policy contained roles' included
                permissions. Example:
                ``policy.role.permissions:compute.instances.create``
        explanation (google.cloud.asset_v1.types.IamPolicySearchResult.Explanation):
            Explanation about the IAM policy search
            result. It contains additional information to
            explain why the search result matches the query.
    """

    class Explanation(proto.Message):
        r"""Explanation about the IAM policy search result.

        Attributes:
            matched_permissions (MutableMapping[str, google.cloud.asset_v1.types.IamPolicySearchResult.Explanation.Permissions]):
                The map from roles to their included permissions that match
                the permission query (i.e., a query containing
                ``policy.role.permissions:``). Example: if query
                ``policy.role.permissions:compute.disk.get`` matches a
                policy binding that contains owner role, the
                matched_permissions will be
                ``{"roles/owner": ["compute.disk.get"]}``. The roles can
                also be found in the returned ``policy`` bindings. Note that
                the map is populated only for requests with permission
                queries.
        """

        class Permissions(proto.Message):
            r"""IAM permissions

            Attributes:
                permissions (MutableSequence[str]):
                    A list of permissions. A sample permission string:
                    ``compute.disk.get``.
            """

            permissions: MutableSequence[str] = proto.RepeatedField(
                proto.STRING,
                number=1,
            )

        matched_permissions: MutableMapping[
            str, "IamPolicySearchResult.Explanation.Permissions"
        ] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="IamPolicySearchResult.Explanation.Permissions",
        )

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    asset_type: str = proto.Field(
        proto.STRING,
        number=5,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    folders: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
    )
    organization: str = proto.Field(
        proto.STRING,
        number=7,
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=3,
        message=policy_pb2.Policy,
    )
    explanation: Explanation = proto.Field(
        proto.MESSAGE,
        number=4,
        message=Explanation,
    )


class IamPolicyAnalysisState(proto.Message):
    r"""Represents the detailed state of an entity under analysis,
    such as a resource, an identity or an access.

    Attributes:
        code (google.rpc.code_pb2.Code):
            The Google standard error code that best describes the
            state. For example:

            - OK means the analysis on this entity has been successfully
              finished;
            - PERMISSION_DENIED means an access denied error is
              encountered;
            - DEADLINE_EXCEEDED means the analysis on this entity hasn't
              been started in time;
        cause (str):
            The human-readable description of the cause
            of failure.
    """

    code: code_pb2.Code = proto.Field(
        proto.ENUM,
        number=1,
        enum=code_pb2.Code,
    )
    cause: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ConditionEvaluation(proto.Message):
    r"""The condition evaluation.

    Attributes:
        evaluation_value (google.cloud.asset_v1.types.ConditionEvaluation.EvaluationValue):
            The evaluation result.
    """

    class EvaluationValue(proto.Enum):
        r"""Value of this expression.

        Values:
            EVALUATION_VALUE_UNSPECIFIED (0):
                Reserved for future use.
            TRUE (1):
                The evaluation result is ``true``.
            FALSE (2):
                The evaluation result is ``false``.
            CONDITIONAL (3):
                The evaluation result is ``conditional`` when the condition
                expression contains variables that are either missing input
                values or have not been supported by Policy Analyzer yet.
        """

        EVALUATION_VALUE_UNSPECIFIED = 0
        TRUE = 1
        FALSE = 2
        CONDITIONAL = 3

    evaluation_value: EvaluationValue = proto.Field(
        proto.ENUM,
        number=1,
        enum=EvaluationValue,
    )


class IamPolicyAnalysisResult(proto.Message):
    r"""IAM Policy analysis result, consisting of one IAM policy
    binding and derived access control lists.

    Attributes:
        attached_resource_full_name (str):
            The `full resource
            name <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            of the resource to which the
            [iam_binding][google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding]
            policy attaches.
        iam_binding (google.iam.v1.policy_pb2.Binding):
            The IAM policy binding under analysis.
        access_control_lists (MutableSequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult.AccessControlList]):
            The access control lists derived from the
            [iam_binding][google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding]
            that match or potentially match resource and access
            selectors specified in the request.
        identity_list (google.cloud.asset_v1.types.IamPolicyAnalysisResult.IdentityList):
            The identity list derived from members of the
            [iam_binding][google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding]
            that match or potentially match identity selector specified
            in the request.
        fully_explored (bool):
            Represents whether all analyses on the
            [iam_binding][google.cloud.asset.v1.IamPolicyAnalysisResult.iam_binding]
            have successfully finished.
    """

    class Resource(proto.Message):
        r"""A Google Cloud resource under analysis.

        Attributes:
            full_resource_name (str):
                The `full resource
                name <https://cloud.google.com/asset-inventory/docs/resource-name-format>`__
            analysis_state (google.cloud.asset_v1.types.IamPolicyAnalysisState):
                The analysis state of this resource.
        """

        full_resource_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        analysis_state: "IamPolicyAnalysisState" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="IamPolicyAnalysisState",
        )

    class Access(proto.Message):
        r"""An IAM role or permission under analysis.

        This message has `oneof`_ fields (mutually exclusive fields).
        For each oneof, at most one member field can be set at the same time.
        Setting any member of the oneof automatically clears all other
        members.

        .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

        Attributes:
            role (str):
                The role.

                This field is a member of `oneof`_ ``oneof_access``.
            permission (str):
                The permission.

                This field is a member of `oneof`_ ``oneof_access``.
            analysis_state (google.cloud.asset_v1.types.IamPolicyAnalysisState):
                The analysis state of this access.
        """

        role: str = proto.Field(
            proto.STRING,
            number=1,
            oneof="oneof_access",
        )
        permission: str = proto.Field(
            proto.STRING,
            number=2,
            oneof="oneof_access",
        )
        analysis_state: "IamPolicyAnalysisState" = proto.Field(
            proto.MESSAGE,
            number=3,
            message="IamPolicyAnalysisState",
        )

    class Identity(proto.Message):
        r"""An identity under analysis.

        Attributes:
            name (str):
                The identity of members, formatted as appear in an `IAM
                policy
                binding <https://cloud.google.com/iam/reference/rest/v1/Binding>`__.
                For example, they might be formatted like the following:

                - user:foo@google.com
                - group:group1@google.com
                - serviceAccount:s1@prj1.iam.gserviceaccount.com
                - projectOwner:some_project_id
                - domain:google.com
                - allUsers
            analysis_state (google.cloud.asset_v1.types.IamPolicyAnalysisState):
                The analysis state of this identity.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        analysis_state: "IamPolicyAnalysisState" = proto.Field(
            proto.MESSAGE,
            number=2,
            message="IamPolicyAnalysisState",
        )

    class Edge(proto.Message):
        r"""A directional edge.

        Attributes:
            source_node (str):
                The source node of the edge. For example, it
                could be a full resource name for a resource
                node or an email of an identity.
            target_node (str):
                The target node of the edge. For example, it
                could be a full resource name for a resource
                node or an email of an identity.
        """

        source_node: str = proto.Field(
            proto.STRING,
            number=1,
        )
        target_node: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AccessControlList(proto.Message):
        r"""An access control list, derived from the above IAM policy binding,
        which contains a set of resources and accesses. May include one item
        from each set to compose an access control entry.

        NOTICE that there could be multiple access control lists for one IAM
        policy binding. The access control lists are created based on
        resource and access combinations.

        For example, assume we have the following cases in one IAM policy
        binding:

        - Permission P1 and P2 apply to resource R1 and R2;
        - Permission P3 applies to resource R2 and R3;

        This will result in the following access control lists:

        - AccessControlList 1: [R1, R2], [P1, P2]
        - AccessControlList 2: [R2, R3], [P3]

        Attributes:
            resources (MutableSequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult.Resource]):
                The resources that match one of the following conditions:

                - The resource_selector, if it is specified in request;
                - Otherwise, resources reachable from the policy attached
                  resource.
            accesses (MutableSequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult.Access]):
                The accesses that match one of the following conditions:

                - The access_selector, if it is specified in request;
                - Otherwise, access specifiers reachable from the policy
                  binding's role.
            resource_edges (MutableSequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult.Edge]):
                Resource edges of the graph starting from the policy
                attached resource to any descendant resources. The
                [Edge.source_node][google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.source_node]
                contains the full resource name of a parent resource and
                [Edge.target_node][google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.target_node]
                contains the full resource name of a child resource. This
                field is present only if the output_resource_edges option is
                enabled in request.
            condition_evaluation (google.cloud.asset_v1.types.ConditionEvaluation):
                Condition evaluation for this
                AccessControlList, if there is a condition
                defined in the above IAM policy binding.
        """

        resources: MutableSequence["IamPolicyAnalysisResult.Resource"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="IamPolicyAnalysisResult.Resource",
            )
        )
        accesses: MutableSequence["IamPolicyAnalysisResult.Access"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="IamPolicyAnalysisResult.Access",
            )
        )
        resource_edges: MutableSequence["IamPolicyAnalysisResult.Edge"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=3,
                message="IamPolicyAnalysisResult.Edge",
            )
        )
        condition_evaluation: "ConditionEvaluation" = proto.Field(
            proto.MESSAGE,
            number=4,
            message="ConditionEvaluation",
        )

    class IdentityList(proto.Message):
        r"""The identities and group edges.

        Attributes:
            identities (MutableSequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult.Identity]):
                Only the identities that match one of the following
                conditions will be presented:

                - The identity_selector, if it is specified in request;
                - Otherwise, identities reachable from the policy binding's
                  members.
            group_edges (MutableSequence[google.cloud.asset_v1.types.IamPolicyAnalysisResult.Edge]):
                Group identity edges of the graph starting from the
                binding's group members to any node of the
                [identities][google.cloud.asset.v1.IamPolicyAnalysisResult.IdentityList.identities].
                The
                [Edge.source_node][google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.source_node]
                contains a group, such as ``group:parent@google.com``. The
                [Edge.target_node][google.cloud.asset.v1.IamPolicyAnalysisResult.Edge.target_node]
                contains a member of the group, such as
                ``group:child@google.com`` or ``user:foo@google.com``. This
                field is present only if the output_group_edges option is
                enabled in request.
        """

        identities: MutableSequence["IamPolicyAnalysisResult.Identity"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=1,
                message="IamPolicyAnalysisResult.Identity",
            )
        )
        group_edges: MutableSequence["IamPolicyAnalysisResult.Edge"] = (
            proto.RepeatedField(
                proto.MESSAGE,
                number=2,
                message="IamPolicyAnalysisResult.Edge",
            )
        )

    attached_resource_full_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    iam_binding: policy_pb2.Binding = proto.Field(
        proto.MESSAGE,
        number=2,
        message=policy_pb2.Binding,
    )
    access_control_lists: MutableSequence[AccessControlList] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AccessControlList,
    )
    identity_list: IdentityList = proto.Field(
        proto.MESSAGE,
        number=4,
        message=IdentityList,
    )
    fully_explored: bool = proto.Field(
        proto.BOOL,
        number=5,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
