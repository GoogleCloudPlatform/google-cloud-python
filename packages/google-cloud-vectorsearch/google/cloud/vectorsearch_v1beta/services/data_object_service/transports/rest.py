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
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.vectorsearch_v1beta._compat import transcode_request
from google.cloud.vectorsearch_v1beta.types import data_object, data_object_service
from google.cloud.vectorsearch_v1beta.types import data_object as gcv_data_object

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataObjectServiceRestTransport

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


class DataObjectServiceRestInterceptor:
    """Interceptor for DataObjectService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataObjectServiceRestTransport.

    .. code-block:: python
        class MyCustomDataObjectServiceInterceptor(DataObjectServiceRestInterceptor):
            def pre_batch_create_data_objects(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_data_objects(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_delete_data_objects(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_batch_update_data_objects(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_data_objects(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_object(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_object(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_data_object(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_data_object(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_object(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_object(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_object(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataObjectServiceRestTransport(interceptor=MyCustomDataObjectServiceInterceptor())
        client = DataObjectServiceClient(transport=transport)


    """

    def pre_batch_create_data_objects(
        self,
        request: data_object_service.BatchCreateDataObjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.BatchCreateDataObjectsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_data_objects

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_batch_create_data_objects(
        self, response: data_object_service.BatchCreateDataObjectsResponse
    ) -> data_object_service.BatchCreateDataObjectsResponse:
        """Post-rpc interceptor for batch_create_data_objects

        DEPRECATED. Please use the `post_batch_create_data_objects_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code. This `post_batch_create_data_objects` interceptor runs
        before the `post_batch_create_data_objects_with_metadata` interceptor.
        """
        return response

    def post_batch_create_data_objects_with_metadata(
        self,
        response: data_object_service.BatchCreateDataObjectsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.BatchCreateDataObjectsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_data_objects

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataObjectService server but before it is returned to user code.

        We recommend only using this `post_batch_create_data_objects_with_metadata`
        interceptor in new development instead of the `post_batch_create_data_objects` interceptor.
        When both interceptors are used, this `post_batch_create_data_objects_with_metadata` interceptor runs after the
        `post_batch_create_data_objects` interceptor. The (possibly modified) response returned by
        `post_batch_create_data_objects` will be passed to
        `post_batch_create_data_objects_with_metadata`.
        """
        return response, metadata

    def pre_batch_delete_data_objects(
        self,
        request: data_object_service.BatchDeleteDataObjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.BatchDeleteDataObjectsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_delete_data_objects

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def pre_batch_update_data_objects(
        self,
        request: data_object_service.BatchUpdateDataObjectsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.BatchUpdateDataObjectsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_data_objects

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_batch_update_data_objects(
        self, response: data_object_service.BatchUpdateDataObjectsResponse
    ) -> data_object_service.BatchUpdateDataObjectsResponse:
        """Post-rpc interceptor for batch_update_data_objects

        DEPRECATED. Please use the `post_batch_update_data_objects_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code. This `post_batch_update_data_objects` interceptor runs
        before the `post_batch_update_data_objects_with_metadata` interceptor.
        """
        return response

    def post_batch_update_data_objects_with_metadata(
        self,
        response: data_object_service.BatchUpdateDataObjectsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.BatchUpdateDataObjectsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_data_objects

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataObjectService server but before it is returned to user code.

        We recommend only using this `post_batch_update_data_objects_with_metadata`
        interceptor in new development instead of the `post_batch_update_data_objects` interceptor.
        When both interceptors are used, this `post_batch_update_data_objects_with_metadata` interceptor runs after the
        `post_batch_update_data_objects` interceptor. The (possibly modified) response returned by
        `post_batch_update_data_objects` will be passed to
        `post_batch_update_data_objects_with_metadata`.
        """
        return response, metadata

    def pre_create_data_object(
        self,
        request: data_object_service.CreateDataObjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.CreateDataObjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_data_object

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_create_data_object(
        self, response: gcv_data_object.DataObject
    ) -> gcv_data_object.DataObject:
        """Post-rpc interceptor for create_data_object

        DEPRECATED. Please use the `post_create_data_object_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code. This `post_create_data_object` interceptor runs
        before the `post_create_data_object_with_metadata` interceptor.
        """
        return response

    def post_create_data_object_with_metadata(
        self,
        response: gcv_data_object.DataObject,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcv_data_object.DataObject, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_object

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataObjectService server but before it is returned to user code.

        We recommend only using this `post_create_data_object_with_metadata`
        interceptor in new development instead of the `post_create_data_object` interceptor.
        When both interceptors are used, this `post_create_data_object_with_metadata` interceptor runs after the
        `post_create_data_object` interceptor. The (possibly modified) response returned by
        `post_create_data_object` will be passed to
        `post_create_data_object_with_metadata`.
        """
        return response, metadata

    def pre_delete_data_object(
        self,
        request: data_object_service.DeleteDataObjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.DeleteDataObjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_data_object

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def pre_get_data_object(
        self,
        request: data_object_service.GetDataObjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.GetDataObjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_object

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_get_data_object(
        self, response: data_object.DataObject
    ) -> data_object.DataObject:
        """Post-rpc interceptor for get_data_object

        DEPRECATED. Please use the `post_get_data_object_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code. This `post_get_data_object` interceptor runs
        before the `post_get_data_object_with_metadata` interceptor.
        """
        return response

    def post_get_data_object_with_metadata(
        self,
        response: data_object.DataObject,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_object.DataObject, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_object

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataObjectService server but before it is returned to user code.

        We recommend only using this `post_get_data_object_with_metadata`
        interceptor in new development instead of the `post_get_data_object` interceptor.
        When both interceptors are used, this `post_get_data_object_with_metadata` interceptor runs after the
        `post_get_data_object` interceptor. The (possibly modified) response returned by
        `post_get_data_object` will be passed to
        `post_get_data_object_with_metadata`.
        """
        return response, metadata

    def pre_update_data_object(
        self,
        request: data_object_service.UpdateDataObjectRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_object_service.UpdateDataObjectRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_data_object

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_update_data_object(
        self, response: gcv_data_object.DataObject
    ) -> gcv_data_object.DataObject:
        """Post-rpc interceptor for update_data_object

        DEPRECATED. Please use the `post_update_data_object_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code. This `post_update_data_object` interceptor runs
        before the `post_update_data_object_with_metadata` interceptor.
        """
        return response

    def post_update_data_object_with_metadata(
        self,
        response: gcv_data_object.DataObject,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcv_data_object.DataObject, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_object

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataObjectService server but before it is returned to user code.

        We recommend only using this `post_update_data_object_with_metadata`
        interceptor in new development instead of the `post_update_data_object` interceptor.
        When both interceptors are used, this `post_update_data_object_with_metadata` interceptor runs after the
        `post_update_data_object` interceptor. The (possibly modified) response returned by
        `post_update_data_object` will be passed to
        `post_update_data_object_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code.
        """
        return response

    def pre_delete_operation(
        self,
        request: operations_pb2.DeleteOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.DeleteOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code.
        """
        return response

    def pre_get_operation(
        self,
        request: operations_pb2.GetOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.GetOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code.
        """
        return response

    def pre_list_operations(
        self,
        request: operations_pb2.ListOperationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.ListOperationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_operations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataObjectService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DataObjectService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DataObjectServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataObjectServiceRestInterceptor


class DataObjectServiceRestTransport(_BaseDataObjectServiceRestTransport):
    """REST backend synchronous transport for DataObjectService.

    Service for creating and managing data objects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "vectorsearch.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataObjectServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'vectorsearch.googleapis.com').
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
            interceptor (Optional[DataObjectServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataObjectServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreateDataObjects(
        _BaseDataObjectServiceRestTransport._BaseBatchCreateDataObjects,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.BatchCreateDataObjects")

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
            request: data_object_service.BatchCreateDataObjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_object_service.BatchCreateDataObjectsResponse:
            r"""Call the batch create data objects method over HTTP.

            Args:
                request (~.data_object_service.BatchCreateDataObjectsRequest):
                    The request object. Request message for
                [DataObjectService.BatchCreateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchCreateDataObjects].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_object_service.BatchCreateDataObjectsResponse:
                    Response message for
                [DataObjectService.BatchCreateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchCreateDataObjects].

            """

            http_options = _BaseDataObjectServiceRestTransport._BaseBatchCreateDataObjects._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_data_objects(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseBatchCreateDataObjects,
                    "_BaseBatchCreateDataObjects__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.BatchCreateDataObjects",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "BatchCreateDataObjects",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataObjectServiceRestTransport._BatchCreateDataObjects._get_response(
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
            resp = data_object_service.BatchCreateDataObjectsResponse()
            pb_resp = data_object_service.BatchCreateDataObjectsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_data_objects(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_data_objects_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_object_service.BatchCreateDataObjectsResponse.to_json(
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
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.batch_create_data_objects",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "BatchCreateDataObjects",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeleteDataObjects(
        _BaseDataObjectServiceRestTransport._BaseBatchDeleteDataObjects,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.BatchDeleteDataObjects")

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
            request: data_object_service.BatchDeleteDataObjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the batch delete data objects method over HTTP.

            Args:
                request (~.data_object_service.BatchDeleteDataObjectsRequest):
                    The request object. Request message for
                [DataObjectService.BatchDeleteDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchDeleteDataObjects].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseBatchDeleteDataObjects._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_data_objects(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseBatchDeleteDataObjects,
                    "_BaseBatchDeleteDataObjects__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.BatchDeleteDataObjects",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "BatchDeleteDataObjects",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataObjectServiceRestTransport._BatchDeleteDataObjects._get_response(
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

    class _BatchUpdateDataObjects(
        _BaseDataObjectServiceRestTransport._BaseBatchUpdateDataObjects,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.BatchUpdateDataObjects")

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
            request: data_object_service.BatchUpdateDataObjectsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_object_service.BatchUpdateDataObjectsResponse:
            r"""Call the batch update data objects method over HTTP.

            Args:
                request (~.data_object_service.BatchUpdateDataObjectsRequest):
                    The request object. Request message for
                [DataObjectService.BatchUpdateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchUpdateDataObjects].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_object_service.BatchUpdateDataObjectsResponse:
                    Response message for
                [DataObjectService.BatchUpdateDataObjects][google.cloud.vectorsearch.v1beta.DataObjectService.BatchUpdateDataObjects].

            """

            http_options = _BaseDataObjectServiceRestTransport._BaseBatchUpdateDataObjects._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_data_objects(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseBatchUpdateDataObjects,
                    "_BaseBatchUpdateDataObjects__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.BatchUpdateDataObjects",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "BatchUpdateDataObjects",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataObjectServiceRestTransport._BatchUpdateDataObjects._get_response(
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
            resp = data_object_service.BatchUpdateDataObjectsResponse()
            pb_resp = data_object_service.BatchUpdateDataObjectsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_data_objects(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_data_objects_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_object_service.BatchUpdateDataObjectsResponse.to_json(
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
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.batch_update_data_objects",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "BatchUpdateDataObjects",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataObject(
        _BaseDataObjectServiceRestTransport._BaseCreateDataObject,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.CreateDataObject")

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
            request: data_object_service.CreateDataObjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcv_data_object.DataObject:
            r"""Call the create data object method over HTTP.

            Args:
                request (~.data_object_service.CreateDataObjectRequest):
                    The request object. Request message for
                [DataObjectService.CreateDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.CreateDataObject].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcv_data_object.DataObject:
                    A dataObject resource in Vector
                Search.

            """

            http_options = _BaseDataObjectServiceRestTransport._BaseCreateDataObject._get_http_options()
            request, metadata = self._interceptor.pre_create_data_object(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseCreateDataObject,
                    "_BaseCreateDataObject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.CreateDataObject",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "CreateDataObject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._CreateDataObject._get_response(
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
            resp = gcv_data_object.DataObject()
            pb_resp = gcv_data_object.DataObject.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_object(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_object_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcv_data_object.DataObject.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.create_data_object",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "CreateDataObject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataObject(
        _BaseDataObjectServiceRestTransport._BaseDeleteDataObject,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.DeleteDataObject")

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
            request: data_object_service.DeleteDataObjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data object method over HTTP.

            Args:
                request (~.data_object_service.DeleteDataObjectRequest):
                    The request object. Request message for
                [DataObjectService.DeleteDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.DeleteDataObject].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseDeleteDataObject._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_object(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseDeleteDataObject,
                    "_BaseDeleteDataObject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.DeleteDataObject",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "DeleteDataObject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._DeleteDataObject._get_response(
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

    class _GetDataObject(
        _BaseDataObjectServiceRestTransport._BaseGetDataObject,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.GetDataObject")

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
            request: data_object_service.GetDataObjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_object.DataObject:
            r"""Call the get data object method over HTTP.

            Args:
                request (~.data_object_service.GetDataObjectRequest):
                    The request object. Request message for
                [DataObjectService.GetDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.GetDataObject].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_object.DataObject:
                    A dataObject resource in Vector
                Search.

            """

            http_options = _BaseDataObjectServiceRestTransport._BaseGetDataObject._get_http_options()
            request, metadata = self._interceptor.pre_get_data_object(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseGetDataObject,
                    "_BaseGetDataObject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.GetDataObject",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "GetDataObject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._GetDataObject._get_response(
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
            resp = data_object.DataObject()
            pb_resp = data_object.DataObject.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_object(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_object_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_object.DataObject.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.get_data_object",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "GetDataObject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataObject(
        _BaseDataObjectServiceRestTransport._BaseUpdateDataObject,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.UpdateDataObject")

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
            request: data_object_service.UpdateDataObjectRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcv_data_object.DataObject:
            r"""Call the update data object method over HTTP.

            Args:
                request (~.data_object_service.UpdateDataObjectRequest):
                    The request object. Request message for
                [DataObjectService.UpdateDataObject][google.cloud.vectorsearch.v1beta.DataObjectService.UpdateDataObject].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcv_data_object.DataObject:
                    A dataObject resource in Vector
                Search.

            """

            http_options = _BaseDataObjectServiceRestTransport._BaseUpdateDataObject._get_http_options()
            request, metadata = self._interceptor.pre_update_data_object(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseUpdateDataObject,
                    "_BaseUpdateDataObject__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.UpdateDataObject",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "UpdateDataObject",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._UpdateDataObject._get_response(
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
            resp = gcv_data_object.DataObject()
            pb_resp = gcv_data_object.DataObject.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_object(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_object_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcv_data_object.DataObject.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.update_data_object",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "UpdateDataObject",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_data_objects(
        self,
    ) -> Callable[
        [data_object_service.BatchCreateDataObjectsRequest],
        data_object_service.BatchCreateDataObjectsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreateDataObjects(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_delete_data_objects(
        self,
    ) -> Callable[[data_object_service.BatchDeleteDataObjectsRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeleteDataObjects(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def batch_update_data_objects(
        self,
    ) -> Callable[
        [data_object_service.BatchUpdateDataObjectsRequest],
        data_object_service.BatchUpdateDataObjectsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdateDataObjects(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_data_object(
        self,
    ) -> Callable[
        [data_object_service.CreateDataObjectRequest], gcv_data_object.DataObject
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataObject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_object(
        self,
    ) -> Callable[[data_object_service.DeleteDataObjectRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataObject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_object(
        self,
    ) -> Callable[[data_object_service.GetDataObjectRequest], data_object.DataObject]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataObject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_object(
        self,
    ) -> Callable[
        [data_object_service.UpdateDataObjectRequest], gcv_data_object.DataObject
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataObject(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(
        _BaseDataObjectServiceRestTransport._BaseGetLocation, DataObjectServiceRestStub
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BaseDataObjectServiceRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._GetLocation._get_response(
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

            content = response.content.decode("utf-8")
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BaseDataObjectServiceRestTransport._BaseListLocations,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseListLocations._get_http_options()
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._ListLocations._get_response(
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

            content = response.content.decode("utf-8")
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDataObjectServiceRestTransport._BaseCancelOperation,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.CancelOperation")

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
            request: operations_pb2.CancelOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the cancel operation method over HTTP.

            Args:
                request (operations_pb2.CancelOperationRequest):
                    The request object for CancelOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseCancelOperation,
                    "_BaseCancelOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _DeleteOperation(
        _BaseDataObjectServiceRestTransport._BaseDeleteOperation,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.DeleteOperation")

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
            request: operations_pb2.DeleteOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> None:
            r"""Call the delete operation method over HTTP.

            Args:
                request (operations_pb2.DeleteOperationRequest):
                    The request object for DeleteOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseDeleteOperation,
                    "_BaseDeleteOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._DeleteOperation._get_response(
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

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseDataObjectServiceRestTransport._BaseGetOperation, DataObjectServiceRestStub
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.GetOperation")

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
            request: operations_pb2.GetOperationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the get operation method over HTTP.

            Args:
                request (operations_pb2.GetOperationRequest):
                    The request object for GetOperation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.Operation: Response from GetOperation method.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseGetOperation,
                    "_BaseGetOperation__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._GetOperation._get_response(
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

            content = response.content.decode("utf-8")
            resp = operations_pb2.Operation()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_operation(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListOperations(
        _BaseDataObjectServiceRestTransport._BaseListOperations,
        DataObjectServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataObjectServiceRestTransport.ListOperations")

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
            request: operations_pb2.ListOperationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.ListOperationsResponse:
            r"""Call the list operations method over HTTP.

            Args:
                request (operations_pb2.ListOperationsRequest):
                    The request object for ListOperations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                operations_pb2.ListOperationsResponse: Response from ListOperations method.
            """

            http_options = _BaseDataObjectServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataObjectServiceRestTransport._BaseListOperations,
                    "_BaseListOperations__REQUIRED_FIELDS_DEFAULT_VALUES",
                    None,
                ),
                rest_numeric_enums=False,
            )

            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                request_url = "{host}{uri}".format(
                    host=self._host, uri=transcoded_request["uri"]
                )
                method = transcoded_request["method"]
                try:
                    request_payload = json_format.MessageToJson(request)
                except:
                    request_payload = None
                http_request = {
                    "payload": request_payload,
                    "requestMethod": method,
                    "requestUrl": request_url,
                    "headers": dict(metadata),
                }
                _LOGGER.debug(
                    f"Sending request for google.cloud.vectorsearch_v1beta.DataObjectServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataObjectServiceRestTransport._ListOperations._get_response(
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

            content = response.content.decode("utf-8")
            resp = operations_pb2.ListOperationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_operations(resp)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = json_format.MessageToJson(resp)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.vectorsearch_v1beta.DataObjectServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.vectorsearch.v1beta.DataObjectService",
                        "rpcName": "ListOperations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DataObjectServiceRestTransport",)
