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

from google.cloud.video.transcoder_v1._compat import transcode_request
from google.cloud.video.transcoder_v1.types import resources, services

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseTranscoderServiceRestTransport

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


class TranscoderServiceRestInterceptor:
    """Interceptor for TranscoderService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the TranscoderServiceRestTransport.

    .. code-block:: python
        class MyCustomTranscoderServiceInterceptor(TranscoderServiceRestInterceptor):
            def pre_create_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_job_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_job_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_job_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_job_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_job_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_job_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_job_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = TranscoderServiceRestTransport(interceptor=MyCustomTranscoderServiceInterceptor())
        client = TranscoderServiceClient(transport=transport)


    """

    def pre_create_job(
        self,
        request: services.CreateJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[services.CreateJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def post_create_job(self, response: resources.Job) -> resources.Job:
        """Post-rpc interceptor for create_job

        DEPRECATED. Please use the `post_create_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TranscoderService server but before
        it is returned to user code. This `post_create_job` interceptor runs
        before the `post_create_job_with_metadata` interceptor.
        """
        return response

    def post_create_job_with_metadata(
        self, response: resources.Job, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[resources.Job, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TranscoderService server but before it is returned to user code.

        We recommend only using this `post_create_job_with_metadata`
        interceptor in new development instead of the `post_create_job` interceptor.
        When both interceptors are used, this `post_create_job_with_metadata` interceptor runs after the
        `post_create_job` interceptor. The (possibly modified) response returned by
        `post_create_job` will be passed to
        `post_create_job_with_metadata`.
        """
        return response, metadata

    def pre_create_job_template(
        self,
        request: services.CreateJobTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        services.CreateJobTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_job_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def post_create_job_template(
        self, response: resources.JobTemplate
    ) -> resources.JobTemplate:
        """Post-rpc interceptor for create_job_template

        DEPRECATED. Please use the `post_create_job_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TranscoderService server but before
        it is returned to user code. This `post_create_job_template` interceptor runs
        before the `post_create_job_template_with_metadata` interceptor.
        """
        return response

    def post_create_job_template_with_metadata(
        self,
        response: resources.JobTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.JobTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_job_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TranscoderService server but before it is returned to user code.

        We recommend only using this `post_create_job_template_with_metadata`
        interceptor in new development instead of the `post_create_job_template` interceptor.
        When both interceptors are used, this `post_create_job_template_with_metadata` interceptor runs after the
        `post_create_job_template` interceptor. The (possibly modified) response returned by
        `post_create_job_template` will be passed to
        `post_create_job_template_with_metadata`.
        """
        return response, metadata

    def pre_delete_job(
        self,
        request: services.DeleteJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[services.DeleteJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def pre_delete_job_template(
        self,
        request: services.DeleteJobTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        services.DeleteJobTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_job_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def pre_get_job(
        self,
        request: services.GetJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[services.GetJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def post_get_job(self, response: resources.Job) -> resources.Job:
        """Post-rpc interceptor for get_job

        DEPRECATED. Please use the `post_get_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TranscoderService server but before
        it is returned to user code. This `post_get_job` interceptor runs
        before the `post_get_job_with_metadata` interceptor.
        """
        return response

    def post_get_job_with_metadata(
        self, response: resources.Job, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[resources.Job, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TranscoderService server but before it is returned to user code.

        We recommend only using this `post_get_job_with_metadata`
        interceptor in new development instead of the `post_get_job` interceptor.
        When both interceptors are used, this `post_get_job_with_metadata` interceptor runs after the
        `post_get_job` interceptor. The (possibly modified) response returned by
        `post_get_job` will be passed to
        `post_get_job_with_metadata`.
        """
        return response, metadata

    def pre_get_job_template(
        self,
        request: services.GetJobTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[services.GetJobTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_job_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def post_get_job_template(
        self, response: resources.JobTemplate
    ) -> resources.JobTemplate:
        """Post-rpc interceptor for get_job_template

        DEPRECATED. Please use the `post_get_job_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TranscoderService server but before
        it is returned to user code. This `post_get_job_template` interceptor runs
        before the `post_get_job_template_with_metadata` interceptor.
        """
        return response

    def post_get_job_template_with_metadata(
        self,
        response: resources.JobTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.JobTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_job_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TranscoderService server but before it is returned to user code.

        We recommend only using this `post_get_job_template_with_metadata`
        interceptor in new development instead of the `post_get_job_template` interceptor.
        When both interceptors are used, this `post_get_job_template_with_metadata` interceptor runs after the
        `post_get_job_template` interceptor. The (possibly modified) response returned by
        `post_get_job_template` will be passed to
        `post_get_job_template_with_metadata`.
        """
        return response, metadata

    def pre_list_jobs(
        self,
        request: services.ListJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[services.ListJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def post_list_jobs(
        self, response: services.ListJobsResponse
    ) -> services.ListJobsResponse:
        """Post-rpc interceptor for list_jobs

        DEPRECATED. Please use the `post_list_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TranscoderService server but before
        it is returned to user code. This `post_list_jobs` interceptor runs
        before the `post_list_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_jobs_with_metadata(
        self,
        response: services.ListJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[services.ListJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TranscoderService server but before it is returned to user code.

        We recommend only using this `post_list_jobs_with_metadata`
        interceptor in new development instead of the `post_list_jobs` interceptor.
        When both interceptors are used, this `post_list_jobs_with_metadata` interceptor runs after the
        `post_list_jobs` interceptor. The (possibly modified) response returned by
        `post_list_jobs` will be passed to
        `post_list_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_job_templates(
        self,
        request: services.ListJobTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        services.ListJobTemplatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_job_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the TranscoderService server.
        """
        return request, metadata

    def post_list_job_templates(
        self, response: services.ListJobTemplatesResponse
    ) -> services.ListJobTemplatesResponse:
        """Post-rpc interceptor for list_job_templates

        DEPRECATED. Please use the `post_list_job_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the TranscoderService server but before
        it is returned to user code. This `post_list_job_templates` interceptor runs
        before the `post_list_job_templates_with_metadata` interceptor.
        """
        return response

    def post_list_job_templates_with_metadata(
        self,
        response: services.ListJobTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        services.ListJobTemplatesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_job_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the TranscoderService server but before it is returned to user code.

        We recommend only using this `post_list_job_templates_with_metadata`
        interceptor in new development instead of the `post_list_job_templates` interceptor.
        When both interceptors are used, this `post_list_job_templates_with_metadata` interceptor runs after the
        `post_list_job_templates` interceptor. The (possibly modified) response returned by
        `post_list_job_templates` will be passed to
        `post_list_job_templates_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class TranscoderServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: TranscoderServiceRestInterceptor


class TranscoderServiceRestTransport(_BaseTranscoderServiceRestTransport):
    """REST backend synchronous transport for TranscoderService.

    Using the Transcoder API, you can queue asynchronous jobs for
    transcoding media into various output formats. Output formats
    may include different streaming standards such as HTTP Live
    Streaming (HLS) and Dynamic Adaptive Streaming over HTTP (DASH).
    You can also customize jobs using advanced features such as
    Digital Rights Management (DRM), audio equalization, content
    concatenation, and digital ad-stitch ready content generation.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "transcoder.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[TranscoderServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'transcoder.googleapis.com').
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
            interceptor (Optional[TranscoderServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or TranscoderServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateJob(
        _BaseTranscoderServiceRestTransport._BaseCreateJob, TranscoderServiceRestStub
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.CreateJob")

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
            request: services.CreateJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Job:
            r"""Call the create job method over HTTP.

            Args:
                request (~.services.CreateJobRequest):
                    The request object. Request message for ``TranscoderService.CreateJob``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Job:
                    Transcoding job resource.
            """

            http_options = (
                _BaseTranscoderServiceRestTransport._BaseCreateJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseCreateJob,
                    "_BaseCreateJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.CreateJob",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "CreateJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._CreateJob._get_response(
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
            resp = resources.Job()
            pb_resp = resources.Job.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Job.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.transcoder_v1.TranscoderServiceClient.create_job",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "CreateJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateJobTemplate(
        _BaseTranscoderServiceRestTransport._BaseCreateJobTemplate,
        TranscoderServiceRestStub,
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.CreateJobTemplate")

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
            request: services.CreateJobTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.JobTemplate:
            r"""Call the create job template method over HTTP.

            Args:
                request (~.services.CreateJobTemplateRequest):
                    The request object. Request message for
                ``TranscoderService.CreateJobTemplate``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.JobTemplate:
                    Transcoding job template resource.
            """

            http_options = _BaseTranscoderServiceRestTransport._BaseCreateJobTemplate._get_http_options()
            request, metadata = self._interceptor.pre_create_job_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseCreateJobTemplate,
                    "_BaseCreateJobTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.CreateJobTemplate",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "CreateJobTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._CreateJobTemplate._get_response(
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
            resp = resources.JobTemplate()
            pb_resp = resources.JobTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_job_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_job_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.JobTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.transcoder_v1.TranscoderServiceClient.create_job_template",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "CreateJobTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteJob(
        _BaseTranscoderServiceRestTransport._BaseDeleteJob, TranscoderServiceRestStub
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.DeleteJob")

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
            request: services.DeleteJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete job method over HTTP.

            Args:
                request (~.services.DeleteJobRequest):
                    The request object. Request message for ``TranscoderService.DeleteJob``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseTranscoderServiceRestTransport._BaseDeleteJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseDeleteJob,
                    "_BaseDeleteJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.DeleteJob",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "DeleteJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._DeleteJob._get_response(
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

    class _DeleteJobTemplate(
        _BaseTranscoderServiceRestTransport._BaseDeleteJobTemplate,
        TranscoderServiceRestStub,
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.DeleteJobTemplate")

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
            request: services.DeleteJobTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete job template method over HTTP.

            Args:
                request (~.services.DeleteJobTemplateRequest):
                    The request object. Request message for
                ``TranscoderService.DeleteJobTemplate``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseTranscoderServiceRestTransport._BaseDeleteJobTemplate._get_http_options()
            request, metadata = self._interceptor.pre_delete_job_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseDeleteJobTemplate,
                    "_BaseDeleteJobTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.DeleteJobTemplate",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "DeleteJobTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._DeleteJobTemplate._get_response(
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

    class _GetJob(
        _BaseTranscoderServiceRestTransport._BaseGetJob, TranscoderServiceRestStub
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.GetJob")

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
            request: services.GetJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Job:
            r"""Call the get job method over HTTP.

            Args:
                request (~.services.GetJobRequest):
                    The request object. Request message for ``TranscoderService.GetJob``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Job:
                    Transcoding job resource.
            """

            http_options = (
                _BaseTranscoderServiceRestTransport._BaseGetJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseGetJob,
                    "_BaseGetJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.GetJob",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "GetJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._GetJob._get_response(
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
            resp = resources.Job()
            pb_resp = resources.Job.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Job.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.transcoder_v1.TranscoderServiceClient.get_job",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "GetJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetJobTemplate(
        _BaseTranscoderServiceRestTransport._BaseGetJobTemplate,
        TranscoderServiceRestStub,
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.GetJobTemplate")

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
            request: services.GetJobTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.JobTemplate:
            r"""Call the get job template method over HTTP.

            Args:
                request (~.services.GetJobTemplateRequest):
                    The request object. Request message for
                ``TranscoderService.GetJobTemplate``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.JobTemplate:
                    Transcoding job template resource.
            """

            http_options = _BaseTranscoderServiceRestTransport._BaseGetJobTemplate._get_http_options()
            request, metadata = self._interceptor.pre_get_job_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseGetJobTemplate,
                    "_BaseGetJobTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.GetJobTemplate",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "GetJobTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._GetJobTemplate._get_response(
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
            resp = resources.JobTemplate()
            pb_resp = resources.JobTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_job_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_job_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.JobTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.transcoder_v1.TranscoderServiceClient.get_job_template",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "GetJobTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListJobs(
        _BaseTranscoderServiceRestTransport._BaseListJobs, TranscoderServiceRestStub
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.ListJobs")

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
            request: services.ListJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> services.ListJobsResponse:
            r"""Call the list jobs method over HTTP.

            Args:
                request (~.services.ListJobsRequest):
                    The request object. Request message for ``TranscoderService.ListJobs``. The
                parent location from which to retrieve the collection of
                jobs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.services.ListJobsResponse:
                    Response message for ``TranscoderService.ListJobs``.
            """

            http_options = (
                _BaseTranscoderServiceRestTransport._BaseListJobs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_jobs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseListJobs,
                    "_BaseListJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.ListJobs",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "ListJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._ListJobs._get_response(
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
            resp = services.ListJobsResponse()
            pb_resp = services.ListJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = services.ListJobsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.transcoder_v1.TranscoderServiceClient.list_jobs",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "ListJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListJobTemplates(
        _BaseTranscoderServiceRestTransport._BaseListJobTemplates,
        TranscoderServiceRestStub,
    ):
        def __hash__(self):
            return hash("TranscoderServiceRestTransport.ListJobTemplates")

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
            request: services.ListJobTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> services.ListJobTemplatesResponse:
            r"""Call the list job templates method over HTTP.

            Args:
                request (~.services.ListJobTemplatesRequest):
                    The request object. Request message for
                ``TranscoderService.ListJobTemplates``.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.services.ListJobTemplatesResponse:
                    Response message for
                ``TranscoderService.ListJobTemplates``.

            """

            http_options = _BaseTranscoderServiceRestTransport._BaseListJobTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_job_templates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseTranscoderServiceRestTransport._BaseListJobTemplates,
                    "_BaseListJobTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.video.transcoder_v1.TranscoderServiceClient.ListJobTemplates",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "ListJobTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = TranscoderServiceRestTransport._ListJobTemplates._get_response(
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
            resp = services.ListJobTemplatesResponse()
            pb_resp = services.ListJobTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_job_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_job_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = services.ListJobTemplatesResponse.to_json(
                        response
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.video.transcoder_v1.TranscoderServiceClient.list_job_templates",
                    extra={
                        "serviceName": "google.cloud.video.transcoder.v1.TranscoderService",
                        "rpcName": "ListJobTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_job(self) -> Callable[[services.CreateJobRequest], resources.Job]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_job_template(
        self,
    ) -> Callable[[services.CreateJobTemplateRequest], resources.JobTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateJobTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_job(self) -> Callable[[services.DeleteJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_job_template(
        self,
    ) -> Callable[[services.DeleteJobTemplateRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteJobTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_job(self) -> Callable[[services.GetJobRequest], resources.Job]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_job_template(
        self,
    ) -> Callable[[services.GetJobTemplateRequest], resources.JobTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetJobTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_jobs(
        self,
    ) -> Callable[[services.ListJobsRequest], services.ListJobsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_job_templates(
        self,
    ) -> Callable[
        [services.ListJobTemplatesRequest], services.ListJobTemplatesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListJobTemplates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("TranscoderServiceRestTransport",)
