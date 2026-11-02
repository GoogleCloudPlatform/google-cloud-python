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
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.visionai_v1 import gapic_version as package_version
from google.cloud.visionai_v1.types import warehouse

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class WarehouseTransport(abc.ABC):
    """Abstract transport class for Warehouse."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "warehouse-visionai.googleapis.com"

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
                 The hostname to connect to (default: 'warehouse-visionai.googleapis.com').
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
            self.create_asset: gapic_v1.method.wrap_method(
                self.create_asset,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=120.0,
                    multiplier=2.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_asset: gapic_v1.method.wrap_method(
                self.update_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_asset: gapic_v1.method.wrap_method(
                self.get_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_assets: gapic_v1.method.wrap_method(
                self.list_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_asset: gapic_v1.method.wrap_method(
                self.delete_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.upload_asset: gapic_v1.method.wrap_method(
                self.upload_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_retrieval_url: gapic_v1.method.wrap_method(
                self.generate_retrieval_url,
                default_timeout=None,
                client_info=client_info,
            ),
            self.analyze_asset: gapic_v1.method.wrap_method(
                self.analyze_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.index_asset: gapic_v1.method.wrap_method(
                self.index_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_index_asset: gapic_v1.method.wrap_method(
                self.remove_index_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.view_indexed_assets: gapic_v1.method.wrap_method(
                self.view_indexed_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_index: gapic_v1.method.wrap_method(
                self.create_index,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_index: gapic_v1.method.wrap_method(
                self.update_index,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_index: gapic_v1.method.wrap_method(
                self.get_index,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_indexes: gapic_v1.method.wrap_method(
                self.list_indexes,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_index: gapic_v1.method.wrap_method(
                self.delete_index,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_corpus: gapic_v1.method.wrap_method(
                self.create_corpus,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=120.0,
                    multiplier=2.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_corpus: gapic_v1.method.wrap_method(
                self.get_corpus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_corpus: gapic_v1.method.wrap_method(
                self.update_corpus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_corpora: gapic_v1.method.wrap_method(
                self.list_corpora,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_corpus: gapic_v1.method.wrap_method(
                self.delete_corpus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.analyze_corpus: gapic_v1.method.wrap_method(
                self.analyze_corpus,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_data_schema: gapic_v1.method.wrap_method(
                self.create_data_schema,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=120.0,
                    multiplier=2.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.update_data_schema: gapic_v1.method.wrap_method(
                self.update_data_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_data_schema: gapic_v1.method.wrap_method(
                self.get_data_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_data_schema: gapic_v1.method.wrap_method(
                self.delete_data_schema,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_data_schemas: gapic_v1.method.wrap_method(
                self.list_data_schemas,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_annotation: gapic_v1.method.wrap_method(
                self.create_annotation,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=120.0,
                    multiplier=2.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.get_annotation: gapic_v1.method.wrap_method(
                self.get_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_annotations: gapic_v1.method.wrap_method(
                self.list_annotations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_annotation: gapic_v1.method.wrap_method(
                self.update_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_annotation: gapic_v1.method.wrap_method(
                self.delete_annotation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.ingest_asset: gapic_v1.method.wrap_method(
                self.ingest_asset,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=120.0,
                    multiplier=2.5,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=120.0,
                ),
                default_timeout=120.0,
                client_info=client_info,
            ),
            self.clip_asset: gapic_v1.method.wrap_method(
                self.clip_asset,
                default_timeout=None,
                client_info=client_info,
            ),
            self.generate_hls_uri: gapic_v1.method.wrap_method(
                self.generate_hls_uri,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_assets: gapic_v1.method.wrap_method(
                self.import_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_search_config: gapic_v1.method.wrap_method(
                self.create_search_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_search_config: gapic_v1.method.wrap_method(
                self.update_search_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_search_config: gapic_v1.method.wrap_method(
                self.get_search_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_search_config: gapic_v1.method.wrap_method(
                self.delete_search_config,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_search_configs: gapic_v1.method.wrap_method(
                self.list_search_configs,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_search_hypernym: gapic_v1.method.wrap_method(
                self.create_search_hypernym,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_search_hypernym: gapic_v1.method.wrap_method(
                self.update_search_hypernym,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_search_hypernym: gapic_v1.method.wrap_method(
                self.get_search_hypernym,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_search_hypernym: gapic_v1.method.wrap_method(
                self.delete_search_hypernym,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_search_hypernyms: gapic_v1.method.wrap_method(
                self.list_search_hypernyms,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_assets: gapic_v1.method.wrap_method(
                self.search_assets,
                default_timeout=None,
                client_info=client_info,
            ),
            self.search_index_endpoint: gapic_v1.method.wrap_method(
                self.search_index_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_index_endpoint: gapic_v1.method.wrap_method(
                self.create_index_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_index_endpoint: gapic_v1.method.wrap_method(
                self.get_index_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_index_endpoints: gapic_v1.method.wrap_method(
                self.list_index_endpoints,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_index_endpoint: gapic_v1.method.wrap_method(
                self.update_index_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_index_endpoint: gapic_v1.method.wrap_method(
                self.delete_index_endpoint,
                default_timeout=None,
                client_info=client_info,
            ),
            self.deploy_index: gapic_v1.method.wrap_method(
                self.deploy_index,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undeploy_index: gapic_v1.method.wrap_method(
                self.undeploy_index,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_collection: gapic_v1.method.wrap_method(
                self.create_collection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_collection: gapic_v1.method.wrap_method(
                self.delete_collection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_collection: gapic_v1.method.wrap_method(
                self.get_collection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_collection: gapic_v1.method.wrap_method(
                self.update_collection,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_collections: gapic_v1.method.wrap_method(
                self.list_collections,
                default_timeout=None,
                client_info=client_info,
            ),
            self.add_collection_item: gapic_v1.method.wrap_method(
                self.add_collection_item,
                default_timeout=None,
                client_info=client_info,
            ),
            self.remove_collection_item: gapic_v1.method.wrap_method(
                self.remove_collection_item,
                default_timeout=None,
                client_info=client_info,
            ),
            self.view_collection_items: gapic_v1.method.wrap_method(
                self.view_collection_items,
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
            self.delete_operation: gapic_v1.method.wrap_method(
                self.delete_operation,
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
    def create_asset(
        self,
    ) -> Callable[
        [warehouse.CreateAssetRequest],
        Union[warehouse.Asset, Awaitable[warehouse.Asset]],
    ]:
        raise NotImplementedError()

    @property
    def update_asset(
        self,
    ) -> Callable[
        [warehouse.UpdateAssetRequest],
        Union[warehouse.Asset, Awaitable[warehouse.Asset]],
    ]:
        raise NotImplementedError()

    @property
    def get_asset(
        self,
    ) -> Callable[
        [warehouse.GetAssetRequest], Union[warehouse.Asset, Awaitable[warehouse.Asset]]
    ]:
        raise NotImplementedError()

    @property
    def list_assets(
        self,
    ) -> Callable[
        [warehouse.ListAssetsRequest],
        Union[warehouse.ListAssetsResponse, Awaitable[warehouse.ListAssetsResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_asset(
        self,
    ) -> Callable[
        [warehouse.DeleteAssetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def upload_asset(
        self,
    ) -> Callable[
        [warehouse.UploadAssetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def generate_retrieval_url(
        self,
    ) -> Callable[
        [warehouse.GenerateRetrievalUrlRequest],
        Union[
            warehouse.GenerateRetrievalUrlResponse,
            Awaitable[warehouse.GenerateRetrievalUrlResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def analyze_asset(
        self,
    ) -> Callable[
        [warehouse.AnalyzeAssetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def index_asset(
        self,
    ) -> Callable[
        [warehouse.IndexAssetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def remove_index_asset(
        self,
    ) -> Callable[
        [warehouse.RemoveIndexAssetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def view_indexed_assets(
        self,
    ) -> Callable[
        [warehouse.ViewIndexedAssetsRequest],
        Union[
            warehouse.ViewIndexedAssetsResponse,
            Awaitable[warehouse.ViewIndexedAssetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_index(
        self,
    ) -> Callable[
        [warehouse.CreateIndexRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_index(
        self,
    ) -> Callable[
        [warehouse.UpdateIndexRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_index(
        self,
    ) -> Callable[
        [warehouse.GetIndexRequest], Union[warehouse.Index, Awaitable[warehouse.Index]]
    ]:
        raise NotImplementedError()

    @property
    def list_indexes(
        self,
    ) -> Callable[
        [warehouse.ListIndexesRequest],
        Union[warehouse.ListIndexesResponse, Awaitable[warehouse.ListIndexesResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_index(
        self,
    ) -> Callable[
        [warehouse.DeleteIndexRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_corpus(
        self,
    ) -> Callable[
        [warehouse.CreateCorpusRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_corpus(
        self,
    ) -> Callable[
        [warehouse.GetCorpusRequest],
        Union[warehouse.Corpus, Awaitable[warehouse.Corpus]],
    ]:
        raise NotImplementedError()

    @property
    def update_corpus(
        self,
    ) -> Callable[
        [warehouse.UpdateCorpusRequest],
        Union[warehouse.Corpus, Awaitable[warehouse.Corpus]],
    ]:
        raise NotImplementedError()

    @property
    def list_corpora(
        self,
    ) -> Callable[
        [warehouse.ListCorporaRequest],
        Union[warehouse.ListCorporaResponse, Awaitable[warehouse.ListCorporaResponse]],
    ]:
        raise NotImplementedError()

    @property
    def delete_corpus(
        self,
    ) -> Callable[
        [warehouse.DeleteCorpusRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def analyze_corpus(
        self,
    ) -> Callable[
        [warehouse.AnalyzeCorpusRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_data_schema(
        self,
    ) -> Callable[
        [warehouse.CreateDataSchemaRequest],
        Union[warehouse.DataSchema, Awaitable[warehouse.DataSchema]],
    ]:
        raise NotImplementedError()

    @property
    def update_data_schema(
        self,
    ) -> Callable[
        [warehouse.UpdateDataSchemaRequest],
        Union[warehouse.DataSchema, Awaitable[warehouse.DataSchema]],
    ]:
        raise NotImplementedError()

    @property
    def get_data_schema(
        self,
    ) -> Callable[
        [warehouse.GetDataSchemaRequest],
        Union[warehouse.DataSchema, Awaitable[warehouse.DataSchema]],
    ]:
        raise NotImplementedError()

    @property
    def delete_data_schema(
        self,
    ) -> Callable[
        [warehouse.DeleteDataSchemaRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_data_schemas(
        self,
    ) -> Callable[
        [warehouse.ListDataSchemasRequest],
        Union[
            warehouse.ListDataSchemasResponse,
            Awaitable[warehouse.ListDataSchemasResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_annotation(
        self,
    ) -> Callable[
        [warehouse.CreateAnnotationRequest],
        Union[warehouse.Annotation, Awaitable[warehouse.Annotation]],
    ]:
        raise NotImplementedError()

    @property
    def get_annotation(
        self,
    ) -> Callable[
        [warehouse.GetAnnotationRequest],
        Union[warehouse.Annotation, Awaitable[warehouse.Annotation]],
    ]:
        raise NotImplementedError()

    @property
    def list_annotations(
        self,
    ) -> Callable[
        [warehouse.ListAnnotationsRequest],
        Union[
            warehouse.ListAnnotationsResponse,
            Awaitable[warehouse.ListAnnotationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_annotation(
        self,
    ) -> Callable[
        [warehouse.UpdateAnnotationRequest],
        Union[warehouse.Annotation, Awaitable[warehouse.Annotation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_annotation(
        self,
    ) -> Callable[
        [warehouse.DeleteAnnotationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def ingest_asset(
        self,
    ) -> Callable[
        [warehouse.IngestAssetRequest],
        Union[warehouse.IngestAssetResponse, Awaitable[warehouse.IngestAssetResponse]],
    ]:
        raise NotImplementedError()

    @property
    def clip_asset(
        self,
    ) -> Callable[
        [warehouse.ClipAssetRequest],
        Union[warehouse.ClipAssetResponse, Awaitable[warehouse.ClipAssetResponse]],
    ]:
        raise NotImplementedError()

    @property
    def generate_hls_uri(
        self,
    ) -> Callable[
        [warehouse.GenerateHlsUriRequest],
        Union[
            warehouse.GenerateHlsUriResponse,
            Awaitable[warehouse.GenerateHlsUriResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def import_assets(
        self,
    ) -> Callable[
        [warehouse.ImportAssetsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_search_config(
        self,
    ) -> Callable[
        [warehouse.CreateSearchConfigRequest],
        Union[warehouse.SearchConfig, Awaitable[warehouse.SearchConfig]],
    ]:
        raise NotImplementedError()

    @property
    def update_search_config(
        self,
    ) -> Callable[
        [warehouse.UpdateSearchConfigRequest],
        Union[warehouse.SearchConfig, Awaitable[warehouse.SearchConfig]],
    ]:
        raise NotImplementedError()

    @property
    def get_search_config(
        self,
    ) -> Callable[
        [warehouse.GetSearchConfigRequest],
        Union[warehouse.SearchConfig, Awaitable[warehouse.SearchConfig]],
    ]:
        raise NotImplementedError()

    @property
    def delete_search_config(
        self,
    ) -> Callable[
        [warehouse.DeleteSearchConfigRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_search_configs(
        self,
    ) -> Callable[
        [warehouse.ListSearchConfigsRequest],
        Union[
            warehouse.ListSearchConfigsResponse,
            Awaitable[warehouse.ListSearchConfigsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_search_hypernym(
        self,
    ) -> Callable[
        [warehouse.CreateSearchHypernymRequest],
        Union[warehouse.SearchHypernym, Awaitable[warehouse.SearchHypernym]],
    ]:
        raise NotImplementedError()

    @property
    def update_search_hypernym(
        self,
    ) -> Callable[
        [warehouse.UpdateSearchHypernymRequest],
        Union[warehouse.SearchHypernym, Awaitable[warehouse.SearchHypernym]],
    ]:
        raise NotImplementedError()

    @property
    def get_search_hypernym(
        self,
    ) -> Callable[
        [warehouse.GetSearchHypernymRequest],
        Union[warehouse.SearchHypernym, Awaitable[warehouse.SearchHypernym]],
    ]:
        raise NotImplementedError()

    @property
    def delete_search_hypernym(
        self,
    ) -> Callable[
        [warehouse.DeleteSearchHypernymRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_search_hypernyms(
        self,
    ) -> Callable[
        [warehouse.ListSearchHypernymsRequest],
        Union[
            warehouse.ListSearchHypernymsResponse,
            Awaitable[warehouse.ListSearchHypernymsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_assets(
        self,
    ) -> Callable[
        [warehouse.SearchAssetsRequest],
        Union[
            warehouse.SearchAssetsResponse, Awaitable[warehouse.SearchAssetsResponse]
        ],
    ]:
        raise NotImplementedError()

    @property
    def search_index_endpoint(
        self,
    ) -> Callable[
        [warehouse.SearchIndexEndpointRequest],
        Union[
            warehouse.SearchIndexEndpointResponse,
            Awaitable[warehouse.SearchIndexEndpointResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_index_endpoint(
        self,
    ) -> Callable[
        [warehouse.CreateIndexEndpointRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_index_endpoint(
        self,
    ) -> Callable[
        [warehouse.GetIndexEndpointRequest],
        Union[warehouse.IndexEndpoint, Awaitable[warehouse.IndexEndpoint]],
    ]:
        raise NotImplementedError()

    @property
    def list_index_endpoints(
        self,
    ) -> Callable[
        [warehouse.ListIndexEndpointsRequest],
        Union[
            warehouse.ListIndexEndpointsResponse,
            Awaitable[warehouse.ListIndexEndpointsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_index_endpoint(
        self,
    ) -> Callable[
        [warehouse.UpdateIndexEndpointRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_index_endpoint(
        self,
    ) -> Callable[
        [warehouse.DeleteIndexEndpointRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def deploy_index(
        self,
    ) -> Callable[
        [warehouse.DeployIndexRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def undeploy_index(
        self,
    ) -> Callable[
        [warehouse.UndeployIndexRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_collection(
        self,
    ) -> Callable[
        [warehouse.CreateCollectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_collection(
        self,
    ) -> Callable[
        [warehouse.DeleteCollectionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_collection(
        self,
    ) -> Callable[
        [warehouse.GetCollectionRequest],
        Union[warehouse.Collection, Awaitable[warehouse.Collection]],
    ]:
        raise NotImplementedError()

    @property
    def update_collection(
        self,
    ) -> Callable[
        [warehouse.UpdateCollectionRequest],
        Union[warehouse.Collection, Awaitable[warehouse.Collection]],
    ]:
        raise NotImplementedError()

    @property
    def list_collections(
        self,
    ) -> Callable[
        [warehouse.ListCollectionsRequest],
        Union[
            warehouse.ListCollectionsResponse,
            Awaitable[warehouse.ListCollectionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def add_collection_item(
        self,
    ) -> Callable[
        [warehouse.AddCollectionItemRequest],
        Union[
            warehouse.AddCollectionItemResponse,
            Awaitable[warehouse.AddCollectionItemResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def remove_collection_item(
        self,
    ) -> Callable[
        [warehouse.RemoveCollectionItemRequest],
        Union[
            warehouse.RemoveCollectionItemResponse,
            Awaitable[warehouse.RemoveCollectionItemResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def view_collection_items(
        self,
    ) -> Callable[
        [warehouse.ViewCollectionItemsRequest],
        Union[
            warehouse.ViewCollectionItemsResponse,
            Awaitable[warehouse.ViewCollectionItemsResponse],
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


__all__ = ("WarehouseTransport",)
