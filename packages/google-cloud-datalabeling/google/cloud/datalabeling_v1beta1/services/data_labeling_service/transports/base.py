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
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.datalabeling_v1beta1 import gapic_version as package_version
from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set,
    data_labeling_service,
    dataset,
    evaluation,
    evaluation_job,
    instruction,
)
from google.cloud.datalabeling_v1beta1.types import (
    annotation_spec_set as gcd_annotation_spec_set,
)
from google.cloud.datalabeling_v1beta1.types import dataset as gcd_dataset
from google.cloud.datalabeling_v1beta1.types import evaluation_job as gcd_evaluation_job

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class DataLabelingServiceTransport(abc.ABC):
    """Abstract transport class for DataLabelingService."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "datalabeling.googleapis.com"

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
                 The hostname to connect to (default: 'datalabeling.googleapis.com').
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
            self.create_dataset: gapic_v1.method.wrap_method(
                self.create_dataset,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_dataset: gapic_v1.method.wrap_method(
                self.get_dataset,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_datasets: gapic_v1.method.wrap_method(
                self.list_datasets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_dataset: gapic_v1.method.wrap_method(
                self.delete_dataset,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.import_data: gapic_v1.method.wrap_method(
                self.import_data,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.export_data: gapic_v1.method.wrap_method(
                self.export_data,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_data_item: gapic_v1.method.wrap_method(
                self.get_data_item,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_data_items: gapic_v1.method.wrap_method(
                self.list_data_items,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_annotated_dataset: gapic_v1.method.wrap_method(
                self.get_annotated_dataset,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_annotated_datasets: gapic_v1.method.wrap_method(
                self.list_annotated_datasets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_annotated_dataset: gapic_v1.method.wrap_method(
                self.delete_annotated_dataset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.label_image: gapic_v1.method.wrap_method(
                self.label_image,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.label_video: gapic_v1.method.wrap_method(
                self.label_video,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.label_text: gapic_v1.method.wrap_method(
                self.label_text,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_example: gapic_v1.method.wrap_method(
                self.get_example,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_examples: gapic_v1.method.wrap_method(
                self.list_examples,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.create_annotation_spec_set: gapic_v1.method.wrap_method(
                self.create_annotation_spec_set,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_annotation_spec_set: gapic_v1.method.wrap_method(
                self.get_annotation_spec_set,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_annotation_spec_sets: gapic_v1.method.wrap_method(
                self.list_annotation_spec_sets,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_annotation_spec_set: gapic_v1.method.wrap_method(
                self.delete_annotation_spec_set,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.create_instruction: gapic_v1.method.wrap_method(
                self.create_instruction,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_instruction: gapic_v1.method.wrap_method(
                self.get_instruction,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_instructions: gapic_v1.method.wrap_method(
                self.list_instructions,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_instruction: gapic_v1.method.wrap_method(
                self.delete_instruction,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_evaluation: gapic_v1.method.wrap_method(
                self.get_evaluation,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.search_evaluations: gapic_v1.method.wrap_method(
                self.search_evaluations,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.search_example_comparisons: gapic_v1.method.wrap_method(
                self.search_example_comparisons,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.create_evaluation_job: gapic_v1.method.wrap_method(
                self.create_evaluation_job,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.update_evaluation_job: gapic_v1.method.wrap_method(
                self.update_evaluation_job,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.get_evaluation_job: gapic_v1.method.wrap_method(
                self.get_evaluation_job,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.pause_evaluation_job: gapic_v1.method.wrap_method(
                self.pause_evaluation_job,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.resume_evaluation_job: gapic_v1.method.wrap_method(
                self.resume_evaluation_job,
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.delete_evaluation_job: gapic_v1.method.wrap_method(
                self.delete_evaluation_job,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
                client_info=client_info,
            ),
            self.list_evaluation_jobs: gapic_v1.method.wrap_method(
                self.list_evaluation_jobs,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=30.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=30.0,
                ),
                default_timeout=30.0,
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
    def create_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.CreateDatasetRequest],
        Union[gcd_dataset.Dataset, Awaitable[gcd_dataset.Dataset]],
    ]:
        raise NotImplementedError()

    @property
    def get_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.GetDatasetRequest],
        Union[dataset.Dataset, Awaitable[dataset.Dataset]],
    ]:
        raise NotImplementedError()

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [data_labeling_service.ListDatasetsRequest],
        Union[
            data_labeling_service.ListDatasetsResponse,
            Awaitable[data_labeling_service.ListDatasetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteDatasetRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def import_data(
        self,
    ) -> Callable[
        [data_labeling_service.ImportDataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_data(
        self,
    ) -> Callable[
        [data_labeling_service.ExportDataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_data_item(
        self,
    ) -> Callable[
        [data_labeling_service.GetDataItemRequest],
        Union[dataset.DataItem, Awaitable[dataset.DataItem]],
    ]:
        raise NotImplementedError()

    @property
    def list_data_items(
        self,
    ) -> Callable[
        [data_labeling_service.ListDataItemsRequest],
        Union[
            data_labeling_service.ListDataItemsResponse,
            Awaitable[data_labeling_service.ListDataItemsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_annotated_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.GetAnnotatedDatasetRequest],
        Union[dataset.AnnotatedDataset, Awaitable[dataset.AnnotatedDataset]],
    ]:
        raise NotImplementedError()

    @property
    def list_annotated_datasets(
        self,
    ) -> Callable[
        [data_labeling_service.ListAnnotatedDatasetsRequest],
        Union[
            data_labeling_service.ListAnnotatedDatasetsResponse,
            Awaitable[data_labeling_service.ListAnnotatedDatasetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_annotated_dataset(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteAnnotatedDatasetRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def label_image(
        self,
    ) -> Callable[
        [data_labeling_service.LabelImageRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def label_video(
        self,
    ) -> Callable[
        [data_labeling_service.LabelVideoRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def label_text(
        self,
    ) -> Callable[
        [data_labeling_service.LabelTextRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_example(
        self,
    ) -> Callable[
        [data_labeling_service.GetExampleRequest],
        Union[dataset.Example, Awaitable[dataset.Example]],
    ]:
        raise NotImplementedError()

    @property
    def list_examples(
        self,
    ) -> Callable[
        [data_labeling_service.ListExamplesRequest],
        Union[
            data_labeling_service.ListExamplesResponse,
            Awaitable[data_labeling_service.ListExamplesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_annotation_spec_set(
        self,
    ) -> Callable[
        [data_labeling_service.CreateAnnotationSpecSetRequest],
        Union[
            gcd_annotation_spec_set.AnnotationSpecSet,
            Awaitable[gcd_annotation_spec_set.AnnotationSpecSet],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_annotation_spec_set(
        self,
    ) -> Callable[
        [data_labeling_service.GetAnnotationSpecSetRequest],
        Union[
            annotation_spec_set.AnnotationSpecSet,
            Awaitable[annotation_spec_set.AnnotationSpecSet],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_annotation_spec_sets(
        self,
    ) -> Callable[
        [data_labeling_service.ListAnnotationSpecSetsRequest],
        Union[
            data_labeling_service.ListAnnotationSpecSetsResponse,
            Awaitable[data_labeling_service.ListAnnotationSpecSetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_annotation_spec_set(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteAnnotationSpecSetRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_instruction(
        self,
    ) -> Callable[
        [data_labeling_service.CreateInstructionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_instruction(
        self,
    ) -> Callable[
        [data_labeling_service.GetInstructionRequest],
        Union[instruction.Instruction, Awaitable[instruction.Instruction]],
    ]:
        raise NotImplementedError()

    @property
    def list_instructions(
        self,
    ) -> Callable[
        [data_labeling_service.ListInstructionsRequest],
        Union[
            data_labeling_service.ListInstructionsResponse,
            Awaitable[data_labeling_service.ListInstructionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_instruction(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteInstructionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_evaluation(
        self,
    ) -> Callable[
        [data_labeling_service.GetEvaluationRequest],
        Union[evaluation.Evaluation, Awaitable[evaluation.Evaluation]],
    ]:
        raise NotImplementedError()

    @property
    def search_evaluations(
        self,
    ) -> Callable[
        [data_labeling_service.SearchEvaluationsRequest],
        Union[
            data_labeling_service.SearchEvaluationsResponse,
            Awaitable[data_labeling_service.SearchEvaluationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_example_comparisons(
        self,
    ) -> Callable[
        [data_labeling_service.SearchExampleComparisonsRequest],
        Union[
            data_labeling_service.SearchExampleComparisonsResponse,
            Awaitable[data_labeling_service.SearchExampleComparisonsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.CreateEvaluationJobRequest],
        Union[evaluation_job.EvaluationJob, Awaitable[evaluation_job.EvaluationJob]],
    ]:
        raise NotImplementedError()

    @property
    def update_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.UpdateEvaluationJobRequest],
        Union[
            gcd_evaluation_job.EvaluationJob,
            Awaitable[gcd_evaluation_job.EvaluationJob],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.GetEvaluationJobRequest],
        Union[evaluation_job.EvaluationJob, Awaitable[evaluation_job.EvaluationJob]],
    ]:
        raise NotImplementedError()

    @property
    def pause_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.PauseEvaluationJobRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def resume_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.ResumeEvaluationJobRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def delete_evaluation_job(
        self,
    ) -> Callable[
        [data_labeling_service.DeleteEvaluationJobRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_evaluation_jobs(
        self,
    ) -> Callable[
        [data_labeling_service.ListEvaluationJobsRequest],
        Union[
            data_labeling_service.ListEvaluationJobsResponse,
            Awaitable[data_labeling_service.ListEvaluationJobsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("DataLabelingServiceTransport",)
