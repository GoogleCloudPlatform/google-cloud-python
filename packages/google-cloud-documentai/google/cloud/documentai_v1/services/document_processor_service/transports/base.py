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

import google.api_core
import google.auth  # type: ignore
import google.protobuf
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.documentai_v1 import gapic_version as package_version
from google.cloud.documentai_v1.types import (
    document_processor_service,
    evaluation,
    processor,
    processor_type,
)
from google.cloud.documentai_v1.types import processor as gcd_processor

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

        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.process_document: gapic_v1.method.wrap_method(
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
            ),
            self.batch_process_documents: gapic_v1.method.wrap_method(
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
            ),
            self.fetch_processor_types: gapic_v1.method.wrap_method(
                self.fetch_processor_types,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_processor_types: gapic_v1.method.wrap_method(
                self.list_processor_types,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_processor_type: gapic_v1.method.wrap_method(
                self.get_processor_type,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_processors: gapic_v1.method.wrap_method(
                self.list_processors,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_processor: gapic_v1.method.wrap_method(
                self.get_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.train_processor_version: gapic_v1.method.wrap_method(
                self.train_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_processor_version: gapic_v1.method.wrap_method(
                self.get_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_processor_versions: gapic_v1.method.wrap_method(
                self.list_processor_versions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_processor_version: gapic_v1.method.wrap_method(
                self.delete_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.deploy_processor_version: gapic_v1.method.wrap_method(
                self.deploy_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undeploy_processor_version: gapic_v1.method.wrap_method(
                self.undeploy_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_processor: gapic_v1.method.wrap_method(
                self.create_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_processor: gapic_v1.method.wrap_method(
                self.delete_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.enable_processor: gapic_v1.method.wrap_method(
                self.enable_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.disable_processor: gapic_v1.method.wrap_method(
                self.disable_processor,
                default_timeout=None,
                client_info=client_info,
            ),
            self.set_default_processor_version: gapic_v1.method.wrap_method(
                self.set_default_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.review_document: gapic_v1.method.wrap_method(
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
            ),
            self.evaluate_processor_version: gapic_v1.method.wrap_method(
                self.evaluate_processor_version,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_evaluation: gapic_v1.method.wrap_method(
                self.get_evaluation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_evaluations: gapic_v1.method.wrap_method(
                self.list_evaluations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_location: gapic_v1.method.wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_locations: gapic_v1.method.wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_operation: gapic_v1.method.wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_operations: gapic_v1.method.wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
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
