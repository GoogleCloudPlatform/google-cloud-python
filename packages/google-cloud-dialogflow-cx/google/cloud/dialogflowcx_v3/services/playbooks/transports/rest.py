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
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dialogflowcx_v3._compat import transcode_request
from google.cloud.dialogflowcx_v3.types import playbook
from google.cloud.dialogflowcx_v3.types import playbook as gcdc_playbook

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BasePlaybooksRestTransport

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


class PlaybooksRestInterceptor:
    """Interceptor for Playbooks.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the PlaybooksRestTransport.

    .. code-block:: python
        class MyCustomPlaybooksInterceptor(PlaybooksRestInterceptor):
            def pre_create_playbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_playbook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_playbook_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_playbook_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_playbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_playbook_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_export_playbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_playbook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_playbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_playbook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_playbook_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_playbook_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_playbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_playbook(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_playbooks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_playbooks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_playbook_versions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_playbook_versions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_playbook_version(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_playbook_version(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_playbook(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_playbook(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = PlaybooksRestTransport(interceptor=MyCustomPlaybooksInterceptor())
        client = PlaybooksClient(transport=transport)


    """

    def pre_create_playbook(
        self,
        request: gcdc_playbook.CreatePlaybookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcdc_playbook.CreatePlaybookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_playbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_create_playbook(
        self, response: gcdc_playbook.Playbook
    ) -> gcdc_playbook.Playbook:
        """Post-rpc interceptor for create_playbook

        DEPRECATED. Please use the `post_create_playbook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_create_playbook` interceptor runs
        before the `post_create_playbook_with_metadata` interceptor.
        """
        return response

    def post_create_playbook_with_metadata(
        self,
        response: gcdc_playbook.Playbook,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_playbook.Playbook, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_playbook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_create_playbook_with_metadata`
        interceptor in new development instead of the `post_create_playbook` interceptor.
        When both interceptors are used, this `post_create_playbook_with_metadata` interceptor runs after the
        `post_create_playbook` interceptor. The (possibly modified) response returned by
        `post_create_playbook` will be passed to
        `post_create_playbook_with_metadata`.
        """
        return response, metadata

    def pre_create_playbook_version(
        self,
        request: playbook.CreatePlaybookVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.CreatePlaybookVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_playbook_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_create_playbook_version(
        self, response: playbook.PlaybookVersion
    ) -> playbook.PlaybookVersion:
        """Post-rpc interceptor for create_playbook_version

        DEPRECATED. Please use the `post_create_playbook_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_create_playbook_version` interceptor runs
        before the `post_create_playbook_version_with_metadata` interceptor.
        """
        return response

    def post_create_playbook_version_with_metadata(
        self,
        response: playbook.PlaybookVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.PlaybookVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_playbook_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_create_playbook_version_with_metadata`
        interceptor in new development instead of the `post_create_playbook_version` interceptor.
        When both interceptors are used, this `post_create_playbook_version_with_metadata` interceptor runs after the
        `post_create_playbook_version` interceptor. The (possibly modified) response returned by
        `post_create_playbook_version` will be passed to
        `post_create_playbook_version_with_metadata`.
        """
        return response, metadata

    def pre_delete_playbook(
        self,
        request: playbook.DeletePlaybookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.DeletePlaybookRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_playbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def pre_delete_playbook_version(
        self,
        request: playbook.DeletePlaybookVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.DeletePlaybookVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_playbook_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def pre_export_playbook(
        self,
        request: playbook.ExportPlaybookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.ExportPlaybookRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for export_playbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_export_playbook(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_playbook

        DEPRECATED. Please use the `post_export_playbook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_export_playbook` interceptor runs
        before the `post_export_playbook_with_metadata` interceptor.
        """
        return response

    def post_export_playbook_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_playbook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_export_playbook_with_metadata`
        interceptor in new development instead of the `post_export_playbook` interceptor.
        When both interceptors are used, this `post_export_playbook_with_metadata` interceptor runs after the
        `post_export_playbook` interceptor. The (possibly modified) response returned by
        `post_export_playbook` will be passed to
        `post_export_playbook_with_metadata`.
        """
        return response, metadata

    def pre_get_playbook(
        self,
        request: playbook.GetPlaybookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.GetPlaybookRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_playbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_get_playbook(self, response: playbook.Playbook) -> playbook.Playbook:
        """Post-rpc interceptor for get_playbook

        DEPRECATED. Please use the `post_get_playbook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_get_playbook` interceptor runs
        before the `post_get_playbook_with_metadata` interceptor.
        """
        return response

    def post_get_playbook_with_metadata(
        self,
        response: playbook.Playbook,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.Playbook, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_playbook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_get_playbook_with_metadata`
        interceptor in new development instead of the `post_get_playbook` interceptor.
        When both interceptors are used, this `post_get_playbook_with_metadata` interceptor runs after the
        `post_get_playbook` interceptor. The (possibly modified) response returned by
        `post_get_playbook` will be passed to
        `post_get_playbook_with_metadata`.
        """
        return response, metadata

    def pre_get_playbook_version(
        self,
        request: playbook.GetPlaybookVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.GetPlaybookVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_playbook_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_get_playbook_version(
        self, response: playbook.PlaybookVersion
    ) -> playbook.PlaybookVersion:
        """Post-rpc interceptor for get_playbook_version

        DEPRECATED. Please use the `post_get_playbook_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_get_playbook_version` interceptor runs
        before the `post_get_playbook_version_with_metadata` interceptor.
        """
        return response

    def post_get_playbook_version_with_metadata(
        self,
        response: playbook.PlaybookVersion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.PlaybookVersion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_playbook_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_get_playbook_version_with_metadata`
        interceptor in new development instead of the `post_get_playbook_version` interceptor.
        When both interceptors are used, this `post_get_playbook_version_with_metadata` interceptor runs after the
        `post_get_playbook_version` interceptor. The (possibly modified) response returned by
        `post_get_playbook_version` will be passed to
        `post_get_playbook_version_with_metadata`.
        """
        return response, metadata

    def pre_import_playbook(
        self,
        request: playbook.ImportPlaybookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.ImportPlaybookRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for import_playbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_import_playbook(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_playbook

        DEPRECATED. Please use the `post_import_playbook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_import_playbook` interceptor runs
        before the `post_import_playbook_with_metadata` interceptor.
        """
        return response

    def post_import_playbook_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_playbook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_import_playbook_with_metadata`
        interceptor in new development instead of the `post_import_playbook` interceptor.
        When both interceptors are used, this `post_import_playbook_with_metadata` interceptor runs after the
        `post_import_playbook` interceptor. The (possibly modified) response returned by
        `post_import_playbook` will be passed to
        `post_import_playbook_with_metadata`.
        """
        return response, metadata

    def pre_list_playbooks(
        self,
        request: playbook.ListPlaybooksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.ListPlaybooksRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_playbooks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_list_playbooks(
        self, response: playbook.ListPlaybooksResponse
    ) -> playbook.ListPlaybooksResponse:
        """Post-rpc interceptor for list_playbooks

        DEPRECATED. Please use the `post_list_playbooks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_list_playbooks` interceptor runs
        before the `post_list_playbooks_with_metadata` interceptor.
        """
        return response

    def post_list_playbooks_with_metadata(
        self,
        response: playbook.ListPlaybooksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[playbook.ListPlaybooksResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_playbooks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_list_playbooks_with_metadata`
        interceptor in new development instead of the `post_list_playbooks` interceptor.
        When both interceptors are used, this `post_list_playbooks_with_metadata` interceptor runs after the
        `post_list_playbooks` interceptor. The (possibly modified) response returned by
        `post_list_playbooks` will be passed to
        `post_list_playbooks_with_metadata`.
        """
        return response, metadata

    def pre_list_playbook_versions(
        self,
        request: playbook.ListPlaybookVersionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.ListPlaybookVersionsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_playbook_versions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_list_playbook_versions(
        self, response: playbook.ListPlaybookVersionsResponse
    ) -> playbook.ListPlaybookVersionsResponse:
        """Post-rpc interceptor for list_playbook_versions

        DEPRECATED. Please use the `post_list_playbook_versions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_list_playbook_versions` interceptor runs
        before the `post_list_playbook_versions_with_metadata` interceptor.
        """
        return response

    def post_list_playbook_versions_with_metadata(
        self,
        response: playbook.ListPlaybookVersionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.ListPlaybookVersionsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_playbook_versions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_list_playbook_versions_with_metadata`
        interceptor in new development instead of the `post_list_playbook_versions` interceptor.
        When both interceptors are used, this `post_list_playbook_versions_with_metadata` interceptor runs after the
        `post_list_playbook_versions` interceptor. The (possibly modified) response returned by
        `post_list_playbook_versions` will be passed to
        `post_list_playbook_versions_with_metadata`.
        """
        return response, metadata

    def pre_restore_playbook_version(
        self,
        request: playbook.RestorePlaybookVersionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.RestorePlaybookVersionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for restore_playbook_version

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_restore_playbook_version(
        self, response: playbook.RestorePlaybookVersionResponse
    ) -> playbook.RestorePlaybookVersionResponse:
        """Post-rpc interceptor for restore_playbook_version

        DEPRECATED. Please use the `post_restore_playbook_version_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_restore_playbook_version` interceptor runs
        before the `post_restore_playbook_version_with_metadata` interceptor.
        """
        return response

    def post_restore_playbook_version_with_metadata(
        self,
        response: playbook.RestorePlaybookVersionResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        playbook.RestorePlaybookVersionResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for restore_playbook_version

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_restore_playbook_version_with_metadata`
        interceptor in new development instead of the `post_restore_playbook_version` interceptor.
        When both interceptors are used, this `post_restore_playbook_version_with_metadata` interceptor runs after the
        `post_restore_playbook_version` interceptor. The (possibly modified) response returned by
        `post_restore_playbook_version` will be passed to
        `post_restore_playbook_version_with_metadata`.
        """
        return response, metadata

    def pre_update_playbook(
        self,
        request: gcdc_playbook.UpdatePlaybookRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        gcdc_playbook.UpdatePlaybookRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_playbook

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_update_playbook(
        self, response: gcdc_playbook.Playbook
    ) -> gcdc_playbook.Playbook:
        """Post-rpc interceptor for update_playbook

        DEPRECATED. Please use the `post_update_playbook_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code. This `post_update_playbook` interceptor runs
        before the `post_update_playbook_with_metadata` interceptor.
        """
        return response

    def post_update_playbook_with_metadata(
        self,
        response: gcdc_playbook.Playbook,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[gcdc_playbook.Playbook, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_playbook

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the Playbooks server but before it is returned to user code.

        We recommend only using this `post_update_playbook_with_metadata`
        interceptor in new development instead of the `post_update_playbook` interceptor.
        When both interceptors are used, this `post_update_playbook_with_metadata` interceptor runs after the
        `post_update_playbook` interceptor. The (possibly modified) response returned by
        `post_update_playbook` will be passed to
        `post_update_playbook_with_metadata`.
        """
        return response, metadata

    def pre_get_location(
        self,
        request: locations_pb2.GetLocationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.GetLocationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_location

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code.
        """
        return response

    def pre_list_locations(
        self,
        request: locations_pb2.ListLocationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        locations_pb2.ListLocationsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_locations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code.
        """
        return response

    def pre_cancel_operation(
        self,
        request: operations_pb2.CancelOperationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        operations_pb2.CancelOperationRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the Playbooks server but before
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
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the Playbooks server but before
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
        before they are sent to the Playbooks server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the Playbooks server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class PlaybooksRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: PlaybooksRestInterceptor


class PlaybooksRestTransport(_BasePlaybooksRestTransport):
    """REST backend synchronous transport for Playbooks.

    Service for managing
    [Playbooks][google.cloud.dialogflow.cx.v3.Playbook].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[PlaybooksRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dialogflow.googleapis.com').
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
            interceptor (Optional[PlaybooksRestInterceptor]): Interceptor used
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
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or PlaybooksRestInterceptor()
        self._prep_wrapped_messages(client_info)

    @property
    def operations_client(self) -> operations_v1.AbstractOperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Only create a new client if we do not already have one.
        if self._operations_client is None:
            http_options: Dict[str, List[Dict[str, str]]] = {
                "google.longrunning.Operations.CancelOperation": [
                    {
                        "method": "post",
                        "uri": "/v3/{name=projects/*/operations/*}:cancel",
                    },
                    {
                        "method": "post",
                        "uri": "/v3/{name=projects/*/locations/*/operations/*}:cancel",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*/operations/*}",
                    },
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*}/operations",
                    },
                    {
                        "method": "get",
                        "uri": "/v3/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v3",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CreatePlaybook(
        _BasePlaybooksRestTransport._BaseCreatePlaybook, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.CreatePlaybook")

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
            request: gcdc_playbook.CreatePlaybookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_playbook.Playbook:
            r"""Call the create playbook method over HTTP.

            Args:
                request (~.gcdc_playbook.CreatePlaybookRequest):
                    The request object. The request message for
                [Playbooks.CreatePlaybook][google.cloud.dialogflow.cx.v3.Playbooks.CreatePlaybook].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcdc_playbook.Playbook:
                    Playbook is the basic building block
                to instruct the LLM how to execute a
                certain task.

                A playbook consists of a goal to
                accomplish, an optional list of step by
                step instructions (the step instruction
                may refers to name of the custom or
                default plugin tools to use) to perform
                the task, a list of contextual input
                data to be passed in at the beginning of
                the invoked, and a list of output
                parameters to store the playbook result.

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseCreatePlaybook._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_playbook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseCreatePlaybook,
                    "_BaseCreatePlaybook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.CreatePlaybook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "CreatePlaybook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._CreatePlaybook._get_response(
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
            resp = gcdc_playbook.Playbook()
            pb_resp = gcdc_playbook.Playbook.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_playbook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_playbook_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcdc_playbook.Playbook.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.create_playbook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "CreatePlaybook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePlaybookVersion(
        _BasePlaybooksRestTransport._BaseCreatePlaybookVersion, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.CreatePlaybookVersion")

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
            request: playbook.CreatePlaybookVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> playbook.PlaybookVersion:
            r"""Call the create playbook version method over HTTP.

            Args:
                request (~.playbook.CreatePlaybookVersionRequest):
                    The request object. The request message for
                [Playbooks.CreatePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.CreatePlaybookVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.playbook.PlaybookVersion:
                    Playbook version is a snapshot of the
                playbook at certain timestamp.

            """

            http_options = _BasePlaybooksRestTransport._BaseCreatePlaybookVersion._get_http_options()
            request, metadata = self._interceptor.pre_create_playbook_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseCreatePlaybookVersion,
                    "_BaseCreatePlaybookVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.CreatePlaybookVersion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "CreatePlaybookVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._CreatePlaybookVersion._get_response(
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
            resp = playbook.PlaybookVersion()
            pb_resp = playbook.PlaybookVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_playbook_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_playbook_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = playbook.PlaybookVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.create_playbook_version",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "CreatePlaybookVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePlaybook(
        _BasePlaybooksRestTransport._BaseDeletePlaybook, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.DeletePlaybook")

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
            request: playbook.DeletePlaybookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete playbook method over HTTP.

            Args:
                request (~.playbook.DeletePlaybookRequest):
                    The request object. The request message for
                [Playbooks.DeletePlaybook][google.cloud.dialogflow.cx.v3.Playbooks.DeletePlaybook].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BasePlaybooksRestTransport._BaseDeletePlaybook._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_playbook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseDeletePlaybook,
                    "_BaseDeletePlaybook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.DeletePlaybook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "DeletePlaybook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._DeletePlaybook._get_response(
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

    class _DeletePlaybookVersion(
        _BasePlaybooksRestTransport._BaseDeletePlaybookVersion, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.DeletePlaybookVersion")

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
            request: playbook.DeletePlaybookVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete playbook version method over HTTP.

            Args:
                request (~.playbook.DeletePlaybookVersionRequest):
                    The request object. The request message for
                [Playbooks.DeletePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.DeletePlaybookVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BasePlaybooksRestTransport._BaseDeletePlaybookVersion._get_http_options()
            request, metadata = self._interceptor.pre_delete_playbook_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseDeletePlaybookVersion,
                    "_BaseDeletePlaybookVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.DeletePlaybookVersion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "DeletePlaybookVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._DeletePlaybookVersion._get_response(
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

    class _ExportPlaybook(
        _BasePlaybooksRestTransport._BaseExportPlaybook, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.ExportPlaybook")

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
            request: playbook.ExportPlaybookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export playbook method over HTTP.

            Args:
                request (~.playbook.ExportPlaybookRequest):
                    The request object. The request message for
                [Playbooks.ExportPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.ExportPlaybook].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseExportPlaybook._get_http_options()
            )
            request, metadata = self._interceptor.pre_export_playbook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseExportPlaybook,
                    "_BaseExportPlaybook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.ExportPlaybook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ExportPlaybook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._ExportPlaybook._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_playbook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_playbook_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.export_playbook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ExportPlaybook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPlaybook(_BasePlaybooksRestTransport._BaseGetPlaybook, PlaybooksRestStub):
        def __hash__(self):
            return hash("PlaybooksRestTransport.GetPlaybook")

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
            request: playbook.GetPlaybookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> playbook.Playbook:
            r"""Call the get playbook method over HTTP.

            Args:
                request (~.playbook.GetPlaybookRequest):
                    The request object. The request message for
                [Playbooks.GetPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.GetPlaybook].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.playbook.Playbook:
                    Playbook is the basic building block
                to instruct the LLM how to execute a
                certain task.

                A playbook consists of a goal to
                accomplish, an optional list of step by
                step instructions (the step instruction
                may refers to name of the custom or
                default plugin tools to use) to perform
                the task, a list of contextual input
                data to be passed in at the beginning of
                the invoked, and a list of output
                parameters to store the playbook result.

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseGetPlaybook._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_playbook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseGetPlaybook,
                    "_BaseGetPlaybook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.GetPlaybook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetPlaybook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._GetPlaybook._get_response(
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
            resp = playbook.Playbook()
            pb_resp = playbook.Playbook.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_playbook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_playbook_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = playbook.Playbook.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.get_playbook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetPlaybook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPlaybookVersion(
        _BasePlaybooksRestTransport._BaseGetPlaybookVersion, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.GetPlaybookVersion")

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
            request: playbook.GetPlaybookVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> playbook.PlaybookVersion:
            r"""Call the get playbook version method over HTTP.

            Args:
                request (~.playbook.GetPlaybookVersionRequest):
                    The request object. The request message for
                [Playbooks.GetPlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.GetPlaybookVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.playbook.PlaybookVersion:
                    Playbook version is a snapshot of the
                playbook at certain timestamp.

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseGetPlaybookVersion._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_playbook_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseGetPlaybookVersion,
                    "_BaseGetPlaybookVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.GetPlaybookVersion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetPlaybookVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._GetPlaybookVersion._get_response(
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
            resp = playbook.PlaybookVersion()
            pb_resp = playbook.PlaybookVersion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_playbook_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_playbook_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = playbook.PlaybookVersion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.get_playbook_version",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetPlaybookVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportPlaybook(
        _BasePlaybooksRestTransport._BaseImportPlaybook, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.ImportPlaybook")

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
            request: playbook.ImportPlaybookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import playbook method over HTTP.

            Args:
                request (~.playbook.ImportPlaybookRequest):
                    The request object. The request message for
                [Playbooks.ImportPlaybook][google.cloud.dialogflow.cx.v3.Playbooks.ImportPlaybook].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.operations_pb2.Operation:
                    This resource represents a
                long-running operation that is the
                result of a network API call.

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseImportPlaybook._get_http_options()
            )
            request, metadata = self._interceptor.pre_import_playbook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseImportPlaybook,
                    "_BaseImportPlaybook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.ImportPlaybook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ImportPlaybook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._ImportPlaybook._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_playbook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_playbook_with_metadata(
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.import_playbook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ImportPlaybook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPlaybooks(
        _BasePlaybooksRestTransport._BaseListPlaybooks, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.ListPlaybooks")

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
            request: playbook.ListPlaybooksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> playbook.ListPlaybooksResponse:
            r"""Call the list playbooks method over HTTP.

            Args:
                request (~.playbook.ListPlaybooksRequest):
                    The request object. The request message for
                [Playbooks.ListPlaybooks][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybooks].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.playbook.ListPlaybooksResponse:
                    The response message for
                [Playbooks.ListPlaybooks][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybooks].

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseListPlaybooks._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_playbooks(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseListPlaybooks,
                    "_BaseListPlaybooks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.ListPlaybooks",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListPlaybooks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._ListPlaybooks._get_response(
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
            resp = playbook.ListPlaybooksResponse()
            pb_resp = playbook.ListPlaybooksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_playbooks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_playbooks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = playbook.ListPlaybooksResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.list_playbooks",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListPlaybooks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPlaybookVersions(
        _BasePlaybooksRestTransport._BaseListPlaybookVersions, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.ListPlaybookVersions")

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
            request: playbook.ListPlaybookVersionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> playbook.ListPlaybookVersionsResponse:
            r"""Call the list playbook versions method over HTTP.

            Args:
                request (~.playbook.ListPlaybookVersionsRequest):
                    The request object. The request message for
                [Playbooks.ListPlaybookVersions][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybookVersions].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.playbook.ListPlaybookVersionsResponse:
                    The response message for
                [Playbooks.ListPlaybookVersions][google.cloud.dialogflow.cx.v3.Playbooks.ListPlaybookVersions].

            """

            http_options = _BasePlaybooksRestTransport._BaseListPlaybookVersions._get_http_options()
            request, metadata = self._interceptor.pre_list_playbook_versions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseListPlaybookVersions,
                    "_BaseListPlaybookVersions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.ListPlaybookVersions",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListPlaybookVersions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._ListPlaybookVersions._get_response(
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
            resp = playbook.ListPlaybookVersionsResponse()
            pb_resp = playbook.ListPlaybookVersionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_playbook_versions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_playbook_versions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = playbook.ListPlaybookVersionsResponse.to_json(
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.list_playbook_versions",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListPlaybookVersions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestorePlaybookVersion(
        _BasePlaybooksRestTransport._BaseRestorePlaybookVersion, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.RestorePlaybookVersion")

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
            request: playbook.RestorePlaybookVersionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> playbook.RestorePlaybookVersionResponse:
            r"""Call the restore playbook version method over HTTP.

            Args:
                request (~.playbook.RestorePlaybookVersionRequest):
                    The request object. The request message for
                [Playbooks.RestorePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.RestorePlaybookVersion].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.playbook.RestorePlaybookVersionResponse:
                    The response message for
                [Playbooks.RestorePlaybookVersion][google.cloud.dialogflow.cx.v3.Playbooks.RestorePlaybookVersion].

            """

            http_options = _BasePlaybooksRestTransport._BaseRestorePlaybookVersion._get_http_options()
            request, metadata = self._interceptor.pre_restore_playbook_version(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseRestorePlaybookVersion,
                    "_BaseRestorePlaybookVersion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.RestorePlaybookVersion",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "RestorePlaybookVersion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._RestorePlaybookVersion._get_response(
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
            resp = playbook.RestorePlaybookVersionResponse()
            pb_resp = playbook.RestorePlaybookVersionResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_restore_playbook_version(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_playbook_version_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = playbook.RestorePlaybookVersionResponse.to_json(
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.restore_playbook_version",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "RestorePlaybookVersion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePlaybook(
        _BasePlaybooksRestTransport._BaseUpdatePlaybook, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.UpdatePlaybook")

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
            request: gcdc_playbook.UpdatePlaybookRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> gcdc_playbook.Playbook:
            r"""Call the update playbook method over HTTP.

            Args:
                request (~.gcdc_playbook.UpdatePlaybookRequest):
                    The request object. The request message for
                [Playbooks.UpdatePlaybook][google.cloud.dialogflow.cx.v3.Playbooks.UpdatePlaybook].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.gcdc_playbook.Playbook:
                    Playbook is the basic building block
                to instruct the LLM how to execute a
                certain task.

                A playbook consists of a goal to
                accomplish, an optional list of step by
                step instructions (the step instruction
                may refers to name of the custom or
                default plugin tools to use) to perform
                the task, a list of contextual input
                data to be passed in at the beginning of
                the invoked, and a list of output
                parameters to store the playbook result.

            """

            http_options = (
                _BasePlaybooksRestTransport._BaseUpdatePlaybook._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_playbook(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseUpdatePlaybook,
                    "_BaseUpdatePlaybook__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.UpdatePlaybook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "UpdatePlaybook",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._UpdatePlaybook._get_response(
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
            resp = gcdc_playbook.Playbook()
            pb_resp = gcdc_playbook.Playbook.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_playbook(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_playbook_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = gcdc_playbook.Playbook.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksClient.update_playbook",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "UpdatePlaybook",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def create_playbook(
        self,
    ) -> Callable[[gcdc_playbook.CreatePlaybookRequest], gcdc_playbook.Playbook]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePlaybook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_playbook_version(
        self,
    ) -> Callable[[playbook.CreatePlaybookVersionRequest], playbook.PlaybookVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePlaybookVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_playbook(
        self,
    ) -> Callable[[playbook.DeletePlaybookRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePlaybook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_playbook_version(
        self,
    ) -> Callable[[playbook.DeletePlaybookVersionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePlaybookVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_playbook(
        self,
    ) -> Callable[[playbook.ExportPlaybookRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportPlaybook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_playbook(
        self,
    ) -> Callable[[playbook.GetPlaybookRequest], playbook.Playbook]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPlaybook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_playbook_version(
        self,
    ) -> Callable[[playbook.GetPlaybookVersionRequest], playbook.PlaybookVersion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPlaybookVersion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_playbook(
        self,
    ) -> Callable[[playbook.ImportPlaybookRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportPlaybook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_playbooks(
        self,
    ) -> Callable[[playbook.ListPlaybooksRequest], playbook.ListPlaybooksResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPlaybooks(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_playbook_versions(
        self,
    ) -> Callable[
        [playbook.ListPlaybookVersionsRequest], playbook.ListPlaybookVersionsResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPlaybookVersions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_playbook_version(
        self,
    ) -> Callable[
        [playbook.RestorePlaybookVersionRequest],
        playbook.RestorePlaybookVersionResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestorePlaybookVersion(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_playbook(
        self,
    ) -> Callable[[gcdc_playbook.UpdatePlaybookRequest], gcdc_playbook.Playbook]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePlaybook(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetLocation(_BasePlaybooksRestTransport._BaseGetLocation, PlaybooksRestStub):
        def __hash__(self):
            return hash("PlaybooksRestTransport.GetLocation")

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
            request: locations_pb2.GetLocationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.Location:
            r"""Call the get location method over HTTP.

            Args:
                request (locations_pb2.GetLocationRequest):
                    The request object for GetLocation method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.Location: Response from GetLocation method.
            """

            http_options = (
                _BasePlaybooksRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseGetLocation,
                    "_BaseGetLocation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._GetLocation._get_response(
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
            resp = locations_pb2.Location()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_location(resp)
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(self._session, self._host, self._interceptor)  # type: ignore

    class _ListLocations(
        _BasePlaybooksRestTransport._BaseListLocations, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.ListLocations")

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
            request: locations_pb2.ListLocationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> locations_pb2.ListLocationsResponse:
            r"""Call the list locations method over HTTP.

            Args:
                request (locations_pb2.ListLocationsRequest):
                    The request object for ListLocations method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                locations_pb2.ListLocationsResponse: Response from ListLocations method.
            """

            http_options = (
                _BasePlaybooksRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseListLocations,
                    "_BaseListLocations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._ListLocations._get_response(
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
            resp = locations_pb2.ListLocationsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_list_locations(resp)
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BasePlaybooksRestTransport._BaseCancelOperation, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.CancelOperation")

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

            http_options = (
                _BasePlaybooksRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BasePlaybooksRestTransport._BaseGetOperation, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.GetOperation")

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
                _BasePlaybooksRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
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
        _BasePlaybooksRestTransport._BaseListOperations, PlaybooksRestStub
    ):
        def __hash__(self):
            return hash("PlaybooksRestTransport.ListOperations")

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

            http_options = (
                _BasePlaybooksRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BasePlaybooksRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.dialogflow.cx_v3.PlaybooksClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = PlaybooksRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.dialogflow.cx_v3.PlaybooksAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.dialogflow.cx.v3.Playbooks",
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


__all__ = ("PlaybooksRestTransport",)
