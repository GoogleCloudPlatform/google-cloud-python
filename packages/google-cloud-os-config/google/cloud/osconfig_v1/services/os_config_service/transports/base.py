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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.osconfig_v1 import gapic_version as package_version
from google.cloud.osconfig_v1.types import patch_deployments, patch_jobs

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class OsConfigServiceTransport(abc.ABC):
    """Abstract transport class for OsConfigService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "osconfig.googleapis.com"

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
                 The hostname to connect to (default: 'osconfig.googleapis.com').
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
            self.execute_patch_job: gapic_v1.method.wrap_method(
                self.execute_patch_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_patch_job: gapic_v1.method.wrap_method(
                self.get_patch_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_patch_job: gapic_v1.method.wrap_method(
                self.cancel_patch_job,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_patch_jobs: gapic_v1.method.wrap_method(
                self.list_patch_jobs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_patch_job_instance_details: gapic_v1.method.wrap_method(
                self.list_patch_job_instance_details,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_patch_deployment: gapic_v1.method.wrap_method(
                self.create_patch_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_patch_deployment: gapic_v1.method.wrap_method(
                self.get_patch_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_patch_deployments: gapic_v1.method.wrap_method(
                self.list_patch_deployments,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_patch_deployment: gapic_v1.method.wrap_method(
                self.delete_patch_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_patch_deployment: gapic_v1.method.wrap_method(
                self.update_patch_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.pause_patch_deployment: gapic_v1.method.wrap_method(
                self.pause_patch_deployment,
                default_timeout=None,
                client_info=client_info,
            ),
            self.resume_patch_deployment: gapic_v1.method.wrap_method(
                self.resume_patch_deployment,
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
    def execute_patch_job(
        self,
    ) -> Callable[
        [patch_jobs.ExecutePatchJobRequest],
        Union[patch_jobs.PatchJob, Awaitable[patch_jobs.PatchJob]],
    ]:
        raise NotImplementedError()

    @property
    def get_patch_job(
        self,
    ) -> Callable[
        [patch_jobs.GetPatchJobRequest],
        Union[patch_jobs.PatchJob, Awaitable[patch_jobs.PatchJob]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_patch_job(
        self,
    ) -> Callable[
        [patch_jobs.CancelPatchJobRequest],
        Union[patch_jobs.PatchJob, Awaitable[patch_jobs.PatchJob]],
    ]:
        raise NotImplementedError()

    @property
    def list_patch_jobs(
        self,
    ) -> Callable[
        [patch_jobs.ListPatchJobsRequest],
        Union[
            patch_jobs.ListPatchJobsResponse,
            Awaitable[patch_jobs.ListPatchJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_patch_job_instance_details(
        self,
    ) -> Callable[
        [patch_jobs.ListPatchJobInstanceDetailsRequest],
        Union[
            patch_jobs.ListPatchJobInstanceDetailsResponse,
            Awaitable[patch_jobs.ListPatchJobInstanceDetailsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.CreatePatchDeploymentRequest],
        Union[
            patch_deployments.PatchDeployment,
            Awaitable[patch_deployments.PatchDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.GetPatchDeploymentRequest],
        Union[
            patch_deployments.PatchDeployment,
            Awaitable[patch_deployments.PatchDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_patch_deployments(
        self,
    ) -> Callable[
        [patch_deployments.ListPatchDeploymentsRequest],
        Union[
            patch_deployments.ListPatchDeploymentsResponse,
            Awaitable[patch_deployments.ListPatchDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.DeletePatchDeploymentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.UpdatePatchDeploymentRequest],
        Union[
            patch_deployments.PatchDeployment,
            Awaitable[patch_deployments.PatchDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def pause_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.PausePatchDeploymentRequest],
        Union[
            patch_deployments.PatchDeployment,
            Awaitable[patch_deployments.PatchDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def resume_patch_deployment(
        self,
    ) -> Callable[
        [patch_deployments.ResumePatchDeploymentRequest],
        Union[
            patch_deployments.PatchDeployment,
            Awaitable[patch_deployments.PatchDeployment],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("OsConfigServiceTransport",)
