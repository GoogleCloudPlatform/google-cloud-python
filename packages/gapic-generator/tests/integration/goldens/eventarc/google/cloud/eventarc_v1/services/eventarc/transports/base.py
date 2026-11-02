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

from google.cloud.eventarc_v1 import gapic_version as package_version
from google.cloud.eventarc_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)
_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.auth  # type: ignore
import google.api_core
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import operations_v1
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account # type: ignore
import google.protobuf

from google.cloud.eventarc_v1.types import channel
from google.cloud.eventarc_v1.types import channel_connection
from google.cloud.eventarc_v1.types import discovery
from google.cloud.eventarc_v1.types import enrollment
from google.cloud.eventarc_v1.types import eventarc
from google.cloud.eventarc_v1.types import google_api_source
from google.cloud.eventarc_v1.types import google_channel_config
from google.cloud.eventarc_v1.types import google_channel_config as gce_google_channel_config
from google.cloud.eventarc_v1.types import message_bus
from google.cloud.eventarc_v1.types import pipeline
from google.cloud.eventarc_v1.types import trigger
from google.cloud.location import locations_pb2 # type: ignore
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2 # type: ignore

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(gapic_version=package_version.__version__)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class EventarcTransport(abc.ABC):
    """Abstract transport class for Eventarc."""

    AUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    DEFAULT_HOST: str = 'eventarc.googleapis.com'

    def __init__(
            self, *,
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
                 The hostname to connect to (default: 'eventarc.googleapis.com').
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
            raise core_exceptions.DuplicateCredentialArgs("'credentials_file' and 'credentials' are mutually exclusive")

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                                credentials_file,
                                scopes=scopes,
                                quota_project_id=quota_project_id,
                                default_scopes=self.AUTH_SCOPES,
                            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(scopes=scopes, quota_project_id=quota_project_id, default_scopes=self.AUTH_SCOPES)
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(api_audience if api_audience else host)

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if always_use_jwt_access and isinstance(credentials, service_account.Credentials) and hasattr(service_account.Credentials, "with_always_use_jwt_access"):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ':' not in host:
            host += ':443'
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
            self.get_trigger: self._wrap_method(
                self.get_trigger,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetTrigger",
            ),
            self.list_triggers: self._wrap_method(
                self.list_triggers,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListTriggers",
            ),
            self.create_trigger: self._wrap_method(
                self.create_trigger,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreateTrigger",
            ),
            self.update_trigger: self._wrap_method(
                self.update_trigger,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdateTrigger",
            ),
            self.delete_trigger: self._wrap_method(
                self.delete_trigger,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeleteTrigger",
            ),
            self.get_channel: self._wrap_method(
                self.get_channel,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetChannel",
            ),
            self.list_channels: self._wrap_method(
                self.list_channels,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListChannels",
            ),
            self.create_channel_: self._wrap_method(
                self.create_channel_,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreateChannel",
            ),
            self.update_channel: self._wrap_method(
                self.update_channel,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdateChannel",
            ),
            self.delete_channel: self._wrap_method(
                self.delete_channel,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeleteChannel",
            ),
            self.get_provider: self._wrap_method(
                self.get_provider,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetProvider",
            ),
            self.list_providers: self._wrap_method(
                self.list_providers,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListProviders",
            ),
            self.get_channel_connection: self._wrap_method(
                self.get_channel_connection,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetChannelConnection",
            ),
            self.list_channel_connections: self._wrap_method(
                self.list_channel_connections,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListChannelConnections",
            ),
            self.create_channel_connection: self._wrap_method(
                self.create_channel_connection,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreateChannelConnection",
            ),
            self.delete_channel_connection: self._wrap_method(
                self.delete_channel_connection,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeleteChannelConnection",
            ),
            self.get_google_channel_config: self._wrap_method(
                self.get_google_channel_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetGoogleChannelConfig",
            ),
            self.update_google_channel_config: self._wrap_method(
                self.update_google_channel_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdateGoogleChannelConfig",
            ),
            self.get_message_bus: self._wrap_method(
                self.get_message_bus,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetMessageBus",
            ),
            self.list_message_buses: self._wrap_method(
                self.list_message_buses,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListMessageBuses",
            ),
            self.list_message_bus_enrollments: self._wrap_method(
                self.list_message_bus_enrollments,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListMessageBusEnrollments",
            ),
            self.create_message_bus: self._wrap_method(
                self.create_message_bus,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreateMessageBus",
            ),
            self.update_message_bus: self._wrap_method(
                self.update_message_bus,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdateMessageBus",
            ),
            self.delete_message_bus: self._wrap_method(
                self.delete_message_bus,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeleteMessageBus",
            ),
            self.get_enrollment: self._wrap_method(
                self.get_enrollment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetEnrollment",
            ),
            self.list_enrollments: self._wrap_method(
                self.list_enrollments,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListEnrollments",
            ),
            self.create_enrollment: self._wrap_method(
                self.create_enrollment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreateEnrollment",
            ),
            self.update_enrollment: self._wrap_method(
                self.update_enrollment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdateEnrollment",
            ),
            self.delete_enrollment: self._wrap_method(
                self.delete_enrollment,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeleteEnrollment",
            ),
            self.get_pipeline: self._wrap_method(
                self.get_pipeline,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetPipeline",
            ),
            self.list_pipelines: self._wrap_method(
                self.list_pipelines,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListPipelines",
            ),
            self.create_pipeline: self._wrap_method(
                self.create_pipeline,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreatePipeline",
            ),
            self.update_pipeline: self._wrap_method(
                self.update_pipeline,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdatePipeline",
            ),
            self.delete_pipeline: self._wrap_method(
                self.delete_pipeline,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeletePipeline",
            ),
            self.get_google_api_source: self._wrap_method(
                self.get_google_api_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/GetGoogleApiSource",
            ),
            self.list_google_api_sources: self._wrap_method(
                self.list_google_api_sources,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/ListGoogleApiSources",
            ),
            self.create_google_api_source: self._wrap_method(
                self.create_google_api_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/CreateGoogleApiSource",
            ),
            self.update_google_api_source: self._wrap_method(
                self.update_google_api_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/UpdateGoogleApiSource",
            ),
            self.delete_google_api_source: self._wrap_method(
                self.delete_google_api_source,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.eventarc.v1.Eventarc/DeleteGoogleApiSource",
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
            self.get_iam_policy: self._wrap_method(
                self.get_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/GetIamPolicy",
            ),
            self.set_iam_policy: self._wrap_method(
                self.set_iam_policy,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/SetIamPolicy",
            ),
            self.test_iam_permissions: self._wrap_method(
                self.test_iam_permissions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.iam.v1.IAMPolicy/TestIamPermissions",
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
    def get_trigger(self) -> Callable[
            [eventarc.GetTriggerRequest],
            Union[
                trigger.Trigger,
                Awaitable[trigger.Trigger]
            ]]:
        raise NotImplementedError()

    @property
    def list_triggers(self) -> Callable[
            [eventarc.ListTriggersRequest],
            Union[
                eventarc.ListTriggersResponse,
                Awaitable[eventarc.ListTriggersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_trigger(self) -> Callable[
            [eventarc.CreateTriggerRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_trigger(self) -> Callable[
            [eventarc.UpdateTriggerRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_trigger(self) -> Callable[
            [eventarc.DeleteTriggerRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_channel(self) -> Callable[
            [eventarc.GetChannelRequest],
            Union[
                channel.Channel,
                Awaitable[channel.Channel]
            ]]:
        raise NotImplementedError()

    @property
    def list_channels(self) -> Callable[
            [eventarc.ListChannelsRequest],
            Union[
                eventarc.ListChannelsResponse,
                Awaitable[eventarc.ListChannelsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_channel_(self) -> Callable[
            [eventarc.CreateChannelRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_channel(self) -> Callable[
            [eventarc.UpdateChannelRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_channel(self) -> Callable[
            [eventarc.DeleteChannelRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_provider(self) -> Callable[
            [eventarc.GetProviderRequest],
            Union[
                discovery.Provider,
                Awaitable[discovery.Provider]
            ]]:
        raise NotImplementedError()

    @property
    def list_providers(self) -> Callable[
            [eventarc.ListProvidersRequest],
            Union[
                eventarc.ListProvidersResponse,
                Awaitable[eventarc.ListProvidersResponse]
            ]]:
        raise NotImplementedError()

    @property
    def get_channel_connection(self) -> Callable[
            [eventarc.GetChannelConnectionRequest],
            Union[
                channel_connection.ChannelConnection,
                Awaitable[channel_connection.ChannelConnection]
            ]]:
        raise NotImplementedError()

    @property
    def list_channel_connections(self) -> Callable[
            [eventarc.ListChannelConnectionsRequest],
            Union[
                eventarc.ListChannelConnectionsResponse,
                Awaitable[eventarc.ListChannelConnectionsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_channel_connection(self) -> Callable[
            [eventarc.CreateChannelConnectionRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_channel_connection(self) -> Callable[
            [eventarc.DeleteChannelConnectionRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_google_channel_config(self) -> Callable[
            [eventarc.GetGoogleChannelConfigRequest],
            Union[
                google_channel_config.GoogleChannelConfig,
                Awaitable[google_channel_config.GoogleChannelConfig]
            ]]:
        raise NotImplementedError()

    @property
    def update_google_channel_config(self) -> Callable[
            [eventarc.UpdateGoogleChannelConfigRequest],
            Union[
                gce_google_channel_config.GoogleChannelConfig,
                Awaitable[gce_google_channel_config.GoogleChannelConfig]
            ]]:
        raise NotImplementedError()

    @property
    def get_message_bus(self) -> Callable[
            [eventarc.GetMessageBusRequest],
            Union[
                message_bus.MessageBus,
                Awaitable[message_bus.MessageBus]
            ]]:
        raise NotImplementedError()

    @property
    def list_message_buses(self) -> Callable[
            [eventarc.ListMessageBusesRequest],
            Union[
                eventarc.ListMessageBusesResponse,
                Awaitable[eventarc.ListMessageBusesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def list_message_bus_enrollments(self) -> Callable[
            [eventarc.ListMessageBusEnrollmentsRequest],
            Union[
                eventarc.ListMessageBusEnrollmentsResponse,
                Awaitable[eventarc.ListMessageBusEnrollmentsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_message_bus(self) -> Callable[
            [eventarc.CreateMessageBusRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_message_bus(self) -> Callable[
            [eventarc.UpdateMessageBusRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_message_bus(self) -> Callable[
            [eventarc.DeleteMessageBusRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_enrollment(self) -> Callable[
            [eventarc.GetEnrollmentRequest],
            Union[
                enrollment.Enrollment,
                Awaitable[enrollment.Enrollment]
            ]]:
        raise NotImplementedError()

    @property
    def list_enrollments(self) -> Callable[
            [eventarc.ListEnrollmentsRequest],
            Union[
                eventarc.ListEnrollmentsResponse,
                Awaitable[eventarc.ListEnrollmentsResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_enrollment(self) -> Callable[
            [eventarc.CreateEnrollmentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_enrollment(self) -> Callable[
            [eventarc.UpdateEnrollmentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_enrollment(self) -> Callable[
            [eventarc.DeleteEnrollmentRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_pipeline(self) -> Callable[
            [eventarc.GetPipelineRequest],
            Union[
                pipeline.Pipeline,
                Awaitable[pipeline.Pipeline]
            ]]:
        raise NotImplementedError()

    @property
    def list_pipelines(self) -> Callable[
            [eventarc.ListPipelinesRequest],
            Union[
                eventarc.ListPipelinesResponse,
                Awaitable[eventarc.ListPipelinesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_pipeline(self) -> Callable[
            [eventarc.CreatePipelineRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_pipeline(self) -> Callable[
            [eventarc.UpdatePipelineRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_pipeline(self) -> Callable[
            [eventarc.DeletePipelineRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def get_google_api_source(self) -> Callable[
            [eventarc.GetGoogleApiSourceRequest],
            Union[
                google_api_source.GoogleApiSource,
                Awaitable[google_api_source.GoogleApiSource]
            ]]:
        raise NotImplementedError()

    @property
    def list_google_api_sources(self) -> Callable[
            [eventarc.ListGoogleApiSourcesRequest],
            Union[
                eventarc.ListGoogleApiSourcesResponse,
                Awaitable[eventarc.ListGoogleApiSourcesResponse]
            ]]:
        raise NotImplementedError()

    @property
    def create_google_api_source(self) -> Callable[
            [eventarc.CreateGoogleApiSourceRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def update_google_api_source(self) -> Callable[
            [eventarc.UpdateGoogleApiSourceRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def delete_google_api_source(self) -> Callable[
            [eventarc.DeleteGoogleApiSourceRequest],
            Union[
                operations_pb2.Operation,
                Awaitable[operations_pb2.Operation]
            ]]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[operations_pb2.ListOperationsResponse, Awaitable[operations_pb2.ListOperationsResponse]],
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
    def get_location(self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[locations_pb2.ListLocationsResponse, Awaitable[locations_pb2.ListLocationsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = (
    'EventarcTransport',
)
