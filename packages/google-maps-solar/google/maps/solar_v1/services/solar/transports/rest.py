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

import google.api.httpbody_pb2 as httpbody_pb2  # type: ignore
import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.maps.solar_v1._compat import transcode_request
from google.maps.solar_v1.types import solar_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSolarRestTransport

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


class SolarRestInterceptor:
    """Interceptor for Solar.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SolarRestTransport.

    .. code-block:: python
        class MyCustomSolarInterceptor(SolarRestInterceptor):
            def pre_find_closest_building_insights(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_find_closest_building_insights(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_layers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_layers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_geo_tiff(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_geo_tiff(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SolarRestTransport(interceptor=MyCustomSolarInterceptor())
        client = SolarClient(transport=transport)


    """

    def pre_find_closest_building_insights(
        self,
        request: solar_service.FindClosestBuildingInsightsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        solar_service.FindClosestBuildingInsightsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for find_closest_building_insights

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Solar server.
        """
        return request, metadata

    def post_find_closest_building_insights(
        self, response: solar_service.BuildingInsights
    ) -> solar_service.BuildingInsights:
        """Post-rpc interceptor for find_closest_building_insights

        DEPRECATED. Please use the `post_find_closest_building_insights_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Solar server but before
        it is returned to user code. This `post_find_closest_building_insights` interceptor runs
        before the `post_find_closest_building_insights_with_metadata` interceptor.
        """
        return response

    def post_find_closest_building_insights_with_metadata(
        self,
        response: solar_service.BuildingInsights,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[solar_service.BuildingInsights, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for find_closest_building_insights

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Solar server but before it is returned to user code.

        We recommend only using this `post_find_closest_building_insights_with_metadata`
        interceptor in new development instead of the `post_find_closest_building_insights` interceptor.
        When both interceptors are used, this `post_find_closest_building_insights_with_metadata` interceptor runs after the
        `post_find_closest_building_insights` interceptor. The (possibly modified) response returned by
        `post_find_closest_building_insights` will be passed to
        `post_find_closest_building_insights_with_metadata`.
        """
        return response, metadata

    def pre_get_data_layers(
        self,
        request: solar_service.GetDataLayersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        solar_service.GetDataLayersRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_layers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Solar server.
        """
        return request, metadata

    def post_get_data_layers(
        self, response: solar_service.DataLayers
    ) -> solar_service.DataLayers:
        """Post-rpc interceptor for get_data_layers

        DEPRECATED. Please use the `post_get_data_layers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Solar server but before
        it is returned to user code. This `post_get_data_layers` interceptor runs
        before the `post_get_data_layers_with_metadata` interceptor.
        """
        return response

    def post_get_data_layers_with_metadata(
        self,
        response: solar_service.DataLayers,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[solar_service.DataLayers, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_layers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Solar server but before it is returned to user code.

        We recommend only using this `post_get_data_layers_with_metadata`
        interceptor in new development instead of the `post_get_data_layers` interceptor.
        When both interceptors are used, this `post_get_data_layers_with_metadata` interceptor runs after the
        `post_get_data_layers` interceptor. The (possibly modified) response returned by
        `post_get_data_layers` will be passed to
        `post_get_data_layers_with_metadata`.
        """
        return response, metadata

    def pre_get_geo_tiff(
        self,
        request: solar_service.GetGeoTiffRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        solar_service.GetGeoTiffRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_geo_tiff

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Solar server.
        """
        return request, metadata

    def post_get_geo_tiff(
        self, response: httpbody_pb2.HttpBody
    ) -> httpbody_pb2.HttpBody:
        """Post-rpc interceptor for get_geo_tiff

        DEPRECATED. Please use the `post_get_geo_tiff_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Solar server but before
        it is returned to user code. This `post_get_geo_tiff` interceptor runs
        before the `post_get_geo_tiff_with_metadata` interceptor.
        """
        return response

    def post_get_geo_tiff_with_metadata(
        self,
        response: httpbody_pb2.HttpBody,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[httpbody_pb2.HttpBody, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_geo_tiff

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Solar server but before it is returned to user code.

        We recommend only using this `post_get_geo_tiff_with_metadata`
        interceptor in new development instead of the `post_get_geo_tiff` interceptor.
        When both interceptors are used, this `post_get_geo_tiff_with_metadata` interceptor runs after the
        `post_get_geo_tiff` interceptor. The (possibly modified) response returned by
        `post_get_geo_tiff` will be passed to
        `post_get_geo_tiff_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class SolarRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SolarRestInterceptor


class SolarRestTransport(_BaseSolarRestTransport):
    """REST backend synchronous transport for Solar.

    Service definition for the Solar API.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "solar.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SolarRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'solar.googleapis.com').
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
            interceptor (Optional[SolarRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SolarRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _FindClosestBuildingInsights(
        _BaseSolarRestTransport._BaseFindClosestBuildingInsights, SolarRestStub
    ):
        def __hash__(self):
            return hash("SolarRestTransport.FindClosestBuildingInsights")

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
            request: solar_service.FindClosestBuildingInsightsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> solar_service.BuildingInsights:
            r"""Call the find closest building
            insights method over HTTP.

                Args:
                    request (~.solar_service.FindClosestBuildingInsightsRequest):
                        The request object. Request message for
                    ``Solar.FindClosestBuildingInsights``.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.solar_service.BuildingInsights:
                        Response message for
                    ``Solar.FindClosestBuildingInsights``. Information about
                    the location, dimensions, and solar potential of a
                    building.

            """

            http_options = _BaseSolarRestTransport._BaseFindClosestBuildingInsights._get_http_options()
            request, metadata = self._interceptor.pre_find_closest_building_insights(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSolarRestTransport._BaseFindClosestBuildingInsights,
                    "_BaseFindClosestBuildingInsights__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.solar_v1.SolarClient.FindClosestBuildingInsights",
                    extra={
                        "serviceName": "google.maps.solar.v1.Solar",
                        "rpcName": "FindClosestBuildingInsights",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SolarRestTransport._FindClosestBuildingInsights._get_response(
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
            resp = solar_service.BuildingInsights()
            pb_resp = solar_service.BuildingInsights.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_find_closest_building_insights(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_find_closest_building_insights_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = solar_service.BuildingInsights.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.solar_v1.SolarClient.find_closest_building_insights",
                    extra={
                        "serviceName": "google.maps.solar.v1.Solar",
                        "rpcName": "FindClosestBuildingInsights",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataLayers(_BaseSolarRestTransport._BaseGetDataLayers, SolarRestStub):
        def __hash__(self):
            return hash("SolarRestTransport.GetDataLayers")

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
            request: solar_service.GetDataLayersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> solar_service.DataLayers:
            r"""Call the get data layers method over HTTP.

            Args:
                request (~.solar_service.GetDataLayersRequest):
                    The request object. Request message for ``Solar.GetDataLayers``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.solar_service.DataLayers:
                    Information about the solar potential of a region. The
                actual data are contained in a number of GeoTIFF files
                covering the requested region, for which this message
                contains URLs: Each string in the ``DataLayers`` message
                contains a URL from which the corresponding GeoTIFF can
                be fetched. These URLs are valid for a few hours after
                they've been generated. Most of the GeoTIFF files are at
                a resolution of 0.1m/pixel, but the monthly flux file is
                at 0.5m/pixel, and the hourly shade files are at
                1m/pixel. If a ``pixel_size_meters`` value was specified
                in the ``GetDataLayersRequest``, then the minimum
                resolution in the GeoTIFF files will be that value.

            """

            http_options = (
                _BaseSolarRestTransport._BaseGetDataLayers._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_data_layers(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSolarRestTransport._BaseGetDataLayers,
                    "_BaseGetDataLayers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.solar_v1.SolarClient.GetDataLayers",
                    extra={
                        "serviceName": "google.maps.solar.v1.Solar",
                        "rpcName": "GetDataLayers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SolarRestTransport._GetDataLayers._get_response(
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
            resp = solar_service.DataLayers()
            pb_resp = solar_service.DataLayers.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_layers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_layers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = solar_service.DataLayers.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.maps.solar_v1.SolarClient.get_data_layers",
                    extra={
                        "serviceName": "google.maps.solar.v1.Solar",
                        "rpcName": "GetDataLayers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetGeoTiff(_BaseSolarRestTransport._BaseGetGeoTiff, SolarRestStub):
        def __hash__(self):
            return hash("SolarRestTransport.GetGeoTiff")

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
            request: solar_service.GetGeoTiffRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> httpbody_pb2.HttpBody:
            r"""Call the get geo tiff method over HTTP.

            Args:
                request (~.solar_service.GetGeoTiffRequest):
                    The request object. Request message for ``Solar.GetGeoTiff``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.httpbody_pb2.HttpBody:
                    Message that represents an arbitrary HTTP body. It
                should only be used for payload formats that can't be
                represented as JSON, such as raw binary or an HTML page.

                This message can be used both in streaming and
                non-streaming API methods in the request as well as the
                response.

                It can be used as a top-level request field, which is
                convenient if one wants to extract parameters from
                either the URL or HTTP template into the request fields
                and also want access to the raw HTTP body.

                Example:

                ::

                    message GetResourceRequest {
                      // A unique request id.
                      string request_id = 1;

                      // The raw HTTP body is bound to this field.
                      google.api.HttpBody http_body = 2;

                    }

                    service ResourceService {
                      rpc GetResource(GetResourceRequest)
                        returns (google.api.HttpBody);
                      rpc UpdateResource(google.api.HttpBody)
                        returns (google.protobuf.Empty);

                    }

                Example with streaming methods:

                ::

                    service CaldavService {
                      rpc GetCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);
                      rpc UpdateCalendar(stream google.api.HttpBody)
                        returns (stream google.api.HttpBody);

                    }

                Use of this type only changes how the request and
                response bodies are handled, all other features will
                continue to work unchanged.

            """

            http_options = _BaseSolarRestTransport._BaseGetGeoTiff._get_http_options()
            request, metadata = self._interceptor.pre_get_geo_tiff(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSolarRestTransport._BaseGetGeoTiff,
                    "_BaseGetGeoTiff__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.maps.solar_v1.SolarClient.GetGeoTiff",
                    extra={
                        "serviceName": "google.maps.solar.v1.Solar",
                        "rpcName": "GetGeoTiff",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SolarRestTransport._GetGeoTiff._get_response(
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
            resp = httpbody_pb2.HttpBody()
            pb_resp = resp

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_geo_tiff(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_geo_tiff_with_metadata(
                resp, response_metadata
            )
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
                    "Received response for google.maps.solar_v1.SolarClient.get_geo_tiff",
                    extra={
                        "serviceName": "google.maps.solar.v1.Solar",
                        "rpcName": "GetGeoTiff",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def find_closest_building_insights(
        self,
    ) -> Callable[
        [solar_service.FindClosestBuildingInsightsRequest],
        solar_service.BuildingInsights,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FindClosestBuildingInsights(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_data_layers(
        self,
    ) -> Callable[[solar_service.GetDataLayersRequest], solar_service.DataLayers]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataLayers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_geo_tiff(
        self,
    ) -> Callable[[solar_service.GetGeoTiffRequest], httpbody_pb2.HttpBody]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetGeoTiff(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SolarRestTransport",)
