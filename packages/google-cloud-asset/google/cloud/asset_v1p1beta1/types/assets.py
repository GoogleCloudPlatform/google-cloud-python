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

import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import proto  # type: ignore

__protobuf__ = proto.module(
    package="google.cloud.asset.v1p1beta1",
    manifest={
        "StandardResourceMetadata",
        "IamPolicySearchResult",
        "Permissions",
    },
)


class StandardResourceMetadata(proto.Message):
    r"""The standard metadata of a cloud resource.

    Attributes:
        name (str):
            The full resource name. For example:
            ``//compute.googleapis.com/projects/my_project_123/zones/zone1/instances/instance1``.
            See `Resource
            Names <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            for more information.
        asset_type (str):
            The type of this resource.
            For example: "compute.googleapis.com/Disk".
        project (str):
            The project that this resource belongs to, in the form of
            ``projects/{project_number}``.
        display_name (str):
            The display name of this resource.
        description (str):
            One or more paragraphs of text description of
            this resource. Maximum length could be up to 1M
            bytes.
        additional_attributes (MutableSequence[str]):
            Additional searchable attributes of this
            resource. Informational only. The exact set of
            attributes is subject to change. For example:
            project id, DNS name etc.
        location (str):
            Location can be "global", regional like
            "us-east1", or zonal like "us-west1-b".
        labels (MutableMapping[str, str]):
            Labels associated with this resource. See `Labelling and
            grouping Google Cloud
            resources <https://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources>`__
            for more information.
        network_tags (MutableSequence[str]):
            Network tags associated with this resource. Like labels,
            network tags are a type of annotations used to group Google
            Cloud resources. See `Labelling Google Cloud
            resources <lhttps://cloud.google.com/blog/products/gcp/labelling-and-grouping-your-google-cloud-platform-resources>`__
            for more information.
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
    display_name: str = proto.Field(
        proto.STRING,
        number=4,
    )
    description: str = proto.Field(
        proto.STRING,
        number=5,
    )
    additional_attributes: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=10,
    )
    location: str = proto.Field(
        proto.STRING,
        number=11,
    )
    labels: MutableMapping[str, str] = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=12,
    )
    network_tags: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=13,
    )


class IamPolicySearchResult(proto.Message):
    r"""The result for an IAM policy search.

    Attributes:
        resource (str):
            The `full resource
            name <https://cloud.google.com/apis/design/resource_names#full_resource_name>`__
            of the resource associated with this IAM policy.
        project (str):
            The project that the associated Google Cloud resource
            belongs to, in the form of ``projects/{project_number}``. If
            an IAM policy is set on a resource -- such as a Compute
            Engine instance or a Cloud Storage bucket -- the project
            field will indicate the project that contains the resource.
            If an IAM policy is set on a folder or organization, the
            project field will be empty.
        policy (google.iam.v1.policy_pb2.Policy):
            The IAM policy attached to the specified
            resource. Note that the original IAM policy can
            contain multiple bindings. This only contains
            the bindings that match the given query. For
            queries that don't contain a constraint on
            policies (e.g. an empty query), this contains
            all the bindings.
        explanation (google.cloud.asset_v1p1beta1.types.IamPolicySearchResult.Explanation):
            Explanation about the IAM policy search
            result. It contains additional information that
            explains why the search result matches the
            query.
    """

    class Explanation(proto.Message):
        r"""Explanation about the IAM policy search result.

        Attributes:
            matched_permissions (MutableMapping[str, google.cloud.asset_v1p1beta1.types.Permissions]):
                The map from roles to their included permission matching the
                permission query (e.g. containing
                ``policy.role.permissions:``). Example role string:
                "roles/compute.instanceAdmin". The roles can also be found
                in the returned ``policy`` bindings. Note that the map is
                populated only if requesting with a permission query.
        """

        matched_permissions: MutableMapping[str, "Permissions"] = proto.MapField(
            proto.STRING,
            proto.MESSAGE,
            number=1,
            message="Permissions",
        )

    resource: str = proto.Field(
        proto.STRING,
        number=1,
    )
    project: str = proto.Field(
        proto.STRING,
        number=3,
    )
    policy: policy_pb2.Policy = proto.Field(
        proto.MESSAGE,
        number=4,
        message=policy_pb2.Policy,
    )
    explanation: Explanation = proto.Field(
        proto.MESSAGE,
        number=5,
        message=Explanation,
    )


class Permissions(proto.Message):
    r"""IAM permissions.

    Attributes:
        permissions (MutableSequence[str]):
            A list of permissions. Example permission
            string: "compute.disk.get".
    """

    permissions: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
