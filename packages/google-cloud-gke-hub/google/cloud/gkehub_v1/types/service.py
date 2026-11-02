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

from google.cloud.gkehub_v1.types import feature, membership
from google.cloud.gkehub_v1.types import fleet as gcg_fleet

__protobuf__ = proto.module(
    package="google.cloud.gkehub.v1",
    manifest={
        "GetScopeNamespaceRequest",
        "CreateScopeNamespaceRequest",
        "UpdateScopeNamespaceRequest",
        "DeleteScopeNamespaceRequest",
        "ListScopeNamespacesRequest",
        "ListScopeNamespacesResponse",
        "GetScopeRBACRoleBindingRequest",
        "CreateScopeRBACRoleBindingRequest",
        "UpdateScopeRBACRoleBindingRequest",
        "DeleteScopeRBACRoleBindingRequest",
        "ListScopeRBACRoleBindingsRequest",
        "ListScopeRBACRoleBindingsResponse",
        "GetScopeRequest",
        "CreateScopeRequest",
        "UpdateScopeRequest",
        "DeleteScopeRequest",
        "ListScopesRequest",
        "ListScopesResponse",
        "ListPermittedScopesRequest",
        "ListPermittedScopesResponse",
        "GetMembershipBindingRequest",
        "CreateMembershipBindingRequest",
        "UpdateMembershipBindingRequest",
        "DeleteMembershipBindingRequest",
        "ListMembershipBindingsRequest",
        "ListMembershipBindingsResponse",
        "ListMembershipsRequest",
        "GetMembershipRBACRoleBindingRequest",
        "CreateMembershipRBACRoleBindingRequest",
        "UpdateMembershipRBACRoleBindingRequest",
        "DeleteMembershipRBACRoleBindingRequest",
        "ListMembershipRBACRoleBindingsRequest",
        "ListMembershipRBACRoleBindingsResponse",
        "GenerateMembershipRBACRoleBindingYAMLRequest",
        "GenerateMembershipRBACRoleBindingYAMLResponse",
        "ListMembershipsResponse",
        "GetMembershipRequest",
        "ListBoundMembershipsRequest",
        "ListBoundMembershipsResponse",
        "CreateMembershipRequest",
        "DeleteMembershipRequest",
        "UpdateMembershipRequest",
        "GenerateConnectManifestRequest",
        "GenerateConnectManifestResponse",
        "ConnectAgentResource",
        "TypeMeta",
        "ListFeaturesRequest",
        "ListFeaturesResponse",
        "GetFeatureRequest",
        "CreateFeatureRequest",
        "DeleteFeatureRequest",
        "UpdateFeatureRequest",
        "CreateFleetRequest",
        "GetFleetRequest",
        "UpdateFleetRequest",
        "DeleteFleetRequest",
        "ListFleetsRequest",
        "ListFleetsResponse",
        "OperationMetadata",
    },
)


class GetScopeNamespaceRequest(proto.Message):
    r"""Request message for the ``GkeHub.GetNamespace`` method.

    Attributes:
        name (str):
            Required. The Namespace resource name in the format
            ``projects/*/locations/*/scopes/*/namespaces/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateScopeNamespaceRequest(proto.Message):
    r"""Request to create a fleet namespace.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Namespace will be created. Specified in the format
            ``projects/*/locations/*/scopes/*``.
        scope_namespace_id (str):
            Required. Client chosen ID for the Namespace.
            ``namespace_id`` must be a valid RFC 1123 compliant DNS
            label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        scope_namespace (google.cloud.gkehub_v1.types.Namespace):
            Required. The fleet namespace to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope_namespace_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    scope_namespace: gcg_fleet.Namespace = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcg_fleet.Namespace,
    )


class UpdateScopeNamespaceRequest(proto.Message):
    r"""Request to update a fleet namespace.

    Attributes:
        scope_namespace (google.cloud.gkehub_v1.types.Namespace):
            Required. A namespace with fields updated. The 'name' field
            in this namespace is used to identify the resource to
            update. Given 'updated' prefix to follow
            go/proto-best-practices-checkers#keyword_conflict
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The fields to be updated.
    """

    scope_namespace: gcg_fleet.Namespace = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Namespace,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteScopeNamespaceRequest(proto.Message):
    r"""Request to delete a fleet namespace.

    Attributes:
        name (str):
            Required. The Namespace resource name in the format
            ``projects/*/locations/*/scopes/*/namespaces/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListScopeNamespacesRequest(proto.Message):
    r"""Request to list fleet namespaces.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Features will be listed. Specified in the format
            ``projects/*/locations/*/scopes/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListFeatures`` which specifies the position in the list
            from where to continue listing the resources.
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


class ListScopeNamespacesResponse(proto.Message):
    r"""List of fleet namespaces.

    Attributes:
        scope_namespaces (MutableSequence[google.cloud.gkehub_v1.types.Namespace]):
            The list of fleet namespaces
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListNamespaces`` method. The value of an empty string
            means that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    scope_namespaces: MutableSequence[gcg_fleet.Namespace] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Namespace,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetScopeRBACRoleBindingRequest(proto.Message):
    r"""Request message for the ``GkeHub.GetScopeRBACRoleBinding`` method.

    Attributes:
        name (str):
            Required. The RBACRoleBinding resource name in the format
            ``projects/*/locations/*/scopes/*/rbacrolebindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateScopeRBACRoleBindingRequest(proto.Message):
    r"""Request to create a rbacrolebindings.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            RBACRoleBinding will be created. Specified in the format
            ``projects/*/locations/*/scopes/*``.
        rbacrolebinding_id (str):
            Required. Client chosen ID for the RBACRoleBinding.
            ``rbacrolebinding_id`` must be a valid RFC 1123 compliant
            DNS label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        rbacrolebinding (google.cloud.gkehub_v1.types.RBACRoleBinding):
            Required. The rbacrolebindings to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rbacrolebinding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rbacrolebinding: gcg_fleet.RBACRoleBinding = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcg_fleet.RBACRoleBinding,
    )


class UpdateScopeRBACRoleBindingRequest(proto.Message):
    r"""Request to update a scope rbacrolebinding.

    Attributes:
        rbacrolebinding (google.cloud.gkehub_v1.types.RBACRoleBinding):
            Required. A rbacrolebinding with fields
            updated. The 'name' field in this
            rbacrolebinding is used to identify the resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The fields to be updated.
    """

    rbacrolebinding: gcg_fleet.RBACRoleBinding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.RBACRoleBinding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteScopeRBACRoleBindingRequest(proto.Message):
    r"""Request to delete a Scope RBACRoleBinding.

    Attributes:
        name (str):
            Required. The RBACRoleBinding resource name in the format
            ``projects/*/locations/*/scopes/*/rbacrolebindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListScopeRBACRoleBindingsRequest(proto.Message):
    r"""Request to list Scope RBACRoleBindings.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Features will be listed. Specified in the format
            ``projects/*/locations/*/scopes/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListScopeRBACRoleBindings`` which specifies the position
            in the list from where to continue listing the resources.
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


class ListScopeRBACRoleBindingsResponse(proto.Message):
    r"""List of Scope RBACRoleBindings.

    Attributes:
        rbacrolebindings (MutableSequence[google.cloud.gkehub_v1.types.RBACRoleBinding]):
            The list of Scope RBACRoleBindings.
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListScopeRBACRoleBindings`` method. The value of an empty
            string means that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    rbacrolebindings: MutableSequence[gcg_fleet.RBACRoleBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.RBACRoleBinding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetScopeRequest(proto.Message):
    r"""Request message for the ``GkeHub.GetScope`` method.

    Attributes:
        name (str):
            Required. The Scope resource name in the format
            ``projects/*/locations/*/scopes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateScopeRequest(proto.Message):
    r"""Request to create a Scope.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the Scope
            will be created. Specified in the format
            ``projects/*/locations/*``.
        scope_id (str):
            Required. Client chosen ID for the Scope. ``scope_id`` must
            be a ????
        scope (google.cloud.gkehub_v1.types.Scope):
            Required. The Scope to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    scope_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    scope: gcg_fleet.Scope = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcg_fleet.Scope,
    )


class UpdateScopeRequest(proto.Message):
    r"""Request to update a Scope.

    Attributes:
        scope (google.cloud.gkehub_v1.types.Scope):
            Required. A Scope with fields updated. The
            'name' field in this namespace is used to
            identify the resource to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The fields to be updated.
    """

    scope: gcg_fleet.Scope = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Scope,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteScopeRequest(proto.Message):
    r"""Request to delete a Scope.

    Attributes:
        name (str):
            Required. The Scope resource name in the format
            ``projects/*/locations/*/scopes/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListScopesRequest(proto.Message):
    r"""Request to list Scopes.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the Scope
            will be listed. Specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to ``ListScopes``
            which specifies the position in the list from where to
            continue listing the resources.
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


class ListScopesResponse(proto.Message):
    r"""List of Scopes.

    Attributes:
        scopes (MutableSequence[google.cloud.gkehub_v1.types.Scope]):
            The list of Scopes
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListScopes`` method. The value of an empty string means
            that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    scopes: MutableSequence[gcg_fleet.Scope] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Scope,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListPermittedScopesRequest(proto.Message):
    r"""Request to list permitted Scopes.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the Scope
            will be listed. Specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListPermittedScopes`` which specifies the position in the
            list from where to continue listing the resources.
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


class ListPermittedScopesResponse(proto.Message):
    r"""List of permitted Scopes.

    Attributes:
        scopes (MutableSequence[google.cloud.gkehub_v1.types.Scope]):
            The list of permitted Scopes
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListPermittedScopes`` method. The value of an empty string
            means that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    scopes: MutableSequence[gcg_fleet.Scope] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Scope,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetMembershipBindingRequest(proto.Message):
    r"""Request message for the ``GkeHub.GetMembershipBinding`` method.

    Attributes:
        name (str):
            Required. The MembershipBinding resource name in the format
            ``projects/*/locations/*/memberships/*/bindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMembershipBindingRequest(proto.Message):
    r"""Request to create a MembershipBinding.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            MembershipBinding will be created. Specified in the format
            ``projects/*/locations/*/memberships/*``.
        membership_binding (google.cloud.gkehub_v1.types.MembershipBinding):
            Required. The MembershipBinding to create.
        membership_binding_id (str):
            Required. The ID to use for the
            MembershipBinding.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_binding: gcg_fleet.MembershipBinding = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_fleet.MembershipBinding,
    )
    membership_binding_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateMembershipBindingRequest(proto.Message):
    r"""Request to update a MembershipBinding.

    Attributes:
        membership_binding (google.cloud.gkehub_v1.types.MembershipBinding):
            Required. The MembershipBinding object with
            fields updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The fields to be updated.
    """

    membership_binding: gcg_fleet.MembershipBinding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.MembershipBinding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteMembershipBindingRequest(proto.Message):
    r"""Request to delete a Binding.

    Attributes:
        name (str):
            Required. The MembershipBinding resource name in the format
            ``projects/*/locations/*/memberships/*/bindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMembershipBindingsRequest(proto.Message):
    r"""Request to list MembershipBinding.

    Attributes:
        parent (str):
            Required. The parent Membership for which the
            MembershipBindings will be listed. Specified in the format
            ``projects/*/locations/*/memberships/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListMembershipBindings`` which specifies the position in
            the list from where to continue listing the resources.
        filter (str):
            Optional. Lists MembershipBindings that match
            the filter expression, following the syntax
            outlined in https://google.aip.dev/160.
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


class ListMembershipBindingsResponse(proto.Message):
    r"""List of MembershipBindings.

    Attributes:
        membership_bindings (MutableSequence[google.cloud.gkehub_v1.types.MembershipBinding]):
            The list of membership_bindings
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListMembershipBindings`` method. The value of an empty
            string means that there are no more resources to return.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached
            while fetching this list.
    """

    @property
    def raw_page(self):
        return self

    membership_bindings: MutableSequence[gcg_fleet.MembershipBinding] = (
        proto.RepeatedField(
            proto.MESSAGE,
            number=1,
            message=gcg_fleet.MembershipBinding,
        )
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class ListMembershipsRequest(proto.Message):
    r"""Request message for ``GkeHub.ListMemberships`` method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be listed. Specified in the format
            ``projects/*/locations/*``. ``projects/*/locations/-`` list
            memberships in all the regions.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListMemberships`` which specifies the position in the list
            from where to continue listing the resources.
        filter (str):
            Optional. Lists Memberships that match the filter
            expression, following the syntax outlined in
            https://google.aip.dev/160.

            Examples:

            - Name is ``bar`` in project ``foo-proj`` and location
              ``global``:

              name = "projects/foo-proj/locations/global/membership/bar"

            - Memberships that have a label called ``foo``:

              labels.foo:\*

            - Memberships that have a label called ``foo`` whose value
              is ``bar``:

              labels.foo = bar

            - Memberships in the CREATING state:

              state = CREATING
        order_by (str):
            Optional. One or more fields to compare and
            use to sort the output. See
            https://google.aip.dev/132#ordering.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )


class GetMembershipRBACRoleBindingRequest(proto.Message):
    r"""Request message for the ``GkeHub.GetMembershipRBACRoleBinding``
    method.

    Attributes:
        name (str):
            Required. The RBACRoleBinding resource name in the format
            ``projects/*/locations/*/memberships/*/rbacrolebindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMembershipRBACRoleBindingRequest(proto.Message):
    r"""Request to create a rbacrolebindings.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            RBACRoleBinding will be created. Specified in the format
            ``projects/*/locations/*/memberships/*``.
        rbacrolebinding_id (str):
            Required. Client chosen ID for the RBACRoleBinding.
            ``rbacrolebinding_id`` must be a valid RFC 1123 compliant
            DNS label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        rbacrolebinding (google.cloud.gkehub_v1.types.RBACRoleBinding):
            Required. The rbacrolebindings to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rbacrolebinding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rbacrolebinding: gcg_fleet.RBACRoleBinding = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcg_fleet.RBACRoleBinding,
    )


class UpdateMembershipRBACRoleBindingRequest(proto.Message):
    r"""Request to update a membership rbacrolebinding.

    Attributes:
        rbacrolebinding (google.cloud.gkehub_v1.types.RBACRoleBinding):
            Required. A rbacrolebinding with fields
            updated. The 'name' field in this
            rbacrolebinding is used to identify the resource
            to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The fields to be updated.
    """

    rbacrolebinding: gcg_fleet.RBACRoleBinding = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.RBACRoleBinding,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteMembershipRBACRoleBindingRequest(proto.Message):
    r"""Request to delete a Membership RBACRoleBinding.

    Attributes:
        name (str):
            Required. The RBACRoleBinding resource name in the format
            ``projects/*/locations/*/memberships/*/rbacrolebindings/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMembershipRBACRoleBindingsRequest(proto.Message):
    r"""Request to list Membership RBACRoleBindings.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Features will be listed. Specified in the format
            ``projects/*/locations/*/memberships/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListMembershipRBACRoleBindings`` which specifies the
            position in the list from where to continue listing the
            resources.
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


class ListMembershipRBACRoleBindingsResponse(proto.Message):
    r"""List of Membership RBACRoleBindings.

    Attributes:
        rbacrolebindings (MutableSequence[google.cloud.gkehub_v1.types.RBACRoleBinding]):
            The list of Membership RBACRoleBindings.
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListMembershipRBACRoleBindings`` method. The value of an
            empty string means that there are no more resources to
            return.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached
            while fetching this list.
    """

    @property
    def raw_page(self):
        return self

    rbacrolebindings: MutableSequence[gcg_fleet.RBACRoleBinding] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.RBACRoleBinding,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GenerateMembershipRBACRoleBindingYAMLRequest(proto.Message):
    r"""Request to generate a YAML of the RBAC policies for the
    specified RoleBinding and its associated impersonation
    resources.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            RBACRoleBinding will be created. Specified in the format
            ``projects/*/locations/*/memberships/*``.
        rbacrolebinding_id (str):
            Required. Client chosen ID for the RBACRoleBinding.
            ``rbacrolebinding_id`` must be a valid RFC 1123 compliant
            DNS label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        rbacrolebinding (google.cloud.gkehub_v1.types.RBACRoleBinding):
            Required. The rbacrolebindings to generate
            the YAML for.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    rbacrolebinding_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    rbacrolebinding: gcg_fleet.RBACRoleBinding = proto.Field(
        proto.MESSAGE,
        number=3,
        message=gcg_fleet.RBACRoleBinding,
    )


class GenerateMembershipRBACRoleBindingYAMLResponse(proto.Message):
    r"""Response for GenerateRBACRoleBindingYAML.

    Attributes:
        role_bindings_yaml (str):
            a yaml text blob including the RBAC policies.
    """

    role_bindings_yaml: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListMembershipsResponse(proto.Message):
    r"""Response message for the ``GkeHub.ListMemberships`` method.

    Attributes:
        resources (MutableSequence[google.cloud.gkehub_v1.types.Membership]):
            The list of matching Memberships.
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListMemberships`` method. The value of an empty string
            means that there are no more resources to return.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached
            while fetching this list.
    """

    @property
    def raw_page(self):
        return self

    resources: MutableSequence[membership.Membership] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=membership.Membership,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMembershipRequest(proto.Message):
    r"""Request message for ``GkeHub.GetMembership`` method.

    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListBoundMembershipsRequest(proto.Message):
    r"""Request to list Memberships bound to a Scope.

    Attributes:
        scope_name (str):
            Required. Name of the Scope, in the format
            ``projects/*/locations/global/scopes/*``, to which the
            Memberships are bound.
        filter (str):
            Optional. Lists Memberships that match the filter
            expression, following the syntax outlined in
            https://google.aip.dev/160. Currently, filtering can be done
            only based on Memberships's ``name``, ``labels``,
            ``create_time``, ``update_time``, and ``unique_id``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
            Pagination is currently not supported; therefore, setting
            this field does not have any impact for now.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListBoundMemberships`` which specifies the position in the
            list from where to continue listing the resources.
    """

    scope_name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    filter: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=4,
    )


class ListBoundMembershipsResponse(proto.Message):
    r"""List of Memberships bound to a Scope.

    Attributes:
        memberships (MutableSequence[google.cloud.gkehub_v1.types.Membership]):
            The list of Memberships bound to the given
            Scope.
        unreachable (MutableSequence[str]):
            List of locations that could not be reached
            while fetching this list.
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListBoundMemberships`` method. The value of an empty
            string means that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    memberships: MutableSequence[membership.Membership] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=membership.Membership,
    )
    unreachable: MutableSequence[str] = proto.RepeatedField(
        proto.STRING,
        number=2,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=3,
    )


class CreateMembershipRequest(proto.Message):
    r"""Request message for the ``GkeHub.CreateMembership`` method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be created. Specified in the format
            ``projects/*/locations/*``.
        membership_id (str):
            Required. Client chosen ID for the membership.
            ``membership_id`` must be a valid RFC 1123 compliant DNS
            label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        resource (google.cloud.gkehub_v1.types.Membership):
            Required. The membership to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource: membership.Membership = proto.Field(
        proto.MESSAGE,
        number=3,
        message=membership.Membership,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteMembershipRequest(proto.Message):
    r"""Request message for ``GkeHub.DeleteMembership`` method.

    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
        force (bool):
            Optional. If set to true, any subresource
            from this Membership will also be deleted.
            Otherwise, the request will only work if the
            Membership has no subresource.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=3,
    )


class UpdateMembershipRequest(proto.Message):
    r"""Request message for ``GkeHub.UpdateMembership`` method.

    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        resource (google.cloud.gkehub_v1.types.Membership):
            Required. Only fields specified in update_mask are updated.
            If you specify a field in the update_mask but don't specify
            its value here that field will be deleted. If you are
            updating a map field, set the value of a key to null or
            empty string to delete the key from the map. It's not
            possible to update a key's value to the empty string. If you
            specify the update_mask to be a special path "\*", fully
            replaces all user-modifiable fields to match ``resource``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    resource: membership.Membership = proto.Field(
        proto.MESSAGE,
        number=3,
        message=membership.Membership,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class GenerateConnectManifestRequest(proto.Message):
    r"""Request message for ``GkeHub.GenerateConnectManifest`` method. .

    Attributes:
        name (str):
            Required. The Membership resource name the Agent will
            associate with, in the format
            ``projects/*/locations/*/memberships/*``.
        namespace (str):
            Optional. Namespace for GKE Connect agent resources.
            Defaults to ``gke-connect``.

            The Connect Agent is authorized automatically when run in
            the default namespace. Otherwise, explicit authorization
            must be granted with an additional IAM binding.
        proxy (bytes):
            Optional. URI of a proxy if connectivity from the agent to
            gkeconnect.googleapis.com requires the use of a proxy.
            Format must be in the form ``http(s)://{proxy_address}``,
            depending on the HTTP/HTTPS protocol supported by the proxy.
            This will direct the connect agent's outbound traffic
            through a HTTP(S) proxy.
        version (str):
            Optional. The Connect agent version to use.
            Defaults to the most current version.
        is_upgrade (bool):
            Optional. If true, generate the resources for
            upgrade only. Some resources generated only for
            installation (e.g. secrets) will be excluded.
        registry (str):
            Optional. The registry to fetch the connect
            agent image from. Defaults to gcr.io/gkeconnect.
        image_pull_secret_content (bytes):
            Optional. The image pull secret content for
            the registry, if not public.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    namespace: str = proto.Field(
        proto.STRING,
        number=2,
    )
    proxy: bytes = proto.Field(
        proto.BYTES,
        number=3,
    )
    version: str = proto.Field(
        proto.STRING,
        number=4,
    )
    is_upgrade: bool = proto.Field(
        proto.BOOL,
        number=5,
    )
    registry: str = proto.Field(
        proto.STRING,
        number=6,
    )
    image_pull_secret_content: bytes = proto.Field(
        proto.BYTES,
        number=7,
    )


class GenerateConnectManifestResponse(proto.Message):
    r"""GenerateConnectManifestResponse contains manifest information
    for installing/upgrading a Connect agent.

    Attributes:
        manifest (MutableSequence[google.cloud.gkehub_v1.types.ConnectAgentResource]):
            The ordered list of Kubernetes resources that
            need to be applied to the cluster for GKE
            Connect agent installation/upgrade.
    """

    manifest: MutableSequence["ConnectAgentResource"] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ConnectAgentResource",
    )


class ConnectAgentResource(proto.Message):
    r"""ConnectAgentResource represents a Kubernetes resource
    manifest for Connect Agent deployment.

    Attributes:
        type_ (google.cloud.gkehub_v1.types.TypeMeta):
            Kubernetes type of the resource.
        manifest (str):
            YAML manifest of the resource.
    """

    type_: "TypeMeta" = proto.Field(
        proto.MESSAGE,
        number=1,
        message="TypeMeta",
    )
    manifest: str = proto.Field(
        proto.STRING,
        number=2,
    )


class TypeMeta(proto.Message):
    r"""TypeMeta is the type information needed for content
    unmarshalling of Kubernetes resources in the manifest.

    Attributes:
        kind (str):
            Kind of the resource (e.g. Deployment).
        api_version (str):
            APIVersion of the resource (e.g. v1).
    """

    kind: str = proto.Field(
        proto.STRING,
        number=1,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=2,
    )


class ListFeaturesRequest(proto.Message):
    r"""Request message for ``GkeHub.ListFeatures`` method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Features will be listed. Specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            When requesting a 'page' of resources, ``page_size``
            specifies number of resources to return. If unspecified or
            set to 0, all resources will be returned.
        page_token (str):
            Token returned by previous call to ``ListFeatures`` which
            specifies the position in the list from where to continue
            listing the resources.
        filter (str):
            Lists Features that match the filter expression, following
            the syntax outlined in https://google.aip.dev/160.

            Examples:

            - Feature with the name "servicemesh" in project "foo-proj":

              name =
              "projects/foo-proj/locations/global/features/servicemesh"

            - Features that have a label called ``foo``:

              labels.foo:\*

            - Features that have a label called ``foo`` whose value is
              ``bar``:

              labels.foo = bar
        order_by (str):
            One or more fields to compare and use to sort
            the output. See
            https://google.aip.dev/132#ordering.
        return_partial_success (bool):
            Optional. If set to true, the response will
            return partial results when some regions are
            unreachable and the unreachable field in Feature
            proto will be populated. If set to false, the
            request will fail when some regions are
            unreachable.
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
    order_by: str = proto.Field(
        proto.STRING,
        number=5,
    )
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=6,
    )


class ListFeaturesResponse(proto.Message):
    r"""Response message for the ``GkeHub.ListFeatures`` method.

    Attributes:
        resources (MutableSequence[google.cloud.gkehub_v1.types.Feature]):
            The list of matching Features
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListFeatures`` method. The value of an empty string means
            that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    resources: MutableSequence[feature.Feature] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=feature.Feature,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFeatureRequest(proto.Message):
    r"""Request message for ``GkeHub.GetFeature`` method.

    Attributes:
        name (str):
            Required. The Feature resource name in the format
            ``projects/*/locations/*/features/*``
        return_partial_success (bool):
            Optional. If set to true, the response will
            return partial results when some regions are
            unreachable and the unreachable field in Feature
            proto will be populated. If set to false, the
            request will fail when some regions are
            unreachable.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    return_partial_success: bool = proto.Field(
        proto.BOOL,
        number=2,
    )


class CreateFeatureRequest(proto.Message):
    r"""Request message for the ``GkeHub.CreateFeature`` method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Feature will be created. Specified in the format
            ``projects/*/locations/*``.
        feature_id (str):
            The ID of the feature to create.
        resource (google.cloud.gkehub_v1.types.Feature):
            The Feature resource to create.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    feature_id: str = proto.Field(
        proto.STRING,
        number=2,
    )
    resource: feature.Feature = proto.Field(
        proto.MESSAGE,
        number=3,
        message=feature.Feature,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteFeatureRequest(proto.Message):
    r"""Request message for ``GkeHub.DeleteFeature`` method.

    Attributes:
        name (str):
            Required. The Feature resource name in the format
            ``projects/*/locations/*/features/*``.
        force (bool):
            If set to true, the delete will ignore any outstanding
            resources for this Feature (that is,
            ``FeatureState.has_resources`` is set to true). These
            resources will NOT be cleaned up or modified in any way.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    force: bool = proto.Field(
        proto.BOOL,
        number=2,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateFeatureRequest(proto.Message):
    r"""Request message for ``GkeHub.UpdateFeature`` method.

    Attributes:
        name (str):
            Required. The Feature resource name in the format
            ``projects/*/locations/*/features/*``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask of fields to update.
        resource (google.cloud.gkehub_v1.types.Feature):
            Only fields specified in update_mask are updated. If you
            specify a field in the update_mask but don't specify its
            value here that field will be deleted. If you are updating a
            map field, set the value of a key to null or empty string to
            delete the key from the map. It's not possible to update a
            key's value to the empty string. If you specify the
            update_mask to be a special path "\*", fully replaces all
            user-modifiable fields to match ``resource``.
        request_id (str):
            A request ID to identify requests. Specify a
            unique request ID so that if you must retry your
            request, the server will know to ignore the
            request if it has already been completed. The
            server will guarantee that for at least 60
            minutes after the first request.

            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.

            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    resource: feature.Feature = proto.Field(
        proto.MESSAGE,
        number=3,
        message=feature.Feature,
    )
    request_id: str = proto.Field(
        proto.STRING,
        number=4,
    )


class CreateFleetRequest(proto.Message):
    r"""Request message for the ``GkeHub.CreateFleet`` method.

    Attributes:
        parent (str):
            Required. The parent (project and location) where the Fleet
            will be created. Specified in the format
            ``projects/*/locations/*``.
        fleet (google.cloud.gkehub_v1.types.Fleet):
            Required. The fleet to create.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    fleet: gcg_fleet.Fleet = proto.Field(
        proto.MESSAGE,
        number=2,
        message=gcg_fleet.Fleet,
    )


class GetFleetRequest(proto.Message):
    r"""Request message for the ``GkeHub.GetFleet`` method.

    Attributes:
        name (str):
            Required. The Fleet resource name in the format
            ``projects/*/locations/*/fleets/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateFleetRequest(proto.Message):
    r"""Request message for the ``GkeHub.UpdateFleet`` method.

    Attributes:
        fleet (google.cloud.gkehub_v1.types.Fleet):
            Required. The Fleet to update.

            The ``name`` field of the Fleet object identifies which
            fleet will be updated.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The fields to be updated;
    """

    fleet: gcg_fleet.Fleet = proto.Field(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Fleet,
    )
    update_mask: field_mask_pb2.FieldMask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class DeleteFleetRequest(proto.Message):
    r"""Request message for ``GkeHub.DeleteFleet`` method.

    Attributes:
        name (str):
            Required. The Fleet resource name in the format
            ``projects/*/locations/*/fleets/*``.
    """

    name: str = proto.Field(
        proto.STRING,
        number=1,
    )


class ListFleetsRequest(proto.Message):
    r"""Request message for the ``GkeHub.ListFleets`` method.

    Attributes:
        parent (str):
            Required. The organization or project to list for Fleets
            under, in the format ``organizations/*/locations/*`` or
            ``projects/*/locations/*``.
        page_token (str):
            Optional. A page token, received from a previous
            ``ListFleets`` call. Provide this to retrieve the subsequent
            page.

            When paginating, all other parameters provided to
            ``ListFleets`` must match the call that provided the page
            token.
        page_size (int):
            Optional. The maximum number of fleets to
            return. The service may return fewer than this
            value. If unspecified, at most 200 fleets will
            be returned. The maximum value is 1000; values
            above 1000 will be coerced to 1000.
    """

    parent: str = proto.Field(
        proto.STRING,
        number=1,
    )
    page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )
    page_size: int = proto.Field(
        proto.INT32,
        number=3,
    )


class ListFleetsResponse(proto.Message):
    r"""Response message for the ``GkeHub.ListFleetsResponse`` method.

    Attributes:
        fleets (MutableSequence[google.cloud.gkehub_v1.types.Fleet]):
            The list of matching fleets.
        next_page_token (str):
            A token, which can be sent as ``page_token`` to retrieve the
            next page. If this field is omitted, there are no subsequent
            pages. The token is only valid for 1h.
    """

    @property
    def raw_page(self):
        return self

    fleets: MutableSequence[gcg_fleet.Fleet] = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=gcg_fleet.Fleet,
    )
    next_page_token: str = proto.Field(
        proto.STRING,
        number=2,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.

    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_detail (str):
            Output only. Human-readable status of the
            operation, if any.
        cancel_requested (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have
            [google.longrunning.Operation.error][google.longrunning.Operation.error]
            value with a
            [google.rpc.Status.code][google.rpc.Status.code] of 1,
            corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time: timestamp_pb2.Timestamp = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target: str = proto.Field(
        proto.STRING,
        number=3,
    )
    verb: str = proto.Field(
        proto.STRING,
        number=4,
    )
    status_detail: str = proto.Field(
        proto.STRING,
        number=5,
    )
    cancel_requested: bool = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version: str = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
