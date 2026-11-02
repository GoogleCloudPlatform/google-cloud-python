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
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.apihub_v1 import gapic_version as package_version
from google.cloud.apihub_v1.types import apihub_service, common_fields

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ApiHubTransport(abc.ABC):
    """Abstract transport class for ApiHub."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "apihub.googleapis.com"

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
                 The hostname to connect to (default: 'apihub.googleapis.com').
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
            self.create_api: gapic_v1.method.wrap_method(
                self.create_api,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_api: gapic_v1.method.wrap_method(
                self.get_api,
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
            self.list_apis: gapic_v1.method.wrap_method(
                self.list_apis,
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
            self.update_api: gapic_v1.method.wrap_method(
                self.update_api,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_api: gapic_v1.method.wrap_method(
                self.delete_api,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_version: gapic_v1.method.wrap_method(
                self.create_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_version: gapic_v1.method.wrap_method(
                self.get_version,
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
            self.list_versions: gapic_v1.method.wrap_method(
                self.list_versions,
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
            self.update_version: gapic_v1.method.wrap_method(
                self.update_version,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_version: gapic_v1.method.wrap_method(
                self.delete_version,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_spec: gapic_v1.method.wrap_method(
                self.create_spec,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_spec: gapic_v1.method.wrap_method(
                self.get_spec,
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
            self.get_spec_contents: gapic_v1.method.wrap_method(
                self.get_spec_contents,
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
            self.list_specs: gapic_v1.method.wrap_method(
                self.list_specs,
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
            self.update_spec: gapic_v1.method.wrap_method(
                self.update_spec,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_spec: gapic_v1.method.wrap_method(
                self.delete_spec,
                default_timeout=300.0,
                client_info=client_info,
            ),
            self.create_api_operation: gapic_v1.method.wrap_method(
                self.create_api_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_api_operation: gapic_v1.method.wrap_method(
                self.get_api_operation,
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
            self.list_api_operations: gapic_v1.method.wrap_method(
                self.list_api_operations,
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
            self.update_api_operation: gapic_v1.method.wrap_method(
                self.update_api_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_api_operation: gapic_v1.method.wrap_method(
                self.delete_api_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_definition: gapic_v1.method.wrap_method(
                self.get_definition,
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
            self.create_deployment: gapic_v1.method.wrap_method(
                self.create_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_deployment: gapic_v1.method.wrap_method(
                self.get_deployment,
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
            self.list_deployments: gapic_v1.method.wrap_method(
                self.list_deployments,
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
            self.update_deployment: gapic_v1.method.wrap_method(
                self.update_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_deployment: gapic_v1.method.wrap_method(
                self.delete_deployment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_attribute: gapic_v1.method.wrap_method(
                self.create_attribute,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_attribute: gapic_v1.method.wrap_method(
                self.get_attribute,
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
            self.update_attribute: gapic_v1.method.wrap_method(
                self.update_attribute,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_attribute: gapic_v1.method.wrap_method(
                self.delete_attribute,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_attributes: gapic_v1.method.wrap_method(
                self.list_attributes,
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
            self.search_resources: gapic_v1.method.wrap_method(
                self.search_resources,
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
            self.create_external_api: gapic_v1.method.wrap_method(
                self.create_external_api,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_external_api: gapic_v1.method.wrap_method(
                self.get_external_api,
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
            self.update_external_api: gapic_v1.method.wrap_method(
                self.update_external_api,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_external_api: gapic_v1.method.wrap_method(
                self.delete_external_api,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_external_apis: gapic_v1.method.wrap_method(
                self.list_external_apis,
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
    def create_api(
        self,
    ) -> Callable[
        [apihub_service.CreateApiRequest],
        Union[common_fields.Api, Awaitable[common_fields.Api]],
    ]:
        raise NotImplementedError()

    @property
    def get_api(
        self,
    ) -> Callable[
        [apihub_service.GetApiRequest],
        Union[common_fields.Api, Awaitable[common_fields.Api]],
    ]:
        raise NotImplementedError()

    @property
    def list_apis(
        self,
    ) -> Callable[
        [apihub_service.ListApisRequest],
        Union[
            apihub_service.ListApisResponse, Awaitable[apihub_service.ListApisResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_api(
        self,
    ) -> Callable[
        [apihub_service.UpdateApiRequest],
        Union[common_fields.Api, Awaitable[common_fields.Api]],
    ]:
        raise NotImplementedError()

    @property
    def delete_api(
        self,
    ) -> Callable[
        [apihub_service.DeleteApiRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_version(
        self,
    ) -> Callable[
        [apihub_service.CreateVersionRequest],
        Union[common_fields.Version, Awaitable[common_fields.Version]],
    ]:
        raise NotImplementedError()

    @property
    def get_version(
        self,
    ) -> Callable[
        [apihub_service.GetVersionRequest],
        Union[common_fields.Version, Awaitable[common_fields.Version]],
    ]:
        raise NotImplementedError()

    @property
    def list_versions(
        self,
    ) -> Callable[
        [apihub_service.ListVersionsRequest],
        Union[
            apihub_service.ListVersionsResponse,
            Awaitable[apihub_service.ListVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_version(
        self,
    ) -> Callable[
        [apihub_service.UpdateVersionRequest],
        Union[common_fields.Version, Awaitable[common_fields.Version]],
    ]:
        raise NotImplementedError()

    @property
    def delete_version(
        self,
    ) -> Callable[
        [apihub_service.DeleteVersionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_spec(
        self,
    ) -> Callable[
        [apihub_service.CreateSpecRequest],
        Union[common_fields.Spec, Awaitable[common_fields.Spec]],
    ]:
        raise NotImplementedError()

    @property
    def get_spec(
        self,
    ) -> Callable[
        [apihub_service.GetSpecRequest],
        Union[common_fields.Spec, Awaitable[common_fields.Spec]],
    ]:
        raise NotImplementedError()

    @property
    def get_spec_contents(
        self,
    ) -> Callable[
        [apihub_service.GetSpecContentsRequest],
        Union[common_fields.SpecContents, Awaitable[common_fields.SpecContents]],
    ]:
        raise NotImplementedError()

    @property
    def list_specs(
        self,
    ) -> Callable[
        [apihub_service.ListSpecsRequest],
        Union[
            apihub_service.ListSpecsResponse,
            Awaitable[apihub_service.ListSpecsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_spec(
        self,
    ) -> Callable[
        [apihub_service.UpdateSpecRequest],
        Union[common_fields.Spec, Awaitable[common_fields.Spec]],
    ]:
        raise NotImplementedError()

    @property
    def delete_spec(
        self,
    ) -> Callable[
        [apihub_service.DeleteSpecRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_api_operation(
        self,
    ) -> Callable[
        [apihub_service.CreateApiOperationRequest],
        Union[common_fields.ApiOperation, Awaitable[common_fields.ApiOperation]],
    ]:
        raise NotImplementedError()

    @property
    def get_api_operation(
        self,
    ) -> Callable[
        [apihub_service.GetApiOperationRequest],
        Union[common_fields.ApiOperation, Awaitable[common_fields.ApiOperation]],
    ]:
        raise NotImplementedError()

    @property
    def list_api_operations(
        self,
    ) -> Callable[
        [apihub_service.ListApiOperationsRequest],
        Union[
            apihub_service.ListApiOperationsResponse,
            Awaitable[apihub_service.ListApiOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_api_operation(
        self,
    ) -> Callable[
        [apihub_service.UpdateApiOperationRequest],
        Union[common_fields.ApiOperation, Awaitable[common_fields.ApiOperation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_api_operation(
        self,
    ) -> Callable[
        [apihub_service.DeleteApiOperationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_definition(
        self,
    ) -> Callable[
        [apihub_service.GetDefinitionRequest],
        Union[common_fields.Definition, Awaitable[common_fields.Definition]],
    ]:
        raise NotImplementedError()

    @property
    def create_deployment(
        self,
    ) -> Callable[
        [apihub_service.CreateDeploymentRequest],
        Union[common_fields.Deployment, Awaitable[common_fields.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def get_deployment(
        self,
    ) -> Callable[
        [apihub_service.GetDeploymentRequest],
        Union[common_fields.Deployment, Awaitable[common_fields.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def list_deployments(
        self,
    ) -> Callable[
        [apihub_service.ListDeploymentsRequest],
        Union[
            apihub_service.ListDeploymentsResponse,
            Awaitable[apihub_service.ListDeploymentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_deployment(
        self,
    ) -> Callable[
        [apihub_service.UpdateDeploymentRequest],
        Union[common_fields.Deployment, Awaitable[common_fields.Deployment]],
    ]:
        raise NotImplementedError()

    @property
    def delete_deployment(
        self,
    ) -> Callable[
        [apihub_service.DeleteDeploymentRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_attribute(
        self,
    ) -> Callable[
        [apihub_service.CreateAttributeRequest],
        Union[common_fields.Attribute, Awaitable[common_fields.Attribute]],
    ]:
        raise NotImplementedError()

    @property
    def get_attribute(
        self,
    ) -> Callable[
        [apihub_service.GetAttributeRequest],
        Union[common_fields.Attribute, Awaitable[common_fields.Attribute]],
    ]:
        raise NotImplementedError()

    @property
    def update_attribute(
        self,
    ) -> Callable[
        [apihub_service.UpdateAttributeRequest],
        Union[common_fields.Attribute, Awaitable[common_fields.Attribute]],
    ]:
        raise NotImplementedError()

    @property
    def delete_attribute(
        self,
    ) -> Callable[
        [apihub_service.DeleteAttributeRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_attributes(
        self,
    ) -> Callable[
        [apihub_service.ListAttributesRequest],
        Union[
            apihub_service.ListAttributesResponse,
            Awaitable[apihub_service.ListAttributesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_resources(
        self,
    ) -> Callable[
        [apihub_service.SearchResourcesRequest],
        Union[
            apihub_service.SearchResourcesResponse,
            Awaitable[apihub_service.SearchResourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_external_api(
        self,
    ) -> Callable[
        [apihub_service.CreateExternalApiRequest],
        Union[common_fields.ExternalApi, Awaitable[common_fields.ExternalApi]],
    ]:
        raise NotImplementedError()

    @property
    def get_external_api(
        self,
    ) -> Callable[
        [apihub_service.GetExternalApiRequest],
        Union[common_fields.ExternalApi, Awaitable[common_fields.ExternalApi]],
    ]:
        raise NotImplementedError()

    @property
    def update_external_api(
        self,
    ) -> Callable[
        [apihub_service.UpdateExternalApiRequest],
        Union[common_fields.ExternalApi, Awaitable[common_fields.ExternalApi]],
    ]:
        raise NotImplementedError()

    @property
    def delete_external_api(
        self,
    ) -> Callable[
        [apihub_service.DeleteExternalApiRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_external_apis(
        self,
    ) -> Callable[
        [apihub_service.ListExternalApisRequest],
        Union[
            apihub_service.ListExternalApisResponse,
            Awaitable[apihub_service.ListExternalApisResponse],
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


__all__ = ("ApiHubTransport",)
