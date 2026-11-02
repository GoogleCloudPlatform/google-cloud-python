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

from google.shopping.merchant_accounts_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.shopping.merchant_accounts_v1.types import (
    termsofserviceagreementstate,
    termsofservicekind,
)

from .client import TermsOfServiceAgreementStateServiceClient
from .transports.base import (
    DEFAULT_CLIENT_INFO,
    TermsOfServiceAgreementStateServiceTransport,
)
from .transports.grpc_asyncio import (
    TermsOfServiceAgreementStateServiceGrpcAsyncIOTransport,
)

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class TermsOfServiceAgreementStateServiceAsyncClient:
    """Service to support ``TermsOfServiceAgreementState`` API."""

    _client: TermsOfServiceAgreementStateServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = TermsOfServiceAgreementStateServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = (
        TermsOfServiceAgreementStateServiceClient.DEFAULT_MTLS_ENDPOINT
    )
    _DEFAULT_ENDPOINT_TEMPLATE = (
        TermsOfServiceAgreementStateServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    )
    _DEFAULT_UNIVERSE = TermsOfServiceAgreementStateServiceClient._DEFAULT_UNIVERSE

    account_path = staticmethod(TermsOfServiceAgreementStateServiceClient.account_path)
    parse_account_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_account_path
    )
    terms_of_service_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.terms_of_service_path
    )
    parse_terms_of_service_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_terms_of_service_path
    )
    terms_of_service_agreement_state_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.terms_of_service_agreement_state_path
    )
    parse_terms_of_service_agreement_state_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_terms_of_service_agreement_state_path
    )
    common_billing_account_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.common_folder_path
    )
    parse_common_folder_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        TermsOfServiceAgreementStateServiceClient.parse_common_location_path
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
            TermsOfServiceAgreementStateServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            TermsOfServiceAgreementStateServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(
            TermsOfServiceAgreementStateServiceAsyncClient, info, *args, **kwargs
        )

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
            TermsOfServiceAgreementStateServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            TermsOfServiceAgreementStateServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(
            TermsOfServiceAgreementStateServiceAsyncClient, filename, *args, **kwargs
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
        return (
            TermsOfServiceAgreementStateServiceClient.get_mtls_endpoint_and_cert_source(
                client_options
            )
        )  # type: ignore

    @property
    def transport(self) -> TermsOfServiceAgreementStateServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            TermsOfServiceAgreementStateServiceTransport: The transport used by the client instance.
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

    get_transport_class = TermsOfServiceAgreementStateServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                TermsOfServiceAgreementStateServiceTransport,
                Callable[..., TermsOfServiceAgreementStateServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the terms of service agreement state service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,TermsOfServiceAgreementStateServiceTransport,Callable[..., TermsOfServiceAgreementStateServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the TermsOfServiceAgreementStateServiceTransport constructor.
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
        self._client = TermsOfServiceAgreementStateServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.shopping.merchant.accounts_v1.TermsOfServiceAgreementStateServiceAsyncClient`.",
                extra={
                    "serviceName": "google.shopping.merchant.accounts.v1.TermsOfServiceAgreementStateService",
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
                    "serviceName": "google.shopping.merchant.accounts.v1.TermsOfServiceAgreementStateService",
                    "credentialsType": None,
                },
            )

    async def get_terms_of_service_agreement_state(
        self,
        request: Optional[
            Union[
                termsofserviceagreementstate.GetTermsOfServiceAgreementStateRequest,
                dict,
            ]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> termsofserviceagreementstate.TermsOfServiceAgreementState:
        r"""Returns the state of a terms of service agreement.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_get_terms_of_service_agreement_state():
                # Create a client
                client = merchant_accounts_v1.TermsOfServiceAgreementStateServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.GetTermsOfServiceAgreementStateRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_terms_of_service_agreement_state(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.GetTermsOfServiceAgreementStateRequest, dict]]):
                The request object. Request message for the
                ``GetTermsOfServiceAgreementState`` method.
            name (:class:`str`):
                Required. The resource name of the terms of service
                version. Format:
                ``accounts/{account}/termsOfServiceAgreementStates/{identifier}``
                The identifier format is:
                ``{TermsOfServiceKind}-{country}``

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
            google.shopping.merchant_accounts_v1.types.TermsOfServiceAgreementState:
                This resource represents the agreement state for a given account and terms of
                   service kind. The state is as follows:

                   \* If the business has accepted a terms of service,
                   [accepted][google.shopping.merchant.accounts.v1.Accepted]
                   will be populated, otherwise it will be empty \* If
                   the business must sign a terms of service,
                   [required][google.shopping.merchant.accounts.v1.Required]
                   will be populated, otherwise it will be empty.

                   Note that both required and accepted can be present.
                   In this case the accepted terms of services will have
                   an expiration date set in the
                   [valid_until][google.shopping.merchant.accounts.v1.Accepted.valid_until]
                   field. The required terms of services need to be
                   accepted before valid_until in order for the account
                   to continue having a valid agreement. When accepting
                   new terms of services we expect third-party providers
                   to display the text associated with the given terms
                   of service agreement (the url to the file containing
                   the text is added in the Required message below as
                   [tos_file_uri][google.shopping.merchant.accounts.v1.Required.tos_file_uri]).
                   The actual acceptance of the terms of service is done
                   by calling accept on the
                   [TermsOfService][google.shopping.merchant.accounts.v1.Accepted.terms_of_service]
                   resource. valid_until field.

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
            request, termsofserviceagreementstate.GetTermsOfServiceAgreementStateRequest
        ):
            request = (
                termsofserviceagreementstate.GetTermsOfServiceAgreementStateRequest(
                    request
                )
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_terms_of_service_agreement_state
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

    async def retrieve_for_application_terms_of_service_agreement_state(
        self,
        request: Optional[
            Union[
                termsofserviceagreementstate.RetrieveForApplicationTermsOfServiceAgreementStateRequest,
                dict,
            ]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> termsofserviceagreementstate.TermsOfServiceAgreementState:
        r"""Retrieves the state of the agreement for the
        application terms of service.
        Application terms of service covers permissions related
        to the usage of data provided through Merchant Center,
        CSS Center, Manufacturer Center, and more.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.shopping import merchant_accounts_v1

            async def sample_retrieve_for_application_terms_of_service_agreement_state():
                # Create a client
                client = merchant_accounts_v1.TermsOfServiceAgreementStateServiceAsyncClient()

                # Initialize request argument(s)
                request = merchant_accounts_v1.RetrieveForApplicationTermsOfServiceAgreementStateRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.retrieve_for_application_terms_of_service_agreement_state(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.shopping.merchant_accounts_v1.types.RetrieveForApplicationTermsOfServiceAgreementStateRequest, dict]]):
                The request object. Request message for the
                ``RetrieveForApplicationTermsOfServiceAgreementState``
                method.
            parent (:class:`str`):
                Required. The account for which to get a
                TermsOfServiceAgreementState Format:
                ``accounts/{account}``

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
            google.shopping.merchant_accounts_v1.types.TermsOfServiceAgreementState:
                This resource represents the agreement state for a given account and terms of
                   service kind. The state is as follows:

                   \* If the business has accepted a terms of service,
                   [accepted][google.shopping.merchant.accounts.v1.Accepted]
                   will be populated, otherwise it will be empty \* If
                   the business must sign a terms of service,
                   [required][google.shopping.merchant.accounts.v1.Required]
                   will be populated, otherwise it will be empty.

                   Note that both required and accepted can be present.
                   In this case the accepted terms of services will have
                   an expiration date set in the
                   [valid_until][google.shopping.merchant.accounts.v1.Accepted.valid_until]
                   field. The required terms of services need to be
                   accepted before valid_until in order for the account
                   to continue having a valid agreement. When accepting
                   new terms of services we expect third-party providers
                   to display the text associated with the given terms
                   of service agreement (the url to the file containing
                   the text is added in the Required message below as
                   [tos_file_uri][google.shopping.merchant.accounts.v1.Required.tos_file_uri]).
                   The actual acceptance of the terms of service is done
                   by calling accept on the
                   [TermsOfService][google.shopping.merchant.accounts.v1.Accepted.terms_of_service]
                   resource. valid_until field.

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
            request,
            termsofserviceagreementstate.RetrieveForApplicationTermsOfServiceAgreementStateRequest,
        ):
            request = termsofserviceagreementstate.RetrieveForApplicationTermsOfServiceAgreementStateRequest(
                request
            )

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.retrieve_for_application_terms_of_service_agreement_state
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

    async def __aenter__(self) -> "TermsOfServiceAgreementStateServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("TermsOfServiceAgreementStateServiceAsyncClient",)
