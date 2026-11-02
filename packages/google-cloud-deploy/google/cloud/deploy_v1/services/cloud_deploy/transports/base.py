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

from google.cloud.deploy_v1 import gapic_version as package_version
from google.cloud.deploy_v1.types import cloud_deploy

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class CloudDeployTransport(abc.ABC):
    """Abstract transport class for CloudDeploy."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "clouddeploy.googleapis.com"

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
                 The hostname to connect to (default: 'clouddeploy.googleapis.com').
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
            self.list_delivery_pipelines: gapic_v1.method.wrap_method(
                self.list_delivery_pipelines,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_delivery_pipeline: gapic_v1.method.wrap_method(
                self.get_delivery_pipeline,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_delivery_pipeline: gapic_v1.method.wrap_method(
                self.create_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_delivery_pipeline: gapic_v1.method.wrap_method(
                self.update_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_delivery_pipeline: gapic_v1.method.wrap_method(
                self.delete_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_targets: gapic_v1.method.wrap_method(
                self.list_targets,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.rollback_target: gapic_v1.method.wrap_method(
                self.rollback_target,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_target: gapic_v1.method.wrap_method(
                self.get_target,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_target: gapic_v1.method.wrap_method(
                self.create_target,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_target: gapic_v1.method.wrap_method(
                self.update_target,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_target: gapic_v1.method.wrap_method(
                self.delete_target,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_custom_target_types: gapic_v1.method.wrap_method(
                self.list_custom_target_types,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_custom_target_type: gapic_v1.method.wrap_method(
                self.get_custom_target_type,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_custom_target_type: gapic_v1.method.wrap_method(
                self.create_custom_target_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_custom_target_type: gapic_v1.method.wrap_method(
                self.update_custom_target_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_custom_target_type: gapic_v1.method.wrap_method(
                self.delete_custom_target_type,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_releases: gapic_v1.method.wrap_method(
                self.list_releases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_release: gapic_v1.method.wrap_method(
                self.get_release,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_release: gapic_v1.method.wrap_method(
                self.create_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.abandon_release: gapic_v1.method.wrap_method(
                self.abandon_release,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_deploy_policy: gapic_v1.method.wrap_method(
                self.create_deploy_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_deploy_policy: gapic_v1.method.wrap_method(
                self.update_deploy_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_deploy_policy: gapic_v1.method.wrap_method(
                self.delete_deploy_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_deploy_policies: gapic_v1.method.wrap_method(
                self.list_deploy_policies,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_deploy_policy: gapic_v1.method.wrap_method(
                self.get_deploy_policy,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.approve_rollout: gapic_v1.method.wrap_method(
                self.approve_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.advance_rollout: gapic_v1.method.wrap_method(
                self.advance_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.cancel_rollout: gapic_v1.method.wrap_method(
                self.cancel_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_rollouts: gapic_v1.method.wrap_method(
                self.list_rollouts,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_rollout: gapic_v1.method.wrap_method(
                self.get_rollout,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_rollout: gapic_v1.method.wrap_method(
                self.create_rollout,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.ignore_job: gapic_v1.method.wrap_method(
                self.ignore_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.retry_job: gapic_v1.method.wrap_method(
                self.retry_job,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_job_runs: gapic_v1.method.wrap_method(
                self.list_job_runs,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_job_run: gapic_v1.method.wrap_method(
                self.get_job_run,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.terminate_job_run: gapic_v1.method.wrap_method(
                self.terminate_job_run,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_config: gapic_v1.method.wrap_method(
                self.get_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_automation: gapic_v1.method.wrap_method(
                self.create_automation,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_automation: gapic_v1.method.wrap_method(
                self.update_automation,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_automation: gapic_v1.method.wrap_method(
                self.delete_automation,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_automation: gapic_v1.method.wrap_method(
                self.get_automation,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_automations: gapic_v1.method.wrap_method(
                self.list_automations,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_automation_run: gapic_v1.method.wrap_method(
                self.get_automation_run,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_automation_runs: gapic_v1.method.wrap_method(
                self.list_automation_runs,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.cancel_automation_run: gapic_v1.method.wrap_method(
                self.cancel_automation_run,
                default_timeout=60.0,
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
    def list_delivery_pipelines(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeliveryPipelinesRequest],
        Union[
            cloud_deploy.ListDeliveryPipelinesResponse,
            Awaitable[cloud_deploy.ListDeliveryPipelinesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.GetDeliveryPipelineRequest],
        Union[cloud_deploy.DeliveryPipeline, Awaitable[cloud_deploy.DeliveryPipeline]],
    ]:
        raise NotImplementedError()

    @property
    def create_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.CreateDeliveryPipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateDeliveryPipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteDeliveryPipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_targets(
        self,
    ) -> Callable[
        [cloud_deploy.ListTargetsRequest],
        Union[
            cloud_deploy.ListTargetsResponse,
            Awaitable[cloud_deploy.ListTargetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def rollback_target(
        self,
    ) -> Callable[
        [cloud_deploy.RollbackTargetRequest],
        Union[
            cloud_deploy.RollbackTargetResponse,
            Awaitable[cloud_deploy.RollbackTargetResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_target(
        self,
    ) -> Callable[
        [cloud_deploy.GetTargetRequest],
        Union[cloud_deploy.Target, Awaitable[cloud_deploy.Target]],
    ]:
        raise NotImplementedError()

    @property
    def create_target(
        self,
    ) -> Callable[
        [cloud_deploy.CreateTargetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_target(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateTargetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_target(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteTargetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_custom_target_types(
        self,
    ) -> Callable[
        [cloud_deploy.ListCustomTargetTypesRequest],
        Union[
            cloud_deploy.ListCustomTargetTypesResponse,
            Awaitable[cloud_deploy.ListCustomTargetTypesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.GetCustomTargetTypeRequest],
        Union[cloud_deploy.CustomTargetType, Awaitable[cloud_deploy.CustomTargetType]],
    ]:
        raise NotImplementedError()

    @property
    def create_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.CreateCustomTargetTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateCustomTargetTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_custom_target_type(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteCustomTargetTypeRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_releases(
        self,
    ) -> Callable[
        [cloud_deploy.ListReleasesRequest],
        Union[
            cloud_deploy.ListReleasesResponse,
            Awaitable[cloud_deploy.ListReleasesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_release(
        self,
    ) -> Callable[
        [cloud_deploy.GetReleaseRequest],
        Union[cloud_deploy.Release, Awaitable[cloud_deploy.Release]],
    ]:
        raise NotImplementedError()

    @property
    def create_release(
        self,
    ) -> Callable[
        [cloud_deploy.CreateReleaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def abandon_release(
        self,
    ) -> Callable[
        [cloud_deploy.AbandonReleaseRequest],
        Union[
            cloud_deploy.AbandonReleaseResponse,
            Awaitable[cloud_deploy.AbandonReleaseResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.CreateDeployPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateDeployPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteDeployPolicyRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_deploy_policies(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeployPoliciesRequest],
        Union[
            cloud_deploy.ListDeployPoliciesResponse,
            Awaitable[cloud_deploy.ListDeployPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_deploy_policy(
        self,
    ) -> Callable[
        [cloud_deploy.GetDeployPolicyRequest],
        Union[cloud_deploy.DeployPolicy, Awaitable[cloud_deploy.DeployPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def approve_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.ApproveRolloutRequest],
        Union[
            cloud_deploy.ApproveRolloutResponse,
            Awaitable[cloud_deploy.ApproveRolloutResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def advance_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.AdvanceRolloutRequest],
        Union[
            cloud_deploy.AdvanceRolloutResponse,
            Awaitable[cloud_deploy.AdvanceRolloutResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def cancel_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.CancelRolloutRequest],
        Union[
            cloud_deploy.CancelRolloutResponse,
            Awaitable[cloud_deploy.CancelRolloutResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [cloud_deploy.ListRolloutsRequest],
        Union[
            cloud_deploy.ListRolloutsResponse,
            Awaitable[cloud_deploy.ListRolloutsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.GetRolloutRequest],
        Union[cloud_deploy.Rollout, Awaitable[cloud_deploy.Rollout]],
    ]:
        raise NotImplementedError()

    @property
    def create_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.CreateRolloutRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def ignore_job(
        self,
    ) -> Callable[
        [cloud_deploy.IgnoreJobRequest],
        Union[
            cloud_deploy.IgnoreJobResponse, Awaitable[cloud_deploy.IgnoreJobResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def retry_job(
        self,
    ) -> Callable[
        [cloud_deploy.RetryJobRequest],
        Union[cloud_deploy.RetryJobResponse, Awaitable[cloud_deploy.RetryJobResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_job_runs(
        self,
    ) -> Callable[
        [cloud_deploy.ListJobRunsRequest],
        Union[
            cloud_deploy.ListJobRunsResponse,
            Awaitable[cloud_deploy.ListJobRunsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_job_run(
        self,
    ) -> Callable[
        [cloud_deploy.GetJobRunRequest],
        Union[cloud_deploy.JobRun, Awaitable[cloud_deploy.JobRun]],
    ]:
        raise NotImplementedError()

    @property
    def terminate_job_run(
        self,
    ) -> Callable[
        [cloud_deploy.TerminateJobRunRequest],
        Union[
            cloud_deploy.TerminateJobRunResponse,
            Awaitable[cloud_deploy.TerminateJobRunResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_config(
        self,
    ) -> Callable[
        [cloud_deploy.GetConfigRequest],
        Union[cloud_deploy.Config, Awaitable[cloud_deploy.Config]],
    ]:
        raise NotImplementedError()

    @property
    def create_automation(
        self,
    ) -> Callable[
        [cloud_deploy.CreateAutomationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_automation(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateAutomationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_automation(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteAutomationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_automation(
        self,
    ) -> Callable[
        [cloud_deploy.GetAutomationRequest],
        Union[cloud_deploy.Automation, Awaitable[cloud_deploy.Automation]],
    ]:
        raise NotImplementedError()

    @property
    def list_automations(
        self,
    ) -> Callable[
        [cloud_deploy.ListAutomationsRequest],
        Union[
            cloud_deploy.ListAutomationsResponse,
            Awaitable[cloud_deploy.ListAutomationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_automation_run(
        self,
    ) -> Callable[
        [cloud_deploy.GetAutomationRunRequest],
        Union[cloud_deploy.AutomationRun, Awaitable[cloud_deploy.AutomationRun]],
    ]:
        raise NotImplementedError()

    @property
    def list_automation_runs(
        self,
    ) -> Callable[
        [cloud_deploy.ListAutomationRunsRequest],
        Union[
            cloud_deploy.ListAutomationRunsResponse,
            Awaitable[cloud_deploy.ListAutomationRunsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def cancel_automation_run(
        self,
    ) -> Callable[
        [cloud_deploy.CancelAutomationRunRequest],
        Union[
            cloud_deploy.CancelAutomationRunResponse,
            Awaitable[cloud_deploy.CancelAutomationRunResponse],
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


__all__ = ("CloudDeployTransport",)
