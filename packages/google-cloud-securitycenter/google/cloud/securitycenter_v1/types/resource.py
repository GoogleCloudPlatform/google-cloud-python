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

from google.cloud.securitycenter_v1.types import folder

__protobuf__ = proto.module(
    package="google.cloud.securitycenter.v1",
    manifest={
        "CloudProvider",
        "Resource",
        "AwsMetadata",
        "AzureMetadata",
        "ResourcePath",
    },
)


class CloudProvider(proto.Enum):
    r"""Enumeration representing the various cloud providers a
    finding's resource could reside in.

    Values:
        CLOUD_PROVIDER_UNSPECIFIED (0):
            The cloud provider is unspecified.
        GOOGLE_CLOUD_PLATFORM (1):
            The cloud provider is Google Cloud Platform.
        AMAZON_WEB_SERVICES (2):
            The cloud provider is Amazon Web Services.
        MICROSOFT_AZURE (3):
            The cloud provider is Microsoft Azure.
    """

    CLOUD_PROVIDER_UNSPECIFIED = 0
    GOOGLE_CLOUD_PLATFORM = 1
    AMAZON_WEB_SERVICES = 2
    MICROSOFT_AZURE = 3


class Resource(proto.Message):
    r"""Information related to the Google Cloud resource.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        name (str):
            The full resource name of the resource. See:
            https://cloud.google.com/apis/design/resource_names#full_resource_name
        display_name (str):
            The human readable name of the resource.
        type_ (str):
            The full resource type of the resource.
        project (str):
            The full resource name of project that the
            resource belongs to.
        project_display_name (str):
            The project ID that the resource belongs to.
        parent (str):
            The full resource name of resource's parent.
        parent_display_name (str):
            The human readable name of resource's parent.
        folders (MutableSequence[google.cloud.securitycenter_v1.types.Folder]):
            Output only. Contains a Folder message for
            each folder in the assets ancestry. The first
            folder is the deepest nested folder, and the
            last folder is the folder directly under the
            Organization.
        cloud_provider (google.cloud.securitycenter_v1.types.CloudProvider):
            Indicates which cloud provider the resource
            resides in.
        organization (str):
            Indicates which organization or tenant in the
            cloud provider the finding applies to.
        service (str):
            The parent service or product from which the
            resource is provided, for example, GKE or SNS.
        location (str):
            The region or location of the service (if
            applicable).
        aws_metadata (google.cloud.securitycenter_v1.types.AwsMetadata):
            The AWS metadata associated with the finding.

            This field is a member of `oneof`_ ``cloud_provider_metadata``.
        azure_metadata (google.cloud.securitycenter_v1.types.AzureMetadata):
            The Azure metadata associated with the
            finding.

            This field is a member of `oneof`_ ``cloud_provider_metadata``.
        resource_path (google.cloud.securitycenter_v1.types.ResourcePath):
            Provides the path to the resource within the
            resource hierarchy.
        resource_path_string (str):
            A string representation of the resource path. For Google
            Cloud, it has the format of
            ``organizations/{organization_id}/folders/{folder_id}/folders/{folder_id}/projects/{project_id}``
            where there can be any number of folders. For AWS, it has
            the format of
            ``org/{organization_id}/ou/{organizational_unit_id}/ou/{organizational_unit_id}/account/{account_id}``
            where there can be any number of organizational units. For
            Azure, it has the format of
            ``mg/{management_group_id}/mg/{management_group_id}/subscription/{subscription_id}/rg/{resource_group_name}``
            where there can be any number of management groups.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    display_name: str = proto.Field(
        proto.STRING,
        number=8,
    )
    type_: str = proto.Field(
        proto.STRING,
        number=6,
    )
    project: str = proto.Field(
        proto.STRING,
        number=2,
    )
    project_display_name: str = proto.Field(
        proto.STRING,
        number=3,
    )
    parent: str = proto.Field(
        proto.STRING,
        number=4,
    )
    parent_display_name: str = proto.Field(
        proto.STRING,
        number=5,
    )
    folders: MutableSequence[folder.Folder] = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message=folder.Folder,
    )
    cloud_provider: "CloudProvider" = proto.Field(
        proto.ENUM,
        number=9,
        enum="CloudProvider",
    )
    organization: str = proto.Field(
        proto.STRING,
        number=10,
    )
    service: str = proto.Field(
        proto.STRING,
        number=11,
    )
    location: str = proto.Field(
        proto.STRING,
        number=12,
    )
    aws_metadata: "AwsMetadata" = proto.Field(
        proto.MESSAGE,
        number=16,
        oneof="cloud_provider_metadata",
        message="AwsMetadata",
    )
    azure_metadata: "AzureMetadata" = proto.Field(
        proto.MESSAGE,
        number=17,
        oneof="cloud_provider_metadata",
        message="AzureMetadata",
    )
    resource_path: "ResourcePath" = proto.Field(
        proto.MESSAGE,
        number=18,
        message="ResourcePath",
    )
    resource_path_string: str = proto.Field(
        proto.STRING,
        number=19,
    )


class AwsMetadata(proto.Message):
    r"""AWS metadata associated with the resource, only applicable if
    the finding's cloud provider is Amazon Web Services.

    Attributes:
        organization (google.cloud.securitycenter_v1.types.AwsMetadata.AwsOrganization):
            The AWS organization associated with the
            resource.
        organizational_units (MutableSequence[google.cloud.securitycenter_v1.types.AwsMetadata.AwsOrganizationalUnit]):
            A list of AWS organizational units associated
            with the resource, ordered from lowest level
            (closest to the account) to highest level.
        account (google.cloud.securitycenter_v1.types.AwsMetadata.AwsAccount):
            The AWS account associated with the resource.
    """

    class AwsOrganization(proto.Message):
        r"""An organization is a collection of accounts that are
        centrally managed together using consolidated billing, organized
        hierarchically with organizational units (OUs), and controlled
        with policies.

        Attributes:
            id (str):
                The unique identifier (ID) for the
                organization. The regex pattern for an
                organization ID string requires "o-" followed by
                from 10 to 32 lowercase letters or digits.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )

    class AwsOrganizationalUnit(proto.Message):
        r"""An Organizational Unit (OU) is a container of AWS accounts
        within a root of an organization. Policies that are attached to
        an OU apply to all accounts contained in that OU and in any
        child OUs.

        Attributes:
            id (str):
                The unique identifier (ID) associated with
                this OU. The regex pattern for an organizational
                unit ID string requires "ou-" followed by from 4
                to 32 lowercase letters or digits (the ID of the
                root that contains the OU). This string is
                followed by a second "-" dash and from 8 to 32
                additional lowercase letters or digits. For
                example, "ou-ab12-cd34ef56".
            name (str):
                The friendly name of the OU.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AwsAccount(proto.Message):
        r"""An AWS account that is a member of an organization.

        Attributes:
            id (str):
                The unique identifier (ID) of the account,
                containing exactly 12 digits.
            name (str):
                The friendly name of this account.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    organization: AwsOrganization = proto.Field(
        proto.MESSAGE,
        number=2,
        message=AwsOrganization,
    )
    organizational_units: MutableSequence[AwsOrganizationalUnit] = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message=AwsOrganizationalUnit,
    )
    account: AwsAccount = proto.Field(
        proto.MESSAGE,
        number=4,
        message=AwsAccount,
    )


class AzureMetadata(proto.Message):
    r"""Azure metadata associated with the resource, only applicable
    if the finding's cloud provider is Microsoft Azure.

    Attributes:
        management_groups (MutableSequence[google.cloud.securitycenter_v1.types.AzureMetadata.AzureManagementGroup]):
            A list of Azure management groups associated
            with the resource, ordered from lowest level
            (closest to the subscription) to highest level.
        subscription (google.cloud.securitycenter_v1.types.AzureMetadata.AzureSubscription):
            The Azure subscription associated with the
            resource.
        resource_group (google.cloud.securitycenter_v1.types.AzureMetadata.AzureResourceGroup):
            The Azure resource group associated with the
            resource.
    """

    class AzureManagementGroup(proto.Message):
        r"""Represents an Azure management group.

        Attributes:
            id (str):
                The UUID of the Azure management group, for example,
                ``20000000-0001-0000-0000-000000000000``.
            display_name (str):
                The display name of the Azure management
                group.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AzureSubscription(proto.Message):
        r"""Represents an Azure subscription.

        Attributes:
            id (str):
                The UUID of the Azure subscription, for example,
                ``291bba3f-e0a5-47bc-a099-3bdcb2a50a05``.
            display_name (str):
                The display name of the Azure subscription.
        """

        id: str = proto.Field(
            proto.STRING,
            number=1,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=2,
        )

    class AzureResourceGroup(proto.Message):
        r"""Represents an Azure resource group.

        Attributes:
            name (str):
                The name of the Azure resource group. This is
                not a UUID.
        """

        name: str = proto.Field(
            proto.STRING,
            number=1,
        )

    management_groups: MutableSequence[AzureManagementGroup] = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message=AzureManagementGroup,
    )
    subscription: AzureSubscription = proto.Field(
        proto.MESSAGE,
        number=5,
        message=AzureSubscription,
    )
    resource_group: AzureResourceGroup = proto.Field(
        proto.MESSAGE,
        number=6,
        message=AzureResourceGroup,
    )


class ResourcePath(proto.Message):
    r"""Represents the path of resources leading up to the resource
    this finding is about.

    Attributes:
        nodes (MutableSequence[google.cloud.securitycenter_v1.types.ResourcePath.ResourcePathNode]):
            The list of nodes that make the up resource
            path, ordered from lowest level to highest
            level.
    """

    class ResourcePathNodeType(proto.Enum):
        r"""The type of resource the node represents.

        Values:
            RESOURCE_PATH_NODE_TYPE_UNSPECIFIED (0):
                Node type is unspecified.
            GCP_ORGANIZATION (1):
                The node represents a Google Cloud
                organization.
            GCP_FOLDER (2):
                The node represents a Google Cloud folder.
            GCP_PROJECT (3):
                The node represents a Google Cloud project.
            AWS_ORGANIZATION (4):
                The node represents an AWS organization.
            AWS_ORGANIZATIONAL_UNIT (5):
                The node represents an AWS organizational
                unit.
            AWS_ACCOUNT (6):
                The node represents an AWS account.
            AZURE_MANAGEMENT_GROUP (7):
                The node represents an Azure management
                group.
            AZURE_SUBSCRIPTION (8):
                The node represents an Azure subscription.
            AZURE_RESOURCE_GROUP (9):
                The node represents an Azure resource group.
        """

        RESOURCE_PATH_NODE_TYPE_UNSPECIFIED = 0
        GCP_ORGANIZATION = 1
        GCP_FOLDER = 2
        GCP_PROJECT = 3
        AWS_ORGANIZATION = 4
        AWS_ORGANIZATIONAL_UNIT = 5
        AWS_ACCOUNT = 6
        AZURE_MANAGEMENT_GROUP = 7
        AZURE_SUBSCRIPTION = 8
        AZURE_RESOURCE_GROUP = 9

    class ResourcePathNode(proto.Message):
        r"""A node within the resource path. Each node represents a
        resource within the resource hierarchy.

        Attributes:
            node_type (google.cloud.securitycenter_v1.types.ResourcePath.ResourcePathNodeType):
                The type of resource this node represents.
            id (str):
                The ID of the resource this node represents.
            display_name (str):
                The display name of the resource this node
                represents.
        """

        node_type: "ResourcePath.ResourcePathNodeType" = proto.Field(
            proto.ENUM,
            number=1,
            enum="ResourcePath.ResourcePathNodeType",
        )
        id: str = proto.Field(
            proto.STRING,
            number=2,
        )
        display_name: str = proto.Field(
            proto.STRING,
            number=3,
        )

    nodes: MutableSequence[ResourcePathNode] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=ResourcePathNode,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
