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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union

from google.cloud.documentai_v1beta3 import gapic_version as package_version
from google.cloud.documentai_v1beta3._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.documentai_v1beta3._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.documentai_v1beta3.types import (
    document_processor_service,
    evaluation,
    processor,
    processor_type,
)
from google.cloud.documentai_v1beta3.types import processor as gcd_processor

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DocumentProcessorServiceTransport(abc.ABC):
    """Abstract transport class for DocumentProcessorService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "documentai.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        api_audience: Optional[str] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'documentai.googleapis.com').
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): Deprecated. A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials. This argument will be
                removed in the next major version of this library.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
        """

        # Save the scopes.
        self._scopes = scopes
        if not hasattr(self, "_ignore_credentials"):
            self._ignore_credentials: bool = False

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file,
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
        elif credentials is None and not self._ignore_credentials:
            credentials, _ = google.auth.default(
                scopes=scopes,
                quota_project_id=quota_project_id,
                default_scopes=self.AUTH_SCOPES,
            )
            # Don't apply audience if the credentials file passed from user.
            if hasattr(credentials, "with_gdch_audience"):
                credentials = credentials.with_gdch_audience(
                    api_audience if api_audience else host
                )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        self._client_options = client_options
        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _wrap_method(self, func, *args, **kwargs):
        """Wrap an RPC method with common client-level features.

        Applies retry, timeout, metadata, and tracing wrappers to the
        underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method.wrap_method(func, *args, **kwargs)

    def _wrap_async_method(self, func, *args, **kwargs):
        """Wrap an async RPC method with common client-level features.

        Applies asynchronous retry, timeout, metadata, and tracing wrappers
        to the underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _ASYNC_WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method_async.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _ASYNC_WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for RPC dispatch."""
        self._wrapped_methods = {
            self.process_document: self._wrap_method(
                self.process_document,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=90.0,
                    multiplier=9.0,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ResourceExhausted,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=300.0,
                ),
                default_timeout=300.0,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ProcessDocument",
            ),
            self.batch_process_documents: self._wrap_method(
                self.batch_process_documents,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/BatchProcessDocuments",
            ),
            self.fetch_processor_types: self._wrap_method(
                self.fetch_processor_types,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/FetchProcessorTypes",
            ),
            self.list_processor_types: self._wrap_method(
                self.list_processor_types,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ListProcessorTypes",
            ),
            self.get_processor_type: self._wrap_method(
                self.get_processor_type,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/GetProcessorType",
            ),
            self.list_processors: self._wrap_method(
                self.list_processors,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ListProcessors",
            ),
            self.get_processor: self._wrap_method(
                self.get_processor,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/GetProcessor",
            ),
            self.train_processor_version: self._wrap_method(
                self.train_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/TrainProcessorVersion",
            ),
            self.get_processor_version: self._wrap_method(
                self.get_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/GetProcessorVersion",
            ),
            self.list_processor_versions: self._wrap_method(
                self.list_processor_versions,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ListProcessorVersions",
            ),
            self.delete_processor_version: self._wrap_method(
                self.delete_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/DeleteProcessorVersion",
            ),
            self.deploy_processor_version: self._wrap_method(
                self.deploy_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/DeployProcessorVersion",
            ),
            self.undeploy_processor_version: self._wrap_method(
                self.undeploy_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/UndeployProcessorVersion",
            ),
            self.create_processor: self._wrap_method(
                self.create_processor,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/CreateProcessor",
            ),
            self.delete_processor: self._wrap_method(
                self.delete_processor,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/DeleteProcessor",
            ),
            self.enable_processor: self._wrap_method(
                self.enable_processor,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/EnableProcessor",
            ),
            self.disable_processor: self._wrap_method(
                self.disable_processor,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/DisableProcessor",
            ),
            self.set_default_processor_version: self._wrap_method(
                self.set_default_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/SetDefaultProcessorVersion",
            ),
            self.review_document: self._wrap_method(
                self.review_document,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ReviewDocument",
            ),
            self.evaluate_processor_version: self._wrap_method(
                self.evaluate_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/EvaluateProcessorVersion",
            ),
            self.get_evaluation: self._wrap_method(
                self.get_evaluation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/GetEvaluation",
            ),
            self.list_evaluations: self._wrap_method(
                self.list_evaluations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ListEvaluations",
            ),
            self.import_processor_version: self._wrap_method(
                self.import_processor_version,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.documentai.v1beta3.DocumentProcessorService/ImportProcessorVersion",
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/GetLocation",
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/ListLocations",
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/CancelOperation",
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
            ),
        }

    def close(self):
        """Closes resources associated with the transport.

        .. warning::
             Only call this method if the transport is NOT shared
             with other clients - this may cause errors in other clients!
        """
        raise NotImplementedError()

    @property
    def operations_client(self):
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def process_document(
        self,
    ) -> Callable[
        [document_processor_service.ProcessRequest],
        Union[
            document_processor_service.ProcessResponse,
            Awaitable[document_processor_service.ProcessResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_process_documents(
        self,
    ) -> Callable[
        [document_processor_service.BatchProcessRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def fetch_processor_types(
        self,
    ) -> Callable[
        [document_processor_service.FetchProcessorTypesRequest],
        Union[
            document_processor_service.FetchProcessorTypesResponse,
            Awaitable[document_processor_service.FetchProcessorTypesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_processor_types(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorTypesRequest],
        Union[
            document_processor_service.ListProcessorTypesResponse,
            Awaitable[document_processor_service.ListProcessorTypesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_processor_type(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorTypeRequest],
        Union[processor_type.ProcessorType, Awaitable[processor_type.ProcessorType]],
    ]:
        raise NotImplementedError()

    @property
    def list_processors(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorsRequest],
        Union[
            document_processor_service.ListProcessorsResponse,
            Awaitable[document_processor_service.ListProcessorsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_processor(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorRequest],
        Union[processor.Processor, Awaitable[processor.Processor]],
    ]:
        raise NotImplementedError()

    @property
    def train_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.TrainProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.GetProcessorVersionRequest],
        Union[processor.ProcessorVersion, Awaitable[processor.ProcessorVersion]],
    ]:
        raise NotImplementedError()

    @property
    def list_processor_versions(
        self,
    ) -> Callable[
        [document_processor_service.ListProcessorVersionsRequest],
        Union[
            document_processor_service.ListProcessorVersionsResponse,
            Awaitable[document_processor_service.ListProcessorVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.DeleteProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def deploy_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.DeployProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def undeploy_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.UndeployProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_processor(
        self,
    ) -> Callable[
        [document_processor_service.CreateProcessorRequest],
        Union[gcd_processor.Processor, Awaitable[gcd_processor.Processor]],
    ]:
        raise NotImplementedError()

    @property
    def delete_processor(
        self,
    ) -> Callable[
        [document_processor_service.DeleteProcessorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def enable_processor(
        self,
    ) -> Callable[
        [document_processor_service.EnableProcessorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def disable_processor(
        self,
    ) -> Callable[
        [document_processor_service.DisableProcessorRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def set_default_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.SetDefaultProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def review_document(
        self,
    ) -> Callable[
        [document_processor_service.ReviewDocumentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def evaluate_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.EvaluateProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_evaluation(
        self,
    ) -> Callable[
        [document_processor_service.GetEvaluationRequest],
        Union[evaluation.Evaluation, Awaitable[evaluation.Evaluation]],
    ]:
        raise NotImplementedError()

    @property
    def list_evaluations(
        self,
    ) -> Callable[
        [document_processor_service.ListEvaluationsRequest],
        Union[
            document_processor_service.ListEvaluationsResponse,
            Awaitable[document_processor_service.ListEvaluationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def import_processor_version(
        self,
    ) -> Callable[
        [document_processor_service.ImportProcessorVersionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_operations(
        self,
    ) -> Callable[
        [operations_pb2.ListOperationsRequest],
        Union[
            operations_pb2.ListOperationsResponse,
            Awaitable[operations_pb2.ListOperationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_operation(
        self,
    ) -> Callable[
        [operations_pb2.GetOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def cancel_operation(
        self,
    ) -> Callable[
        [operations_pb2.CancelOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("DocumentProcessorServiceTransport",)
