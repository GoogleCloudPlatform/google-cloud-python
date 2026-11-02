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

import google.protobuf.struct_pb2 as struct_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import proto  # type: ignore

from google.cloud.securitycenter_v1.types import folder
from google.cloud.securitycenter_v1.types import security_marks as gcs_security_marks

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "Asset",
    },
)


class Asset(proto.Message):
    r"""Security Command Center representation of a Google Cloud
    resource.

    The Asset is a Security Command Center resource that captures
    information about a single Google Cloud resource. All
    modifications to an Asset are only within the context of
    Security Command Center and don't affect the referenced Google
    Cloud resource.

    Attributes:
        name (str):
            The relative resource name of this asset. See:
            https://cloud.google.com/apis/design/resource_names#relative_resource_name
            Example:
            "organizations/{organization_id}/assets/{asset_id}".
        security_center_properties (google.cloud.securitycenter_v1.types.Asset.SecurityCenterProperties):
            Security Command Center managed properties.
            These properties are managed by Security Command
            Center and cannot be modified by the user.
        resource_properties (MutableMapping[str, google.protobuf.struct_pb2.Value]):
            Resource managed properties. These properties
            are managed and defined by the Google Cloud
            resource and cannot be modified by the user.
        security_marks (google.cloud.securitycenter_v1.types.SecurityMarks):
            User specified security marks. These marks
            are entirely managed by the user and come from
            the SecurityMarks resource that belongs to the
            asset.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the asset was created in
            Security Command Center.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            The time at which the asset was last updated
            or added in Cloud SCC.
        iam_policy (google.cloud.securitycenter_v1.types.Asset.IamPolicy):
            Cloud IAM Policy information associated with
            the Google Cloud resource described by the
            Security Command Center asset. This information
            is managed and defined by the Google Cloud
            resource and cannot be modified by the user.
        canonical_name (str):
            The canonical name of the resource. It's either
            "organizations/{organization_id}/assets/{asset_id}",
            "folders/{folder_id}/assets/{asset_id}" or
            "projects/{project_number}/assets/{asset_id}", depending on
            the closest CRM ancestor of the resource.
    """

    class SecurityCenterProperties(proto.Message):
        r"""Security Command Center managed properties. These properties
        are managed by Security Command Center and cannot be modified by
        the user.

        Attributes:
            resource_name (str):
                The full resource name of the Google Cloud resource this
                asset represents. This field is immutable after create time.
                See:
                https://cloud.google.com/apis/design/resource_names#full_resource_name
            resource_type (str):
                The type of the Google Cloud resource.
                Examples include: APPLICATION, PROJECT, and
                ORGANIZATION. This is a case insensitive field
                defined by Security Command Center and/or the
                producer of the resource and is immutable after
                create time.
            resource_parent (str):
                The full resource name of the immediate parent of the
                resource. See:
                https://cloud.google.com/apis/design/resource_names#full_resource_name
            resource_project (str):
                The full resource name of the project the resource belongs
                to. See:
                https://cloud.google.com/apis/design/resource_names#full_resource_name
            resource_owners (MutableSequence[str]):
                Owners of the Google Cloud resource.
            resource_display_name (str):
                The user defined display name for this
                resource.
            resource_parent_display_name (str):
                The user defined display name for the parent
                of this resource.
            resource_project_display_name (str):
                The user defined display name for the project
                of this resource.
            folders (MutableSequence[google.cloud.securitycenter_v1.types.Folder]):
                Contains a Folder message for each folder in
                the assets ancestry. The first folder is the
                deepest nested folder, and the last folder is
                the folder directly under the Organization.
        """

        resource_name: str = proto.Field(
            proto.STRING,
            number=1,
        )
        resource_type: str = proto.Field(
            proto.STRING,
            number=2,
        )
        resource_parent: str = proto.Field(
            proto.STRING,
            number=3,
        )
        resource_project: str = proto.Field(
            proto.STRING,
            number=4,
        )
        resource_owners: MutableSequence[str] = proto.RepeatedField(
            proto.STRING,
            number=5,
        )
        resource_display_name: str = proto.Field(
            proto.STRING,
            number=6,
        )
        resource_parent_display_name: str = proto.Field(
            proto.STRING,
            number=7,
        )
        resource_project_display_name: str = proto.Field(
            proto.STRING,
            number=8,
        )
        folders: MutableSequence[folder.Folder] = proto.RepeatedField(
            proto.MESSAGE,
            number=10,
            message=folder.Folder,
        )

    class IamPolicy(proto.Message):
        r"""Cloud IAM Policy information associated with the Google Cloud
        resource described by the Security Command Center asset. This
        information is managed and defined by the Google Cloud resource
        and cannot be modified by the user.

        Attributes:
            policy_blob (str):
                The JSON representation of the Policy
                associated with the asset. See
                https://cloud.google.com/iam/reference/rest/v1/Policy
                for format details.
        """

        policy_blob: str = proto.Field(
            proto.STRING,
            number=1,
        )

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    security_center_properties: SecurityCenterProperties = proto.Field(
        proto.MESSAGE,
        number=2,
        message=SecurityCenterProperties,
    )
    resource_properties: MutableMapping[str, struct_pb2.Value] = proto.MapField(
        proto.STRING,
        proto.MESSAGE,
        number=7,
        message=struct_pb2.Value,
    )
    security_marks: gcs_security_marks.SecurityMarks = proto.Field(
        proto.MESSAGE,
        number=8,
        message=gcs_security_marks.SecurityMarks,
    )
    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    update_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=10,
        message=timestamp_pb2.Timestamp,
    )
    iam_policy: IamPolicy = proto.Field(
        proto.MESSAGE,
        number=11,
        message=IamPolicy,
    )
    canonical_name: str = proto.Field(
        proto.STRING,
        number=13,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
