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

from google.cloud.datalabeling_v1beta1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore

from google.cloud.datalabeling_v1beta1.services.data_labeling_service import pagers
from google.cloud.datalabeling_v1beta1.types import (
    annotation,
    annotation_spec_set,
    data_labeling_service,
    data_payloads,
    dataset,
    evaluation,
    evaluation_job,
    human_annotation_config,
    instruction,
    operations,
)
from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set as gcd_annotation_spec_set,
)
from google.cloud.datalabeling_v1beta1.types import dataset as gcd_dataset
from google.cloud.datalabeling_v1beta1.types import evaluation_job as gcd_evaluation_job
from google.cloud.datalabeling_v1beta1.types import instruction as gcd_instruction

from .client import DataLabelingServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DataLabelingServiceTransport
from .transports.grpc_asyncio import DataLabelingServiceGrpcAsyncIOTransport

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class DataLabelingServiceAsyncClient:
    """Service for the AI Platform Data Labeling API."""

    _client: DataLabelingServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = DataLabelingServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DataLabelingServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = DataLabelingServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = DataLabelingServiceClient._DEFAULT_UNIVERSE

    annotated_dataset_path = staticmethod(
        DataLabelingServiceClient.annotated_dataset_path
    )
    parse_annotated_dataset_path = staticmethod(
        DataLabelingServiceClient.parse_annotated_dataset_path
    )
    annotation_spec_set_path = staticmethod(
        DataLabelingServiceClient.annotation_spec_set_path
    )
    parse_annotation_spec_set_path = staticmethod(
        DataLabelingServiceClient.parse_annotation_spec_set_path
    )
    data_item_path = staticmethod(DataLabelingServiceClient.data_item_path)
    parse_data_item_path = staticmethod(DataLabelingServiceClient.parse_data_item_path)
    dataset_path = staticmethod(DataLabelingServiceClient.dataset_path)
    parse_dataset_path = staticmethod(DataLabelingServiceClient.parse_dataset_path)
    evaluation_path = staticmethod(DataLabelingServiceClient.evaluation_path)
    parse_evaluation_path = staticmethod(
        DataLabelingServiceClient.parse_evaluation_path
    )
    evaluation_job_path = staticmethod(DataLabelingServiceClient.evaluation_job_path)
    parse_evaluation_job_path = staticmethod(
        DataLabelingServiceClient.parse_evaluation_job_path
    )
    example_path = staticmethod(DataLabelingServiceClient.example_path)
    parse_example_path = staticmethod(DataLabelingServiceClient.parse_example_path)
    instruction_path = staticmethod(DataLabelingServiceClient.instruction_path)
    parse_instruction_path = staticmethod(
        DataLabelingServiceClient.parse_instruction_path
    )
    common_billing_account_path = staticmethod(
        DataLabelingServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DataLabelingServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DataLabelingServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DataLabelingServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DataLabelingServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DataLabelingServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DataLabelingServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DataLabelingServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(DataLabelingServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        DataLabelingServiceClient.parse_common_location_path
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
            DataLabelingServiceAsyncClient: The constructed client.
        """
        sa_info_func = (
            DataLabelingServiceClient.from_service_account_info.__func__  # type: ignore
        )
        return sa_info_func(DataLabelingServiceAsyncClient, info, *args, **kwargs)

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
            DataLabelingServiceAsyncClient: The constructed client.
        """
        sa_file_func = (
            DataLabelingServiceClient.from_service_account_file.__func__  # type: ignore
        )
        return sa_file_func(DataLabelingServiceAsyncClient, filename, *args, **kwargs)

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
        return DataLabelingServiceClient.get_mtls_endpoint_and_cert_source(
            client_options
        )  # type: ignore

    @property
    def transport(self) -> DataLabelingServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DataLabelingServiceTransport: The transport used by the client instance.
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

    get_transport_class = DataLabelingServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                DataLabelingServiceTransport,
                Callable[..., DataLabelingServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the data labeling service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,DataLabelingServiceTransport,Callable[..., DataLabelingServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the DataLabelingServiceTransport constructor.
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
        self._client = DataLabelingServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.cloud.datalabeling_v1beta1.DataLabelingServiceAsyncClient`.",
                extra={
                    "serviceName": "google.cloud.datalabeling.v1beta1.DataLabelingService",
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
                    "serviceName": "google.cloud.datalabeling.v1beta1.DataLabelingService",
                    "credentialsType": None,
                },
            )

    async def create_dataset(
        self,
        request: Optional[
            Union[data_labeling_service.CreateDatasetRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        dataset: Optional[gcd_dataset.Dataset] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_dataset.Dataset:
        r"""Creates dataset. If success return a Dataset
        resource.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_create_dataset():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.CreateDatasetRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.CreateDatasetRequest, dict]]):
                The request object. Request message for CreateDataset.
            parent (:class:`str`):
                Required. Dataset resource parent, format:
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            dataset (:class:`google.cloud.datalabeling_v1beta1.types.Dataset`):
                Required. The dataset to be created.
                This corresponds to the ``dataset`` field
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
            google.cloud.datalabeling_v1beta1.types.Dataset:
                Dataset is the resource to hold your
                data. You can request multiple labeling
                tasks for a dataset while each one will
                generate an AnnotatedDataset.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, dataset]
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
        if not isinstance(request, data_labeling_service.CreateDatasetRequest):
            request = data_labeling_service.CreateDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if dataset is not None:
            request.dataset = dataset

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_dataset
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

    async def get_dataset(
        self,
        request: Optional[Union[data_labeling_service.GetDatasetRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> dataset.Dataset:
        r"""Gets dataset by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_dataset():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetDatasetRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetDatasetRequest, dict]]):
                The request object. Request message for GetDataSet.
            name (:class:`str`):
                Required. Dataset resource name, format:
                projects/{project_id}/datasets/{dataset_id}

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
            google.cloud.datalabeling_v1beta1.types.Dataset:
                Dataset is the resource to hold your
                data. You can request multiple labeling
                tasks for a dataset while each one will
                generate an AnnotatedDataset.

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
        if not isinstance(request, data_labeling_service.GetDatasetRequest):
            request = data_labeling_service.GetDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_dataset
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

    async def list_datasets(
        self,
        request: Optional[
            Union[data_labeling_service.ListDatasetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDatasetsAsyncPager:
        r"""Lists datasets under a project. Pagination is
        supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_datasets():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListDatasetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_datasets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListDatasetsRequest, dict]]):
                The request object. Request message for ListDataset.
            parent (:class:`str`):
                Required. Dataset resource parent, format:
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filter on dataset is not
                supported at this moment.

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListDatasetsAsyncPager:
                Results of listing datasets within a
                project.
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
        if not isinstance(request, data_labeling_service.ListDatasetsRequest):
            request = data_labeling_service.ListDatasetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_datasets
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
        response = pagers.ListDatasetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_dataset(
        self,
        request: Optional[
            Union[data_labeling_service.DeleteDatasetRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a dataset by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_delete_dataset():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.DeleteDatasetRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_dataset(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.DeleteDatasetRequest, dict]]):
                The request object. Request message for DeleteDataset.
            name (:class:`str`):
                Required. Dataset resource name, format:
                projects/{project_id}/datasets/{dataset_id}

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
        if not isinstance(request, data_labeling_service.DeleteDatasetRequest):
            request = data_labeling_service.DeleteDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_dataset
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

    async def import_data(
        self,
        request: Optional[Union[data_labeling_service.ImportDataRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        input_config: Optional[dataset.InputConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Imports data into dataset based on source locations
        defined in request. It can be called multiple times for
        the same dataset. Each dataset can only have one long
        running operation running on it. For example, no
        labeling task (also long running operation) can be
        started while importing is still ongoing. Vice versa.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_import_data():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ImportDataRequest(
                    name="name_value",
                )

                # Make the request
                operation = await client.import_data(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ImportDataRequest, dict]]):
                The request object. Request message for ImportData API.
            name (:class:`str`):
                Required. Dataset resource name, format:
                projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            input_config (:class:`google.cloud.datalabeling_v1beta1.types.InputConfig`):
                Required. Specify the input source of
                the data.

                This corresponds to the ``input_config`` field
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
                :class:`google.cloud.datalabeling_v1beta1.types.ImportDataOperationResponse`
                Response used for ImportData longrunning operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, input_config]
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
        if not isinstance(request, data_labeling_service.ImportDataRequest):
            request = data_labeling_service.ImportDataRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if input_config is not None:
            request.input_config = input_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.import_data
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
            operations.ImportDataOperationResponse,
            metadata_type=operations.ImportDataOperationMetadata,
        )

        # Done; return the response.
        return response

    async def export_data(
        self,
        request: Optional[Union[data_labeling_service.ExportDataRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        annotated_dataset: Optional[str] = None,
        filter: Optional[str] = None,
        output_config: Optional[dataset.OutputConfig] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Exports data and annotations from dataset.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_export_data():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ExportDataRequest(
                    name="name_value",
                    annotated_dataset="annotated_dataset_value",
                )

                # Make the request
                operation = await client.export_data(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ExportDataRequest, dict]]):
                The request object. Request message for ExportData API.
            name (:class:`str`):
                Required. Dataset resource name, format:
                projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            annotated_dataset (:class:`str`):
                Required. Annotated dataset resource name. DataItem in
                Dataset and their annotations in specified annotated
                dataset will be exported. It's in format of
                projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
                {annotated_dataset_id}

                This corresponds to the ``annotated_dataset`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filter is not supported at
                this moment.

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            output_config (:class:`google.cloud.datalabeling_v1beta1.types.OutputConfig`):
                Required. Specify the output
                destination.

                This corresponds to the ``output_config`` field
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
                :class:`google.cloud.datalabeling_v1beta1.types.ExportDataOperationResponse`
                Response used for ExportDataset longrunning operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, annotated_dataset, filter, output_config]
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
        if not isinstance(request, data_labeling_service.ExportDataRequest):
            request = data_labeling_service.ExportDataRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if annotated_dataset is not None:
            request.annotated_dataset = annotated_dataset
        if filter is not None:
            request.filter = filter
        if output_config is not None:
            request.output_config = output_config

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.export_data
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
            operations.ExportDataOperationResponse,
            metadata_type=operations.ExportDataOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_data_item(
        self,
        request: Optional[Union[data_labeling_service.GetDataItemRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> dataset.DataItem:
        r"""Gets a data item in a dataset by resource name. This
        API can be called after data are imported into dataset.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_data_item():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetDataItemRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_data_item(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetDataItemRequest, dict]]):
                The request object. Request message for GetDataItem.
            name (:class:`str`):
                Required. The name of the data item to get, format:
                projects/{project_id}/datasets/{dataset_id}/dataItems/{data_item_id}

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
            google.cloud.datalabeling_v1beta1.types.DataItem:
                DataItem is a piece of data, without
                annotation. For example, an image.

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
        if not isinstance(request, data_labeling_service.GetDataItemRequest):
            request = data_labeling_service.GetDataItemRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_data_item
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

    async def list_data_items(
        self,
        request: Optional[
            Union[data_labeling_service.ListDataItemsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListDataItemsAsyncPager:
        r"""Lists data items in a dataset. This API can be called
        after data are imported into dataset. Pagination is
        supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_data_items():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListDataItemsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_data_items(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListDataItemsRequest, dict]]):
                The request object. Request message for ListDataItems.
            parent (:class:`str`):
                Required. Name of the dataset to list data items,
                format: projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filter is not supported at
                this moment.

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListDataItemsAsyncPager:
                Results of listing data items in a
                dataset.
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
        if not isinstance(request, data_labeling_service.ListDataItemsRequest):
            request = data_labeling_service.ListDataItemsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_data_items
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
        response = pagers.ListDataItemsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_annotated_dataset(
        self,
        request: Optional[
            Union[data_labeling_service.GetAnnotatedDatasetRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> dataset.AnnotatedDataset:
        r"""Gets an annotated dataset by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_annotated_dataset():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetAnnotatedDatasetRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_annotated_dataset(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetAnnotatedDatasetRequest, dict]]):
                The request object. Request message for
                GetAnnotatedDataset.
            name (:class:`str`):
                Required. Name of the annotated dataset to get, format:
                projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
                {annotated_dataset_id}

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
            google.cloud.datalabeling_v1beta1.types.AnnotatedDataset:
                AnnotatedDataset is a set holding
                annotations for data in a Dataset. Each
                labeling task will generate an
                AnnotatedDataset under the Dataset that
                the task is requested for.

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
        if not isinstance(request, data_labeling_service.GetAnnotatedDatasetRequest):
            request = data_labeling_service.GetAnnotatedDatasetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_annotated_dataset
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

    async def list_annotated_datasets(
        self,
        request: Optional[
            Union[data_labeling_service.ListAnnotatedDatasetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAnnotatedDatasetsAsyncPager:
        r"""Lists annotated datasets for a dataset. Pagination is
        supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_annotated_datasets():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListAnnotatedDatasetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_annotated_datasets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListAnnotatedDatasetsRequest, dict]]):
                The request object. Request message for
                ListAnnotatedDatasets.
            parent (:class:`str`):
                Required. Name of the dataset to list annotated
                datasets, format:
                projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filter is not supported at
                this moment.

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListAnnotatedDatasetsAsyncPager:
                Results of listing annotated datasets
                for a dataset.
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
        if not isinstance(request, data_labeling_service.ListAnnotatedDatasetsRequest):
            request = data_labeling_service.ListAnnotatedDatasetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_annotated_datasets
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
        response = pagers.ListAnnotatedDatasetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_annotated_dataset(
        self,
        request: Optional[
            Union[data_labeling_service.DeleteAnnotatedDatasetRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an annotated dataset by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_delete_annotated_dataset():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.DeleteAnnotatedDatasetRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_annotated_dataset(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.DeleteAnnotatedDatasetRequest, dict]]):
                The request object. Request message for
                DeleteAnnotatedDataset.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, data_labeling_service.DeleteAnnotatedDatasetRequest):
            request = data_labeling_service.DeleteAnnotatedDatasetRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_annotated_dataset
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

    async def label_image(
        self,
        request: Optional[Union[data_labeling_service.LabelImageRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        basic_config: Optional[human_annotation_config.HumanAnnotationConfig] = None,
        feature: Optional[data_labeling_service.LabelImageRequest.Feature] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts a labeling task for image. The type of image
        labeling task is configured by feature in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_label_image():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                image_classification_config = datalabeling_v1beta1.ImageClassificationConfig()
                image_classification_config.annotation_spec_set = "annotation_spec_set_value"

                basic_config = datalabeling_v1beta1.HumanAnnotationConfig()
                basic_config.instruction = "instruction_value"
                basic_config.annotated_dataset_display_name = "annotated_dataset_display_name_value"

                request = datalabeling_v1beta1.LabelImageRequest(
                    image_classification_config=image_classification_config,
                    parent="parent_value",
                    basic_config=basic_config,
                    feature="SEGMENTATION",
                )

                # Make the request
                operation = await client.label_image(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.LabelImageRequest, dict]]):
                The request object. Request message for starting an image
                labeling task.
            parent (:class:`str`):
                Required. Name of the dataset to request labeling task,
                format: projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            basic_config (:class:`google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig`):
                Required. Basic human annotation
                config.

                This corresponds to the ``basic_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            feature (:class:`google.cloud.datalabeling_v1beta1.types.LabelImageRequest.Feature`):
                Required. The type of image labeling
                task.

                This corresponds to the ``feature`` field
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

                The result type for the operation will be :class:`google.cloud.datalabeling_v1beta1.types.AnnotatedDataset` AnnotatedDataset is a set holding annotations for data in a Dataset. Each
                   labeling task will generate an AnnotatedDataset under
                   the Dataset that the task is requested for.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, basic_config, feature]
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
        if not isinstance(request, data_labeling_service.LabelImageRequest):
            request = data_labeling_service.LabelImageRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if basic_config is not None:
            request.basic_config = basic_config
        if feature is not None:
            request.feature = feature

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.label_image
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
            dataset.AnnotatedDataset,
            metadata_type=operations.LabelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def label_video(
        self,
        request: Optional[Union[data_labeling_service.LabelVideoRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        basic_config: Optional[human_annotation_config.HumanAnnotationConfig] = None,
        feature: Optional[data_labeling_service.LabelVideoRequest.Feature] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts a labeling task for video. The type of video
        labeling task is configured by feature in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_label_video():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                video_classification_config = datalabeling_v1beta1.VideoClassificationConfig()
                video_classification_config.annotation_spec_set_configs.annotation_spec_set = "annotation_spec_set_value"

                basic_config = datalabeling_v1beta1.HumanAnnotationConfig()
                basic_config.instruction = "instruction_value"
                basic_config.annotated_dataset_display_name = "annotated_dataset_display_name_value"

                request = datalabeling_v1beta1.LabelVideoRequest(
                    video_classification_config=video_classification_config,
                    parent="parent_value",
                    basic_config=basic_config,
                    feature="EVENT",
                )

                # Make the request
                operation = await client.label_video(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.LabelVideoRequest, dict]]):
                The request object. Request message for LabelVideo.
            parent (:class:`str`):
                Required. Name of the dataset to request labeling task,
                format: projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            basic_config (:class:`google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig`):
                Required. Basic human annotation
                config.

                This corresponds to the ``basic_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            feature (:class:`google.cloud.datalabeling_v1beta1.types.LabelVideoRequest.Feature`):
                Required. The type of video labeling
                task.

                This corresponds to the ``feature`` field
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

                The result type for the operation will be :class:`google.cloud.datalabeling_v1beta1.types.AnnotatedDataset` AnnotatedDataset is a set holding annotations for data in a Dataset. Each
                   labeling task will generate an AnnotatedDataset under
                   the Dataset that the task is requested for.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, basic_config, feature]
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
        if not isinstance(request, data_labeling_service.LabelVideoRequest):
            request = data_labeling_service.LabelVideoRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if basic_config is not None:
            request.basic_config = basic_config
        if feature is not None:
            request.feature = feature

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.label_video
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
            dataset.AnnotatedDataset,
            metadata_type=operations.LabelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def label_text(
        self,
        request: Optional[Union[data_labeling_service.LabelTextRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        basic_config: Optional[human_annotation_config.HumanAnnotationConfig] = None,
        feature: Optional[data_labeling_service.LabelTextRequest.Feature] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Starts a labeling task for text. The type of text
        labeling task is configured by feature in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_label_text():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                text_classification_config = datalabeling_v1beta1.TextClassificationConfig()
                text_classification_config.annotation_spec_set = "annotation_spec_set_value"

                basic_config = datalabeling_v1beta1.HumanAnnotationConfig()
                basic_config.instruction = "instruction_value"
                basic_config.annotated_dataset_display_name = "annotated_dataset_display_name_value"

                request = datalabeling_v1beta1.LabelTextRequest(
                    text_classification_config=text_classification_config,
                    parent="parent_value",
                    basic_config=basic_config,
                    feature="TEXT_ENTITY_EXTRACTION",
                )

                # Make the request
                operation = await client.label_text(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.LabelTextRequest, dict]]):
                The request object. Request message for LabelText.
            parent (:class:`str`):
                Required. Name of the data set to request labeling task,
                format: projects/{project_id}/datasets/{dataset_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            basic_config (:class:`google.cloud.datalabeling_v1beta1.types.HumanAnnotationConfig`):
                Required. Basic human annotation
                config.

                This corresponds to the ``basic_config`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            feature (:class:`google.cloud.datalabeling_v1beta1.types.LabelTextRequest.Feature`):
                Required. The type of text labeling
                task.

                This corresponds to the ``feature`` field
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

                The result type for the operation will be :class:`google.cloud.datalabeling_v1beta1.types.AnnotatedDataset` AnnotatedDataset is a set holding annotations for data in a Dataset. Each
                   labeling task will generate an AnnotatedDataset under
                   the Dataset that the task is requested for.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, basic_config, feature]
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
        if not isinstance(request, data_labeling_service.LabelTextRequest):
            request = data_labeling_service.LabelTextRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if basic_config is not None:
            request.basic_config = basic_config
        if feature is not None:
            request.feature = feature

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.label_text
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
            dataset.AnnotatedDataset,
            metadata_type=operations.LabelOperationMetadata,
        )

        # Done; return the response.
        return response

    async def get_example(
        self,
        request: Optional[Union[data_labeling_service.GetExampleRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> dataset.Example:
        r"""Gets an example by resource name, including both data
        and annotation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_example():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetExampleRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_example(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetExampleRequest, dict]]):
                The request object. Request message for GetExample
            name (:class:`str`):
                Required. Name of example, format:
                projects/{project_id}/datasets/{dataset_id}/annotatedDatasets/
                {annotated_dataset_id}/examples/{example_id}

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. An expression for filtering Examples. Filter
                by annotation_spec.display_name is supported. Format
                "annotation_spec.display_name = {display_name}"

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
            google.cloud.datalabeling_v1beta1.types.Example:
                An Example is a piece of data and its
                annotation. For example, an image with
                label "house".

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name, filter]
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
        if not isinstance(request, data_labeling_service.GetExampleRequest):
            request = data_labeling_service.GetExampleRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_example
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

    async def list_examples(
        self,
        request: Optional[
            Union[data_labeling_service.ListExamplesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListExamplesAsyncPager:
        r"""Lists examples in an annotated dataset. Pagination is
        supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_examples():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListExamplesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_examples(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListExamplesRequest, dict]]):
                The request object. Request message for ListExamples.
            parent (:class:`str`):
                Required. Example resource parent.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. An expression for filtering Examples. For
                annotated datasets that have annotation spec set, filter
                by annotation_spec.display_name is supported. Format
                "annotation_spec.display_name = {display_name}"

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListExamplesAsyncPager:
                Results of listing Examples in and
                annotated dataset.
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
        if not isinstance(request, data_labeling_service.ListExamplesRequest):
            request = data_labeling_service.ListExamplesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_examples
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
        response = pagers.ListExamplesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_annotation_spec_set(
        self,
        request: Optional[
            Union[data_labeling_service.CreateAnnotationSpecSetRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        annotation_spec_set: Optional[gcd_annotation_spec_set.AnnotationSpecSet] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_annotation_spec_set.AnnotationSpecSet:
        r"""Creates an annotation spec set by providing a set of
        labels.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_create_annotation_spec_set():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.CreateAnnotationSpecSetRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_annotation_spec_set(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.CreateAnnotationSpecSetRequest, dict]]):
                The request object. Request message for
                CreateAnnotationSpecSet.
            parent (:class:`str`):
                Required. AnnotationSpecSet resource parent, format:
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            annotation_spec_set (:class:`google.cloud.datalabeling_v1beta1.types.AnnotationSpecSet`):
                Required. Annotation spec set to create. Annotation
                specs must be included. Only one annotation spec will be
                accepted for annotation specs with same display_name.

                This corresponds to the ``annotation_spec_set`` field
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
            google.cloud.datalabeling_v1beta1.types.AnnotationSpecSet:
                An AnnotationSpecSet is a collection
                of label definitions. For example, in
                image classification tasks, you define a
                set of possible labels for images as an
                AnnotationSpecSet. An AnnotationSpecSet
                is immutable upon creation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, annotation_spec_set]
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
            request, data_labeling_service.CreateAnnotationSpecSetRequest
        ):
            request = data_labeling_service.CreateAnnotationSpecSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if annotation_spec_set is not None:
            request.annotation_spec_set = annotation_spec_set

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_annotation_spec_set
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

    async def get_annotation_spec_set(
        self,
        request: Optional[
            Union[data_labeling_service.GetAnnotationSpecSetRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> annotation_spec_set.AnnotationSpecSet:
        r"""Gets an annotation spec set by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_annotation_spec_set():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetAnnotationSpecSetRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_annotation_spec_set(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetAnnotationSpecSetRequest, dict]]):
                The request object. Request message for
                GetAnnotationSpecSet.
            name (:class:`str`):
                Required. AnnotationSpecSet resource name, format:
                projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}

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
            google.cloud.datalabeling_v1beta1.types.AnnotationSpecSet:
                An AnnotationSpecSet is a collection
                of label definitions. For example, in
                image classification tasks, you define a
                set of possible labels for images as an
                AnnotationSpecSet. An AnnotationSpecSet
                is immutable upon creation.

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
        if not isinstance(request, data_labeling_service.GetAnnotationSpecSetRequest):
            request = data_labeling_service.GetAnnotationSpecSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_annotation_spec_set
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

    async def list_annotation_spec_sets(
        self,
        request: Optional[
            Union[data_labeling_service.ListAnnotationSpecSetsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAnnotationSpecSetsAsyncPager:
        r"""Lists annotation spec sets for a project. Pagination
        is supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_annotation_spec_sets():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListAnnotationSpecSetsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_annotation_spec_sets(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListAnnotationSpecSetsRequest, dict]]):
                The request object. Request message for
                ListAnnotationSpecSets.
            parent (:class:`str`):
                Required. Parent of AnnotationSpecSet resource, format:
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filter is not supported at
                this moment.

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListAnnotationSpecSetsAsyncPager:
                Results of listing annotation spec
                set under a project.
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
        if not isinstance(request, data_labeling_service.ListAnnotationSpecSetsRequest):
            request = data_labeling_service.ListAnnotationSpecSetsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_annotation_spec_sets
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
        response = pagers.ListAnnotationSpecSetsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_annotation_spec_set(
        self,
        request: Optional[
            Union[data_labeling_service.DeleteAnnotationSpecSetRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an annotation spec set by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_delete_annotation_spec_set():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.DeleteAnnotationSpecSetRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_annotation_spec_set(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.DeleteAnnotationSpecSetRequest, dict]]):
                The request object. Request message for
                DeleteAnnotationSpecSet.
            name (:class:`str`):
                Required. AnnotationSpec resource name, format:
                ``projects/{project_id}/annotationSpecSets/{annotation_spec_set_id}``.

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
            request, data_labeling_service.DeleteAnnotationSpecSetRequest
        ):
            request = data_labeling_service.DeleteAnnotationSpecSetRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_annotation_spec_set
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

    async def create_instruction(
        self,
        request: Optional[
            Union[data_labeling_service.CreateInstructionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        instruction: Optional[gcd_instruction.Instruction] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates an instruction for how data should be
        labeled.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_create_instruction():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.CreateInstructionRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = await client.create_instruction(request=request)

                print("Waiting for operation to complete...")

                response = await operation.result()

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.CreateInstructionRequest, dict]]):
                The request object. Request message for
                CreateInstruction.
            parent (:class:`str`):
                Required. Instruction resource parent, format:
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            instruction (:class:`google.cloud.datalabeling_v1beta1.types.Instruction`):
                Required. Instruction of how to
                perform the labeling task.

                This corresponds to the ``instruction`` field
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

                The result type for the operation will be :class:`google.cloud.datalabeling_v1beta1.types.Instruction` Instruction of how to perform the labeling task for human operators.
                   Currently only PDF instruction is supported.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, instruction]
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
        if not isinstance(request, data_labeling_service.CreateInstructionRequest):
            request = data_labeling_service.CreateInstructionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if instruction is not None:
            request.instruction = instruction

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_instruction
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
            gcd_instruction.Instruction,
            metadata_type=operations.CreateInstructionMetadata,
        )

        # Done; return the response.
        return response

    async def get_instruction(
        self,
        request: Optional[
            Union[data_labeling_service.GetInstructionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> instruction.Instruction:
        r"""Gets an instruction by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_instruction():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetInstructionRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_instruction(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetInstructionRequest, dict]]):
                The request object. Request message for GetInstruction.
            name (:class:`str`):
                Required. Instruction resource name, format:
                projects/{project_id}/instructions/{instruction_id}

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
            google.cloud.datalabeling_v1beta1.types.Instruction:
                Instruction of how to perform the
                labeling task for human operators.
                Currently only PDF instruction is
                supported.

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
        if not isinstance(request, data_labeling_service.GetInstructionRequest):
            request = data_labeling_service.GetInstructionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_instruction
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

    async def list_instructions(
        self,
        request: Optional[
            Union[data_labeling_service.ListInstructionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListInstructionsAsyncPager:
        r"""Lists instructions for a project. Pagination is
        supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_instructions():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListInstructionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_instructions(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListInstructionsRequest, dict]]):
                The request object. Request message for ListInstructions.
            parent (:class:`str`):
                Required. Instruction resource parent, format:
                projects/{project_id}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. Filter is not supported at
                this moment.

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListInstructionsAsyncPager:
                Results of listing instructions under
                a project.
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
        if not isinstance(request, data_labeling_service.ListInstructionsRequest):
            request = data_labeling_service.ListInstructionsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_instructions
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
        response = pagers.ListInstructionsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_instruction(
        self,
        request: Optional[
            Union[data_labeling_service.DeleteInstructionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an instruction object by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_delete_instruction():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.DeleteInstructionRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_instruction(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.DeleteInstructionRequest, dict]]):
                The request object. Request message for
                DeleteInstruction.
            name (:class:`str`):
                Required. Instruction resource name, format:
                projects/{project_id}/instructions/{instruction_id}

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
        if not isinstance(request, data_labeling_service.DeleteInstructionRequest):
            request = data_labeling_service.DeleteInstructionRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_instruction
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

    async def get_evaluation(
        self,
        request: Optional[
            Union[data_labeling_service.GetEvaluationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation.Evaluation:
        r"""Gets an evaluation by resource name (to search, use
        [projects.evaluations.search][google.cloud.datalabeling.v1beta1.DataLabelingService.SearchEvaluations]).

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_evaluation():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetEvaluationRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetEvaluationRequest, dict]]):
                The request object. Request message for GetEvaluation.
            name (:class:`str`):
                Required. Name of the evaluation. Format:

                "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}'

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
            google.cloud.datalabeling_v1beta1.types.Evaluation:
                Describes an evaluation between a machine learning model's predictions and
                   ground truth labels. Created when an
                   [EvaluationJob][google.cloud.datalabeling.v1beta1.EvaluationJob]
                   runs successfully.

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
        if not isinstance(request, data_labeling_service.GetEvaluationRequest):
            request = data_labeling_service.GetEvaluationRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation
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

    async def search_evaluations(
        self,
        request: Optional[
            Union[data_labeling_service.SearchEvaluationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchEvaluationsAsyncPager:
        r"""Searches
        [evaluations][google.cloud.datalabeling.v1beta1.Evaluation]
        within a project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_search_evaluations():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.SearchEvaluationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.search_evaluations(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.SearchEvaluationsRequest, dict]]):
                The request object. Request message for SearchEvaluation.
            parent (:class:`str`):
                Required. Evaluation search parent (project ID). Format:
                "projects/{project_id}"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. To search evaluations, you can filter by the
                following:

                - evaluation\_job.evaluation_job_id (the last part of
                  [EvaluationJob.name][google.cloud.datalabeling.v1beta1.EvaluationJob.name])
                - evaluation\_job.model_id (the {model_name} portion of
                  [EvaluationJob.modelVersion][google.cloud.datalabeling.v1beta1.EvaluationJob.model_version])
                - evaluation\_job.evaluation_job_run_time_start (Minimum
                  threshold for the
                  [evaluationJobRunTime][google.cloud.datalabeling.v1beta1.Evaluation.evaluation_job_run_time]
                  that created the evaluation)
                - evaluation\_job.evaluation_job_run_time_end (Maximum
                  threshold for the
                  [evaluationJobRunTime][google.cloud.datalabeling.v1beta1.Evaluation.evaluation_job_run_time]
                  that created the evaluation)
                - evaluation\_job.job_state
                  ([EvaluationJob.state][google.cloud.datalabeling.v1beta1.EvaluationJob.state])
                - annotation\_spec.display_name (the Evaluation contains
                  a metric for the annotation spec with this
                  [displayName][google.cloud.datalabeling.v1beta1.AnnotationSpec.display_name])

                To filter by multiple critiera, use the ``AND`` operator
                or the ``OR`` operator. The following examples shows a
                string that filters by several critiera:

                "evaluation\ *job.evaluation_job_id =
                {evaluation_job_id} AND evaluation*\ job.model_id =
                {model_name} AND
                evaluation\ *job.evaluation_job_run_time_start =
                {timestamp_1} AND
                evaluation*\ job.evaluation_job_run_time_end =
                {timestamp_2} AND annotation\_spec.display_name =
                {display_name}"

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.SearchEvaluationsAsyncPager:
                Results of searching evaluations.

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
        if not isinstance(request, data_labeling_service.SearchEvaluationsRequest):
            request = data_labeling_service.SearchEvaluationsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_evaluations
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
        response = pagers.SearchEvaluationsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def search_example_comparisons(
        self,
        request: Optional[
            Union[data_labeling_service.SearchExampleComparisonsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.SearchExampleComparisonsAsyncPager:
        r"""Searches example comparisons from an evaluation. The
        return format is a list of example comparisons that show
        ground truth and prediction(s) for a single input.
        Search by providing an evaluation ID.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_search_example_comparisons():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.SearchExampleComparisonsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.search_example_comparisons(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.SearchExampleComparisonsRequest, dict]]):
                The request object. Request message of
                SearchExampleComparisons.
            parent (:class:`str`):
                Required. Name of the
                [Evaluation][google.cloud.datalabeling.v1beta1.Evaluation]
                resource to search for example comparisons from. Format:

                "projects/{project_id}/datasets/{dataset_id}/evaluations/{evaluation_id}"

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.SearchExampleComparisonsAsyncPager:
                Results of searching example
                comparisons.
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
            request, data_labeling_service.SearchExampleComparisonsRequest
        ):
            request = data_labeling_service.SearchExampleComparisonsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.search_example_comparisons
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
        response = pagers.SearchExampleComparisonsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_evaluation_job(
        self,
        request: Optional[
            Union[data_labeling_service.CreateEvaluationJobRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        job: Optional[evaluation_job.EvaluationJob] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation_job.EvaluationJob:
        r"""Creates an evaluation job.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_create_evaluation_job():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.CreateEvaluationJobRequest(
                    parent="parent_value",
                )

                # Make the request
                response = await client.create_evaluation_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.CreateEvaluationJobRequest, dict]]):
                The request object. Request message for
                CreateEvaluationJob.
            parent (:class:`str`):
                Required. Evaluation job resource parent. Format:
                "projects/{project_id}"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            job (:class:`google.cloud.datalabeling_v1beta1.types.EvaluationJob`):
                Required. The evaluation job to
                create.

                This corresponds to the ``job`` field
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
            google.cloud.datalabeling_v1beta1.types.EvaluationJob:
                Defines an evaluation job that runs periodically to generate
                   [Evaluations][google.cloud.datalabeling.v1beta1.Evaluation].
                   [Creating an evaluation
                   job](/ml-engine/docs/continuous-evaluation/create-job)
                   is the starting point for using continuous
                   evaluation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, job]
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
        if not isinstance(request, data_labeling_service.CreateEvaluationJobRequest):
            request = data_labeling_service.CreateEvaluationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if job is not None:
            request.job = job

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.create_evaluation_job
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

    async def update_evaluation_job(
        self,
        request: Optional[
            Union[data_labeling_service.UpdateEvaluationJobRequest, dict]
        ] = None,
        *,
        evaluation_job: Optional[gcd_evaluation_job.EvaluationJob] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_evaluation_job.EvaluationJob:
        r"""Updates an evaluation job. You can only update certain fields of
        the job's
        [EvaluationJobConfig][google.cloud.datalabeling.v1beta1.EvaluationJobConfig]:
        ``humanAnnotationConfig.instruction``, ``exampleCount``, and
        ``exampleSamplePercentage``.

        If you want to change any other aspect of the evaluation job,
        you must delete the job and create a new one.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_update_evaluation_job():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.UpdateEvaluationJobRequest(
                )

                # Make the request
                response = await client.update_evaluation_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.UpdateEvaluationJobRequest, dict]]):
                The request object. Request message for
                UpdateEvaluationJob.
            evaluation_job (:class:`google.cloud.datalabeling_v1beta1.types.EvaluationJob`):
                Required. Evaluation job that is
                going to be updated.

                This corresponds to the ``evaluation_job`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. Mask for which fields to update. You can only
                provide the following fields:

                - ``evaluationJobConfig.humanAnnotationConfig.instruction``
                - ``evaluationJobConfig.exampleCount``
                - ``evaluationJobConfig.exampleSamplePercentage``

                You can provide more than one of these fields by
                separating them with commas.

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
            google.cloud.datalabeling_v1beta1.types.EvaluationJob:
                Defines an evaluation job that runs periodically to generate
                   [Evaluations][google.cloud.datalabeling.v1beta1.Evaluation].
                   [Creating an evaluation
                   job](/ml-engine/docs/continuous-evaluation/create-job)
                   is the starting point for using continuous
                   evaluation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [evaluation_job, update_mask]
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
        if not isinstance(request, data_labeling_service.UpdateEvaluationJobRequest):
            request = data_labeling_service.UpdateEvaluationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if evaluation_job is not None:
            request.evaluation_job = evaluation_job
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.update_evaluation_job
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("evaluation_job.name", request.evaluation_job.name),)
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

    async def get_evaluation_job(
        self,
        request: Optional[
            Union[data_labeling_service.GetEvaluationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> evaluation_job.EvaluationJob:
        r"""Gets an evaluation job by resource name.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_get_evaluation_job():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.GetEvaluationJobRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_evaluation_job(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.GetEvaluationJobRequest, dict]]):
                The request object. Request message for GetEvaluationJob.
            name (:class:`str`):
                Required. Name of the evaluation job. Format:

                "projects/{project_id}/evaluationJobs/{evaluation_job_id}"

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
            google.cloud.datalabeling_v1beta1.types.EvaluationJob:
                Defines an evaluation job that runs periodically to generate
                   [Evaluations][google.cloud.datalabeling.v1beta1.Evaluation].
                   [Creating an evaluation
                   job](/ml-engine/docs/continuous-evaluation/create-job)
                   is the starting point for using continuous
                   evaluation.

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
        if not isinstance(request, data_labeling_service.GetEvaluationJobRequest):
            request = data_labeling_service.GetEvaluationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.get_evaluation_job
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

    async def pause_evaluation_job(
        self,
        request: Optional[
            Union[data_labeling_service.PauseEvaluationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Pauses an evaluation job. Pausing an evaluation job that is
        already in a ``PAUSED`` state is a no-op.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_pause_evaluation_job():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.PauseEvaluationJobRequest(
                    name="name_value",
                )

                # Make the request
                await client.pause_evaluation_job(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.PauseEvaluationJobRequest, dict]]):
                The request object. Request message for
                PauseEvaluationJob.
            name (:class:`str`):
                Required. Name of the evaluation job that is going to be
                paused. Format:

                "projects/{project_id}/evaluationJobs/{evaluation_job_id}"

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
        if not isinstance(request, data_labeling_service.PauseEvaluationJobRequest):
            request = data_labeling_service.PauseEvaluationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.pause_evaluation_job
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

    async def resume_evaluation_job(
        self,
        request: Optional[
            Union[data_labeling_service.ResumeEvaluationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Resumes a paused evaluation job. A deleted evaluation
        job can't be resumed. Resuming a running or scheduled
        evaluation job is a no-op.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_resume_evaluation_job():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ResumeEvaluationJobRequest(
                    name="name_value",
                )

                # Make the request
                await client.resume_evaluation_job(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ResumeEvaluationJobRequest, dict]]):
                The request object. Request message ResumeEvaluationJob.
            name (:class:`str`):
                Required. Name of the evaluation job that is going to be
                resumed. Format:

                "projects/{project_id}/evaluationJobs/{evaluation_job_id}"

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
        if not isinstance(request, data_labeling_service.ResumeEvaluationJobRequest):
            request = data_labeling_service.ResumeEvaluationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.resume_evaluation_job
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

    async def delete_evaluation_job(
        self,
        request: Optional[
            Union[data_labeling_service.DeleteEvaluationJobRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Stops and deletes an evaluation job.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_delete_evaluation_job():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.DeleteEvaluationJobRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_evaluation_job(request=request)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.DeleteEvaluationJobRequest, dict]]):
                The request object. Request message DeleteEvaluationJob.
            name (:class:`str`):
                Required. Name of the evaluation job that is going to be
                deleted. Format:

                "projects/{project_id}/evaluationJobs/{evaluation_job_id}"

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
        if not isinstance(request, data_labeling_service.DeleteEvaluationJobRequest):
            request = data_labeling_service.DeleteEvaluationJobRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_evaluation_job
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

    async def list_evaluation_jobs(
        self,
        request: Optional[
            Union[data_labeling_service.ListEvaluationJobsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEvaluationJobsAsyncPager:
        r"""Lists all evaluation jobs within a project with
        possible filters. Pagination is supported.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import datalabeling_v1beta1

            async def sample_list_evaluation_jobs():
                # Create a client
                client = datalabeling_v1beta1.DataLabelingServiceAsyncClient()

                # Initialize request argument(s)
                request = datalabeling_v1beta1.ListEvaluationJobsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_evaluation_jobs(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.datalabeling_v1beta1.types.ListEvaluationJobsRequest, dict]]):
                The request object. Request message for
                ListEvaluationJobs.
            parent (:class:`str`):
                Required. Evaluation job resource parent. Format:
                "projects/{project_id}"

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (:class:`str`):
                Optional. You can filter the jobs to list by model_id
                (also known as model_name, as described in
                [EvaluationJob.modelVersion][google.cloud.datalabeling.v1beta1.EvaluationJob.model_version])
                or by evaluation job state (as described in
                [EvaluationJob.state][google.cloud.datalabeling.v1beta1.EvaluationJob.state]).
                To filter by both criteria, use the ``AND`` operator or
                the ``OR`` operator. For example, you can use the
                following string for your filter:
                "evaluation\ *job.model_id = {model_name} AND
                evaluation*\ job.state = {evaluation_job_state}"

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
            google.cloud.datalabeling_v1beta1.services.data_labeling_service.pagers.ListEvaluationJobsAsyncPager:
                Results for listing evaluation jobs.

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
        if not isinstance(request, data_labeling_service.ListEvaluationJobsRequest):
            request = data_labeling_service.ListEvaluationJobsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if filter is not None:
            request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_evaluation_jobs
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
        response = pagers.ListEvaluationJobsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "DataLabelingServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("DataLabelingServiceAsyncClient",)
