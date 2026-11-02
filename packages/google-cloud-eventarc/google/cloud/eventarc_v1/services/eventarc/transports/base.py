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

from google.cloud.eventarc_v1 import gapic_version as package_version
from google.cloud.eventarc_v1.types import (
    channel,
    channel_connection,
    discovery,
    enrollment,
    eventarc,
    google_api_source,
    google_channel_config,
    message_bus,
    pipeline,
    trigger,
)
from google.cloud.eventarc_v1.types import (
    google_channel_config as gce_google_channel_config,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class EventarcTransport(abc.ABC):
    """Abstract transport class for Eventarc."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "eventarc.googleapis.com"

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
            self.get_trigger: gapic_v1.method.wrap_method(
                self.get_trigger,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_triggers: gapic_v1.method.wrap_method(
                self.list_triggers,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_trigger: gapic_v1.method.wrap_method(
                self.create_trigger,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_trigger: gapic_v1.method.wrap_method(
                self.update_trigger,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_trigger: gapic_v1.method.wrap_method(
                self.delete_trigger,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_channel: gapic_v1.method.wrap_method(
                self.get_channel,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_channels: gapic_v1.method.wrap_method(
                self.list_channels,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_channel_: gapic_v1.method.wrap_method(
                self.create_channel_,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_channel: gapic_v1.method.wrap_method(
                self.update_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_channel: gapic_v1.method.wrap_method(
                self.delete_channel,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_provider: gapic_v1.method.wrap_method(
                self.get_provider,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_providers: gapic_v1.method.wrap_method(
                self.list_providers,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_channel_connection: gapic_v1.method.wrap_method(
                self.get_channel_connection,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_channel_connections: gapic_v1.method.wrap_method(
                self.list_channel_connections,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_channel_connection: gapic_v1.method.wrap_method(
                self.create_channel_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_channel_connection: gapic_v1.method.wrap_method(
                self.delete_channel_connection,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_google_channel_config: gapic_v1.method.wrap_method(
                self.get_google_channel_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_google_channel_config: gapic_v1.method.wrap_method(
                self.update_google_channel_config,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_message_bus: gapic_v1.method.wrap_method(
                self.get_message_bus,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_message_buses: gapic_v1.method.wrap_method(
                self.list_message_buses,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_message_bus_enrollments: gapic_v1.method.wrap_method(
                self.list_message_bus_enrollments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_message_bus: gapic_v1.method.wrap_method(
                self.create_message_bus,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_message_bus: gapic_v1.method.wrap_method(
                self.update_message_bus,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_message_bus: gapic_v1.method.wrap_method(
                self.delete_message_bus,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_enrollment: gapic_v1.method.wrap_method(
                self.get_enrollment,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_enrollments: gapic_v1.method.wrap_method(
                self.list_enrollments,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_enrollment: gapic_v1.method.wrap_method(
                self.create_enrollment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_enrollment: gapic_v1.method.wrap_method(
                self.update_enrollment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_enrollment: gapic_v1.method.wrap_method(
                self.delete_enrollment,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_pipeline: gapic_v1.method.wrap_method(
                self.get_pipeline,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_pipelines: gapic_v1.method.wrap_method(
                self.list_pipelines,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_pipeline: gapic_v1.method.wrap_method(
                self.create_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_pipeline: gapic_v1.method.wrap_method(
                self.update_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_pipeline: gapic_v1.method.wrap_method(
                self.delete_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_google_api_source: gapic_v1.method.wrap_method(
                self.get_google_api_source,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_google_api_sources: gapic_v1.method.wrap_method(
                self.list_google_api_sources,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                        core_exceptions.Unknown,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_google_api_source: gapic_v1.method.wrap_method(
                self.create_google_api_source,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_google_api_source: gapic_v1.method.wrap_method(
                self.update_google_api_source,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_google_api_source: gapic_v1.method.wrap_method(
                self.delete_google_api_source,
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
    def get_trigger(
        self,
    ) -> Callable[
        [eventarc.GetTriggerRequest], Union[trigger.Trigger, Awaitable[trigger.Trigger]]
    ]:
        raise NotImplementedError()

    @property
    def list_triggers(
        self,
    ) -> Callable[
        [eventarc.ListTriggersRequest],
        Union[eventarc.ListTriggersResponse, Awaitable[eventarc.ListTriggersResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_trigger(
        self,
    ) -> Callable[
        [eventarc.CreateTriggerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_trigger(
        self,
    ) -> Callable[
        [eventarc.UpdateTriggerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_trigger(
        self,
    ) -> Callable[
        [eventarc.DeleteTriggerRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_channel(
        self,
    ) -> Callable[
        [eventarc.GetChannelRequest], Union[channel.Channel, Awaitable[channel.Channel]]
    ]:
        raise NotImplementedError()

    @property
    def list_channels(
        self,
    ) -> Callable[
        [eventarc.ListChannelsRequest],
        Union[eventarc.ListChannelsResponse, Awaitable[eventarc.ListChannelsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def create_channel_(
        self,
    ) -> Callable[
        [eventarc.CreateChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_channel(
        self,
    ) -> Callable[
        [eventarc.UpdateChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_channel(
        self,
    ) -> Callable[
        [eventarc.DeleteChannelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_provider(
        self,
    ) -> Callable[
        [eventarc.GetProviderRequest],
        Union[discovery.Provider, Awaitable[discovery.Provider]],
    ]:
        raise NotImplementedError()

    @property
    def list_providers(
        self,
    ) -> Callable[
        [eventarc.ListProvidersRequest],
        Union[
            eventarc.ListProvidersResponse, Awaitable[eventarc.ListProvidersResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_channel_connection(
        self,
    ) -> Callable[
        [eventarc.GetChannelConnectionRequest],
        Union[
            channel_connection.ChannelConnection,
            Awaitable[channel_connection.ChannelConnection],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_channel_connections(
        self,
    ) -> Callable[
        [eventarc.ListChannelConnectionsRequest],
        Union[
            eventarc.ListChannelConnectionsResponse,
            Awaitable[eventarc.ListChannelConnectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_channel_connection(
        self,
    ) -> Callable[
        [eventarc.CreateChannelConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_channel_connection(
        self,
    ) -> Callable[
        [eventarc.DeleteChannelConnectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_google_channel_config(
        self,
    ) -> Callable[
        [eventarc.GetGoogleChannelConfigRequest],
        Union[
            google_channel_config.GoogleChannelConfig,
            Awaitable[google_channel_config.GoogleChannelConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_google_channel_config(
        self,
    ) -> Callable[
        [eventarc.UpdateGoogleChannelConfigRequest],
        Union[
            gce_google_channel_config.GoogleChannelConfig,
            Awaitable[gce_google_channel_config.GoogleChannelConfig],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_message_bus(
        self,
    ) -> Callable[
        [eventarc.GetMessageBusRequest],
        Union[message_bus.MessageBus, Awaitable[message_bus.MessageBus]],
    ]:
        raise NotImplementedError()

    @property
    def list_message_buses(
        self,
    ) -> Callable[
        [eventarc.ListMessageBusesRequest],
        Union[
            eventarc.ListMessageBusesResponse,
            Awaitable[eventarc.ListMessageBusesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_message_bus_enrollments(
        self,
    ) -> Callable[
        [eventarc.ListMessageBusEnrollmentsRequest],
        Union[
            eventarc.ListMessageBusEnrollmentsResponse,
            Awaitable[eventarc.ListMessageBusEnrollmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_message_bus(
        self,
    ) -> Callable[
        [eventarc.CreateMessageBusRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_message_bus(
        self,
    ) -> Callable[
        [eventarc.UpdateMessageBusRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_message_bus(
        self,
    ) -> Callable[
        [eventarc.DeleteMessageBusRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_enrollment(
        self,
    ) -> Callable[
        [eventarc.GetEnrollmentRequest],
        Union[enrollment.Enrollment, Awaitable[enrollment.Enrollment]],
    ]:
        raise NotImplementedError()

    @property
    def list_enrollments(
        self,
    ) -> Callable[
        [eventarc.ListEnrollmentsRequest],
        Union[
            eventarc.ListEnrollmentsResponse,
            Awaitable[eventarc.ListEnrollmentsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_enrollment(
        self,
    ) -> Callable[
        [eventarc.CreateEnrollmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_enrollment(
        self,
    ) -> Callable[
        [eventarc.UpdateEnrollmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_enrollment(
        self,
    ) -> Callable[
        [eventarc.DeleteEnrollmentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_pipeline(
        self,
    ) -> Callable[
        [eventarc.GetPipelineRequest],
        Union[pipeline.Pipeline, Awaitable[pipeline.Pipeline]],
    ]:
        raise NotImplementedError()

    @property
    def list_pipelines(
        self,
    ) -> Callable[
        [eventarc.ListPipelinesRequest],
        Union[
            eventarc.ListPipelinesResponse, Awaitable[eventarc.ListPipelinesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_pipeline(
        self,
    ) -> Callable[
        [eventarc.CreatePipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_pipeline(
        self,
    ) -> Callable[
        [eventarc.UpdatePipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_pipeline(
        self,
    ) -> Callable[
        [eventarc.DeletePipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_google_api_source(
        self,
    ) -> Callable[
        [eventarc.GetGoogleApiSourceRequest],
        Union[
            google_api_source.GoogleApiSource,
            Awaitable[google_api_source.GoogleApiSource],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_google_api_sources(
        self,
    ) -> Callable[
        [eventarc.ListGoogleApiSourcesRequest],
        Union[
            eventarc.ListGoogleApiSourcesResponse,
            Awaitable[eventarc.ListGoogleApiSourcesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_google_api_source(
        self,
    ) -> Callable[
        [eventarc.CreateGoogleApiSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_google_api_source(
        self,
    ) -> Callable[
        [eventarc.UpdateGoogleApiSourceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_google_api_source(
        self,
    ) -> Callable[
        [eventarc.DeleteGoogleApiSourceRequest],
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


__all__ = ("EventarcTransport",)
