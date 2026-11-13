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

from google.cloud.billing.budgets_v1._compat import transcode_request
from google.cloud.billing.budgets_v1.types import budget_model, budget_service

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseBudgetServiceRestTransport

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


class BudgetServiceRestInterceptor:
    """Interceptor for BudgetService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the BudgetServiceRestTransport.

    .. code-block:: python
        class MyCustomBudgetServiceInterceptor(BudgetServiceRestInterceptor):
            def pre_create_budget(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_budget(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_budget(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_budget(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_budget(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_budgets(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_budgets(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_budget(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_budget(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = BudgetServiceRestTransport(interceptor=MyCustomBudgetServiceInterceptor())
        client = BudgetServiceClient(transport=transport)


    """

    def pre_create_budget(
        self,
        request: budget_service.CreateBudgetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        budget_service.CreateBudgetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_budget

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BudgetService server.
        """
        return request, metadata

    def post_create_budget(self, response: budget_model.Budget) -> budget_model.Budget:
        """Post-rpc interceptor for create_budget

        DEPRECATED. Please use the `post_create_budget_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BudgetService server but before
        it is returned to user code. This `post_create_budget` interceptor runs
        before the `post_create_budget_with_metadata` interceptor.
        """
        return response

    def post_create_budget_with_metadata(
        self,
        response: budget_model.Budget,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[budget_model.Budget, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_budget

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BudgetService server but before it is returned to user code.

        We recommend only using this `post_create_budget_with_metadata`
        interceptor in new development instead of the `post_create_budget` interceptor.
        When both interceptors are used, this `post_create_budget_with_metadata` interceptor runs after the
        `post_create_budget` interceptor. The (possibly modified) response returned by
        `post_create_budget` will be passed to
        `post_create_budget_with_metadata`.
        """
        return response, metadata

    def pre_delete_budget(
        self,
        request: budget_service.DeleteBudgetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        budget_service.DeleteBudgetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_budget

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BudgetService server.
        """
        return request, metadata

    def pre_get_budget(
        self,
        request: budget_service.GetBudgetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        budget_service.GetBudgetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_budget

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BudgetService server.
        """
        return request, metadata

    def post_get_budget(self, response: budget_model.Budget) -> budget_model.Budget:
        """Post-rpc interceptor for get_budget

        DEPRECATED. Please use the `post_get_budget_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BudgetService server but before
        it is returned to user code. This `post_get_budget` interceptor runs
        before the `post_get_budget_with_metadata` interceptor.
        """
        return response

    def post_get_budget_with_metadata(
        self,
        response: budget_model.Budget,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[budget_model.Budget, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_budget

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BudgetService server but before it is returned to user code.

        We recommend only using this `post_get_budget_with_metadata`
        interceptor in new development instead of the `post_get_budget` interceptor.
        When both interceptors are used, this `post_get_budget_with_metadata` interceptor runs after the
        `post_get_budget` interceptor. The (possibly modified) response returned by
        `post_get_budget` will be passed to
        `post_get_budget_with_metadata`.
        """
        return response, metadata

    def pre_list_budgets(
        self,
        request: budget_service.ListBudgetsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        budget_service.ListBudgetsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_budgets

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BudgetService server.
        """
        return request, metadata

    def post_list_budgets(
        self, response: budget_service.ListBudgetsResponse
    ) -> budget_service.ListBudgetsResponse:
        """Post-rpc interceptor for list_budgets

        DEPRECATED. Please use the `post_list_budgets_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BudgetService server but before
        it is returned to user code. This `post_list_budgets` interceptor runs
        before the `post_list_budgets_with_metadata` interceptor.
        """
        return response

    def post_list_budgets_with_metadata(
        self,
        response: budget_service.ListBudgetsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        budget_service.ListBudgetsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_budgets

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BudgetService server but before it is returned to user code.

        We recommend only using this `post_list_budgets_with_metadata`
        interceptor in new development instead of the `post_list_budgets` interceptor.
        When both interceptors are used, this `post_list_budgets_with_metadata` interceptor runs after the
        `post_list_budgets` interceptor. The (possibly modified) response returned by
        `post_list_budgets` will be passed to
        `post_list_budgets_with_metadata`.
        """
        return response, metadata

    def pre_update_budget(
        self,
        request: budget_service.UpdateBudgetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        budget_service.UpdateBudgetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_budget

        Override in a subclass to manipulate the request or metadata
        before they are sent to the BudgetService server.
        """
        return request, metadata

    def post_update_budget(self, response: budget_model.Budget) -> budget_model.Budget:
        """Post-rpc interceptor for update_budget

        DEPRECATED. Please use the `post_update_budget_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the BudgetService server but before
        it is returned to user code. This `post_update_budget` interceptor runs
        before the `post_update_budget_with_metadata` interceptor.
        """
        return response

    def post_update_budget_with_metadata(
        self,
        response: budget_model.Budget,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[budget_model.Budget, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_budget

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the BudgetService server but before it is returned to user code.

        We recommend only using this `post_update_budget_with_metadata`
        interceptor in new development instead of the `post_update_budget` interceptor.
        When both interceptors are used, this `post_update_budget_with_metadata` interceptor runs after the
        `post_update_budget` interceptor. The (possibly modified) response returned by
        `post_update_budget` will be passed to
        `post_update_budget_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class BudgetServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: BudgetServiceRestInterceptor


class BudgetServiceRestTransport(_BaseBudgetServiceRestTransport):
    """REST backend synchronous transport for BudgetService.

    BudgetService stores Cloud Billing budgets, which define a
    budget plan and rules to execute as we track spend against that
    plan.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "billingbudgets.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[BudgetServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'billingbudgets.googleapis.com').
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
            interceptor (Optional[BudgetServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or BudgetServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _CreateBudget(
        _BaseBudgetServiceRestTransport._BaseCreateBudget, BudgetServiceRestStub
    ):
        def __hash__(self):
            return hash("BudgetServiceRestTransport.CreateBudget")

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
            request: budget_service.CreateBudgetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> budget_model.Budget:
            r"""Call the create budget method over HTTP.

            Args:
                request (~.budget_service.CreateBudgetRequest):
                    The request object. Request for CreateBudget
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.budget_model.Budget:
                    A budget is a plan that describes
                what you expect to spend on Cloud
                projects, plus the rules to execute as
                spend is tracked against that plan, (for
                example, send an alert when 90% of the
                target spend is met). The budget time
                period is configurable, with options
                such as month (default), quarter, year,
                or custom time period.

            """

            http_options = (
                _BaseBudgetServiceRestTransport._BaseCreateBudget._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_budget(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBudgetServiceRestTransport._BaseCreateBudget,
                    "_BaseCreateBudget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.billing.budgets_v1.BudgetServiceClient.CreateBudget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "CreateBudget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BudgetServiceRestTransport._CreateBudget._get_response(
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
            resp = budget_model.Budget()
            pb_resp = budget_model.Budget.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_budget(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_budget_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = budget_model.Budget.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.billing.budgets_v1.BudgetServiceClient.create_budget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "CreateBudget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteBudget(
        _BaseBudgetServiceRestTransport._BaseDeleteBudget, BudgetServiceRestStub
    ):
        def __hash__(self):
            return hash("BudgetServiceRestTransport.DeleteBudget")

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
            request: budget_service.DeleteBudgetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete budget method over HTTP.

            Args:
                request (~.budget_service.DeleteBudgetRequest):
                    The request object. Request for DeleteBudget
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseBudgetServiceRestTransport._BaseDeleteBudget._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_budget(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBudgetServiceRestTransport._BaseDeleteBudget,
                    "_BaseDeleteBudget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.billing.budgets_v1.BudgetServiceClient.DeleteBudget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "DeleteBudget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BudgetServiceRestTransport._DeleteBudget._get_response(
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

    class _GetBudget(
        _BaseBudgetServiceRestTransport._BaseGetBudget, BudgetServiceRestStub
    ):
        def __hash__(self):
            return hash("BudgetServiceRestTransport.GetBudget")

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
            request: budget_service.GetBudgetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> budget_model.Budget:
            r"""Call the get budget method over HTTP.

            Args:
                request (~.budget_service.GetBudgetRequest):
                    The request object. Request for GetBudget
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.budget_model.Budget:
                    A budget is a plan that describes
                what you expect to spend on Cloud
                projects, plus the rules to execute as
                spend is tracked against that plan, (for
                example, send an alert when 90% of the
                target spend is met). The budget time
                period is configurable, with options
                such as month (default), quarter, year,
                or custom time period.

            """

            http_options = (
                _BaseBudgetServiceRestTransport._BaseGetBudget._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_budget(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBudgetServiceRestTransport._BaseGetBudget,
                    "_BaseGetBudget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.billing.budgets_v1.BudgetServiceClient.GetBudget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "GetBudget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BudgetServiceRestTransport._GetBudget._get_response(
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
            resp = budget_model.Budget()
            pb_resp = budget_model.Budget.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_budget(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_budget_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = budget_model.Budget.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.billing.budgets_v1.BudgetServiceClient.get_budget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "GetBudget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListBudgets(
        _BaseBudgetServiceRestTransport._BaseListBudgets, BudgetServiceRestStub
    ):
        def __hash__(self):
            return hash("BudgetServiceRestTransport.ListBudgets")

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
            request: budget_service.ListBudgetsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> budget_service.ListBudgetsResponse:
            r"""Call the list budgets method over HTTP.

            Args:
                request (~.budget_service.ListBudgetsRequest):
                    The request object. Request for ListBudgets
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.budget_service.ListBudgetsResponse:
                    Response for ListBudgets
            """

            http_options = (
                _BaseBudgetServiceRestTransport._BaseListBudgets._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_budgets(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBudgetServiceRestTransport._BaseListBudgets,
                    "_BaseListBudgets__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.billing.budgets_v1.BudgetServiceClient.ListBudgets",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "ListBudgets",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BudgetServiceRestTransport._ListBudgets._get_response(
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
            resp = budget_service.ListBudgetsResponse()
            pb_resp = budget_service.ListBudgetsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_budgets(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_budgets_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = budget_service.ListBudgetsResponse.to_json(
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
                    "Received response for google.cloud.billing.budgets_v1.BudgetServiceClient.list_budgets",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "ListBudgets",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateBudget(
        _BaseBudgetServiceRestTransport._BaseUpdateBudget, BudgetServiceRestStub
    ):
        def __hash__(self):
            return hash("BudgetServiceRestTransport.UpdateBudget")

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
            request: budget_service.UpdateBudgetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> budget_model.Budget:
            r"""Call the update budget method over HTTP.

            Args:
                request (~.budget_service.UpdateBudgetRequest):
                    The request object. Request for UpdateBudget
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.budget_model.Budget:
                    A budget is a plan that describes
                what you expect to spend on Cloud
                projects, plus the rules to execute as
                spend is tracked against that plan, (for
                example, send an alert when 90% of the
                target spend is met). The budget time
                period is configurable, with options
                such as month (default), quarter, year,
                or custom time period.

            """

            http_options = (
                _BaseBudgetServiceRestTransport._BaseUpdateBudget._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_budget(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseBudgetServiceRestTransport._BaseUpdateBudget,
                    "_BaseUpdateBudget__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.billing.budgets_v1.BudgetServiceClient.UpdateBudget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "UpdateBudget",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = BudgetServiceRestTransport._UpdateBudget._get_response(
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
            resp = budget_model.Budget()
            pb_resp = budget_model.Budget.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_budget(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_budget_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = budget_model.Budget.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.billing.budgets_v1.BudgetServiceClient.update_budget",
                    extra={
                        "serviceName": "google.cloud.billing.budgets.v1.BudgetService",
                        "rpcName": "UpdateBudget",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_budget(
        self,
    ) -> Callable[[budget_service.CreateBudgetRequest], budget_model.Budget]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateBudget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_budget(
        self,
    ) -> Callable[[budget_service.DeleteBudgetRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteBudget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_budget(
        self,
    ) -> Callable[[budget_service.GetBudgetRequest], budget_model.Budget]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetBudget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_budgets(
        self,
    ) -> Callable[
        [budget_service.ListBudgetsRequest], budget_service.ListBudgetsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListBudgets(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_budget(
        self,
    ) -> Callable[[budget_service.UpdateBudgetRequest], budget_model.Budget]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateBudget(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("BudgetServiceRestTransport",)
