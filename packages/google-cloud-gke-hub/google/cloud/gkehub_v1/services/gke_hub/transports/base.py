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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.gkehub_v1 import gapic_version as package_version
from google.cloud.gkehub_v1.types import feature, fleet, membership, service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class GkeHubTransport(abc.ABC):
    """Abstract transport class for GkeHub."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "gkehub.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'gkehub.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_memberships: gapic_v1.method.wrap_method(
                self.list_memberships,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_bound_memberships: gapic_v1.method.wrap_method(
                self.list_bound_memberships,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_features: gapic_v1.method.wrap_method(
                self.list_features,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_membership: gapic_v1.method.wrap_method(
                self.get_membership,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_feature: gapic_v1.method.wrap_method(
                self.get_feature,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_membership: gapic_v1.method.wrap_method(
                self.create_membership,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_feature: gapic_v1.method.wrap_method(
                self.create_feature,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_membership: gapic_v1.method.wrap_method(
                self.delete_membership,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_feature: gapic_v1.method.wrap_method(
                self.delete_feature,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_membership: gapic_v1.method.wrap_method(
                self.update_membership,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_feature: gapic_v1.method.wrap_method(
                self.update_feature,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_connect_manifest: gapic_v1.method.wrap_method(
                self.generate_connect_manifest,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_fleet: gapic_v1.method.wrap_method(
                self.create_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_fleet: gapic_v1.method.wrap_method(
                self.get_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_fleet: gapic_v1.method.wrap_method(
                self.update_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_fleet: gapic_v1.method.wrap_method(
                self.delete_fleet,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_fleets: gapic_v1.method.wrap_method(
                self.list_fleets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_scope_namespace: gapic_v1.method.wrap_method(
                self.get_scope_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_scope_namespace: gapic_v1.method.wrap_method(
                self.create_scope_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_scope_namespace: gapic_v1.method.wrap_method(
                self.update_scope_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_scope_namespace: gapic_v1.method.wrap_method(
                self.delete_scope_namespace,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_scope_namespaces: gapic_v1.method.wrap_method(
                self.list_scope_namespaces,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_scope_rbac_role_binding: gapic_v1.method.wrap_method(
                self.get_scope_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_scope_rbac_role_binding: gapic_v1.method.wrap_method(
                self.create_scope_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_scope_rbac_role_binding: gapic_v1.method.wrap_method(
                self.update_scope_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_scope_rbac_role_binding: gapic_v1.method.wrap_method(
                self.delete_scope_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_scope_rbac_role_bindings: gapic_v1.method.wrap_method(
                self.list_scope_rbac_role_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_scope: gapic_v1.method.wrap_method(
                self.get_scope,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_scope: gapic_v1.method.wrap_method(
                self.create_scope,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_scope: gapic_v1.method.wrap_method(
                self.update_scope,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_scope: gapic_v1.method.wrap_method(
                self.delete_scope,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_scopes: gapic_v1.method.wrap_method(
                self.list_scopes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_permitted_scopes: gapic_v1.method.wrap_method(
                self.list_permitted_scopes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_membership_binding: gapic_v1.method.wrap_method(
                self.get_membership_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_membership_binding: gapic_v1.method.wrap_method(
                self.create_membership_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_membership_binding: gapic_v1.method.wrap_method(
                self.update_membership_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_membership_binding: gapic_v1.method.wrap_method(
                self.delete_membership_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_membership_bindings: gapic_v1.method.wrap_method(
                self.list_membership_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_membership_rbac_role_binding: gapic_v1.method.wrap_method(
                self.get_membership_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_membership_rbac_role_binding: gapic_v1.method.wrap_method(
                self.create_membership_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_membership_rbac_role_binding: gapic_v1.method.wrap_method(
                self.update_membership_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_membership_rbac_role_binding: gapic_v1.method.wrap_method(
                self.delete_membership_rbac_role_binding,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_membership_rbac_role_bindings: gapic_v1.method.wrap_method(
                self.list_membership_rbac_role_bindings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_membership_rbac_role_binding_yaml: gapic_v1.method.wrap_method(
                self.generate_membership_rbac_role_binding_yaml,
                default_timeout=None,
                client_info=client_info,
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_memberships(
        self,
    ) -> Callable[
        [service.ListMembershipsRequest],
        Union[
            service.ListMembershipsResponse, Awaitable[service.ListMembershipsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_bound_memberships(
        self,
    ) -> Callable[
        [service.ListBoundMembershipsRequest],
        Union[
            service.ListBoundMembershipsResponse,
            Awaitable[service.ListBoundMembershipsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_features(
        self,
    ) -> Callable[
        [service.ListFeaturesRequest],
        Union[service.ListFeaturesResponse, Awaitable[service.ListFeaturesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_membership(
        self,
    ) -> Callable[
        [service.GetMembershipRequest],
        Union[membership.Membership, Awaitable[membership.Membership]],
    ]:
        raise NotImplementedError()

    @property
    def get_feature(
        self,
    ) -> Callable[
        [service.GetFeatureRequest], Union[feature.Feature, Awaitable[feature.Feature]]
    ]:
        raise NotImplementedError()

    @property
    def create_membership(
        self,
    ) -> Callable[
        [service.CreateMembershipRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_feature(
        self,
    ) -> Callable[
        [service.CreateFeatureRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_membership(
        self,
    ) -> Callable[
        [service.DeleteMembershipRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_feature(
        self,
    ) -> Callable[
        [service.DeleteFeatureRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_membership(
        self,
    ) -> Callable[
        [service.UpdateMembershipRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_feature(
        self,
    ) -> Callable[
        [service.UpdateFeatureRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_connect_manifest(
        self,
    ) -> Callable[
        [service.GenerateConnectManifestRequest],
        Union[
            service.GenerateConnectManifestResponse,
            Awaitable[service.GenerateConnectManifestResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_fleet(
        self,
    ) -> Callable[
        [service.CreateFleetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_fleet(
        self,
    ) -> Callable[
        [service.GetFleetRequest], Union[fleet.Fleet, Awaitable[fleet.Fleet]]
    ]:
        raise NotImplementedError()

    @property
    def update_fleet(
        self,
    ) -> Callable[
        [service.UpdateFleetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_fleet(
        self,
    ) -> Callable[
        [service.DeleteFleetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_fleets(
        self,
    ) -> Callable[
        [service.ListFleetsRequest],
        Union[service.ListFleetsResponse, Awaitable[service.ListFleetsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_scope_namespace(
        self,
    ) -> Callable[
        [service.GetScopeNamespaceRequest],
        Union[fleet.Namespace, Awaitable[fleet.Namespace]],
    ]:
        raise NotImplementedError()

    @property
    def create_scope_namespace(
        self,
    ) -> Callable[
        [service.CreateScopeNamespaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_scope_namespace(
        self,
    ) -> Callable[
        [service.UpdateScopeNamespaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_scope_namespace(
        self,
    ) -> Callable[
        [service.DeleteScopeNamespaceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_scope_namespaces(
        self,
    ) -> Callable[
        [service.ListScopeNamespacesRequest],
        Union[
            service.ListScopeNamespacesResponse,
            Awaitable[service.ListScopeNamespacesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.GetScopeRBACRoleBindingRequest],
        Union[fleet.RBACRoleBinding, Awaitable[fleet.RBACRoleBinding]],
    ]:
        raise NotImplementedError()

    @property
    def create_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.CreateScopeRBACRoleBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.UpdateScopeRBACRoleBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_scope_rbac_role_binding(
        self,
    ) -> Callable[
        [service.DeleteScopeRBACRoleBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_scope_rbac_role_bindings(
        self,
    ) -> Callable[
        [service.ListScopeRBACRoleBindingsRequest],
        Union[
            service.ListScopeRBACRoleBindingsResponse,
            Awaitable[service.ListScopeRBACRoleBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_scope(
        self,
    ) -> Callable[
        [service.GetScopeRequest], Union[fleet.Scope, Awaitable[fleet.Scope]]
    ]:
        raise NotImplementedError()

    @property
    def create_scope(
        self,
    ) -> Callable[
        [service.CreateScopeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_scope(
        self,
    ) -> Callable[
        [service.UpdateScopeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_scope(
        self,
    ) -> Callable[
        [service.DeleteScopeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_scopes(
        self,
    ) -> Callable[
        [service.ListScopesRequest],
        Union[service.ListScopesResponse, Awaitable[service.ListScopesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_permitted_scopes(
        self,
    ) -> Callable[
        [service.ListPermittedScopesRequest],
        Union[
            service.ListPermittedScopesResponse,
            Awaitable[service.ListPermittedScopesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_membership_binding(
        self,
    ) -> Callable[
        [service.GetMembershipBindingRequest],
        Union[fleet.MembershipBinding, Awaitable[fleet.MembershipBinding]],
    ]:
        raise NotImplementedError()

    @property
    def create_membership_binding(
        self,
    ) -> Callable[
        [service.CreateMembershipBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_membership_binding(
        self,
    ) -> Callable[
        [service.UpdateMembershipBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_membership_binding(
        self,
    ) -> Callable[
        [service.DeleteMembershipBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_membership_bindings(
        self,
    ) -> Callable[
        [service.ListMembershipBindingsRequest],
        Union[
            service.ListMembershipBindingsResponse,
            Awaitable[service.ListMembershipBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.GetMembershipRBACRoleBindingRequest],
        Union[fleet.RBACRoleBinding, Awaitable[fleet.RBACRoleBinding]],
    ]:
        raise NotImplementedError()

    @property
    def create_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.CreateMembershipRBACRoleBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.UpdateMembershipRBACRoleBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_membership_rbac_role_binding(
        self,
    ) -> Callable[
        [service.DeleteMembershipRBACRoleBindingRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_membership_rbac_role_bindings(
        self,
    ) -> Callable[
        [service.ListMembershipRBACRoleBindingsRequest],
        Union[
            service.ListMembershipRBACRoleBindingsResponse,
            Awaitable[service.ListMembershipRBACRoleBindingsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def generate_membership_rbac_role_binding_yaml(
        self,
    ) -> Callable[
        [service.GenerateMembershipRBACRoleBindingYAMLRequest],
        Union[
            service.GenerateMembershipRBACRoleBindingYAMLResponse,
            Awaitable[service.GenerateMembershipRBACRoleBindingYAMLResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("GkeHubTransport",)
