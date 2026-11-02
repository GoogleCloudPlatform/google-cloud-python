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

from google.cloud.parametermanager_v1 import gapic_version as package_version
from google.cloud.parametermanager_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.parametermanager_v1._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.parametermanager_v1.types import service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ParameterManagerTransport(abc.ABC):
    """Abstract transport class for ParameterManager."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "parametermanager.googleapis.com"

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
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'parametermanager.googleapis.com').
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
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
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

        self._client_options = client_options
        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _wrap_method(self, func, *args, **kwargs):
        """Wrap an RPC method with common client-level features.

        Applies retry, timeout, metadata, and tracing wrappers to the
        underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method.wrap_method(func, *args, **kwargs)

    def _wrap_async_method(self, func, *args, **kwargs):
        """Wrap an async RPC method with common client-level features.

        Applies asynchronous retry, timeout, metadata, and tracing wrappers
        to the underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _ASYNC_WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method_async.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _ASYNC_WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for RPC dispatch."""
        self._wrapped_methods = {
            self.list_parameters: self._wrap_method(
                self.list_parameters,
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
                method_name="google.cloud.parametermanager.v1.ParameterManager/ListParameters",
            ),
            self.get_parameter: self._wrap_method(
                self.get_parameter,
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
                method_name="google.cloud.parametermanager.v1.ParameterManager/GetParameter",
            ),
            self.create_parameter: self._wrap_method(
                self.create_parameter,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/CreateParameter",
            ),
            self.update_parameter: self._wrap_method(
                self.update_parameter,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/UpdateParameter",
            ),
            self.delete_parameter: self._wrap_method(
                self.delete_parameter,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/DeleteParameter",
            ),
            self.list_parameter_versions: self._wrap_method(
                self.list_parameter_versions,
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
                method_name="google.cloud.parametermanager.v1.ParameterManager/ListParameterVersions",
            ),
            self.get_parameter_version: self._wrap_method(
                self.get_parameter_version,
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
                method_name="google.cloud.parametermanager.v1.ParameterManager/GetParameterVersion",
            ),
            self.render_parameter_version: self._wrap_method(
                self.render_parameter_version,
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
                method_name="google.cloud.parametermanager.v1.ParameterManager/RenderParameterVersion",
            ),
            self.create_parameter_version: self._wrap_method(
                self.create_parameter_version,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/CreateParameterVersion",
            ),
            self.update_parameter_version: self._wrap_method(
                self.update_parameter_version,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/UpdateParameterVersion",
            ),
            self.delete_parameter_version: self._wrap_method(
                self.delete_parameter_version,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/DeleteParameterVersion",
            ),
            self.list_templates: self._wrap_method(
                self.list_templates,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/ListTemplates",
            ),
            self.get_template: self._wrap_method(
                self.get_template,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/GetTemplate",
            ),
            self.create_template: self._wrap_method(
                self.create_template,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/CreateTemplate",
            ),
            self.update_template: self._wrap_method(
                self.update_template,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/UpdateTemplate",
            ),
            self.delete_template: self._wrap_method(
                self.delete_template,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/DeleteTemplate",
            ),
            self.list_template_versions: self._wrap_method(
                self.list_template_versions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/ListTemplateVersions",
            ),
            self.get_template_version: self._wrap_method(
                self.get_template_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/GetTemplateVersion",
            ),
            self.create_template_version: self._wrap_method(
                self.create_template_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/CreateTemplateVersion",
            ),
            self.update_template_version: self._wrap_method(
                self.update_template_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/UpdateTemplateVersion",
            ),
            self.delete_template_version: self._wrap_method(
                self.delete_template_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/DeleteTemplateVersion",
            ),
            self.render_template_version: self._wrap_method(
                self.render_template_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.parametermanager.v1.ParameterManager/RenderTemplateVersion",
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/GetLocation",
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/ListLocations",
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
    def list_parameters(
        self,
    ) -> Callable[
        [service.ListParametersRequest],
        Union[
            service.ListParametersResponse, Awaitable[service.ListParametersResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_parameter(
        self,
    ) -> Callable[
        [service.GetParameterRequest],
        Union[service.Parameter, Awaitable[service.Parameter]],
    ]:
        raise NotImplementedError()

    @property
    def create_parameter(
        self,
    ) -> Callable[
        [service.CreateParameterRequest],
        Union[service.Parameter, Awaitable[service.Parameter]],
    ]:
        raise NotImplementedError()

    @property
    def update_parameter(
        self,
    ) -> Callable[
        [service.UpdateParameterRequest],
        Union[service.Parameter, Awaitable[service.Parameter]],
    ]:
        raise NotImplementedError()

    @property
    def delete_parameter(
        self,
    ) -> Callable[
        [service.DeleteParameterRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_parameter_versions(
        self,
    ) -> Callable[
        [service.ListParameterVersionsRequest],
        Union[
            service.ListParameterVersionsResponse,
            Awaitable[service.ListParameterVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_parameter_version(
        self,
    ) -> Callable[
        [service.GetParameterVersionRequest],
        Union[service.ParameterVersion, Awaitable[service.ParameterVersion]],
    ]:
        raise NotImplementedError()

    @property
    def render_parameter_version(
        self,
    ) -> Callable[
        [service.RenderParameterVersionRequest],
        Union[
            service.RenderParameterVersionResponse,
            Awaitable[service.RenderParameterVersionResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_parameter_version(
        self,
    ) -> Callable[
        [service.CreateParameterVersionRequest],
        Union[service.ParameterVersion, Awaitable[service.ParameterVersion]],
    ]:
        raise NotImplementedError()

    @property
    def update_parameter_version(
        self,
    ) -> Callable[
        [service.UpdateParameterVersionRequest],
        Union[service.ParameterVersion, Awaitable[service.ParameterVersion]],
    ]:
        raise NotImplementedError()

    @property
    def delete_parameter_version(
        self,
    ) -> Callable[
        [service.DeleteParameterVersionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_templates(
        self,
    ) -> Callable[
        [service.ListTemplatesRequest],
        Union[service.ListTemplatesResponse, Awaitable[service.ListTemplatesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_template(
        self,
    ) -> Callable[
        [service.GetTemplateRequest],
        Union[service.Template, Awaitable[service.Template]],
    ]:
        raise NotImplementedError()

    @property
    def create_template(
        self,
    ) -> Callable[
        [service.CreateTemplateRequest],
        Union[service.Template, Awaitable[service.Template]],
    ]:
        raise NotImplementedError()

    @property
    def update_template(
        self,
    ) -> Callable[
        [service.UpdateTemplateRequest],
        Union[service.Template, Awaitable[service.Template]],
    ]:
        raise NotImplementedError()

    @property
    def delete_template(
        self,
    ) -> Callable[
        [service.DeleteTemplateRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_template_versions(
        self,
    ) -> Callable[
        [service.ListTemplateVersionsRequest],
        Union[
            service.ListTemplateVersionsResponse,
            Awaitable[service.ListTemplateVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_template_version(
        self,
    ) -> Callable[
        [service.GetTemplateVersionRequest],
        Union[service.TemplateVersion, Awaitable[service.TemplateVersion]],
    ]:
        raise NotImplementedError()

    @property
    def create_template_version(
        self,
    ) -> Callable[
        [service.CreateTemplateVersionRequest],
        Union[service.TemplateVersion, Awaitable[service.TemplateVersion]],
    ]:
        raise NotImplementedError()

    @property
    def update_template_version(
        self,
    ) -> Callable[
        [service.UpdateTemplateVersionRequest],
        Union[service.TemplateVersion, Awaitable[service.TemplateVersion]],
    ]:
        raise NotImplementedError()

    @property
    def delete_template_version(
        self,
    ) -> Callable[
        [service.DeleteTemplateVersionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def render_template_version(
        self,
    ) -> Callable[
        [service.RenderTemplateVersionRequest],
        Union[
            service.RenderTemplateVersionResponse,
            Awaitable[service.RenderTemplateVersionResponse],
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


__all__ = ("ParameterManagerTransport",)
