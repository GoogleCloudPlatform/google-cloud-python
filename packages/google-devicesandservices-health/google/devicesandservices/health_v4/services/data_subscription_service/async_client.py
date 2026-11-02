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

from google.devicesandservices.health_v4 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore

from google.devicesandservices.health_v4.services.data_subscription_service import (
    pagers,
)
from google.devicesandservices.health_v4.types import data_subscription_service

from .client import DataSubscriptionServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DataSubscriptionServiceTransport
from .transports.grpc_asyncio import DataSubscriptionServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DataSubscriptionServiceAsyncClient:
    """Data Subscription Service that allows clients (e.g., Fitbit
    3P applications, internal Fitbit Services) to manage their
    subscriber endpoints. This service provides CRUD APIs for
    subscribers,
    and also offers functionalities for subscriber verification and
    statistics.
    """

    _client: DataSubscriptionServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataSubscriptionServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataSubscriptionServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = (
        DataSubscriptionServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = DataSubscriptionServiceClient._DEFAULT_UNIVERSE

    data_type_path = staticmethod(DataSubscriptionServiceClient.data_type_path)
    parse_data_type_path = staticmethod(
        DataSubscriptionServiceClient.parse_data_type_path
    )
    subscriber_path = staticmethod(DataSubscriptionServiceClient.subscriber_path)
    parse_subscriber_path = staticmethod(
        DataSubscriptionServiceClient.parse_subscriber_path
    )
    subscription_path = staticmethod(DataSubscriptionServiceClient.subscription_path)
    parse_subscription_path = staticmethod(
        DataSubscriptionServiceClient.parse_subscription_path
    )
    user_path = staticmethod(DataSubscriptionServiceClient.user_path)
    parse_user_path = staticmethod(DataSubscriptionServiceClient.parse_user_path)
    common_billing_account_path = staticmethod(
        DataSubscriptionServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataSubscriptionServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataSubscriptionServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DataSubscriptionServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataSubscriptionServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataSubscriptionServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        DataSubscriptionServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        DataSubscriptionServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        DataSubscriptionServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        DataSubscriptionServiceClient.parse_common_location_path
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
            DataSubscriptionServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DataSubscriptionServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DataSubscriptionServiceAsyncClient, info, *args, **kwargs)

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
            DataSubscriptionServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DataSubscriptionServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            DataSubscriptionServiceAsyncClient, filename, *args, **kwargs
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
        return DataSubscriptionServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> DataSubscriptionServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataSubscriptionServiceTransport: The transport used by the client instance.
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

    get_transport_class = DataSubscriptionServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DataSubscriptionServiceTransport,
                Callable[..., DataSubscriptionServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data subscription service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataSubscriptionServiceTransport,Callable[..., DataSubscriptionServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataSubscriptionServiceTransport constructor.
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
        self._client = DataSubscriptionServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.devicesandservices.health_v4.DataSubscriptionServiceAsyncClient`.",
                extra={
                    "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
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
                    "serviceName": "google.devicesandservices.health.v4.DataSubscriptionService",
                    "credentialsType": None,
                },
            )

    async def create_subscriber(
        self,
        request: Optional[
            Union[data_subscription_service.CreateSubscriberRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        subscriber: Optional[data_subscription_service.CreateSubscriberPayload] = None,
        subscriber_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Registers a new subscriber endpoint to receive notifications. A
        subscriber represents an application or service that wishes to
        receive data change notifications for users who have granted
        consent.

        **Endpoint Verification:** For a subscriber to be successfully
        created, the provided ``endpoint_uri`` must be a valid HTTPS
        endpoint and must pass an automated verification check. The
        backend will send two HTTP POST requests to the
        ``endpoint_uri``:

        1. **Verification with Authorization:**

           - **Headers:** Includes ``Content-Type: application/json``
             and ``Authorization`` (with the exact value from
             ``CreateSubscriberPayload.endpoint_authorization.secret``).
           - **Body:** ``{"type": "verification"}``
           - **Expected Response:** HTTP ``201 Created``.

        2. **Verification without Authorization:**

           - **Headers:** Includes ``Content-Type: application/json``.
             The ``Authorization`` header is OMITTED.
           - **Body:** ``{"type": "verification"}``
           - **Expected Response:** HTTP ``401 Unauthorized`` or
             ``403 Forbidden``.

        Both tests must pass for the subscriber creation to succeed. If
        verification fails, the operation will not be completed and an
        error will be returned. This process ensures the endpoint is
        reachable and correctly validates the ``Authorization`` header.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_create_subscriber():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                subscriber = health_v4.CreateSubscriberPayload()
                subscriber.endpoint_uri = "endpoint_uri_value"
                subscriber.endpoint_authorization.secret = "secret_value"

                request = health_v4.CreateSubscriberRequest(
                    parent="parent_value",
                    subscriber=subscriber,
                )

                # Make the request
                operation = await client.create_subscriber(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.CreateSubscriberRequest, dict]]):
                The request object. -- Messages --
                Request message for CreateSubscriber.
            parent (:class:`str`):
                Required. The parent resource where this subscriber will
                be created. Format: projects/{project_number} Example:
                projects/1234567890

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subscriber (:class:`google.devicesandservices.health_v4.types.CreateSubscriberPayload`):
                Required. The subscriber to create.
                This corresponds to the ``subscriber`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subscriber_id (:class:`str`):
                Optional. The ID to use for the subscriber, which will
                become the final component of the subscriber's resource
                name.

                This value should be 4-36 characters, and valid
                characters are /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/.

                This corresponds to the ``subscriber_id`` field
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

                The result type for the operation will be
                :class:`google.devicesandservices.health_v4.types.Subscriber`
                -- Resource Messages -- A subscriber receives
                notifications from Google Health API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, subscriber, subscriber_id]
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
        if not isinstance(request, data_subscription_service.CreateSubscriberRequest):
            request = data_subscription_service.CreateSubscriberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if subscriber is not None:
            request.subscriber = subscriber
        if subscriber_id is not None:
            request.subscriber_id = subscriber_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_subscriber
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
            data_subscription_service.Subscriber,
            metadata_type=data_subscription_service.CreateSubscriberMetadata,
        )

        # Done; return the response.
        return response

    async def list_subscribers(
        self,
        request: Optional[
            Union[data_subscription_service.ListSubscribersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSubscribersAsyncPager:
        r"""Lists all subscribers registered within the owned
        Google Cloud Project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_list_subscribers():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.ListSubscribersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_subscribers(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.ListSubscribersRequest, dict]]):
                The request object. Request message for ListSubscribers.
            parent (:class:`str`):
                Required. The parent, which owns this
                collection of subscribers. Format:
                projects/{project}

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
            google.devicesandservices.health_v4.services.data_subscription_service.pagers.ListSubscribersAsyncPager:
                Response message for ListSubscribers.

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
        if not isinstance(request, data_subscription_service.ListSubscribersRequest):
            request = data_subscription_service.ListSubscribersRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_subscribers
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
        response = pagers.ListSubscribersAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_subscriber(
        self,
        request: Optional[
            Union[data_subscription_service.UpdateSubscriberRequest, dict]
        ] = None,
        *,
        subscriber: Optional[data_subscription_service.Subscriber] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates the configuration of an existing subscriber, such as the
        endpoint URI or the data types it's interested in.

        **Endpoint Verification:** If the ``endpoint_uri`` or
        ``endpoint_authorization`` field is included in the
        ``update_mask``, the backend will re-verify the endpoint. The
        verification process is the same as described in
        ``CreateSubscriber``:

        1. **Verification with Authorization:** POST to the new or
           existing ``endpoint_uri`` with the new or existing
           ``Authorization`` secret. Expects HTTP ``201 Created``.
        2. **Verification without Authorization:** POST to the
           ``endpoint_uri`` without the ``Authorization`` header.
           Expects HTTP ``401 Unauthorized`` or ``403 Forbidden``.

        Both tests must pass using the potentially updated values for
        the subscriber update to succeed. If verification fails, the
        update will not be applied, and an error will be returned.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_update_subscriber():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                subscriber = health_v4.Subscriber()
                subscriber.endpoint_uri = "endpoint_uri_value"
                subscriber.endpoint_authorization.secret = "secret_value"

                request = health_v4.UpdateSubscriberRequest(
                    subscriber=subscriber,
                )

                # Make the request
                operation = await client.update_subscriber(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.UpdateSubscriberRequest, dict]]):
                The request object. Request message for UpdateSubscriber.
            subscriber (:class:`google.devicesandservices.health_v4.types.Subscriber`):
                Required. The subscriber resource to update. Its 'name'
                field is mapped to the URI, and the value of the 'name'
                field should be of the form:
                "projects/{project}/subscribers/{subscriber_id}". The
                remaining fields of the Subscriber object represent the
                new values for the corresponding fields in the existing
                subscriber resource.

                This corresponds to the ``subscriber`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. A field mask that specifies which fields of
                the Subscriber message are to be updated. This allows
                for partial updates. Supported fields:

                - endpoint_uri
                - subscriber_configs
                - endpoint_authorization

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

                The result type for the operation will be
                :class:`google.devicesandservices.health_v4.types.Subscriber`
                -- Resource Messages -- A subscriber receives
                notifications from Google Health API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [subscriber, update_mask]
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
        if not isinstance(request, data_subscription_service.UpdateSubscriberRequest):
            request = data_subscription_service.UpdateSubscriberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if subscriber is not None:
            request.subscriber = subscriber
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_subscriber
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("subscriber.name", request.subscriber.name),)
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
            data_subscription_service.Subscriber,
            metadata_type=data_subscription_service.UpdateSubscriberMetadata,
        )

        # Done; return the response.
        return response

    async def delete_subscriber(
        self,
        request: Optional[
            Union[data_subscription_service.DeleteSubscriberRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes a subscriber registration. This will stop all
        notifications to the subscriber's endpoint.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_delete_subscriber():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.DeleteSubscriberRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.delete_subscriber(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.DeleteSubscriberRequest, dict]]):
                The request object. Request message for DeleteSubscriber.
            name (:class:`str`):
                Required. The name of the subscriber to delete. Format:
                projects/{project}/subscribers/{subscriber} Example:
                projects/my-project/subscribers/my-subscriber-123 The
                {subscriber} ID is user-settable (4-36 characters,
                matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or
                system-generated if not provided during creation.

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
        if not isinstance(request, data_subscription_service.DeleteSubscriberRequest):
            request = data_subscription_service.DeleteSubscriberRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_subscriber
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
            metadata_type=data_subscription_service.DeleteSubscriberMetadata,
        )

        # Done; return the response.
        return response

    async def create_subscription(
        self,
        request: Optional[
            Union[data_subscription_service.CreateSubscriptionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        subscription: Optional[
            data_subscription_service.CreateSubscriptionPayload
        ] = None,
        subscription_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> data_subscription_service.Subscription:
        r"""Creates a subscription for a specific user to a specific
        subscriber. This method requires the subscriber to have a
        ``SubscriptionCreatePolicy`` set to ``MANUAL`` for the given
        data types.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_create_subscription():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                subscription = health_v4.CreateSubscriptionPayload()
                subscription.user = "user_value"

                request = health_v4.CreateSubscriptionRequest(
                    parent="parent_value",
                    subscription=subscription,
                )

                # Make the request
                response = await client.create_subscription(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.CreateSubscriptionRequest, dict]]):
                The request object. Request message for
                CreateSubscription.
            parent (:class:`str`):
                Required. The parent subscriber. Format:
                projects/{project}/subscribers/{subscriber} The
                {subscriber} ID is user-settable (4-36 characters,
                matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if
                provided during creation, or system-generated otherwise.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subscription (:class:`google.devicesandservices.health_v4.types.CreateSubscriptionPayload`):
                Required. The subscription to create.
                This corresponds to the ``subscription`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            subscription_id (:class:`str`):
                Optional. The {subscription_id} is user-settable (4-36
                chars, matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or
                system-generated otherwise. If provided, the ID must be
                unique within the parent subscriber.

                This corresponds to the ``subscription_id`` field
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
            google.devicesandservices.health_v4.types.Subscription:
                A subscription to a data collection
                for a specific user, to be delivered to
                a subscriber.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, subscription, subscription_id]
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
        if not isinstance(request, data_subscription_service.CreateSubscriptionRequest):
            request = data_subscription_service.CreateSubscriptionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if subscription is not None:
            request.subscription = subscription
        if subscription_id is not None:
            request.subscription_id = subscription_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_subscription
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

    async def list_subscriptions(
        self,
        request: Optional[
            Union[data_subscription_service.ListSubscriptionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSubscriptionsAsyncPager:
        r"""Lists all active subscriptions for a given
        subscriber. This can be filtered, for example, by user
        or data type.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_list_subscriptions():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.ListSubscriptionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_subscriptions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.ListSubscriptionsRequest, dict]]):
                The request object. Request message for
                ListSubscriptions.
            parent (:class:`str`):
                Required. The parent subscriber. Format:
                projects/{project}/subscribers/{subscriber} The
                {subscriber} ID is user-settable (4-36 characters,
                matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if
                provided during creation, or system-generated otherwise.

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
            google.devicesandservices.health_v4.services.data_subscription_service.pagers.ListSubscriptionsAsyncPager:
                Response message for
                ListSubscriptions.
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
        if not isinstance(request, data_subscription_service.ListSubscriptionsRequest):
            request = data_subscription_service.ListSubscriptionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_subscriptions
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
            Union[data_subscription_service.UpdateSubscriptionRequest, dict]
        ] = None,
        *,
        subscription: Optional[data_subscription_service.Subscription] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> data_subscription_service.Subscription:
        r"""Updates the data types for an existing user
        subscription.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_update_subscription():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.UpdateSubscriptionRequest(
                )

                # Make the request
                response = await client.update_subscription(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.UpdateSubscriptionRequest, dict]]):
                The request object. Request message for
                UpdateSubscription.
            subscription (:class:`google.devicesandservices.health_v4.types.Subscription`):
                Required. The subscription to update. The subscription's
                ``name`` field is used to identify the subscription to
                update. Format:
                projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}

                This corresponds to the ``subscription`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The list of fields to
                update.

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
            google.devicesandservices.health_v4.types.Subscription:
                A subscription to a data collection
                for a specific user, to be delivered to
                a subscriber.

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
        if not isinstance(request, data_subscription_service.UpdateSubscriptionRequest):
            request = data_subscription_service.UpdateSubscriptionRequest(request)

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

        # Done; return the response.
        return response

    async def delete_subscription(
        self,
        request: Optional[
            Union[data_subscription_service.DeleteSubscriptionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a specific user subscription, stopping
        notifications for this user to this subscriber.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.devicesandservices import health_v4

            async def sample_delete_subscription():
                # Create a client
                client = health_v4.DataSubscriptionServiceAsyncClient()

                # Initialize request argument(s)
                request = health_v4.DeleteSubscriptionRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_subscription(request=request)

        Args:
            request (Optional[Union[google.devicesandservices.health_v4.types.DeleteSubscriptionRequest, dict]]):
                The request object. Request message for
                DeleteSubscription.
            name (:class:`str`):
                Required. The resource name of the subscription to
                delete. Format:
                ``projects/{project}/subscribers/{subscriber}/subscriptions/{subscription}``
                Example:
                ``projects/my-project/subscribers/my-subscriber-123/subscriptions/my-subscription-456``
                The {subscriber} ID is user-settable (4-36 characters,
                matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) if
                provided during creation, or system-generated otherwise.
                The {subscription} ID is user-settable (4-36 characters,
                matching /`a-z <[a-z0-9-]{2,34}[a-z0-9]>`__/) or
                system-generated if not provided during creation.

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
        if not isinstance(request, data_subscription_service.DeleteSubscriptionRequest):
            request = data_subscription_service.DeleteSubscriptionRequest(request)

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
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def __aenter__(self) -> "DataSubscriptionServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DataSubscriptionServiceAsyncClient",)
