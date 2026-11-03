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
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.sqladmin_v1beta4._compat import transcode_request
from google.cloud.sqladmin_v1beta4.types import cloud_sql, cloud_sql_resources

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseSqlInstancesServiceRestTransport

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


class SqlInstancesServiceRestInterceptor:
    """Interceptor for SqlInstancesService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the SqlInstancesServiceRestTransport.

    .. code-block:: python
        class MyCustomSqlInstancesServiceInterceptor(SqlInstancesServiceRestInterceptor):
            def pre_acquire_ssrs_lease(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_acquire_ssrs_lease(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_entra_id_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_entra_id_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_server_ca(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_server_ca(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_add_server_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_add_server_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_clone(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_clone(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_ephemeral(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_ephemeral(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_demote(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_demote(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_demote_master(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_demote_master(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_execute_sql(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_execute_sql(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_failover(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_failover(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_disk_shrink_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_disk_shrink_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_latest_recovery_time(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_latest_recovery_time(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_insert(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_insert(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_entra_id_certificates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_entra_id_certificates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_server_cas(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_server_cas(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_server_certificates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_server_certificates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_patch(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_patch(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_perform_disk_shrink(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_perform_disk_shrink(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_point_in_time_restore(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_point_in_time_restore(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_pre_check_major_version_upgrade(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_pre_check_major_version_upgrade(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_promote_replica(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_promote_replica(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reencrypt(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reencrypt(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_release_ssrs_lease(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_release_ssrs_lease(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reschedule_maintenance(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reschedule_maintenance(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_replica_size(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_replica_size(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reset_ssl_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reset_ssl_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restart(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restart(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_restore_backup(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_restore_backup(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rotate_entra_id_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rotate_entra_id_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rotate_server_ca(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rotate_server_ca(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_rotate_server_certificate(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_rotate_server_certificate(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_external_sync(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_external_sync(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_start_replica(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_start_replica(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_stop_replica(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_stop_replica(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_switchover(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_switchover(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_truncate_log(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_truncate_log(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_verify_external_sync_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_verify_external_sync_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = SqlInstancesServiceRestTransport(interceptor=MyCustomSqlInstancesServiceInterceptor())
        client = SqlInstancesServiceClient(transport=transport)


    """

    def pre_acquire_ssrs_lease(
        self,
        request: cloud_sql.SqlInstancesAcquireSsrsLeaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesAcquireSsrsLeaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for acquire_ssrs_lease

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_acquire_ssrs_lease(
        self, response: cloud_sql.SqlInstancesAcquireSsrsLeaseResponse
    ) -> cloud_sql.SqlInstancesAcquireSsrsLeaseResponse:
        """Post-rpc interceptor for acquire_ssrs_lease

        DEPRECATED. Please use the `post_acquire_ssrs_lease_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_acquire_ssrs_lease` interceptor runs
        before the `post_acquire_ssrs_lease_with_metadata` interceptor.
        """
        return response

    def post_acquire_ssrs_lease_with_metadata(
        self,
        response: cloud_sql.SqlInstancesAcquireSsrsLeaseResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesAcquireSsrsLeaseResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for acquire_ssrs_lease

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_acquire_ssrs_lease_with_metadata`
        interceptor in new development instead of the `post_acquire_ssrs_lease` interceptor.
        When both interceptors are used, this `post_acquire_ssrs_lease_with_metadata` interceptor runs after the
        `post_acquire_ssrs_lease` interceptor. The (possibly modified) response returned by
        `post_acquire_ssrs_lease` will be passed to
        `post_acquire_ssrs_lease_with_metadata`.
        """
        return response, metadata

    def pre_add_entra_id_certificate(
        self,
        request: cloud_sql.SqlInstancesAddEntraIdCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesAddEntraIdCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_entra_id_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_add_entra_id_certificate(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for add_entra_id_certificate

        DEPRECATED. Please use the `post_add_entra_id_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_add_entra_id_certificate` interceptor runs
        before the `post_add_entra_id_certificate_with_metadata` interceptor.
        """
        return response

    def post_add_entra_id_certificate_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_entra_id_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_add_entra_id_certificate_with_metadata`
        interceptor in new development instead of the `post_add_entra_id_certificate` interceptor.
        When both interceptors are used, this `post_add_entra_id_certificate_with_metadata` interceptor runs after the
        `post_add_entra_id_certificate` interceptor. The (possibly modified) response returned by
        `post_add_entra_id_certificate` will be passed to
        `post_add_entra_id_certificate_with_metadata`.
        """
        return response, metadata

    def pre_add_server_ca(
        self,
        request: cloud_sql.SqlInstancesAddServerCaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesAddServerCaRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_server_ca

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_add_server_ca(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for add_server_ca

        DEPRECATED. Please use the `post_add_server_ca_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_add_server_ca` interceptor runs
        before the `post_add_server_ca_with_metadata` interceptor.
        """
        return response

    def post_add_server_ca_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_server_ca

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_add_server_ca_with_metadata`
        interceptor in new development instead of the `post_add_server_ca` interceptor.
        When both interceptors are used, this `post_add_server_ca_with_metadata` interceptor runs after the
        `post_add_server_ca` interceptor. The (possibly modified) response returned by
        `post_add_server_ca` will be passed to
        `post_add_server_ca_with_metadata`.
        """
        return response, metadata

    def pre_add_server_certificate(
        self,
        request: cloud_sql.SqlInstancesAddServerCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesAddServerCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for add_server_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_add_server_certificate(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for add_server_certificate

        DEPRECATED. Please use the `post_add_server_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_add_server_certificate` interceptor runs
        before the `post_add_server_certificate_with_metadata` interceptor.
        """
        return response

    def post_add_server_certificate_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for add_server_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_add_server_certificate_with_metadata`
        interceptor in new development instead of the `post_add_server_certificate` interceptor.
        When both interceptors are used, this `post_add_server_certificate_with_metadata` interceptor runs after the
        `post_add_server_certificate` interceptor. The (possibly modified) response returned by
        `post_add_server_certificate` will be passed to
        `post_add_server_certificate_with_metadata`.
        """
        return response, metadata

    def pre_clone(
        self,
        request: cloud_sql.SqlInstancesCloneRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesCloneRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for clone

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_clone(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for clone

        DEPRECATED. Please use the `post_clone_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_clone` interceptor runs
        before the `post_clone_with_metadata` interceptor.
        """
        return response

    def post_clone_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for clone

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_clone_with_metadata`
        interceptor in new development instead of the `post_clone` interceptor.
        When both interceptors are used, this `post_clone_with_metadata` interceptor runs after the
        `post_clone` interceptor. The (possibly modified) response returned by
        `post_clone` will be passed to
        `post_clone_with_metadata`.
        """
        return response, metadata

    def pre_create_ephemeral(
        self,
        request: cloud_sql.SqlInstancesCreateEphemeralCertRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesCreateEphemeralCertRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_ephemeral

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_create_ephemeral(
        self, response: cloud_sql_resources.SslCert
    ) -> cloud_sql_resources.SslCert:
        """Post-rpc interceptor for create_ephemeral

        DEPRECATED. Please use the `post_create_ephemeral_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_create_ephemeral` interceptor runs
        before the `post_create_ephemeral_with_metadata` interceptor.
        """
        return response

    def post_create_ephemeral_with_metadata(
        self,
        response: cloud_sql_resources.SslCert,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.SslCert, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_ephemeral

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_create_ephemeral_with_metadata`
        interceptor in new development instead of the `post_create_ephemeral` interceptor.
        When both interceptors are used, this `post_create_ephemeral_with_metadata` interceptor runs after the
        `post_create_ephemeral` interceptor. The (possibly modified) response returned by
        `post_create_ephemeral` will be passed to
        `post_create_ephemeral_with_metadata`.
        """
        return response, metadata

    def pre_delete(
        self,
        request: cloud_sql.SqlInstancesDeleteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesDeleteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_delete(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for delete

        DEPRECATED. Please use the `post_delete_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_delete` interceptor runs
        before the `post_delete_with_metadata` interceptor.
        """
        return response

    def post_delete_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_delete_with_metadata`
        interceptor in new development instead of the `post_delete` interceptor.
        When both interceptors are used, this `post_delete_with_metadata` interceptor runs after the
        `post_delete` interceptor. The (possibly modified) response returned by
        `post_delete` will be passed to
        `post_delete_with_metadata`.
        """
        return response, metadata

    def pre_demote(
        self,
        request: cloud_sql.SqlInstancesDemoteRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesDemoteRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for demote

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_demote(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for demote

        DEPRECATED. Please use the `post_demote_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_demote` interceptor runs
        before the `post_demote_with_metadata` interceptor.
        """
        return response

    def post_demote_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for demote

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_demote_with_metadata`
        interceptor in new development instead of the `post_demote` interceptor.
        When both interceptors are used, this `post_demote_with_metadata` interceptor runs after the
        `post_demote` interceptor. The (possibly modified) response returned by
        `post_demote` will be passed to
        `post_demote_with_metadata`.
        """
        return response, metadata

    def pre_demote_master(
        self,
        request: cloud_sql.SqlInstancesDemoteMasterRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesDemoteMasterRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for demote_master

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_demote_master(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for demote_master

        DEPRECATED. Please use the `post_demote_master_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_demote_master` interceptor runs
        before the `post_demote_master_with_metadata` interceptor.
        """
        return response

    def post_demote_master_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for demote_master

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_demote_master_with_metadata`
        interceptor in new development instead of the `post_demote_master` interceptor.
        When both interceptors are used, this `post_demote_master_with_metadata` interceptor runs after the
        `post_demote_master` interceptor. The (possibly modified) response returned by
        `post_demote_master` will be passed to
        `post_demote_master_with_metadata`.
        """
        return response, metadata

    def pre_execute_sql(
        self,
        request: cloud_sql.SqlInstancesExecuteSqlRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesExecuteSqlRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for execute_sql

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_execute_sql(
        self, response: cloud_sql.SqlInstancesExecuteSqlResponse
    ) -> cloud_sql.SqlInstancesExecuteSqlResponse:
        """Post-rpc interceptor for execute_sql

        DEPRECATED. Please use the `post_execute_sql_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_execute_sql` interceptor runs
        before the `post_execute_sql_with_metadata` interceptor.
        """
        return response

    def post_execute_sql_with_metadata(
        self,
        response: cloud_sql.SqlInstancesExecuteSqlResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesExecuteSqlResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for execute_sql

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_execute_sql_with_metadata`
        interceptor in new development instead of the `post_execute_sql` interceptor.
        When both interceptors are used, this `post_execute_sql_with_metadata` interceptor runs after the
        `post_execute_sql` interceptor. The (possibly modified) response returned by
        `post_execute_sql` will be passed to
        `post_execute_sql_with_metadata`.
        """
        return response, metadata

    def pre_export(
        self,
        request: cloud_sql.SqlInstancesExportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesExportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for export

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_export(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for export

        DEPRECATED. Please use the `post_export_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_export` interceptor runs
        before the `post_export_with_metadata` interceptor.
        """
        return response

    def post_export_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_export_with_metadata`
        interceptor in new development instead of the `post_export` interceptor.
        When both interceptors are used, this `post_export_with_metadata` interceptor runs after the
        `post_export` interceptor. The (possibly modified) response returned by
        `post_export` will be passed to
        `post_export_with_metadata`.
        """
        return response, metadata

    def pre_failover(
        self,
        request: cloud_sql.SqlInstancesFailoverRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesFailoverRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for failover

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_failover(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for failover

        DEPRECATED. Please use the `post_failover_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_failover` interceptor runs
        before the `post_failover_with_metadata` interceptor.
        """
        return response

    def post_failover_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for failover

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_failover_with_metadata`
        interceptor in new development instead of the `post_failover` interceptor.
        When both interceptors are used, this `post_failover_with_metadata` interceptor runs after the
        `post_failover` interceptor. The (possibly modified) response returned by
        `post_failover` will be passed to
        `post_failover_with_metadata`.
        """
        return response, metadata

    def pre_get(
        self,
        request: cloud_sql.SqlInstancesGetRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesGetRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_get(
        self, response: cloud_sql_resources.DatabaseInstance
    ) -> cloud_sql_resources.DatabaseInstance:
        """Post-rpc interceptor for get

        DEPRECATED. Please use the `post_get_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_get` interceptor runs
        before the `post_get_with_metadata` interceptor.
        """
        return response

    def post_get_with_metadata(
        self,
        response: cloud_sql_resources.DatabaseInstance,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.DatabaseInstance, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_get_with_metadata`
        interceptor in new development instead of the `post_get` interceptor.
        When both interceptors are used, this `post_get_with_metadata` interceptor runs after the
        `post_get` interceptor. The (possibly modified) response returned by
        `post_get` will be passed to
        `post_get_with_metadata`.
        """
        return response, metadata

    def pre_get_disk_shrink_config(
        self,
        request: cloud_sql.SqlInstancesGetDiskShrinkConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesGetDiskShrinkConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_disk_shrink_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_get_disk_shrink_config(
        self, response: cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse
    ) -> cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse:
        """Post-rpc interceptor for get_disk_shrink_config

        DEPRECATED. Please use the `post_get_disk_shrink_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_get_disk_shrink_config` interceptor runs
        before the `post_get_disk_shrink_config_with_metadata` interceptor.
        """
        return response

    def post_get_disk_shrink_config_with_metadata(
        self,
        response: cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_disk_shrink_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_get_disk_shrink_config_with_metadata`
        interceptor in new development instead of the `post_get_disk_shrink_config` interceptor.
        When both interceptors are used, this `post_get_disk_shrink_config_with_metadata` interceptor runs after the
        `post_get_disk_shrink_config` interceptor. The (possibly modified) response returned by
        `post_get_disk_shrink_config` will be passed to
        `post_get_disk_shrink_config_with_metadata`.
        """
        return response, metadata

    def pre_get_latest_recovery_time(
        self,
        request: cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_latest_recovery_time

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_get_latest_recovery_time(
        self, response: cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse
    ) -> cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse:
        """Post-rpc interceptor for get_latest_recovery_time

        DEPRECATED. Please use the `post_get_latest_recovery_time_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_get_latest_recovery_time` interceptor runs
        before the `post_get_latest_recovery_time_with_metadata` interceptor.
        """
        return response

    def post_get_latest_recovery_time_with_metadata(
        self,
        response: cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_latest_recovery_time

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_get_latest_recovery_time_with_metadata`
        interceptor in new development instead of the `post_get_latest_recovery_time` interceptor.
        When both interceptors are used, this `post_get_latest_recovery_time_with_metadata` interceptor runs after the
        `post_get_latest_recovery_time` interceptor. The (possibly modified) response returned by
        `post_get_latest_recovery_time` will be passed to
        `post_get_latest_recovery_time_with_metadata`.
        """
        return response, metadata

    def pre_import(
        self,
        request: cloud_sql.SqlInstancesImportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesImportRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for import

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_import(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for import

        DEPRECATED. Please use the `post_import_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_import` interceptor runs
        before the `post_import_with_metadata` interceptor.
        """
        return response

    def post_import_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_import_with_metadata`
        interceptor in new development instead of the `post_import` interceptor.
        When both interceptors are used, this `post_import_with_metadata` interceptor runs after the
        `post_import` interceptor. The (possibly modified) response returned by
        `post_import` will be passed to
        `post_import_with_metadata`.
        """
        return response, metadata

    def pre_insert(
        self,
        request: cloud_sql.SqlInstancesInsertRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesInsertRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for insert

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_insert(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for insert

        DEPRECATED. Please use the `post_insert_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_insert` interceptor runs
        before the `post_insert_with_metadata` interceptor.
        """
        return response

    def post_insert_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for insert

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_insert_with_metadata`
        interceptor in new development instead of the `post_insert` interceptor.
        When both interceptors are used, this `post_insert_with_metadata` interceptor runs after the
        `post_insert` interceptor. The (possibly modified) response returned by
        `post_insert` will be passed to
        `post_insert_with_metadata`.
        """
        return response, metadata

    def pre_list(
        self,
        request: cloud_sql.SqlInstancesListRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesListRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_list(
        self, response: cloud_sql_resources.InstancesListResponse
    ) -> cloud_sql_resources.InstancesListResponse:
        """Post-rpc interceptor for list

        DEPRECATED. Please use the `post_list_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_list` interceptor runs
        before the `post_list_with_metadata` interceptor.
        """
        return response

    def post_list_with_metadata(
        self,
        response: cloud_sql_resources.InstancesListResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.InstancesListResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_list_with_metadata`
        interceptor in new development instead of the `post_list` interceptor.
        When both interceptors are used, this `post_list_with_metadata` interceptor runs after the
        `post_list` interceptor. The (possibly modified) response returned by
        `post_list` will be passed to
        `post_list_with_metadata`.
        """
        return response, metadata

    def pre_list_entra_id_certificates(
        self,
        request: cloud_sql.SqlInstancesListEntraIdCertificatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesListEntraIdCertificatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_entra_id_certificates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_list_entra_id_certificates(
        self, response: cloud_sql_resources.InstancesListEntraIdCertificatesResponse
    ) -> cloud_sql_resources.InstancesListEntraIdCertificatesResponse:
        """Post-rpc interceptor for list_entra_id_certificates

        DEPRECATED. Please use the `post_list_entra_id_certificates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_list_entra_id_certificates` interceptor runs
        before the `post_list_entra_id_certificates_with_metadata` interceptor.
        """
        return response

    def post_list_entra_id_certificates_with_metadata(
        self,
        response: cloud_sql_resources.InstancesListEntraIdCertificatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.InstancesListEntraIdCertificatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_entra_id_certificates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_list_entra_id_certificates_with_metadata`
        interceptor in new development instead of the `post_list_entra_id_certificates` interceptor.
        When both interceptors are used, this `post_list_entra_id_certificates_with_metadata` interceptor runs after the
        `post_list_entra_id_certificates` interceptor. The (possibly modified) response returned by
        `post_list_entra_id_certificates` will be passed to
        `post_list_entra_id_certificates_with_metadata`.
        """
        return response, metadata

    def pre_list_server_cas(
        self,
        request: cloud_sql.SqlInstancesListServerCasRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesListServerCasRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_server_cas

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_list_server_cas(
        self, response: cloud_sql_resources.InstancesListServerCasResponse
    ) -> cloud_sql_resources.InstancesListServerCasResponse:
        """Post-rpc interceptor for list_server_cas

        DEPRECATED. Please use the `post_list_server_cas_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_list_server_cas` interceptor runs
        before the `post_list_server_cas_with_metadata` interceptor.
        """
        return response

    def post_list_server_cas_with_metadata(
        self,
        response: cloud_sql_resources.InstancesListServerCasResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.InstancesListServerCasResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_server_cas

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_list_server_cas_with_metadata`
        interceptor in new development instead of the `post_list_server_cas` interceptor.
        When both interceptors are used, this `post_list_server_cas_with_metadata` interceptor runs after the
        `post_list_server_cas` interceptor. The (possibly modified) response returned by
        `post_list_server_cas` will be passed to
        `post_list_server_cas_with_metadata`.
        """
        return response, metadata

    def pre_list_server_certificates(
        self,
        request: cloud_sql.SqlInstancesListServerCertificatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesListServerCertificatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_server_certificates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_list_server_certificates(
        self, response: cloud_sql_resources.InstancesListServerCertificatesResponse
    ) -> cloud_sql_resources.InstancesListServerCertificatesResponse:
        """Post-rpc interceptor for list_server_certificates

        DEPRECATED. Please use the `post_list_server_certificates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_list_server_certificates` interceptor runs
        before the `post_list_server_certificates_with_metadata` interceptor.
        """
        return response

    def post_list_server_certificates_with_metadata(
        self,
        response: cloud_sql_resources.InstancesListServerCertificatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.InstancesListServerCertificatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_server_certificates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_list_server_certificates_with_metadata`
        interceptor in new development instead of the `post_list_server_certificates` interceptor.
        When both interceptors are used, this `post_list_server_certificates_with_metadata` interceptor runs after the
        `post_list_server_certificates` interceptor. The (possibly modified) response returned by
        `post_list_server_certificates` will be passed to
        `post_list_server_certificates_with_metadata`.
        """
        return response, metadata

    def pre_patch(
        self,
        request: cloud_sql.SqlInstancesPatchRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesPatchRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for patch

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_patch(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for patch

        DEPRECATED. Please use the `post_patch_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_patch` interceptor runs
        before the `post_patch_with_metadata` interceptor.
        """
        return response

    def post_patch_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for patch

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_patch_with_metadata`
        interceptor in new development instead of the `post_patch` interceptor.
        When both interceptors are used, this `post_patch_with_metadata` interceptor runs after the
        `post_patch` interceptor. The (possibly modified) response returned by
        `post_patch` will be passed to
        `post_patch_with_metadata`.
        """
        return response, metadata

    def pre_perform_disk_shrink(
        self,
        request: cloud_sql.SqlInstancesPerformDiskShrinkRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesPerformDiskShrinkRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for perform_disk_shrink

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_perform_disk_shrink(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for perform_disk_shrink

        DEPRECATED. Please use the `post_perform_disk_shrink_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_perform_disk_shrink` interceptor runs
        before the `post_perform_disk_shrink_with_metadata` interceptor.
        """
        return response

    def post_perform_disk_shrink_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for perform_disk_shrink

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_perform_disk_shrink_with_metadata`
        interceptor in new development instead of the `post_perform_disk_shrink` interceptor.
        When both interceptors are used, this `post_perform_disk_shrink_with_metadata` interceptor runs after the
        `post_perform_disk_shrink` interceptor. The (possibly modified) response returned by
        `post_perform_disk_shrink` will be passed to
        `post_perform_disk_shrink_with_metadata`.
        """
        return response, metadata

    def pre_point_in_time_restore(
        self,
        request: cloud_sql.SqlInstancesPointInTimeRestoreRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesPointInTimeRestoreRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for point_in_time_restore

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_point_in_time_restore(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for point_in_time_restore

        DEPRECATED. Please use the `post_point_in_time_restore_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_point_in_time_restore` interceptor runs
        before the `post_point_in_time_restore_with_metadata` interceptor.
        """
        return response

    def post_point_in_time_restore_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for point_in_time_restore

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_point_in_time_restore_with_metadata`
        interceptor in new development instead of the `post_point_in_time_restore` interceptor.
        When both interceptors are used, this `post_point_in_time_restore_with_metadata` interceptor runs after the
        `post_point_in_time_restore` interceptor. The (possibly modified) response returned by
        `post_point_in_time_restore` will be passed to
        `post_point_in_time_restore_with_metadata`.
        """
        return response, metadata

    def pre_pre_check_major_version_upgrade(
        self,
        request: cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for pre_check_major_version_upgrade

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_pre_check_major_version_upgrade(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for pre_check_major_version_upgrade

        DEPRECATED. Please use the `post_pre_check_major_version_upgrade_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_pre_check_major_version_upgrade` interceptor runs
        before the `post_pre_check_major_version_upgrade_with_metadata` interceptor.
        """
        return response

    def post_pre_check_major_version_upgrade_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for pre_check_major_version_upgrade

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_pre_check_major_version_upgrade_with_metadata`
        interceptor in new development instead of the `post_pre_check_major_version_upgrade` interceptor.
        When both interceptors are used, this `post_pre_check_major_version_upgrade_with_metadata` interceptor runs after the
        `post_pre_check_major_version_upgrade` interceptor. The (possibly modified) response returned by
        `post_pre_check_major_version_upgrade` will be passed to
        `post_pre_check_major_version_upgrade_with_metadata`.
        """
        return response, metadata

    def pre_promote_replica(
        self,
        request: cloud_sql.SqlInstancesPromoteReplicaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesPromoteReplicaRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for promote_replica

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_promote_replica(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for promote_replica

        DEPRECATED. Please use the `post_promote_replica_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_promote_replica` interceptor runs
        before the `post_promote_replica_with_metadata` interceptor.
        """
        return response

    def post_promote_replica_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for promote_replica

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_promote_replica_with_metadata`
        interceptor in new development instead of the `post_promote_replica` interceptor.
        When both interceptors are used, this `post_promote_replica_with_metadata` interceptor runs after the
        `post_promote_replica` interceptor. The (possibly modified) response returned by
        `post_promote_replica` will be passed to
        `post_promote_replica_with_metadata`.
        """
        return response, metadata

    def pre_reencrypt(
        self,
        request: cloud_sql.SqlInstancesReencryptRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesReencryptRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for reencrypt

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_reencrypt(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for reencrypt

        DEPRECATED. Please use the `post_reencrypt_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_reencrypt` interceptor runs
        before the `post_reencrypt_with_metadata` interceptor.
        """
        return response

    def post_reencrypt_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reencrypt

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_reencrypt_with_metadata`
        interceptor in new development instead of the `post_reencrypt` interceptor.
        When both interceptors are used, this `post_reencrypt_with_metadata` interceptor runs after the
        `post_reencrypt` interceptor. The (possibly modified) response returned by
        `post_reencrypt` will be passed to
        `post_reencrypt_with_metadata`.
        """
        return response, metadata

    def pre_release_ssrs_lease(
        self,
        request: cloud_sql.SqlInstancesReleaseSsrsLeaseRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesReleaseSsrsLeaseRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for release_ssrs_lease

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_release_ssrs_lease(
        self, response: cloud_sql.SqlInstancesReleaseSsrsLeaseResponse
    ) -> cloud_sql.SqlInstancesReleaseSsrsLeaseResponse:
        """Post-rpc interceptor for release_ssrs_lease

        DEPRECATED. Please use the `post_release_ssrs_lease_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_release_ssrs_lease` interceptor runs
        before the `post_release_ssrs_lease_with_metadata` interceptor.
        """
        return response

    def post_release_ssrs_lease_with_metadata(
        self,
        response: cloud_sql.SqlInstancesReleaseSsrsLeaseResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesReleaseSsrsLeaseResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for release_ssrs_lease

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_release_ssrs_lease_with_metadata`
        interceptor in new development instead of the `post_release_ssrs_lease` interceptor.
        When both interceptors are used, this `post_release_ssrs_lease_with_metadata` interceptor runs after the
        `post_release_ssrs_lease` interceptor. The (possibly modified) response returned by
        `post_release_ssrs_lease` will be passed to
        `post_release_ssrs_lease_with_metadata`.
        """
        return response, metadata

    def pre_reschedule_maintenance(
        self,
        request: cloud_sql.SqlInstancesRescheduleMaintenanceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesRescheduleMaintenanceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reschedule_maintenance

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_reschedule_maintenance(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for reschedule_maintenance

        DEPRECATED. Please use the `post_reschedule_maintenance_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_reschedule_maintenance` interceptor runs
        before the `post_reschedule_maintenance_with_metadata` interceptor.
        """
        return response

    def post_reschedule_maintenance_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reschedule_maintenance

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_reschedule_maintenance_with_metadata`
        interceptor in new development instead of the `post_reschedule_maintenance` interceptor.
        When both interceptors are used, this `post_reschedule_maintenance_with_metadata` interceptor runs after the
        `post_reschedule_maintenance` interceptor. The (possibly modified) response returned by
        `post_reschedule_maintenance` will be passed to
        `post_reschedule_maintenance_with_metadata`.
        """
        return response, metadata

    def pre_reset_replica_size(
        self,
        request: cloud_sql.SqlInstancesResetReplicaSizeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesResetReplicaSizeRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reset_replica_size

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_reset_replica_size(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for reset_replica_size

        DEPRECATED. Please use the `post_reset_replica_size_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_reset_replica_size` interceptor runs
        before the `post_reset_replica_size_with_metadata` interceptor.
        """
        return response

    def post_reset_replica_size_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_replica_size

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_reset_replica_size_with_metadata`
        interceptor in new development instead of the `post_reset_replica_size` interceptor.
        When both interceptors are used, this `post_reset_replica_size_with_metadata` interceptor runs after the
        `post_reset_replica_size` interceptor. The (possibly modified) response returned by
        `post_reset_replica_size` will be passed to
        `post_reset_replica_size_with_metadata`.
        """
        return response, metadata

    def pre_reset_ssl_config(
        self,
        request: cloud_sql.SqlInstancesResetSslConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesResetSslConfigRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for reset_ssl_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_reset_ssl_config(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for reset_ssl_config

        DEPRECATED. Please use the `post_reset_ssl_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_reset_ssl_config` interceptor runs
        before the `post_reset_ssl_config_with_metadata` interceptor.
        """
        return response

    def post_reset_ssl_config_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reset_ssl_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_reset_ssl_config_with_metadata`
        interceptor in new development instead of the `post_reset_ssl_config` interceptor.
        When both interceptors are used, this `post_reset_ssl_config_with_metadata` interceptor runs after the
        `post_reset_ssl_config` interceptor. The (possibly modified) response returned by
        `post_reset_ssl_config` will be passed to
        `post_reset_ssl_config_with_metadata`.
        """
        return response, metadata

    def pre_restart(
        self,
        request: cloud_sql.SqlInstancesRestartRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesRestartRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for restart

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_restart(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for restart

        DEPRECATED. Please use the `post_restart_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_restart` interceptor runs
        before the `post_restart_with_metadata` interceptor.
        """
        return response

    def post_restart_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restart

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_restart_with_metadata`
        interceptor in new development instead of the `post_restart` interceptor.
        When both interceptors are used, this `post_restart_with_metadata` interceptor runs after the
        `post_restart` interceptor. The (possibly modified) response returned by
        `post_restart` will be passed to
        `post_restart_with_metadata`.
        """
        return response, metadata

    def pre_restore_backup(
        self,
        request: cloud_sql.SqlInstancesRestoreBackupRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesRestoreBackupRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for restore_backup

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_restore_backup(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for restore_backup

        DEPRECATED. Please use the `post_restore_backup_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_restore_backup` interceptor runs
        before the `post_restore_backup_with_metadata` interceptor.
        """
        return response

    def post_restore_backup_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for restore_backup

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_restore_backup_with_metadata`
        interceptor in new development instead of the `post_restore_backup` interceptor.
        When both interceptors are used, this `post_restore_backup_with_metadata` interceptor runs after the
        `post_restore_backup` interceptor. The (possibly modified) response returned by
        `post_restore_backup` will be passed to
        `post_restore_backup_with_metadata`.
        """
        return response, metadata

    def pre_rotate_entra_id_certificate(
        self,
        request: cloud_sql.SqlInstancesRotateEntraIdCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesRotateEntraIdCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for rotate_entra_id_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_rotate_entra_id_certificate(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for rotate_entra_id_certificate

        DEPRECATED. Please use the `post_rotate_entra_id_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_rotate_entra_id_certificate` interceptor runs
        before the `post_rotate_entra_id_certificate_with_metadata` interceptor.
        """
        return response

    def post_rotate_entra_id_certificate_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rotate_entra_id_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_rotate_entra_id_certificate_with_metadata`
        interceptor in new development instead of the `post_rotate_entra_id_certificate` interceptor.
        When both interceptors are used, this `post_rotate_entra_id_certificate_with_metadata` interceptor runs after the
        `post_rotate_entra_id_certificate` interceptor. The (possibly modified) response returned by
        `post_rotate_entra_id_certificate` will be passed to
        `post_rotate_entra_id_certificate_with_metadata`.
        """
        return response, metadata

    def pre_rotate_server_ca(
        self,
        request: cloud_sql.SqlInstancesRotateServerCaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesRotateServerCaRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for rotate_server_ca

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_rotate_server_ca(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for rotate_server_ca

        DEPRECATED. Please use the `post_rotate_server_ca_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_rotate_server_ca` interceptor runs
        before the `post_rotate_server_ca_with_metadata` interceptor.
        """
        return response

    def post_rotate_server_ca_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rotate_server_ca

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_rotate_server_ca_with_metadata`
        interceptor in new development instead of the `post_rotate_server_ca` interceptor.
        When both interceptors are used, this `post_rotate_server_ca_with_metadata` interceptor runs after the
        `post_rotate_server_ca` interceptor. The (possibly modified) response returned by
        `post_rotate_server_ca` will be passed to
        `post_rotate_server_ca_with_metadata`.
        """
        return response, metadata

    def pre_rotate_server_certificate(
        self,
        request: cloud_sql.SqlInstancesRotateServerCertificateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesRotateServerCertificateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for rotate_server_certificate

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_rotate_server_certificate(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for rotate_server_certificate

        DEPRECATED. Please use the `post_rotate_server_certificate_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_rotate_server_certificate` interceptor runs
        before the `post_rotate_server_certificate_with_metadata` interceptor.
        """
        return response

    def post_rotate_server_certificate_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for rotate_server_certificate

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_rotate_server_certificate_with_metadata`
        interceptor in new development instead of the `post_rotate_server_certificate` interceptor.
        When both interceptors are used, this `post_rotate_server_certificate_with_metadata` interceptor runs after the
        `post_rotate_server_certificate` interceptor. The (possibly modified) response returned by
        `post_rotate_server_certificate` will be passed to
        `post_rotate_server_certificate_with_metadata`.
        """
        return response, metadata

    def pre_start_external_sync(
        self,
        request: cloud_sql.SqlInstancesStartExternalSyncRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesStartExternalSyncRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_external_sync

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_start_external_sync(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for start_external_sync

        DEPRECATED. Please use the `post_start_external_sync_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_start_external_sync` interceptor runs
        before the `post_start_external_sync_with_metadata` interceptor.
        """
        return response

    def post_start_external_sync_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_external_sync

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_start_external_sync_with_metadata`
        interceptor in new development instead of the `post_start_external_sync` interceptor.
        When both interceptors are used, this `post_start_external_sync_with_metadata` interceptor runs after the
        `post_start_external_sync` interceptor. The (possibly modified) response returned by
        `post_start_external_sync` will be passed to
        `post_start_external_sync_with_metadata`.
        """
        return response, metadata

    def pre_start_replica(
        self,
        request: cloud_sql.SqlInstancesStartReplicaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesStartReplicaRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for start_replica

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_start_replica(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for start_replica

        DEPRECATED. Please use the `post_start_replica_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_start_replica` interceptor runs
        before the `post_start_replica_with_metadata` interceptor.
        """
        return response

    def post_start_replica_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for start_replica

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_start_replica_with_metadata`
        interceptor in new development instead of the `post_start_replica` interceptor.
        When both interceptors are used, this `post_start_replica_with_metadata` interceptor runs after the
        `post_start_replica` interceptor. The (possibly modified) response returned by
        `post_start_replica` will be passed to
        `post_start_replica_with_metadata`.
        """
        return response, metadata

    def pre_stop_replica(
        self,
        request: cloud_sql.SqlInstancesStopReplicaRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesStopReplicaRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for stop_replica

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_stop_replica(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for stop_replica

        DEPRECATED. Please use the `post_stop_replica_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_stop_replica` interceptor runs
        before the `post_stop_replica_with_metadata` interceptor.
        """
        return response

    def post_stop_replica_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for stop_replica

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_stop_replica_with_metadata`
        interceptor in new development instead of the `post_stop_replica` interceptor.
        When both interceptors are used, this `post_stop_replica_with_metadata` interceptor runs after the
        `post_stop_replica` interceptor. The (possibly modified) response returned by
        `post_stop_replica` will be passed to
        `post_stop_replica_with_metadata`.
        """
        return response, metadata

    def pre_switchover(
        self,
        request: cloud_sql.SqlInstancesSwitchoverRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesSwitchoverRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for switchover

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_switchover(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for switchover

        DEPRECATED. Please use the `post_switchover_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_switchover` interceptor runs
        before the `post_switchover_with_metadata` interceptor.
        """
        return response

    def post_switchover_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for switchover

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_switchover_with_metadata`
        interceptor in new development instead of the `post_switchover` interceptor.
        When both interceptors are used, this `post_switchover_with_metadata` interceptor runs after the
        `post_switchover` interceptor. The (possibly modified) response returned by
        `post_switchover` will be passed to
        `post_switchover_with_metadata`.
        """
        return response, metadata

    def pre_truncate_log(
        self,
        request: cloud_sql.SqlInstancesTruncateLogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesTruncateLogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for truncate_log

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_truncate_log(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for truncate_log

        DEPRECATED. Please use the `post_truncate_log_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_truncate_log` interceptor runs
        before the `post_truncate_log_with_metadata` interceptor.
        """
        return response

    def post_truncate_log_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for truncate_log

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_truncate_log_with_metadata`
        interceptor in new development instead of the `post_truncate_log` interceptor.
        When both interceptors are used, this `post_truncate_log_with_metadata` interceptor runs after the
        `post_truncate_log` interceptor. The (possibly modified) response returned by
        `post_truncate_log` will be passed to
        `post_truncate_log_with_metadata`.
        """
        return response, metadata

    def pre_update(
        self,
        request: cloud_sql.SqlInstancesUpdateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesUpdateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_update(
        self, response: cloud_sql_resources.Operation
    ) -> cloud_sql_resources.Operation:
        """Post-rpc interceptor for update

        DEPRECATED. Please use the `post_update_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_update` interceptor runs
        before the `post_update_with_metadata` interceptor.
        """
        return response

    def post_update_with_metadata(
        self,
        response: cloud_sql_resources.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[cloud_sql_resources.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_update_with_metadata`
        interceptor in new development instead of the `post_update` interceptor.
        When both interceptors are used, this `post_update_with_metadata` interceptor runs after the
        `post_update` interceptor. The (possibly modified) response returned by
        `post_update` will be passed to
        `post_update_with_metadata`.
        """
        return response, metadata

    def pre_verify_external_sync_settings(
        self,
        request: cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for verify_external_sync_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the SqlInstancesService server.
        """
        return request, metadata

    def post_verify_external_sync_settings(
        self,
        response: cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse,
    ) -> cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse:
        """Post-rpc interceptor for verify_external_sync_settings

        DEPRECATED. Please use the `post_verify_external_sync_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the SqlInstancesService server but before
        it is returned to user code. This `post_verify_external_sync_settings` interceptor runs
        before the `post_verify_external_sync_settings_with_metadata` interceptor.
        """
        return response

    def post_verify_external_sync_settings_with_metadata(
        self,
        response: cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for verify_external_sync_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the SqlInstancesService server but before it is returned to user code.

        We recommend only using this `post_verify_external_sync_settings_with_metadata`
        interceptor in new development instead of the `post_verify_external_sync_settings` interceptor.
        When both interceptors are used, this `post_verify_external_sync_settings_with_metadata` interceptor runs after the
        `post_verify_external_sync_settings` interceptor. The (possibly modified) response returned by
        `post_verify_external_sync_settings` will be passed to
        `post_verify_external_sync_settings_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class SqlInstancesServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: SqlInstancesServiceRestInterceptor


class SqlInstancesServiceRestTransport(_BaseSqlInstancesServiceRestTransport):
    """REST backend synchronous transport for SqlInstancesService.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "sqladmin.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[SqlInstancesServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'sqladmin.googleapis.com').
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
            interceptor (Optional[SqlInstancesServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or SqlInstancesServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _AcquireSsrsLease(
        _BaseSqlInstancesServiceRestTransport._BaseAcquireSsrsLease,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.AcquireSsrsLease")

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
            request: cloud_sql.SqlInstancesAcquireSsrsLeaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql.SqlInstancesAcquireSsrsLeaseResponse:
            r"""Call the acquire ssrs lease method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesAcquireSsrsLeaseRequest):
                    The request object. Request to acquire a lease for SSRS.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql.SqlInstancesAcquireSsrsLeaseResponse:
                    Acquire SSRS lease response.
            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseAcquireSsrsLease._get_http_options()
            request, metadata = self._interceptor.pre_acquire_ssrs_lease(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseAcquireSsrsLease,
                    "_BaseAcquireSsrsLease__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.AcquireSsrsLease",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AcquireSsrsLease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._AcquireSsrsLease._get_response(
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
            resp = cloud_sql.SqlInstancesAcquireSsrsLeaseResponse()
            pb_resp = cloud_sql.SqlInstancesAcquireSsrsLeaseResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_acquire_ssrs_lease(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_acquire_ssrs_lease_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_sql.SqlInstancesAcquireSsrsLeaseResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.acquire_ssrs_lease",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AcquireSsrsLease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddEntraIdCertificate(
        _BaseSqlInstancesServiceRestTransport._BaseAddEntraIdCertificate,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.AddEntraIdCertificate")

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
            request: cloud_sql.SqlInstancesAddEntraIdCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the add entra id certificate method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesAddEntraIdCertificateRequest):
                    The request object. Request for AddEntraIdCertificate
                RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseAddEntraIdCertificate._get_http_options()
            request, metadata = self._interceptor.pre_add_entra_id_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseAddEntraIdCertificate,
                    "_BaseAddEntraIdCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.AddEntraIdCertificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AddEntraIdCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._AddEntraIdCertificate._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_entra_id_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_entra_id_certificate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.add_entra_id_certificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AddEntraIdCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddServerCa(
        _BaseSqlInstancesServiceRestTransport._BaseAddServerCa,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.AddServerCa")

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
            request: cloud_sql.SqlInstancesAddServerCaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the add server ca method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesAddServerCaRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseAddServerCa._get_http_options()
            request, metadata = self._interceptor.pre_add_server_ca(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseAddServerCa,
                    "_BaseAddServerCa__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.AddServerCa",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AddServerCa",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._AddServerCa._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_server_ca(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_server_ca_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.add_server_ca",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AddServerCa",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _AddServerCertificate(
        _BaseSqlInstancesServiceRestTransport._BaseAddServerCertificate,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.AddServerCertificate")

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
            request: cloud_sql.SqlInstancesAddServerCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the add server certificate method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesAddServerCertificateRequest):
                    The request object. Request for AddServerCertificate RPC.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseAddServerCertificate._get_http_options()
            request, metadata = self._interceptor.pre_add_server_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseAddServerCertificate,
                    "_BaseAddServerCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.AddServerCertificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AddServerCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._AddServerCertificate._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_add_server_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_add_server_certificate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.add_server_certificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "AddServerCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Clone(
        _BaseSqlInstancesServiceRestTransport._BaseClone, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Clone")

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
            request: cloud_sql.SqlInstancesCloneRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the clone method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesCloneRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseClone._get_http_options()
            )
            request, metadata = self._interceptor.pre_clone(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseClone,
                    "_BaseClone__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Clone",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Clone",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Clone._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_clone(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_clone_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.clone",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Clone",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateEphemeral(
        _BaseSqlInstancesServiceRestTransport._BaseCreateEphemeral,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.CreateEphemeral")

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
            request: cloud_sql.SqlInstancesCreateEphemeralCertRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.SslCert:
            r"""Call the create ephemeral method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesCreateEphemeralCertRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.SslCert:
                    SslCerts Resource
            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseCreateEphemeral._get_http_options()
            request, metadata = self._interceptor.pre_create_ephemeral(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseCreateEphemeral,
                    "_BaseCreateEphemeral__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.CreateEphemeral",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "CreateEphemeral",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._CreateEphemeral._get_response(
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
            resp = cloud_sql_resources.SslCert()
            pb_resp = cloud_sql_resources.SslCert.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_ephemeral(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_ephemeral_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.SslCert.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.create_ephemeral",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "CreateEphemeral",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Delete(
        _BaseSqlInstancesServiceRestTransport._BaseDelete, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Delete")

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
            request: cloud_sql.SqlInstancesDeleteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the delete method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesDeleteRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseDelete._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseDelete,
                    "_BaseDelete__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Delete",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Delete",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Delete._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.delete",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Delete",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Demote(
        _BaseSqlInstancesServiceRestTransport._BaseDemote, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Demote")

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
            request: cloud_sql.SqlInstancesDemoteRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the demote method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesDemoteRequest):
                    The request object. Instance demote request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseDemote._get_http_options()
            )
            request, metadata = self._interceptor.pre_demote(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseDemote,
                    "_BaseDemote__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Demote",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Demote",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Demote._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_demote(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_demote_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.demote",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Demote",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DemoteMaster(
        _BaseSqlInstancesServiceRestTransport._BaseDemoteMaster,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.DemoteMaster")

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
            request: cloud_sql.SqlInstancesDemoteMasterRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the demote master method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesDemoteMasterRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseDemoteMaster._get_http_options()
            request, metadata = self._interceptor.pre_demote_master(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseDemoteMaster,
                    "_BaseDemoteMaster__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.DemoteMaster",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "DemoteMaster",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._DemoteMaster._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_demote_master(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_demote_master_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.demote_master",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "DemoteMaster",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExecuteSql(
        _BaseSqlInstancesServiceRestTransport._BaseExecuteSql,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ExecuteSql")

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
            request: cloud_sql.SqlInstancesExecuteSqlRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql.SqlInstancesExecuteSqlResponse:
            r"""Call the execute sql method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesExecuteSqlRequest):
                    The request object. Execute SQL statements request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql.SqlInstancesExecuteSqlResponse:

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseExecuteSql._get_http_options()
            request, metadata = self._interceptor.pre_execute_sql(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseExecuteSql,
                    "_BaseExecuteSql__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ExecuteSql",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ExecuteSql",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._ExecuteSql._get_response(
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
            resp = cloud_sql.SqlInstancesExecuteSqlResponse()
            pb_resp = cloud_sql.SqlInstancesExecuteSqlResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_execute_sql(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_execute_sql_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql.SqlInstancesExecuteSqlResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.execute_sql",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ExecuteSql",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Export(
        _BaseSqlInstancesServiceRestTransport._BaseExport, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Export")

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
            request: cloud_sql.SqlInstancesExportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the export method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesExportRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseExport._get_http_options()
            )
            request, metadata = self._interceptor.pre_export(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseExport,
                    "_BaseExport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Export",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Export",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Export._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.export",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Export",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Failover(
        _BaseSqlInstancesServiceRestTransport._BaseFailover, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Failover")

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
            request: cloud_sql.SqlInstancesFailoverRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the failover method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesFailoverRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseFailover._get_http_options()
            )
            request, metadata = self._interceptor.pre_failover(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseFailover,
                    "_BaseFailover__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Failover",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Failover",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Failover._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_failover(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_failover_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.failover",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Failover",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Get(
        _BaseSqlInstancesServiceRestTransport._BaseGet, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Get")

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
            request: cloud_sql.SqlInstancesGetRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.DatabaseInstance:
            r"""Call the get method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesGetRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.DatabaseInstance:
                    A Cloud SQL instance resource.
            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseGet._get_http_options()
            )
            request, metadata = self._interceptor.pre_get(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseGet,
                    "_BaseGet__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Get",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Get",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Get._get_response(
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
            resp = cloud_sql_resources.DatabaseInstance()
            pb_resp = cloud_sql_resources.DatabaseInstance.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.DatabaseInstance.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.get",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Get",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDiskShrinkConfig(
        _BaseSqlInstancesServiceRestTransport._BaseGetDiskShrinkConfig,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.GetDiskShrinkConfig")

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
            request: cloud_sql.SqlInstancesGetDiskShrinkConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse:
            r"""Call the get disk shrink config method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesGetDiskShrinkConfigRequest):
                    The request object. Instance get disk shrink config
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse:
                    Instance get disk shrink config
                response.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseGetDiskShrinkConfig._get_http_options()
            request, metadata = self._interceptor.pre_get_disk_shrink_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseGetDiskShrinkConfig,
                    "_BaseGetDiskShrinkConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.GetDiskShrinkConfig",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "GetDiskShrinkConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._GetDiskShrinkConfig._get_response(
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
            resp = cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse()
            pb_resp = cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_disk_shrink_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_disk_shrink_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.get_disk_shrink_config",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "GetDiskShrinkConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetLatestRecoveryTime(
        _BaseSqlInstancesServiceRestTransport._BaseGetLatestRecoveryTime,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.GetLatestRecoveryTime")

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
            request: cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse:
            r"""Call the get latest recovery time method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest):
                    The request object. Instance get latest recovery time
                request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse:
                    Instance get latest recovery time
                response.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseGetLatestRecoveryTime._get_http_options()
            request, metadata = self._interceptor.pre_get_latest_recovery_time(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseGetLatestRecoveryTime,
                    "_BaseGetLatestRecoveryTime__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.GetLatestRecoveryTime",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "GetLatestRecoveryTime",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._GetLatestRecoveryTime._get_response(
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
            resp = cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse()
            pb_resp = cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_latest_recovery_time(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_latest_recovery_time_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.get_latest_recovery_time",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "GetLatestRecoveryTime",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Import(
        _BaseSqlInstancesServiceRestTransport._BaseImport, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Import")

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
            request: cloud_sql.SqlInstancesImportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the import method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesImportRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseImport._get_http_options()
            )
            request, metadata = self._interceptor.pre_import(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseImport,
                    "_BaseImport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Import",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Import",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Import._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.import_",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Import",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Insert(
        _BaseSqlInstancesServiceRestTransport._BaseInsert, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Insert")

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
            request: cloud_sql.SqlInstancesInsertRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the insert method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesInsertRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseInsert._get_http_options()
            )
            request, metadata = self._interceptor.pre_insert(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseInsert,
                    "_BaseInsert__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Insert",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Insert",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Insert._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_insert(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_insert_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.insert",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Insert",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _List(
        _BaseSqlInstancesServiceRestTransport._BaseList, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.List")

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
            request: cloud_sql.SqlInstancesListRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.InstancesListResponse:
            r"""Call the list method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesListRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.InstancesListResponse:
                    Database instances list response.
            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseList._get_http_options()
            )
            request, metadata = self._interceptor.pre_list(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseList,
                    "_BaseList__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.List",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "List",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._List._get_response(
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
            resp = cloud_sql_resources.InstancesListResponse()
            pb_resp = cloud_sql_resources.InstancesListResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_with_metadata(resp, response_metadata)
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_sql_resources.InstancesListResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.list",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "List",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListEntraIdCertificates(
        _BaseSqlInstancesServiceRestTransport._BaseListEntraIdCertificates,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ListEntraIdCertificates")

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
            request: cloud_sql.SqlInstancesListEntraIdCertificatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.InstancesListEntraIdCertificatesResponse:
            r"""Call the list entra id
            certificates method over HTTP.

                Args:
                    request (~.cloud_sql.SqlInstancesListEntraIdCertificatesRequest):
                        The request object. Request message for
                    SqlInstancesService.ListEntraIdCertificates.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.InstancesListEntraIdCertificatesResponse:
                        Instances ListEntraIdCertificates
                    response.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseListEntraIdCertificates._get_http_options()
            request, metadata = self._interceptor.pre_list_entra_id_certificates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseListEntraIdCertificates,
                    "_BaseListEntraIdCertificates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ListEntraIdCertificates",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ListEntraIdCertificates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._ListEntraIdCertificates._get_response(
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
            resp = cloud_sql_resources.InstancesListEntraIdCertificatesResponse()
            pb_resp = cloud_sql_resources.InstancesListEntraIdCertificatesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_entra_id_certificates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_entra_id_certificates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.InstancesListEntraIdCertificatesResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.list_entra_id_certificates",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ListEntraIdCertificates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServerCas(
        _BaseSqlInstancesServiceRestTransport._BaseListServerCas,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ListServerCas")

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
            request: cloud_sql.SqlInstancesListServerCasRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.InstancesListServerCasResponse:
            r"""Call the list server cas method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesListServerCasRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.InstancesListServerCasResponse:
                    Instances ListServerCas response.
            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseListServerCas._get_http_options()
            request, metadata = self._interceptor.pre_list_server_cas(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseListServerCas,
                    "_BaseListServerCas__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ListServerCas",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ListServerCas",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._ListServerCas._get_response(
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
            resp = cloud_sql_resources.InstancesListServerCasResponse()
            pb_resp = cloud_sql_resources.InstancesListServerCasResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_server_cas(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_server_cas_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_sql_resources.InstancesListServerCasResponse.to_json(
                            response
                        )
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.list_server_cas",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ListServerCas",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListServerCertificates(
        _BaseSqlInstancesServiceRestTransport._BaseListServerCertificates,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ListServerCertificates")

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
            request: cloud_sql.SqlInstancesListServerCertificatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.InstancesListServerCertificatesResponse:
            r"""Call the list server certificates method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesListServerCertificatesRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.InstancesListServerCertificatesResponse:
                    Instances ListServerCertificatess
                response.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseListServerCertificates._get_http_options()
            request, metadata = self._interceptor.pre_list_server_certificates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseListServerCertificates,
                    "_BaseListServerCertificates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ListServerCertificates",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ListServerCertificates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._ListServerCertificates._get_response(
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
            resp = cloud_sql_resources.InstancesListServerCertificatesResponse()
            pb_resp = cloud_sql_resources.InstancesListServerCertificatesResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_server_certificates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_server_certificates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.InstancesListServerCertificatesResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.list_server_certificates",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ListServerCertificates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Patch(
        _BaseSqlInstancesServiceRestTransport._BasePatch, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Patch")

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
            request: cloud_sql.SqlInstancesPatchRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the patch method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesPatchRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BasePatch._get_http_options()
            )
            request, metadata = self._interceptor.pre_patch(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BasePatch,
                    "_BasePatch__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Patch",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Patch",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Patch._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_patch(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_patch_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.patch",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Patch",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PerformDiskShrink(
        _BaseSqlInstancesServiceRestTransport._BasePerformDiskShrink,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.PerformDiskShrink")

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
            request: cloud_sql.SqlInstancesPerformDiskShrinkRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the perform disk shrink method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesPerformDiskShrinkRequest):
                    The request object. Instance perform disk shrink request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BasePerformDiskShrink._get_http_options()
            request, metadata = self._interceptor.pre_perform_disk_shrink(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BasePerformDiskShrink,
                    "_BasePerformDiskShrink__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.PerformDiskShrink",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PerformDiskShrink",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._PerformDiskShrink._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_perform_disk_shrink(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_perform_disk_shrink_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.perform_disk_shrink",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PerformDiskShrink",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PointInTimeRestore(
        _BaseSqlInstancesServiceRestTransport._BasePointInTimeRestore,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.PointInTimeRestore")

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
            request: cloud_sql.SqlInstancesPointInTimeRestoreRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the point in time restore method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesPointInTimeRestoreRequest):
                    The request object. Request to perform a point in time
                restore on a Google Cloud Backup and
                Disaster Recovery managed instance.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BasePointInTimeRestore._get_http_options()
            request, metadata = self._interceptor.pre_point_in_time_restore(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BasePointInTimeRestore,
                    "_BasePointInTimeRestore__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.PointInTimeRestore",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PointInTimeRestore",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._PointInTimeRestore._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_point_in_time_restore(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_point_in_time_restore_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.point_in_time_restore",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PointInTimeRestore",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PreCheckMajorVersionUpgrade(
        _BaseSqlInstancesServiceRestTransport._BasePreCheckMajorVersionUpgrade,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.PreCheckMajorVersionUpgrade")

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
            request: cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the pre check major version
            upgrade method over HTTP.

                Args:
                    request (~.cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest):
                        The request object. Request for Pre-checks for MVU
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.Operation:
                        An Operation resource.&nbsp;For
                    successful operations that return an
                    Operation resource, only the fields
                    relevant to the operation are populated
                    in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BasePreCheckMajorVersionUpgrade._get_http_options()
            request, metadata = self._interceptor.pre_pre_check_major_version_upgrade(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BasePreCheckMajorVersionUpgrade,
                    "_BasePreCheckMajorVersionUpgrade__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.PreCheckMajorVersionUpgrade",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PreCheckMajorVersionUpgrade",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._PreCheckMajorVersionUpgrade._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_pre_check_major_version_upgrade(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_pre_check_major_version_upgrade_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.pre_check_major_version_upgrade",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PreCheckMajorVersionUpgrade",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PromoteReplica(
        _BaseSqlInstancesServiceRestTransport._BasePromoteReplica,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.PromoteReplica")

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
            request: cloud_sql.SqlInstancesPromoteReplicaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the promote replica method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesPromoteReplicaRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BasePromoteReplica._get_http_options()
            request, metadata = self._interceptor.pre_promote_replica(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BasePromoteReplica,
                    "_BasePromoteReplica__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.PromoteReplica",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PromoteReplica",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._PromoteReplica._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_promote_replica(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_promote_replica_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.promote_replica",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "PromoteReplica",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Reencrypt(
        _BaseSqlInstancesServiceRestTransport._BaseReencrypt,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Reencrypt")

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
            request: cloud_sql.SqlInstancesReencryptRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the reencrypt method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesReencryptRequest):
                    The request object. Instance reencrypt request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseReencrypt._get_http_options()
            )
            request, metadata = self._interceptor.pre_reencrypt(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseReencrypt,
                    "_BaseReencrypt__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Reencrypt",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Reencrypt",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Reencrypt._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reencrypt(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reencrypt_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.reencrypt",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Reencrypt",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReleaseSsrsLease(
        _BaseSqlInstancesServiceRestTransport._BaseReleaseSsrsLease,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ReleaseSsrsLease")

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
            request: cloud_sql.SqlInstancesReleaseSsrsLeaseRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql.SqlInstancesReleaseSsrsLeaseResponse:
            r"""Call the release ssrs lease method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesReleaseSsrsLeaseRequest):
                    The request object. Request to release a lease for SSRS.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql.SqlInstancesReleaseSsrsLeaseResponse:
                    The response for the release of the
                SSRS lease.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseReleaseSsrsLease._get_http_options()
            request, metadata = self._interceptor.pre_release_ssrs_lease(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseReleaseSsrsLease,
                    "_BaseReleaseSsrsLease__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ReleaseSsrsLease",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ReleaseSsrsLease",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._ReleaseSsrsLease._get_response(
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
            resp = cloud_sql.SqlInstancesReleaseSsrsLeaseResponse()
            pb_resp = cloud_sql.SqlInstancesReleaseSsrsLeaseResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_release_ssrs_lease(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_release_ssrs_lease_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        cloud_sql.SqlInstancesReleaseSsrsLeaseResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.release_ssrs_lease",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ReleaseSsrsLease",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RescheduleMaintenance(
        _BaseSqlInstancesServiceRestTransport._BaseRescheduleMaintenance,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.RescheduleMaintenance")

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
            request: cloud_sql.SqlInstancesRescheduleMaintenanceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the reschedule maintenance method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesRescheduleMaintenanceRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseRescheduleMaintenance._get_http_options()
            request, metadata = self._interceptor.pre_reschedule_maintenance(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseRescheduleMaintenance,
                    "_BaseRescheduleMaintenance__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.RescheduleMaintenance",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RescheduleMaintenance",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._RescheduleMaintenance._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reschedule_maintenance(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reschedule_maintenance_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.reschedule_maintenance",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RescheduleMaintenance",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetReplicaSize(
        _BaseSqlInstancesServiceRestTransport._BaseResetReplicaSize,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ResetReplicaSize")

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
            request: cloud_sql.SqlInstancesResetReplicaSizeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the reset replica size method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesResetReplicaSizeRequest):
                    The request object. Instance reset replica size request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseResetReplicaSize._get_http_options()
            request, metadata = self._interceptor.pre_reset_replica_size(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseResetReplicaSize,
                    "_BaseResetReplicaSize__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ResetReplicaSize",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ResetReplicaSize",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._ResetReplicaSize._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reset_replica_size(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_replica_size_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.reset_replica_size",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ResetReplicaSize",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ResetSslConfig(
        _BaseSqlInstancesServiceRestTransport._BaseResetSslConfig,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.ResetSslConfig")

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
            request: cloud_sql.SqlInstancesResetSslConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the reset ssl config method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesResetSslConfigRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseResetSslConfig._get_http_options()
            request, metadata = self._interceptor.pre_reset_ssl_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseResetSslConfig,
                    "_BaseResetSslConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.ResetSslConfig",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ResetSslConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._ResetSslConfig._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reset_ssl_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reset_ssl_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.reset_ssl_config",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "ResetSslConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Restart(
        _BaseSqlInstancesServiceRestTransport._BaseRestart, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Restart")

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
            request: cloud_sql.SqlInstancesRestartRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the restart method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesRestartRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseRestart._get_http_options()
            )
            request, metadata = self._interceptor.pre_restart(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseRestart,
                    "_BaseRestart__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Restart",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Restart",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Restart._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_restart(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restart_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.restart",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Restart",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RestoreBackup(
        _BaseSqlInstancesServiceRestTransport._BaseRestoreBackup,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.RestoreBackup")

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
            request: cloud_sql.SqlInstancesRestoreBackupRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the restore backup method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesRestoreBackupRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseRestoreBackup._get_http_options()
            request, metadata = self._interceptor.pre_restore_backup(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseRestoreBackup,
                    "_BaseRestoreBackup__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.RestoreBackup",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RestoreBackup",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._RestoreBackup._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_restore_backup(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_restore_backup_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.restore_backup",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RestoreBackup",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RotateEntraIdCertificate(
        _BaseSqlInstancesServiceRestTransport._BaseRotateEntraIdCertificate,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.RotateEntraIdCertificate")

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
            request: cloud_sql.SqlInstancesRotateEntraIdCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the rotate entra id
            certificate method over HTTP.

                Args:
                    request (~.cloud_sql.SqlInstancesRotateEntraIdCertificateRequest):
                        The request object. Request message for
                    SqlInstancesService.RotateEntraIdCertificate.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.Operation:
                        An Operation resource.&nbsp;For
                    successful operations that return an
                    Operation resource, only the fields
                    relevant to the operation are populated
                    in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseRotateEntraIdCertificate._get_http_options()
            request, metadata = self._interceptor.pre_rotate_entra_id_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseRotateEntraIdCertificate,
                    "_BaseRotateEntraIdCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.RotateEntraIdCertificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RotateEntraIdCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._RotateEntraIdCertificate._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rotate_entra_id_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rotate_entra_id_certificate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.rotate_entra_id_certificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RotateEntraIdCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RotateServerCa(
        _BaseSqlInstancesServiceRestTransport._BaseRotateServerCa,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.RotateServerCa")

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
            request: cloud_sql.SqlInstancesRotateServerCaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the rotate server ca method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesRotateServerCaRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseRotateServerCa._get_http_options()
            request, metadata = self._interceptor.pre_rotate_server_ca(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseRotateServerCa,
                    "_BaseRotateServerCa__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.RotateServerCa",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RotateServerCa",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._RotateServerCa._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rotate_server_ca(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rotate_server_ca_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.rotate_server_ca",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RotateServerCa",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RotateServerCertificate(
        _BaseSqlInstancesServiceRestTransport._BaseRotateServerCertificate,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.RotateServerCertificate")

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
            request: cloud_sql.SqlInstancesRotateServerCertificateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the rotate server certificate method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesRotateServerCertificateRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseRotateServerCertificate._get_http_options()
            request, metadata = self._interceptor.pre_rotate_server_certificate(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseRotateServerCertificate,
                    "_BaseRotateServerCertificate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.RotateServerCertificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RotateServerCertificate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._RotateServerCertificate._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_rotate_server_certificate(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_rotate_server_certificate_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.rotate_server_certificate",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "RotateServerCertificate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartExternalSync(
        _BaseSqlInstancesServiceRestTransport._BaseStartExternalSync,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.StartExternalSync")

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
            request: cloud_sql.SqlInstancesStartExternalSyncRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the start external sync method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesStartExternalSyncRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseStartExternalSync._get_http_options()
            request, metadata = self._interceptor.pre_start_external_sync(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseStartExternalSync,
                    "_BaseStartExternalSync__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.StartExternalSync",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "StartExternalSync",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                SqlInstancesServiceRestTransport._StartExternalSync._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_external_sync(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_external_sync_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.start_external_sync",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "StartExternalSync",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StartReplica(
        _BaseSqlInstancesServiceRestTransport._BaseStartReplica,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.StartReplica")

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
            request: cloud_sql.SqlInstancesStartReplicaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the start replica method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesStartReplicaRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseStartReplica._get_http_options()
            request, metadata = self._interceptor.pre_start_replica(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseStartReplica,
                    "_BaseStartReplica__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.StartReplica",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "StartReplica",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._StartReplica._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_start_replica(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_start_replica_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.start_replica",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "StartReplica",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _StopReplica(
        _BaseSqlInstancesServiceRestTransport._BaseStopReplica,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.StopReplica")

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
            request: cloud_sql.SqlInstancesStopReplicaRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the stop replica method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesStopReplicaRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseStopReplica._get_http_options()
            request, metadata = self._interceptor.pre_stop_replica(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseStopReplica,
                    "_BaseStopReplica__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.StopReplica",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "StopReplica",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._StopReplica._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_stop_replica(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_stop_replica_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.stop_replica",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "StopReplica",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Switchover(
        _BaseSqlInstancesServiceRestTransport._BaseSwitchover,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Switchover")

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
            request: cloud_sql.SqlInstancesSwitchoverRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the switchover method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesSwitchoverRequest):
                    The request object. Instance switchover request.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseSwitchover._get_http_options()
            request, metadata = self._interceptor.pre_switchover(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseSwitchover,
                    "_BaseSwitchover__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Switchover",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Switchover",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Switchover._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_switchover(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_switchover_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.switchover",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Switchover",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TruncateLog(
        _BaseSqlInstancesServiceRestTransport._BaseTruncateLog,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.TruncateLog")

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
            request: cloud_sql.SqlInstancesTruncateLogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the truncate log method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesTruncateLogRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseTruncateLog._get_http_options()
            request, metadata = self._interceptor.pre_truncate_log(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseTruncateLog,
                    "_BaseTruncateLog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.TruncateLog",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "TruncateLog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._TruncateLog._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_truncate_log(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_truncate_log_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.truncate_log",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "TruncateLog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _Update(
        _BaseSqlInstancesServiceRestTransport._BaseUpdate, SqlInstancesServiceRestStub
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.Update")

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
            request: cloud_sql.SqlInstancesUpdateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.Operation:
            r"""Call the update method over HTTP.

            Args:
                request (~.cloud_sql.SqlInstancesUpdateRequest):
                    The request object.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.cloud_sql_resources.Operation:
                    An Operation resource.&nbsp;For
                successful operations that return an
                Operation resource, only the fields
                relevant to the operation are populated
                in the resource.

            """

            http_options = (
                _BaseSqlInstancesServiceRestTransport._BaseUpdate._get_http_options()
            )
            request, metadata = self._interceptor.pre_update(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseUpdate,
                    "_BaseUpdate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.Update",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Update",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._Update._get_response(
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
            resp = cloud_sql_resources.Operation()
            pb_resp = cloud_sql_resources.Operation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.Operation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.update",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "Update",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _VerifyExternalSyncSettings(
        _BaseSqlInstancesServiceRestTransport._BaseVerifyExternalSyncSettings,
        SqlInstancesServiceRestStub,
    ):
        def __hash__(self):
            return hash("SqlInstancesServiceRestTransport.VerifyExternalSyncSettings")

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
            request: cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse:
            r"""Call the verify external sync
            settings method over HTTP.

                Args:
                    request (~.cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest):
                        The request object.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse:
                        Instance verify external sync
                    settings response.

            """

            http_options = _BaseSqlInstancesServiceRestTransport._BaseVerifyExternalSyncSettings._get_http_options()
            request, metadata = self._interceptor.pre_verify_external_sync_settings(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseSqlInstancesServiceRestTransport._BaseVerifyExternalSyncSettings,
                    "_BaseVerifyExternalSyncSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.sql_v1beta4.SqlInstancesServiceClient.VerifyExternalSyncSettings",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "VerifyExternalSyncSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = SqlInstancesServiceRestTransport._VerifyExternalSyncSettings._get_response(
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
            resp = cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse()
            pb_resp = (
                cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_verify_external_sync_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_verify_external_sync_settings_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse.to_json(
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
                    "Received response for google.cloud.sql_v1beta4.SqlInstancesServiceClient.verify_external_sync_settings",
                    extra={
                        "serviceName": "google.cloud.sql.v1beta4.SqlInstancesService",
                        "rpcName": "VerifyExternalSyncSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def acquire_ssrs_lease(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAcquireSsrsLeaseRequest],
        cloud_sql.SqlInstancesAcquireSsrsLeaseResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AcquireSsrsLease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_entra_id_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAddEntraIdCertificateRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddEntraIdCertificate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_server_ca(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAddServerCaRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddServerCa(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def add_server_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesAddServerCertificateRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._AddServerCertificate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def clone(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesCloneRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Clone(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_ephemeral(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesCreateEphemeralCertRequest], cloud_sql_resources.SslCert
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateEphemeral(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesDeleteRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Delete(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def demote(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesDemoteRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Demote(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def demote_master(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesDemoteMasterRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DemoteMaster(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def execute_sql(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesExecuteSqlRequest],
        cloud_sql.SqlInstancesExecuteSqlResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExecuteSql(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesExportRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Export(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def failover(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesFailoverRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Failover(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesGetRequest], cloud_sql_resources.DatabaseInstance
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Get(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_disk_shrink_config(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesGetDiskShrinkConfigRequest],
        cloud_sql_resources.SqlInstancesGetDiskShrinkConfigResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDiskShrinkConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_latest_recovery_time(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesGetLatestRecoveryTimeRequest],
        cloud_sql.SqlInstancesGetLatestRecoveryTimeResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetLatestRecoveryTime(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesImportRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Import(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def insert(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesInsertRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Insert(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListRequest], cloud_sql_resources.InstancesListResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._List(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_entra_id_certificates(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListEntraIdCertificatesRequest],
        cloud_sql_resources.InstancesListEntraIdCertificatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListEntraIdCertificates(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_server_cas(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListServerCasRequest],
        cloud_sql_resources.InstancesListServerCasResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServerCas(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_server_certificates(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesListServerCertificatesRequest],
        cloud_sql_resources.InstancesListServerCertificatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListServerCertificates(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def patch(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesPatchRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Patch(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def perform_disk_shrink(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPerformDiskShrinkRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PerformDiskShrink(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def point_in_time_restore(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPointInTimeRestoreRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PointInTimeRestore(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def pre_check_major_version_upgrade(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPreCheckMajorVersionUpgradeRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PreCheckMajorVersionUpgrade(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def promote_replica(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesPromoteReplicaRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PromoteReplica(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reencrypt(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesReencryptRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Reencrypt(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def release_ssrs_lease(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesReleaseSsrsLeaseRequest],
        cloud_sql.SqlInstancesReleaseSsrsLeaseResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReleaseSsrsLease(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reschedule_maintenance(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRescheduleMaintenanceRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RescheduleMaintenance(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_replica_size(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesResetReplicaSizeRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetReplicaSize(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reset_ssl_config(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesResetSslConfigRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ResetSslConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restart(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRestartRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Restart(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def restore_backup(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRestoreBackupRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RestoreBackup(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rotate_entra_id_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRotateEntraIdCertificateRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RotateEntraIdCertificate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def rotate_server_ca(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRotateServerCaRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RotateServerCa(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def rotate_server_certificate(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesRotateServerCertificateRequest],
        cloud_sql_resources.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RotateServerCertificate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def start_external_sync(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesStartExternalSyncRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartExternalSync(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def start_replica(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesStartReplicaRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StartReplica(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def stop_replica(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesStopReplicaRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._StopReplica(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def switchover(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesSwitchoverRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Switchover(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def truncate_log(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesTruncateLogRequest], cloud_sql_resources.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TruncateLog(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update(
        self,
    ) -> Callable[[cloud_sql.SqlInstancesUpdateRequest], cloud_sql_resources.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._Update(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def verify_external_sync_settings(
        self,
    ) -> Callable[
        [cloud_sql.SqlInstancesVerifyExternalSyncSettingsRequest],
        cloud_sql_resources.SqlInstancesVerifyExternalSyncSettingsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._VerifyExternalSyncSettings(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("SqlInstancesServiceRestTransport",)
