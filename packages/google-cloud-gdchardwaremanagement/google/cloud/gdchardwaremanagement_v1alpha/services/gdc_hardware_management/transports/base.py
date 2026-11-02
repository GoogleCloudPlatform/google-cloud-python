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

from google.cloud.gdchardwaremanagement_v1alpha import gapic_version as package_version
from google.cloud.gdchardwaremanagement_v1alpha._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.gdchardwaremanagement_v1alpha._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.gdchardwaremanagement_v1alpha.types import resources, service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class GDCHardwareManagementTransport(abc.ABC):
    """Abstract transport class for GDCHardwareManagement."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "gdchardwaremanagement.googleapis.com"

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
                 The hostname to connect to (default: 'gdchardwaremanagement.googleapis.com').
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
            self.list_orders: self._wrap_method(
                self.list_orders,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListOrders",
            ),
            self.get_order: self._wrap_method(
                self.get_order,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetOrder",
            ),
            self.create_order: self._wrap_method(
                self.create_order,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateOrder",
            ),
            self.update_order: self._wrap_method(
                self.update_order,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateOrder",
            ),
            self.delete_order: self._wrap_method(
                self.delete_order,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteOrder",
            ),
            self.submit_order: self._wrap_method(
                self.submit_order,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SubmitOrder",
            ),
            self.cancel_order: self._wrap_method(
                self.cancel_order,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CancelOrder",
            ),
            self.list_sites: self._wrap_method(
                self.list_sites,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSites",
            ),
            self.get_site: self._wrap_method(
                self.get_site,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSite",
            ),
            self.create_site: self._wrap_method(
                self.create_site,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateSite",
            ),
            self.update_site: self._wrap_method(
                self.update_site,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateSite",
            ),
            self.delete_site: self._wrap_method(
                self.delete_site,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteSite",
            ),
            self.list_hardware_groups: self._wrap_method(
                self.list_hardware_groups,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardwareGroups",
            ),
            self.get_hardware_group: self._wrap_method(
                self.get_hardware_group,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardwareGroup",
            ),
            self.create_hardware_group: self._wrap_method(
                self.create_hardware_group,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardwareGroup",
            ),
            self.update_hardware_group: self._wrap_method(
                self.update_hardware_group,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardwareGroup",
            ),
            self.delete_hardware_group: self._wrap_method(
                self.delete_hardware_group,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardwareGroup",
            ),
            self.list_hardware: self._wrap_method(
                self.list_hardware,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListHardware",
            ),
            self.get_hardware: self._wrap_method(
                self.get_hardware,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetHardware",
            ),
            self.create_hardware: self._wrap_method(
                self.create_hardware,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateHardware",
            ),
            self.update_hardware: self._wrap_method(
                self.update_hardware,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateHardware",
            ),
            self.delete_hardware: self._wrap_method(
                self.delete_hardware,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteHardware",
            ),
            self.list_comments: self._wrap_method(
                self.list_comments,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListComments",
            ),
            self.get_comment: self._wrap_method(
                self.get_comment,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetComment",
            ),
            self.create_comment: self._wrap_method(
                self.create_comment,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateComment",
            ),
            self.record_action_on_comment: self._wrap_method(
                self.record_action_on_comment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/RecordActionOnComment",
            ),
            self.list_change_log_entries: self._wrap_method(
                self.list_change_log_entries,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListChangeLogEntries",
            ),
            self.get_change_log_entry: self._wrap_method(
                self.get_change_log_entry,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetChangeLogEntry",
            ),
            self.list_skus: self._wrap_method(
                self.list_skus,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListSkus",
            ),
            self.get_sku: self._wrap_method(
                self.get_sku,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetSku",
            ),
            self.list_zones: self._wrap_method(
                self.list_zones,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/ListZones",
            ),
            self.get_zone: self._wrap_method(
                self.get_zone,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/GetZone",
            ),
            self.create_zone: self._wrap_method(
                self.create_zone,
                default_timeout=60.0,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/CreateZone",
            ),
            self.update_zone: self._wrap_method(
                self.update_zone,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/UpdateZone",
            ),
            self.delete_zone: self._wrap_method(
                self.delete_zone,
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
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/DeleteZone",
            ),
            self.signal_zone_state: self._wrap_method(
                self.signal_zone_state,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/SignalZoneState",
            ),
            self.request_order_date_change: self._wrap_method(
                self.request_order_date_change,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagement/RequestOrderDateChange",
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
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/CancelOperation",
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/DeleteOperation",
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
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
    def list_orders(
        self,
    ) -> Callable[
        [service.ListOrdersRequest],
        Union[service.ListOrdersResponse, Awaitable[service.ListOrdersResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_order(
        self,
    ) -> Callable[
        [service.GetOrderRequest], Union[resources.Order, Awaitable[resources.Order]]
    ]:
        raise NotImplementedError()

    @property
    def create_order(
        self,
    ) -> Callable[
        [service.CreateOrderRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_order(
        self,
    ) -> Callable[
        [service.UpdateOrderRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_order(
        self,
    ) -> Callable[
        [service.DeleteOrderRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def submit_order(
        self,
    ) -> Callable[
        [service.SubmitOrderRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_order(
        self,
    ) -> Callable[
        [service.CancelOrderRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_sites(
        self,
    ) -> Callable[
        [service.ListSitesRequest],
        Union[service.ListSitesResponse, Awaitable[service.ListSitesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_site(
        self,
    ) -> Callable[
        [service.GetSiteRequest], Union[resources.Site, Awaitable[resources.Site]]
    ]:
        raise NotImplementedError()

    @property
    def create_site(
        self,
    ) -> Callable[
        [service.CreateSiteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_site(
        self,
    ) -> Callable[
        [service.UpdateSiteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_site(
        self,
    ) -> Callable[
        [service.DeleteSiteRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_hardware_groups(
        self,
    ) -> Callable[
        [service.ListHardwareGroupsRequest],
        Union[
            service.ListHardwareGroupsResponse,
            Awaitable[service.ListHardwareGroupsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_hardware_group(
        self,
    ) -> Callable[
        [service.GetHardwareGroupRequest],
        Union[resources.HardwareGroup, Awaitable[resources.HardwareGroup]],
    ]:
        raise NotImplementedError()

    @property
    def create_hardware_group(
        self,
    ) -> Callable[
        [service.CreateHardwareGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_hardware_group(
        self,
    ) -> Callable[
        [service.UpdateHardwareGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_hardware_group(
        self,
    ) -> Callable[
        [service.DeleteHardwareGroupRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_hardware(
        self,
    ) -> Callable[
        [service.ListHardwareRequest],
        Union[service.ListHardwareResponse, Awaitable[service.ListHardwareResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_hardware(
        self,
    ) -> Callable[
        [service.GetHardwareRequest],
        Union[resources.Hardware, Awaitable[resources.Hardware]],
    ]:
        raise NotImplementedError()

    @property
    def create_hardware(
        self,
    ) -> Callable[
        [service.CreateHardwareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_hardware(
        self,
    ) -> Callable[
        [service.UpdateHardwareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_hardware(
        self,
    ) -> Callable[
        [service.DeleteHardwareRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_comments(
        self,
    ) -> Callable[
        [service.ListCommentsRequest],
        Union[service.ListCommentsResponse, Awaitable[service.ListCommentsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_comment(
        self,
    ) -> Callable[
        [service.GetCommentRequest],
        Union[resources.Comment, Awaitable[resources.Comment]],
    ]:
        raise NotImplementedError()

    @property
    def create_comment(
        self,
    ) -> Callable[
        [service.CreateCommentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def record_action_on_comment(
        self,
    ) -> Callable[
        [service.RecordActionOnCommentRequest],
        Union[resources.Comment, Awaitable[resources.Comment]],
    ]:
        raise NotImplementedError()

    @property
    def list_change_log_entries(
        self,
    ) -> Callable[
        [service.ListChangeLogEntriesRequest],
        Union[
            service.ListChangeLogEntriesResponse,
            Awaitable[service.ListChangeLogEntriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_change_log_entry(
        self,
    ) -> Callable[
        [service.GetChangeLogEntryRequest],
        Union[resources.ChangeLogEntry, Awaitable[resources.ChangeLogEntry]],
    ]:
        raise NotImplementedError()

    @property
    def list_skus(
        self,
    ) -> Callable[
        [service.ListSkusRequest],
        Union[service.ListSkusResponse, Awaitable[service.ListSkusResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_sku(
        self,
    ) -> Callable[
        [service.GetSkuRequest], Union[resources.Sku, Awaitable[resources.Sku]]
    ]:
        raise NotImplementedError()

    @property
    def list_zones(
        self,
    ) -> Callable[
        [service.ListZonesRequest],
        Union[service.ListZonesResponse, Awaitable[service.ListZonesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_zone(
        self,
    ) -> Callable[
        [service.GetZoneRequest], Union[resources.Zone, Awaitable[resources.Zone]]
    ]:
        raise NotImplementedError()

    @property
    def create_zone(
        self,
    ) -> Callable[
        [service.CreateZoneRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_zone(
        self,
    ) -> Callable[
        [service.UpdateZoneRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_zone(
        self,
    ) -> Callable[
        [service.DeleteZoneRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def signal_zone_state(
        self,
    ) -> Callable[
        [service.SignalZoneStateRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def request_order_date_change(
        self,
    ) -> Callable[
        [service.RequestOrderDateChangeRequest],
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


__all__ = ("GDCHardwareManagementTransport",)
