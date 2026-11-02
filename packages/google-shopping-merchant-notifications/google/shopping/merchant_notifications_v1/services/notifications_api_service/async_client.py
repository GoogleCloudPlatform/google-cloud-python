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

from google.shopping.merchant_notifications_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore

from google.shopping.merchant_notifications_v1.services.notifications_api_service import (
    pagers,
)
from google.shopping.merchant_notifications_v1.types import notificationsapi

from .client import NotificationsApiServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, NotificationsApiServiceTransport
from .transports.grpc_asyncio import NotificationsApiServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class NotificationsApiServiceAsyncClient:
    """Service to manage notification subscriptions for merchants"""

    _client: NotificationsApiServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = NotificationsApiServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = NotificationsApiServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        NotificationsApiServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = NotificationsApiServiceClient._DEFAULT_UNIVERSE

    notification_subscription_path = staticmethod(
        NotificationsApiServiceClient.notification_subscription_path
    )
    parse_notification_subscription_path = staticmethod(
        NotificationsApiServiceClient.parse_notification_subscription_path
    )
    notification_subscription_health_metrics_path = staticmethod(
        NotificationsApiServiceClient.notification_subscription_health_metrics_path
    )
    parse_notification_subscription_health_metrics_path = staticmethod(
        NotificationsApiServiceClient.parse_notification_subscription_health_metrics_path
    )
    common_billing_account_path = staticmethod(
        NotificationsApiServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        NotificationsApiServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(NotificationsApiServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        NotificationsApiServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        NotificationsApiServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        NotificationsApiServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        NotificationsApiServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        NotificationsApiServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        NotificationsApiServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        NotificationsApiServiceClient.parse_common_location_path
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
            NotificationsApiServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            NotificationsApiServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(NotificationsApiServiceAsyncClient, info, *args, **kwargs)

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
            NotificationsApiServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            NotificationsApiServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            NotificationsApiServiceAsyncClient, filename, *args, **kwargs
        )

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
        return NotificationsApiServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> NotificationsApiServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            NotificationsApiServiceTransport: The transport used by the client instance.
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

    get_transport_class = NotificationsApiServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                NotificationsApiServiceTransport,
                Callable[..., NotificationsApiServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the notifications api service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,NotificationsApiServiceTransport,Callable[..., NotificationsApiServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the NotificationsApiServiceTransport constructor.
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
        self._client = NotificationsApiServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.notifications_v1.NotificationsApiServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.notifications.v1.NotificationsApiService",
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
                    "serviceName": "google.shopping.merchant.notifications.v1.NotificationsApiService",
                    "credentialsType": None,
                },
            )

    async def get_notification_subscription(
        self,
        request: Optional[
            Union[notificationsapi.GetNotificationSubscriptionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> notificationsapi.NotificationSubscription:
        r"""Gets notification subscriptions for an account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_notifications_v1

            async def sample_get_notification_subscription():
                # Create a client
                client = merchant_notifications_v1.NotificationsApiServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_notifications_v1.GetNotificationSubscriptionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_notification_subscription(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_notifications_v1.types.GetNotificationSubscriptionRequest, dict]]):
                The request object. Request message for the
                GetNotificationSubscription method.
            name (:class:`str`):
                Required. The ``name`` of the notification subscription.
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
            google.shopping.merchant_notifications_v1.types.NotificationSubscription:
                Represents a notification
                subscription owned by a Merchant
                account.

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
        if not isinstance(request, notificationsapi.GetNotificationSubscriptionRequest):
            request = notificationsapi.GetNotificationSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_notification_subscription
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

    async def create_notification_subscription(
        self,
        request: Optional[
            Union[notificationsapi.CreateNotificationSubscriptionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        notification_subscription: Optional[
            notificationsapi.NotificationSubscription
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> notificationsapi.NotificationSubscription:
        r"""Creates a notification subscription for a business.
        For standalone or subaccounts accounts, the business can
        create a subscription for self. For MCAs, the business
        can create a subscription for all managed accounts or
        for a specific subaccount.

        We will allow the following types of notification
        subscriptions to exist together (per business as a
        subscriber per event type):

        1. Subscription for all managed accounts + subscription
            for self.

        2. Multiple "partial" subscriptions for managed accounts
            + subscription for self.

        we will not allow (per business as a subscriber per
        event type):

        1. Multiple self subscriptions.

        2. Multiple "all managed accounts" subscriptions.

        3. "All managed accounts" subscription and partial
            subscriptions at the same time.

        4. Multiple partial subscriptions for the same target
            account.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_notifications_v1

            async def sample_create_notification_subscription():
                # Create a client
                client = merchant_notifications_v1.NotificationsApiServiceAsyncClient()

                # Initialize request argument(s)
                notification_subscription = merchant_notifications_v1.NotificationSubscription()
                notification_subscription.all_managed_accounts = True

                request = merchant_notifications_v1.CreateNotificationSubscriptionRequest(
                    parent="parent_value",
                    notification_subscription=notification_subscription,
                )

                # Make the request
                response = await client.create_notification_subscription(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_notifications_v1.types.CreateNotificationSubscriptionRequest, dict]]):
                The request object. Request message for the
                CreateNotificationSubscription method.
            parent (:class:`str`):
                Required. The merchant account that owns the new
                notification subscription. Format:
                ``accounts/{account}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            notification_subscription (:class:`google.shopping.merchant_notifications_v1.types.NotificationSubscription`):
                Required. The notification
                subscription to create.

                This corresponds to the ``notification_subscription`` field
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
            google.shopping.merchant_notifications_v1.types.NotificationSubscription:
                Represents a notification
                subscription owned by a Merchant
                account.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, notification_subscription]
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
        if not isinstance(
            request, notificationsapi.CreateNotificationSubscriptionRequest
        ):
            request = notificationsapi.CreateNotificationSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if notification_subscription is not None:
            request.notification_subscription = notification_subscription

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_notification_subscription
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

    async def update_notification_subscription(
        self,
        request: Optional[
            Union[notificationsapi.UpdateNotificationSubscriptionRequest, dict]
        ] = None,
        *,
        notification_subscription: Optional[
            notificationsapi.NotificationSubscription
        ] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> notificationsapi.NotificationSubscription:
        r"""Updates an existing notification subscription for a
        merchant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_notifications_v1

            async def sample_update_notification_subscription():
                # Create a client
                client = merchant_notifications_v1.NotificationsApiServiceAsyncClient()

                # Initialize request argument(s)
                notification_subscription = merchant_notifications_v1.NotificationSubscription()
                notification_subscription.all_managed_accounts = True

                request = merchant_notifications_v1.UpdateNotificationSubscriptionRequest(
                    notification_subscription=notification_subscription,
                )

                # Make the request
                response = await client.update_notification_subscription(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_notifications_v1.types.UpdateNotificationSubscriptionRequest, dict]]):
                The request object. Request message for the
                UpdateNotificationSubscription method.
            notification_subscription (:class:`google.shopping.merchant_notifications_v1.types.NotificationSubscription`):
                Required. The new version of the
                notification subscription that should be
                updated.

                This corresponds to the ``notification_subscription`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                List of fields being updated.
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
            google.shopping.merchant_notifications_v1.types.NotificationSubscription:
                Represents a notification
                subscription owned by a Merchant
                account.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [notification_subscription, update_mask]
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
        if not isinstance(
            request, notificationsapi.UpdateNotificationSubscriptionRequest
        ):
            request = notificationsapi.UpdateNotificationSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if notification_subscription is not None:
            request.notification_subscription = notification_subscription
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_notification_subscription
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "notification_subscription.name",
                        request.notification_subscription.name,
                    ),
                )
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

        # Done; return the response.
        return response

    async def delete_notification_subscription(
        self,
        request: Optional[
            Union[notificationsapi.DeleteNotificationSubscriptionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a notification subscription for a merchant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_notifications_v1

            async def sample_delete_notification_subscription():
                # Create a client
                client = merchant_notifications_v1.NotificationsApiServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_notifications_v1.DeleteNotificationSubscriptionRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_notification_subscription(request=request)

        Args:
            request (Optional[Union[google.shopping.merchant_notifications_v1.types.DeleteNotificationSubscriptionRequest, dict]]):
                The request object. Request message for the
                DeleteNotificationSubscription method.
            name (:class:`str`):
                Required. The name of the
                notification subscription to be deleted.

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
        if not isinstance(
            request, notificationsapi.DeleteNotificationSubscriptionRequest
        ):
            request = notificationsapi.DeleteNotificationSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_notification_subscription
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def list_notification_subscriptions(
        self,
        request: Optional[
            Union[notificationsapi.ListNotificationSubscriptionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListNotificationSubscriptionsAsyncPager:
        r"""Gets all the notification subscriptions for a
        merchant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_notifications_v1

            async def sample_list_notification_subscriptions():
                # Create a client
                client = merchant_notifications_v1.NotificationsApiServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_notifications_v1.ListNotificationSubscriptionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_notification_subscriptions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_notifications_v1.types.ListNotificationSubscriptionsRequest, dict]]):
                The request object. Request message for the
                ListNotificationSubscription method.
            parent (:class:`str`):
                Required. The merchant account who owns the notification
                subscriptions. Format: ``accounts/{account}``

                This corresponds to the ``parent`` field
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
            google.shopping.merchant_notifications_v1.services.notifications_api_service.pagers.ListNotificationSubscriptionsAsyncPager:
                Response message for the
                ListNotificationSubscription method.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
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
        if not isinstance(
            request, notificationsapi.ListNotificationSubscriptionsRequest
        ):
            request = notificationsapi.ListNotificationSubscriptionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_notification_subscriptions
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
        response = pagers.ListNotificationSubscriptionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_notification_subscription_health_metrics(
        self,
        request: Optional[
            Union[
                notificationsapi.GetNotificationSubscriptionHealthMetricsRequest, dict
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> notificationsapi.NotificationSubscriptionHealthMetrics:
        r"""Retrieves notification subscription health metrics
        for a merchant. We recommend calling this periodically
        (hourly or daily) to monitor health of your callback
        endpoint.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_notifications_v1

            async def sample_get_notification_subscription_health_metrics():
                # Create a client
                client = merchant_notifications_v1.NotificationsApiServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_notifications_v1.GetNotificationSubscriptionHealthMetricsRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_notification_subscription_health_metrics(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_notifications_v1.types.GetNotificationSubscriptionHealthMetricsRequest, dict]]):
                The request object. Request for notification subscription
                health metrics.
            name (:class:`str`):
                Required. The ``name`` of the notification subscription
                for which metrics are retrieved. Format:
                ``accounts/{account}/notificationsubscriptions/{notification_subscription}``

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
            google.shopping.merchant_notifications_v1.types.NotificationSubscriptionHealthMetrics:
                Represents a notification
                subscription health metrics.

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
        if not isinstance(
            request, notificationsapi.GetNotificationSubscriptionHealthMetricsRequest
        ):
            request = notificationsapi.GetNotificationSubscriptionHealthMetricsRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_notification_subscription_health_metrics
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

    async def __aenter__(self) -> "NotificationsApiServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("NotificationsApiServiceAsyncClient",)
