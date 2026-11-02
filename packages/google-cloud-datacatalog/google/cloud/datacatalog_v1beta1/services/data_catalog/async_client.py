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
import warnings
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

from google.cloud.datacatalog_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
import google.iam.v1.policy_pb2 as policy_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.datacatalog_v1beta1.services.data_catalog import pagers
from google.cloud.datacatalog_v1beta1.types import (
    common,
    datacatalog,
    gcs_fileset_spec,
    schema,
    search,
    table_spec,
    tags,
    timestamps,
    usage,
)

from .client import DataCatalogClient
from .transports.base import DEFAULT_CLIENT_INFO, DataCatalogTransport
from .transports.grpc_asyncio import DataCatalogGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DataCatalogAsyncClient:
    """Deprecated: Please use Dataplex Catalog instead.

    Data Catalog API service allows clients to discover, understand,
    and manage their data.
    """

    _client: DataCatalogClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataCatalogClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataCatalogClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DataCatalogClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DataCatalogClient._DEFAULT_UNIVERSE

    entry_path = staticmethod(DataCatalogClient.entry_path)
    parse_entry_path = staticmethod(DataCatalogClient.parse_entry_path)
    entry_group_path = staticmethod(DataCatalogClient.entry_group_path)
    parse_entry_group_path = staticmethod(DataCatalogClient.parse_entry_group_path)
    tag_path = staticmethod(DataCatalogClient.tag_path)
    parse_tag_path = staticmethod(DataCatalogClient.parse_tag_path)
    tag_template_path = staticmethod(DataCatalogClient.tag_template_path)
    parse_tag_template_path = staticmethod(DataCatalogClient.parse_tag_template_path)
    tag_template_field_path = staticmethod(DataCatalogClient.tag_template_field_path)
    parse_tag_template_field_path = staticmethod(
        DataCatalogClient.parse_tag_template_field_path
    )
    tag_template_field_enum_value_path = staticmethod(
        DataCatalogClient.tag_template_field_enum_value_path
    )
    parse_tag_template_field_enum_value_path = staticmethod(
        DataCatalogClient.parse_tag_template_field_enum_value_path
    )
    common_billing_account_path = staticmethod(
        DataCatalogClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataCatalogClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataCatalogClient.common_folder_path)
    parse_common_folder_path = staticmethod(DataCatalogClient.parse_common_folder_path)
    common_organization_path = staticmethod(DataCatalogClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        DataCatalogClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DataCatalogClient.common_project_path)
    parse_common_project_path = staticmethod(
        DataCatalogClient.parse_common_project_path
    )
    common_location_path = staticmethod(DataCatalogClient.common_location_path)
    parse_common_location_path = staticmethod(
        DataCatalogClient.parse_common_location_path
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
            DataCatalogAsyncClient: The constructed client.
        """
        sa_info_func = (
            DataCatalogClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DataCatalogAsyncClient, info, *args, **kwargs)

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
            DataCatalogAsyncClient: The constructed client.
        """
        sa_file_func = (
            DataCatalogClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DataCatalogAsyncClient, filename, *args, **kwargs)

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
        return DataCatalogClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DataCatalogTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataCatalogTransport: The transport used by the client instance.
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

    get_transport_class = DataCatalogClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[str, DataCatalogTransport, Callable[..., DataCatalogTransport]]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data catalog async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataCatalogTransport,Callable[..., DataCatalogTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataCatalogTransport constructor.
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
        self._client = DataCatalogClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.datacatalog_v1beta1.DataCatalogAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.datacatalog.v1beta1.DataCatalog",
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
                    "serviceName": "google.cloud.datacatalog.v1beta1.DataCatalog",
                    "credentialsType": None,
                },
            )

    async def search_catalog(
        self,
        request: Optional[Union[datacatalog.SearchCatalogRequest, dict]] = None,
        *,
        scope: Optional[datacatalog.SearchCatalogRequest.Scope] = None,
        query: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchCatalogAsyncPager:
        r"""Searches Data Catalog for multiple resources like entries, tags
        that match a query.

        This is a custom method
        (https://cloud.google.com/apis/design/custom_methods) and does
        not return the complete resource, only the resource identifier
        and high level fields. Clients can subsequently call ``Get``
        methods.

        Note that Data Catalog search queries do not guarantee full
        recall. Query results that match your query may not be returned,
        even in subsequent result pages. Also note that results returned
        (and not returned) can vary across repeated search queries.

        See `Data Catalog Search
        Syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__
        for more information.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_search_catalog():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.SearchCatalogRequest(
                )

                # Make the request
                page_result = client.search_catalog(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.SearchCatalogRequest, dict]]):
                The request object. Request message for
                [SearchCatalog][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog].
            scope (:class:`google.cloud.datacatalog_v1beta1.types.SearchCatalogRequest.Scope`):
                Required. The scope of this search request. A ``scope``
                that has empty ``include_org_ids``,
                ``include_project_ids`` AND false
                ``include_gcp_public_datasets`` is considered invalid.
                Data Catalog will return an error in such a case.

                This corresponds to the ``scope`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            query (:class:`str`):
                Optional. The query string in search query syntax. An
                empty query string will result in all data assets (in
                the specified scope) that the user has access to. Query
                strings can be simple as "x" or more qualified as:

                - name:x
                - column:x
                - description:y

                Note: Query tokens need to have a minimum of 3
                characters for substring matching to work correctly. See
                `Data Catalog Search
                Syntax <https://cloud.google.com/data-catalog/docs/how-to/search-reference>`__
                for more information.

                This corresponds to the ``query`` field
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
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.SearchCatalogAsyncPager:
                Response message for
                   [SearchCatalog][google.cloud.datacatalog.v1beta1.DataCatalog.SearchCatalog].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "DataCatalogAsyncClient.search_catalog is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [scope, query]
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
        if not isinstance(request, datacatalog.SearchCatalogRequest):
            request = datacatalog.SearchCatalogRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if scope is not None:
            request.scope = scope
        if query is not None:
            request.query = query

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_catalog
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
        response = pagers.SearchCatalogAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_entry_group(
        self,
        request: Optional[Union[datacatalog.CreateEntryGroupRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        entry_group_id: Optional[str] = None,
        entry_group: Optional[datacatalog.EntryGroup] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.EntryGroup:
        r"""A maximum of 10,000 entry groups may be created per organization
        across all locations.

        Users should enable the Data Catalog API in the project
        identified by the ``parent`` parameter (see [Data Catalog
        Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_create_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.CreateEntryGroupRequest(
                    parent="parent_value",
                    entry_group_id="entry_group_id_value",
                )

                # Make the request
                response = await client.create_entry_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.CreateEntryGroupRequest, dict]]):
                The request object. Request message for
                [CreateEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntryGroup].
            parent (:class:`str`):
                Required. The name of the project this entry group is
                in. Example:

                - projects/{project_id}/locations/{location}

                Note that this EntryGroup and its child resources may
                not actually be stored in the location in this name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry_group_id (:class:`str`):
                Required. The id of the entry group
                to create. The id must begin with a
                letter or underscore, contain only
                English letters, numbers and
                underscores, and be at most 64
                characters.

                This corresponds to the ``entry_group_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry_group (:class:`google.cloud.datacatalog_v1beta1.types.EntryGroup`):
                The entry group to create. Defaults
                to an empty entry group.

                This corresponds to the ``entry_group`` field
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
            google.cloud.datacatalog_v1beta1.types.EntryGroup:
                EntryGroup Metadata.
                   An EntryGroup resource represents a logical grouping
                   of zero or more Data Catalog
                   [Entry][google.cloud.datacatalog.v1beta1.Entry]
                   resources.

        """
        warnings.warn(
            "DataCatalogAsyncClient.create_entry_group is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, entry_group_id, entry_group]
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
        if not isinstance(request, datacatalog.CreateEntryGroupRequest):
            request = datacatalog.CreateEntryGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if entry_group_id is not None:
            request.entry_group_id = entry_group_id
        if entry_group is not None:
            request.entry_group = entry_group

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_entry_group
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

    async def update_entry_group(
        self,
        request: Optional[Union[datacatalog.UpdateEntryGroupRequest, dict]] = None,
        *,
        entry_group: Optional[datacatalog.EntryGroup] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.EntryGroup:
        r"""Updates an EntryGroup. The user should enable the Data Catalog
        API in the project identified by the ``entry_group.name``
        parameter (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_update_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.UpdateEntryGroupRequest(
                )

                # Make the request
                response = await client.update_entry_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.UpdateEntryGroupRequest, dict]]):
                The request object. Request message for
                [UpdateEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateEntryGroup].
            entry_group (:class:`google.cloud.datacatalog_v1beta1.types.EntryGroup`):
                Required. The updated entry group.
                "name" field must be set.

                This corresponds to the ``entry_group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Names of fields whose values to
                overwrite on an entry group.
                If this parameter is absent or empty,
                all modifiable fields are overwritten.
                If such fields are non-required and
                omitted in the request body, their
                values are emptied.

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
            google.cloud.datacatalog_v1beta1.types.EntryGroup:
                EntryGroup Metadata.
                   An EntryGroup resource represents a logical grouping
                   of zero or more Data Catalog
                   [Entry][google.cloud.datacatalog.v1beta1.Entry]
                   resources.

        """
        warnings.warn(
            "DataCatalogAsyncClient.update_entry_group is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [entry_group, update_mask]
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
        if not isinstance(request, datacatalog.UpdateEntryGroupRequest):
            request = datacatalog.UpdateEntryGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if entry_group is not None:
            request.entry_group = entry_group
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_entry_group
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entry_group.name", request.entry_group.name),)
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

    async def get_entry_group(
        self,
        request: Optional[Union[datacatalog.GetEntryGroupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        read_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.EntryGroup:
        r"""Gets an EntryGroup.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_get_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.GetEntryGroupRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_entry_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.GetEntryGroupRequest, dict]]):
                The request object. Request message for
                [GetEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.GetEntryGroup].
            name (:class:`str`):
                Required. The name of the entry group. For example,
                ``projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}``.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            read_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                The fields to return. If not set or
                empty, all fields are returned.

                This corresponds to the ``read_mask`` field
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
            google.cloud.datacatalog_v1beta1.types.EntryGroup:
                EntryGroup Metadata.
                   An EntryGroup resource represents a logical grouping
                   of zero or more Data Catalog
                   [Entry][google.cloud.datacatalog.v1beta1.Entry]
                   resources.

        """
        warnings.warn(
            "DataCatalogAsyncClient.get_entry_group is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, read_mask]
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
        if not isinstance(request, datacatalog.GetEntryGroupRequest):
            request = datacatalog.GetEntryGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if read_mask is not None:
            request.read_mask = read_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_entry_group
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

    async def delete_entry_group(
        self,
        request: Optional[Union[datacatalog.DeleteEntryGroupRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an EntryGroup. Only entry groups that do not contain
        entries can be deleted. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_delete_entry_group():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteEntryGroupRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_entry_group(request=request)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.DeleteEntryGroupRequest, dict]]):
                The request object. Request message for
                [DeleteEntryGroup][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteEntryGroup].
            name (:class:`str`):
                Required. The name of the entry group. For example,
                ``projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}``.

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
        warnings.warn(
            "DataCatalogAsyncClient.delete_entry_group is deprecated",
            DeprecationWarning,
        )

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
        if not isinstance(request, datacatalog.DeleteEntryGroupRequest):
            request = datacatalog.DeleteEntryGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_entry_group
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

    async def list_entry_groups(
        self,
        request: Optional[Union[datacatalog.ListEntryGroupsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEntryGroupsAsyncPager:
        r"""Lists entry groups.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_list_entry_groups():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.ListEntryGroupsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entry_groups(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.ListEntryGroupsRequest, dict]]):
                The request object. Request message for
                [ListEntryGroups][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntryGroups].
            parent (:class:`str`):
                Required. The name of the location that contains the
                entry groups, which can be provided in URL format.
                Example:

                - projects/{project_id}/locations/{location}

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
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.ListEntryGroupsAsyncPager:
                Response message for
                   [ListEntryGroups][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntryGroups].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "DataCatalogAsyncClient.list_entry_groups is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.ListEntryGroupsRequest):
            request = datacatalog.ListEntryGroupsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_entry_groups
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
        response = pagers.ListEntryGroupsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_entry(
        self,
        request: Optional[Union[datacatalog.CreateEntryRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        entry_id: Optional[str] = None,
        entry: Optional[datacatalog.Entry] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.Entry:
        r"""Creates an entry. Only entries of 'FILESET' type or
        user-specified type can be created.

        Users should enable the Data Catalog API in the project
        identified by the ``parent`` parameter (see [Data Catalog
        Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        A maximum of 100,000 entries may be created per entry group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_create_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                entry = datacatalog_v1beta1.Entry()
                entry.type_ = "FILESET"
                entry.integrated_system = "CLOUD_PUBSUB"
                entry.gcs_fileset_spec.file_patterns = ['file_patterns_value1', 'file_patterns_value2']

                request = datacatalog_v1beta1.CreateEntryRequest(
                    parent="parent_value",
                    entry_id="entry_id_value",
                    entry=entry,
                )

                # Make the request
                response = await client.create_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.CreateEntryRequest, dict]]):
                The request object. Request message for
                [CreateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntry].
            parent (:class:`str`):
                Required. The name of the entry group this entry is in.
                Example:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

                Note that this Entry and its child resources may not
                actually be stored in the location in this name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry_id (:class:`str`):
                Required. The id of the entry to
                create.

                This corresponds to the ``entry_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entry (:class:`google.cloud.datacatalog_v1beta1.types.Entry`):
                Required. The entry to create.
                This corresponds to the ``entry`` field
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
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        warnings.warn(
            "DataCatalogAsyncClient.create_entry is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, entry_id, entry]
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
        if not isinstance(request, datacatalog.CreateEntryRequest):
            request = datacatalog.CreateEntryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if entry_id is not None:
            request.entry_id = entry_id
        if entry is not None:
            request.entry = entry

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_entry
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

    async def update_entry(
        self,
        request: Optional[Union[datacatalog.UpdateEntryRequest, dict]] = None,
        *,
        entry: Optional[datacatalog.Entry] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.Entry:
        r"""Updates an existing entry. Users should enable the Data Catalog
        API in the project identified by the ``entry.name`` parameter
        (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_update_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                entry = datacatalog_v1beta1.Entry()
                entry.type_ = "FILESET"
                entry.integrated_system = "CLOUD_PUBSUB"
                entry.gcs_fileset_spec.file_patterns = ['file_patterns_value1', 'file_patterns_value2']

                request = datacatalog_v1beta1.UpdateEntryRequest(
                    entry=entry,
                )

                # Make the request
                response = await client.update_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.UpdateEntryRequest, dict]]):
                The request object. Request message for
                [UpdateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateEntry].
            entry (:class:`google.cloud.datacatalog_v1beta1.types.Entry`):
                Required. The updated entry. The
                "name" field must be set.

                This corresponds to the ``entry`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Names of fields whose values to overwrite on an entry.

                If this parameter is absent or empty, all modifiable
                fields are overwritten. If such fields are non-required
                and omitted in the request body, their values are
                emptied.

                The following fields are modifiable:

                - For entries with type ``DATA_STREAM``:

                  - ``schema``

                - For entries with type ``FILESET``:

                  - ``schema``
                  - ``display_name``
                  - ``description``
                  - ``gcs_fileset_spec``
                  - ``gcs_fileset_spec.file_patterns``

                - For entries with ``user_specified_type``:

                  - ``schema``
                  - ``display_name``
                  - ``description``
                  - ``user_specified_type``
                  - ``user_specified_system``
                  - ``linked_resource``
                  - ``source_system_timestamps``

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
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        warnings.warn(
            "DataCatalogAsyncClient.update_entry is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [entry, update_mask]
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
        if not isinstance(request, datacatalog.UpdateEntryRequest):
            request = datacatalog.UpdateEntryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if entry is not None:
            request.entry = entry
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_entry
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entry.name", request.entry.name),)
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

    async def delete_entry(
        self,
        request: Optional[Union[datacatalog.DeleteEntryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an existing entry. Only entries created through
        [CreateEntry][google.cloud.datacatalog.v1beta1.DataCatalog.CreateEntry]
        method can be deleted. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_delete_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteEntryRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_entry(request=request)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.DeleteEntryRequest, dict]]):
                The request object. Request message for
                [DeleteEntry][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteEntry].
            name (:class:`str`):
                Required. The name of the entry. Example:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

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
        warnings.warn(
            "DataCatalogAsyncClient.delete_entry is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.DeleteEntryRequest):
            request = datacatalog.DeleteEntryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_entry
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

    async def get_entry(
        self,
        request: Optional[Union[datacatalog.GetEntryRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.Entry:
        r"""Gets an entry.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_get_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.GetEntryRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.GetEntryRequest, dict]]):
                The request object. Request message for
                [GetEntry][google.cloud.datacatalog.v1beta1.DataCatalog.GetEntry].
            name (:class:`str`):
                Required. The name of the entry. Example:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

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
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        warnings.warn(
            "DataCatalogAsyncClient.get_entry is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.GetEntryRequest):
            request = datacatalog.GetEntryRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_entry
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

    async def lookup_entry(
        self,
        request: Optional[Union[datacatalog.LookupEntryRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> datacatalog.Entry:
        r"""Get an entry by target resource name. This method
        allows clients to use the resource name from the source
        Google Cloud Platform service to get the Data Catalog
        Entry.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_lookup_entry():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.LookupEntryRequest(
                    linked_resource="linked_resource_value",
                )

                # Make the request
                response = await client.lookup_entry(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.LookupEntryRequest, dict]]):
                The request object. Request message for
                [LookupEntry][google.cloud.datacatalog.v1beta1.DataCatalog.LookupEntry].
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.datacatalog_v1beta1.types.Entry:
                Entry Metadata.
                   A Data Catalog Entry resource represents another
                   resource in Google Cloud Platform (such as a BigQuery
                   dataset or a Pub/Sub topic), or outside of Google
                   Cloud Platform. Clients can use the linked_resource
                   field in the Entry resource to refer to the original
                   resource ID of the source system.

                   An Entry resource contains resource details, such as
                   its schema. An Entry can also be used to attach
                   flexible metadata, such as a
                   [Tag][google.cloud.datacatalog.v1beta1.Tag].

        """
        warnings.warn(
            "DataCatalogAsyncClient.lookup_entry is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, datacatalog.LookupEntryRequest):
            request = datacatalog.LookupEntryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.lookup_entry
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

        # Done; return the response.
        return response

    async def list_entries(
        self,
        request: Optional[Union[datacatalog.ListEntriesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEntriesAsyncPager:
        r"""Lists entries.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_list_entries():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.ListEntriesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entries(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.ListEntriesRequest, dict]]):
                The request object. Request message for
                [ListEntries][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntries].
            parent (:class:`str`):
                Required. The name of the entry group that contains the
                entries, which can be provided in URL format. Example:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}

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
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.ListEntriesAsyncPager:
                Response message for
                   [ListEntries][google.cloud.datacatalog.v1beta1.DataCatalog.ListEntries].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "DataCatalogAsyncClient.list_entries is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.ListEntriesRequest):
            request = datacatalog.ListEntriesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_entries
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
        response = pagers.ListEntriesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_tag_template(
        self,
        request: Optional[Union[datacatalog.CreateTagTemplateRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        tag_template_id: Optional[str] = None,
        tag_template: Optional[tags.TagTemplate] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplate:
        r"""Creates a tag template. The user should enable the Data Catalog
        API in the project identified by the ``parent`` parameter (see
        `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_create_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.CreateTagTemplateRequest(
                    parent="parent_value",
                    tag_template_id="tag_template_id_value",
                )

                # Make the request
                response = await client.create_tag_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.CreateTagTemplateRequest, dict]]):
                The request object. Request message for
                [CreateTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTagTemplate].
            parent (:class:`str`):
                Required. The name of the project and the template
                location
                [region](https://cloud.google.com/data-catalog/docs/concepts/regions.

                Example:

                - projects/{project_id}/locations/us-central1

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_id (:class:`str`):
                Required. The id of the tag template
                to create.

                This corresponds to the ``tag_template_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template (:class:`google.cloud.datacatalog_v1beta1.types.TagTemplate`):
                Required. The tag template to create.
                This corresponds to the ``tag_template`` field
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
            google.cloud.datacatalog_v1beta1.types.TagTemplate:
                A tag template defines a tag, which can have one or more typed fields.
                   The template is used to create and attach the tag to
                   Google Cloud resources. [Tag template
                   roles](https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
                   provide permissions to create, edit, and use the
                   template. See, for example, the [TagTemplate
                   User](https://cloud.google.com/data-catalog/docs/how-to/template-user)
                   role, which includes permission to use the tag
                   template to tag resources.

        """
        warnings.warn(
            "DataCatalogAsyncClient.create_tag_template is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, tag_template_id, tag_template]
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
        if not isinstance(request, datacatalog.CreateTagTemplateRequest):
            request = datacatalog.CreateTagTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if tag_template_id is not None:
            request.tag_template_id = tag_template_id
        if tag_template is not None:
            request.tag_template = tag_template

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_tag_template
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

    async def get_tag_template(
        self,
        request: Optional[Union[datacatalog.GetTagTemplateRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplate:
        r"""Gets a tag template.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_get_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.GetTagTemplateRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_tag_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.GetTagTemplateRequest, dict]]):
                The request object. Request message for
                [GetTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.GetTagTemplate].
            name (:class:`str`):
                Required. The name of the tag template. Example:

                - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

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
            google.cloud.datacatalog_v1beta1.types.TagTemplate:
                A tag template defines a tag, which can have one or more typed fields.
                   The template is used to create and attach the tag to
                   Google Cloud resources. [Tag template
                   roles](https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
                   provide permissions to create, edit, and use the
                   template. See, for example, the [TagTemplate
                   User](https://cloud.google.com/data-catalog/docs/how-to/template-user)
                   role, which includes permission to use the tag
                   template to tag resources.

        """
        warnings.warn(
            "DataCatalogAsyncClient.get_tag_template is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.GetTagTemplateRequest):
            request = datacatalog.GetTagTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_tag_template
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

    async def update_tag_template(
        self,
        request: Optional[Union[datacatalog.UpdateTagTemplateRequest, dict]] = None,
        *,
        tag_template: Optional[tags.TagTemplate] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplate:
        r"""Updates a tag template. This method cannot be used to update the
        fields of a template. The tag template fields are represented as
        separate resources and should be updated using their own
        create/update/delete methods. Users should enable the Data
        Catalog API in the project identified by the
        ``tag_template.name`` parameter (see [Data Catalog Resource
        Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_update_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.UpdateTagTemplateRequest(
                )

                # Make the request
                response = await client.update_tag_template(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.UpdateTagTemplateRequest, dict]]):
                The request object. Request message for
                [UpdateTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTagTemplate].
            tag_template (:class:`google.cloud.datacatalog_v1beta1.types.TagTemplate`):
                Required. The template to update. The
                "name" field must be set.

                This corresponds to the ``tag_template`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Names of fields whose values to overwrite on a tag
                template. Currently, only ``display_name`` can be
                overwritten.

                In general, if this parameter is absent or empty, all
                modifiable fields are overwritten. If such fields are
                non-required and omitted in the request body, their
                values are emptied.

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
            google.cloud.datacatalog_v1beta1.types.TagTemplate:
                A tag template defines a tag, which can have one or more typed fields.
                   The template is used to create and attach the tag to
                   Google Cloud resources. [Tag template
                   roles](https://cloud.google.com/iam/docs/understanding-roles#data-catalog-roles)
                   provide permissions to create, edit, and use the
                   template. See, for example, the [TagTemplate
                   User](https://cloud.google.com/data-catalog/docs/how-to/template-user)
                   role, which includes permission to use the tag
                   template to tag resources.

        """
        warnings.warn(
            "DataCatalogAsyncClient.update_tag_template is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [tag_template, update_mask]
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
        if not isinstance(request, datacatalog.UpdateTagTemplateRequest):
            request = datacatalog.UpdateTagTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if tag_template is not None:
            request.tag_template = tag_template
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_tag_template
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("tag_template.name", request.tag_template.name),)
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

    async def delete_tag_template(
        self,
        request: Optional[Union[datacatalog.DeleteTagTemplateRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        force: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a tag template and all tags using the template. Users
        should enable the Data Catalog API in the project identified by
        the ``name`` parameter (see [Data Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_delete_tag_template():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteTagTemplateRequest(
                    name="name_value",
                    force=True,
                )

                # Make the request
                await client.delete_tag_template(request=request)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.DeleteTagTemplateRequest, dict]]):
                The request object. Request message for
                [DeleteTagTemplate][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTagTemplate].
            name (:class:`str`):
                Required. The name of the tag template to delete.
                Example:

                - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (:class:`bool`):
                Required. Currently, this field must always be set to
                ``true``. This confirms the deletion of any possible
                tags using this template. ``force = false`` will be
                supported in the future.

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
        """
        warnings.warn(
            "DataCatalogAsyncClient.delete_tag_template is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, force]
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
        if not isinstance(request, datacatalog.DeleteTagTemplateRequest):
            request = datacatalog.DeleteTagTemplateRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if force is not None:
            request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_tag_template
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

    async def create_tag_template_field(
        self,
        request: Optional[
            Union[datacatalog.CreateTagTemplateFieldRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        tag_template_field_id: Optional[str] = None,
        tag_template_field: Optional[tags.TagTemplateField] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplateField:
        r"""Creates a field in a tag template. The user should enable the
        Data Catalog API in the project identified by the ``parent``
        parameter (see `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_create_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                tag_template_field = datacatalog_v1beta1.TagTemplateField()
                tag_template_field.type_.primitive_type = "TIMESTAMP"

                request = datacatalog_v1beta1.CreateTagTemplateFieldRequest(
                    parent="parent_value",
                    tag_template_field_id="tag_template_field_id_value",
                    tag_template_field=tag_template_field,
                )

                # Make the request
                response = await client.create_tag_template_field(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.CreateTagTemplateFieldRequest, dict]]):
                The request object. Request message for
                [CreateTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTagTemplateField].
            parent (:class:`str`):
                Required. The name of the project and the template
                location
                `region <https://cloud.google.com/data-catalog/docs/concepts/regions>`__.

                Example:

                - projects/{project_id}/locations/us-central1/tagTemplates/{tag_template_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_field_id (:class:`str`):
                Required. The ID of the tag template field to create.
                Field ids can contain letters (both uppercase and
                lowercase), numbers (0-9), underscores (\_) and dashes
                (-). Field IDs must be at least 1 character long and at
                most 128 characters long. Field IDs must also be unique
                within their template.

                This corresponds to the ``tag_template_field_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_field (:class:`google.cloud.datacatalog_v1beta1.types.TagTemplateField`):
                Required. The tag template field to
                create.

                This corresponds to the ``tag_template_field`` field
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
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        warnings.warn(
            "DataCatalogAsyncClient.create_tag_template_field is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, tag_template_field_id, tag_template_field]
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
        if not isinstance(request, datacatalog.CreateTagTemplateFieldRequest):
            request = datacatalog.CreateTagTemplateFieldRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if tag_template_field_id is not None:
            request.tag_template_field_id = tag_template_field_id
        if tag_template_field is not None:
            request.tag_template_field = tag_template_field

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_tag_template_field
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

    async def update_tag_template_field(
        self,
        request: Optional[
            Union[datacatalog.UpdateTagTemplateFieldRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        tag_template_field: Optional[tags.TagTemplateField] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplateField:
        r"""Updates a field in a tag template. This method cannot be used to
        update the field type. Users should enable the Data Catalog API
        in the project identified by the ``name`` parameter (see [Data
        Catalog Resource Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_update_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                tag_template_field = datacatalog_v1beta1.TagTemplateField()
                tag_template_field.type_.primitive_type = "TIMESTAMP"

                request = datacatalog_v1beta1.UpdateTagTemplateFieldRequest(
                    name="name_value",
                    tag_template_field=tag_template_field,
                )

                # Make the request
                response = await client.update_tag_template_field(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.UpdateTagTemplateFieldRequest, dict]]):
                The request object. Request message for
                [UpdateTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTagTemplateField].
            name (:class:`str`):
                Required. The name of the tag template field. Example:

                - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag_template_field (:class:`google.cloud.datacatalog_v1beta1.types.TagTemplateField`):
                Required. The template to update.
                This corresponds to the ``tag_template_field`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Names of fields whose values to overwrite on
                an individual field of a tag template. The following
                fields are modifiable:

                - ``display_name``
                - ``type.enum_type``
                - ``is_required``

                If this parameter is absent or empty, all modifiable
                fields are overwritten. If such fields are non-required
                and omitted in the request body, their values are
                emptied with one exception: when updating an enum type,
                the provided values are merged with the existing values.
                Therefore, enum values can only be added, existing enum
                values cannot be deleted or renamed.

                Additionally, updating a template field from optional to
                required is *not* allowed.

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
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        warnings.warn(
            "DataCatalogAsyncClient.update_tag_template_field is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, tag_template_field, update_mask]
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
        if not isinstance(request, datacatalog.UpdateTagTemplateFieldRequest):
            request = datacatalog.UpdateTagTemplateFieldRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if tag_template_field is not None:
            request.tag_template_field = tag_template_field
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_tag_template_field
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

    async def rename_tag_template_field(
        self,
        request: Optional[
            Union[datacatalog.RenameTagTemplateFieldRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        new_tag_template_field_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplateField:
        r"""Renames a field in a tag template. The user should enable the
        Data Catalog API in the project identified by the ``name``
        parameter (see `Data Catalog Resource
        Project <https://cloud.google.com/data-catalog/docs/concepts/resource-project>`__
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_rename_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.RenameTagTemplateFieldRequest(
                    name="name_value",
                    new_tag_template_field_id="new_tag_template_field_id_value",
                )

                # Make the request
                response = await client.rename_tag_template_field(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.RenameTagTemplateFieldRequest, dict]]):
                The request object. Request message for
                [RenameTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.RenameTagTemplateField].
            name (:class:`str`):
                Required. The name of the tag template. Example:

                - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            new_tag_template_field_id (:class:`str`):
                Required. The new ID of this tag template field. For
                example, ``my_new_field``.

                This corresponds to the ``new_tag_template_field_id`` field
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
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        warnings.warn(
            "DataCatalogAsyncClient.rename_tag_template_field is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, new_tag_template_field_id]
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
        if not isinstance(request, datacatalog.RenameTagTemplateFieldRequest):
            request = datacatalog.RenameTagTemplateFieldRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if new_tag_template_field_id is not None:
            request.new_tag_template_field_id = new_tag_template_field_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.rename_tag_template_field
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

    async def rename_tag_template_field_enum_value(
        self,
        request: Optional[
            Union[datacatalog.RenameTagTemplateFieldEnumValueRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        new_enum_value_display_name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.TagTemplateField:
        r"""Renames an enum value in a tag template. The enum
        values have to be unique within one enum field. Thus, an
        enum value cannot be renamed with a name used in any
        other enum value within the same enum field.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_rename_tag_template_field_enum_value():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.RenameTagTemplateFieldEnumValueRequest(
                    name="name_value",
                    new_enum_value_display_name="new_enum_value_display_name_value",
                )

                # Make the request
                response = await client.rename_tag_template_field_enum_value(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.RenameTagTemplateFieldEnumValueRequest, dict]]):
                The request object. Request message for
                [RenameTagTemplateFieldEnumValue][google.cloud.datacatalog.v1.DataCatalog.RenameTagTemplateFieldEnumValue].
            name (:class:`str`):
                Required. The name of the enum field value. Example:

                - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}/enumValues/{enum_value_display_name}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            new_enum_value_display_name (:class:`str`):
                Required. The new display name of the enum value. For
                example, ``my_new_enum_value``.

                This corresponds to the ``new_enum_value_display_name`` field
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
            google.cloud.datacatalog_v1beta1.types.TagTemplateField:
                The template for an individual field
                within a tag template.

        """
        warnings.warn(
            "DataCatalogAsyncClient.rename_tag_template_field_enum_value is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, new_enum_value_display_name]
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
        if not isinstance(request, datacatalog.RenameTagTemplateFieldEnumValueRequest):
            request = datacatalog.RenameTagTemplateFieldEnumValueRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if new_enum_value_display_name is not None:
            request.new_enum_value_display_name = new_enum_value_display_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.rename_tag_template_field_enum_value
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

    async def delete_tag_template_field(
        self,
        request: Optional[
            Union[datacatalog.DeleteTagTemplateFieldRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        force: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a field in a tag template and all uses of that field.
        Users should enable the Data Catalog API in the project
        identified by the ``name`` parameter (see [Data Catalog Resource
        Project]
        (https://cloud.google.com/data-catalog/docs/concepts/resource-project)
        for more information).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_delete_tag_template_field():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteTagTemplateFieldRequest(
                    name="name_value",
                    force=True,
                )

                # Make the request
                await client.delete_tag_template_field(request=request)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.DeleteTagTemplateFieldRequest, dict]]):
                The request object. Request message for
                [DeleteTagTemplateField][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTagTemplateField].
            name (:class:`str`):
                Required. The name of the tag template field to delete.
                Example:

                - projects/{project_id}/locations/{location}/tagTemplates/{tag_template_id}/fields/{tag_template_field_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            force (:class:`bool`):
                Required. Currently, this field must always be set to
                ``true``. This confirms the deletion of this field from
                any tags using this field. ``force = false`` will be
                supported in the future.

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
        """
        warnings.warn(
            "DataCatalogAsyncClient.delete_tag_template_field is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, force]
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
        if not isinstance(request, datacatalog.DeleteTagTemplateFieldRequest):
            request = datacatalog.DeleteTagTemplateFieldRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if force is not None:
            request.force = force

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_tag_template_field
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

    async def create_tag(
        self,
        request: Optional[Union[datacatalog.CreateTagRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        tag: Optional[tags.Tag] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.Tag:
        r"""Creates a tag on an
        [Entry][google.cloud.datacatalog.v1beta1.Entry]. Note: The
        project identified by the ``parent`` parameter for the
        `tag <https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups.entries.tags/create#path-parameters>`__
        and the `tag
        template <https://cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.tagTemplates/create#path-parameters>`__
        used to create the tag must be from the same organization.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_create_tag():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                tag = datacatalog_v1beta1.Tag()
                tag.column = "column_value"
                tag.template = "template_value"

                request = datacatalog_v1beta1.CreateTagRequest(
                    parent="parent_value",
                    tag=tag,
                )

                # Make the request
                response = await client.create_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.CreateTagRequest, dict]]):
                The request object. Request message for
                [CreateTag][google.cloud.datacatalog.v1beta1.DataCatalog.CreateTag].
            parent (:class:`str`):
                Required. The name of the resource to attach this tag
                to. Tags can be attached to Entries. Example:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

                Note that this Tag and its child resources may not
                actually be stored in the location in this name.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            tag (:class:`google.cloud.datacatalog_v1beta1.types.Tag`):
                Required. The tag to create.
                This corresponds to the ``tag`` field
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
            google.cloud.datacatalog_v1beta1.types.Tag:
                Tags are used to attach custom metadata to Data Catalog resources. Tags
                   conform to the specifications within their tag
                   template.

                   See [Data Catalog
                   IAM](https://cloud.google.com/data-catalog/docs/concepts/iam)
                   for information on the permissions needed to create
                   or view tags.

        """
        warnings.warn(
            "DataCatalogAsyncClient.create_tag is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, tag]
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
        if not isinstance(request, datacatalog.CreateTagRequest):
            request = datacatalog.CreateTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if tag is not None:
            request.tag = tag

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_tag
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

    async def update_tag(
        self,
        request: Optional[Union[datacatalog.UpdateTagRequest, dict]] = None,
        *,
        tag: Optional[tags.Tag] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> tags.Tag:
        r"""Updates an existing tag.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_update_tag():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                tag = datacatalog_v1beta1.Tag()
                tag.column = "column_value"
                tag.template = "template_value"

                request = datacatalog_v1beta1.UpdateTagRequest(
                    tag=tag,
                )

                # Make the request
                response = await client.update_tag(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.UpdateTagRequest, dict]]):
                The request object. Request message for
                [UpdateTag][google.cloud.datacatalog.v1beta1.DataCatalog.UpdateTag].
            tag (:class:`google.cloud.datacatalog_v1beta1.types.Tag`):
                Required. The updated tag. The "name"
                field must be set.

                This corresponds to the ``tag`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Note: Currently, this parameter can only take
                ``"fields"`` as value.

                Names of fields whose values to overwrite on a tag.
                Currently, a tag has the only modifiable field with the
                name ``fields``.

                In general, if this parameter is absent or empty, all
                modifiable fields are overwritten. If such fields are
                non-required and omitted in the request body, their
                values are emptied.

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
            google.cloud.datacatalog_v1beta1.types.Tag:
                Tags are used to attach custom metadata to Data Catalog resources. Tags
                   conform to the specifications within their tag
                   template.

                   See [Data Catalog
                   IAM](https://cloud.google.com/data-catalog/docs/concepts/iam)
                   for information on the permissions needed to create
                   or view tags.

        """
        warnings.warn(
            "DataCatalogAsyncClient.update_tag is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [tag, update_mask]
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
        if not isinstance(request, datacatalog.UpdateTagRequest):
            request = datacatalog.UpdateTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if tag is not None:
            request.tag = tag
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_tag
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("tag.name", request.tag.name),)),
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

    async def delete_tag(
        self,
        request: Optional[Union[datacatalog.DeleteTagRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a tag.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_delete_tag():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.DeleteTagRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_tag(request=request)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.DeleteTagRequest, dict]]):
                The request object. Request message for
                [DeleteTag][google.cloud.datacatalog.v1beta1.DataCatalog.DeleteTag].
            name (:class:`str`):
                Required. The name of the tag to delete. Example:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}/tags/{tag_id}

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
        warnings.warn(
            "DataCatalogAsyncClient.delete_tag is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.DeleteTagRequest):
            request = datacatalog.DeleteTagRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_tag
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

    async def list_tags(
        self,
        request: Optional[Union[datacatalog.ListTagsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListTagsAsyncPager:
        r"""Lists tags assigned to an
        [Entry][google.cloud.datacatalog.v1beta1.Entry]. The
        [columns][google.cloud.datacatalog.v1beta1.Tag.column] in the
        response are lowercased.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1

            async def sample_list_tags():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = datacatalog_v1beta1.ListTagsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_tags(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datacatalog_v1beta1.types.ListTagsRequest, dict]]):
                The request object. Request message for
                [ListTags][google.cloud.datacatalog.v1beta1.DataCatalog.ListTags].
            parent (:class:`str`):
                Required. The name of the Data Catalog resource to list
                the tags of. The resource could be an
                [Entry][google.cloud.datacatalog.v1beta1.Entry] or an
                [EntryGroup][google.cloud.datacatalog.v1beta1.EntryGroup].

                Examples:

                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}
                - projects/{project_id}/locations/{location}/entryGroups/{entry_group_id}/entries/{entry_id}

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
            google.cloud.datacatalog_v1beta1.services.data_catalog.pagers.ListTagsAsyncPager:
                Response message for
                   [ListTags][google.cloud.datacatalog.v1beta1.DataCatalog.ListTags].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "DataCatalogAsyncClient.list_tags is deprecated", DeprecationWarning
        )

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
        if not isinstance(request, datacatalog.ListTagsRequest):
            request = datacatalog.ListTagsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_tags
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
        response = pagers.ListTagsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def set_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.SetIamPolicyRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Sets the access control policy for a resource. Replaces any
        existing policy. Supported resources are:

        - Tag templates.
        - Entries.
        - Entry groups. Note, this method cannot be used to manage
          policies for BigQuery, Pub/Sub and any external Google Cloud
          Platform resources synced to Data Catalog.

        Callers must have following Google IAM permission

        - ``datacatalog.tagTemplates.setIamPolicy`` to set policies on
          tag templates.
        - ``datacatalog.entries.setIamPolicy`` to set policies on
          entries.
        - ``datacatalog.entryGroups.setIamPolicy`` to set policies on
          entry groups.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            async def sample_set_iam_policy():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.SetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.set_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]]):
                The request object. Request message for ``SetIamPolicy`` method.
            resource (:class:`str`):
                REQUIRED: The resource for which the
                policy is being specified. See the
                operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
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
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time <             timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

                   **YAML example:**

                   :literal:``     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\ \`

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](https://cloud.google.com/iam/docs/).

        """
        warnings.warn(
            "DataCatalogAsyncClient.set_iam_policy is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - The request isn't a proto-plus wrapped type,
        #   so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.SetIamPolicyRequest(**request)
        elif not request:
            request = iam_policy_pb2.SetIamPolicyRequest(resource=resource)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.set_iam_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
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

    async def get_iam_policy(
        self,
        request: Optional[Union[iam_policy_pb2.GetIamPolicyRequest, dict]] = None,
        *,
        resource: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> policy_pb2.Policy:
        r"""Gets the access control policy for a resource. A ``NOT_FOUND``
        error is returned if the resource does not exist. An empty
        policy is returned if the resource exists but does not have a
        policy set on it.

        Supported resources are:

        - Tag templates.
        - Entries.
        - Entry groups. Note, this method cannot be used to manage
          policies for BigQuery, Pub/Sub and any external Google Cloud
          Platform resources synced to Data Catalog.

        Callers must have following Google IAM permission

        - ``datacatalog.tagTemplates.getIamPolicy`` to get policies on
          tag templates.
        - ``datacatalog.entries.getIamPolicy`` to get policies on
          entries.
        - ``datacatalog.entryGroups.getIamPolicy`` to get policies on
          entry groups.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            async def sample_get_iam_policy():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.GetIamPolicyRequest(
                    resource="resource_value",
                )

                # Make the request
                response = await client.get_iam_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]]):
                The request object. Request message for ``GetIamPolicy`` method.
            resource (:class:`str`):
                REQUIRED: The resource for which the
                policy is being requested. See the
                operation documentation for the
                appropriate value for this field.

                This corresponds to the ``resource`` field
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
            google.iam.v1.policy_pb2.Policy:
                An Identity and Access Management (IAM) policy, which specifies access
                   controls for Google Cloud resources.

                   A Policy is a collection of bindings. A binding binds
                   one or more members, or principals, to a single role.
                   Principals can be user accounts, service accounts,
                   Google groups, and domains (such as G Suite). A role
                   is a named list of permissions; each role can be an
                   IAM predefined role or a user-created custom role.

                   For some types of Google Cloud resources, a binding
                   can also specify a condition, which is a logical
                   expression that allows access to a resource only if
                   the expression evaluates to true. A condition can add
                   constraints based on attributes of the request, the
                   resource, or both. To learn which resources support
                   conditions in their IAM policies, see the [IAM
                   documentation](https://cloud.google.com/iam/help/conditions/resource-policies).

                   **JSON example:**

                   :literal:``     {       "bindings": [         {           "role": "roles/resourcemanager.organizationAdmin",           "members": [             "user:mike@example.com",             "group:admins@example.com",             "domain:google.com",             "serviceAccount:my-project-id@appspot.gserviceaccount.com"           ]         },         {           "role": "roles/resourcemanager.organizationViewer",           "members": [             "user:eve@example.com"           ],           "condition": {             "title": "expirable access",             "description": "Does not grant access after Sep 2020",             "expression": "request.time <             timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],       "etag": "BwWWja0YfJA=",       "version": 3     }`\ \`

                   **YAML example:**

                   :literal:``     bindings:     - members:       - user:mike@example.com       - group:admins@example.com       - domain:google.com       - serviceAccount:my-project-id@appspot.gserviceaccount.com       role: roles/resourcemanager.organizationAdmin     - members:       - user:eve@example.com       role: roles/resourcemanager.organizationViewer       condition:         title: expirable access         description: Does not grant access after Sep 2020         expression: request.time < timestamp('2020-10-01T00:00:00.000Z')     etag: BwWWja0YfJA=     version: 3`\ \`

                   For a description of IAM and its features, see the
                   [IAM
                   documentation](https://cloud.google.com/iam/docs/).

        """
        warnings.warn(
            "DataCatalogAsyncClient.get_iam_policy is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [resource]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - The request isn't a proto-plus wrapped type,
        #   so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.GetIamPolicyRequest(**request)
        elif not request:
            request = iam_policy_pb2.GetIamPolicyRequest(resource=resource)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_iam_policy
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
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

    async def test_iam_permissions(
        self,
        request: Optional[Union[iam_policy_pb2.TestIamPermissionsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        r"""Returns the caller's permissions on a resource. If the resource
        does not exist, an empty set of permissions is returned (We
        don't return a ``NOT_FOUND`` error).

        Supported resources are:

        - Tag templates.
        - Entries.
        - Entry groups. Note, this method cannot be used to manage
          policies for BigQuery, Pub/Sub and any external Google Cloud
          Platform resources synced to Data Catalog.

        A caller is not required to have Google IAM permission to make
        this request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datacatalog_v1beta1
            import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore

            async def sample_test_iam_permissions():
                # Create a client
                client = datacatalog_v1beta1.DataCatalogAsyncClient()

                # Initialize request argument(s)
                request = iam_policy_pb2.TestIamPermissionsRequest(
                    resource="resource_value",
                    permissions=['permissions_value1', 'permissions_value2'],
                )

                # Make the request
                response = await client.test_iam_permissions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]]):
                The request object. Request message for ``TestIamPermissions`` method.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse:
                Response message for TestIamPermissions method.
        """
        warnings.warn(
            "DataCatalogAsyncClient.test_iam_permissions is deprecated",
            DeprecationWarning,
        )

        # Create or coerce a protobuf request object.
        # - The request isn't a proto-plus wrapped type,
        #   so it must be constructed via keyword expansion.
        if isinstance(request, dict):
            request = iam_policy_pb2.TestIamPermissionsRequest(**request)
        elif not request:
            request = iam_policy_pb2.TestIamPermissionsRequest()

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.test_iam_permissions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("resource", request.resource),)),
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

    async def __aenter__(self) -> "DataCatalogAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DataCatalogAsyncClient",)
