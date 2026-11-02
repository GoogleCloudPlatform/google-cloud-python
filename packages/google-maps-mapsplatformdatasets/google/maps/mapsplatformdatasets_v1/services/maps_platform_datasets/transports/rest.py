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
import dataclasses
import json  # type: ignore
import logging
import warnings
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.maps.mapsplatformdatasets_v1._compat import transcode_request
from google.maps.mapsplatformdatasets_v1.types import dataset, maps_platform_datasets
from google.maps.mapsplatformdatasets_v1.types import dataset as gmm_dataset

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseMapsPlatformDatasetsRestTransport

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = logging.getLogger(__name__)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=BASE_DEFAULT_CLIENT_INFO.gapic_version,
    grpc_version=None,
    rest_version=f"requests@{requests_version}",
)

DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class MapsPlatformDatasetsRestInterceptor:
    """Interceptor for MapsPlatformDatasets.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the MapsPlatformDatasetsRestTransport.

    .. code-block:: python
        class MyCustomMapsPlatformDatasetsInterceptor(MapsPlatformDatasetsRestInterceptor):
            def pre_create_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_fetch_dataset_errors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_dataset_errors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dataset(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dataset(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_datasets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_datasets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_dataset_metadata(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_dataset_metadata(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = MapsPlatformDatasetsRestTransport(interceptor=MyCustomMapsPlatformDatasetsInterceptor())
        client = MapsPlatformDatasetsClient(transport=transport)


    """

    def pre_create_dataset(
        self,
        request: maps_platform_datasets.CreateDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.CreateDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapsPlatformDatasets server.
        """
        return request, metadata

    def post_create_dataset(self, response: gmm_dataset.Dataset) -> gmm_dataset.Dataset:
        """Post-rpc interceptor for create_dataset

        DEPRECATED. Please use the `post_create_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapsPlatformDatasets server but before
        it is returned to user code. This `post_create_dataset` interceptor runs
        before the `post_create_dataset_with_metadata` interceptor.
        """
        return response

    def post_create_dataset_with_metadata(
        self,
        response: gmm_dataset.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gmm_dataset.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapsPlatformDatasets server but before it is returned to user code.

        We recommend only using this `post_create_dataset_with_metadata`
        interceptor in new development instead of the `post_create_dataset` interceptor.
        When both interceptors are used, this `post_create_dataset_with_metadata` interceptor runs after the
        `post_create_dataset` interceptor. The (possibly modified) response returned by
        `post_create_dataset` will be passed to
        `post_create_dataset_with_metadata`.
        """
        return response, metadata

    def pre_delete_dataset(
        self,
        request: maps_platform_datasets.DeleteDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.DeleteDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapsPlatformDatasets server.
        """
        return request, metadata

    def pre_fetch_dataset_errors(
        self,
        request: maps_platform_datasets.FetchDatasetErrorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.FetchDatasetErrorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_dataset_errors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapsPlatformDatasets server.
        """
        return request, metadata

    def post_fetch_dataset_errors(
        self, response: maps_platform_datasets.FetchDatasetErrorsResponse
    ) -> maps_platform_datasets.FetchDatasetErrorsResponse:
        """Post-rpc interceptor for fetch_dataset_errors

        DEPRECATED. Please use the `post_fetch_dataset_errors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapsPlatformDatasets server but before
        it is returned to user code. This `post_fetch_dataset_errors` interceptor runs
        before the `post_fetch_dataset_errors_with_metadata` interceptor.
        """
        return response

    def post_fetch_dataset_errors_with_metadata(
        self,
        response: maps_platform_datasets.FetchDatasetErrorsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.FetchDatasetErrorsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_dataset_errors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapsPlatformDatasets server but before it is returned to user code.

        We recommend only using this `post_fetch_dataset_errors_with_metadata`
        interceptor in new development instead of the `post_fetch_dataset_errors` interceptor.
        When both interceptors are used, this `post_fetch_dataset_errors_with_metadata` interceptor runs after the
        `post_fetch_dataset_errors` interceptor. The (possibly modified) response returned by
        `post_fetch_dataset_errors` will be passed to
        `post_fetch_dataset_errors_with_metadata`.
        """
        return response, metadata

    def pre_get_dataset(
        self,
        request: maps_platform_datasets.GetDatasetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.GetDatasetRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_dataset

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapsPlatformDatasets server.
        """
        return request, metadata

    def post_get_dataset(self, response: dataset.Dataset) -> dataset.Dataset:
        """Post-rpc interceptor for get_dataset

        DEPRECATED. Please use the `post_get_dataset_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapsPlatformDatasets server but before
        it is returned to user code. This `post_get_dataset` interceptor runs
        before the `post_get_dataset_with_metadata` interceptor.
        """
        return response

    def post_get_dataset_with_metadata(
        self,
        response: dataset.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dataset.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dataset

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapsPlatformDatasets server but before it is returned to user code.

        We recommend only using this `post_get_dataset_with_metadata`
        interceptor in new development instead of the `post_get_dataset` interceptor.
        When both interceptors are used, this `post_get_dataset_with_metadata` interceptor runs after the
        `post_get_dataset` interceptor. The (possibly modified) response returned by
        `post_get_dataset` will be passed to
        `post_get_dataset_with_metadata`.
        """
        return response, metadata

    def pre_list_datasets(
        self,
        request: maps_platform_datasets.ListDatasetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.ListDatasetsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_datasets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapsPlatformDatasets server.
        """
        return request, metadata

    def post_list_datasets(
        self, response: maps_platform_datasets.ListDatasetsResponse
    ) -> maps_platform_datasets.ListDatasetsResponse:
        """Post-rpc interceptor for list_datasets

        DEPRECATED. Please use the `post_list_datasets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapsPlatformDatasets server but before
        it is returned to user code. This `post_list_datasets` interceptor runs
        before the `post_list_datasets_with_metadata` interceptor.
        """
        return response

    def post_list_datasets_with_metadata(
        self,
        response: maps_platform_datasets.ListDatasetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.ListDatasetsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_datasets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapsPlatformDatasets server but before it is returned to user code.

        We recommend only using this `post_list_datasets_with_metadata`
        interceptor in new development instead of the `post_list_datasets` interceptor.
        When both interceptors are used, this `post_list_datasets_with_metadata` interceptor runs after the
        `post_list_datasets` interceptor. The (possibly modified) response returned by
        `post_list_datasets` will be passed to
        `post_list_datasets_with_metadata`.
        """
        return response, metadata

    def pre_update_dataset_metadata(
        self,
        request: maps_platform_datasets.UpdateDatasetMetadataRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        maps_platform_datasets.UpdateDatasetMetadataRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_dataset_metadata

        Override in a subclass to manipulate the request or metadata
        before they are sent to the MapsPlatformDatasets server.
        """
        return request, metadata

    def post_update_dataset_metadata(
        self, response: gmm_dataset.Dataset
    ) -> gmm_dataset.Dataset:
        """Post-rpc interceptor for update_dataset_metadata

        DEPRECATED. Please use the `post_update_dataset_metadata_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the MapsPlatformDatasets server but before
        it is returned to user code. This `post_update_dataset_metadata` interceptor runs
        before the `post_update_dataset_metadata_with_metadata` interceptor.
        """
        return response

    def post_update_dataset_metadata_with_metadata(
        self,
        response: gmm_dataset.Dataset,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gmm_dataset.Dataset, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_dataset_metadata

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the MapsPlatformDatasets server but before it is returned to user code.

        We recommend only using this `post_update_dataset_metadata_with_metadata`
        interceptor in new development instead of the `post_update_dataset_metadata` interceptor.
        When both interceptors are used, this `post_update_dataset_metadata_with_metadata` interceptor runs after the
        `post_update_dataset_metadata` interceptor. The (possibly modified) response returned by
        `post_update_dataset_metadata` will be passed to
        `post_update_dataset_metadata_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class MapsPlatformDatasetsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: MapsPlatformDatasetsRestInterceptor


class MapsPlatformDatasetsRestTransport(_BaseMapsPlatformDatasetsRestTransport):
    """REST backend synchronous transport for MapsPlatformDatasets.

    Service definition for the Maps Platform Datasets API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "mapsplatformdatasets.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[MapsPlatformDatasetsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'mapsplatformdatasets.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.

            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided. This argument will be
                removed in the next major version of this library.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Callable[[], Tuple[bytes, bytes]]): Client
                certificate to configure mutual TLS HTTP channel. It is ignored
                if ``channel`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you are developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            url_scheme: the protocol scheme for the API endpoint.  Normally
                "https", but for testing or local servers,
                "http" can be specified.
            interceptor (Optional[MapsPlatformDatasetsRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
        """
        # Run the base constructor
        # TODO(yon-mg): resolve other ctor params i.e. scopes, quota, etc.
        # TODO: When custom host (api_endpoint) is set, `scopes` must *also* be set on the
        # credentials object
        super().__init__(
            host=host,
            credentials=credentials,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
            url_scheme=url_scheme,
            api_audience=api_audience,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or MapsPlatformDatasetsRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateDataset(
        _BaseMapsPlatformDatasetsRestTransport._BaseCreateDataset,
        MapsPlatformDatasetsRestStub,
    ):
        def __hash__(self):
            return hash("MapsPlatformDatasetsRestTransport.CreateDataset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: maps_platform_datasets.CreateDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gmm_dataset.Dataset:
            r"""Call the create dataset method over HTTP.

            Args:
                request (~.maps_platform_datasets.CreateDatasetRequest):
                    The request object. Request to create a maps dataset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gmm_dataset.Dataset:
                    A representation of a dataset
                resource.

            """

            http_options = _BaseMapsPlatformDatasetsRestTransport._BaseCreateDataset._get_http_options()
            request, metadata = self._interceptor.pre_create_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapsPlatformDatasetsRestTransport._BaseCreateDataset,
                    "_BaseCreateDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.CreateDataset",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "CreateDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapsPlatformDatasetsRestTransport._CreateDataset._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gmm_dataset.Dataset()
            pb_resp = gmm_dataset.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gmm_dataset.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.create_dataset",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "CreateDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataset(
        _BaseMapsPlatformDatasetsRestTransport._BaseDeleteDataset,
        MapsPlatformDatasetsRestStub,
    ):
        def __hash__(self):
            return hash("MapsPlatformDatasetsRestTransport.DeleteDataset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: maps_platform_datasets.DeleteDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete dataset method over HTTP.

            Args:
                request (~.maps_platform_datasets.DeleteDatasetRequest):
                    The request object. Request to delete a dataset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseMapsPlatformDatasetsRestTransport._BaseDeleteDataset._get_http_options()
            request, metadata = self._interceptor.pre_delete_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapsPlatformDatasetsRestTransport._BaseDeleteDataset,
                    "_BaseDeleteDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.DeleteDataset",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "DeleteDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapsPlatformDatasetsRestTransport._DeleteDataset._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _FetchDatasetErrors(
        _BaseMapsPlatformDatasetsRestTransport._BaseFetchDatasetErrors,
        MapsPlatformDatasetsRestStub,
    ):
        def __hash__(self):
            return hash("MapsPlatformDatasetsRestTransport.FetchDatasetErrors")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: maps_platform_datasets.FetchDatasetErrorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> maps_platform_datasets.FetchDatasetErrorsResponse:
            r"""Call the fetch dataset errors method over HTTP.

            Args:
                request (~.maps_platform_datasets.FetchDatasetErrorsRequest):
                    The request object. Request to list detailed errors
                belonging to a dataset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.maps_platform_datasets.FetchDatasetErrorsResponse:
                    Response object of
                FetchDatasetErrors.

            """

            http_options = _BaseMapsPlatformDatasetsRestTransport._BaseFetchDatasetErrors._get_http_options()
            request, metadata = self._interceptor.pre_fetch_dataset_errors(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapsPlatformDatasetsRestTransport._BaseFetchDatasetErrors,
                    "_BaseFetchDatasetErrors__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.FetchDatasetErrors",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "FetchDatasetErrors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MapsPlatformDatasetsRestTransport._FetchDatasetErrors._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = maps_platform_datasets.FetchDatasetErrorsResponse()
            pb_resp = maps_platform_datasets.FetchDatasetErrorsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_fetch_dataset_errors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_dataset_errors_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        maps_platform_datasets.FetchDatasetErrorsResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.fetch_dataset_errors",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "FetchDatasetErrors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataset(
        _BaseMapsPlatformDatasetsRestTransport._BaseGetDataset,
        MapsPlatformDatasetsRestStub,
    ):
        def __hash__(self):
            return hash("MapsPlatformDatasetsRestTransport.GetDataset")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: maps_platform_datasets.GetDatasetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dataset.Dataset:
            r"""Call the get dataset method over HTTP.

            Args:
                request (~.maps_platform_datasets.GetDatasetRequest):
                    The request object. Request to get the specified dataset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dataset.Dataset:
                    A representation of a dataset
                resource.

            """

            http_options = _BaseMapsPlatformDatasetsRestTransport._BaseGetDataset._get_http_options()
            request, metadata = self._interceptor.pre_get_dataset(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapsPlatformDatasetsRestTransport._BaseGetDataset,
                    "_BaseGetDataset__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.GetDataset",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "GetDataset",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapsPlatformDatasetsRestTransport._GetDataset._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = dataset.Dataset()
            pb_resp = dataset.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dataset(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dataset_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dataset.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.get_dataset",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "GetDataset",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDatasets(
        _BaseMapsPlatformDatasetsRestTransport._BaseListDatasets,
        MapsPlatformDatasetsRestStub,
    ):
        def __hash__(self):
            return hash("MapsPlatformDatasetsRestTransport.ListDatasets")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
            )
            return response

        def __call__(
            self,
            request: maps_platform_datasets.ListDatasetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> maps_platform_datasets.ListDatasetsResponse:
            r"""Call the list datasets method over HTTP.

            Args:
                request (~.maps_platform_datasets.ListDatasetsRequest):
                    The request object. Request to list datasets for the
                project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.maps_platform_datasets.ListDatasetsResponse:
                    Response object of ListDatasets.
            """

            http_options = _BaseMapsPlatformDatasetsRestTransport._BaseListDatasets._get_http_options()
            request, metadata = self._interceptor.pre_list_datasets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapsPlatformDatasetsRestTransport._BaseListDatasets,
                    "_BaseListDatasets__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.ListDatasets",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "ListDatasets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = MapsPlatformDatasetsRestTransport._ListDatasets._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = maps_platform_datasets.ListDatasetsResponse()
            pb_resp = maps_platform_datasets.ListDatasetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_datasets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_datasets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        maps_platform_datasets.ListDatasetsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.list_datasets",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "ListDatasets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDatasetMetadata(
        _BaseMapsPlatformDatasetsRestTransport._BaseUpdateDatasetMetadata,
        MapsPlatformDatasetsRestStub,
    ):
        def __hash__(self):
            return hash("MapsPlatformDatasetsRestTransport.UpdateDatasetMetadata")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
        ):
            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            response = getattr(session, method)(
                "{host}{uri}".format(host=host, uri=uri),
                timeout=timeout,
                headers=headers,
                params=rest_helpers.flatten_query_params(query_params, strict=True),
                data=body,
            )
            return response

        def __call__(
            self,
            request: maps_platform_datasets.UpdateDatasetMetadataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gmm_dataset.Dataset:
            r"""Call the update dataset metadata method over HTTP.

            Args:
                request (~.maps_platform_datasets.UpdateDatasetMetadataRequest):
                    The request object. Request to update the metadata fields
                of the dataset.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gmm_dataset.Dataset:
                    A representation of a dataset
                resource.

            """

            http_options = _BaseMapsPlatformDatasetsRestTransport._BaseUpdateDatasetMetadata._get_http_options()
            request, metadata = self._interceptor.pre_update_dataset_metadata(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseMapsPlatformDatasetsRestTransport._BaseUpdateDatasetMetadata,
                    "_BaseUpdateDatasetMetadata__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=True,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = type(request).to_json(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.UpdateDatasetMetadata",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "UpdateDatasetMetadata",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                MapsPlatformDatasetsRestTransport._UpdateDatasetMetadata._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = gmm_dataset.Dataset()
            pb_resp = gmm_dataset.Dataset.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_dataset_metadata(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_dataset_metadata_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gmm_dataset.Dataset.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.mapsplatformdatasets_v1.MapsPlatformDatasetsClient.update_dataset_metadata",
                    extra={
                        "serviceName": "google.maps.mapsplatformdatasets.v1.MapsPlatformDatasets",
                        "rpcName": "UpdateDatasetMetadata",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_dataset(
        self,
    ) -> Callable[[maps_platform_datasets.CreateDatasetRequest], gmm_dataset.Dataset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_dataset(
        self,
    ) -> Callable[[maps_platform_datasets.DeleteDatasetRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def fetch_dataset_errors(
        self,
    ) -> Callable[
        [maps_platform_datasets.FetchDatasetErrorsRequest],
        maps_platform_datasets.FetchDatasetErrorsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchDatasetErrors(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dataset(
        self,
    ) -> Callable[[maps_platform_datasets.GetDatasetRequest], dataset.Dataset]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataset(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [maps_platform_datasets.ListDatasetsRequest],
        maps_platform_datasets.ListDatasetsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDatasets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_dataset_metadata(
        self,
    ) -> Callable[
        [maps_platform_datasets.UpdateDatasetMetadataRequest], gmm_dataset.Dataset
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDatasetMetadata(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("MapsPlatformDatasetsRestTransport",)
