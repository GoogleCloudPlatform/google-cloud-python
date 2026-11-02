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

from google.cloud.visionai_v1 import gapic_version as package_version
from google.cloud.visionai_v1.types import common, streams_resources, streams_service

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class StreamsServiceTransport(abc.ABC):
    """Abstract transport class for StreamsService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "visionai.googleapis.com"

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
                 The hostname to connect to (default: 'visionai.googleapis.com').
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
            self.list_clusters: gapic_v1.method.wrap_method(
                self.list_clusters,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_cluster: gapic_v1.method.wrap_method(
                self.get_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_cluster: gapic_v1.method.wrap_method(
                self.create_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_cluster: gapic_v1.method.wrap_method(
                self.update_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_cluster: gapic_v1.method.wrap_method(
                self.delete_cluster,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_streams: gapic_v1.method.wrap_method(
                self.list_streams,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_stream: gapic_v1.method.wrap_method(
                self.get_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_stream: gapic_v1.method.wrap_method(
                self.create_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_stream: gapic_v1.method.wrap_method(
                self.update_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_stream: gapic_v1.method.wrap_method(
                self.delete_stream,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_stream_thumbnail: gapic_v1.method.wrap_method(
                self.get_stream_thumbnail,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_stream_hls_token: gapic_v1.method.wrap_method(
                self.generate_stream_hls_token,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_events: gapic_v1.method.wrap_method(
                self.list_events,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_event: gapic_v1.method.wrap_method(
                self.get_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_event: gapic_v1.method.wrap_method(
                self.create_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_event: gapic_v1.method.wrap_method(
                self.update_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_event: gapic_v1.method.wrap_method(
                self.delete_event,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_series: gapic_v1.method.wrap_method(
                self.list_series,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_series: gapic_v1.method.wrap_method(
                self.get_series,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_series: gapic_v1.method.wrap_method(
                self.create_series,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_series: gapic_v1.method.wrap_method(
                self.update_series,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_series: gapic_v1.method.wrap_method(
                self.delete_series,
                default_timeout=None,
                client_info=client_info,
            ),
            self.materialize_channel: gapic_v1.method.wrap_method(
                self.materialize_channel,
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
    def list_clusters(
        self,
    ) -> Callable[
        [streams_service.ListClustersRequest],
        Union[
            streams_service.ListClustersResponse,
            Awaitable[streams_service.ListClustersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_cluster(
        self,
    ) -> Callable[
        [streams_service.GetClusterRequest],
        Union[common.Cluster, Awaitable[common.Cluster]],
    ]:
        raise NotImplementedError()

    @property
    def create_cluster(
        self,
    ) -> Callable[
        [streams_service.CreateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_cluster(
        self,
    ) -> Callable[
        [streams_service.UpdateClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_cluster(
        self,
    ) -> Callable[
        [streams_service.DeleteClusterRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_streams(
        self,
    ) -> Callable[
        [streams_service.ListStreamsRequest],
        Union[
            streams_service.ListStreamsResponse,
            Awaitable[streams_service.ListStreamsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_stream(
        self,
    ) -> Callable[
        [streams_service.GetStreamRequest],
        Union[streams_resources.Stream, Awaitable[streams_resources.Stream]],
    ]:
        raise NotImplementedError()

    @property
    def create_stream(
        self,
    ) -> Callable[
        [streams_service.CreateStreamRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_stream(
        self,
    ) -> Callable[
        [streams_service.UpdateStreamRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_stream(
        self,
    ) -> Callable[
        [streams_service.DeleteStreamRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_stream_thumbnail(
        self,
    ) -> Callable[
        [streams_service.GetStreamThumbnailRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_stream_hls_token(
        self,
    ) -> Callable[
        [streams_service.GenerateStreamHlsTokenRequest],
        Union[
            streams_service.GenerateStreamHlsTokenResponse,
            Awaitable[streams_service.GenerateStreamHlsTokenResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_events(
        self,
    ) -> Callable[
        [streams_service.ListEventsRequest],
        Union[
            streams_service.ListEventsResponse,
            Awaitable[streams_service.ListEventsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_event(
        self,
    ) -> Callable[
        [streams_service.GetEventRequest],
        Union[streams_resources.Event, Awaitable[streams_resources.Event]],
    ]:
        raise NotImplementedError()

    @property
    def create_event(
        self,
    ) -> Callable[
        [streams_service.CreateEventRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_event(
        self,
    ) -> Callable[
        [streams_service.UpdateEventRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_event(
        self,
    ) -> Callable[
        [streams_service.DeleteEventRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_series(
        self,
    ) -> Callable[
        [streams_service.ListSeriesRequest],
        Union[
            streams_service.ListSeriesResponse,
            Awaitable[streams_service.ListSeriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_series(
        self,
    ) -> Callable[
        [streams_service.GetSeriesRequest],
        Union[streams_resources.Series, Awaitable[streams_resources.Series]],
    ]:
        raise NotImplementedError()

    @property
    def create_series(
        self,
    ) -> Callable[
        [streams_service.CreateSeriesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_series(
        self,
    ) -> Callable[
        [streams_service.UpdateSeriesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_series(
        self,
    ) -> Callable[
        [streams_service.DeleteSeriesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def materialize_channel(
        self,
    ) -> Callable[
        [streams_service.MaterializeChannelRequest],
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


__all__ = ("StreamsServiceTransport",)
