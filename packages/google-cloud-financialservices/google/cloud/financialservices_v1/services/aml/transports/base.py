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

from google.cloud.financialservices_v1 import gapic_version as package_version
from google.cloud.financialservices_v1._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.financialservices_v1._compat import (
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

from google.cloud.financialservices_v1.types import (
    backtest_result,
    dataset,
    engine_config,
    engine_version,
    instance,
    model,
    prediction_result,
)
from google.cloud.financialservices_v1.types import (
    backtest_result as gcf_backtest_result,
)
from google.cloud.financialservices_v1.types import dataset as gcf_dataset
from google.cloud.financialservices_v1.types import engine_config as gcf_engine_config
from google.cloud.financialservices_v1.types import instance as gcf_instance
from google.cloud.financialservices_v1.types import model as gcf_model
from google.cloud.financialservices_v1.types import (
    prediction_result as gcf_prediction_result,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class AMLTransport(abc.ABC):
    """Abstract transport class for AML."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "financialservices.googleapis.com"

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
                 The hostname to connect to (default: 'financialservices.googleapis.com').
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
            self.list_instances: self._wrap_method(
                self.list_instances,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListInstances",
            ),
            self.get_instance: self._wrap_method(
                self.get_instance,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetInstance",
            ),
            self.create_instance: self._wrap_method(
                self.create_instance,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/CreateInstance",
            ),
            self.update_instance: self._wrap_method(
                self.update_instance,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/UpdateInstance",
            ),
            self.delete_instance: self._wrap_method(
                self.delete_instance,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/DeleteInstance",
            ),
            self.import_registered_parties: self._wrap_method(
                self.import_registered_parties,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ImportRegisteredParties",
            ),
            self.export_registered_parties: self._wrap_method(
                self.export_registered_parties,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ExportRegisteredParties",
            ),
            self.list_datasets: self._wrap_method(
                self.list_datasets,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListDatasets",
            ),
            self.get_dataset: self._wrap_method(
                self.get_dataset,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetDataset",
            ),
            self.create_dataset: self._wrap_method(
                self.create_dataset,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/CreateDataset",
            ),
            self.update_dataset: self._wrap_method(
                self.update_dataset,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/UpdateDataset",
            ),
            self.delete_dataset: self._wrap_method(
                self.delete_dataset,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/DeleteDataset",
            ),
            self.list_models: self._wrap_method(
                self.list_models,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListModels",
            ),
            self.get_model: self._wrap_method(
                self.get_model,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetModel",
            ),
            self.create_model: self._wrap_method(
                self.create_model,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/CreateModel",
            ),
            self.update_model: self._wrap_method(
                self.update_model,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/UpdateModel",
            ),
            self.export_model_metadata: self._wrap_method(
                self.export_model_metadata,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ExportModelMetadata",
            ),
            self.delete_model: self._wrap_method(
                self.delete_model,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/DeleteModel",
            ),
            self.list_engine_configs: self._wrap_method(
                self.list_engine_configs,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListEngineConfigs",
            ),
            self.get_engine_config: self._wrap_method(
                self.get_engine_config,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetEngineConfig",
            ),
            self.create_engine_config: self._wrap_method(
                self.create_engine_config,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/CreateEngineConfig",
            ),
            self.update_engine_config: self._wrap_method(
                self.update_engine_config,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/UpdateEngineConfig",
            ),
            self.export_engine_config_metadata: self._wrap_method(
                self.export_engine_config_metadata,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ExportEngineConfigMetadata",
            ),
            self.delete_engine_config: self._wrap_method(
                self.delete_engine_config,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/DeleteEngineConfig",
            ),
            self.get_engine_version: self._wrap_method(
                self.get_engine_version,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetEngineVersion",
            ),
            self.list_engine_versions: self._wrap_method(
                self.list_engine_versions,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListEngineVersions",
            ),
            self.list_prediction_results: self._wrap_method(
                self.list_prediction_results,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListPredictionResults",
            ),
            self.get_prediction_result: self._wrap_method(
                self.get_prediction_result,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetPredictionResult",
            ),
            self.create_prediction_result: self._wrap_method(
                self.create_prediction_result,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/CreatePredictionResult",
            ),
            self.update_prediction_result: self._wrap_method(
                self.update_prediction_result,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/UpdatePredictionResult",
            ),
            self.export_prediction_result_metadata: self._wrap_method(
                self.export_prediction_result_metadata,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ExportPredictionResultMetadata",
            ),
            self.delete_prediction_result: self._wrap_method(
                self.delete_prediction_result,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/DeletePredictionResult",
            ),
            self.list_backtest_results: self._wrap_method(
                self.list_backtest_results,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ListBacktestResults",
            ),
            self.get_backtest_result: self._wrap_method(
                self.get_backtest_result,
                default_timeout=10.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/GetBacktestResult",
            ),
            self.create_backtest_result: self._wrap_method(
                self.create_backtest_result,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/CreateBacktestResult",
            ),
            self.update_backtest_result: self._wrap_method(
                self.update_backtest_result,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/UpdateBacktestResult",
            ),
            self.export_backtest_result_metadata: self._wrap_method(
                self.export_backtest_result_metadata,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/ExportBacktestResultMetadata",
            ),
            self.delete_backtest_result: self._wrap_method(
                self.delete_backtest_result,
                default_timeout=120.0,
                client_info=client_info,
                method_name="google.cloud.financialservices.v1.AML/DeleteBacktestResult",
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
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/DeleteOperation",
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
    def list_instances(
        self,
    ) -> Callable[
        [instance.ListInstancesRequest],
        Union[
            instance.ListInstancesResponse, Awaitable[instance.ListInstancesResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_instance(
        self,
    ) -> Callable[
        [instance.GetInstanceRequest],
        Union[instance.Instance, Awaitable[instance.Instance]],
    ]:
        raise NotImplementedError()

    @property
    def create_instance(
        self,
    ) -> Callable[
        [gcf_instance.CreateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_instance(
        self,
    ) -> Callable[
        [gcf_instance.UpdateInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_instance(
        self,
    ) -> Callable[
        [instance.DeleteInstanceRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_registered_parties(
        self,
    ) -> Callable[
        [instance.ImportRegisteredPartiesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_registered_parties(
        self,
    ) -> Callable[
        [instance.ExportRegisteredPartiesRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [dataset.ListDatasetsRequest],
        Union[dataset.ListDatasetsResponse, Awaitable[dataset.ListDatasetsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_dataset(
        self,
    ) -> Callable[
        [dataset.GetDatasetRequest], Union[dataset.Dataset, Awaitable[dataset.Dataset]]
    ]:
        raise NotImplementedError()

    @property
    def create_dataset(
        self,
    ) -> Callable[
        [gcf_dataset.CreateDatasetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_dataset(
        self,
    ) -> Callable[
        [gcf_dataset.UpdateDatasetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_dataset(
        self,
    ) -> Callable[
        [dataset.DeleteDatasetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_models(
        self,
    ) -> Callable[
        [model.ListModelsRequest],
        Union[model.ListModelsResponse, Awaitable[model.ListModelsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def get_model(
        self,
    ) -> Callable[[model.GetModelRequest], Union[model.Model, Awaitable[model.Model]]]:
        raise NotImplementedError()

    @property
    def create_model(
        self,
    ) -> Callable[
        [gcf_model.CreateModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_model(
        self,
    ) -> Callable[
        [gcf_model.UpdateModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_model_metadata(
        self,
    ) -> Callable[
        [gcf_model.ExportModelMetadataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_model(
        self,
    ) -> Callable[
        [model.DeleteModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_engine_configs(
        self,
    ) -> Callable[
        [engine_config.ListEngineConfigsRequest],
        Union[
            engine_config.ListEngineConfigsResponse,
            Awaitable[engine_config.ListEngineConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_engine_config(
        self,
    ) -> Callable[
        [engine_config.GetEngineConfigRequest],
        Union[engine_config.EngineConfig, Awaitable[engine_config.EngineConfig]],
    ]:
        raise NotImplementedError()

    @property
    def create_engine_config(
        self,
    ) -> Callable[
        [gcf_engine_config.CreateEngineConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_engine_config(
        self,
    ) -> Callable[
        [gcf_engine_config.UpdateEngineConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_engine_config_metadata(
        self,
    ) -> Callable[
        [gcf_engine_config.ExportEngineConfigMetadataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_engine_config(
        self,
    ) -> Callable[
        [engine_config.DeleteEngineConfigRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_engine_version(
        self,
    ) -> Callable[
        [engine_version.GetEngineVersionRequest],
        Union[engine_version.EngineVersion, Awaitable[engine_version.EngineVersion]],
    ]:
        raise NotImplementedError()

    @property
    def list_engine_versions(
        self,
    ) -> Callable[
        [engine_version.ListEngineVersionsRequest],
        Union[
            engine_version.ListEngineVersionsResponse,
            Awaitable[engine_version.ListEngineVersionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_prediction_results(
        self,
    ) -> Callable[
        [prediction_result.ListPredictionResultsRequest],
        Union[
            prediction_result.ListPredictionResultsResponse,
            Awaitable[prediction_result.ListPredictionResultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_prediction_result(
        self,
    ) -> Callable[
        [prediction_result.GetPredictionResultRequest],
        Union[
            prediction_result.PredictionResult,
            Awaitable[prediction_result.PredictionResult],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_prediction_result(
        self,
    ) -> Callable[
        [gcf_prediction_result.CreatePredictionResultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_prediction_result(
        self,
    ) -> Callable[
        [gcf_prediction_result.UpdatePredictionResultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_prediction_result_metadata(
        self,
    ) -> Callable[
        [gcf_prediction_result.ExportPredictionResultMetadataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_prediction_result(
        self,
    ) -> Callable[
        [prediction_result.DeletePredictionResultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_backtest_results(
        self,
    ) -> Callable[
        [backtest_result.ListBacktestResultsRequest],
        Union[
            backtest_result.ListBacktestResultsResponse,
            Awaitable[backtest_result.ListBacktestResultsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_backtest_result(
        self,
    ) -> Callable[
        [backtest_result.GetBacktestResultRequest],
        Union[
            backtest_result.BacktestResult, Awaitable[backtest_result.BacktestResult]
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_backtest_result(
        self,
    ) -> Callable[
        [gcf_backtest_result.CreateBacktestResultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_backtest_result(
        self,
    ) -> Callable[
        [gcf_backtest_result.UpdateBacktestResultRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_backtest_result_metadata(
        self,
    ) -> Callable[
        [gcf_backtest_result.ExportBacktestResultMetadataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_backtest_result(
        self,
    ) -> Callable[
        [backtest_result.DeleteBacktestResultRequest],
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
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
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


__all__ = ("AMLTransport",)
