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
from google.cloud.location import locations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.dlp_v2 import gapic_version as package_version
from google.cloud.dlp_v2.types import dlp

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DlpServiceTransport(abc.ABC):
    """Abstract transport class for DlpService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "dlp.googleapis.com"

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
                 The hostname to connect to (default: 'dlp.googleapis.com').
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
            self.inspect_content: gapic_v1.method.wrap_method(
                self.inspect_content,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.redact_image: gapic_v1.method.wrap_method(
                self.redact_image,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.deidentify_content: gapic_v1.method.wrap_method(
                self.deidentify_content,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.reidentify_content: gapic_v1.method.wrap_method(
                self.reidentify_content,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_info_types: gapic_v1.method.wrap_method(
                self.list_info_types,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_inspect_template: gapic_v1.method.wrap_method(
                self.create_inspect_template,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_inspect_template: gapic_v1.method.wrap_method(
                self.update_inspect_template,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_inspect_template: gapic_v1.method.wrap_method(
                self.get_inspect_template,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_inspect_templates: gapic_v1.method.wrap_method(
                self.list_inspect_templates,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_inspect_template: gapic_v1.method.wrap_method(
                self.delete_inspect_template,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_deidentify_template: gapic_v1.method.wrap_method(
                self.create_deidentify_template,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_deidentify_template: gapic_v1.method.wrap_method(
                self.update_deidentify_template,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_deidentify_template: gapic_v1.method.wrap_method(
                self.get_deidentify_template,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_deidentify_templates: gapic_v1.method.wrap_method(
                self.list_deidentify_templates,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_deidentify_template: gapic_v1.method.wrap_method(
                self.delete_deidentify_template,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_job_trigger: gapic_v1.method.wrap_method(
                self.create_job_trigger,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_job_trigger: gapic_v1.method.wrap_method(
                self.update_job_trigger,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.hybrid_inspect_job_trigger: gapic_v1.method.wrap_method(
                self.hybrid_inspect_job_trigger,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_job_trigger: gapic_v1.method.wrap_method(
                self.get_job_trigger,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_job_triggers: gapic_v1.method.wrap_method(
                self.list_job_triggers,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_job_trigger: gapic_v1.method.wrap_method(
                self.delete_job_trigger,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.activate_job_trigger: gapic_v1.method.wrap_method(
                self.activate_job_trigger,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_discovery_config: gapic_v1.method.wrap_method(
                self.create_discovery_config,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_discovery_config: gapic_v1.method.wrap_method(
                self.update_discovery_config,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_discovery_config: gapic_v1.method.wrap_method(
                self.get_discovery_config,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_discovery_configs: gapic_v1.method.wrap_method(
                self.list_discovery_configs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_discovery_config: gapic_v1.method.wrap_method(
                self.delete_discovery_config,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_dlp_job: gapic_v1.method.wrap_method(
                self.create_dlp_job,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_dlp_jobs: gapic_v1.method.wrap_method(
                self.list_dlp_jobs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_dlp_job: gapic_v1.method.wrap_method(
                self.get_dlp_job,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_dlp_job: gapic_v1.method.wrap_method(
                self.delete_dlp_job,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.cancel_dlp_job: gapic_v1.method.wrap_method(
                self.cancel_dlp_job,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_stored_info_type: gapic_v1.method.wrap_method(
                self.create_stored_info_type,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.update_stored_info_type: gapic_v1.method.wrap_method(
                self.update_stored_info_type,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_stored_info_type: gapic_v1.method.wrap_method(
                self.get_stored_info_type,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_stored_info_types: gapic_v1.method.wrap_method(
                self.list_stored_info_types,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_stored_info_type: gapic_v1.method.wrap_method(
                self.delete_stored_info_type,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_project_data_profiles: gapic_v1.method.wrap_method(
                self.list_project_data_profiles,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_table_data_profiles: gapic_v1.method.wrap_method(
                self.list_table_data_profiles,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_column_data_profiles: gapic_v1.method.wrap_method(
                self.list_column_data_profiles,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_project_data_profile: gapic_v1.method.wrap_method(
                self.get_project_data_profile,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.list_file_store_data_profiles: gapic_v1.method.wrap_method(
                self.list_file_store_data_profiles,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_file_store_data_profile: gapic_v1.method.wrap_method(
                self.get_file_store_data_profile,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_file_store_data_profile: gapic_v1.method.wrap_method(
                self.delete_file_store_data_profile,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_table_data_profile: gapic_v1.method.wrap_method(
                self.get_table_data_profile,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.get_column_data_profile: gapic_v1.method.wrap_method(
                self.get_column_data_profile,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.delete_table_data_profile: gapic_v1.method.wrap_method(
                self.delete_table_data_profile,
                default_timeout=None,
                client_info=client_info,
            ),
            self.hybrid_inspect_dlp_job: gapic_v1.method.wrap_method(
                self.hybrid_inspect_dlp_job,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.finish_dlp_job: gapic_v1.method.wrap_method(
                self.finish_dlp_job,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_connection: gapic_v1.method.wrap_method(
                self.create_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_connection: gapic_v1.method.wrap_method(
                self.get_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_connections: gapic_v1.method.wrap_method(
                self.list_connections,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_connections: gapic_v1.method.wrap_method(
                self.search_connections,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_connection: gapic_v1.method.wrap_method(
                self.delete_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_connection: gapic_v1.method.wrap_method(
                self.update_connection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_content_policy: gapic_v1.method.wrap_method(
                self.create_content_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_content_policy: gapic_v1.method.wrap_method(
                self.update_content_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_content_policy: gapic_v1.method.wrap_method(
                self.get_content_policy,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_content_policies: gapic_v1.method.wrap_method(
                self.list_content_policies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_content_policy: gapic_v1.method.wrap_method(
                self.delete_content_policy,
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
    def inspect_content(
        self,
    ) -> Callable[
        [dlp.InspectContentRequest],
        Union[dlp.InspectContentResponse, Awaitable[dlp.InspectContentResponse]],
    ]:
        raise NotImplementedError()

    @property
    def redact_image(
        self,
    ) -> Callable[
        [dlp.RedactImageRequest],
        Union[dlp.RedactImageResponse, Awaitable[dlp.RedactImageResponse]],
    ]:
        raise NotImplementedError()

    @property
    def deidentify_content(
        self,
    ) -> Callable[
        [dlp.DeidentifyContentRequest],
        Union[dlp.DeidentifyContentResponse, Awaitable[dlp.DeidentifyContentResponse]],
    ]:
        raise NotImplementedError()

    @property
    def reidentify_content(
        self,
    ) -> Callable[
        [dlp.ReidentifyContentRequest],
        Union[dlp.ReidentifyContentResponse, Awaitable[dlp.ReidentifyContentResponse]],
    ]:
        raise NotImplementedError()

    @property
    def list_info_types(
        self,
    ) -> Callable[
        [dlp.ListInfoTypesRequest],
        Union[dlp.ListInfoTypesResponse, Awaitable[dlp.ListInfoTypesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_inspect_template(
        self,
    ) -> Callable[
        [dlp.CreateInspectTemplateRequest],
        Union[dlp.InspectTemplate, Awaitable[dlp.InspectTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def update_inspect_template(
        self,
    ) -> Callable[
        [dlp.UpdateInspectTemplateRequest],
        Union[dlp.InspectTemplate, Awaitable[dlp.InspectTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def get_inspect_template(
        self,
    ) -> Callable[
        [dlp.GetInspectTemplateRequest],
        Union[dlp.InspectTemplate, Awaitable[dlp.InspectTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def list_inspect_templates(
        self,
    ) -> Callable[
        [dlp.ListInspectTemplatesRequest],
        Union[
            dlp.ListInspectTemplatesResponse,
            Awaitable[dlp.ListInspectTemplatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_inspect_template(
        self,
    ) -> Callable[
        [dlp.DeleteInspectTemplateRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_deidentify_template(
        self,
    ) -> Callable[
        [dlp.CreateDeidentifyTemplateRequest],
        Union[dlp.DeidentifyTemplate, Awaitable[dlp.DeidentifyTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def update_deidentify_template(
        self,
    ) -> Callable[
        [dlp.UpdateDeidentifyTemplateRequest],
        Union[dlp.DeidentifyTemplate, Awaitable[dlp.DeidentifyTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def get_deidentify_template(
        self,
    ) -> Callable[
        [dlp.GetDeidentifyTemplateRequest],
        Union[dlp.DeidentifyTemplate, Awaitable[dlp.DeidentifyTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def list_deidentify_templates(
        self,
    ) -> Callable[
        [dlp.ListDeidentifyTemplatesRequest],
        Union[
            dlp.ListDeidentifyTemplatesResponse,
            Awaitable[dlp.ListDeidentifyTemplatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_deidentify_template(
        self,
    ) -> Callable[
        [dlp.DeleteDeidentifyTemplateRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_job_trigger(
        self,
    ) -> Callable[
        [dlp.CreateJobTriggerRequest], Union[dlp.JobTrigger, Awaitable[dlp.JobTrigger]]
    ]:
        raise NotImplementedError()

    @property
    def update_job_trigger(
        self,
    ) -> Callable[
        [dlp.UpdateJobTriggerRequest], Union[dlp.JobTrigger, Awaitable[dlp.JobTrigger]]
    ]:
        raise NotImplementedError()

    @property
    def hybrid_inspect_job_trigger(
        self,
    ) -> Callable[
        [dlp.HybridInspectJobTriggerRequest],
        Union[dlp.HybridInspectResponse, Awaitable[dlp.HybridInspectResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_job_trigger(
        self,
    ) -> Callable[
        [dlp.GetJobTriggerRequest], Union[dlp.JobTrigger, Awaitable[dlp.JobTrigger]]
    ]:
        raise NotImplementedError()

    @property
    def list_job_triggers(
        self,
    ) -> Callable[
        [dlp.ListJobTriggersRequest],
        Union[dlp.ListJobTriggersResponse, Awaitable[dlp.ListJobTriggersResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_job_trigger(
        self,
    ) -> Callable[
        [dlp.DeleteJobTriggerRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def activate_job_trigger(
        self,
    ) -> Callable[
        [dlp.ActivateJobTriggerRequest], Union[dlp.DlpJob, Awaitable[dlp.DlpJob]]
    ]:
        raise NotImplementedError()

    @property
    def create_discovery_config(
        self,
    ) -> Callable[
        [dlp.CreateDiscoveryConfigRequest],
        Union[dlp.DiscoveryConfig, Awaitable[dlp.DiscoveryConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_discovery_config(
        self,
    ) -> Callable[
        [dlp.UpdateDiscoveryConfigRequest],
        Union[dlp.DiscoveryConfig, Awaitable[dlp.DiscoveryConfig]],
    ]:
        raise NotImplementedError()

    @property
    def get_discovery_config(
        self,
    ) -> Callable[
        [dlp.GetDiscoveryConfigRequest],
        Union[dlp.DiscoveryConfig, Awaitable[dlp.DiscoveryConfig]],
    ]:
        raise NotImplementedError()

    @property
    def list_discovery_configs(
        self,
    ) -> Callable[
        [dlp.ListDiscoveryConfigsRequest],
        Union[
            dlp.ListDiscoveryConfigsResponse,
            Awaitable[dlp.ListDiscoveryConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_discovery_config(
        self,
    ) -> Callable[
        [dlp.DeleteDiscoveryConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_dlp_job(
        self,
    ) -> Callable[[dlp.CreateDlpJobRequest], Union[dlp.DlpJob, Awaitable[dlp.DlpJob]]]:
        raise NotImplementedError()

    @property
    def list_dlp_jobs(
        self,
    ) -> Callable[
        [dlp.ListDlpJobsRequest],
        Union[dlp.ListDlpJobsResponse, Awaitable[dlp.ListDlpJobsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_dlp_job(
        self,
    ) -> Callable[[dlp.GetDlpJobRequest], Union[dlp.DlpJob, Awaitable[dlp.DlpJob]]]:
        raise NotImplementedError()

    @property
    def delete_dlp_job(
        self,
    ) -> Callable[
        [dlp.DeleteDlpJobRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def cancel_dlp_job(
        self,
    ) -> Callable[
        [dlp.CancelDlpJobRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def create_stored_info_type(
        self,
    ) -> Callable[
        [dlp.CreateStoredInfoTypeRequest],
        Union[dlp.StoredInfoType, Awaitable[dlp.StoredInfoType]],
    ]:
        raise NotImplementedError()

    @property
    def update_stored_info_type(
        self,
    ) -> Callable[
        [dlp.UpdateStoredInfoTypeRequest],
        Union[dlp.StoredInfoType, Awaitable[dlp.StoredInfoType]],
    ]:
        raise NotImplementedError()

    @property
    def get_stored_info_type(
        self,
    ) -> Callable[
        [dlp.GetStoredInfoTypeRequest],
        Union[dlp.StoredInfoType, Awaitable[dlp.StoredInfoType]],
    ]:
        raise NotImplementedError()

    @property
    def list_stored_info_types(
        self,
    ) -> Callable[
        [dlp.ListStoredInfoTypesRequest],
        Union[
            dlp.ListStoredInfoTypesResponse, Awaitable[dlp.ListStoredInfoTypesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_stored_info_type(
        self,
    ) -> Callable[
        [dlp.DeleteStoredInfoTypeRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_project_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListProjectDataProfilesRequest],
        Union[
            dlp.ListProjectDataProfilesResponse,
            Awaitable[dlp.ListProjectDataProfilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_table_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListTableDataProfilesRequest],
        Union[
            dlp.ListTableDataProfilesResponse,
            Awaitable[dlp.ListTableDataProfilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_column_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListColumnDataProfilesRequest],
        Union[
            dlp.ListColumnDataProfilesResponse,
            Awaitable[dlp.ListColumnDataProfilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_project_data_profile(
        self,
    ) -> Callable[
        [dlp.GetProjectDataProfileRequest],
        Union[dlp.ProjectDataProfile, Awaitable[dlp.ProjectDataProfile]],
    ]:
        raise NotImplementedError()

    @property
    def list_file_store_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListFileStoreDataProfilesRequest],
        Union[
            dlp.ListFileStoreDataProfilesResponse,
            Awaitable[dlp.ListFileStoreDataProfilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_file_store_data_profile(
        self,
    ) -> Callable[
        [dlp.GetFileStoreDataProfileRequest],
        Union[dlp.FileStoreDataProfile, Awaitable[dlp.FileStoreDataProfile]],
    ]:
        raise NotImplementedError()

    @property
    def delete_file_store_data_profile(
        self,
    ) -> Callable[
        [dlp.DeleteFileStoreDataProfileRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_table_data_profile(
        self,
    ) -> Callable[
        [dlp.GetTableDataProfileRequest],
        Union[dlp.TableDataProfile, Awaitable[dlp.TableDataProfile]],
    ]:
        raise NotImplementedError()

    @property
    def get_column_data_profile(
        self,
    ) -> Callable[
        [dlp.GetColumnDataProfileRequest],
        Union[dlp.ColumnDataProfile, Awaitable[dlp.ColumnDataProfile]],
    ]:
        raise NotImplementedError()

    @property
    def delete_table_data_profile(
        self,
    ) -> Callable[
        [dlp.DeleteTableDataProfileRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def hybrid_inspect_dlp_job(
        self,
    ) -> Callable[
        [dlp.HybridInspectDlpJobRequest],
        Union[dlp.HybridInspectResponse, Awaitable[dlp.HybridInspectResponse]],
    ]:
        raise NotImplementedError()

    @property
    def finish_dlp_job(
        self,
    ) -> Callable[
        [dlp.FinishDlpJobRequest], Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]]
    ]:
        raise NotImplementedError()

    @property
    def create_connection(
        self,
    ) -> Callable[
        [dlp.CreateConnectionRequest], Union[dlp.Connection, Awaitable[dlp.Connection]]
    ]:
        raise NotImplementedError()

    @property
    def get_connection(
        self,
    ) -> Callable[
        [dlp.GetConnectionRequest], Union[dlp.Connection, Awaitable[dlp.Connection]]
    ]:
        raise NotImplementedError()

    @property
    def list_connections(
        self,
    ) -> Callable[
        [dlp.ListConnectionsRequest],
        Union[dlp.ListConnectionsResponse, Awaitable[dlp.ListConnectionsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def search_connections(
        self,
    ) -> Callable[
        [dlp.SearchConnectionsRequest],
        Union[dlp.SearchConnectionsResponse, Awaitable[dlp.SearchConnectionsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_connection(
        self,
    ) -> Callable[
        [dlp.DeleteConnectionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_connection(
        self,
    ) -> Callable[
        [dlp.UpdateConnectionRequest], Union[dlp.Connection, Awaitable[dlp.Connection]]
    ]:
        raise NotImplementedError()

    @property
    def create_content_policy(
        self,
    ) -> Callable[
        [dlp.CreateContentPolicyRequest],
        Union[dlp.ContentPolicy, Awaitable[dlp.ContentPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def update_content_policy(
        self,
    ) -> Callable[
        [dlp.UpdateContentPolicyRequest],
        Union[dlp.ContentPolicy, Awaitable[dlp.ContentPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def get_content_policy(
        self,
    ) -> Callable[
        [dlp.GetContentPolicyRequest],
        Union[dlp.ContentPolicy, Awaitable[dlp.ContentPolicy]],
    ]:
        raise NotImplementedError()

    @property
    def list_content_policies(
        self,
    ) -> Callable[
        [dlp.ListContentPoliciesRequest],
        Union[
            dlp.ListContentPoliciesResponse, Awaitable[dlp.ListContentPoliciesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_content_policy(
        self,
    ) -> Callable[
        [dlp.DeleteContentPolicyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("DlpServiceTransport",)
