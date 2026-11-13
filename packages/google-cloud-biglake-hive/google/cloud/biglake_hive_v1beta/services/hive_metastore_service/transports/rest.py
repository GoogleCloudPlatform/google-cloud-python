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

from google.cloud.biglake_hive_v1beta._compat import transcode_request
from google.cloud.biglake_hive_v1beta.types import hive_metastore

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseHiveMetastoreServiceRestTransport

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


class HiveMetastoreServiceRestInterceptor:
    """Interceptor for HiveMetastoreService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the HiveMetastoreServiceRestTransport.

    .. code-block:: python
        class MyCustomHiveMetastoreServiceInterceptor(HiveMetastoreServiceRestInterceptor):
            def pre_batch_create_partitions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_create_partitions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_batch_delete_partitions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_batch_update_partitions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_batch_update_partitions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_hive_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_hive_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_hive_database(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_hive_database(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_hive_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_hive_table(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_hive_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_hive_database(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_hive_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_failover_hive_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_failover_hive_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_hive_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_hive_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_hive_database(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_hive_database(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_hive_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_hive_table(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_hive_catalogs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_hive_catalogs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_hive_databases(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_hive_databases(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_hive_tables(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_hive_tables(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_partitions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_partitions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_hive_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_hive_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_hive_database(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_hive_database(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_hive_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_hive_table(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = HiveMetastoreServiceRestTransport(interceptor=MyCustomHiveMetastoreServiceInterceptor())
        client = HiveMetastoreServiceClient(transport=transport)


    """

    def pre_batch_create_partitions(
        self,
        request: hive_metastore.BatchCreatePartitionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.BatchCreatePartitionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_create_partitions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_batch_create_partitions(
        self, response: hive_metastore.BatchCreatePartitionsResponse
    ) -> hive_metastore.BatchCreatePartitionsResponse:
        """Post-rpc interceptor for batch_create_partitions

        DEPRECATED. Please use the `post_batch_create_partitions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_batch_create_partitions` interceptor runs
        before the `post_batch_create_partitions_with_metadata` interceptor.
        """
        return response

    def post_batch_create_partitions_with_metadata(
        self,
        response: hive_metastore.BatchCreatePartitionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.BatchCreatePartitionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_create_partitions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_batch_create_partitions_with_metadata`
        interceptor in new development instead of the `post_batch_create_partitions` interceptor.
        When both interceptors are used, this `post_batch_create_partitions_with_metadata` interceptor runs after the
        `post_batch_create_partitions` interceptor. The (possibly modified) response returned by
        `post_batch_create_partitions` will be passed to
        `post_batch_create_partitions_with_metadata`.
        """
        return response, metadata

    def pre_batch_delete_partitions(
        self,
        request: hive_metastore.BatchDeletePartitionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.BatchDeletePartitionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_delete_partitions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def pre_batch_update_partitions(
        self,
        request: hive_metastore.BatchUpdatePartitionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.BatchUpdatePartitionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for batch_update_partitions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_batch_update_partitions(
        self, response: hive_metastore.BatchUpdatePartitionsResponse
    ) -> hive_metastore.BatchUpdatePartitionsResponse:
        """Post-rpc interceptor for batch_update_partitions

        DEPRECATED. Please use the `post_batch_update_partitions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_batch_update_partitions` interceptor runs
        before the `post_batch_update_partitions_with_metadata` interceptor.
        """
        return response

    def post_batch_update_partitions_with_metadata(
        self,
        response: hive_metastore.BatchUpdatePartitionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.BatchUpdatePartitionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for batch_update_partitions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_batch_update_partitions_with_metadata`
        interceptor in new development instead of the `post_batch_update_partitions` interceptor.
        When both interceptors are used, this `post_batch_update_partitions_with_metadata` interceptor runs after the
        `post_batch_update_partitions` interceptor. The (possibly modified) response returned by
        `post_batch_update_partitions` will be passed to
        `post_batch_update_partitions_with_metadata`.
        """
        return response, metadata

    def pre_create_hive_catalog(
        self,
        request: hive_metastore.CreateHiveCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.CreateHiveCatalogRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_hive_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_create_hive_catalog(
        self, response: hive_metastore.HiveCatalog
    ) -> hive_metastore.HiveCatalog:
        """Post-rpc interceptor for create_hive_catalog

        DEPRECATED. Please use the `post_create_hive_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_create_hive_catalog` interceptor runs
        before the `post_create_hive_catalog_with_metadata` interceptor.
        """
        return response

    def post_create_hive_catalog_with_metadata(
        self,
        response: hive_metastore.HiveCatalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveCatalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_hive_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_create_hive_catalog_with_metadata`
        interceptor in new development instead of the `post_create_hive_catalog` interceptor.
        When both interceptors are used, this `post_create_hive_catalog_with_metadata` interceptor runs after the
        `post_create_hive_catalog` interceptor. The (possibly modified) response returned by
        `post_create_hive_catalog` will be passed to
        `post_create_hive_catalog_with_metadata`.
        """
        return response, metadata

    def pre_create_hive_database(
        self,
        request: hive_metastore.CreateHiveDatabaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.CreateHiveDatabaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_hive_database

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_create_hive_database(
        self, response: hive_metastore.HiveDatabase
    ) -> hive_metastore.HiveDatabase:
        """Post-rpc interceptor for create_hive_database

        DEPRECATED. Please use the `post_create_hive_database_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_create_hive_database` interceptor runs
        before the `post_create_hive_database_with_metadata` interceptor.
        """
        return response

    def post_create_hive_database_with_metadata(
        self,
        response: hive_metastore.HiveDatabase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveDatabase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_hive_database

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_create_hive_database_with_metadata`
        interceptor in new development instead of the `post_create_hive_database` interceptor.
        When both interceptors are used, this `post_create_hive_database_with_metadata` interceptor runs after the
        `post_create_hive_database` interceptor. The (possibly modified) response returned by
        `post_create_hive_database` will be passed to
        `post_create_hive_database_with_metadata`.
        """
        return response, metadata

    def pre_create_hive_table(
        self,
        request: hive_metastore.CreateHiveTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.CreateHiveTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_hive_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_create_hive_table(
        self, response: hive_metastore.HiveTable
    ) -> hive_metastore.HiveTable:
        """Post-rpc interceptor for create_hive_table

        DEPRECATED. Please use the `post_create_hive_table_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_create_hive_table` interceptor runs
        before the `post_create_hive_table_with_metadata` interceptor.
        """
        return response

    def post_create_hive_table_with_metadata(
        self,
        response: hive_metastore.HiveTable,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveTable, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_hive_table

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_create_hive_table_with_metadata`
        interceptor in new development instead of the `post_create_hive_table` interceptor.
        When both interceptors are used, this `post_create_hive_table_with_metadata` interceptor runs after the
        `post_create_hive_table` interceptor. The (possibly modified) response returned by
        `post_create_hive_table` will be passed to
        `post_create_hive_table_with_metadata`.
        """
        return response, metadata

    def pre_delete_hive_catalog(
        self,
        request: hive_metastore.DeleteHiveCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.DeleteHiveCatalogRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_hive_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def pre_delete_hive_database(
        self,
        request: hive_metastore.DeleteHiveDatabaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.DeleteHiveDatabaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_hive_database

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def pre_delete_hive_table(
        self,
        request: hive_metastore.DeleteHiveTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.DeleteHiveTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_hive_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def pre_failover_hive_catalog(
        self,
        request: hive_metastore.FailoverHiveCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.FailoverHiveCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for failover_hive_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_failover_hive_catalog(
        self, response: hive_metastore.FailoverHiveCatalogResponse
    ) -> hive_metastore.FailoverHiveCatalogResponse:
        """Post-rpc interceptor for failover_hive_catalog

        DEPRECATED. Please use the `post_failover_hive_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_failover_hive_catalog` interceptor runs
        before the `post_failover_hive_catalog_with_metadata` interceptor.
        """
        return response

    def post_failover_hive_catalog_with_metadata(
        self,
        response: hive_metastore.FailoverHiveCatalogResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.FailoverHiveCatalogResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for failover_hive_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_failover_hive_catalog_with_metadata`
        interceptor in new development instead of the `post_failover_hive_catalog` interceptor.
        When both interceptors are used, this `post_failover_hive_catalog_with_metadata` interceptor runs after the
        `post_failover_hive_catalog` interceptor. The (possibly modified) response returned by
        `post_failover_hive_catalog` will be passed to
        `post_failover_hive_catalog_with_metadata`.
        """
        return response, metadata

    def pre_get_hive_catalog(
        self,
        request: hive_metastore.GetHiveCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.GetHiveCatalogRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_hive_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_get_hive_catalog(
        self, response: hive_metastore.HiveCatalog
    ) -> hive_metastore.HiveCatalog:
        """Post-rpc interceptor for get_hive_catalog

        DEPRECATED. Please use the `post_get_hive_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_get_hive_catalog` interceptor runs
        before the `post_get_hive_catalog_with_metadata` interceptor.
        """
        return response

    def post_get_hive_catalog_with_metadata(
        self,
        response: hive_metastore.HiveCatalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveCatalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_hive_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_get_hive_catalog_with_metadata`
        interceptor in new development instead of the `post_get_hive_catalog` interceptor.
        When both interceptors are used, this `post_get_hive_catalog_with_metadata` interceptor runs after the
        `post_get_hive_catalog` interceptor. The (possibly modified) response returned by
        `post_get_hive_catalog` will be passed to
        `post_get_hive_catalog_with_metadata`.
        """
        return response, metadata

    def pre_get_hive_database(
        self,
        request: hive_metastore.GetHiveDatabaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.GetHiveDatabaseRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_hive_database

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_get_hive_database(
        self, response: hive_metastore.HiveDatabase
    ) -> hive_metastore.HiveDatabase:
        """Post-rpc interceptor for get_hive_database

        DEPRECATED. Please use the `post_get_hive_database_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_get_hive_database` interceptor runs
        before the `post_get_hive_database_with_metadata` interceptor.
        """
        return response

    def post_get_hive_database_with_metadata(
        self,
        response: hive_metastore.HiveDatabase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveDatabase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_hive_database

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_get_hive_database_with_metadata`
        interceptor in new development instead of the `post_get_hive_database` interceptor.
        When both interceptors are used, this `post_get_hive_database_with_metadata` interceptor runs after the
        `post_get_hive_database` interceptor. The (possibly modified) response returned by
        `post_get_hive_database` will be passed to
        `post_get_hive_database_with_metadata`.
        """
        return response, metadata

    def pre_get_hive_table(
        self,
        request: hive_metastore.GetHiveTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.GetHiveTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_hive_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_get_hive_table(
        self, response: hive_metastore.HiveTable
    ) -> hive_metastore.HiveTable:
        """Post-rpc interceptor for get_hive_table

        DEPRECATED. Please use the `post_get_hive_table_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_get_hive_table` interceptor runs
        before the `post_get_hive_table_with_metadata` interceptor.
        """
        return response

    def post_get_hive_table_with_metadata(
        self,
        response: hive_metastore.HiveTable,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveTable, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_hive_table

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_get_hive_table_with_metadata`
        interceptor in new development instead of the `post_get_hive_table` interceptor.
        When both interceptors are used, this `post_get_hive_table_with_metadata` interceptor runs after the
        `post_get_hive_table` interceptor. The (possibly modified) response returned by
        `post_get_hive_table` will be passed to
        `post_get_hive_table_with_metadata`.
        """
        return response, metadata

    def pre_list_hive_catalogs(
        self,
        request: hive_metastore.ListHiveCatalogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListHiveCatalogsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_hive_catalogs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_list_hive_catalogs(
        self, response: hive_metastore.ListHiveCatalogsResponse
    ) -> hive_metastore.ListHiveCatalogsResponse:
        """Post-rpc interceptor for list_hive_catalogs

        DEPRECATED. Please use the `post_list_hive_catalogs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_list_hive_catalogs` interceptor runs
        before the `post_list_hive_catalogs_with_metadata` interceptor.
        """
        return response

    def post_list_hive_catalogs_with_metadata(
        self,
        response: hive_metastore.ListHiveCatalogsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListHiveCatalogsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_hive_catalogs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_list_hive_catalogs_with_metadata`
        interceptor in new development instead of the `post_list_hive_catalogs` interceptor.
        When both interceptors are used, this `post_list_hive_catalogs_with_metadata` interceptor runs after the
        `post_list_hive_catalogs` interceptor. The (possibly modified) response returned by
        `post_list_hive_catalogs` will be passed to
        `post_list_hive_catalogs_with_metadata`.
        """
        return response, metadata

    def pre_list_hive_databases(
        self,
        request: hive_metastore.ListHiveDatabasesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListHiveDatabasesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_hive_databases

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_list_hive_databases(
        self, response: hive_metastore.ListHiveDatabasesResponse
    ) -> hive_metastore.ListHiveDatabasesResponse:
        """Post-rpc interceptor for list_hive_databases

        DEPRECATED. Please use the `post_list_hive_databases_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_list_hive_databases` interceptor runs
        before the `post_list_hive_databases_with_metadata` interceptor.
        """
        return response

    def post_list_hive_databases_with_metadata(
        self,
        response: hive_metastore.ListHiveDatabasesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListHiveDatabasesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_hive_databases

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_list_hive_databases_with_metadata`
        interceptor in new development instead of the `post_list_hive_databases` interceptor.
        When both interceptors are used, this `post_list_hive_databases_with_metadata` interceptor runs after the
        `post_list_hive_databases` interceptor. The (possibly modified) response returned by
        `post_list_hive_databases` will be passed to
        `post_list_hive_databases_with_metadata`.
        """
        return response, metadata

    def pre_list_hive_tables(
        self,
        request: hive_metastore.ListHiveTablesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListHiveTablesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_hive_tables

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_list_hive_tables(
        self, response: hive_metastore.ListHiveTablesResponse
    ) -> hive_metastore.ListHiveTablesResponse:
        """Post-rpc interceptor for list_hive_tables

        DEPRECATED. Please use the `post_list_hive_tables_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_list_hive_tables` interceptor runs
        before the `post_list_hive_tables_with_metadata` interceptor.
        """
        return response

    def post_list_hive_tables_with_metadata(
        self,
        response: hive_metastore.ListHiveTablesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListHiveTablesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_hive_tables

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_list_hive_tables_with_metadata`
        interceptor in new development instead of the `post_list_hive_tables` interceptor.
        When both interceptors are used, this `post_list_hive_tables_with_metadata` interceptor runs after the
        `post_list_hive_tables` interceptor. The (possibly modified) response returned by
        `post_list_hive_tables` will be passed to
        `post_list_hive_tables_with_metadata`.
        """
        return response, metadata

    def pre_list_partitions(
        self,
        request: hive_metastore.ListPartitionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.ListPartitionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_partitions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_list_partitions(
        self, response: rest_streaming.ResponseIterator
    ) -> rest_streaming.ResponseIterator:
        """Post-rpc interceptor for list_partitions

        DEPRECATED. Please use the `post_list_partitions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_list_partitions` interceptor runs
        before the `post_list_partitions_with_metadata` interceptor.
        """
        return response

    def post_list_partitions_with_metadata(
        self,
        response: rest_streaming.ResponseIterator,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        rest_streaming.ResponseIterator, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_partitions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_list_partitions_with_metadata`
        interceptor in new development instead of the `post_list_partitions` interceptor.
        When both interceptors are used, this `post_list_partitions_with_metadata` interceptor runs after the
        `post_list_partitions` interceptor. The (possibly modified) response returned by
        `post_list_partitions` will be passed to
        `post_list_partitions_with_metadata`.
        """
        return response, metadata

    def pre_update_hive_catalog(
        self,
        request: hive_metastore.UpdateHiveCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.UpdateHiveCatalogRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_hive_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_update_hive_catalog(
        self, response: hive_metastore.HiveCatalog
    ) -> hive_metastore.HiveCatalog:
        """Post-rpc interceptor for update_hive_catalog

        DEPRECATED. Please use the `post_update_hive_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_update_hive_catalog` interceptor runs
        before the `post_update_hive_catalog_with_metadata` interceptor.
        """
        return response

    def post_update_hive_catalog_with_metadata(
        self,
        response: hive_metastore.HiveCatalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveCatalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_hive_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_update_hive_catalog_with_metadata`
        interceptor in new development instead of the `post_update_hive_catalog` interceptor.
        When both interceptors are used, this `post_update_hive_catalog_with_metadata` interceptor runs after the
        `post_update_hive_catalog` interceptor. The (possibly modified) response returned by
        `post_update_hive_catalog` will be passed to
        `post_update_hive_catalog_with_metadata`.
        """
        return response, metadata

    def pre_update_hive_database(
        self,
        request: hive_metastore.UpdateHiveDatabaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.UpdateHiveDatabaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_hive_database

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_update_hive_database(
        self, response: hive_metastore.HiveDatabase
    ) -> hive_metastore.HiveDatabase:
        """Post-rpc interceptor for update_hive_database

        DEPRECATED. Please use the `post_update_hive_database_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_update_hive_database` interceptor runs
        before the `post_update_hive_database_with_metadata` interceptor.
        """
        return response

    def post_update_hive_database_with_metadata(
        self,
        response: hive_metastore.HiveDatabase,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveDatabase, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_hive_database

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_update_hive_database_with_metadata`
        interceptor in new development instead of the `post_update_hive_database` interceptor.
        When both interceptors are used, this `post_update_hive_database_with_metadata` interceptor runs after the
        `post_update_hive_database` interceptor. The (possibly modified) response returned by
        `post_update_hive_database` will be passed to
        `post_update_hive_database_with_metadata`.
        """
        return response, metadata

    def pre_update_hive_table(
        self,
        request: hive_metastore.UpdateHiveTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        hive_metastore.UpdateHiveTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_hive_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the HiveMetastoreService server.
        """
        return request, metadata

    def post_update_hive_table(
        self, response: hive_metastore.HiveTable
    ) -> hive_metastore.HiveTable:
        """Post-rpc interceptor for update_hive_table

        DEPRECATED. Please use the `post_update_hive_table_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the HiveMetastoreService server but before
        it is returned to user code. This `post_update_hive_table` interceptor runs
        before the `post_update_hive_table_with_metadata` interceptor.
        """
        return response

    def post_update_hive_table_with_metadata(
        self,
        response: hive_metastore.HiveTable,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[hive_metastore.HiveTable, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_hive_table

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the HiveMetastoreService server but before it is returned to user code.

        We recommend only using this `post_update_hive_table_with_metadata`
        interceptor in new development instead of the `post_update_hive_table` interceptor.
        When both interceptors are used, this `post_update_hive_table_with_metadata` interceptor runs after the
        `post_update_hive_table` interceptor. The (possibly modified) response returned by
        `post_update_hive_table` will be passed to
        `post_update_hive_table_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class HiveMetastoreServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: HiveMetastoreServiceRestInterceptor


class HiveMetastoreServiceRestTransport(_BaseHiveMetastoreServiceRestTransport):
    """REST backend synchronous transport for HiveMetastoreService.

    Hive Metastore Service is a biglake service that allows users to
    manage their external Hive catalogs. Full API compatibility with OSS
    Hive Metastore APIs is not supported. The methods match the Hive
    Metastore API spec mostly except for a few exceptions. These include
    listing resources with pattern, environment context which are
    combined in a single List API, return of ListResponse object instead
    of a list of resources, transactions, locks, etc.

    The BigLake Hive Metastore API defines the following resources:

    - A collection of Google Cloud projects: ``/projects/*``
    - Each project has a collection of catalogs: ``/catalogs/*``
    - Each catalog has a collection of databases: ``/databases/*``
    - Each database has a collection of tables: ``/tables/*``

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "biglake.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[HiveMetastoreServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'biglake.googleapis.com').
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
            interceptor (Optional[HiveMetastoreServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or HiveMetastoreServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BatchCreatePartitions(
        _BaseHiveMetastoreServiceRestTransport._BaseBatchCreatePartitions,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.BatchCreatePartitions")

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
            request: hive_metastore.BatchCreatePartitionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.BatchCreatePartitionsResponse:
            r"""Call the batch create partitions method over HTTP.

            Args:
                request (~.hive_metastore.BatchCreatePartitionsRequest):
                    The request object. Request message for the
                BatchCreatePartitions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.BatchCreatePartitionsResponse:
                    Response message for
                BatchCreatePartitions.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseBatchCreatePartitions._get_http_options()
            request, metadata = self._interceptor.pre_batch_create_partitions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseBatchCreatePartitions,
                    "_BaseBatchCreatePartitions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.BatchCreatePartitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "BatchCreatePartitions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._BatchCreatePartitions._get_response(
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
            resp = hive_metastore.BatchCreatePartitionsResponse()
            pb_resp = hive_metastore.BatchCreatePartitionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_create_partitions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_create_partitions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        hive_metastore.BatchCreatePartitionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.batch_create_partitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "BatchCreatePartitions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BatchDeletePartitions(
        _BaseHiveMetastoreServiceRestTransport._BaseBatchDeletePartitions,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.BatchDeletePartitions")

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
            request: hive_metastore.BatchDeletePartitionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the batch delete partitions method over HTTP.

            Args:
                request (~.hive_metastore.BatchDeletePartitionsRequest):
                    The request object. Request message for
                BatchDeletePartitions. The Partition is
                uniquely identified by values, which is
                an ordered list. Hence, there is no
                separate name or partition id field.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseBatchDeletePartitions._get_http_options()
            request, metadata = self._interceptor.pre_batch_delete_partitions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseBatchDeletePartitions,
                    "_BaseBatchDeletePartitions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.BatchDeletePartitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "BatchDeletePartitions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._BatchDeletePartitions._get_response(
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

    class _BatchUpdatePartitions(
        _BaseHiveMetastoreServiceRestTransport._BaseBatchUpdatePartitions,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.BatchUpdatePartitions")

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
            request: hive_metastore.BatchUpdatePartitionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.BatchUpdatePartitionsResponse:
            r"""Call the batch update partitions method over HTTP.

            Args:
                request (~.hive_metastore.BatchUpdatePartitionsRequest):
                    The request object. Request message for
                BatchUpdatePartitions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.BatchUpdatePartitionsResponse:
                    Response message for
                BatchUpdatePartitions.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseBatchUpdatePartitions._get_http_options()
            request, metadata = self._interceptor.pre_batch_update_partitions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseBatchUpdatePartitions,
                    "_BaseBatchUpdatePartitions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.BatchUpdatePartitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "BatchUpdatePartitions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._BatchUpdatePartitions._get_response(
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
            resp = hive_metastore.BatchUpdatePartitionsResponse()
            pb_resp = hive_metastore.BatchUpdatePartitionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_batch_update_partitions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_batch_update_partitions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        hive_metastore.BatchUpdatePartitionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.batch_update_partitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "BatchUpdatePartitions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHiveCatalog(
        _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveCatalog,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.CreateHiveCatalog")

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
            request: hive_metastore.CreateHiveCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveCatalog:
            r"""Call the create hive catalog method over HTTP.

            Args:
                request (~.hive_metastore.CreateHiveCatalogRequest):
                    The request object. Request message for the
                CreateHiveCatalog method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveCatalog:
                    The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveCatalog._get_http_options()
            request, metadata = self._interceptor.pre_create_hive_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveCatalog,
                    "_BaseCreateHiveCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.CreateHiveCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "CreateHiveCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._CreateHiveCatalog._get_response(
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
            resp = hive_metastore.HiveCatalog()
            pb_resp = hive_metastore.HiveCatalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_hive_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_hive_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveCatalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.create_hive_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "CreateHiveCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHiveDatabase(
        _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveDatabase,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.CreateHiveDatabase")

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
            request: hive_metastore.CreateHiveDatabaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveDatabase:
            r"""Call the create hive database method over HTTP.

            Args:
                request (~.hive_metastore.CreateHiveDatabaseRequest):
                    The request object. Request message for the
                CreateHiveDatabase method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveDatabase:
                    Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveDatabase._get_http_options()
            request, metadata = self._interceptor.pre_create_hive_database(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveDatabase,
                    "_BaseCreateHiveDatabase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.CreateHiveDatabase",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "CreateHiveDatabase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._CreateHiveDatabase._get_response(
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
            resp = hive_metastore.HiveDatabase()
            pb_resp = hive_metastore.HiveDatabase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_hive_database(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_hive_database_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveDatabase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.create_hive_database",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "CreateHiveDatabase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateHiveTable(
        _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveTable,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.CreateHiveTable")

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
            request: hive_metastore.CreateHiveTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveTable:
            r"""Call the create hive table method over HTTP.

            Args:
                request (~.hive_metastore.CreateHiveTableRequest):
                    The request object. Request message for the
                CreateHiveTable method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveTable:
                    Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveTable._get_http_options()
            request, metadata = self._interceptor.pre_create_hive_table(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseCreateHiveTable,
                    "_BaseCreateHiveTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.CreateHiveTable",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "CreateHiveTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._CreateHiveTable._get_response(
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
            resp = hive_metastore.HiveTable()
            pb_resp = hive_metastore.HiveTable.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_hive_table(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_hive_table_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveTable.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.create_hive_table",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "CreateHiveTable",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteHiveCatalog(
        _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveCatalog,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.DeleteHiveCatalog")

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
            request: hive_metastore.DeleteHiveCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete hive catalog method over HTTP.

            Args:
                request (~.hive_metastore.DeleteHiveCatalogRequest):
                    The request object. Request message for the
                DeleteHiveCatalog method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveCatalog._get_http_options()
            request, metadata = self._interceptor.pre_delete_hive_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveCatalog,
                    "_BaseDeleteHiveCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.DeleteHiveCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "DeleteHiveCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._DeleteHiveCatalog._get_response(
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

    class _DeleteHiveDatabase(
        _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveDatabase,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.DeleteHiveDatabase")

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
            request: hive_metastore.DeleteHiveDatabaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete hive database method over HTTP.

            Args:
                request (~.hive_metastore.DeleteHiveDatabaseRequest):
                    The request object. Request message for the
                DeleteHiveDatabase method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveDatabase._get_http_options()
            request, metadata = self._interceptor.pre_delete_hive_database(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveDatabase,
                    "_BaseDeleteHiveDatabase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.DeleteHiveDatabase",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "DeleteHiveDatabase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._DeleteHiveDatabase._get_response(
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

    class _DeleteHiveTable(
        _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveTable,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.DeleteHiveTable")

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
            request: hive_metastore.DeleteHiveTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete hive table method over HTTP.

            Args:
                request (~.hive_metastore.DeleteHiveTableRequest):
                    The request object. Request message for the
                DeleteHiveTable method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveTable._get_http_options()
            request, metadata = self._interceptor.pre_delete_hive_table(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseDeleteHiveTable,
                    "_BaseDeleteHiveTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.DeleteHiveTable",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "DeleteHiveTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._DeleteHiveTable._get_response(
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

    class _FailoverHiveCatalog(
        _BaseHiveMetastoreServiceRestTransport._BaseFailoverHiveCatalog,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.FailoverHiveCatalog")

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
            request: hive_metastore.FailoverHiveCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.FailoverHiveCatalogResponse:
            r"""Call the failover hive catalog method over HTTP.

            Args:
                request (~.hive_metastore.FailoverHiveCatalogRequest):
                    The request object. Request message for
                FailoverHiveCatalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.FailoverHiveCatalogResponse:
                    Response message for
                FailoverHiveCatalog.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseFailoverHiveCatalog._get_http_options()
            request, metadata = self._interceptor.pre_failover_hive_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseFailoverHiveCatalog,
                    "_BaseFailoverHiveCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.FailoverHiveCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "FailoverHiveCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._FailoverHiveCatalog._get_response(
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
            resp = hive_metastore.FailoverHiveCatalogResponse()
            pb_resp = hive_metastore.FailoverHiveCatalogResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_failover_hive_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_failover_hive_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        hive_metastore.FailoverHiveCatalogResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.failover_hive_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "FailoverHiveCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHiveCatalog(
        _BaseHiveMetastoreServiceRestTransport._BaseGetHiveCatalog,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.GetHiveCatalog")

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
            request: hive_metastore.GetHiveCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveCatalog:
            r"""Call the get hive catalog method over HTTP.

            Args:
                request (~.hive_metastore.GetHiveCatalogRequest):
                    The request object. Request message for the
                GetHiveCatalog method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveCatalog:
                    The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseGetHiveCatalog._get_http_options()
            request, metadata = self._interceptor.pre_get_hive_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseGetHiveCatalog,
                    "_BaseGetHiveCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.GetHiveCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "GetHiveCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._GetHiveCatalog._get_response(
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
            resp = hive_metastore.HiveCatalog()
            pb_resp = hive_metastore.HiveCatalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_hive_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_hive_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveCatalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.get_hive_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "GetHiveCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHiveDatabase(
        _BaseHiveMetastoreServiceRestTransport._BaseGetHiveDatabase,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.GetHiveDatabase")

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
            request: hive_metastore.GetHiveDatabaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveDatabase:
            r"""Call the get hive database method over HTTP.

            Args:
                request (~.hive_metastore.GetHiveDatabaseRequest):
                    The request object. Request message for the
                GetHiveDatabase method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveDatabase:
                    Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseGetHiveDatabase._get_http_options()
            request, metadata = self._interceptor.pre_get_hive_database(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseGetHiveDatabase,
                    "_BaseGetHiveDatabase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.GetHiveDatabase",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "GetHiveDatabase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._GetHiveDatabase._get_response(
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
            resp = hive_metastore.HiveDatabase()
            pb_resp = hive_metastore.HiveDatabase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_hive_database(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_hive_database_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveDatabase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.get_hive_database",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "GetHiveDatabase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetHiveTable(
        _BaseHiveMetastoreServiceRestTransport._BaseGetHiveTable,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.GetHiveTable")

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
            request: hive_metastore.GetHiveTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveTable:
            r"""Call the get hive table method over HTTP.

            Args:
                request (~.hive_metastore.GetHiveTableRequest):
                    The request object. Request message for the GetHiveTable
                method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveTable:
                    Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseGetHiveTable._get_http_options()
            request, metadata = self._interceptor.pre_get_hive_table(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseGetHiveTable,
                    "_BaseGetHiveTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.GetHiveTable",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "GetHiveTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._GetHiveTable._get_response(
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
            resp = hive_metastore.HiveTable()
            pb_resp = hive_metastore.HiveTable.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_hive_table(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_hive_table_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveTable.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.get_hive_table",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "GetHiveTable",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHiveCatalogs(
        _BaseHiveMetastoreServiceRestTransport._BaseListHiveCatalogs,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.ListHiveCatalogs")

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
            request: hive_metastore.ListHiveCatalogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.ListHiveCatalogsResponse:
            r"""Call the list hive catalogs method over HTTP.

            Args:
                request (~.hive_metastore.ListHiveCatalogsRequest):
                    The request object. Request message for the
                ListHiveCatalogs method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.ListHiveCatalogsResponse:
                    Response message for the
                ListHiveCatalogs method.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseListHiveCatalogs._get_http_options()
            request, metadata = self._interceptor.pre_list_hive_catalogs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseListHiveCatalogs,
                    "_BaseListHiveCatalogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.ListHiveCatalogs",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListHiveCatalogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._ListHiveCatalogs._get_response(
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
            resp = hive_metastore.ListHiveCatalogsResponse()
            pb_resp = hive_metastore.ListHiveCatalogsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_hive_catalogs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_hive_catalogs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.ListHiveCatalogsResponse.to_json(
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
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.list_hive_catalogs",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListHiveCatalogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHiveDatabases(
        _BaseHiveMetastoreServiceRestTransport._BaseListHiveDatabases,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.ListHiveDatabases")

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
            request: hive_metastore.ListHiveDatabasesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.ListHiveDatabasesResponse:
            r"""Call the list hive databases method over HTTP.

            Args:
                request (~.hive_metastore.ListHiveDatabasesRequest):
                    The request object. Request message for the
                ListHiveDatabases method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.ListHiveDatabasesResponse:
                    Response message for the
                ListHiveDatabases method.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseListHiveDatabases._get_http_options()
            request, metadata = self._interceptor.pre_list_hive_databases(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseListHiveDatabases,
                    "_BaseListHiveDatabases__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.ListHiveDatabases",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListHiveDatabases",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._ListHiveDatabases._get_response(
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
            resp = hive_metastore.ListHiveDatabasesResponse()
            pb_resp = hive_metastore.ListHiveDatabasesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_hive_databases(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_hive_databases_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.ListHiveDatabasesResponse.to_json(
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
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.list_hive_databases",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListHiveDatabases",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListHiveTables(
        _BaseHiveMetastoreServiceRestTransport._BaseListHiveTables,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.ListHiveTables")

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
            request: hive_metastore.ListHiveTablesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.ListHiveTablesResponse:
            r"""Call the list hive tables method over HTTP.

            Args:
                request (~.hive_metastore.ListHiveTablesRequest):
                    The request object. Request message for the
                ListHiveTables method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.ListHiveTablesResponse:
                    Response message for the
                ListHiveTables method.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseListHiveTables._get_http_options()
            request, metadata = self._interceptor.pre_list_hive_tables(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseListHiveTables,
                    "_BaseListHiveTables__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.ListHiveTables",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListHiveTables",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._ListHiveTables._get_response(
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
            resp = hive_metastore.ListHiveTablesResponse()
            pb_resp = hive_metastore.ListHiveTablesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_hive_tables(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_hive_tables_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.ListHiveTablesResponse.to_json(
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
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.list_hive_tables",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListHiveTables",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPartitions(
        _BaseHiveMetastoreServiceRestTransport._BaseListPartitions,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.ListPartitions")

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
                stream=True,
            )
            return response

        def __call__(
            self,
            request: hive_metastore.ListPartitionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> rest_streaming.ResponseIterator:
            r"""Call the list partitions method over HTTP.

            Args:
                request (~.hive_metastore.ListPartitionsRequest):
                    The request object. Request message for ListPartitions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.ListPartitionsResponse:
                    Response message for ListPartitions.
            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseListPartitions._get_http_options()
            request, metadata = self._interceptor.pre_list_partitions(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseListPartitions,
                    "_BaseListPartitions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.ListPartitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListPartitions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._ListPartitions._get_response(
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
            resp = rest_streaming.ResponseIterator(
                response, hive_metastore.ListPartitionsResponse
            )

            resp = self._interceptor.post_list_partitions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_partitions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                http_response = {
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.list_partitions",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "ListPartitions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHiveCatalog(
        _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveCatalog,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.UpdateHiveCatalog")

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
            request: hive_metastore.UpdateHiveCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveCatalog:
            r"""Call the update hive catalog method over HTTP.

            Args:
                request (~.hive_metastore.UpdateHiveCatalogRequest):
                    The request object. Request message for the
                UpdateHiveCatalog method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveCatalog:
                    The HiveCatalog contains spark/hive
                databases and tables in the BigLake
                Metastore. While creating resources
                under a catalog, ideally ensure that the
                storage bucket location, spark / hive
                engine location or any other compute
                location  match. Catalog can be viewed
                as the destination for migrating an
                on-prem Hive metastore to GCP.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveCatalog._get_http_options()
            request, metadata = self._interceptor.pre_update_hive_catalog(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveCatalog,
                    "_BaseUpdateHiveCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.UpdateHiveCatalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "UpdateHiveCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._UpdateHiveCatalog._get_response(
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
            resp = hive_metastore.HiveCatalog()
            pb_resp = hive_metastore.HiveCatalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_hive_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_hive_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveCatalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.update_hive_catalog",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "UpdateHiveCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHiveDatabase(
        _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveDatabase,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.UpdateHiveDatabase")

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
            request: hive_metastore.UpdateHiveDatabaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveDatabase:
            r"""Call the update hive database method over HTTP.

            Args:
                request (~.hive_metastore.UpdateHiveDatabaseRequest):
                    The request object. Request message for the
                UpdateHiveDatabase method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveDatabase:
                    Stores the hive database information.
                It includes the database name,
                description, location and properties
                associated with the database.

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveDatabase._get_http_options()
            request, metadata = self._interceptor.pre_update_hive_database(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveDatabase,
                    "_BaseUpdateHiveDatabase__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.UpdateHiveDatabase",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "UpdateHiveDatabase",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                HiveMetastoreServiceRestTransport._UpdateHiveDatabase._get_response(
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
            resp = hive_metastore.HiveDatabase()
            pb_resp = hive_metastore.HiveDatabase.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_hive_database(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_hive_database_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveDatabase.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.update_hive_database",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "UpdateHiveDatabase",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateHiveTable(
        _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveTable,
        HiveMetastoreServiceRestStub,
    ):
        def __hash__(self):
            return hash("HiveMetastoreServiceRestTransport.UpdateHiveTable")

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
            request: hive_metastore.UpdateHiveTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> hive_metastore.HiveTable:
            r"""Call the update hive table method over HTTP.

            Args:
                request (~.hive_metastore.UpdateHiveTableRequest):
                    The request object. Request message for the
                UpdateHiveTable method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.hive_metastore.HiveTable:
                    Stores the hive table information. It
                includes the table name, schema (column
                names and types), data location, storage
                format, serde info, etc. This message
                closely matches the Table object in the
                IMetastoreClient

            """

            http_options = _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveTable._get_http_options()
            request, metadata = self._interceptor.pre_update_hive_table(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseHiveMetastoreServiceRestTransport._BaseUpdateHiveTable,
                    "_BaseUpdateHiveTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.UpdateHiveTable",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "UpdateHiveTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = HiveMetastoreServiceRestTransport._UpdateHiveTable._get_response(
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
            resp = hive_metastore.HiveTable()
            pb_resp = hive_metastore.HiveTable.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_hive_table(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_hive_table_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = hive_metastore.HiveTable.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.biglake.hive_v1beta.HiveMetastoreServiceClient.update_hive_table",
                    extra={
                        "serviceName": "google.cloud.biglake.hive.v1beta.HiveMetastoreService",
                        "rpcName": "UpdateHiveTable",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def batch_create_partitions(
        self,
    ) -> Callable[
        [hive_metastore.BatchCreatePartitionsRequest],
        hive_metastore.BatchCreatePartitionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchCreatePartitions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_delete_partitions(
        self,
    ) -> Callable[[hive_metastore.BatchDeletePartitionsRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchDeletePartitions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def batch_update_partitions(
        self,
    ) -> Callable[
        [hive_metastore.BatchUpdatePartitionsRequest],
        hive_metastore.BatchUpdatePartitionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BatchUpdatePartitions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.CreateHiveCatalogRequest], hive_metastore.HiveCatalog
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHiveCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_hive_database(
        self,
    ) -> Callable[
        [hive_metastore.CreateHiveDatabaseRequest], hive_metastore.HiveDatabase
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHiveDatabase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_hive_table(
        self,
    ) -> Callable[[hive_metastore.CreateHiveTableRequest], hive_metastore.HiveTable]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateHiveTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_hive_catalog(
        self,
    ) -> Callable[[hive_metastore.DeleteHiveCatalogRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteHiveCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_hive_database(
        self,
    ) -> Callable[[hive_metastore.DeleteHiveDatabaseRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteHiveDatabase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_hive_table(
        self,
    ) -> Callable[[hive_metastore.DeleteHiveTableRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteHiveTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def failover_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.FailoverHiveCatalogRequest],
        hive_metastore.FailoverHiveCatalogResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FailoverHiveCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_hive_catalog(
        self,
    ) -> Callable[[hive_metastore.GetHiveCatalogRequest], hive_metastore.HiveCatalog]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHiveCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_hive_database(
        self,
    ) -> Callable[[hive_metastore.GetHiveDatabaseRequest], hive_metastore.HiveDatabase]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHiveDatabase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_hive_table(
        self,
    ) -> Callable[[hive_metastore.GetHiveTableRequest], hive_metastore.HiveTable]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetHiveTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_hive_catalogs(
        self,
    ) -> Callable[
        [hive_metastore.ListHiveCatalogsRequest],
        hive_metastore.ListHiveCatalogsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHiveCatalogs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_hive_databases(
        self,
    ) -> Callable[
        [hive_metastore.ListHiveDatabasesRequest],
        hive_metastore.ListHiveDatabasesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHiveDatabases(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_hive_tables(
        self,
    ) -> Callable[
        [hive_metastore.ListHiveTablesRequest], hive_metastore.ListHiveTablesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListHiveTables(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_partitions(
        self,
    ) -> Callable[
        [hive_metastore.ListPartitionsRequest], hive_metastore.ListPartitionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPartitions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_hive_catalog(
        self,
    ) -> Callable[
        [hive_metastore.UpdateHiveCatalogRequest], hive_metastore.HiveCatalog
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHiveCatalog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_hive_database(
        self,
    ) -> Callable[
        [hive_metastore.UpdateHiveDatabaseRequest], hive_metastore.HiveDatabase
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHiveDatabase(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_hive_table(
        self,
    ) -> Callable[[hive_metastore.UpdateHiveTableRequest], hive_metastore.HiveTable]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateHiveTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("HiveMetastoreServiceRestTransport",)
