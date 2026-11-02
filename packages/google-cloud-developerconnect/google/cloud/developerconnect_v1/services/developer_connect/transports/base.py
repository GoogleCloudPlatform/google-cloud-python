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
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.developerconnect_v1 import gapic_version as package_version
from google.cloud.developerconnect_v1.types import developer_connect

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DeveloperConnectTransport(abc.ABC):
    """Abstract transport class for DeveloperConnect."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "developerconnect.googleapis.com"

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
                 The hostname to connect to (default: 'developerconnect.googleapis.com').
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
            self.list_connections: gapic_v1.method.wrap_method(
                self.list_connections,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_connection: gapic_v1.method.wrap_method(
                self.get_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_connection: gapic_v1.method.wrap_method(
                self.create_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_connection: gapic_v1.method.wrap_method(
                self.update_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_connection: gapic_v1.method.wrap_method(
                self.delete_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_git_repository_link: gapic_v1.method.wrap_method(
                self.create_git_repository_link,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_git_repository_link: gapic_v1.method.wrap_method(
                self.delete_git_repository_link,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_git_repository_links: gapic_v1.method.wrap_method(
                self.list_git_repository_links,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_git_repository_link: gapic_v1.method.wrap_method(
                self.get_git_repository_link,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_read_write_token: gapic_v1.method.wrap_method(
                self.fetch_read_write_token,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_read_token: gapic_v1.method.wrap_method(
                self.fetch_read_token,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_linkable_git_repositories: gapic_v1.method.wrap_method(
                self.fetch_linkable_git_repositories,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_git_hub_installations: gapic_v1.method.wrap_method(
                self.fetch_git_hub_installations,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=10.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_git_refs: gapic_v1.method.wrap_method(
                self.fetch_git_refs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_account_connectors: gapic_v1.method.wrap_method(
                self.list_account_connectors,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_account_connector: gapic_v1.method.wrap_method(
                self.get_account_connector,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_account_connector: gapic_v1.method.wrap_method(
                self.create_account_connector,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_account_connector: gapic_v1.method.wrap_method(
                self.update_account_connector,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_account_connector: gapic_v1.method.wrap_method(
                self.delete_account_connector,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_access_token: gapic_v1.method.wrap_method(
                self.fetch_access_token,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_users: gapic_v1.method.wrap_method(
                self.list_users,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_user: gapic_v1.method.wrap_method(
                self.delete_user,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_self: gapic_v1.method.wrap_method(
                self.fetch_self,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_self: gapic_v1.method.wrap_method(
                self.delete_self,
                default_timeout=None,
                client_info=client_info,
            ),
            self.start_o_auth: gapic_v1.method.wrap_method(
                self.start_o_auth,
                default_timeout=None,
                client_info=client_info,
            ),
            self.finish_o_auth: gapic_v1.method.wrap_method(
                self.finish_o_auth,
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
    def list_connections(
        self,
    ) -> Callable[
        [developer_connect.ListConnectionsRequest],
        Union[
            developer_connect.ListConnectionsResponse,
            Awaitable[developer_connect.ListConnectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_connection(
        self,
    ) -> Callable[
        [developer_connect.GetConnectionRequest],
        Union[developer_connect.Connection, Awaitable[developer_connect.Connection]],
    ]:
        raise NotImplementedError()

    @property
    def create_connection(
        self,
    ) -> Callable[
        [developer_connect.CreateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_connection(
        self,
    ) -> Callable[
        [developer_connect.UpdateConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_connection(
        self,
    ) -> Callable[
        [developer_connect.DeleteConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_git_repository_link(
        self,
    ) -> Callable[
        [developer_connect.CreateGitRepositoryLinkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_git_repository_link(
        self,
    ) -> Callable[
        [developer_connect.DeleteGitRepositoryLinkRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_git_repository_links(
        self,
    ) -> Callable[
        [developer_connect.ListGitRepositoryLinksRequest],
        Union[
            developer_connect.ListGitRepositoryLinksResponse,
            Awaitable[developer_connect.ListGitRepositoryLinksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_git_repository_link(
        self,
    ) -> Callable[
        [developer_connect.GetGitRepositoryLinkRequest],
        Union[
            developer_connect.GitRepositoryLink,
            Awaitable[developer_connect.GitRepositoryLink],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_read_write_token(
        self,
    ) -> Callable[
        [developer_connect.FetchReadWriteTokenRequest],
        Union[
            developer_connect.FetchReadWriteTokenResponse,
            Awaitable[developer_connect.FetchReadWriteTokenResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_read_token(
        self,
    ) -> Callable[
        [developer_connect.FetchReadTokenRequest],
        Union[
            developer_connect.FetchReadTokenResponse,
            Awaitable[developer_connect.FetchReadTokenResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_linkable_git_repositories(
        self,
    ) -> Callable[
        [developer_connect.FetchLinkableGitRepositoriesRequest],
        Union[
            developer_connect.FetchLinkableGitRepositoriesResponse,
            Awaitable[developer_connect.FetchLinkableGitRepositoriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_git_hub_installations(
        self,
    ) -> Callable[
        [developer_connect.FetchGitHubInstallationsRequest],
        Union[
            developer_connect.FetchGitHubInstallationsResponse,
            Awaitable[developer_connect.FetchGitHubInstallationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_git_refs(
        self,
    ) -> Callable[
        [developer_connect.FetchGitRefsRequest],
        Union[
            developer_connect.FetchGitRefsResponse,
            Awaitable[developer_connect.FetchGitRefsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_account_connectors(
        self,
    ) -> Callable[
        [developer_connect.ListAccountConnectorsRequest],
        Union[
            developer_connect.ListAccountConnectorsResponse,
            Awaitable[developer_connect.ListAccountConnectorsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_account_connector(
        self,
    ) -> Callable[
        [developer_connect.GetAccountConnectorRequest],
        Union[
            developer_connect.AccountConnector,
            Awaitable[developer_connect.AccountConnector],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_account_connector(
        self,
    ) -> Callable[
        [developer_connect.CreateAccountConnectorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_account_connector(
        self,
    ) -> Callable[
        [developer_connect.UpdateAccountConnectorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_account_connector(
        self,
    ) -> Callable[
        [developer_connect.DeleteAccountConnectorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_access_token(
        self,
    ) -> Callable[
        [developer_connect.FetchAccessTokenRequest],
        Union[
            developer_connect.FetchAccessTokenResponse,
            Awaitable[developer_connect.FetchAccessTokenResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_users(
        self,
    ) -> Callable[
        [developer_connect.ListUsersRequest],
        Union[
            developer_connect.ListUsersResponse,
            Awaitable[developer_connect.ListUsersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_user(
        self,
    ) -> Callable[
        [developer_connect.DeleteUserRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_self(
        self,
    ) -> Callable[
        [developer_connect.FetchSelfRequest],
        Union[developer_connect.User, Awaitable[developer_connect.User]],
    ]:
        raise NotImplementedError()

    @property
    def delete_self(
        self,
    ) -> Callable[
        [developer_connect.DeleteSelfRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def start_o_auth(
        self,
    ) -> Callable[
        [developer_connect.StartOAuthRequest],
        Union[
            developer_connect.StartOAuthResponse,
            Awaitable[developer_connect.StartOAuthResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def finish_o_auth(
        self,
    ) -> Callable[
        [developer_connect.FinishOAuthRequest],
        Union[
            developer_connect.FinishOAuthResponse,
            Awaitable[developer_connect.FinishOAuthResponse],
        ],
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


__all__ = ("DeveloperConnectTransport",)
