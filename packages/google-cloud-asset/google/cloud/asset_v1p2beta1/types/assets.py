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
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.asset.v1p2beta1",
    manifest={
        "TemporalAsset",
        "TimeWindow",
        "Asset",
        "Resource",
    },
)


class TemporalAsset(proto.Message):
    r"""An asset in Google Cloud and its temporal metadata, including
    the time window when it was observed and its status during that
    window.

    Attributes:
        window (google.cloud.asset_v1p2beta1.types.TimeWindow):
            The time window when the asset data and state
            was observed.
        deleted (bool):
            Whether the asset has been deleted or not.
        asset (google.cloud.asset_v1p2beta1.types.Asset):
            An asset in Google Cloud.
    """

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


class Asset(proto.Message):
    r"""An asset in Google Cloud. An asset can be any resource in the Google
    Cloud `resource
    hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`__,
    a resource outside the Google Cloud resource hierarchy (such as
    Google Kubernetes Engine clusters and objects), or a policy (e.g.
    IAM policy). See `Supported asset
    types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`__
    for more information.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
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
        resource (google.cloud.asset_v1p2beta1.types.Resource):
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
        access_policy (google.identity.accesscontextmanager.v1.access_policy_pb2.AccessPolicy):
            Please also refer to the `access policy user
            guide <https://cloud.google.com/access-context-manager/docs/overview#access-policies>`__.

            This field is a member of `oneof`_ ``access_context_policy``.
        access_level (google.identity.accesscontextmanager.v1.access_level_pb2.AccessLevel):
            Please also refer to the `access level user
            guide <https://cloud.google.com/access-context-manager/docs/overview#access-levels>`__.

            This field is a member of `oneof`_ ``access_context_policy``.
        service_perimeter (google.identity.accesscontextmanager.v1.service_perimeter_pb2.ServicePerimeter):
            Please also refer to the `service perimeter user
            guide <https://cloud.google.com/vpc-service-controls/docs/overview>`__.

            This field is a member of `oneof`_ ``access_context_policy``.
        org_policy (MutableSequence[google.cloud.orgpolicy.v1.orgpolicy_pb2.Policy]):
            A representation of an `organization
            policy <https://cloud.google.com/resource-manager/docs/organization-policy/overview#organization_policy>`__.
            There can be more than one organization policy with
            different constraints set on a given resource.
    """

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
    ancestors: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=6,
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
    org_policy: MutableSequence[orgpolicy_pb2.Policy] = proto.RepeatedField(
        proto.MESSAGE,
        number=10,
        message=orgpolicy_pb2.Policy,
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

            For third-party assets, this field may be set differently.
        data (google.protobuf.struct_pb2.Struct):
            The content of the resource, in which some
            sensitive fields are removed and may not be
            present.
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


__all__ = tuple(sorted(__protobuf__.manifest))
