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
import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
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

from google.cloud.securesourcemanager_v1 import gapic_version as package_version
from google.cloud.securesourcemanager_v1.types import secure_source_manager

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class SecureSourceManagerTransport(abc.ABC):
    """Abstract transport class for SecureSourceManager."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/securesourcemanager.read-write",
    )

    DEFAULT_HOST: str = "securesourcemanager.googleapis.com"

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
                 The hostname to connect to (default: 'securesourcemanager.googleapis.com').
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
            self.list_instances: gapic_v1.method.wrap_method(
                self.list_instances,
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
            self.get_instance: gapic_v1.method.wrap_method(
                self.get_instance,
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
            self.create_instance: gapic_v1.method.wrap_method(
                self.create_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_instance: gapic_v1.method.wrap_method(
                self.delete_instance,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_repositories: gapic_v1.method.wrap_method(
                self.list_repositories,
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
            self.get_repository: gapic_v1.method.wrap_method(
                self.get_repository,
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
            self.create_repository: gapic_v1.method.wrap_method(
                self.create_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_repository: gapic_v1.method.wrap_method(
                self.update_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_repository: gapic_v1.method.wrap_method(
                self.delete_repository,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_hooks: gapic_v1.method.wrap_method(
                self.list_hooks,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_hook: gapic_v1.method.wrap_method(
                self.get_hook,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_hook: gapic_v1.method.wrap_method(
                self.create_hook,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_hook: gapic_v1.method.wrap_method(
                self.update_hook,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_hook: gapic_v1.method.wrap_method(
                self.delete_hook,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_iam_policy_repo: gapic_v1.method.wrap_method(
                self.get_iam_policy_repo,
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
            self.set_iam_policy_repo: gapic_v1.method.wrap_method(
                self.set_iam_policy_repo,
                default_timeout=None,
                client_info=client_info,
            ),
            self.test_iam_permissions_repo: gapic_v1.method.wrap_method(
                self.test_iam_permissions_repo,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_branch_rule: gapic_v1.method.wrap_method(
                self.create_branch_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_branch_rules: gapic_v1.method.wrap_method(
                self.list_branch_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_branch_rule: gapic_v1.method.wrap_method(
                self.get_branch_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_branch_rule: gapic_v1.method.wrap_method(
                self.update_branch_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_branch_rule: gapic_v1.method.wrap_method(
                self.delete_branch_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_pull_request: gapic_v1.method.wrap_method(
                self.create_pull_request,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_pull_request: gapic_v1.method.wrap_method(
                self.get_pull_request,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_pull_requests: gapic_v1.method.wrap_method(
                self.list_pull_requests,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_pull_request: gapic_v1.method.wrap_method(
                self.update_pull_request,
                default_timeout=None,
                client_info=client_info,
            ),
            self.merge_pull_request: gapic_v1.method.wrap_method(
                self.merge_pull_request,
                default_timeout=None,
                client_info=client_info,
            ),
            self.open_pull_request: gapic_v1.method.wrap_method(
                self.open_pull_request,
                default_timeout=None,
                client_info=client_info,
            ),
            self.close_pull_request: gapic_v1.method.wrap_method(
                self.close_pull_request,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_pull_request_file_diffs: gapic_v1.method.wrap_method(
                self.list_pull_request_file_diffs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_tree: gapic_v1.method.wrap_method(
                self.fetch_tree,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_blob: gapic_v1.method.wrap_method(
                self.fetch_blob,
                default_timeout=None,
                client_info=client_info,
            ),
            self.fetch_refs: gapic_v1.method.wrap_method(
                self.fetch_refs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_issue: gapic_v1.method.wrap_method(
                self.create_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_issue: gapic_v1.method.wrap_method(
                self.get_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_issues: gapic_v1.method.wrap_method(
                self.list_issues,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_issue: gapic_v1.method.wrap_method(
                self.update_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_issue: gapic_v1.method.wrap_method(
                self.delete_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.open_issue: gapic_v1.method.wrap_method(
                self.open_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.close_issue: gapic_v1.method.wrap_method(
                self.close_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_pull_request_comment: gapic_v1.method.wrap_method(
                self.get_pull_request_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_pull_request_comments: gapic_v1.method.wrap_method(
                self.list_pull_request_comments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_pull_request_comment: gapic_v1.method.wrap_method(
                self.create_pull_request_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_pull_request_comment: gapic_v1.method.wrap_method(
                self.update_pull_request_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_pull_request_comment: gapic_v1.method.wrap_method(
                self.delete_pull_request_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.batch_create_pull_request_comments: gapic_v1.method.wrap_method(
                self.batch_create_pull_request_comments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.resolve_pull_request_comments: gapic_v1.method.wrap_method(
                self.resolve_pull_request_comments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.unresolve_pull_request_comments: gapic_v1.method.wrap_method(
                self.unresolve_pull_request_comments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_issue_comment: gapic_v1.method.wrap_method(
                self.create_issue_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_issue_comment: gapic_v1.method.wrap_method(
                self.get_issue_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_issue_comments: gapic_v1.method.wrap_method(
                self.list_issue_comments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_issue_comment: gapic_v1.method.wrap_method(
                self.update_issue_comment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_issue_comment: gapic_v1.method.wrap_method(
                self.delete_issue_comment,
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
    def list_instances(
        self,
    ) -> Callable[
        [secure_source_manager.ListInstancesRequest],
        Union[
            secure_source_manager.ListInstancesResponse,
            Awaitable[secure_source_manager.ListInstancesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_instance(
        self,
    ) -> Callable[
        [secure_source_manager.GetInstanceRequest],
        Union[
            secure_source_manager.Instance, Awaitable[secure_source_manager.Instance]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_instance(
        self,
    ) -> Callable[
        [secure_source_manager.CreateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_instance(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_repositories(
        self,
    ) -> Callable[
        [secure_source_manager.ListRepositoriesRequest],
        Union[
            secure_source_manager.ListRepositoriesResponse,
            Awaitable[secure_source_manager.ListRepositoriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_repository(
        self,
    ) -> Callable[
        [secure_source_manager.GetRepositoryRequest],
        Union[
            secure_source_manager.Repository,
            Awaitable[secure_source_manager.Repository],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_repository(
        self,
    ) -> Callable[
        [secure_source_manager.CreateRepositoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_repository(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateRepositoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_repository(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteRepositoryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_hooks(
        self,
    ) -> Callable[
        [secure_source_manager.ListHooksRequest],
        Union[
            secure_source_manager.ListHooksResponse,
            Awaitable[secure_source_manager.ListHooksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_hook(
        self,
    ) -> Callable[
        [secure_source_manager.GetHookRequest],
        Union[secure_source_manager.Hook, Awaitable[secure_source_manager.Hook]],
    ]:
        raise NotImplementedError()

    @property
    def create_hook(
        self,
    ) -> Callable[
        [secure_source_manager.CreateHookRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_hook(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateHookRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_hook(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteHookRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_iam_policy_repo(
        self,
    ) -> Callable[
        [iam_policy_pb2.GetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def set_iam_policy_repo(
        self,
    ) -> Callable[
        [iam_policy_pb2.SetIamPolicyRequest],
        Union[policy_pb2.Policy, Awaitable[policy_pb2.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def test_iam_permissions_repo(
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
    def create_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.CreateBranchRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_branch_rules(
        self,
    ) -> Callable[
        [secure_source_manager.ListBranchRulesRequest],
        Union[
            secure_source_manager.ListBranchRulesResponse,
            Awaitable[secure_source_manager.ListBranchRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.GetBranchRuleRequest],
        Union[
            secure_source_manager.BranchRule,
            Awaitable[secure_source_manager.BranchRule],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateBranchRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_branch_rule(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteBranchRuleRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.CreatePullRequestRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.GetPullRequestRequest],
        Union[
            secure_source_manager.PullRequest,
            Awaitable[secure_source_manager.PullRequest],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_pull_requests(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestsRequest],
        Union[
            secure_source_manager.ListPullRequestsResponse,
            Awaitable[secure_source_manager.ListPullRequestsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.UpdatePullRequestRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def merge_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.MergePullRequestRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def open_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.OpenPullRequestRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def close_pull_request(
        self,
    ) -> Callable[
        [secure_source_manager.ClosePullRequestRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_pull_request_file_diffs(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestFileDiffsRequest],
        Union[
            secure_source_manager.ListPullRequestFileDiffsResponse,
            Awaitable[secure_source_manager.ListPullRequestFileDiffsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_tree(
        self,
    ) -> Callable[
        [secure_source_manager.FetchTreeRequest],
        Union[
            secure_source_manager.FetchTreeResponse,
            Awaitable[secure_source_manager.FetchTreeResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_blob(
        self,
    ) -> Callable[
        [secure_source_manager.FetchBlobRequest],
        Union[
            secure_source_manager.FetchBlobResponse,
            Awaitable[secure_source_manager.FetchBlobResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def fetch_refs(
        self,
    ) -> Callable[
        [secure_source_manager.FetchRefsRequest],
        Union[
            secure_source_manager.FetchRefsResponse,
            Awaitable[secure_source_manager.FetchRefsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_issue(
        self,
    ) -> Callable[
        [secure_source_manager.CreateIssueRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_issue(
        self,
    ) -> Callable[
        [secure_source_manager.GetIssueRequest],
        Union[secure_source_manager.Issue, Awaitable[secure_source_manager.Issue]],
    ]:
        raise NotImplementedError()

    @property
    def list_issues(
        self,
    ) -> Callable[
        [secure_source_manager.ListIssuesRequest],
        Union[
            secure_source_manager.ListIssuesResponse,
            Awaitable[secure_source_manager.ListIssuesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_issue(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateIssueRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_issue(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteIssueRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def open_issue(
        self,
    ) -> Callable[
        [secure_source_manager.OpenIssueRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def close_issue(
        self,
    ) -> Callable[
        [secure_source_manager.CloseIssueRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.GetPullRequestCommentRequest],
        Union[
            secure_source_manager.PullRequestComment,
            Awaitable[secure_source_manager.PullRequestComment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ListPullRequestCommentsRequest],
        Union[
            secure_source_manager.ListPullRequestCommentsResponse,
            Awaitable[secure_source_manager.ListPullRequestCommentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.CreatePullRequestCommentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.UpdatePullRequestCommentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_pull_request_comment(
        self,
    ) -> Callable[
        [secure_source_manager.DeletePullRequestCommentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def batch_create_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.BatchCreatePullRequestCommentsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def resolve_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ResolvePullRequestCommentsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def unresolve_pull_request_comments(
        self,
    ) -> Callable[
        [secure_source_manager.UnresolvePullRequestCommentsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.CreateIssueCommentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.GetIssueCommentRequest],
        Union[
            secure_source_manager.IssueComment,
            Awaitable[secure_source_manager.IssueComment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_issue_comments(
        self,
    ) -> Callable[
        [secure_source_manager.ListIssueCommentsRequest],
        Union[
            secure_source_manager.ListIssueCommentsResponse,
            Awaitable[secure_source_manager.ListIssueCommentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.UpdateIssueCommentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_issue_comment(
        self,
    ) -> Callable[
        [secure_source_manager.DeleteIssueCommentRequest],
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


__all__ = ("SecureSourceManagerTransport",)
