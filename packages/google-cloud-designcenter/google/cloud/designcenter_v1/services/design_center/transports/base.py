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

from google.cloud.designcenter_v1 import gapic_version as package_version
from google.cloud.designcenter_v1.types import (
    apphub_integration_messages,
    authoring,
    authoring_messages,
    best_practices,
    best_practices_messages,
    catalog_management,
    catalog_management_messages,
    deployment_messages,
    deployment_resources,
    sharing,
    sharing_messages,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DesignCenterTransport(abc.ABC):
    """Abstract transport class for DesignCenter."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "designcenter.googleapis.com"

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
                 The hostname to connect to (default: 'designcenter.googleapis.com').
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
            self.get_space: gapic_v1.method.wrap_method(
                self.get_space,
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
            self.list_spaces: gapic_v1.method.wrap_method(
                self.list_spaces,
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
            self.create_space: gapic_v1.method.wrap_method(
                self.create_space,
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_space: gapic_v1.method.wrap_method(
                self.update_space,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_space: gapic_v1.method.wrap_method(
                self.delete_space,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_application_template: gapic_v1.method.wrap_method(
                self.get_application_template,
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
            self.list_application_templates: gapic_v1.method.wrap_method(
                self.list_application_templates,
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
            self.create_application_template: gapic_v1.method.wrap_method(
                self.create_application_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_application_template: gapic_v1.method.wrap_method(
                self.update_application_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.import_application_template: gapic_v1.method.wrap_method(
                self.import_application_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_application_template: gapic_v1.method.wrap_method(
                self.delete_application_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.commit_application_template: gapic_v1.method.wrap_method(
                self.commit_application_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.snapshot_application_template: gapic_v1.method.wrap_method(
                self.snapshot_application_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_application_template_ia_c: gapic_v1.method.wrap_method(
                self.generate_application_template_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.export_application_template_ia_c: gapic_v1.method.wrap_method(
                self.export_application_template_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_application_template_revision_ia_c: gapic_v1.method.wrap_method(
                self.generate_application_template_revision_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.export_application_template_revision_ia_c: gapic_v1.method.wrap_method(
                self.export_application_template_revision_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_component: gapic_v1.method.wrap_method(
                self.get_component,
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
            self.list_components: gapic_v1.method.wrap_method(
                self.list_components,
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
            self.create_component: gapic_v1.method.wrap_method(
                self.create_component,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_component: gapic_v1.method.wrap_method(
                self.update_component,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_component: gapic_v1.method.wrap_method(
                self.delete_component,
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
            self.create_connection: gapic_v1.method.wrap_method(
                self.create_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_connection: gapic_v1.method.wrap_method(
                self.update_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_connection: gapic_v1.method.wrap_method(
                self.delete_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_application_template_revision: gapic_v1.method.wrap_method(
                self.get_application_template_revision,
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
            self.list_application_template_revisions: gapic_v1.method.wrap_method(
                self.list_application_template_revisions,
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
            self.delete_application_template_revision: gapic_v1.method.wrap_method(
                self.delete_application_template_revision,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_catalog: gapic_v1.method.wrap_method(
                self.get_catalog,
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
            self.list_catalogs: gapic_v1.method.wrap_method(
                self.list_catalogs,
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
            self.create_catalog: gapic_v1.method.wrap_method(
                self.create_catalog,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_catalog: gapic_v1.method.wrap_method(
                self.update_catalog,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_catalog: gapic_v1.method.wrap_method(
                self.delete_catalog,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_catalog_template: gapic_v1.method.wrap_method(
                self.create_catalog_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_catalog_template: gapic_v1.method.wrap_method(
                self.get_catalog_template,
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
            self.list_catalog_templates: gapic_v1.method.wrap_method(
                self.list_catalog_templates,
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
            self.update_catalog_template: gapic_v1.method.wrap_method(
                self.update_catalog_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_catalog_template: gapic_v1.method.wrap_method(
                self.delete_catalog_template,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_share: gapic_v1.method.wrap_method(
                self.create_share,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_shares: gapic_v1.method.wrap_method(
                self.list_shares,
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
            self.get_share: gapic_v1.method.wrap_method(
                self.get_share,
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
            self.delete_share: gapic_v1.method.wrap_method(
                self.delete_share,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.sync_share: gapic_v1.method.wrap_method(
                self.sync_share,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_shared_template: gapic_v1.method.wrap_method(
                self.get_shared_template,
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
            self.list_shared_templates: gapic_v1.method.wrap_method(
                self.list_shared_templates,
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
            self.get_shared_template_revision: gapic_v1.method.wrap_method(
                self.get_shared_template_revision,
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
            self.list_shared_template_revisions: gapic_v1.method.wrap_method(
                self.list_shared_template_revisions,
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
            self.create_catalog_template_revision: gapic_v1.method.wrap_method(
                self.create_catalog_template_revision,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_catalog_template_revision: gapic_v1.method.wrap_method(
                self.get_catalog_template_revision,
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
            self.list_catalog_template_revisions: gapic_v1.method.wrap_method(
                self.list_catalog_template_revisions,
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
            self.delete_catalog_template_revision: gapic_v1.method.wrap_method(
                self.delete_catalog_template_revision,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_application: gapic_v1.method.wrap_method(
                self.create_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_application: gapic_v1.method.wrap_method(
                self.get_application,
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
            self.list_applications: gapic_v1.method.wrap_method(
                self.list_applications,
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
            self.update_application: gapic_v1.method.wrap_method(
                self.update_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_application: gapic_v1.method.wrap_method(
                self.delete_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.deploy_application: gapic_v1.method.wrap_method(
                self.deploy_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.preview_application: gapic_v1.method.wrap_method(
                self.preview_application,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_application_assessment_report: gapic_v1.method.wrap_method(
                self.fetch_application_assessment_report,
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
            self.generate_application_assessment_report: gapic_v1.method.wrap_method(
                self.generate_application_assessment_report,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_application_template_assessment_report: gapic_v1.method.wrap_method(
                self.generate_application_template_assessment_report,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_assessment_report: gapic_v1.method.wrap_method(
                self.generate_assessment_report,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.generate_terraform_plan_assessment_report: gapic_v1.method.wrap_method(
                self.generate_terraform_plan_assessment_report,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_policy: gapic_v1.method.wrap_method(
                self.get_policy,
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
            self.list_policies: gapic_v1.method.wrap_method(
                self.list_policies,
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
            self.create_policy: gapic_v1.method.wrap_method(
                self.create_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_policy: gapic_v1.method.wrap_method(
                self.update_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_policy: gapic_v1.method.wrap_method(
                self.delete_policy,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.fetch_frameworks: gapic_v1.method.wrap_method(
                self.fetch_frameworks,
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
            self.generate_application_ia_c: gapic_v1.method.wrap_method(
                self.generate_application_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.export_application_ia_c: gapic_v1.method.wrap_method(
                self.export_application_ia_c,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_application_template_ia_c: gapic_v1.method.wrap_method(
                self.import_application_template_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.ingest_application_template_ia_c: gapic_v1.method.wrap_method(
                self.ingest_application_template_ia_c,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_application_ia_c: gapic_v1.method.wrap_method(
                self.import_application_ia_c,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.register_app_hub_application_resources: gapic_v1.method.wrap_method(
                self.register_app_hub_application_resources,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_application_template_system_revisions: gapic_v1.method.wrap_method(
                self.list_application_template_system_revisions,
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
            self.get_application_template_system_revision: gapic_v1.method.wrap_method(
                self.get_application_template_system_revision,
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
            self.recommend_iam_roles: gapic_v1.method.wrap_method(
                self.recommend_iam_roles,
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
    def get_space(
        self,
    ) -> Callable[
        [catalog_management_messages.GetSpaceRequest],
        Union[catalog_management.Space, Awaitable[catalog_management.Space]],
    ]:
        raise NotImplementedError()

    @property
    def list_spaces(
        self,
    ) -> Callable[
        [catalog_management_messages.ListSpacesRequest],
        Union[
            catalog_management_messages.ListSpacesResponse,
            Awaitable[catalog_management_messages.ListSpacesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_space(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateSpaceRequest],
        Union[catalog_management.Space, Awaitable[catalog_management.Space]],
    ]:
        raise NotImplementedError()

    @property
    def update_space(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateSpaceRequest],
        Union[catalog_management.Space, Awaitable[catalog_management.Space]],
    ]:
        raise NotImplementedError()

    @property
    def delete_space(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteSpaceRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_application_template(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateRequest],
        Union[authoring.ApplicationTemplate, Awaitable[authoring.ApplicationTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def list_application_templates(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplatesRequest],
        Union[
            authoring_messages.ListApplicationTemplatesResponse,
            Awaitable[authoring_messages.ListApplicationTemplatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_application_template(
        self,
    ) -> Callable[
        [authoring_messages.CreateApplicationTemplateRequest],
        Union[authoring.ApplicationTemplate, Awaitable[authoring.ApplicationTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def update_application_template(
        self,
    ) -> Callable[
        [authoring_messages.UpdateApplicationTemplateRequest],
        Union[authoring.ApplicationTemplate, Awaitable[authoring.ApplicationTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def import_application_template(
        self,
    ) -> Callable[
        [authoring_messages.ImportApplicationTemplateRequest],
        Union[authoring.ApplicationTemplate, Awaitable[authoring.ApplicationTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def delete_application_template(
        self,
    ) -> Callable[
        [authoring_messages.DeleteApplicationTemplateRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def commit_application_template(
        self,
    ) -> Callable[
        [authoring_messages.CommitApplicationTemplateRequest],
        Union[
            authoring.ApplicationTemplateRevision,
            Awaitable[authoring.ApplicationTemplateRevision],
        ],
    ]:
        raise NotImplementedError()

    @property
    def snapshot_application_template(
        self,
    ) -> Callable[
        [authoring_messages.SnapshotApplicationTemplateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.GenerateApplicationTemplateIaCRequest],
        Union[
            authoring_messages.GenerateApplicationTemplateIaCResponse,
            Awaitable[authoring_messages.GenerateApplicationTemplateIaCResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def export_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ExportApplicationTemplateIaCRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_application_template_revision_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.GenerateApplicationTemplateRevisionIaCRequest],
        Union[
            authoring_messages.GenerateApplicationTemplateRevisionIaCResponse,
            Awaitable[
                authoring_messages.GenerateApplicationTemplateRevisionIaCResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def export_application_template_revision_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ExportApplicationTemplateRevisionIaCRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_component(
        self,
    ) -> Callable[
        [authoring_messages.GetComponentRequest],
        Union[authoring.Component, Awaitable[authoring.Component]],
    ]:
        raise NotImplementedError()

    @property
    def list_components(
        self,
    ) -> Callable[
        [authoring_messages.ListComponentsRequest],
        Union[
            authoring_messages.ListComponentsResponse,
            Awaitable[authoring_messages.ListComponentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_component(
        self,
    ) -> Callable[
        [authoring_messages.CreateComponentRequest],
        Union[authoring.Component, Awaitable[authoring.Component]],
    ]:
        raise NotImplementedError()

    @property
    def update_component(
        self,
    ) -> Callable[
        [authoring_messages.UpdateComponentRequest],
        Union[authoring.Component, Awaitable[authoring.Component]],
    ]:
        raise NotImplementedError()

    @property
    def delete_component(
        self,
    ) -> Callable[
        [authoring_messages.DeleteComponentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_connection(
        self,
    ) -> Callable[
        [authoring_messages.GetConnectionRequest],
        Union[authoring.Connection, Awaitable[authoring.Connection]],
    ]:
        raise NotImplementedError()

    @property
    def list_connections(
        self,
    ) -> Callable[
        [authoring_messages.ListConnectionsRequest],
        Union[
            authoring_messages.ListConnectionsResponse,
            Awaitable[authoring_messages.ListConnectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_connection(
        self,
    ) -> Callable[
        [authoring_messages.CreateConnectionRequest],
        Union[authoring.Connection, Awaitable[authoring.Connection]],
    ]:
        raise NotImplementedError()

    @property
    def update_connection(
        self,
    ) -> Callable[
        [authoring_messages.UpdateConnectionRequest],
        Union[authoring.Connection, Awaitable[authoring.Connection]],
    ]:
        raise NotImplementedError()

    @property
    def delete_connection(
        self,
    ) -> Callable[
        [authoring_messages.DeleteConnectionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_application_template_revision(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateRevisionRequest],
        Union[
            authoring.ApplicationTemplateRevision,
            Awaitable[authoring.ApplicationTemplateRevision],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_application_template_revisions(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplateRevisionsRequest],
        Union[
            authoring_messages.ListApplicationTemplateRevisionsResponse,
            Awaitable[authoring_messages.ListApplicationTemplateRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_application_template_revision(
        self,
    ) -> Callable[
        [authoring_messages.DeleteApplicationTemplateRevisionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogRequest],
        Union[catalog_management.Catalog, Awaitable[catalog_management.Catalog]],
    ]:
        raise NotImplementedError()

    @property
    def list_catalogs(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogsRequest],
        Union[
            catalog_management_messages.ListCatalogsResponse,
            Awaitable[catalog_management_messages.ListCatalogsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogRequest],
        Union[catalog_management.Catalog, Awaitable[catalog_management.Catalog]],
    ]:
        raise NotImplementedError()

    @property
    def update_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateCatalogRequest],
        Union[catalog_management.Catalog, Awaitable[catalog_management.Catalog]],
    ]:
        raise NotImplementedError()

    @property
    def delete_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogTemplateRequest],
        Union[
            catalog_management.CatalogTemplate,
            Awaitable[catalog_management.CatalogTemplate],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogTemplateRequest],
        Union[
            catalog_management.CatalogTemplate,
            Awaitable[catalog_management.CatalogTemplate],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_catalog_templates(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogTemplatesRequest],
        Union[
            catalog_management_messages.ListCatalogTemplatesResponse,
            Awaitable[catalog_management_messages.ListCatalogTemplatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateCatalogTemplateRequest],
        Union[
            catalog_management.CatalogTemplate,
            Awaitable[catalog_management.CatalogTemplate],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogTemplateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_share(
        self,
    ) -> Callable[
        [sharing_messages.CreateShareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_shares(
        self,
    ) -> Callable[
        [sharing_messages.ListSharesRequest],
        Union[
            sharing_messages.ListSharesResponse,
            Awaitable[sharing_messages.ListSharesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_share(
        self,
    ) -> Callable[
        [sharing_messages.GetShareRequest],
        Union[sharing.Share, Awaitable[sharing.Share]],
    ]:
        raise NotImplementedError()

    @property
    def delete_share(
        self,
    ) -> Callable[
        [sharing_messages.DeleteShareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def sync_share(
        self,
    ) -> Callable[
        [sharing_messages.SyncShareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_shared_template(
        self,
    ) -> Callable[
        [sharing_messages.GetSharedTemplateRequest],
        Union[sharing.SharedTemplate, Awaitable[sharing.SharedTemplate]],
    ]:
        raise NotImplementedError()

    @property
    def list_shared_templates(
        self,
    ) -> Callable[
        [sharing_messages.ListSharedTemplatesRequest],
        Union[
            sharing_messages.ListSharedTemplatesResponse,
            Awaitable[sharing_messages.ListSharedTemplatesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_shared_template_revision(
        self,
    ) -> Callable[
        [sharing_messages.GetSharedTemplateRevisionRequest],
        Union[
            sharing.SharedTemplateRevision, Awaitable[sharing.SharedTemplateRevision]
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_shared_template_revisions(
        self,
    ) -> Callable[
        [sharing_messages.ListSharedTemplateRevisionsRequest],
        Union[
            sharing_messages.ListSharedTemplateRevisionsResponse,
            Awaitable[sharing_messages.ListSharedTemplateRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogTemplateRevisionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogTemplateRevisionRequest],
        Union[
            catalog_management.CatalogTemplateRevision,
            Awaitable[catalog_management.CatalogTemplateRevision],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_catalog_template_revisions(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogTemplateRevisionsRequest],
        Union[
            catalog_management_messages.ListCatalogTemplateRevisionsResponse,
            Awaitable[catalog_management_messages.ListCatalogTemplateRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogTemplateRevisionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_application(
        self,
    ) -> Callable[
        [deployment_messages.CreateApplicationRequest],
        Union[
            deployment_resources.Application,
            Awaitable[deployment_resources.Application],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_application(
        self,
    ) -> Callable[
        [deployment_messages.GetApplicationRequest],
        Union[
            deployment_resources.Application,
            Awaitable[deployment_resources.Application],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_applications(
        self,
    ) -> Callable[
        [deployment_messages.ListApplicationsRequest],
        Union[
            deployment_messages.ListApplicationsResponse,
            Awaitable[deployment_messages.ListApplicationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_application(
        self,
    ) -> Callable[
        [deployment_messages.UpdateApplicationRequest],
        Union[
            deployment_resources.Application,
            Awaitable[deployment_resources.Application],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_application(
        self,
    ) -> Callable[
        [deployment_messages.DeleteApplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def deploy_application(
        self,
    ) -> Callable[
        [deployment_messages.DeployApplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def preview_application(
        self,
    ) -> Callable[
        [deployment_messages.PreviewApplicationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_application_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.FetchApplicationAssessmentReportRequest],
        Union[
            best_practices_messages.FetchApplicationAssessmentReportResponse,
            Awaitable[best_practices_messages.FetchApplicationAssessmentReportResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def generate_application_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateApplicationAssessmentReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_application_template_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateAssessmentReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_terraform_plan_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateTerraformPlanAssessmentReportRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_policy(
        self,
    ) -> Callable[
        [best_practices_messages.GetPolicyRequest],
        Union[best_practices.Policy, Awaitable[best_practices.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def list_policies(
        self,
    ) -> Callable[
        [best_practices_messages.ListPoliciesRequest],
        Union[
            best_practices_messages.ListPoliciesResponse,
            Awaitable[best_practices_messages.ListPoliciesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_policy(
        self,
    ) -> Callable[
        [best_practices_messages.CreatePolicyRequest],
        Union[best_practices.Policy, Awaitable[best_practices.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def update_policy(
        self,
    ) -> Callable[
        [best_practices_messages.UpdatePolicyRequest],
        Union[best_practices.Policy, Awaitable[best_practices.Policy]],
    ]:
        raise NotImplementedError()

    @property
    def delete_policy(
        self,
    ) -> Callable[
        [best_practices_messages.DeletePolicyRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_frameworks(
        self,
    ) -> Callable[
        [best_practices_messages.FetchFrameworksRequest],
        Union[
            best_practices_messages.FetchFrameworksResponse,
            Awaitable[best_practices_messages.FetchFrameworksResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def generate_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.GenerateApplicationIaCRequest],
        Union[
            deployment_messages.GenerateApplicationIaCResponse,
            Awaitable[deployment_messages.GenerateApplicationIaCResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def export_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.ExportApplicationIaCRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ImportApplicationTemplateIaCRequest],
        Union[
            authoring_messages.ImportApplicationTemplateIaCResponse,
            Awaitable[authoring_messages.ImportApplicationTemplateIaCResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def ingest_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.IngestApplicationTemplateIaCRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.ImportApplicationIaCRequest],
        Union[
            deployment_messages.ImportApplicationIaCResponse,
            Awaitable[deployment_messages.ImportApplicationIaCResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def register_app_hub_application_resources(
        self,
    ) -> Callable[
        [apphub_integration_messages.RegisterAppHubApplicationResourcesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_application_template_system_revisions(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplateSystemRevisionsRequest],
        Union[
            authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
            Awaitable[
                authoring_messages.ListApplicationTemplateSystemRevisionsResponse
            ],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_application_template_system_revision(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateSystemRevisionRequest],
        Union[
            authoring.ApplicationTemplateSystemRevision,
            Awaitable[authoring.ApplicationTemplateSystemRevision],
        ],
    ]:
        raise NotImplementedError()

    @property
    def recommend_iam_roles(
        self,
    ) -> Callable[
        [deployment_messages.RecommendIAMRolesRequest],
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


__all__ = ("DesignCenterTransport",)
