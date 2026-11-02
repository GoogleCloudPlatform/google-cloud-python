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

from google.apps.events_subscriptions_v1beta import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.apps.events_subscriptions_v1beta.services.subscriptions_service import (
    pagers,
)
from google.apps.events_subscriptions_v1beta.types import (
    subscription_resource,
    subscriptions_service,
)

from .client import SubscriptionsServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, SubscriptionsServiceTransport
from .transports.grpc_asyncio import SubscriptionsServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class SubscriptionsServiceAsyncClient:
    """A service that manages subscriptions to Google Workspace
    events.
    """

    _client: SubscriptionsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = SubscriptionsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = SubscriptionsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = SubscriptionsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = SubscriptionsServiceClient._DEFAULT_UNIVERSE

    subscription_path = staticmethod(SubscriptionsServiceClient.subscription_path)
    parse_subscription_path = staticmethod(
        SubscriptionsServiceClient.parse_subscription_path
    )
    topic_path = staticmethod(SubscriptionsServiceClient.topic_path)
    parse_topic_path = staticmethod(SubscriptionsServiceClient.parse_topic_path)
    user_path = staticmethod(SubscriptionsServiceClient.user_path)
    parse_user_path = staticmethod(SubscriptionsServiceClient.parse_user_path)
    common_billing_account_path = staticmethod(
        SubscriptionsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        SubscriptionsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(SubscriptionsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        SubscriptionsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        SubscriptionsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        SubscriptionsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(SubscriptionsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        SubscriptionsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(SubscriptionsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        SubscriptionsServiceClient.parse_common_location_path
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
            SubscriptionsServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            SubscriptionsServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(SubscriptionsServiceAsyncClient, info, *args, **kwargs)

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
            SubscriptionsServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            SubscriptionsServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(SubscriptionsServiceAsyncClient, filename, *args, **kwargs)

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
        return SubscriptionsServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> SubscriptionsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            SubscriptionsServiceTransport: The transport used by the client instance.
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

    get_transport_class = SubscriptionsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                SubscriptionsServiceTransport,
                Callable[..., SubscriptionsServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the subscriptions service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,SubscriptionsServiceTransport,Callable[..., SubscriptionsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the SubscriptionsServiceTransport constructor.
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
        self._client = SubscriptionsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.apps.events.subscriptions_v1beta.SubscriptionsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
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
                    "serviceName": "google.apps.events.subscriptions.v1beta.SubscriptionsService",
                    "credentialsType": None,
                },
            )

    async def create_subscription(
        self,
        request: Optional[
            Union[subscriptions_service.CreateSubscriptionRequest, dict]
        ] = None,
        *,
        subscription: Optional[subscription_resource.Subscription] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates a Google Workspace subscription. To learn how to use
        this method, see `Create a Google Workspace
        subscription <https://developers.google.com/workspace/events/guides/create-subscription>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import events_subscriptions_v1beta

            async def sample_create_subscription():
                # Create a client
                client = events_subscriptions_v1beta.SubscriptionsServiceAsyncClient()

                # Initialize request argument(s)
                subscription = events_subscriptions_v1beta.Subscription()
                subscription.target_resource = "target_resource_value"
                subscription.event_types = ['event_types_value1', 'event_types_value2']
                subscription.notification_endpoint.pubsub_topic = "pubsub_topic_value"

                request = events_subscriptions_v1beta.CreateSubscriptionRequest(
                    subscription=subscription,
                )

                # Make the request
                operation = await client.create_subscription(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.events_subscriptions_v1beta.types.CreateSubscriptionRequest, dict]]):
                The request object. The request message for
                [SubscriptionsService.CreateSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.CreateSubscription].
            subscription (:class:`google.apps.events_subscriptions_v1beta.types.Subscription`):
                Required. The subscription resource
                to create.

                This corresponds to the ``subscription`` field
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

                The result type for the operation will be :class:`google.apps.events_subscriptions_v1beta.types.Subscription` A subscription to receive events about a Google Workspace resource. To learn
                   more about subscriptions, see the [Google Workspace
                   Events API
                   overview](https://developers.google.com/workspace/events).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [subscription]
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
        if not isinstance(request, subscriptions_service.CreateSubscriptionRequest):
            request = subscriptions_service.CreateSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if subscription is not None:
            request.subscription = subscription

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_subscription
        ]

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
            subscription_resource.Subscription,
            metadata_type=subscriptions_service.CreateSubscriptionMetadata,
        )

        # Done; return the response.
        return response

    async def delete_subscription(
        self,
        request: Optional[
            Union[subscriptions_service.DeleteSubscriptionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a Google Workspace subscription. To learn how to use
        this method, see `Delete a Google Workspace
        subscription <https://developers.google.com/workspace/events/guides/delete-subscription>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import events_subscriptions_v1beta

            async def sample_delete_subscription():
                # Create a client
                client = events_subscriptions_v1beta.SubscriptionsServiceAsyncClient()

                # Initialize request argument(s)
                request = events_subscriptions_v1beta.DeleteSubscriptionRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_subscription(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.events_subscriptions_v1beta.types.DeleteSubscriptionRequest, dict]]):
                The request object. The request message for
                [SubscriptionsService.DeleteSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.DeleteSubscription].
            name (:class:`str`):
                Required. Resource name of the subscription to delete.

                Format: ``subscriptions/{subscription}``

                This corresponds to the ``name`` field
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

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
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
        if not isinstance(request, subscriptions_service.DeleteSubscriptionRequest):
            request = subscriptions_service.DeleteSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_subscription
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
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
            empty_pb2.Empty,
            metadata_type=subscriptions_service.DeleteSubscriptionMetadata,
        )

        # Done; return the response.
        return response

    async def get_subscription(
        self,
        request: Optional[
            Union[subscriptions_service.GetSubscriptionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> subscription_resource.Subscription:
        r"""Gets details about a Google Workspace subscription. To learn how
        to use this method, see `Get details about a Google Workspace
        subscription <https://developers.google.com/workspace/events/guides/get-subscription>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import events_subscriptions_v1beta

            async def sample_get_subscription():
                # Create a client
                client = events_subscriptions_v1beta.SubscriptionsServiceAsyncClient()

                # Initialize request argument(s)
                request = events_subscriptions_v1beta.GetSubscriptionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_subscription(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.events_subscriptions_v1beta.types.GetSubscriptionRequest, dict]]):
                The request object. The request message for
                [SubscriptionsService.GetSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.GetSubscription].
            name (:class:`str`):
                Required. Resource name of the subscription.

                Format: ``subscriptions/{subscription}``

                This corresponds to the ``name`` field
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
            google.apps.events_subscriptions_v1beta.types.Subscription:
                A subscription to receive events about a Google Workspace resource. To learn
                   more about subscriptions, see the [Google Workspace
                   Events API
                   overview](https://developers.google.com/workspace/events).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
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
        if not isinstance(request, subscriptions_service.GetSubscriptionRequest):
            request = subscriptions_service.GetSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_subscription
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
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

    async def list_subscriptions(
        self,
        request: Optional[
            Union[subscriptions_service.ListSubscriptionsRequest, dict]
        ] = None,
        *,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSubscriptionsAsyncPager:
        r"""Lists Google Workspace subscriptions. To learn how to use this
        method, see `List Google Workspace
        subscriptions <https://developers.google.com/workspace/events/guides/list-subscriptions>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import events_subscriptions_v1beta

            async def sample_list_subscriptions():
                # Create a client
                client = events_subscriptions_v1beta.SubscriptionsServiceAsyncClient()

                # Initialize request argument(s)
                request = events_subscriptions_v1beta.ListSubscriptionsRequest(
                    filter="filter_value",
                )

                # Make the request
                page_result = client.list_subscriptions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.apps.events_subscriptions_v1beta.types.ListSubscriptionsRequest, dict]]):
                The request object. The request message for
                [SubscriptionsService.ListSubscriptions][google.apps.events.subscriptions.v1beta.SubscriptionsService.ListSubscriptions].
            filter (:class:`str`):
                Required. A query filter.

                You can filter subscriptions by event type
                (``event_types``) and target resource
                (``target_resource``).

                You must specify at least one event type in your query.
                To filter for multiple event types, use the ``OR``
                operator.

                To filter by both event type and target resource, use
                the ``AND`` operator and specify the full resource name,
                such as ``//chat.googleapis.com/spaces/{space}``.

                For example, the following queries are valid:

                ::

                   event_types:"google.workspace.chat.membership.v1.updated" OR
                     event_types:"google.workspace.chat.message.v1.created"

                   event_types:"google.workspace.chat.message.v1.created" AND
                     target_resource="//chat.googleapis.com/spaces/{space}"

                   ( event_types:"google.workspace.chat.membership.v1.updated" OR
                     event_types:"google.workspace.chat.message.v1.created" ) AND
                     target_resource="//chat.googleapis.com/spaces/{space}"

                The server rejects invalid queries with an
                ``INVALID_ARGUMENT`` error.

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
            google.apps.events_subscriptions_v1beta.services.subscriptions_service.pagers.ListSubscriptionsAsyncPager:
                The response message for
                   [SubscriptionsService.ListSubscriptions][google.apps.events.subscriptions.v1beta.SubscriptionsService.ListSubscriptions].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [filter]
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
        if not isinstance(request, subscriptions_service.ListSubscriptionsRequest):
            request = subscriptions_service.ListSubscriptionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_subscriptions
        ]

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
        response = pagers.ListSubscriptionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_subscription(
        self,
        request: Optional[
            Union[subscriptions_service.UpdateSubscriptionRequest, dict]
        ] = None,
        *,
        subscription: Optional[subscription_resource.Subscription] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates or renews a Google Workspace subscription. To learn how
        to use this method, see `Update or renew a Google Workspace
        subscription <https://developers.google.com/workspace/events/guides/update-subscription>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import events_subscriptions_v1beta

            async def sample_update_subscription():
                # Create a client
                client = events_subscriptions_v1beta.SubscriptionsServiceAsyncClient()

                # Initialize request argument(s)
                subscription = events_subscriptions_v1beta.Subscription()
                subscription.target_resource = "target_resource_value"
                subscription.event_types = ['event_types_value1', 'event_types_value2']
                subscription.notification_endpoint.pubsub_topic = "pubsub_topic_value"

                request = events_subscriptions_v1beta.UpdateSubscriptionRequest(
                    subscription=subscription,
                )

                # Make the request
                operation = await client.update_subscription(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.events_subscriptions_v1beta.types.UpdateSubscriptionRequest, dict]]):
                The request object. The request message for
                [SubscriptionsService.UpdateSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.UpdateSubscription].
            subscription (:class:`google.apps.events_subscriptions_v1beta.types.Subscription`):
                Required. The subscription to update.

                The subscription's ``name`` field is used to identify
                the subscription to update.

                This corresponds to the ``subscription`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The field to update. If omitted, updates any
                fields included in the request.

                You can update one of the following fields in a
                subscription:

                - [``expire_time``][google.apps.events.subscriptions.v1beta.Subscription.expire_time]:
                  The timestamp when the subscription expires.
                - [``ttl``][google.apps.events.subscriptions.v1beta.Subscription.ttl]:
                  The time-to-live (TTL) or duration of the
                  subscription.
                - [``event_types``][google.apps.events.subscriptions.v1beta.Subscription.event_types]:
                  The list of event types to receive about the target
                  resource.

                To fully replace the subscription (the equivalent of
                ``PUT``), use ``*``. Any omitted fields are updated with
                empty values.

                This corresponds to the ``update_mask`` field
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

                The result type for the operation will be :class:`google.apps.events_subscriptions_v1beta.types.Subscription` A subscription to receive events about a Google Workspace resource. To learn
                   more about subscriptions, see the [Google Workspace
                   Events API
                   overview](https://developers.google.com/workspace/events).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [subscription, update_mask]
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
        if not isinstance(request, subscriptions_service.UpdateSubscriptionRequest):
            request = subscriptions_service.UpdateSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if subscription is not None:
            request.subscription = subscription
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_subscription
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("subscription.name", request.subscription.name),)
            ),
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
            subscription_resource.Subscription,
            metadata_type=subscriptions_service.UpdateSubscriptionMetadata,
        )

        # Done; return the response.
        return response

    async def reactivate_subscription(
        self,
        request: Optional[
            Union[subscriptions_service.ReactivateSubscriptionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Reactivates a suspended Google Workspace subscription.

        This method resets your subscription's ``State`` field to
        ``ACTIVE``. Before you use this method, you must fix the error
        that suspended the subscription. This method will ignore or
        reject any subscription that isn't currently in a suspended
        state. To learn how to use this method, see `Reactivate a Google
        Workspace
        subscription <https://developers.google.com/workspace/events/guides/reactivate-subscription>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.apps import events_subscriptions_v1beta

            async def sample_reactivate_subscription():
                # Create a client
                client = events_subscriptions_v1beta.SubscriptionsServiceAsyncClient()

                # Initialize request argument(s)
                request = events_subscriptions_v1beta.ReactivateSubscriptionRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.reactivate_subscription(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.apps.events_subscriptions_v1beta.types.ReactivateSubscriptionRequest, dict]]):
                The request object. The request message for
                [SubscriptionsService.ReactivateSubscription][google.apps.events.subscriptions.v1beta.SubscriptionsService.ReactivateSubscription].
            name (:class:`str`):
                Required. Resource name of the subscription.

                Format: ``subscriptions/{subscription}``

                This corresponds to the ``name`` field
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

                The result type for the operation will be :class:`google.apps.events_subscriptions_v1beta.types.Subscription` A subscription to receive events about a Google Workspace resource. To learn
                   more about subscriptions, see the [Google Workspace
                   Events API
                   overview](https://developers.google.com/workspace/events).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
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
        if not isinstance(request, subscriptions_service.ReactivateSubscriptionRequest):
            request = subscriptions_service.ReactivateSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.reactivate_subscription
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
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
            subscription_resource.Subscription,
            metadata_type=subscriptions_service.ReactivateSubscriptionMetadata,
        )

        # Done; return the response.
        return response

    async def get_operation(
        self,
        request: Optional[Union[operations_pb2.GetOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.GetOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.GetOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self.transport._wrapped_methods[self._client._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "SubscriptionsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("SubscriptionsServiceAsyncClient",)
