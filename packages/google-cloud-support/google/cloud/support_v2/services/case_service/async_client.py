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

from google.cloud.support_v2 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.support_v2.services.case_service import pagers
from google.cloud.support_v2.types import actor, case, case_service
from google.cloud.support_v2.types import case as gcs_case

from .client import CaseServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, CaseServiceTransport
from .transports.grpc_asyncio import CaseServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class CaseServiceAsyncClient:
    """A service to manage Google Cloud support cases."""

    _client: CaseServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = CaseServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = CaseServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = CaseServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = CaseServiceClient._DEFAULT_UNIVERSE

    case_path = staticmethod(CaseServiceClient.case_path)
    parse_case_path = staticmethod(CaseServiceClient.parse_case_path)
    common_billing_account_path = staticmethod(
        CaseServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        CaseServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(CaseServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(CaseServiceClient.parse_common_folder_path)
    common_organization_path = staticmethod(CaseServiceClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        CaseServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(CaseServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        CaseServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(CaseServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        CaseServiceClient.parse_common_location_path
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
            CaseServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            CaseServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(CaseServiceAsyncClient, info, *args, **kwargs)

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
            CaseServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            CaseServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(CaseServiceAsyncClient, filename, *args, **kwargs)

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
        return CaseServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> CaseServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            CaseServiceTransport: The transport used by the client instance.
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

    get_transport_class = CaseServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, CaseServiceTransport, Callable[..., CaseServiceTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the case service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,CaseServiceTransport,Callable[..., CaseServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the CaseServiceTransport constructor.
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
        self._client = CaseServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.support_v2.CaseServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.support.v2.CaseService",
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
                    "serviceName": "google.cloud.support.v2.CaseService",
                    "credentialsType": None,
                },
            )

    async def get_case(
        self,
        request: Optional[Union[case_service.GetCaseRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> case.Case:
        r"""Retrieve a case.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_get_case():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.GetCaseRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_case(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.GetCaseRequest, dict]]):
                The request object. The request message for the GetCase
                endpoint.
            name (:class:`str`):
                Required. The full name of a case to
                be retrieved.

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
            google.cloud.support_v2.types.Case:
                A Case is an object that contains the details of a support case. It
                   contains fields for the time it was created, its
                   priority, its classification, and more. Cases can
                   also have comments and attachments that get added
                   over time.

                   A case is parented by a Google Cloud organization or
                   project.

                   Organizations are identified by a number, so the name
                   of a case parented by an organization would look like
                   this:

                   :literal:`` organizations/123/cases/456`\ \`

                   Projects have two unique identifiers, an ID and a
                   number, and they look like this:

                   :literal:`` projects/abc/cases/456`\ \`

                   :literal:`` projects/123/cases/456`\ \`

                   You can use either of them when calling the API. To
                   learn more about project identifiers, see
                   [AIP-2510](https://google.aip.dev/cloud/2510).

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
        if not isinstance(request, case_service.GetCaseRequest):
            request = case_service.GetCaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[self._client._transport.get_case]

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

    async def list_cases(
        self,
        request: Optional[Union[case_service.ListCasesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListCasesAsyncPager:
        r"""Retrieve all cases under a parent, but not its children.

        For example, listing cases under an organization only returns
        the cases that are directly parented by that organization. To
        retrieve cases under an organization and its projects, use
        ``cases.search``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_list_cases():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.ListCasesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_cases(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.ListCasesRequest, dict]]):
                The request object. The request message for the ListCases
                endpoint.
            parent (:class:`str`):
                Required. The name of a parent to
                list cases under.

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
            google.cloud.support_v2.services.case_service.pagers.ListCasesAsyncPager:
                The response message for the
                ListCases endpoint.
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
        if not isinstance(request, case_service.ListCasesRequest):
            request = case_service.ListCasesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_cases
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
        response = pagers.ListCasesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_cases(
        self,
        request: Optional[Union[case_service.SearchCasesRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchCasesAsyncPager:
        r"""Search for cases using a query.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_search_cases():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.SearchCasesRequest(
                )

                # Make the request
                page_result = client.search_cases(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.SearchCasesRequest, dict]]):
                The request object. The request message for the
                SearchCases endpoint.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.support_v2.services.case_service.pagers.SearchCasesAsyncPager:
                The response message for the
                SearchCases endpoint.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, case_service.SearchCasesRequest):
            request = case_service.SearchCasesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_cases
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
        response = pagers.SearchCasesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_case(
        self,
        request: Optional[Union[case_service.CreateCaseRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        case: Optional[gcs_case.Case] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_case.Case:
        r"""Create a new case and associate it with a parent.

        It must have the following fields set: ``display_name``,
        ``description``, ``classification``, and ``priority``. If you're
        just testing the API and don't want to route your case to an
        agent, set ``testCase=true``.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_create_case():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.CreateCaseRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_case(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.CreateCaseRequest, dict]]):
                The request object. The request message for the
                CreateCase endpoint.
            parent (:class:`str`):
                Required. The name of the parent
                under which the case should be created.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            case (:class:`google.cloud.support_v2.types.Case`):
                Required. The case to be created.
                This corresponds to the ``case`` field
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
            google.cloud.support_v2.types.Case:
                A Case is an object that contains the details of a support case. It
                   contains fields for the time it was created, its
                   priority, its classification, and more. Cases can
                   also have comments and attachments that get added
                   over time.

                   A case is parented by a Google Cloud organization or
                   project.

                   Organizations are identified by a number, so the name
                   of a case parented by an organization would look like
                   this:

                   :literal:`` organizations/123/cases/456`\ \`

                   Projects have two unique identifiers, an ID and a
                   number, and they look like this:

                   :literal:`` projects/abc/cases/456`\ \`

                   :literal:`` projects/123/cases/456`\ \`

                   You can use either of them when calling the API. To
                   learn more about project identifiers, see
                   [AIP-2510](https://google.aip.dev/cloud/2510).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, case]
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
        if not isinstance(request, case_service.CreateCaseRequest):
            request = case_service.CreateCaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if case is not None:
            request.case = case

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_case
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

    async def update_case(
        self,
        request: Optional[Union[case_service.UpdateCaseRequest, dict]] = None,
        *,
        case: Optional[gcs_case.Case] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcs_case.Case:
        r"""Update a case. Only some fields can be updated.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_update_case():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.UpdateCaseRequest(
                )

                # Make the request
                response = await client.update_case(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.UpdateCaseRequest, dict]]):
                The request object. The request message for the
                UpdateCase endpoint
            case (:class:`google.cloud.support_v2.types.Case`):
                Required. The case to update.
                This corresponds to the ``case`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                A list of attributes of the case that should be updated.
                Supported values are ``priority``, ``display_name``, and
                ``subscriber_email_addresses``. If no fields are
                specified, all supported fields are updated.

                Be careful - if you do not provide a field mask, then
                you might accidentally clear some fields. For example,
                if you leave the field mask empty and do not provide a
                value for ``subscriber_email_addresses``, then
                ``subscriber_email_addresses`` is updated to empty.

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
            google.cloud.support_v2.types.Case:
                A Case is an object that contains the details of a support case. It
                   contains fields for the time it was created, its
                   priority, its classification, and more. Cases can
                   also have comments and attachments that get added
                   over time.

                   A case is parented by a Google Cloud organization or
                   project.

                   Organizations are identified by a number, so the name
                   of a case parented by an organization would look like
                   this:

                   :literal:`` organizations/123/cases/456`\ \`

                   Projects have two unique identifiers, an ID and a
                   number, and they look like this:

                   :literal:`` projects/abc/cases/456`\ \`

                   :literal:`` projects/123/cases/456`\ \`

                   You can use either of them when calling the API. To
                   learn more about project identifiers, see
                   [AIP-2510](https://google.aip.dev/cloud/2510).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [case, update_mask]
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
        if not isinstance(request, case_service.UpdateCaseRequest):
            request = case_service.UpdateCaseRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if case is not None:
            request.case = case
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_case
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("case.name", request.case.name),)
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

    async def escalate_case(
        self,
        request: Optional[Union[case_service.EscalateCaseRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> case.Case:
        r"""Escalate a case, starting the Google Cloud Support
        escalation management process.

        This operation is only available for some support
        services. Go to https://cloud.google.com/support and
        look for 'Technical support escalations' in the feature
        list to find out which ones let you do that.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_escalate_case():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.EscalateCaseRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.escalate_case(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.EscalateCaseRequest, dict]]):
                The request object. The request message for the
                EscalateCase endpoint.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.support_v2.types.Case:
                A Case is an object that contains the details of a support case. It
                   contains fields for the time it was created, its
                   priority, its classification, and more. Cases can
                   also have comments and attachments that get added
                   over time.

                   A case is parented by a Google Cloud organization or
                   project.

                   Organizations are identified by a number, so the name
                   of a case parented by an organization would look like
                   this:

                   :literal:`` organizations/123/cases/456`\ \`

                   Projects have two unique identifiers, an ID and a
                   number, and they look like this:

                   :literal:`` projects/abc/cases/456`\ \`

                   :literal:`` projects/123/cases/456`\ \`

                   You can use either of them when calling the API. To
                   learn more about project identifiers, see
                   [AIP-2510](https://google.aip.dev/cloud/2510).

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, case_service.EscalateCaseRequest):
            request = case_service.EscalateCaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.escalate_case
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

    async def close_case(
        self,
        request: Optional[Union[case_service.CloseCaseRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> case.Case:
        r"""Close a case.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_close_case():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.CloseCaseRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.close_case(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.CloseCaseRequest, dict]]):
                The request object. The request message for the CloseCase
                endpoint.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.support_v2.types.Case:
                A Case is an object that contains the details of a support case. It
                   contains fields for the time it was created, its
                   priority, its classification, and more. Cases can
                   also have comments and attachments that get added
                   over time.

                   A case is parented by a Google Cloud organization or
                   project.

                   Organizations are identified by a number, so the name
                   of a case parented by an organization would look like
                   this:

                   :literal:`` organizations/123/cases/456`\ \`

                   Projects have two unique identifiers, an ID and a
                   number, and they look like this:

                   :literal:`` projects/abc/cases/456`\ \`

                   :literal:`` projects/123/cases/456`\ \`

                   You can use either of them when calling the API. To
                   learn more about project identifiers, see
                   [AIP-2510](https://google.aip.dev/cloud/2510).

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, case_service.CloseCaseRequest):
            request = case_service.CloseCaseRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.close_case
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

    async def search_case_classifications(
        self,
        request: Optional[
            Union[case_service.SearchCaseClassificationsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchCaseClassificationsAsyncPager:
        r"""Retrieve valid classifications to use when creating a support
        case.

        Classifications are hierarchical. Each classification is a
        string containing all levels of the hierarchy separated by
        ``" > "``. For example,
        ``"Technical Issue > Compute > Compute Engine"``.

        Classification IDs returned by this endpoint are valid for at
        least six months. When a classification is deactivated, this
        endpoint immediately stops returning it. After six months,
        ``case.create`` requests using the classification will fail.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import support_v2

            async def sample_search_case_classifications():
                # Create a client
                client = support_v2.CaseServiceAsyncClient()

                # Initialize request argument(s)
                request = support_v2.SearchCaseClassificationsRequest(
                )

                # Make the request
                page_result = client.search_case_classifications(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.support_v2.types.SearchCaseClassificationsRequest, dict]]):
                The request object. The request message for the
                SearchCaseClassifications endpoint.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.support_v2.services.case_service.pagers.SearchCaseClassificationsAsyncPager:
                The response message for
                SearchCaseClassifications endpoint.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, case_service.SearchCaseClassificationsRequest):
            request = case_service.SearchCaseClassificationsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_case_classifications
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
        response = pagers.SearchCaseClassificationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "CaseServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("CaseServiceAsyncClient",)
