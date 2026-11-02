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
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.chronicle_v1._compat import transcode_request
from google.cloud.chronicle_v1.types import data_table
from google.cloud.chronicle_v1.types import data_table as gcc_data_table

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDataTableServiceRestTransport

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


class DataTableServiceRestInterceptor:
    """Interceptor for DataTableService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DataTableServiceRestTransport.

    .. code-block:: python
        class MyCustomDataTableServiceInterceptor(DataTableServiceRestInterceptor):
            def pre_bulk_create_data_table_rows(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_create_data_table_rows(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_get_data_table_rows(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_get_data_table_rows(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_replace_data_table_rows(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_replace_data_table_rows(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_update_data_table_rows(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_update_data_table_rows(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_table(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_data_table_row(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_data_table_row(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_data_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_data_table_row(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_data_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_table(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_table_operation_errors(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_table_operation_errors(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_data_table_row(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_data_table_row(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_table_rows(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_table_rows(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_data_tables(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_data_tables(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_table(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_table(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_data_table_row(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_data_table_row(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DataTableServiceRestTransport(interceptor=MyCustomDataTableServiceInterceptor())
        client = DataTableServiceClient(transport=transport)


    """

    def pre_bulk_create_data_table_rows(
        self,
        request: data_table.BulkCreateDataTableRowsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkCreateDataTableRowsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_create_data_table_rows

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_bulk_create_data_table_rows(
        self, response: data_table.BulkCreateDataTableRowsResponse
    ) -> data_table.BulkCreateDataTableRowsResponse:
        """Post-rpc interceptor for bulk_create_data_table_rows

        DEPRECATED. Please use the `post_bulk_create_data_table_rows_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_bulk_create_data_table_rows` interceptor runs
        before the `post_bulk_create_data_table_rows_with_metadata` interceptor.
        """
        return response

    def post_bulk_create_data_table_rows_with_metadata(
        self,
        response: data_table.BulkCreateDataTableRowsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkCreateDataTableRowsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for bulk_create_data_table_rows

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_bulk_create_data_table_rows_with_metadata`
        interceptor in new development instead of the `post_bulk_create_data_table_rows` interceptor.
        When both interceptors are used, this `post_bulk_create_data_table_rows_with_metadata` interceptor runs after the
        `post_bulk_create_data_table_rows` interceptor. The (possibly modified) response returned by
        `post_bulk_create_data_table_rows` will be passed to
        `post_bulk_create_data_table_rows_with_metadata`.
        """
        return response, metadata

    def pre_bulk_get_data_table_rows(
        self,
        request: data_table.BulkGetDataTableRowsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkGetDataTableRowsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for bulk_get_data_table_rows

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_bulk_get_data_table_rows(
        self, response: data_table.BulkGetDataTableRowsResponse
    ) -> data_table.BulkGetDataTableRowsResponse:
        """Post-rpc interceptor for bulk_get_data_table_rows

        DEPRECATED. Please use the `post_bulk_get_data_table_rows_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_bulk_get_data_table_rows` interceptor runs
        before the `post_bulk_get_data_table_rows_with_metadata` interceptor.
        """
        return response

    def post_bulk_get_data_table_rows_with_metadata(
        self,
        response: data_table.BulkGetDataTableRowsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkGetDataTableRowsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for bulk_get_data_table_rows

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_bulk_get_data_table_rows_with_metadata`
        interceptor in new development instead of the `post_bulk_get_data_table_rows` interceptor.
        When both interceptors are used, this `post_bulk_get_data_table_rows_with_metadata` interceptor runs after the
        `post_bulk_get_data_table_rows` interceptor. The (possibly modified) response returned by
        `post_bulk_get_data_table_rows` will be passed to
        `post_bulk_get_data_table_rows_with_metadata`.
        """
        return response, metadata

    def pre_bulk_replace_data_table_rows(
        self,
        request: data_table.BulkReplaceDataTableRowsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkReplaceDataTableRowsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_replace_data_table_rows

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_bulk_replace_data_table_rows(
        self, response: data_table.BulkReplaceDataTableRowsResponse
    ) -> data_table.BulkReplaceDataTableRowsResponse:
        """Post-rpc interceptor for bulk_replace_data_table_rows

        DEPRECATED. Please use the `post_bulk_replace_data_table_rows_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_bulk_replace_data_table_rows` interceptor runs
        before the `post_bulk_replace_data_table_rows_with_metadata` interceptor.
        """
        return response

    def post_bulk_replace_data_table_rows_with_metadata(
        self,
        response: data_table.BulkReplaceDataTableRowsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkReplaceDataTableRowsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for bulk_replace_data_table_rows

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_bulk_replace_data_table_rows_with_metadata`
        interceptor in new development instead of the `post_bulk_replace_data_table_rows` interceptor.
        When both interceptors are used, this `post_bulk_replace_data_table_rows_with_metadata` interceptor runs after the
        `post_bulk_replace_data_table_rows` interceptor. The (possibly modified) response returned by
        `post_bulk_replace_data_table_rows` will be passed to
        `post_bulk_replace_data_table_rows_with_metadata`.
        """
        return response, metadata

    def pre_bulk_update_data_table_rows(
        self,
        request: data_table.BulkUpdateDataTableRowsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkUpdateDataTableRowsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_update_data_table_rows

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_bulk_update_data_table_rows(
        self, response: data_table.BulkUpdateDataTableRowsResponse
    ) -> data_table.BulkUpdateDataTableRowsResponse:
        """Post-rpc interceptor for bulk_update_data_table_rows

        DEPRECATED. Please use the `post_bulk_update_data_table_rows_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_bulk_update_data_table_rows` interceptor runs
        before the `post_bulk_update_data_table_rows_with_metadata` interceptor.
        """
        return response

    def post_bulk_update_data_table_rows_with_metadata(
        self,
        response: data_table.BulkUpdateDataTableRowsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.BulkUpdateDataTableRowsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for bulk_update_data_table_rows

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_bulk_update_data_table_rows_with_metadata`
        interceptor in new development instead of the `post_bulk_update_data_table_rows` interceptor.
        When both interceptors are used, this `post_bulk_update_data_table_rows_with_metadata` interceptor runs after the
        `post_bulk_update_data_table_rows` interceptor. The (possibly modified) response returned by
        `post_bulk_update_data_table_rows` will be passed to
        `post_bulk_update_data_table_rows_with_metadata`.
        """
        return response, metadata

    def pre_create_data_table(
        self,
        request: gcc_data_table.CreateDataTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_data_table.CreateDataTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_data_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_create_data_table(
        self, response: gcc_data_table.DataTable
    ) -> gcc_data_table.DataTable:
        """Post-rpc interceptor for create_data_table

        DEPRECATED. Please use the `post_create_data_table_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_create_data_table` interceptor runs
        before the `post_create_data_table_with_metadata` interceptor.
        """
        return response

    def post_create_data_table_with_metadata(
        self,
        response: gcc_data_table.DataTable,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_data_table.DataTable, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_table

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_create_data_table_with_metadata`
        interceptor in new development instead of the `post_create_data_table` interceptor.
        When both interceptors are used, this `post_create_data_table_with_metadata` interceptor runs after the
        `post_create_data_table` interceptor. The (possibly modified) response returned by
        `post_create_data_table` will be passed to
        `post_create_data_table_with_metadata`.
        """
        return response, metadata

    def pre_create_data_table_row(
        self,
        request: data_table.CreateDataTableRowRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.CreateDataTableRowRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_data_table_row

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_create_data_table_row(
        self, response: data_table.DataTableRow
    ) -> data_table.DataTableRow:
        """Post-rpc interceptor for create_data_table_row

        DEPRECATED. Please use the `post_create_data_table_row_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_create_data_table_row` interceptor runs
        before the `post_create_data_table_row_with_metadata` interceptor.
        """
        return response

    def post_create_data_table_row_with_metadata(
        self,
        response: data_table.DataTableRow,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_table.DataTableRow, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_data_table_row

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_create_data_table_row_with_metadata`
        interceptor in new development instead of the `post_create_data_table_row` interceptor.
        When both interceptors are used, this `post_create_data_table_row_with_metadata` interceptor runs after the
        `post_create_data_table_row` interceptor. The (possibly modified) response returned by
        `post_create_data_table_row` will be passed to
        `post_create_data_table_row_with_metadata`.
        """
        return response, metadata

    def pre_delete_data_table(
        self,
        request: data_table.DeleteDataTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.DeleteDataTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_data_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def pre_delete_data_table_row(
        self,
        request: data_table.DeleteDataTableRowRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.DeleteDataTableRowRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_data_table_row

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def pre_get_data_table(
        self,
        request: data_table.GetDataTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_table.GetDataTableRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_data_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_get_data_table(
        self, response: data_table.DataTable
    ) -> data_table.DataTable:
        """Post-rpc interceptor for get_data_table

        DEPRECATED. Please use the `post_get_data_table_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_get_data_table` interceptor runs
        before the `post_get_data_table_with_metadata` interceptor.
        """
        return response

    def post_get_data_table_with_metadata(
        self,
        response: data_table.DataTable,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_table.DataTable, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_table

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_get_data_table_with_metadata`
        interceptor in new development instead of the `post_get_data_table` interceptor.
        When both interceptors are used, this `post_get_data_table_with_metadata` interceptor runs after the
        `post_get_data_table` interceptor. The (possibly modified) response returned by
        `post_get_data_table` will be passed to
        `post_get_data_table_with_metadata`.
        """
        return response, metadata

    def pre_get_data_table_operation_errors(
        self,
        request: data_table.GetDataTableOperationErrorsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.GetDataTableOperationErrorsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_data_table_operation_errors

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_get_data_table_operation_errors(
        self, response: data_table.DataTableOperationErrors
    ) -> data_table.DataTableOperationErrors:
        """Post-rpc interceptor for get_data_table_operation_errors

        DEPRECATED. Please use the `post_get_data_table_operation_errors_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_get_data_table_operation_errors` interceptor runs
        before the `post_get_data_table_operation_errors_with_metadata` interceptor.
        """
        return response

    def post_get_data_table_operation_errors_with_metadata(
        self,
        response: data_table.DataTableOperationErrors,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.DataTableOperationErrors, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_data_table_operation_errors

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_get_data_table_operation_errors_with_metadata`
        interceptor in new development instead of the `post_get_data_table_operation_errors` interceptor.
        When both interceptors are used, this `post_get_data_table_operation_errors_with_metadata` interceptor runs after the
        `post_get_data_table_operation_errors` interceptor. The (possibly modified) response returned by
        `post_get_data_table_operation_errors` will be passed to
        `post_get_data_table_operation_errors_with_metadata`.
        """
        return response, metadata

    def pre_get_data_table_row(
        self,
        request: data_table.GetDataTableRowRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.GetDataTableRowRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_data_table_row

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_get_data_table_row(
        self, response: data_table.DataTableRow
    ) -> data_table.DataTableRow:
        """Post-rpc interceptor for get_data_table_row

        DEPRECATED. Please use the `post_get_data_table_row_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_get_data_table_row` interceptor runs
        before the `post_get_data_table_row_with_metadata` interceptor.
        """
        return response

    def post_get_data_table_row_with_metadata(
        self,
        response: data_table.DataTableRow,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_table.DataTableRow, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_data_table_row

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_get_data_table_row_with_metadata`
        interceptor in new development instead of the `post_get_data_table_row` interceptor.
        When both interceptors are used, this `post_get_data_table_row_with_metadata` interceptor runs after the
        `post_get_data_table_row` interceptor. The (possibly modified) response returned by
        `post_get_data_table_row` will be passed to
        `post_get_data_table_row_with_metadata`.
        """
        return response, metadata

    def pre_list_data_table_rows(
        self,
        request: data_table.ListDataTableRowsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.ListDataTableRowsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_table_rows

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_list_data_table_rows(
        self, response: data_table.ListDataTableRowsResponse
    ) -> data_table.ListDataTableRowsResponse:
        """Post-rpc interceptor for list_data_table_rows

        DEPRECATED. Please use the `post_list_data_table_rows_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_list_data_table_rows` interceptor runs
        before the `post_list_data_table_rows_with_metadata` interceptor.
        """
        return response

    def post_list_data_table_rows_with_metadata(
        self,
        response: data_table.ListDataTableRowsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.ListDataTableRowsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_table_rows

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_list_data_table_rows_with_metadata`
        interceptor in new development instead of the `post_list_data_table_rows` interceptor.
        When both interceptors are used, this `post_list_data_table_rows_with_metadata` interceptor runs after the
        `post_list_data_table_rows` interceptor. The (possibly modified) response returned by
        `post_list_data_table_rows` will be passed to
        `post_list_data_table_rows_with_metadata`.
        """
        return response, metadata

    def pre_list_data_tables(
        self,
        request: data_table.ListDataTablesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.ListDataTablesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_data_tables

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_list_data_tables(
        self, response: data_table.ListDataTablesResponse
    ) -> data_table.ListDataTablesResponse:
        """Post-rpc interceptor for list_data_tables

        DEPRECATED. Please use the `post_list_data_tables_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_list_data_tables` interceptor runs
        before the `post_list_data_tables_with_metadata` interceptor.
        """
        return response

    def post_list_data_tables_with_metadata(
        self,
        response: data_table.ListDataTablesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.ListDataTablesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_data_tables

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_list_data_tables_with_metadata`
        interceptor in new development instead of the `post_list_data_tables` interceptor.
        When both interceptors are used, this `post_list_data_tables_with_metadata` interceptor runs after the
        `post_list_data_tables` interceptor. The (possibly modified) response returned by
        `post_list_data_tables` will be passed to
        `post_list_data_tables_with_metadata`.
        """
        return response, metadata

    def pre_update_data_table(
        self,
        request: gcc_data_table.UpdateDataTableRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcc_data_table.UpdateDataTableRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_data_table

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_update_data_table(
        self, response: gcc_data_table.DataTable
    ) -> gcc_data_table.DataTable:
        """Post-rpc interceptor for update_data_table

        DEPRECATED. Please use the `post_update_data_table_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_update_data_table` interceptor runs
        before the `post_update_data_table_with_metadata` interceptor.
        """
        return response

    def post_update_data_table_with_metadata(
        self,
        response: gcc_data_table.DataTable,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcc_data_table.DataTable, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_table

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_update_data_table_with_metadata`
        interceptor in new development instead of the `post_update_data_table` interceptor.
        When both interceptors are used, this `post_update_data_table_with_metadata` interceptor runs after the
        `post_update_data_table` interceptor. The (possibly modified) response returned by
        `post_update_data_table` will be passed to
        `post_update_data_table_with_metadata`.
        """
        return response, metadata

    def pre_update_data_table_row(
        self,
        request: data_table.UpdateDataTableRowRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        data_table.UpdateDataTableRowRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_data_table_row

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_update_data_table_row(
        self, response: data_table.DataTableRow
    ) -> data_table.DataTableRow:
        """Post-rpc interceptor for update_data_table_row

        DEPRECATED. Please use the `post_update_data_table_row_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code. This `post_update_data_table_row` interceptor runs
        before the `post_update_data_table_row_with_metadata` interceptor.
        """
        return response

    def post_update_data_table_row_with_metadata(
        self,
        response: data_table.DataTableRow,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[data_table.DataTableRow, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_data_table_row

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DataTableService server but before it is returned to user code.

        We recommend only using this `post_update_data_table_row_with_metadata`
        interceptor in new development instead of the `post_update_data_table_row` interceptor.
        When both interceptors are used, this `post_update_data_table_row_with_metadata` interceptor runs after the
        `post_update_data_table_row` interceptor. The (possibly modified) response returned by
        `post_update_data_table_row` will be passed to
        `post_update_data_table_row_with_metadata`.
        """
        return response, metadata

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataTableService server but before
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
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataTableService server but before
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
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DataTableService server but before
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
        before they are sent to the DataTableService server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DataTableService server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DataTableServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DataTableServiceRestInterceptor


class DataTableServiceRestTransport(_BaseDataTableServiceRestTransport):
    """REST backend synchronous transport for DataTableService.

    DataTableManager provides an interface for managing data
    tables.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "chronicle.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DataTableServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'chronicle.googleapis.com').
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
            interceptor (Optional[DataTableServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DataTableServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _BulkCreateDataTableRows(
        _BaseDataTableServiceRestTransport._BaseBulkCreateDataTableRows,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.BulkCreateDataTableRows")

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
            request: data_table.BulkCreateDataTableRowsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.BulkCreateDataTableRowsResponse:
            r"""Call the bulk create data table
            rows method over HTTP.

                Args:
                    request (~.data_table.BulkCreateDataTableRowsRequest):
                        The request object. Request to create data table rows in
                    bulk.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.data_table.BulkCreateDataTableRowsResponse:
                        Response message with created data
                    table rows.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseBulkCreateDataTableRows._get_http_options()
            request, metadata = self._interceptor.pre_bulk_create_data_table_rows(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseBulkCreateDataTableRows,
                    "_BaseBulkCreateDataTableRows__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.BulkCreateDataTableRows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkCreateDataTableRows",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTableServiceRestTransport._BulkCreateDataTableRows._get_response(
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
            resp = data_table.BulkCreateDataTableRowsResponse()
            pb_resp = data_table.BulkCreateDataTableRowsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_bulk_create_data_table_rows(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_create_data_table_rows_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_table.BulkCreateDataTableRowsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.bulk_create_data_table_rows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkCreateDataTableRows",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkGetDataTableRows(
        _BaseDataTableServiceRestTransport._BaseBulkGetDataTableRows,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.BulkGetDataTableRows")

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
            request: data_table.BulkGetDataTableRowsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.BulkGetDataTableRowsResponse:
            r"""Call the bulk get data table rows method over HTTP.

            Args:
                request (~.data_table.BulkGetDataTableRowsRequest):
                    The request object. Request to get data table rows in
                bulk.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.BulkGetDataTableRowsResponse:
                    Response message with data table
                rows.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseBulkGetDataTableRows._get_http_options()
            request, metadata = self._interceptor.pre_bulk_get_data_table_rows(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseBulkGetDataTableRows,
                    "_BaseBulkGetDataTableRows__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.BulkGetDataTableRows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkGetDataTableRows",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTableServiceRestTransport._BulkGetDataTableRows._get_response(
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
            resp = data_table.BulkGetDataTableRowsResponse()
            pb_resp = data_table.BulkGetDataTableRowsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_bulk_get_data_table_rows(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_get_data_table_rows_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.BulkGetDataTableRowsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.bulk_get_data_table_rows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkGetDataTableRows",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkReplaceDataTableRows(
        _BaseDataTableServiceRestTransport._BaseBulkReplaceDataTableRows,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.BulkReplaceDataTableRows")

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
            request: data_table.BulkReplaceDataTableRowsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.BulkReplaceDataTableRowsResponse:
            r"""Call the bulk replace data table
            rows method over HTTP.

                Args:
                    request (~.data_table.BulkReplaceDataTableRowsRequest):
                        The request object. Request to replace data table rows in
                    bulk.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.data_table.BulkReplaceDataTableRowsResponse:
                        Response message with data table rows
                    that replaced existing data table rows.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseBulkReplaceDataTableRows._get_http_options()
            request, metadata = self._interceptor.pre_bulk_replace_data_table_rows(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseBulkReplaceDataTableRows,
                    "_BaseBulkReplaceDataTableRows__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.BulkReplaceDataTableRows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkReplaceDataTableRows",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTableServiceRestTransport._BulkReplaceDataTableRows._get_response(
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
            resp = data_table.BulkReplaceDataTableRowsResponse()
            pb_resp = data_table.BulkReplaceDataTableRowsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_bulk_replace_data_table_rows(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_replace_data_table_rows_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_table.BulkReplaceDataTableRowsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.bulk_replace_data_table_rows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkReplaceDataTableRows",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkUpdateDataTableRows(
        _BaseDataTableServiceRestTransport._BaseBulkUpdateDataTableRows,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.BulkUpdateDataTableRows")

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
            request: data_table.BulkUpdateDataTableRowsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.BulkUpdateDataTableRowsResponse:
            r"""Call the bulk update data table
            rows method over HTTP.

                Args:
                    request (~.data_table.BulkUpdateDataTableRowsRequest):
                        The request object. Request to update data table rows in
                    bulk.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.data_table.BulkUpdateDataTableRowsResponse:
                        Response message with updated data
                    table rows.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseBulkUpdateDataTableRows._get_http_options()
            request, metadata = self._interceptor.pre_bulk_update_data_table_rows(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseBulkUpdateDataTableRows,
                    "_BaseBulkUpdateDataTableRows__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.BulkUpdateDataTableRows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkUpdateDataTableRows",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DataTableServiceRestTransport._BulkUpdateDataTableRows._get_response(
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
            resp = data_table.BulkUpdateDataTableRowsResponse()
            pb_resp = data_table.BulkUpdateDataTableRowsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_bulk_update_data_table_rows(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_update_data_table_rows_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        data_table.BulkUpdateDataTableRowsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.bulk_update_data_table_rows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "BulkUpdateDataTableRows",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataTable(
        _BaseDataTableServiceRestTransport._BaseCreateDataTable,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.CreateDataTable")

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
            request: gcc_data_table.CreateDataTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_data_table.DataTable:
            r"""Call the create data table method over HTTP.

            Args:
                request (~.gcc_data_table.CreateDataTableRequest):
                    The request object. A request to create DataTable.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_data_table.DataTable:
                    DataTable represents the data table
                resource.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseCreateDataTable._get_http_options()
            request, metadata = self._interceptor.pre_create_data_table(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseCreateDataTable,
                    "_BaseCreateDataTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.CreateDataTable",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "CreateDataTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._CreateDataTable._get_response(
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
            resp = gcc_data_table.DataTable()
            pb_resp = gcc_data_table.DataTable.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_table(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_table_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_data_table.DataTable.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.create_data_table",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "CreateDataTable",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDataTableRow(
        _BaseDataTableServiceRestTransport._BaseCreateDataTableRow,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.CreateDataTableRow")

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
            request: data_table.CreateDataTableRowRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.DataTableRow:
            r"""Call the create data table row method over HTTP.

            Args:
                request (~.data_table.CreateDataTableRowRequest):
                    The request object. Request to create data table row.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.DataTableRow:
                    DataTableRow represents a single row
                in a data table.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseCreateDataTableRow._get_http_options()
            request, metadata = self._interceptor.pre_create_data_table_row(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseCreateDataTableRow,
                    "_BaseCreateDataTableRow__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.CreateDataTableRow",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "CreateDataTableRow",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._CreateDataTableRow._get_response(
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
            resp = data_table.DataTableRow()
            pb_resp = data_table.DataTableRow.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_data_table_row(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_data_table_row_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.DataTableRow.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.create_data_table_row",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "CreateDataTableRow",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteDataTable(
        _BaseDataTableServiceRestTransport._BaseDeleteDataTable,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.DeleteDataTable")

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
            request: data_table.DeleteDataTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data table method over HTTP.

            Args:
                request (~.data_table.DeleteDataTableRequest):
                    The request object. Request message for deleting data
                tables.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataTableServiceRestTransport._BaseDeleteDataTable._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_table(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseDeleteDataTable,
                    "_BaseDeleteDataTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.DeleteDataTable",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "DeleteDataTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._DeleteDataTable._get_response(
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

    class _DeleteDataTableRow(
        _BaseDataTableServiceRestTransport._BaseDeleteDataTableRow,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.DeleteDataTableRow")

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
            request: data_table.DeleteDataTableRowRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete data table row method over HTTP.

            Args:
                request (~.data_table.DeleteDataTableRowRequest):
                    The request object. Request to delete data table row.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDataTableServiceRestTransport._BaseDeleteDataTableRow._get_http_options()
            request, metadata = self._interceptor.pre_delete_data_table_row(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseDeleteDataTableRow,
                    "_BaseDeleteDataTableRow__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.DeleteDataTableRow",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "DeleteDataTableRow",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._DeleteDataTableRow._get_response(
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

    class _GetDataTable(
        _BaseDataTableServiceRestTransport._BaseGetDataTable, DataTableServiceRestStub
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.GetDataTable")

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
            request: data_table.GetDataTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.DataTable:
            r"""Call the get data table method over HTTP.

            Args:
                request (~.data_table.GetDataTableRequest):
                    The request object. A request to get details about a data
                table.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.DataTable:
                    DataTable represents the data table
                resource.

            """

            http_options = (
                _BaseDataTableServiceRestTransport._BaseGetDataTable._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_data_table(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseGetDataTable,
                    "_BaseGetDataTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.GetDataTable",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetDataTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._GetDataTable._get_response(
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
            resp = data_table.DataTable()
            pb_resp = data_table.DataTable.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_table(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_table_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.DataTable.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.get_data_table",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetDataTable",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataTableOperationErrors(
        _BaseDataTableServiceRestTransport._BaseGetDataTableOperationErrors,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.GetDataTableOperationErrors")

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
            request: data_table.GetDataTableOperationErrorsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.DataTableOperationErrors:
            r"""Call the get data table operation
            errors method over HTTP.

                Args:
                    request (~.data_table.GetDataTableOperationErrorsRequest):
                        The request object. The request message for
                    GetDataTableOperationErrors.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.data_table.DataTableOperationErrors:
                        The message containing the errors for
                    a data table operation.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseGetDataTableOperationErrors._get_http_options()
            request, metadata = self._interceptor.pre_get_data_table_operation_errors(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseGetDataTableOperationErrors,
                    "_BaseGetDataTableOperationErrors__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.GetDataTableOperationErrors",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetDataTableOperationErrors",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._GetDataTableOperationErrors._get_response(
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
            resp = data_table.DataTableOperationErrors()
            pb_resp = data_table.DataTableOperationErrors.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_table_operation_errors(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_data_table_operation_errors_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.DataTableOperationErrors.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.get_data_table_operation_errors",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetDataTableOperationErrors",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDataTableRow(
        _BaseDataTableServiceRestTransport._BaseGetDataTableRow,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.GetDataTableRow")

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
            request: data_table.GetDataTableRowRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.DataTableRow:
            r"""Call the get data table row method over HTTP.

            Args:
                request (~.data_table.GetDataTableRowRequest):
                    The request object. Request to get data table row.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.DataTableRow:
                    DataTableRow represents a single row
                in a data table.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseGetDataTableRow._get_http_options()
            request, metadata = self._interceptor.pre_get_data_table_row(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseGetDataTableRow,
                    "_BaseGetDataTableRow__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.GetDataTableRow",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetDataTableRow",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._GetDataTableRow._get_response(
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
            resp = data_table.DataTableRow()
            pb_resp = data_table.DataTableRow.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_data_table_row(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_data_table_row_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.DataTableRow.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.get_data_table_row",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetDataTableRow",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataTableRows(
        _BaseDataTableServiceRestTransport._BaseListDataTableRows,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.ListDataTableRows")

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
            request: data_table.ListDataTableRowsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.ListDataTableRowsResponse:
            r"""Call the list data table rows method over HTTP.

            Args:
                request (~.data_table.ListDataTableRowsRequest):
                    The request object. Request to list data table rows.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.ListDataTableRowsResponse:
                    Response message for listing data
                table rows.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseListDataTableRows._get_http_options()
            request, metadata = self._interceptor.pre_list_data_table_rows(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseListDataTableRows,
                    "_BaseListDataTableRows__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.ListDataTableRows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "ListDataTableRows",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._ListDataTableRows._get_response(
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
            resp = data_table.ListDataTableRowsResponse()
            pb_resp = data_table.ListDataTableRowsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_table_rows(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_table_rows_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.ListDataTableRowsResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.list_data_table_rows",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "ListDataTableRows",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDataTables(
        _BaseDataTableServiceRestTransport._BaseListDataTables, DataTableServiceRestStub
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.ListDataTables")

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
            request: data_table.ListDataTablesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.ListDataTablesResponse:
            r"""Call the list data tables method over HTTP.

            Args:
                request (~.data_table.ListDataTablesRequest):
                    The request object. A request for a list of data tables.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.ListDataTablesResponse:
                    Response message for listing data
                tables.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseListDataTables._get_http_options()
            request, metadata = self._interceptor.pre_list_data_tables(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseListDataTables,
                    "_BaseListDataTables__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.ListDataTables",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "ListDataTables",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._ListDataTables._get_response(
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
            resp = data_table.ListDataTablesResponse()
            pb_resp = data_table.ListDataTablesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_data_tables(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_data_tables_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.ListDataTablesResponse.to_json(
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
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.list_data_tables",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "ListDataTables",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataTable(
        _BaseDataTableServiceRestTransport._BaseUpdateDataTable,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.UpdateDataTable")

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
            request: gcc_data_table.UpdateDataTableRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcc_data_table.DataTable:
            r"""Call the update data table method over HTTP.

            Args:
                request (~.gcc_data_table.UpdateDataTableRequest):
                    The request object. A request to update details of data
                table.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcc_data_table.DataTable:
                    DataTable represents the data table
                resource.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseUpdateDataTable._get_http_options()
            request, metadata = self._interceptor.pre_update_data_table(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseUpdateDataTable,
                    "_BaseUpdateDataTable__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.UpdateDataTable",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "UpdateDataTable",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._UpdateDataTable._get_response(
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
            resp = gcc_data_table.DataTable()
            pb_resp = gcc_data_table.DataTable.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_table(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_table_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcc_data_table.DataTable.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.update_data_table",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "UpdateDataTable",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDataTableRow(
        _BaseDataTableServiceRestTransport._BaseUpdateDataTableRow,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.UpdateDataTableRow")

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
            request: data_table.UpdateDataTableRowRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> data_table.DataTableRow:
            r"""Call the update data table row method over HTTP.

            Args:
                request (~.data_table.UpdateDataTableRowRequest):
                    The request object. Request to update data table row.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.data_table.DataTableRow:
                    DataTableRow represents a single row
                in a data table.

            """

            http_options = _BaseDataTableServiceRestTransport._BaseUpdateDataTableRow._get_http_options()
            request, metadata = self._interceptor.pre_update_data_table_row(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseUpdateDataTableRow,
                    "_BaseUpdateDataTableRow__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.UpdateDataTableRow",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "UpdateDataTableRow",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._UpdateDataTableRow._get_response(
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
            resp = data_table.DataTableRow()
            pb_resp = data_table.DataTableRow.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_data_table_row(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_data_table_row_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = data_table.DataTableRow.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.chronicle_v1.DataTableServiceClient.update_data_table_row",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "UpdateDataTableRow",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def bulk_create_data_table_rows(
        self,
    ) -> Callable[
        [data_table.BulkCreateDataTableRowsRequest],
        data_table.BulkCreateDataTableRowsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkCreateDataTableRows(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def bulk_get_data_table_rows(
        self,
    ) -> Callable[
        [data_table.BulkGetDataTableRowsRequest],
        data_table.BulkGetDataTableRowsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkGetDataTableRows(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def bulk_replace_data_table_rows(
        self,
    ) -> Callable[
        [data_table.BulkReplaceDataTableRowsRequest],
        data_table.BulkReplaceDataTableRowsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkReplaceDataTableRows(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def bulk_update_data_table_rows(
        self,
    ) -> Callable[
        [data_table.BulkUpdateDataTableRowsRequest],
        data_table.BulkUpdateDataTableRowsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkUpdateDataTableRows(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_data_table(
        self,
    ) -> Callable[[gcc_data_table.CreateDataTableRequest], gcc_data_table.DataTable]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_data_table_row(
        self,
    ) -> Callable[[data_table.CreateDataTableRowRequest], data_table.DataTableRow]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDataTableRow(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_table(
        self,
    ) -> Callable[[data_table.DeleteDataTableRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_data_table_row(
        self,
    ) -> Callable[[data_table.DeleteDataTableRowRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDataTableRow(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_table(
        self,
    ) -> Callable[[data_table.GetDataTableRequest], data_table.DataTable]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_data_table_operation_errors(
        self,
    ) -> Callable[
        [data_table.GetDataTableOperationErrorsRequest],
        data_table.DataTableOperationErrors,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataTableOperationErrors(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_data_table_row(
        self,
    ) -> Callable[[data_table.GetDataTableRowRequest], data_table.DataTableRow]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDataTableRow(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_table_rows(
        self,
    ) -> Callable[
        [data_table.ListDataTableRowsRequest], data_table.ListDataTableRowsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataTableRows(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_data_tables(
        self,
    ) -> Callable[
        [data_table.ListDataTablesRequest], data_table.ListDataTablesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDataTables(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_table(
        self,
    ) -> Callable[[gcc_data_table.UpdateDataTableRequest], gcc_data_table.DataTable]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataTable(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_data_table_row(
        self,
    ) -> Callable[[data_table.UpdateDataTableRowRequest], data_table.DataTableRow]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDataTableRow(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseDataTableServiceRestTransport._BaseCancelOperation,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.CancelOperation")

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

            http_options = _BaseDataTableServiceRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._CancelOperation._get_response(
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
        _BaseDataTableServiceRestTransport._BaseDeleteOperation,
        DataTableServiceRestStub,
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.DeleteOperation")

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

            http_options = _BaseDataTableServiceRestTransport._BaseDeleteOperation._get_http_options()
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._DeleteOperation._get_response(
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
        _BaseDataTableServiceRestTransport._BaseGetOperation, DataTableServiceRestStub
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.GetOperation")

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

            http_options = (
                _BaseDataTableServiceRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.chronicle_v1.DataTableServiceAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
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
        _BaseDataTableServiceRestTransport._BaseListOperations, DataTableServiceRestStub
    ):
        def __hash__(self):
            return hash("DataTableServiceRestTransport.ListOperations")

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

            http_options = _BaseDataTableServiceRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDataTableServiceRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.chronicle_v1.DataTableServiceClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DataTableServiceRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.chronicle_v1.DataTableServiceAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.chronicle.v1.DataTableService",
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


__all__ = ("DataTableServiceRestTransport",)
