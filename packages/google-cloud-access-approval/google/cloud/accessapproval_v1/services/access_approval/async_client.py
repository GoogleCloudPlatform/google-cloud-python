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

from google.cloud.accessapproval_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.accessapproval_v1.services.access_approval import pagers
from google.cloud.accessapproval_v1.types import accessapproval

from .client import AccessApprovalClient
from .transports.base import DEFAULT_CLIENT_INFO, AccessApprovalTransport
from .transports.grpc_asyncio import AccessApprovalGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class AccessApprovalAsyncClient:
    """This API allows a customer to manage accesses to cloud resources by
    Google personnel. It defines the following resource model:

    - The API has a collection of
      [ApprovalRequest][google.cloud.accessapproval.v1.ApprovalRequest]
      resources, named ``approvalRequests/{approval_request}``
    - The API has top-level settings per Project/Folder/Organization,
      named ``accessApprovalSettings``

    The service also periodically emails a list of recipients, defined
    at the Project/Folder/Organization level in the
    accessApprovalSettings, when there is a pending ApprovalRequest for
    them to act on. The ApprovalRequests can also optionally be
    published to a Pub/Sub topic owned by the customer (contact support
    if you would like to enable Pub/Sub notifications).

    ApprovalRequests can be approved or dismissed. Google personnel can
    only access the indicated resource or resources if the request is
    approved (subject to some exclusions:
    https://cloud.google.com/access-approval/docs/overview#exclusions).

    Note: Using Access Approval functionality will mean that Google may
    not be able to meet the SLAs for your chosen products, as any
    support response times may be dramatically increased. As such the
    SLAs do not apply to any service disruption to the extent impacted
    by Customer's use of Access Approval. Do not enable Access Approval
    for projects where you may require high service availability and
    rapid response by Google Cloud Support.

    After a request is approved or dismissed, no further action may be
    taken on it. Requests with the requested_expiration in the past or
    with no activity for 14 days are considered dismissed. When an
    approval expires, the request is considered dismissed.

    If a request is not approved or dismissed, we call it pending.
    """

    _client: AccessApprovalClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = AccessApprovalClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AccessApprovalClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = AccessApprovalClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = AccessApprovalClient._DEFAULT_UNIVERSE

    access_approval_service_account_path = staticmethod(
        AccessApprovalClient.access_approval_service_account_path
    )
    parse_access_approval_service_account_path = staticmethod(
        AccessApprovalClient.parse_access_approval_service_account_path
    )
    access_approval_settings_path = staticmethod(
        AccessApprovalClient.access_approval_settings_path
    )
    parse_access_approval_settings_path = staticmethod(
        AccessApprovalClient.parse_access_approval_settings_path
    )
    approval_request_path = staticmethod(AccessApprovalClient.approval_request_path)
    parse_approval_request_path = staticmethod(
        AccessApprovalClient.parse_approval_request_path
    )
    common_billing_account_path = staticmethod(
        AccessApprovalClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AccessApprovalClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AccessApprovalClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AccessApprovalClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AccessApprovalClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AccessApprovalClient.parse_common_organization_path
    )
    common_project_path = staticmethod(AccessApprovalClient.common_project_path)
    parse_common_project_path = staticmethod(
        AccessApprovalClient.parse_common_project_path
    )
    common_location_path = staticmethod(AccessApprovalClient.common_location_path)
    parse_common_location_path = staticmethod(
        AccessApprovalClient.parse_common_location_path
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
            AccessApprovalAsyncClient: The constructed client.
        """
        sa_info_func = (
            AccessApprovalClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(AccessApprovalAsyncClient, info, *args, **kwargs)

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
            AccessApprovalAsyncClient: The constructed client.
        """
        sa_file_func = (
            AccessApprovalClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(AccessApprovalAsyncClient, filename, *args, **kwargs)

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
        return AccessApprovalClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AccessApprovalTransport:
        """Returns the transport used by the client instance.

        Returns:
            AccessApprovalTransport: The transport used by the client instance.
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

    get_transport_class = AccessApprovalClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, AccessApprovalTransport, Callable[..., AccessApprovalTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the access approval async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,AccessApprovalTransport,Callable[..., AccessApprovalTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the AccessApprovalTransport constructor.
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
        self._client = AccessApprovalClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.accessapproval_v1.AccessApprovalAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
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
                    "serviceName": "google.cloud.accessapproval.v1.AccessApproval",
                    "credentialsType": None,
                },
            )

    async def list_approval_requests(
        self,
        request: Optional[
            Union[accessapproval.ListApprovalRequestsMessage, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListApprovalRequestsAsyncPager:
        r"""Lists approval requests associated with a project,
        folder, or organization. Approval requests can be
        filtered by state (pending, active, dismissed). The
        order is reverse chronological.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_list_approval_requests():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.ListApprovalRequestsMessage(
                )

                # Make the request
                page_result = client.list_approval_requests(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.ListApprovalRequestsMessage, dict]]):
                The request object. Request to list approval requests.
            parent (:class:`str`):
                The parent resource. This may be
                "projects/{project}",
                "folders/{folder}", or
                "organizations/{organization}".

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
            google.cloud.accessapproval_v1.services.access_approval.pagers.ListApprovalRequestsAsyncPager:
                Response to listing of
                ApprovalRequest objects.
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
        if not isinstance(request, accessapproval.ListApprovalRequestsMessage):
            request = accessapproval.ListApprovalRequestsMessage(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_approval_requests
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
        response = pagers.ListApprovalRequestsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_approval_request(
        self,
        request: Optional[Union[accessapproval.GetApprovalRequestMessage, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.ApprovalRequest:
        r"""Gets an approval request. Returns NOT_FOUND if the request does
        not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_get_approval_request():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.GetApprovalRequestMessage(
                )

                # Make the request
                response = await client.get_approval_request(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.GetApprovalRequestMessage, dict]]):
                The request object. Request to get an approval request.
            name (:class:`str`):
                The name of the approval request to retrieve. Format:
                "{projects|folders|organizations}/{id}/approvalRequests/{approval_request}"

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
            google.cloud.accessapproval_v1.types.ApprovalRequest:
                A request for the customer to approve
                access to a resource.

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
        if not isinstance(request, accessapproval.GetApprovalRequestMessage):
            request = accessapproval.GetApprovalRequestMessage(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_approval_request
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

    async def approve_approval_request(
        self,
        request: Optional[
            Union[accessapproval.ApproveApprovalRequestMessage, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.ApprovalRequest:
        r"""Approves a request and returns the updated ApprovalRequest.

        Returns NOT_FOUND if the request does not exist. Returns
        FAILED_PRECONDITION if the request exists but is not in a
        pending state.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_approve_approval_request():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.ApproveApprovalRequestMessage(
                )

                # Make the request
                response = await client.approve_approval_request(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.ApproveApprovalRequestMessage, dict]]):
                The request object. Request to approve an
                ApprovalRequest.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.accessapproval_v1.types.ApprovalRequest:
                A request for the customer to approve
                access to a resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, accessapproval.ApproveApprovalRequestMessage):
            request = accessapproval.ApproveApprovalRequestMessage(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.approve_approval_request
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

    async def dismiss_approval_request(
        self,
        request: Optional[
            Union[accessapproval.DismissApprovalRequestMessage, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.ApprovalRequest:
        r"""Dismisses a request. Returns the updated ApprovalRequest.

        NOTE: This does not deny access to the resource if another
        request has been made and approved. It is equivalent in effect
        to ignoring the request altogether.

        Returns NOT_FOUND if the request does not exist.

        Returns FAILED_PRECONDITION if the request exists but is not in
        a pending state.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_dismiss_approval_request():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.DismissApprovalRequestMessage(
                )

                # Make the request
                response = await client.dismiss_approval_request(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.DismissApprovalRequestMessage, dict]]):
                The request object. Request to dismiss an approval
                request.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.accessapproval_v1.types.ApprovalRequest:
                A request for the customer to approve
                access to a resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, accessapproval.DismissApprovalRequestMessage):
            request = accessapproval.DismissApprovalRequestMessage(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.dismiss_approval_request
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

    async def invalidate_approval_request(
        self,
        request: Optional[
            Union[accessapproval.InvalidateApprovalRequestMessage, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.ApprovalRequest:
        r"""Invalidates an existing ApprovalRequest. Returns the updated
        ApprovalRequest.

        NOTE: This does not deny access to the resource if another
        request has been made and approved. It only invalidates a single
        approval.

        Returns FAILED_PRECONDITION if the request exists but is not in
        an approved state.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_invalidate_approval_request():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.InvalidateApprovalRequestMessage(
                )

                # Make the request
                response = await client.invalidate_approval_request(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.InvalidateApprovalRequestMessage, dict]]):
                The request object. Request to invalidate an existing
                approval.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.accessapproval_v1.types.ApprovalRequest:
                A request for the customer to approve
                access to a resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, accessapproval.InvalidateApprovalRequestMessage):
            request = accessapproval.InvalidateApprovalRequestMessage(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.invalidate_approval_request
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

    async def get_access_approval_settings(
        self,
        request: Optional[
            Union[accessapproval.GetAccessApprovalSettingsMessage, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.AccessApprovalSettings:
        r"""Gets the settings associated with a project, folder,
        or organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_get_access_approval_settings():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.GetAccessApprovalSettingsMessage(
                )

                # Make the request
                response = await client.get_access_approval_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.GetAccessApprovalSettingsMessage, dict]]):
                The request object. Request to get access approval
                settings.
            name (:class:`str`):
                The name of the AccessApprovalSettings to retrieve.
                Format:
                "{projects|folders|organizations}/{id}/accessApprovalSettings"

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
            google.cloud.accessapproval_v1.types.AccessApprovalSettings:
                Settings on a
                Project/Folder/Organization related to
                Access Approval.

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
        if not isinstance(request, accessapproval.GetAccessApprovalSettingsMessage):
            request = accessapproval.GetAccessApprovalSettingsMessage(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_access_approval_settings
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

    async def update_access_approval_settings(
        self,
        request: Optional[
            Union[accessapproval.UpdateAccessApprovalSettingsMessage, dict]
        ] = None,
        *,
        settings: Optional[accessapproval.AccessApprovalSettings] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.AccessApprovalSettings:
        r"""Updates the settings associated with a project, folder, or
        organization. Settings to update are determined by the value of
        field_mask.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_update_access_approval_settings():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.UpdateAccessApprovalSettingsMessage(
                )

                # Make the request
                response = await client.update_access_approval_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.UpdateAccessApprovalSettingsMessage, dict]]):
                The request object. Request to update access approval
                settings.
            settings (:class:`google.cloud.accessapproval_v1.types.AccessApprovalSettings`):
                The new AccessApprovalSettings.
                This corresponds to the ``settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The update mask applies to the settings. Only the top
                level fields of AccessApprovalSettings
                (notification_emails & enrolled_services) are supported.
                For each field, if it is included, the currently stored
                value will be entirely overwritten with the value of the
                field passed in this request.

                For the ``FieldMask`` definition, see
                https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#fieldmask
                If this field is left unset, only the
                notification_emails field will be updated.

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
            google.cloud.accessapproval_v1.types.AccessApprovalSettings:
                Settings on a
                Project/Folder/Organization related to
                Access Approval.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [settings, update_mask]
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
        if not isinstance(request, accessapproval.UpdateAccessApprovalSettingsMessage):
            request = accessapproval.UpdateAccessApprovalSettingsMessage(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if settings is not None:
            request.settings = settings
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_access_approval_settings
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("settings.name", request.settings.name),)
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

    async def delete_access_approval_settings(
        self,
        request: Optional[
            Union[accessapproval.DeleteAccessApprovalSettingsMessage, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes the settings associated with a project,
        folder, or organization. This will have the effect of
        disabling Access Approval for the project, folder, or
        organization, but only if all ancestors also have Access
        Approval disabled. If Access Approval is enabled at a
        higher level of the hierarchy, then Access Approval will
        still be enabled at this level as the settings are
        inherited.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_delete_access_approval_settings():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.DeleteAccessApprovalSettingsMessage(
                )

                # Make the request
                await client.delete_access_approval_settings(request=request)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.DeleteAccessApprovalSettingsMessage, dict]]):
                The request object. Request to delete access approval
                settings.
            name (:class:`str`):
                Name of the AccessApprovalSettings to
                delete.

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
        if not isinstance(request, accessapproval.DeleteAccessApprovalSettingsMessage):
            request = accessapproval.DeleteAccessApprovalSettingsMessage(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_access_approval_settings
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

    async def get_access_approval_service_account(
        self,
        request: Optional[
            Union[accessapproval.GetAccessApprovalServiceAccountMessage, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> accessapproval.AccessApprovalServiceAccount:
        r"""Retrieves the service account that is used by Access
        Approval to access KMS keys for signing approved
        approval requests.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import accessapproval_v1

            async def sample_get_access_approval_service_account():
                # Create a client
                client = accessapproval_v1.AccessApprovalAsyncClient()

                # Initialize request argument(s)
                request = accessapproval_v1.GetAccessApprovalServiceAccountMessage(
                )

                # Make the request
                response = await client.get_access_approval_service_account(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.accessapproval_v1.types.GetAccessApprovalServiceAccountMessage, dict]]):
                The request object. Request to get an Access Approval
                service account.
            name (:class:`str`):
                Name of the
                AccessApprovalServiceAccount to
                retrieve.

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
            google.cloud.accessapproval_v1.types.AccessApprovalServiceAccount:
                Access Approval service account
                related to a
                project/folder/organization.

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
            request, accessapproval.GetAccessApprovalServiceAccountMessage
        ):
            request = accessapproval.GetAccessApprovalServiceAccountMessage(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_access_approval_service_account
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

    async def __aenter__(self) -> "AccessApprovalAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("AccessApprovalAsyncClient",)
