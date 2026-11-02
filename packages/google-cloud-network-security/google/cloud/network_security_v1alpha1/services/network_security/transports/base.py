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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.network_security_v1alpha1 import gapic_version as package_version
from google.cloud.network_security_v1alpha1.types import (
    authorization_policy,
    authz_policy,
    backend_authentication_config,
    client_tls_policy,
    gateway_security_policy,
    gateway_security_policy_rule,
    server_tls_policy,
    tls_inspection_policy,
    url_list,
)
from google.cloud.network_security_v1alpha1.types import (
    authorization_policy as gcn_authorization_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    authz_policy as gcn_authz_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    backend_authentication_config as gcn_backend_authentication_config,
)
from google.cloud.network_security_v1alpha1.types import (
    client_tls_policy as gcn_client_tls_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    gateway_security_policy as gcn_gateway_security_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    gateway_security_policy_rule as gcn_gateway_security_policy_rule,
)
from google.cloud.network_security_v1alpha1.types import (
    server_tls_policy as gcn_server_tls_policy,
)
from google.cloud.network_security_v1alpha1.types import (
    tls_inspection_policy as gcn_tls_inspection_policy,
)
from google.cloud.network_security_v1alpha1.types import url_list as gcn_url_list

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class NetworkSecurityTransport(abc.ABC):
    """Abstract transport class for NetworkSecurity."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "networksecurity.googleapis.com"

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
                 The hostname to connect to (default: 'networksecurity.googleapis.com').
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
            self.list_authorization_policies: gapic_v1.method.wrap_method(
                self.list_authorization_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_authorization_policy: gapic_v1.method.wrap_method(
                self.get_authorization_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_authorization_policy: gapic_v1.method.wrap_method(
                self.create_authorization_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_authorization_policy: gapic_v1.method.wrap_method(
                self.update_authorization_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_authorization_policy: gapic_v1.method.wrap_method(
                self.delete_authorization_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_backend_authentication_configs: gapic_v1.method.wrap_method(
                self.list_backend_authentication_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_backend_authentication_config: gapic_v1.method.wrap_method(
                self.get_backend_authentication_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_backend_authentication_config: gapic_v1.method.wrap_method(
                self.create_backend_authentication_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_backend_authentication_config: gapic_v1.method.wrap_method(
                self.update_backend_authentication_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_backend_authentication_config: gapic_v1.method.wrap_method(
                self.delete_backend_authentication_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_server_tls_policies: gapic_v1.method.wrap_method(
                self.list_server_tls_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_server_tls_policy: gapic_v1.method.wrap_method(
                self.get_server_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_server_tls_policy: gapic_v1.method.wrap_method(
                self.create_server_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_server_tls_policy: gapic_v1.method.wrap_method(
                self.update_server_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_server_tls_policy: gapic_v1.method.wrap_method(
                self.delete_server_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_client_tls_policies: gapic_v1.method.wrap_method(
                self.list_client_tls_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_client_tls_policy: gapic_v1.method.wrap_method(
                self.get_client_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_client_tls_policy: gapic_v1.method.wrap_method(
                self.create_client_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_client_tls_policy: gapic_v1.method.wrap_method(
                self.update_client_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_client_tls_policy: gapic_v1.method.wrap_method(
                self.delete_client_tls_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_gateway_security_policies: gapic_v1.method.wrap_method(
                self.list_gateway_security_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_gateway_security_policy: gapic_v1.method.wrap_method(
                self.get_gateway_security_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_gateway_security_policy: gapic_v1.method.wrap_method(
                self.create_gateway_security_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_gateway_security_policy: gapic_v1.method.wrap_method(
                self.update_gateway_security_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_gateway_security_policy: gapic_v1.method.wrap_method(
                self.delete_gateway_security_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_gateway_security_policy_rules: gapic_v1.method.wrap_method(
                self.list_gateway_security_policy_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_gateway_security_policy_rule: gapic_v1.method.wrap_method(
                self.get_gateway_security_policy_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_gateway_security_policy_rule: gapic_v1.method.wrap_method(
                self.create_gateway_security_policy_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_gateway_security_policy_rule: gapic_v1.method.wrap_method(
                self.update_gateway_security_policy_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_gateway_security_policy_rule: gapic_v1.method.wrap_method(
                self.delete_gateway_security_policy_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_url_lists: gapic_v1.method.wrap_method(
                self.list_url_lists,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_url_list: gapic_v1.method.wrap_method(
                self.get_url_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_url_list: gapic_v1.method.wrap_method(
                self.create_url_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_url_list: gapic_v1.method.wrap_method(
                self.update_url_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_url_list: gapic_v1.method.wrap_method(
                self.delete_url_list,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_tls_inspection_policies: gapic_v1.method.wrap_method(
                self.list_tls_inspection_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_tls_inspection_policy: gapic_v1.method.wrap_method(
                self.get_tls_inspection_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_tls_inspection_policy: gapic_v1.method.wrap_method(
                self.create_tls_inspection_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_tls_inspection_policy: gapic_v1.method.wrap_method(
                self.update_tls_inspection_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_tls_inspection_policy: gapic_v1.method.wrap_method(
                self.delete_tls_inspection_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_authz_policies: gapic_v1.method.wrap_method(
                self.list_authz_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_authz_policy: gapic_v1.method.wrap_method(
                self.get_authz_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_authz_policy: gapic_v1.method.wrap_method(
                self.create_authz_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_authz_policy: gapic_v1.method.wrap_method(
                self.update_authz_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_authz_policy: gapic_v1.method.wrap_method(
                self.delete_authz_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy: gapic_v1.method.wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_iam_policy: gapic_v1.method.wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions: gapic_v1.method.wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
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
    def list_authorization_policies(
        self,
    ) -> Callable[
        [authorization_policy.ListAuthorizationPoliciesRequest],
        Union[
            authorization_policy.ListAuthorizationPoliciesResponse,
            Awaitable[authorization_policy.ListAuthorizationPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_authorization_policy(
        self,
    ) -> Callable[
        [authorization_policy.GetAuthorizationPolicyRequest],
        Union[
            authorization_policy.AuthorizationPolicy,
            Awaitable[authorization_policy.AuthorizationPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_authorization_policy(
        self,
    ) -> Callable[
        [gcn_authorization_policy.CreateAuthorizationPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_authorization_policy(
        self,
    ) -> Callable[
        [gcn_authorization_policy.UpdateAuthorizationPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_authorization_policy(
        self,
    ) -> Callable[
        [authorization_policy.DeleteAuthorizationPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backend_authentication_configs(
        self,
    ) -> Callable[
        [backend_authentication_config.ListBackendAuthenticationConfigsRequest],
        Union[
            backend_authentication_config.ListBackendAuthenticationConfigsResponse,
            Awaitable[
                backend_authentication_config.ListBackendAuthenticationConfigsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backend_authentication_config(
        self,
    ) -> Callable[
        [backend_authentication_config.GetBackendAuthenticationConfigRequest],
        Union[
            backend_authentication_config.BackendAuthenticationConfig,
            Awaitable[backend_authentication_config.BackendAuthenticationConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_backend_authentication_config(
        self,
    ) -> Callable[
        [gcn_backend_authentication_config.CreateBackendAuthenticationConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_backend_authentication_config(
        self,
    ) -> Callable[
        [gcn_backend_authentication_config.UpdateBackendAuthenticationConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backend_authentication_config(
        self,
    ) -> Callable[
        [backend_authentication_config.DeleteBackendAuthenticationConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_server_tls_policies(
        self,
    ) -> Callable[
        [server_tls_policy.ListServerTlsPoliciesRequest],
        Union[
            server_tls_policy.ListServerTlsPoliciesResponse,
            Awaitable[server_tls_policy.ListServerTlsPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_server_tls_policy(
        self,
    ) -> Callable[
        [server_tls_policy.GetServerTlsPolicyRequest],
        Union[
            server_tls_policy.ServerTlsPolicy,
            Awaitable[server_tls_policy.ServerTlsPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_server_tls_policy(
        self,
    ) -> Callable[
        [gcn_server_tls_policy.CreateServerTlsPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_server_tls_policy(
        self,
    ) -> Callable[
        [gcn_server_tls_policy.UpdateServerTlsPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_server_tls_policy(
        self,
    ) -> Callable[
        [server_tls_policy.DeleteServerTlsPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_client_tls_policies(
        self,
    ) -> Callable[
        [client_tls_policy.ListClientTlsPoliciesRequest],
        Union[
            client_tls_policy.ListClientTlsPoliciesResponse,
            Awaitable[client_tls_policy.ListClientTlsPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_client_tls_policy(
        self,
    ) -> Callable[
        [client_tls_policy.GetClientTlsPolicyRequest],
        Union[
            client_tls_policy.ClientTlsPolicy,
            Awaitable[client_tls_policy.ClientTlsPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_client_tls_policy(
        self,
    ) -> Callable[
        [gcn_client_tls_policy.CreateClientTlsPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_client_tls_policy(
        self,
    ) -> Callable[
        [gcn_client_tls_policy.UpdateClientTlsPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_client_tls_policy(
        self,
    ) -> Callable[
        [client_tls_policy.DeleteClientTlsPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_gateway_security_policies(
        self,
    ) -> Callable[
        [gateway_security_policy.ListGatewaySecurityPoliciesRequest],
        Union[
            gateway_security_policy.ListGatewaySecurityPoliciesResponse,
            Awaitable[gateway_security_policy.ListGatewaySecurityPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_gateway_security_policy(
        self,
    ) -> Callable[
        [gateway_security_policy.GetGatewaySecurityPolicyRequest],
        Union[
            gateway_security_policy.GatewaySecurityPolicy,
            Awaitable[gateway_security_policy.GatewaySecurityPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_gateway_security_policy(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy.CreateGatewaySecurityPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_gateway_security_policy(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy.UpdateGatewaySecurityPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_gateway_security_policy(
        self,
    ) -> Callable[
        [gateway_security_policy.DeleteGatewaySecurityPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_gateway_security_policy_rules(
        self,
    ) -> Callable[
        [gateway_security_policy_rule.ListGatewaySecurityPolicyRulesRequest],
        Union[
            gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse,
            Awaitable[
                gateway_security_policy_rule.ListGatewaySecurityPolicyRulesResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gateway_security_policy_rule.GetGatewaySecurityPolicyRuleRequest],
        Union[
            gateway_security_policy_rule.GatewaySecurityPolicyRule,
            Awaitable[gateway_security_policy_rule.GatewaySecurityPolicyRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy_rule.CreateGatewaySecurityPolicyRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gcn_gateway_security_policy_rule.UpdateGatewaySecurityPolicyRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_gateway_security_policy_rule(
        self,
    ) -> Callable[
        [gateway_security_policy_rule.DeleteGatewaySecurityPolicyRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_url_lists(
        self,
    ) -> Callable[
        [url_list.ListUrlListsRequest],
        Union[url_list.ListUrlListsResponse, Awaitable[url_list.ListUrlListsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_url_list(
        self,
    ) -> Callable[
        [url_list.GetUrlListRequest],
        Union[url_list.UrlList, Awaitable[url_list.UrlList]],
    ]:
        raise NotImplementedError()

    @property
    def create_url_list(
        self,
    ) -> Callable[
        [gcn_url_list.CreateUrlListRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_url_list(
        self,
    ) -> Callable[
        [gcn_url_list.UpdateUrlListRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_url_list(
        self,
    ) -> Callable[
        [url_list.DeleteUrlListRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_tls_inspection_policies(
        self,
    ) -> Callable[
        [tls_inspection_policy.ListTlsInspectionPoliciesRequest],
        Union[
            tls_inspection_policy.ListTlsInspectionPoliciesResponse,
            Awaitable[tls_inspection_policy.ListTlsInspectionPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_tls_inspection_policy(
        self,
    ) -> Callable[
        [tls_inspection_policy.GetTlsInspectionPolicyRequest],
        Union[
            tls_inspection_policy.TlsInspectionPolicy,
            Awaitable[tls_inspection_policy.TlsInspectionPolicy],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_tls_inspection_policy(
        self,
    ) -> Callable[
        [gcn_tls_inspection_policy.CreateTlsInspectionPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_tls_inspection_policy(
        self,
    ) -> Callable[
        [gcn_tls_inspection_policy.UpdateTlsInspectionPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_tls_inspection_policy(
        self,
    ) -> Callable[
        [tls_inspection_policy.DeleteTlsInspectionPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_authz_policies(
        self,
    ) -> Callable[
        [authz_policy.ListAuthzPoliciesRequest],
        Union[
            authz_policy.ListAuthzPoliciesResponse,
            Awaitable[authz_policy.ListAuthzPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_authz_policy(
        self,
    ) -> Callable[
        [authz_policy.GetAuthzPolicyRequest],
        Union[authz_policy.AuthzPolicy, Awaitable[authz_policy.AuthzPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def create_authz_policy(
        self,
    ) -> Callable[
        [gcn_authz_policy.CreateAuthzPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_authz_policy(
        self,
    ) -> Callable[
        [gcn_authz_policy.UpdateAuthzPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_authz_policy(
        self,
    ) -> Callable[
        [authz_policy.DeleteAuthzPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Union[
            iam_policy_pb2.TestIamPermissionsResponse,
            Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("NetworkSecurityTransport",)
