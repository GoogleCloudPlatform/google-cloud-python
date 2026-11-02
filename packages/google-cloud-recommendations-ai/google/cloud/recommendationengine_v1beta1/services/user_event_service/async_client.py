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
import logging as std_logging
import re
from collections import OrderedDict
from typing import (
    Callable,
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.recommendationengine_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.any_pb2 as any_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.recommendationengine_v1beta1.services.user_event_service import pagers
from google.cloud.recommendationengine_v1beta1.types import (
    import_,
    user_event,
    user_event_service,
)
from google.cloud.recommendationengine_v1beta1.types import user_event as gcr_user_event

from .client import UserEventServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, UserEventServiceTransport
from .transports.grpc_asyncio import UserEventServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class UserEventServiceAsyncClient:
    """Service for ingesting end user actions on the customer
    website.
    """

    _client: UserEventServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = UserEventServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = UserEventServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = UserEventServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = UserEventServiceClient._DEFAULT_UNIVERSE

    event_store_path = staticmethod(UserEventServiceClient.event_store_path)
    parse_event_store_path = staticmethod(UserEventServiceClient.parse_event_store_path)
    common_billing_account_path = staticmethod(
        UserEventServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        UserEventServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(UserEventServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        UserEventServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        UserEventServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        UserEventServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(UserEventServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        UserEventServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(UserEventServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        UserEventServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            UserEventServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            UserEventServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(UserEventServiceAsyncClient, info, *args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            UserEventServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            UserEventServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(UserEventServiceAsyncClient, filename, *args, **kwargs)

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return UserEventServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> UserEventServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            UserEventServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = UserEventServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str, UserEventServiceTransport, Callable[..., UserEventServiceTransport]
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the user event service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,UserEventServiceTransport,Callable[..., UserEventServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the UserEventServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = UserEventServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.recommendationengine_v1beta1.UserEventServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.recommendationengine.v1beta1.UserEventService",
                    "universeDomain": getattr(
                        self._client._transport._credentials, "universe_domain", ""
                    ),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(
                        self.transport._credentials, "get_cred_info", lambda: None
                    )(),
                }
                if hasattr(self._client._transport, "_credentials")
                else {
                    "serviceName": "google.cloud.recommendationengine.v1beta1.UserEventService",
                    "credentialsType": None,
                },
            )

    async def write_user_event(
        self,
        request: Optional[Union[user_event_service.WriteUserEventRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        user_event: Optional[gcr_user_event.UserEvent] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcr_user_event.UserEvent:
        r"""Writes a single user event.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recommendationengine_v1beta1

            async def sample_write_user_event():
                # Create a client
                client = recommendationengine_v1beta1.UserEventServiceAsyncClient()

                # Initialize request argument(s)
                user_event = recommendationengine_v1beta1.UserEvent()
                user_event.event_type = "event_type_value"
                user_event.user_info.visitor_id = "visitor_id_value"

                request = recommendationengine_v1beta1.WriteUserEventRequest(
                    parent="parent_value",
                    user_event=user_event,
                )

                # Make the request
                response = await client.write_user_event(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recommendationengine_v1beta1.types.WriteUserEventRequest, dict]]):
                The request object. Request message for WriteUserEvent
                method.
            parent (:class:`str`):
                Required. The parent eventStore resource name, such as
                ``projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_event (:class:`google.cloud.recommendationengine_v1beta1.types.UserEvent`):
                Required. User event to write.
                This corresponds to the ``user_event`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.recommendationengine_v1beta1.types.UserEvent:
                UserEvent captures all metadata
                information recommendation engine needs
                to know about how end users interact
                with customers' website.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_event]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, user_event_service.WriteUserEventRequest):
            request = user_event_service.WriteUserEventRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if user_event is not None:
            request.user_event = user_event

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.write_user_event
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def collect_user_event(
        self,
        request: Optional[
            Union[user_event_service.CollectUserEventRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        user_event: Optional[str] = None,
        uri: Optional[str] = None,
        ets: Optional[int] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> httpbody_pb2.HttpBody:
        r"""Writes a single user event from the browser. This
        uses a GET request to due to browser restriction of
        POST-ing to a 3rd party domain.

        This method is used only by the Recommendations AI
        JavaScript pixel. Users should not call this method
        directly.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recommendationengine_v1beta1

            async def sample_collect_user_event():
                # Create a client
                client = recommendationengine_v1beta1.UserEventServiceAsyncClient()

                # Initialize request argument(s)
                request = recommendationengine_v1beta1.CollectUserEventRequest(
                    parent="parent_value",
                    user_event="user_event_value",
                )

                # Make the request
                response = await client.collect_user_event(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recommendationengine_v1beta1.types.CollectUserEventRequest, dict]]):
                The request object. Request message for CollectUserEvent
                method.
            parent (:class:`str`):
                Required. The parent eventStore name, such as
                ``projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            user_event (:class:`str`):
                Required. URL encoded UserEvent
                proto.

                This corresponds to the ``user_event`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            uri (:class:`str`):
                Optional. The url including
                cgi-parameters but excluding the hash
                fragment. The URL must be truncated to
                1.5K bytes to conservatively be under
                the 2K bytes. This is often more useful
                than the referer url, because many
                browsers only send the domain for 3rd
                party requests.

                This corresponds to the ``uri`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            ets (:class:`int`):
                Optional. The event timestamp in
                milliseconds. This prevents browser
                caching of otherwise identical get
                requests. The name is abbreviated to
                reduce the payload bytes.

                This corresponds to the ``ets`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api.httpbody_pb2.HttpBody:
                Message that represents an arbitrary HTTP body. It should only be used for
                   payload formats that can't be represented as JSON,
                   such as raw binary or an HTML page.

                   This message can be used both in streaming and
                   non-streaming API methods in the request as well as
                   the response.

                   It can be used as a top-level request field, which is
                   convenient if one wants to extract parameters from
                   either the URL or HTTP template into the request
                   fields and also want access to the raw HTTP body.

                   Example:

                      message GetResourceRequest {
                         // A unique request id. string request_id = 1;

                         // The raw HTTP body is bound to this field.
                         google.api.HttpBody http_body = 2;

                      }

                      service ResourceService {
                         rpc GetResource(GetResourceRequest)
                            returns (google.api.HttpBody);

                         rpc UpdateResource(google.api.HttpBody)
                            returns (google.protobuf.Empty);

                      }

                   Example with streaming methods:

                      service CaldavService {
                         rpc GetCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                         rpc UpdateCalendar(stream google.api.HttpBody)
                            returns (stream google.api.HttpBody);

                      }

                   Use of this type only changes how the request and
                   response bodies are handled, all other features will
                   continue to work unchanged.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, user_event, uri, ets]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, user_event_service.CollectUserEventRequest):
            request = user_event_service.CollectUserEventRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if user_event is not None:
            request.user_event = user_event
        if uri is not None:
            request.uri = uri
        if ets is not None:
            request.ets = ets

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.collect_user_event
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_user_events(
        self,
        request: Optional[Union[user_event_service.ListUserEventsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListUserEventsAsyncPager:
        r"""Gets a list of user events within a time range, with
        potential filtering.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recommendationengine_v1beta1

            async def sample_list_user_events():
                # Create a client
                client = recommendationengine_v1beta1.UserEventServiceAsyncClient()

                # Initialize request argument(s)
                request = recommendationengine_v1beta1.ListUserEventsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_user_events(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.recommendationengine_v1beta1.types.ListUserEventsRequest, dict]]):
                The request object. Request message for ListUserEvents
                method.
            parent (:class:`str`):
                Required. The parent eventStore resource name, such as
                ``projects/*/locations/*/catalogs/default_catalog/eventStores/default_event_store``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filtering expression to specify restrictions
                over returned events. This is a sequence of terms, where
                each term applies some kind of a restriction to the
                returned user events. Use this expression to restrict
                results to a specific time range, or filter events by
                eventType. eg: eventTime > "2012-04-23T18:25:43.511Z"
                eventsMissingCatalogItems
                eventTime<"2012-04-23T18:25:43.511Z" eventType=search

                We expect only 3 types of fields:

                ::

                   * eventTime: this can be specified a maximum of 2 times, once with a
                     less than operator and once with a greater than operator. The
                     eventTime restrict should result in one contiguous valid eventTime
                     range.

                   * eventType: only 1 eventType restriction can be specified.

                   * eventsMissingCatalogItems: specififying this will restrict results
                     to events for which catalog items were not found in the catalog. The
                     default behavior is to return only those events for which catalog
                     items were found.

                Some examples of valid filters expressions:

                - Example 1: eventTime > "2012-04-23T18:25:43.511Z"
                  eventTime < "2012-04-23T18:30:43.511Z"
                - Example 2: eventTime > "2012-04-23T18:25:43.511Z"
                  eventType = detail-page-view
                - Example 3: eventsMissingCatalogItems eventType =
                  search eventTime < "2018-04-23T18:30:43.511Z"
                - Example 4: eventTime > "2012-04-23T18:25:43.511Z"
                - Example 5: eventType = search
                - Example 6: eventsMissingCatalogItems

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.recommendationengine_v1beta1.services.user_event_service.pagers.ListUserEventsAsyncPager:
                Response message for ListUserEvents
                method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, filter]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, user_event_service.ListUserEventsRequest):
            request = user_event_service.ListUserEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_user_events
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListUserEventsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def purge_user_events(
        self,
        request: Optional[
            Union[user_event_service.PurgeUserEventsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        force: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes permanently all user events specified by the
        filter provided. Depending on the number of events
        specified by the filter, this operation could take hours
        or days to complete. To test a filter, use the list
        command first.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recommendationengine_v1beta1

            async def sample_purge_user_events():
                # Create a client
                client = recommendationengine_v1beta1.UserEventServiceAsyncClient()

                # Initialize request argument(s)
                request = recommendationengine_v1beta1.PurgeUserEventsRequest(
                    parent="parent_value",
                    filter="filter_value",
                )

                # Make the request
                operation = await client.purge_user_events(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recommendationengine_v1beta1.types.PurgeUserEventsRequest, dict]]):
                The request object. Request message for PurgeUserEvents
                method.
            parent (:class:`str`):
                Required. The resource name of the event_store under
                which the events are created. The format is
                ``projects/${projectId}/locations/global/catalogs/${catalogId}/eventStores/${eventStoreId}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Required. The filter string to specify the events to be
                deleted. Empty string filter is not allowed. This filter
                can also be used with ListUserEvents API to list events
                that will be deleted. The eligible fields for filtering
                are:

                - eventType - UserEvent.eventType field of type string.
                - eventTime - in ISO 8601 "zulu" format.
                - visitorId - field of type string. Specifying this will
                  delete all events associated with a visitor.
                - userId - field of type string. Specifying this will
                  delete all events associated with a user. Example 1:
                  Deleting all events in a time range.
                  ``eventTime > "2012-04-23T18:25:43.511Z" eventTime < "2012-04-23T18:30:43.511Z"``
                  Example 2: Deleting specific eventType in time range.
                  ``eventTime > "2012-04-23T18:25:43.511Z" eventType = "detail-page-view"``
                  Example 3: Deleting all events for a specific visitor
                  ``visitorId = visitor1024`` The filtering fields are
                  assumed to have an implicit AND.

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (:class:`bool`):
                Optional. The default value is false.
                Override this flag to true to actually
                perform the purge. If the field is not
                set to true, a sampling of events to be
                deleted will be returned.

                This corresponds to the ``force`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.recommendationengine_v1beta1.types.PurgeUserEventsResponse` Response of the PurgeUserEventsRequest. If the long running operation is
                   successfully done, then this message is returned by
                   the google.longrunning.Operations.response field.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, filter, force]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, user_event_service.PurgeUserEventsRequest):
            request = user_event_service.PurgeUserEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter
        if force is not None:
            request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.purge_user_events
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            user_event_service.PurgeUserEventsResponse,
            metadata_type=user_event_service.PurgeUserEventsMetadata,
        )

        # Done; return the response.
        return response

    async def import_user_events(
        self,
        request: Optional[Union[import_.ImportUserEventsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        request_id: Optional[str] = None,
        input_config: Optional[import_.InputConfig] = None,
        errors_config: Optional[import_.ImportErrorsConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Bulk import of User events. Request processing might
        be synchronous. Events that already exist are skipped.
        Use this method for backfilling historical user events.

        Operation.response is of type ImportResponse. Note that
        it is possible for a subset of the items to be
        successfully inserted. Operation.metadata is of type
        ImportMetadata.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import recommendationengine_v1beta1

            async def sample_import_user_events():
                # Create a client
                client = recommendationengine_v1beta1.UserEventServiceAsyncClient()

                # Initialize request argument(s)
                request = recommendationengine_v1beta1.ImportUserEventsRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.import_user_events(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.recommendationengine_v1beta1.types.ImportUserEventsRequest, dict]]):
                The request object. Request message for the
                ImportUserEvents request.
            parent (:class:`str`):
                Required.
                ``projects/1234/locations/global/catalogs/default_catalog/eventStores/default_event_store``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            request_id (:class:`str`):
                Optional. Unique identifier provided by client, within
                the ancestor dataset scope. Ensures idempotency for
                expensive long running operations. Server-generated if
                unspecified. Up to 128 characters long. This is returned
                as google.longrunning.Operation.name in the response.
                Note that this field must not be set if the desired
                input config is catalog_inline_source.

                This corresponds to the ``request_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            input_config (:class:`google.cloud.recommendationengine_v1beta1.types.InputConfig`):
                Required. The desired input location
                of the data.

                This corresponds to the ``input_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            errors_config (:class:`google.cloud.recommendationengine_v1beta1.types.ImportErrorsConfig`):
                Optional. The desired location of
                errors incurred during the Import.

                This corresponds to the ``errors_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.cloud.recommendationengine_v1beta1.types.ImportUserEventsResponse` Response of the ImportUserEventsRequest. If the long running
                   operation was successful, then this message is
                   returned by the
                   google.longrunning.Operations.response field if the
                   operation was successful.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, request_id, input_config, errors_config]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, import_.ImportUserEventsRequest):
            request = import_.ImportUserEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if request_id is not None:
            request.request_id = request_id
        if input_config is not None:
            request.input_config = input_config
        if errors_config is not None:
            request.errors_config = errors_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.import_user_events
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            import_.ImportUserEventsResponse,
            metadata_type=import_.ImportMetadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "UserEventServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("UserEventServiceAsyncClient",)
