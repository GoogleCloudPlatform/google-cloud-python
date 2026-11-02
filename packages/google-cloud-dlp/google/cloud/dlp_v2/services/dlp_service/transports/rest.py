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
from google.cloud.location import locations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.dlp_v2._compat import transcode_request
from google.cloud.dlp_v2.types import dlp

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDlpServiceRestTransport

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


class DlpServiceRestInterceptor:
    """Interceptor for DlpService.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DlpServiceRestTransport.

    .. code-block:: python
        class MyCustomDlpServiceInterceptor(DlpServiceRestInterceptor):
            def pre_activate_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_activate_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_cancel_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_create_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_content_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_content_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_deidentify_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_discovery_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_discovery_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_dlp_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_inspect_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_stored_info_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deidentify_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deidentify_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_content_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_discovery_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_file_store_data_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_table_data_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_finish_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_get_column_data_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_column_data_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_content_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_content_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_deidentify_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_discovery_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_discovery_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_dlp_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_file_store_data_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_file_store_data_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_inspect_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_project_data_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_project_data_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_stored_info_type(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_table_data_profile(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_table_data_profile(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_hybrid_inspect_dlp_job(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_hybrid_inspect_dlp_job(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_hybrid_inspect_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_hybrid_inspect_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_inspect_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_inspect_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_column_data_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_column_data_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_content_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_content_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_deidentify_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_deidentify_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_discovery_configs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_discovery_configs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_dlp_jobs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_dlp_jobs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_file_store_data_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_file_store_data_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_info_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_info_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_inspect_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_inspect_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_job_triggers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_job_triggers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_project_data_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_project_data_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_stored_info_types(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_stored_info_types(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_table_data_profiles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_table_data_profiles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_redact_image(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_redact_image(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_reidentify_content(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_reidentify_content(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_search_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_search_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_content_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_content_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_deidentify_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_deidentify_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_discovery_config(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_discovery_config(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_inspect_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_inspect_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_job_trigger(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_job_trigger(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_stored_info_type(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_stored_info_type(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DlpServiceRestTransport(interceptor=MyCustomDlpServiceInterceptor())
        client = DlpServiceClient(transport=transport)


    """

    def pre_activate_job_trigger(
        self,
        request: dlp.ActivateJobTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ActivateJobTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for activate_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_activate_job_trigger(self, response: dlp.DlpJob) -> dlp.DlpJob:
        """Post-rpc interceptor for activate_job_trigger

        DEPRECATED. Please use the `post_activate_job_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_activate_job_trigger` interceptor runs
        before the `post_activate_job_trigger_with_metadata` interceptor.
        """
        return response

    def post_activate_job_trigger_with_metadata(
        self, response: dlp.DlpJob, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[dlp.DlpJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for activate_job_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_activate_job_trigger_with_metadata`
        interceptor in new development instead of the `post_activate_job_trigger` interceptor.
        When both interceptors are used, this `post_activate_job_trigger_with_metadata` interceptor runs after the
        `post_activate_job_trigger` interceptor. The (possibly modified) response returned by
        `post_activate_job_trigger` will be passed to
        `post_activate_job_trigger_with_metadata`.
        """
        return response, metadata

    def pre_cancel_dlp_job(
        self,
        request: dlp.CancelDlpJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.CancelDlpJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for cancel_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_create_connection(
        self,
        request: dlp.CreateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.CreateConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_connection(self, response: dlp.Connection) -> dlp.Connection:
        """Post-rpc interceptor for create_connection

        DEPRECATED. Please use the `post_create_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_connection` interceptor runs
        before the `post_create_connection_with_metadata` interceptor.
        """
        return response

    def post_create_connection_with_metadata(
        self,
        response: dlp.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_connection_with_metadata`
        interceptor in new development instead of the `post_create_connection` interceptor.
        When both interceptors are used, this `post_create_connection_with_metadata` interceptor runs after the
        `post_create_connection` interceptor. The (possibly modified) response returned by
        `post_create_connection` will be passed to
        `post_create_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_content_policy(
        self,
        request: dlp.CreateContentPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.CreateContentPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_content_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_content_policy(
        self, response: dlp.ContentPolicy
    ) -> dlp.ContentPolicy:
        """Post-rpc interceptor for create_content_policy

        DEPRECATED. Please use the `post_create_content_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_content_policy` interceptor runs
        before the `post_create_content_policy_with_metadata` interceptor.
        """
        return response

    def post_create_content_policy_with_metadata(
        self,
        response: dlp.ContentPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ContentPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_content_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_content_policy_with_metadata`
        interceptor in new development instead of the `post_create_content_policy` interceptor.
        When both interceptors are used, this `post_create_content_policy_with_metadata` interceptor runs after the
        `post_create_content_policy` interceptor. The (possibly modified) response returned by
        `post_create_content_policy` will be passed to
        `post_create_content_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_deidentify_template(
        self,
        request: dlp.CreateDeidentifyTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.CreateDeidentifyTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_deidentify_template(
        self, response: dlp.DeidentifyTemplate
    ) -> dlp.DeidentifyTemplate:
        """Post-rpc interceptor for create_deidentify_template

        DEPRECATED. Please use the `post_create_deidentify_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_deidentify_template` interceptor runs
        before the `post_create_deidentify_template_with_metadata` interceptor.
        """
        return response

    def post_create_deidentify_template_with_metadata(
        self,
        response: dlp.DeidentifyTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeidentifyTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_deidentify_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_deidentify_template_with_metadata`
        interceptor in new development instead of the `post_create_deidentify_template` interceptor.
        When both interceptors are used, this `post_create_deidentify_template_with_metadata` interceptor runs after the
        `post_create_deidentify_template` interceptor. The (possibly modified) response returned by
        `post_create_deidentify_template` will be passed to
        `post_create_deidentify_template_with_metadata`.
        """
        return response, metadata

    def pre_create_discovery_config(
        self,
        request: dlp.CreateDiscoveryConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.CreateDiscoveryConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_discovery_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_discovery_config(
        self, response: dlp.DiscoveryConfig
    ) -> dlp.DiscoveryConfig:
        """Post-rpc interceptor for create_discovery_config

        DEPRECATED. Please use the `post_create_discovery_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_discovery_config` interceptor runs
        before the `post_create_discovery_config_with_metadata` interceptor.
        """
        return response

    def post_create_discovery_config_with_metadata(
        self,
        response: dlp.DiscoveryConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DiscoveryConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_discovery_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_discovery_config_with_metadata`
        interceptor in new development instead of the `post_create_discovery_config` interceptor.
        When both interceptors are used, this `post_create_discovery_config_with_metadata` interceptor runs after the
        `post_create_discovery_config` interceptor. The (possibly modified) response returned by
        `post_create_discovery_config` will be passed to
        `post_create_discovery_config_with_metadata`.
        """
        return response, metadata

    def pre_create_dlp_job(
        self,
        request: dlp.CreateDlpJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.CreateDlpJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_dlp_job(self, response: dlp.DlpJob) -> dlp.DlpJob:
        """Post-rpc interceptor for create_dlp_job

        DEPRECATED. Please use the `post_create_dlp_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_dlp_job` interceptor runs
        before the `post_create_dlp_job_with_metadata` interceptor.
        """
        return response

    def post_create_dlp_job_with_metadata(
        self, response: dlp.DlpJob, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[dlp.DlpJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_dlp_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_dlp_job_with_metadata`
        interceptor in new development instead of the `post_create_dlp_job` interceptor.
        When both interceptors are used, this `post_create_dlp_job_with_metadata` interceptor runs after the
        `post_create_dlp_job` interceptor. The (possibly modified) response returned by
        `post_create_dlp_job` will be passed to
        `post_create_dlp_job_with_metadata`.
        """
        return response, metadata

    def pre_create_inspect_template(
        self,
        request: dlp.CreateInspectTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.CreateInspectTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_inspect_template(
        self, response: dlp.InspectTemplate
    ) -> dlp.InspectTemplate:
        """Post-rpc interceptor for create_inspect_template

        DEPRECATED. Please use the `post_create_inspect_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_inspect_template` interceptor runs
        before the `post_create_inspect_template_with_metadata` interceptor.
        """
        return response

    def post_create_inspect_template_with_metadata(
        self,
        response: dlp.InspectTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.InspectTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_inspect_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_inspect_template_with_metadata`
        interceptor in new development instead of the `post_create_inspect_template` interceptor.
        When both interceptors are used, this `post_create_inspect_template_with_metadata` interceptor runs after the
        `post_create_inspect_template` interceptor. The (possibly modified) response returned by
        `post_create_inspect_template` will be passed to
        `post_create_inspect_template_with_metadata`.
        """
        return response, metadata

    def pre_create_job_trigger(
        self,
        request: dlp.CreateJobTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.CreateJobTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for create_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_job_trigger(self, response: dlp.JobTrigger) -> dlp.JobTrigger:
        """Post-rpc interceptor for create_job_trigger

        DEPRECATED. Please use the `post_create_job_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_job_trigger` interceptor runs
        before the `post_create_job_trigger_with_metadata` interceptor.
        """
        return response

    def post_create_job_trigger_with_metadata(
        self,
        response: dlp.JobTrigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.JobTrigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_job_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_job_trigger_with_metadata`
        interceptor in new development instead of the `post_create_job_trigger` interceptor.
        When both interceptors are used, this `post_create_job_trigger_with_metadata` interceptor runs after the
        `post_create_job_trigger` interceptor. The (possibly modified) response returned by
        `post_create_job_trigger` will be passed to
        `post_create_job_trigger_with_metadata`.
        """
        return response, metadata

    def pre_create_stored_info_type(
        self,
        request: dlp.CreateStoredInfoTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.CreateStoredInfoTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_create_stored_info_type(
        self, response: dlp.StoredInfoType
    ) -> dlp.StoredInfoType:
        """Post-rpc interceptor for create_stored_info_type

        DEPRECATED. Please use the `post_create_stored_info_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_create_stored_info_type` interceptor runs
        before the `post_create_stored_info_type_with_metadata` interceptor.
        """
        return response

    def post_create_stored_info_type_with_metadata(
        self,
        response: dlp.StoredInfoType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.StoredInfoType, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_stored_info_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_create_stored_info_type_with_metadata`
        interceptor in new development instead of the `post_create_stored_info_type` interceptor.
        When both interceptors are used, this `post_create_stored_info_type_with_metadata` interceptor runs after the
        `post_create_stored_info_type` interceptor. The (possibly modified) response returned by
        `post_create_stored_info_type` will be passed to
        `post_create_stored_info_type_with_metadata`.
        """
        return response, metadata

    def pre_deidentify_content(
        self,
        request: dlp.DeidentifyContentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeidentifyContentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for deidentify_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_deidentify_content(
        self, response: dlp.DeidentifyContentResponse
    ) -> dlp.DeidentifyContentResponse:
        """Post-rpc interceptor for deidentify_content

        DEPRECATED. Please use the `post_deidentify_content_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_deidentify_content` interceptor runs
        before the `post_deidentify_content_with_metadata` interceptor.
        """
        return response

    def post_deidentify_content_with_metadata(
        self,
        response: dlp.DeidentifyContentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeidentifyContentResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deidentify_content

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_deidentify_content_with_metadata`
        interceptor in new development instead of the `post_deidentify_content` interceptor.
        When both interceptors are used, this `post_deidentify_content_with_metadata` interceptor runs after the
        `post_deidentify_content` interceptor. The (possibly modified) response returned by
        `post_deidentify_content` will be passed to
        `post_deidentify_content_with_metadata`.
        """
        return response, metadata

    def pre_delete_connection(
        self,
        request: dlp.DeleteConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeleteConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_content_policy(
        self,
        request: dlp.DeleteContentPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeleteContentPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_content_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_deidentify_template(
        self,
        request: dlp.DeleteDeidentifyTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.DeleteDeidentifyTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_discovery_config(
        self,
        request: dlp.DeleteDiscoveryConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.DeleteDiscoveryConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_discovery_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_dlp_job(
        self,
        request: dlp.DeleteDlpJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeleteDlpJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_file_store_data_profile(
        self,
        request: dlp.DeleteFileStoreDataProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.DeleteFileStoreDataProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_file_store_data_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_inspect_template(
        self,
        request: dlp.DeleteInspectTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.DeleteInspectTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_job_trigger(
        self,
        request: dlp.DeleteJobTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeleteJobTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for delete_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_stored_info_type(
        self,
        request: dlp.DeleteStoredInfoTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.DeleteStoredInfoTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_delete_table_data_profile(
        self,
        request: dlp.DeleteTableDataProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.DeleteTableDataProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_table_data_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_finish_dlp_job(
        self,
        request: dlp.FinishDlpJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.FinishDlpJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for finish_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def pre_get_column_data_profile(
        self,
        request: dlp.GetColumnDataProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.GetColumnDataProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_column_data_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_column_data_profile(
        self, response: dlp.ColumnDataProfile
    ) -> dlp.ColumnDataProfile:
        """Post-rpc interceptor for get_column_data_profile

        DEPRECATED. Please use the `post_get_column_data_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_column_data_profile` interceptor runs
        before the `post_get_column_data_profile_with_metadata` interceptor.
        """
        return response

    def post_get_column_data_profile_with_metadata(
        self,
        response: dlp.ColumnDataProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ColumnDataProfile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_column_data_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_column_data_profile_with_metadata`
        interceptor in new development instead of the `post_get_column_data_profile` interceptor.
        When both interceptors are used, this `post_get_column_data_profile_with_metadata` interceptor runs after the
        `post_get_column_data_profile` interceptor. The (possibly modified) response returned by
        `post_get_column_data_profile` will be passed to
        `post_get_column_data_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_connection(
        self,
        request: dlp.GetConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_connection(self, response: dlp.Connection) -> dlp.Connection:
        """Post-rpc interceptor for get_connection

        DEPRECATED. Please use the `post_get_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_connection` interceptor runs
        before the `post_get_connection_with_metadata` interceptor.
        """
        return response

    def post_get_connection_with_metadata(
        self,
        response: dlp.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_connection_with_metadata`
        interceptor in new development instead of the `post_get_connection` interceptor.
        When both interceptors are used, this `post_get_connection_with_metadata` interceptor runs after the
        `post_get_connection` interceptor. The (possibly modified) response returned by
        `post_get_connection` will be passed to
        `post_get_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_content_policy(
        self,
        request: dlp.GetContentPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetContentPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_content_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_content_policy(self, response: dlp.ContentPolicy) -> dlp.ContentPolicy:
        """Post-rpc interceptor for get_content_policy

        DEPRECATED. Please use the `post_get_content_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_content_policy` interceptor runs
        before the `post_get_content_policy_with_metadata` interceptor.
        """
        return response

    def post_get_content_policy_with_metadata(
        self,
        response: dlp.ContentPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ContentPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_content_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_content_policy_with_metadata`
        interceptor in new development instead of the `post_get_content_policy` interceptor.
        When both interceptors are used, this `post_get_content_policy_with_metadata` interceptor runs after the
        `post_get_content_policy` interceptor. The (possibly modified) response returned by
        `post_get_content_policy` will be passed to
        `post_get_content_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_deidentify_template(
        self,
        request: dlp.GetDeidentifyTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.GetDeidentifyTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_deidentify_template(
        self, response: dlp.DeidentifyTemplate
    ) -> dlp.DeidentifyTemplate:
        """Post-rpc interceptor for get_deidentify_template

        DEPRECATED. Please use the `post_get_deidentify_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_deidentify_template` interceptor runs
        before the `post_get_deidentify_template_with_metadata` interceptor.
        """
        return response

    def post_get_deidentify_template_with_metadata(
        self,
        response: dlp.DeidentifyTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeidentifyTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_deidentify_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_deidentify_template_with_metadata`
        interceptor in new development instead of the `post_get_deidentify_template` interceptor.
        When both interceptors are used, this `post_get_deidentify_template_with_metadata` interceptor runs after the
        `post_get_deidentify_template` interceptor. The (possibly modified) response returned by
        `post_get_deidentify_template` will be passed to
        `post_get_deidentify_template_with_metadata`.
        """
        return response, metadata

    def pre_get_discovery_config(
        self,
        request: dlp.GetDiscoveryConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetDiscoveryConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_discovery_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_discovery_config(
        self, response: dlp.DiscoveryConfig
    ) -> dlp.DiscoveryConfig:
        """Post-rpc interceptor for get_discovery_config

        DEPRECATED. Please use the `post_get_discovery_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_discovery_config` interceptor runs
        before the `post_get_discovery_config_with_metadata` interceptor.
        """
        return response

    def post_get_discovery_config_with_metadata(
        self,
        response: dlp.DiscoveryConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DiscoveryConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_discovery_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_discovery_config_with_metadata`
        interceptor in new development instead of the `post_get_discovery_config` interceptor.
        When both interceptors are used, this `post_get_discovery_config_with_metadata` interceptor runs after the
        `post_get_discovery_config` interceptor. The (possibly modified) response returned by
        `post_get_discovery_config` will be passed to
        `post_get_discovery_config_with_metadata`.
        """
        return response, metadata

    def pre_get_dlp_job(
        self,
        request: dlp.GetDlpJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetDlpJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_dlp_job(self, response: dlp.DlpJob) -> dlp.DlpJob:
        """Post-rpc interceptor for get_dlp_job

        DEPRECATED. Please use the `post_get_dlp_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_dlp_job` interceptor runs
        before the `post_get_dlp_job_with_metadata` interceptor.
        """
        return response

    def post_get_dlp_job_with_metadata(
        self, response: dlp.DlpJob, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[dlp.DlpJob, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_dlp_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_dlp_job_with_metadata`
        interceptor in new development instead of the `post_get_dlp_job` interceptor.
        When both interceptors are used, this `post_get_dlp_job_with_metadata` interceptor runs after the
        `post_get_dlp_job` interceptor. The (possibly modified) response returned by
        `post_get_dlp_job` will be passed to
        `post_get_dlp_job_with_metadata`.
        """
        return response, metadata

    def pre_get_file_store_data_profile(
        self,
        request: dlp.GetFileStoreDataProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.GetFileStoreDataProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_file_store_data_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_file_store_data_profile(
        self, response: dlp.FileStoreDataProfile
    ) -> dlp.FileStoreDataProfile:
        """Post-rpc interceptor for get_file_store_data_profile

        DEPRECATED. Please use the `post_get_file_store_data_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_file_store_data_profile` interceptor runs
        before the `post_get_file_store_data_profile_with_metadata` interceptor.
        """
        return response

    def post_get_file_store_data_profile_with_metadata(
        self,
        response: dlp.FileStoreDataProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.FileStoreDataProfile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_file_store_data_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_file_store_data_profile_with_metadata`
        interceptor in new development instead of the `post_get_file_store_data_profile` interceptor.
        When both interceptors are used, this `post_get_file_store_data_profile_with_metadata` interceptor runs after the
        `post_get_file_store_data_profile` interceptor. The (possibly modified) response returned by
        `post_get_file_store_data_profile` will be passed to
        `post_get_file_store_data_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_inspect_template(
        self,
        request: dlp.GetInspectTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetInspectTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_inspect_template(
        self, response: dlp.InspectTemplate
    ) -> dlp.InspectTemplate:
        """Post-rpc interceptor for get_inspect_template

        DEPRECATED. Please use the `post_get_inspect_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_inspect_template` interceptor runs
        before the `post_get_inspect_template_with_metadata` interceptor.
        """
        return response

    def post_get_inspect_template_with_metadata(
        self,
        response: dlp.InspectTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.InspectTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_inspect_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_inspect_template_with_metadata`
        interceptor in new development instead of the `post_get_inspect_template` interceptor.
        When both interceptors are used, this `post_get_inspect_template_with_metadata` interceptor runs after the
        `post_get_inspect_template` interceptor. The (possibly modified) response returned by
        `post_get_inspect_template` will be passed to
        `post_get_inspect_template_with_metadata`.
        """
        return response, metadata

    def pre_get_job_trigger(
        self,
        request: dlp.GetJobTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetJobTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_job_trigger(self, response: dlp.JobTrigger) -> dlp.JobTrigger:
        """Post-rpc interceptor for get_job_trigger

        DEPRECATED. Please use the `post_get_job_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_job_trigger` interceptor runs
        before the `post_get_job_trigger_with_metadata` interceptor.
        """
        return response

    def post_get_job_trigger_with_metadata(
        self,
        response: dlp.JobTrigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.JobTrigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_job_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_job_trigger_with_metadata`
        interceptor in new development instead of the `post_get_job_trigger` interceptor.
        When both interceptors are used, this `post_get_job_trigger_with_metadata` interceptor runs after the
        `post_get_job_trigger` interceptor. The (possibly modified) response returned by
        `post_get_job_trigger` will be passed to
        `post_get_job_trigger_with_metadata`.
        """
        return response, metadata

    def pre_get_project_data_profile(
        self,
        request: dlp.GetProjectDataProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.GetProjectDataProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_project_data_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_project_data_profile(
        self, response: dlp.ProjectDataProfile
    ) -> dlp.ProjectDataProfile:
        """Post-rpc interceptor for get_project_data_profile

        DEPRECATED. Please use the `post_get_project_data_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_project_data_profile` interceptor runs
        before the `post_get_project_data_profile_with_metadata` interceptor.
        """
        return response

    def post_get_project_data_profile_with_metadata(
        self,
        response: dlp.ProjectDataProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ProjectDataProfile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_project_data_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_project_data_profile_with_metadata`
        interceptor in new development instead of the `post_get_project_data_profile` interceptor.
        When both interceptors are used, this `post_get_project_data_profile_with_metadata` interceptor runs after the
        `post_get_project_data_profile` interceptor. The (possibly modified) response returned by
        `post_get_project_data_profile` will be passed to
        `post_get_project_data_profile_with_metadata`.
        """
        return response, metadata

    def pre_get_stored_info_type(
        self,
        request: dlp.GetStoredInfoTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetStoredInfoTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_stored_info_type(
        self, response: dlp.StoredInfoType
    ) -> dlp.StoredInfoType:
        """Post-rpc interceptor for get_stored_info_type

        DEPRECATED. Please use the `post_get_stored_info_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_stored_info_type` interceptor runs
        before the `post_get_stored_info_type_with_metadata` interceptor.
        """
        return response

    def post_get_stored_info_type_with_metadata(
        self,
        response: dlp.StoredInfoType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.StoredInfoType, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_stored_info_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_stored_info_type_with_metadata`
        interceptor in new development instead of the `post_get_stored_info_type` interceptor.
        When both interceptors are used, this `post_get_stored_info_type_with_metadata` interceptor runs after the
        `post_get_stored_info_type` interceptor. The (possibly modified) response returned by
        `post_get_stored_info_type` will be passed to
        `post_get_stored_info_type_with_metadata`.
        """
        return response, metadata

    def pre_get_table_data_profile(
        self,
        request: dlp.GetTableDataProfileRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.GetTableDataProfileRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for get_table_data_profile

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_get_table_data_profile(
        self, response: dlp.TableDataProfile
    ) -> dlp.TableDataProfile:
        """Post-rpc interceptor for get_table_data_profile

        DEPRECATED. Please use the `post_get_table_data_profile_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_get_table_data_profile` interceptor runs
        before the `post_get_table_data_profile_with_metadata` interceptor.
        """
        return response

    def post_get_table_data_profile_with_metadata(
        self,
        response: dlp.TableDataProfile,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.TableDataProfile, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_table_data_profile

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_get_table_data_profile_with_metadata`
        interceptor in new development instead of the `post_get_table_data_profile` interceptor.
        When both interceptors are used, this `post_get_table_data_profile_with_metadata` interceptor runs after the
        `post_get_table_data_profile` interceptor. The (possibly modified) response returned by
        `post_get_table_data_profile` will be passed to
        `post_get_table_data_profile_with_metadata`.
        """
        return response, metadata

    def pre_hybrid_inspect_dlp_job(
        self,
        request: dlp.HybridInspectDlpJobRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.HybridInspectDlpJobRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for hybrid_inspect_dlp_job

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_hybrid_inspect_dlp_job(
        self, response: dlp.HybridInspectResponse
    ) -> dlp.HybridInspectResponse:
        """Post-rpc interceptor for hybrid_inspect_dlp_job

        DEPRECATED. Please use the `post_hybrid_inspect_dlp_job_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_hybrid_inspect_dlp_job` interceptor runs
        before the `post_hybrid_inspect_dlp_job_with_metadata` interceptor.
        """
        return response

    def post_hybrid_inspect_dlp_job_with_metadata(
        self,
        response: dlp.HybridInspectResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.HybridInspectResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for hybrid_inspect_dlp_job

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_hybrid_inspect_dlp_job_with_metadata`
        interceptor in new development instead of the `post_hybrid_inspect_dlp_job` interceptor.
        When both interceptors are used, this `post_hybrid_inspect_dlp_job_with_metadata` interceptor runs after the
        `post_hybrid_inspect_dlp_job` interceptor. The (possibly modified) response returned by
        `post_hybrid_inspect_dlp_job` will be passed to
        `post_hybrid_inspect_dlp_job_with_metadata`.
        """
        return response, metadata

    def pre_hybrid_inspect_job_trigger(
        self,
        request: dlp.HybridInspectJobTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.HybridInspectJobTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for hybrid_inspect_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_hybrid_inspect_job_trigger(
        self, response: dlp.HybridInspectResponse
    ) -> dlp.HybridInspectResponse:
        """Post-rpc interceptor for hybrid_inspect_job_trigger

        DEPRECATED. Please use the `post_hybrid_inspect_job_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_hybrid_inspect_job_trigger` interceptor runs
        before the `post_hybrid_inspect_job_trigger_with_metadata` interceptor.
        """
        return response

    def post_hybrid_inspect_job_trigger_with_metadata(
        self,
        response: dlp.HybridInspectResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.HybridInspectResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for hybrid_inspect_job_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_hybrid_inspect_job_trigger_with_metadata`
        interceptor in new development instead of the `post_hybrid_inspect_job_trigger` interceptor.
        When both interceptors are used, this `post_hybrid_inspect_job_trigger_with_metadata` interceptor runs after the
        `post_hybrid_inspect_job_trigger` interceptor. The (possibly modified) response returned by
        `post_hybrid_inspect_job_trigger` will be passed to
        `post_hybrid_inspect_job_trigger_with_metadata`.
        """
        return response, metadata

    def pre_inspect_content(
        self,
        request: dlp.InspectContentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.InspectContentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for inspect_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_inspect_content(
        self, response: dlp.InspectContentResponse
    ) -> dlp.InspectContentResponse:
        """Post-rpc interceptor for inspect_content

        DEPRECATED. Please use the `post_inspect_content_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_inspect_content` interceptor runs
        before the `post_inspect_content_with_metadata` interceptor.
        """
        return response

    def post_inspect_content_with_metadata(
        self,
        response: dlp.InspectContentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.InspectContentResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for inspect_content

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_inspect_content_with_metadata`
        interceptor in new development instead of the `post_inspect_content` interceptor.
        When both interceptors are used, this `post_inspect_content_with_metadata` interceptor runs after the
        `post_inspect_content` interceptor. The (possibly modified) response returned by
        `post_inspect_content` will be passed to
        `post_inspect_content_with_metadata`.
        """
        return response, metadata

    def pre_list_column_data_profiles(
        self,
        request: dlp.ListColumnDataProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListColumnDataProfilesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_column_data_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_column_data_profiles(
        self, response: dlp.ListColumnDataProfilesResponse
    ) -> dlp.ListColumnDataProfilesResponse:
        """Post-rpc interceptor for list_column_data_profiles

        DEPRECATED. Please use the `post_list_column_data_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_column_data_profiles` interceptor runs
        before the `post_list_column_data_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_column_data_profiles_with_metadata(
        self,
        response: dlp.ListColumnDataProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListColumnDataProfilesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_column_data_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_column_data_profiles_with_metadata`
        interceptor in new development instead of the `post_list_column_data_profiles` interceptor.
        When both interceptors are used, this `post_list_column_data_profiles_with_metadata` interceptor runs after the
        `post_list_column_data_profiles` interceptor. The (possibly modified) response returned by
        `post_list_column_data_profiles` will be passed to
        `post_list_column_data_profiles_with_metadata`.
        """
        return response, metadata

    def pre_list_connections(
        self,
        request: dlp.ListConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListConnectionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_connections(
        self, response: dlp.ListConnectionsResponse
    ) -> dlp.ListConnectionsResponse:
        """Post-rpc interceptor for list_connections

        DEPRECATED. Please use the `post_list_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_connections` interceptor runs
        before the `post_list_connections_with_metadata` interceptor.
        """
        return response

    def post_list_connections_with_metadata(
        self,
        response: dlp.ListConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListConnectionsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_connections_with_metadata`
        interceptor in new development instead of the `post_list_connections` interceptor.
        When both interceptors are used, this `post_list_connections_with_metadata` interceptor runs after the
        `post_list_connections` interceptor. The (possibly modified) response returned by
        `post_list_connections` will be passed to
        `post_list_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_content_policies(
        self,
        request: dlp.ListContentPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListContentPoliciesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_content_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_content_policies(
        self, response: dlp.ListContentPoliciesResponse
    ) -> dlp.ListContentPoliciesResponse:
        """Post-rpc interceptor for list_content_policies

        DEPRECATED. Please use the `post_list_content_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_content_policies` interceptor runs
        before the `post_list_content_policies_with_metadata` interceptor.
        """
        return response

    def post_list_content_policies_with_metadata(
        self,
        response: dlp.ListContentPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListContentPoliciesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_content_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_content_policies_with_metadata`
        interceptor in new development instead of the `post_list_content_policies` interceptor.
        When both interceptors are used, this `post_list_content_policies_with_metadata` interceptor runs after the
        `post_list_content_policies` interceptor. The (possibly modified) response returned by
        `post_list_content_policies` will be passed to
        `post_list_content_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_deidentify_templates(
        self,
        request: dlp.ListDeidentifyTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListDeidentifyTemplatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_deidentify_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_deidentify_templates(
        self, response: dlp.ListDeidentifyTemplatesResponse
    ) -> dlp.ListDeidentifyTemplatesResponse:
        """Post-rpc interceptor for list_deidentify_templates

        DEPRECATED. Please use the `post_list_deidentify_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_deidentify_templates` interceptor runs
        before the `post_list_deidentify_templates_with_metadata` interceptor.
        """
        return response

    def post_list_deidentify_templates_with_metadata(
        self,
        response: dlp.ListDeidentifyTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListDeidentifyTemplatesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_deidentify_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_deidentify_templates_with_metadata`
        interceptor in new development instead of the `post_list_deidentify_templates` interceptor.
        When both interceptors are used, this `post_list_deidentify_templates_with_metadata` interceptor runs after the
        `post_list_deidentify_templates` interceptor. The (possibly modified) response returned by
        `post_list_deidentify_templates` will be passed to
        `post_list_deidentify_templates_with_metadata`.
        """
        return response, metadata

    def pre_list_discovery_configs(
        self,
        request: dlp.ListDiscoveryConfigsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListDiscoveryConfigsRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_discovery_configs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_discovery_configs(
        self, response: dlp.ListDiscoveryConfigsResponse
    ) -> dlp.ListDiscoveryConfigsResponse:
        """Post-rpc interceptor for list_discovery_configs

        DEPRECATED. Please use the `post_list_discovery_configs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_discovery_configs` interceptor runs
        before the `post_list_discovery_configs_with_metadata` interceptor.
        """
        return response

    def post_list_discovery_configs_with_metadata(
        self,
        response: dlp.ListDiscoveryConfigsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListDiscoveryConfigsResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_discovery_configs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_discovery_configs_with_metadata`
        interceptor in new development instead of the `post_list_discovery_configs` interceptor.
        When both interceptors are used, this `post_list_discovery_configs_with_metadata` interceptor runs after the
        `post_list_discovery_configs` interceptor. The (possibly modified) response returned by
        `post_list_discovery_configs` will be passed to
        `post_list_discovery_configs_with_metadata`.
        """
        return response, metadata

    def pre_list_dlp_jobs(
        self,
        request: dlp.ListDlpJobsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListDlpJobsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_dlp_jobs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_dlp_jobs(
        self, response: dlp.ListDlpJobsResponse
    ) -> dlp.ListDlpJobsResponse:
        """Post-rpc interceptor for list_dlp_jobs

        DEPRECATED. Please use the `post_list_dlp_jobs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_dlp_jobs` interceptor runs
        before the `post_list_dlp_jobs_with_metadata` interceptor.
        """
        return response

    def post_list_dlp_jobs_with_metadata(
        self,
        response: dlp.ListDlpJobsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListDlpJobsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_dlp_jobs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_dlp_jobs_with_metadata`
        interceptor in new development instead of the `post_list_dlp_jobs` interceptor.
        When both interceptors are used, this `post_list_dlp_jobs_with_metadata` interceptor runs after the
        `post_list_dlp_jobs` interceptor. The (possibly modified) response returned by
        `post_list_dlp_jobs` will be passed to
        `post_list_dlp_jobs_with_metadata`.
        """
        return response, metadata

    def pre_list_file_store_data_profiles(
        self,
        request: dlp.ListFileStoreDataProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListFileStoreDataProfilesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_file_store_data_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_file_store_data_profiles(
        self, response: dlp.ListFileStoreDataProfilesResponse
    ) -> dlp.ListFileStoreDataProfilesResponse:
        """Post-rpc interceptor for list_file_store_data_profiles

        DEPRECATED. Please use the `post_list_file_store_data_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_file_store_data_profiles` interceptor runs
        before the `post_list_file_store_data_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_file_store_data_profiles_with_metadata(
        self,
        response: dlp.ListFileStoreDataProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListFileStoreDataProfilesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_file_store_data_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_file_store_data_profiles_with_metadata`
        interceptor in new development instead of the `post_list_file_store_data_profiles` interceptor.
        When both interceptors are used, this `post_list_file_store_data_profiles_with_metadata` interceptor runs after the
        `post_list_file_store_data_profiles` interceptor. The (possibly modified) response returned by
        `post_list_file_store_data_profiles` will be passed to
        `post_list_file_store_data_profiles_with_metadata`.
        """
        return response, metadata

    def pre_list_info_types(
        self,
        request: dlp.ListInfoTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListInfoTypesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_info_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_info_types(
        self, response: dlp.ListInfoTypesResponse
    ) -> dlp.ListInfoTypesResponse:
        """Post-rpc interceptor for list_info_types

        DEPRECATED. Please use the `post_list_info_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_info_types` interceptor runs
        before the `post_list_info_types_with_metadata` interceptor.
        """
        return response

    def post_list_info_types_with_metadata(
        self,
        response: dlp.ListInfoTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListInfoTypesResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_info_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_info_types_with_metadata`
        interceptor in new development instead of the `post_list_info_types` interceptor.
        When both interceptors are used, this `post_list_info_types_with_metadata` interceptor runs after the
        `post_list_info_types` interceptor. The (possibly modified) response returned by
        `post_list_info_types` will be passed to
        `post_list_info_types_with_metadata`.
        """
        return response, metadata

    def pre_list_inspect_templates(
        self,
        request: dlp.ListInspectTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListInspectTemplatesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_inspect_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_inspect_templates(
        self, response: dlp.ListInspectTemplatesResponse
    ) -> dlp.ListInspectTemplatesResponse:
        """Post-rpc interceptor for list_inspect_templates

        DEPRECATED. Please use the `post_list_inspect_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_inspect_templates` interceptor runs
        before the `post_list_inspect_templates_with_metadata` interceptor.
        """
        return response

    def post_list_inspect_templates_with_metadata(
        self,
        response: dlp.ListInspectTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListInspectTemplatesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_inspect_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_inspect_templates_with_metadata`
        interceptor in new development instead of the `post_list_inspect_templates` interceptor.
        When both interceptors are used, this `post_list_inspect_templates_with_metadata` interceptor runs after the
        `post_list_inspect_templates` interceptor. The (possibly modified) response returned by
        `post_list_inspect_templates` will be passed to
        `post_list_inspect_templates_with_metadata`.
        """
        return response, metadata

    def pre_list_job_triggers(
        self,
        request: dlp.ListJobTriggersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListJobTriggersRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_job_triggers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_job_triggers(
        self, response: dlp.ListJobTriggersResponse
    ) -> dlp.ListJobTriggersResponse:
        """Post-rpc interceptor for list_job_triggers

        DEPRECATED. Please use the `post_list_job_triggers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_job_triggers` interceptor runs
        before the `post_list_job_triggers_with_metadata` interceptor.
        """
        return response

    def post_list_job_triggers_with_metadata(
        self,
        response: dlp.ListJobTriggersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListJobTriggersResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for list_job_triggers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_job_triggers_with_metadata`
        interceptor in new development instead of the `post_list_job_triggers` interceptor.
        When both interceptors are used, this `post_list_job_triggers_with_metadata` interceptor runs after the
        `post_list_job_triggers` interceptor. The (possibly modified) response returned by
        `post_list_job_triggers` will be passed to
        `post_list_job_triggers_with_metadata`.
        """
        return response, metadata

    def pre_list_project_data_profiles(
        self,
        request: dlp.ListProjectDataProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListProjectDataProfilesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_project_data_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_project_data_profiles(
        self, response: dlp.ListProjectDataProfilesResponse
    ) -> dlp.ListProjectDataProfilesResponse:
        """Post-rpc interceptor for list_project_data_profiles

        DEPRECATED. Please use the `post_list_project_data_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_project_data_profiles` interceptor runs
        before the `post_list_project_data_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_project_data_profiles_with_metadata(
        self,
        response: dlp.ListProjectDataProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListProjectDataProfilesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_project_data_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_project_data_profiles_with_metadata`
        interceptor in new development instead of the `post_list_project_data_profiles` interceptor.
        When both interceptors are used, this `post_list_project_data_profiles_with_metadata` interceptor runs after the
        `post_list_project_data_profiles` interceptor. The (possibly modified) response returned by
        `post_list_project_data_profiles` will be passed to
        `post_list_project_data_profiles_with_metadata`.
        """
        return response, metadata

    def pre_list_stored_info_types(
        self,
        request: dlp.ListStoredInfoTypesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ListStoredInfoTypesRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for list_stored_info_types

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_stored_info_types(
        self, response: dlp.ListStoredInfoTypesResponse
    ) -> dlp.ListStoredInfoTypesResponse:
        """Post-rpc interceptor for list_stored_info_types

        DEPRECATED. Please use the `post_list_stored_info_types_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_stored_info_types` interceptor runs
        before the `post_list_stored_info_types_with_metadata` interceptor.
        """
        return response

    def post_list_stored_info_types_with_metadata(
        self,
        response: dlp.ListStoredInfoTypesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListStoredInfoTypesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_stored_info_types

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_stored_info_types_with_metadata`
        interceptor in new development instead of the `post_list_stored_info_types` interceptor.
        When both interceptors are used, this `post_list_stored_info_types_with_metadata` interceptor runs after the
        `post_list_stored_info_types` interceptor. The (possibly modified) response returned by
        `post_list_stored_info_types` will be passed to
        `post_list_stored_info_types_with_metadata`.
        """
        return response, metadata

    def pre_list_table_data_profiles(
        self,
        request: dlp.ListTableDataProfilesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListTableDataProfilesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_table_data_profiles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_list_table_data_profiles(
        self, response: dlp.ListTableDataProfilesResponse
    ) -> dlp.ListTableDataProfilesResponse:
        """Post-rpc interceptor for list_table_data_profiles

        DEPRECATED. Please use the `post_list_table_data_profiles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_list_table_data_profiles` interceptor runs
        before the `post_list_table_data_profiles_with_metadata` interceptor.
        """
        return response

    def post_list_table_data_profiles_with_metadata(
        self,
        response: dlp.ListTableDataProfilesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.ListTableDataProfilesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_table_data_profiles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_list_table_data_profiles_with_metadata`
        interceptor in new development instead of the `post_list_table_data_profiles` interceptor.
        When both interceptors are used, this `post_list_table_data_profiles_with_metadata` interceptor runs after the
        `post_list_table_data_profiles` interceptor. The (possibly modified) response returned by
        `post_list_table_data_profiles` will be passed to
        `post_list_table_data_profiles_with_metadata`.
        """
        return response, metadata

    def pre_redact_image(
        self,
        request: dlp.RedactImageRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.RedactImageRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for redact_image

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_redact_image(
        self, response: dlp.RedactImageResponse
    ) -> dlp.RedactImageResponse:
        """Post-rpc interceptor for redact_image

        DEPRECATED. Please use the `post_redact_image_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_redact_image` interceptor runs
        before the `post_redact_image_with_metadata` interceptor.
        """
        return response

    def post_redact_image_with_metadata(
        self,
        response: dlp.RedactImageResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.RedactImageResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for redact_image

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_redact_image_with_metadata`
        interceptor in new development instead of the `post_redact_image` interceptor.
        When both interceptors are used, this `post_redact_image_with_metadata` interceptor runs after the
        `post_redact_image` interceptor. The (possibly modified) response returned by
        `post_redact_image` will be passed to
        `post_redact_image_with_metadata`.
        """
        return response, metadata

    def pre_reidentify_content(
        self,
        request: dlp.ReidentifyContentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ReidentifyContentRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for reidentify_content

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_reidentify_content(
        self, response: dlp.ReidentifyContentResponse
    ) -> dlp.ReidentifyContentResponse:
        """Post-rpc interceptor for reidentify_content

        DEPRECATED. Please use the `post_reidentify_content_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_reidentify_content` interceptor runs
        before the `post_reidentify_content_with_metadata` interceptor.
        """
        return response

    def post_reidentify_content_with_metadata(
        self,
        response: dlp.ReidentifyContentResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ReidentifyContentResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for reidentify_content

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_reidentify_content_with_metadata`
        interceptor in new development instead of the `post_reidentify_content` interceptor.
        When both interceptors are used, this `post_reidentify_content_with_metadata` interceptor runs after the
        `post_reidentify_content` interceptor. The (possibly modified) response returned by
        `post_reidentify_content` will be passed to
        `post_reidentify_content_with_metadata`.
        """
        return response, metadata

    def pre_search_connections(
        self,
        request: dlp.SearchConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.SearchConnectionsRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for search_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_search_connections(
        self, response: dlp.SearchConnectionsResponse
    ) -> dlp.SearchConnectionsResponse:
        """Post-rpc interceptor for search_connections

        DEPRECATED. Please use the `post_search_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_search_connections` interceptor runs
        before the `post_search_connections_with_metadata` interceptor.
        """
        return response

    def post_search_connections_with_metadata(
        self,
        response: dlp.SearchConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.SearchConnectionsResponse, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for search_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_search_connections_with_metadata`
        interceptor in new development instead of the `post_search_connections` interceptor.
        When both interceptors are used, this `post_search_connections_with_metadata` interceptor runs after the
        `post_search_connections` interceptor. The (possibly modified) response returned by
        `post_search_connections` will be passed to
        `post_search_connections_with_metadata`.
        """
        return response, metadata

    def pre_update_connection(
        self,
        request: dlp.UpdateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.UpdateConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_connection(self, response: dlp.Connection) -> dlp.Connection:
        """Post-rpc interceptor for update_connection

        DEPRECATED. Please use the `post_update_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_connection` interceptor runs
        before the `post_update_connection_with_metadata` interceptor.
        """
        return response

    def post_update_connection_with_metadata(
        self,
        response: dlp.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_connection_with_metadata`
        interceptor in new development instead of the `post_update_connection` interceptor.
        When both interceptors are used, this `post_update_connection_with_metadata` interceptor runs after the
        `post_update_connection` interceptor. The (possibly modified) response returned by
        `post_update_connection` will be passed to
        `post_update_connection_with_metadata`.
        """
        return response, metadata

    def pre_update_content_policy(
        self,
        request: dlp.UpdateContentPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.UpdateContentPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_content_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_content_policy(
        self, response: dlp.ContentPolicy
    ) -> dlp.ContentPolicy:
        """Post-rpc interceptor for update_content_policy

        DEPRECATED. Please use the `post_update_content_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_content_policy` interceptor runs
        before the `post_update_content_policy_with_metadata` interceptor.
        """
        return response

    def post_update_content_policy_with_metadata(
        self,
        response: dlp.ContentPolicy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.ContentPolicy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_content_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_content_policy_with_metadata`
        interceptor in new development instead of the `post_update_content_policy` interceptor.
        When both interceptors are used, this `post_update_content_policy_with_metadata` interceptor runs after the
        `post_update_content_policy` interceptor. The (possibly modified) response returned by
        `post_update_content_policy` will be passed to
        `post_update_content_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_deidentify_template(
        self,
        request: dlp.UpdateDeidentifyTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.UpdateDeidentifyTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_deidentify_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_deidentify_template(
        self, response: dlp.DeidentifyTemplate
    ) -> dlp.DeidentifyTemplate:
        """Post-rpc interceptor for update_deidentify_template

        DEPRECATED. Please use the `post_update_deidentify_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_deidentify_template` interceptor runs
        before the `post_update_deidentify_template_with_metadata` interceptor.
        """
        return response

    def post_update_deidentify_template_with_metadata(
        self,
        response: dlp.DeidentifyTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DeidentifyTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_deidentify_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_deidentify_template_with_metadata`
        interceptor in new development instead of the `post_update_deidentify_template` interceptor.
        When both interceptors are used, this `post_update_deidentify_template_with_metadata` interceptor runs after the
        `post_update_deidentify_template` interceptor. The (possibly modified) response returned by
        `post_update_deidentify_template` will be passed to
        `post_update_deidentify_template_with_metadata`.
        """
        return response, metadata

    def pre_update_discovery_config(
        self,
        request: dlp.UpdateDiscoveryConfigRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.UpdateDiscoveryConfigRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_discovery_config

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_discovery_config(
        self, response: dlp.DiscoveryConfig
    ) -> dlp.DiscoveryConfig:
        """Post-rpc interceptor for update_discovery_config

        DEPRECATED. Please use the `post_update_discovery_config_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_discovery_config` interceptor runs
        before the `post_update_discovery_config_with_metadata` interceptor.
        """
        return response

    def post_update_discovery_config_with_metadata(
        self,
        response: dlp.DiscoveryConfig,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.DiscoveryConfig, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_discovery_config

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_discovery_config_with_metadata`
        interceptor in new development instead of the `post_update_discovery_config` interceptor.
        When both interceptors are used, this `post_update_discovery_config_with_metadata` interceptor runs after the
        `post_update_discovery_config` interceptor. The (possibly modified) response returned by
        `post_update_discovery_config` will be passed to
        `post_update_discovery_config_with_metadata`.
        """
        return response, metadata

    def pre_update_inspect_template(
        self,
        request: dlp.UpdateInspectTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.UpdateInspectTemplateRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_inspect_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_inspect_template(
        self, response: dlp.InspectTemplate
    ) -> dlp.InspectTemplate:
        """Post-rpc interceptor for update_inspect_template

        DEPRECATED. Please use the `post_update_inspect_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_inspect_template` interceptor runs
        before the `post_update_inspect_template_with_metadata` interceptor.
        """
        return response

    def post_update_inspect_template_with_metadata(
        self,
        response: dlp.InspectTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.InspectTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_inspect_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_inspect_template_with_metadata`
        interceptor in new development instead of the `post_update_inspect_template` interceptor.
        When both interceptors are used, this `post_update_inspect_template_with_metadata` interceptor runs after the
        `post_update_inspect_template` interceptor. The (possibly modified) response returned by
        `post_update_inspect_template` will be passed to
        `post_update_inspect_template_with_metadata`.
        """
        return response, metadata

    def pre_update_job_trigger(
        self,
        request: dlp.UpdateJobTriggerRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.UpdateJobTriggerRequest, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Pre-rpc interceptor for update_job_trigger

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_job_trigger(self, response: dlp.JobTrigger) -> dlp.JobTrigger:
        """Post-rpc interceptor for update_job_trigger

        DEPRECATED. Please use the `post_update_job_trigger_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_job_trigger` interceptor runs
        before the `post_update_job_trigger_with_metadata` interceptor.
        """
        return response

    def post_update_job_trigger_with_metadata(
        self,
        response: dlp.JobTrigger,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.JobTrigger, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_job_trigger

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_job_trigger_with_metadata`
        interceptor in new development instead of the `post_update_job_trigger` interceptor.
        When both interceptors are used, this `post_update_job_trigger_with_metadata` interceptor runs after the
        `post_update_job_trigger` interceptor. The (possibly modified) response returned by
        `post_update_job_trigger` will be passed to
        `post_update_job_trigger_with_metadata`.
        """
        return response, metadata

    def pre_update_stored_info_type(
        self,
        request: dlp.UpdateStoredInfoTypeRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        dlp.UpdateStoredInfoTypeRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for update_stored_info_type

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DlpService server.
        """
        return request, metadata

    def post_update_stored_info_type(
        self, response: dlp.StoredInfoType
    ) -> dlp.StoredInfoType:
        """Post-rpc interceptor for update_stored_info_type

        DEPRECATED. Please use the `post_update_stored_info_type_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DlpService server but before
        it is returned to user code. This `post_update_stored_info_type` interceptor runs
        before the `post_update_stored_info_type_with_metadata` interceptor.
        """
        return response

    def post_update_stored_info_type_with_metadata(
        self,
        response: dlp.StoredInfoType,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[dlp.StoredInfoType, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_stored_info_type

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DlpService server but before it is returned to user code.

        We recommend only using this `post_update_stored_info_type_with_metadata`
        interceptor in new development instead of the `post_update_stored_info_type` interceptor.
        When both interceptors are used, this `post_update_stored_info_type_with_metadata` interceptor runs after the
        `post_update_stored_info_type` interceptor. The (possibly modified) response returned by
        `post_update_stored_info_type` will be passed to
        `post_update_stored_info_type_with_metadata`.
        """
        return response, metadata


@dataclasses.dataclass
class DlpServiceRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DlpServiceRestInterceptor


class DlpServiceRestTransport(_BaseDlpServiceRestTransport):
    """REST backend synchronous transport for DlpService.

    Sensitive Data Protection provides access to a powerful
    sensitive data inspection, classification, and de-identification
    platform that works on text, images, and Google Cloud storage
    repositories. To learn more about concepts and find how-to
    guides see
    https://docs.cloud.google.com/sensitive-data-protection/docs/.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "dlp.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DlpServiceRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'dlp.googleapis.com').
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
            interceptor (Optional[DlpServiceRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or DlpServiceRestInterceptor()
        self._prep_wrapped_messages(client_info)

    class _ActivateJobTrigger(
        _BaseDlpServiceRestTransport._BaseActivateJobTrigger, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ActivateJobTrigger")

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
            request: dlp.ActivateJobTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DlpJob:
            r"""Call the activate job trigger method over HTTP.

            Args:
                request (~.dlp.ActivateJobTriggerRequest):
                    The request object. Request message for
                ActivateJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DlpJob:
                    Combines all of the information about
                a DLP job.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseActivateJobTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_activate_job_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseActivateJobTrigger,
                    "_BaseActivateJobTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ActivateJobTrigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ActivateJobTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ActivateJobTrigger._get_response(
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
            resp = dlp.DlpJob()
            pb_resp = dlp.DlpJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_activate_job_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_activate_job_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DlpJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.activate_job_trigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ActivateJobTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CancelDlpJob(
        _BaseDlpServiceRestTransport._BaseCancelDlpJob, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CancelDlpJob")

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
            request: dlp.CancelDlpJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the cancel dlp job method over HTTP.

            Args:
                request (~.dlp.CancelDlpJobRequest):
                    The request object. The request message for canceling a
                DLP job.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseCancelDlpJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_dlp_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCancelDlpJob,
                    "_BaseCancelDlpJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CancelDlpJob",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CancelDlpJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CancelDlpJob._get_response(
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

    class _CreateConnection(
        _BaseDlpServiceRestTransport._BaseCreateConnection, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateConnection")

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
            request: dlp.CreateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.Connection:
            r"""Call the create connection method over HTTP.

            Args:
                request (~.dlp.CreateConnectionRequest):
                    The request object. Request message for CreateConnection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.Connection:
                    A data connection to allow the DLP
                API to profile data in locations that
                require additional configuration.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseCreateConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateConnection,
                    "_BaseCreateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateConnection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateConnection._get_response(
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
            resp = dlp.Connection()
            pb_resp = dlp.Connection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_connection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateContentPolicy(
        _BaseDlpServiceRestTransport._BaseCreateContentPolicy, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateContentPolicy")

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
            request: dlp.CreateContentPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ContentPolicy:
            r"""Call the create content policy method over HTTP.

            Args:
                request (~.dlp.CreateContentPolicyRequest):
                    The request object. Request message for
                CreateContentPolicy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ContentPolicy:
                    A policy to apply to content based on
                its inspection findings.

            """

            http_options = _BaseDlpServiceRestTransport._BaseCreateContentPolicy._get_http_options()
            request, metadata = self._interceptor.pre_create_content_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateContentPolicy,
                    "_BaseCreateContentPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateContentPolicy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateContentPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateContentPolicy._get_response(
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
            resp = dlp.ContentPolicy()
            pb_resp = dlp.ContentPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_content_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_content_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ContentPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_content_policy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateContentPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDeidentifyTemplate(
        _BaseDlpServiceRestTransport._BaseCreateDeidentifyTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateDeidentifyTemplate")

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
            request: dlp.CreateDeidentifyTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DeidentifyTemplate:
            r"""Call the create deidentify
            template method over HTTP.

                Args:
                    request (~.dlp.CreateDeidentifyTemplateRequest):
                        The request object. Request message for
                    CreateDeidentifyTemplate.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dlp.DeidentifyTemplate:
                        DeidentifyTemplates contains
                    instructions on how to de-identify
                    content. See
                    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
                    to learn more.

            """

            http_options = _BaseDlpServiceRestTransport._BaseCreateDeidentifyTemplate._get_http_options()
            request, metadata = self._interceptor.pre_create_deidentify_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateDeidentifyTemplate,
                    "_BaseCreateDeidentifyTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateDeidentifyTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateDeidentifyTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateDeidentifyTemplate._get_response(
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
            resp = dlp.DeidentifyTemplate()
            pb_resp = dlp.DeidentifyTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_deidentify_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_deidentify_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DeidentifyTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_deidentify_template",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateDeidentifyTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDiscoveryConfig(
        _BaseDlpServiceRestTransport._BaseCreateDiscoveryConfig, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateDiscoveryConfig")

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
            request: dlp.CreateDiscoveryConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DiscoveryConfig:
            r"""Call the create discovery config method over HTTP.

            Args:
                request (~.dlp.CreateDiscoveryConfigRequest):
                    The request object. Request message for
                CreateDiscoveryConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DiscoveryConfig:
                    Configuration for discovery to scan resources for
                profile generation. Only one discovery configuration may
                exist per organization, folder, or project.

                The generated data profiles are retained according to
                the [data retention policy]
                (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

            """

            http_options = _BaseDlpServiceRestTransport._BaseCreateDiscoveryConfig._get_http_options()
            request, metadata = self._interceptor.pre_create_discovery_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateDiscoveryConfig,
                    "_BaseCreateDiscoveryConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateDiscoveryConfig",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateDiscoveryConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateDiscoveryConfig._get_response(
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
            resp = dlp.DiscoveryConfig()
            pb_resp = dlp.DiscoveryConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_discovery_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_discovery_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DiscoveryConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_discovery_config",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateDiscoveryConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateDlpJob(
        _BaseDlpServiceRestTransport._BaseCreateDlpJob, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateDlpJob")

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
            request: dlp.CreateDlpJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DlpJob:
            r"""Call the create dlp job method over HTTP.

            Args:
                request (~.dlp.CreateDlpJobRequest):
                    The request object. Request message for
                CreateDlpJobRequest. Used to initiate
                long running jobs such as calculating
                risk metrics or inspecting Google Cloud
                Storage.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DlpJob:
                    Combines all of the information about
                a DLP job.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseCreateDlpJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_dlp_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateDlpJob,
                    "_BaseCreateDlpJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateDlpJob",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateDlpJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateDlpJob._get_response(
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
            resp = dlp.DlpJob()
            pb_resp = dlp.DlpJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_dlp_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_dlp_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DlpJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_dlp_job",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateDlpJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateInspectTemplate(
        _BaseDlpServiceRestTransport._BaseCreateInspectTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateInspectTemplate")

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
            request: dlp.CreateInspectTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.InspectTemplate:
            r"""Call the create inspect template method over HTTP.

            Args:
                request (~.dlp.CreateInspectTemplateRequest):
                    The request object. Request message for
                CreateInspectTemplate.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.InspectTemplate:
                    The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
                to learn more.

            """

            http_options = _BaseDlpServiceRestTransport._BaseCreateInspectTemplate._get_http_options()
            request, metadata = self._interceptor.pre_create_inspect_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateInspectTemplate,
                    "_BaseCreateInspectTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateInspectTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateInspectTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateInspectTemplate._get_response(
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
            resp = dlp.InspectTemplate()
            pb_resp = dlp.InspectTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_inspect_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_inspect_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.InspectTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_inspect_template",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateInspectTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateJobTrigger(
        _BaseDlpServiceRestTransport._BaseCreateJobTrigger, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateJobTrigger")

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
            request: dlp.CreateJobTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.JobTrigger:
            r"""Call the create job trigger method over HTTP.

            Args:
                request (~.dlp.CreateJobTriggerRequest):
                    The request object. Request message for CreateJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.JobTrigger:
                    Contains a configuration to make API
                calls on a repeating basis. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers
                to learn more.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseCreateJobTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_job_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateJobTrigger,
                    "_BaseCreateJobTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateJobTrigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateJobTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateJobTrigger._get_response(
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
            resp = dlp.JobTrigger()
            pb_resp = dlp.JobTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_job_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_job_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.JobTrigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_job_trigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateJobTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateStoredInfoType(
        _BaseDlpServiceRestTransport._BaseCreateStoredInfoType, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.CreateStoredInfoType")

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
            request: dlp.CreateStoredInfoTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.StoredInfoType:
            r"""Call the create stored info type method over HTTP.

            Args:
                request (~.dlp.CreateStoredInfoTypeRequest):
                    The request object. Request message for
                CreateStoredInfoType.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.StoredInfoType:
                    StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

            """

            http_options = _BaseDlpServiceRestTransport._BaseCreateStoredInfoType._get_http_options()
            request, metadata = self._interceptor.pre_create_stored_info_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseCreateStoredInfoType,
                    "_BaseCreateStoredInfoType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.CreateStoredInfoType",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateStoredInfoType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._CreateStoredInfoType._get_response(
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
            resp = dlp.StoredInfoType()
            pb_resp = dlp.StoredInfoType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_stored_info_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_stored_info_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.StoredInfoType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.create_stored_info_type",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "CreateStoredInfoType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeidentifyContent(
        _BaseDlpServiceRestTransport._BaseDeidentifyContent, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeidentifyContent")

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
            request: dlp.DeidentifyContentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DeidentifyContentResponse:
            r"""Call the deidentify content method over HTTP.

            Args:
                request (~.dlp.DeidentifyContentRequest):
                    The request object. Request to de-identify a ContentItem.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DeidentifyContentResponse:
                    Results of de-identifying a
                ContentItem.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseDeidentifyContent._get_http_options()
            )
            request, metadata = self._interceptor.pre_deidentify_content(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeidentifyContent,
                    "_BaseDeidentifyContent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeidentifyContent",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeidentifyContent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeidentifyContent._get_response(
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
            resp = dlp.DeidentifyContentResponse()
            pb_resp = dlp.DeidentifyContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_deidentify_content(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deidentify_content_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DeidentifyContentResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.deidentify_content",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeidentifyContent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteConnection(
        _BaseDlpServiceRestTransport._BaseDeleteConnection, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteConnection")

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
            request: dlp.DeleteConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete connection method over HTTP.

            Args:
                request (~.dlp.DeleteConnectionRequest):
                    The request object. Request message for DeleteConnection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseDeleteConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteConnection,
                    "_BaseDeleteConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteConnection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteConnection._get_response(
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

    class _DeleteContentPolicy(
        _BaseDlpServiceRestTransport._BaseDeleteContentPolicy, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteContentPolicy")

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
            request: dlp.DeleteContentPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete content policy method over HTTP.

            Args:
                request (~.dlp.DeleteContentPolicyRequest):
                    The request object. Request message for
                DeleteContentPolicy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteContentPolicy._get_http_options()
            request, metadata = self._interceptor.pre_delete_content_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteContentPolicy,
                    "_BaseDeleteContentPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteContentPolicy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteContentPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteContentPolicy._get_response(
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

    class _DeleteDeidentifyTemplate(
        _BaseDlpServiceRestTransport._BaseDeleteDeidentifyTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteDeidentifyTemplate")

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
            request: dlp.DeleteDeidentifyTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete deidentify
            template method over HTTP.

                Args:
                    request (~.dlp.DeleteDeidentifyTemplateRequest):
                        The request object. Request message for
                    DeleteDeidentifyTemplate.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteDeidentifyTemplate._get_http_options()
            request, metadata = self._interceptor.pre_delete_deidentify_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteDeidentifyTemplate,
                    "_BaseDeleteDeidentifyTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteDeidentifyTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteDeidentifyTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteDeidentifyTemplate._get_response(
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

    class _DeleteDiscoveryConfig(
        _BaseDlpServiceRestTransport._BaseDeleteDiscoveryConfig, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteDiscoveryConfig")

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
            request: dlp.DeleteDiscoveryConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete discovery config method over HTTP.

            Args:
                request (~.dlp.DeleteDiscoveryConfigRequest):
                    The request object. Request message for
                DeleteDiscoveryConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteDiscoveryConfig._get_http_options()
            request, metadata = self._interceptor.pre_delete_discovery_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteDiscoveryConfig,
                    "_BaseDeleteDiscoveryConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteDiscoveryConfig",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteDiscoveryConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteDiscoveryConfig._get_response(
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

    class _DeleteDlpJob(
        _BaseDlpServiceRestTransport._BaseDeleteDlpJob, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteDlpJob")

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
            request: dlp.DeleteDlpJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete dlp job method over HTTP.

            Args:
                request (~.dlp.DeleteDlpJobRequest):
                    The request object. The request message for deleting a
                DLP job.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseDeleteDlpJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_dlp_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteDlpJob,
                    "_BaseDeleteDlpJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteDlpJob",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteDlpJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteDlpJob._get_response(
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

    class _DeleteFileStoreDataProfile(
        _BaseDlpServiceRestTransport._BaseDeleteFileStoreDataProfile, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteFileStoreDataProfile")

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
            request: dlp.DeleteFileStoreDataProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete file store data
            profile method over HTTP.

                Args:
                    request (~.dlp.DeleteFileStoreDataProfileRequest):
                        The request object. Request message for
                    DeleteFileStoreProfile.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteFileStoreDataProfile._get_http_options()
            request, metadata = self._interceptor.pre_delete_file_store_data_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteFileStoreDataProfile,
                    "_BaseDeleteFileStoreDataProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteFileStoreDataProfile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteFileStoreDataProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DlpServiceRestTransport._DeleteFileStoreDataProfile._get_response(
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

    class _DeleteInspectTemplate(
        _BaseDlpServiceRestTransport._BaseDeleteInspectTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteInspectTemplate")

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
            request: dlp.DeleteInspectTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete inspect template method over HTTP.

            Args:
                request (~.dlp.DeleteInspectTemplateRequest):
                    The request object. Request message for
                DeleteInspectTemplate.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteInspectTemplate._get_http_options()
            request, metadata = self._interceptor.pre_delete_inspect_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteInspectTemplate,
                    "_BaseDeleteInspectTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteInspectTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteInspectTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteInspectTemplate._get_response(
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

    class _DeleteJobTrigger(
        _BaseDlpServiceRestTransport._BaseDeleteJobTrigger, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteJobTrigger")

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
            request: dlp.DeleteJobTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete job trigger method over HTTP.

            Args:
                request (~.dlp.DeleteJobTriggerRequest):
                    The request object. Request message for DeleteJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseDeleteJobTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_job_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteJobTrigger,
                    "_BaseDeleteJobTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteJobTrigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteJobTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteJobTrigger._get_response(
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

    class _DeleteStoredInfoType(
        _BaseDlpServiceRestTransport._BaseDeleteStoredInfoType, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteStoredInfoType")

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
            request: dlp.DeleteStoredInfoTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete stored info type method over HTTP.

            Args:
                request (~.dlp.DeleteStoredInfoTypeRequest):
                    The request object. Request message for
                DeleteStoredInfoType.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteStoredInfoType._get_http_options()
            request, metadata = self._interceptor.pre_delete_stored_info_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteStoredInfoType,
                    "_BaseDeleteStoredInfoType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteStoredInfoType",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteStoredInfoType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteStoredInfoType._get_response(
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

    class _DeleteTableDataProfile(
        _BaseDlpServiceRestTransport._BaseDeleteTableDataProfile, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.DeleteTableDataProfile")

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
            request: dlp.DeleteTableDataProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete table data profile method over HTTP.

            Args:
                request (~.dlp.DeleteTableDataProfileRequest):
                    The request object. Request message for
                DeleteTableProfile.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseDlpServiceRestTransport._BaseDeleteTableDataProfile._get_http_options()
            request, metadata = self._interceptor.pre_delete_table_data_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseDeleteTableDataProfile,
                    "_BaseDeleteTableDataProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.DeleteTableDataProfile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "DeleteTableDataProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._DeleteTableDataProfile._get_response(
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

    class _FinishDlpJob(
        _BaseDlpServiceRestTransport._BaseFinishDlpJob, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.FinishDlpJob")

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
            request: dlp.FinishDlpJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the finish dlp job method over HTTP.

            Args:
                request (~.dlp.FinishDlpJobRequest):
                    The request object. The request message for finishing a
                DLP hybrid job.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseFinishDlpJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_finish_dlp_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseFinishDlpJob,
                    "_BaseFinishDlpJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.FinishDlpJob",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "FinishDlpJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._FinishDlpJob._get_response(
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

    class _GetColumnDataProfile(
        _BaseDlpServiceRestTransport._BaseGetColumnDataProfile, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetColumnDataProfile")

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
            request: dlp.GetColumnDataProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ColumnDataProfile:
            r"""Call the get column data profile method over HTTP.

            Args:
                request (~.dlp.GetColumnDataProfileRequest):
                    The request object. Request to get a column data profile.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ColumnDataProfile:
                    The profile for a scanned column
                within a table.

            """

            http_options = _BaseDlpServiceRestTransport._BaseGetColumnDataProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_column_data_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetColumnDataProfile,
                    "_BaseGetColumnDataProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetColumnDataProfile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetColumnDataProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetColumnDataProfile._get_response(
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
            resp = dlp.ColumnDataProfile()
            pb_resp = dlp.ColumnDataProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_column_data_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_column_data_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ColumnDataProfile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_column_data_profile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetColumnDataProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnection(
        _BaseDlpServiceRestTransport._BaseGetConnection, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetConnection")

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
            request: dlp.GetConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.Connection:
            r"""Call the get connection method over HTTP.

            Args:
                request (~.dlp.GetConnectionRequest):
                    The request object. Request message for GetConnection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.Connection:
                    A data connection to allow the DLP
                API to profile data in locations that
                require additional configuration.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_connection(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetConnection,
                    "_BaseGetConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetConnection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetConnection._get_response(
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
            resp = dlp.Connection()
            pb_resp = dlp.Connection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_connection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetContentPolicy(
        _BaseDlpServiceRestTransport._BaseGetContentPolicy, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetContentPolicy")

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
            request: dlp.GetContentPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ContentPolicy:
            r"""Call the get content policy method over HTTP.

            Args:
                request (~.dlp.GetContentPolicyRequest):
                    The request object. Request message for GetContentPolicy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ContentPolicy:
                    A policy to apply to content based on
                its inspection findings.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetContentPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_content_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetContentPolicy,
                    "_BaseGetContentPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetContentPolicy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetContentPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetContentPolicy._get_response(
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
            resp = dlp.ContentPolicy()
            pb_resp = dlp.ContentPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_content_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_content_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ContentPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_content_policy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetContentPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDeidentifyTemplate(
        _BaseDlpServiceRestTransport._BaseGetDeidentifyTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetDeidentifyTemplate")

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
            request: dlp.GetDeidentifyTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DeidentifyTemplate:
            r"""Call the get deidentify template method over HTTP.

            Args:
                request (~.dlp.GetDeidentifyTemplateRequest):
                    The request object. Request message for
                GetDeidentifyTemplate.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DeidentifyTemplate:
                    DeidentifyTemplates contains
                instructions on how to de-identify
                content. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
                to learn more.

            """

            http_options = _BaseDlpServiceRestTransport._BaseGetDeidentifyTemplate._get_http_options()
            request, metadata = self._interceptor.pre_get_deidentify_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetDeidentifyTemplate,
                    "_BaseGetDeidentifyTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetDeidentifyTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetDeidentifyTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetDeidentifyTemplate._get_response(
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
            resp = dlp.DeidentifyTemplate()
            pb_resp = dlp.DeidentifyTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_deidentify_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_deidentify_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DeidentifyTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_deidentify_template",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetDeidentifyTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDiscoveryConfig(
        _BaseDlpServiceRestTransport._BaseGetDiscoveryConfig, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetDiscoveryConfig")

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
            request: dlp.GetDiscoveryConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DiscoveryConfig:
            r"""Call the get discovery config method over HTTP.

            Args:
                request (~.dlp.GetDiscoveryConfigRequest):
                    The request object. Request message for
                GetDiscoveryConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DiscoveryConfig:
                    Configuration for discovery to scan resources for
                profile generation. Only one discovery configuration may
                exist per organization, folder, or project.

                The generated data profiles are retained according to
                the [data retention policy]
                (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetDiscoveryConfig._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_discovery_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetDiscoveryConfig,
                    "_BaseGetDiscoveryConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetDiscoveryConfig",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetDiscoveryConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetDiscoveryConfig._get_response(
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
            resp = dlp.DiscoveryConfig()
            pb_resp = dlp.DiscoveryConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_discovery_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_discovery_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DiscoveryConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_discovery_config",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetDiscoveryConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetDlpJob(_BaseDlpServiceRestTransport._BaseGetDlpJob, DlpServiceRestStub):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetDlpJob")

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
            request: dlp.GetDlpJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DlpJob:
            r"""Call the get dlp job method over HTTP.

            Args:
                request (~.dlp.GetDlpJobRequest):
                    The request object. The request message for
                [GetDlpJob][google.privacy.dlp.v2.DlpService.GetDlpJob].
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DlpJob:
                    Combines all of the information about
                a DLP job.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetDlpJob._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_dlp_job(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetDlpJob,
                    "_BaseGetDlpJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetDlpJob",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetDlpJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetDlpJob._get_response(
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
            resp = dlp.DlpJob()
            pb_resp = dlp.DlpJob.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_dlp_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_dlp_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DlpJob.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_dlp_job",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetDlpJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFileStoreDataProfile(
        _BaseDlpServiceRestTransport._BaseGetFileStoreDataProfile, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetFileStoreDataProfile")

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
            request: dlp.GetFileStoreDataProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.FileStoreDataProfile:
            r"""Call the get file store data
            profile method over HTTP.

                Args:
                    request (~.dlp.GetFileStoreDataProfileRequest):
                        The request object. Request to get a file store data
                    profile.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dlp.FileStoreDataProfile:
                        The profile for a file store.

                    - Cloud Storage: maps 1:1 with a bucket.
                    - Amazon S3: maps 1:1 with a bucket.

            """

            http_options = _BaseDlpServiceRestTransport._BaseGetFileStoreDataProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_file_store_data_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetFileStoreDataProfile,
                    "_BaseGetFileStoreDataProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetFileStoreDataProfile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetFileStoreDataProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetFileStoreDataProfile._get_response(
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
            resp = dlp.FileStoreDataProfile()
            pb_resp = dlp.FileStoreDataProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_file_store_data_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_file_store_data_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.FileStoreDataProfile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_file_store_data_profile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetFileStoreDataProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetInspectTemplate(
        _BaseDlpServiceRestTransport._BaseGetInspectTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetInspectTemplate")

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
            request: dlp.GetInspectTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.InspectTemplate:
            r"""Call the get inspect template method over HTTP.

            Args:
                request (~.dlp.GetInspectTemplateRequest):
                    The request object. Request message for
                GetInspectTemplate.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.InspectTemplate:
                    The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
                to learn more.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetInspectTemplate._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_inspect_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetInspectTemplate,
                    "_BaseGetInspectTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetInspectTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetInspectTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetInspectTemplate._get_response(
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
            resp = dlp.InspectTemplate()
            pb_resp = dlp.InspectTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_inspect_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_inspect_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.InspectTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_inspect_template",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetInspectTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetJobTrigger(
        _BaseDlpServiceRestTransport._BaseGetJobTrigger, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetJobTrigger")

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
            request: dlp.GetJobTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.JobTrigger:
            r"""Call the get job trigger method over HTTP.

            Args:
                request (~.dlp.GetJobTriggerRequest):
                    The request object. Request message for GetJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.JobTrigger:
                    Contains a configuration to make API
                calls on a repeating basis. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers
                to learn more.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetJobTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_job_trigger(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetJobTrigger,
                    "_BaseGetJobTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetJobTrigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetJobTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetJobTrigger._get_response(
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
            resp = dlp.JobTrigger()
            pb_resp = dlp.JobTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_job_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_job_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.JobTrigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_job_trigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetJobTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetProjectDataProfile(
        _BaseDlpServiceRestTransport._BaseGetProjectDataProfile, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetProjectDataProfile")

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
            request: dlp.GetProjectDataProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ProjectDataProfile:
            r"""Call the get project data profile method over HTTP.

            Args:
                request (~.dlp.GetProjectDataProfileRequest):
                    The request object. Request to get a project data
                profile.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ProjectDataProfile:
                    An aggregated profile for this
                project, based on the resources profiled
                within it.

            """

            http_options = _BaseDlpServiceRestTransport._BaseGetProjectDataProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_project_data_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetProjectDataProfile,
                    "_BaseGetProjectDataProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetProjectDataProfile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetProjectDataProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetProjectDataProfile._get_response(
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
            resp = dlp.ProjectDataProfile()
            pb_resp = dlp.ProjectDataProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_project_data_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_project_data_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ProjectDataProfile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_project_data_profile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetProjectDataProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetStoredInfoType(
        _BaseDlpServiceRestTransport._BaseGetStoredInfoType, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetStoredInfoType")

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
            request: dlp.GetStoredInfoTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.StoredInfoType:
            r"""Call the get stored info type method over HTTP.

            Args:
                request (~.dlp.GetStoredInfoTypeRequest):
                    The request object. Request message for
                GetStoredInfoType.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.StoredInfoType:
                    StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseGetStoredInfoType._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_stored_info_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetStoredInfoType,
                    "_BaseGetStoredInfoType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetStoredInfoType",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetStoredInfoType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetStoredInfoType._get_response(
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
            resp = dlp.StoredInfoType()
            pb_resp = dlp.StoredInfoType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_stored_info_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_stored_info_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.StoredInfoType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_stored_info_type",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetStoredInfoType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetTableDataProfile(
        _BaseDlpServiceRestTransport._BaseGetTableDataProfile, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.GetTableDataProfile")

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
            request: dlp.GetTableDataProfileRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.TableDataProfile:
            r"""Call the get table data profile method over HTTP.

            Args:
                request (~.dlp.GetTableDataProfileRequest):
                    The request object. Request to get a table data profile.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.TableDataProfile:
                    The profile for a scanned table.
            """

            http_options = _BaseDlpServiceRestTransport._BaseGetTableDataProfile._get_http_options()
            request, metadata = self._interceptor.pre_get_table_data_profile(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseGetTableDataProfile,
                    "_BaseGetTableDataProfile__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.GetTableDataProfile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetTableDataProfile",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._GetTableDataProfile._get_response(
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
            resp = dlp.TableDataProfile()
            pb_resp = dlp.TableDataProfile.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_table_data_profile(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_table_data_profile_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.TableDataProfile.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.get_table_data_profile",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "GetTableDataProfile",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _HybridInspectDlpJob(
        _BaseDlpServiceRestTransport._BaseHybridInspectDlpJob, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.HybridInspectDlpJob")

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
            request: dlp.HybridInspectDlpJobRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.HybridInspectResponse:
            r"""Call the hybrid inspect dlp job method over HTTP.

            Args:
                request (~.dlp.HybridInspectDlpJobRequest):
                    The request object. Request to search for potentially
                sensitive info in a custom location.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.HybridInspectResponse:
                    Quota exceeded errors will be thrown
                once quota has been met.

            """

            http_options = _BaseDlpServiceRestTransport._BaseHybridInspectDlpJob._get_http_options()
            request, metadata = self._interceptor.pre_hybrid_inspect_dlp_job(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseHybridInspectDlpJob,
                    "_BaseHybridInspectDlpJob__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.HybridInspectDlpJob",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "HybridInspectDlpJob",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._HybridInspectDlpJob._get_response(
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
            resp = dlp.HybridInspectResponse()
            pb_resp = dlp.HybridInspectResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_hybrid_inspect_dlp_job(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_hybrid_inspect_dlp_job_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.HybridInspectResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.hybrid_inspect_dlp_job",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "HybridInspectDlpJob",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _HybridInspectJobTrigger(
        _BaseDlpServiceRestTransport._BaseHybridInspectJobTrigger, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.HybridInspectJobTrigger")

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
            request: dlp.HybridInspectJobTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.HybridInspectResponse:
            r"""Call the hybrid inspect job
            trigger method over HTTP.

                Args:
                    request (~.dlp.HybridInspectJobTriggerRequest):
                        The request object. Request to search for potentially
                    sensitive info in a custom location.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dlp.HybridInspectResponse:
                        Quota exceeded errors will be thrown
                    once quota has been met.

            """

            http_options = _BaseDlpServiceRestTransport._BaseHybridInspectJobTrigger._get_http_options()
            request, metadata = self._interceptor.pre_hybrid_inspect_job_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseHybridInspectJobTrigger,
                    "_BaseHybridInspectJobTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.HybridInspectJobTrigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "HybridInspectJobTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._HybridInspectJobTrigger._get_response(
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
            resp = dlp.HybridInspectResponse()
            pb_resp = dlp.HybridInspectResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_hybrid_inspect_job_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_hybrid_inspect_job_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.HybridInspectResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.hybrid_inspect_job_trigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "HybridInspectJobTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InspectContent(
        _BaseDlpServiceRestTransport._BaseInspectContent, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.InspectContent")

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
            request: dlp.InspectContentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.InspectContentResponse:
            r"""Call the inspect content method over HTTP.

            Args:
                request (~.dlp.InspectContentRequest):
                    The request object. Request to search for potentially
                sensitive info in a ContentItem.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.InspectContentResponse:
                    Results of inspecting an item.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseInspectContent._get_http_options()
            )
            request, metadata = self._interceptor.pre_inspect_content(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseInspectContent,
                    "_BaseInspectContent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.InspectContent",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "InspectContent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._InspectContent._get_response(
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
            resp = dlp.InspectContentResponse()
            pb_resp = dlp.InspectContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_inspect_content(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_inspect_content_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.InspectContentResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.inspect_content",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "InspectContent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListColumnDataProfiles(
        _BaseDlpServiceRestTransport._BaseListColumnDataProfiles, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListColumnDataProfiles")

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
            request: dlp.ListColumnDataProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListColumnDataProfilesResponse:
            r"""Call the list column data profiles method over HTTP.

            Args:
                request (~.dlp.ListColumnDataProfilesRequest):
                    The request object. Request to list the profiles
                generated for a given organization or
                project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListColumnDataProfilesResponse:
                    List of profiles generated for a
                given organization or project.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListColumnDataProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_column_data_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListColumnDataProfiles,
                    "_BaseListColumnDataProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListColumnDataProfiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListColumnDataProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListColumnDataProfiles._get_response(
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
            resp = dlp.ListColumnDataProfilesResponse()
            pb_resp = dlp.ListColumnDataProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_column_data_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_column_data_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListColumnDataProfilesResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_column_data_profiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListColumnDataProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnections(
        _BaseDlpServiceRestTransport._BaseListConnections, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListConnections")

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
            request: dlp.ListConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListConnectionsResponse:
            r"""Call the list connections method over HTTP.

            Args:
                request (~.dlp.ListConnectionsRequest):
                    The request object. Request message for ListConnections.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListConnectionsResponse:
                    Response message for ListConnections.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseListConnections._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListConnections,
                    "_BaseListConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListConnections",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListConnections._get_response(
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
            resp = dlp.ListConnectionsResponse()
            pb_resp = dlp.ListConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListConnectionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_connections",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListContentPolicies(
        _BaseDlpServiceRestTransport._BaseListContentPolicies, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListContentPolicies")

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
            request: dlp.ListContentPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListContentPoliciesResponse:
            r"""Call the list content policies method over HTTP.

            Args:
                request (~.dlp.ListContentPoliciesRequest):
                    The request object. Request message for
                ListContentPolicies.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListContentPoliciesResponse:
                    Response message for
                ListContentPolicies.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListContentPolicies._get_http_options()
            request, metadata = self._interceptor.pre_list_content_policies(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListContentPolicies,
                    "_BaseListContentPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListContentPolicies",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListContentPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListContentPolicies._get_response(
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
            resp = dlp.ListContentPoliciesResponse()
            pb_resp = dlp.ListContentPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_content_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_content_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListContentPoliciesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_content_policies",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListContentPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDeidentifyTemplates(
        _BaseDlpServiceRestTransport._BaseListDeidentifyTemplates, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListDeidentifyTemplates")

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
            request: dlp.ListDeidentifyTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListDeidentifyTemplatesResponse:
            r"""Call the list deidentify templates method over HTTP.

            Args:
                request (~.dlp.ListDeidentifyTemplatesRequest):
                    The request object. Request message for
                ListDeidentifyTemplates.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListDeidentifyTemplatesResponse:
                    Response message for
                ListDeidentifyTemplates.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListDeidentifyTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_deidentify_templates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListDeidentifyTemplates,
                    "_BaseListDeidentifyTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListDeidentifyTemplates",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListDeidentifyTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListDeidentifyTemplates._get_response(
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
            resp = dlp.ListDeidentifyTemplatesResponse()
            pb_resp = dlp.ListDeidentifyTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_deidentify_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_deidentify_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListDeidentifyTemplatesResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_deidentify_templates",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListDeidentifyTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDiscoveryConfigs(
        _BaseDlpServiceRestTransport._BaseListDiscoveryConfigs, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListDiscoveryConfigs")

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
            request: dlp.ListDiscoveryConfigsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListDiscoveryConfigsResponse:
            r"""Call the list discovery configs method over HTTP.

            Args:
                request (~.dlp.ListDiscoveryConfigsRequest):
                    The request object. Request message for
                ListDiscoveryConfigs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListDiscoveryConfigsResponse:
                    Response message for
                ListDiscoveryConfigs.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListDiscoveryConfigs._get_http_options()
            request, metadata = self._interceptor.pre_list_discovery_configs(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListDiscoveryConfigs,
                    "_BaseListDiscoveryConfigs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListDiscoveryConfigs",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListDiscoveryConfigs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListDiscoveryConfigs._get_response(
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
            resp = dlp.ListDiscoveryConfigsResponse()
            pb_resp = dlp.ListDiscoveryConfigsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_discovery_configs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_discovery_configs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListDiscoveryConfigsResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_discovery_configs",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListDiscoveryConfigs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListDlpJobs(
        _BaseDlpServiceRestTransport._BaseListDlpJobs, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListDlpJobs")

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
            request: dlp.ListDlpJobsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListDlpJobsResponse:
            r"""Call the list dlp jobs method over HTTP.

            Args:
                request (~.dlp.ListDlpJobsRequest):
                    The request object. The request message for listing DLP
                jobs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListDlpJobsResponse:
                    The response message for listing DLP
                jobs.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseListDlpJobs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_dlp_jobs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListDlpJobs,
                    "_BaseListDlpJobs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListDlpJobs",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListDlpJobs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListDlpJobs._get_response(
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
            resp = dlp.ListDlpJobsResponse()
            pb_resp = dlp.ListDlpJobsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_dlp_jobs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_dlp_jobs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListDlpJobsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_dlp_jobs",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListDlpJobs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFileStoreDataProfiles(
        _BaseDlpServiceRestTransport._BaseListFileStoreDataProfiles, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListFileStoreDataProfiles")

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
            request: dlp.ListFileStoreDataProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListFileStoreDataProfilesResponse:
            r"""Call the list file store data
            profiles method over HTTP.

                Args:
                    request (~.dlp.ListFileStoreDataProfilesRequest):
                        The request object. Request to list the file store
                    profiles generated for a given
                    organization or project.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dlp.ListFileStoreDataProfilesResponse:
                        List of file store data profiles
                    generated for a given organization or
                    project.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListFileStoreDataProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_file_store_data_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListFileStoreDataProfiles,
                    "_BaseListFileStoreDataProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListFileStoreDataProfiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListFileStoreDataProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListFileStoreDataProfiles._get_response(
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
            resp = dlp.ListFileStoreDataProfilesResponse()
            pb_resp = dlp.ListFileStoreDataProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_file_store_data_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_file_store_data_profiles_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListFileStoreDataProfilesResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_file_store_data_profiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListFileStoreDataProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInfoTypes(
        _BaseDlpServiceRestTransport._BaseListInfoTypes, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListInfoTypes")

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
            request: dlp.ListInfoTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListInfoTypesResponse:
            r"""Call the list info types method over HTTP.

            Args:
                request (~.dlp.ListInfoTypesRequest):
                    The request object. Request for the list of infoTypes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListInfoTypesResponse:
                    Response to the ListInfoTypes
                request.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseListInfoTypes._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_info_types(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListInfoTypes,
                    "_BaseListInfoTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListInfoTypes",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListInfoTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListInfoTypes._get_response(
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
            resp = dlp.ListInfoTypesResponse()
            pb_resp = dlp.ListInfoTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_info_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_info_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListInfoTypesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_info_types",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListInfoTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListInspectTemplates(
        _BaseDlpServiceRestTransport._BaseListInspectTemplates, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListInspectTemplates")

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
            request: dlp.ListInspectTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListInspectTemplatesResponse:
            r"""Call the list inspect templates method over HTTP.

            Args:
                request (~.dlp.ListInspectTemplatesRequest):
                    The request object. Request message for
                ListInspectTemplates.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListInspectTemplatesResponse:
                    Response message for
                ListInspectTemplates.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListInspectTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_inspect_templates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListInspectTemplates,
                    "_BaseListInspectTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListInspectTemplates",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListInspectTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListInspectTemplates._get_response(
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
            resp = dlp.ListInspectTemplatesResponse()
            pb_resp = dlp.ListInspectTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_inspect_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_inspect_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListInspectTemplatesResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_inspect_templates",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListInspectTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListJobTriggers(
        _BaseDlpServiceRestTransport._BaseListJobTriggers, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListJobTriggers")

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
            request: dlp.ListJobTriggersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListJobTriggersResponse:
            r"""Call the list job triggers method over HTTP.

            Args:
                request (~.dlp.ListJobTriggersRequest):
                    The request object. Request message for ListJobTriggers.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListJobTriggersResponse:
                    Response message for ListJobTriggers.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseListJobTriggers._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_job_triggers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListJobTriggers,
                    "_BaseListJobTriggers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListJobTriggers",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListJobTriggers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListJobTriggers._get_response(
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
            resp = dlp.ListJobTriggersResponse()
            pb_resp = dlp.ListJobTriggersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_job_triggers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_job_triggers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListJobTriggersResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_job_triggers",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListJobTriggers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListProjectDataProfiles(
        _BaseDlpServiceRestTransport._BaseListProjectDataProfiles, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListProjectDataProfiles")

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
            request: dlp.ListProjectDataProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListProjectDataProfilesResponse:
            r"""Call the list project data
            profiles method over HTTP.

                Args:
                    request (~.dlp.ListProjectDataProfilesRequest):
                        The request object. Request to list the profiles
                    generated for a given organization or
                    project.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dlp.ListProjectDataProfilesResponse:
                        List of profiles generated for a
                    given organization or project.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListProjectDataProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_project_data_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListProjectDataProfiles,
                    "_BaseListProjectDataProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListProjectDataProfiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListProjectDataProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListProjectDataProfiles._get_response(
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
            resp = dlp.ListProjectDataProfilesResponse()
            pb_resp = dlp.ListProjectDataProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_project_data_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_project_data_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListProjectDataProfilesResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_project_data_profiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListProjectDataProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListStoredInfoTypes(
        _BaseDlpServiceRestTransport._BaseListStoredInfoTypes, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListStoredInfoTypes")

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
            request: dlp.ListStoredInfoTypesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListStoredInfoTypesResponse:
            r"""Call the list stored info types method over HTTP.

            Args:
                request (~.dlp.ListStoredInfoTypesRequest):
                    The request object. Request message for
                ListStoredInfoTypes.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListStoredInfoTypesResponse:
                    Response message for
                ListStoredInfoTypes.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListStoredInfoTypes._get_http_options()
            request, metadata = self._interceptor.pre_list_stored_info_types(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListStoredInfoTypes,
                    "_BaseListStoredInfoTypes__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListStoredInfoTypes",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListStoredInfoTypes",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListStoredInfoTypes._get_response(
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
            resp = dlp.ListStoredInfoTypesResponse()
            pb_resp = dlp.ListStoredInfoTypesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_stored_info_types(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_stored_info_types_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListStoredInfoTypesResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_stored_info_types",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListStoredInfoTypes",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListTableDataProfiles(
        _BaseDlpServiceRestTransport._BaseListTableDataProfiles, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ListTableDataProfiles")

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
            request: dlp.ListTableDataProfilesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ListTableDataProfilesResponse:
            r"""Call the list table data profiles method over HTTP.

            Args:
                request (~.dlp.ListTableDataProfilesRequest):
                    The request object. Request to list the profiles
                generated for a given organization or
                project.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ListTableDataProfilesResponse:
                    List of profiles generated for a
                given organization or project.

            """

            http_options = _BaseDlpServiceRestTransport._BaseListTableDataProfiles._get_http_options()
            request, metadata = self._interceptor.pre_list_table_data_profiles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseListTableDataProfiles,
                    "_BaseListTableDataProfiles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ListTableDataProfiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListTableDataProfiles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ListTableDataProfiles._get_response(
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
            resp = dlp.ListTableDataProfilesResponse()
            pb_resp = dlp.ListTableDataProfilesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_table_data_profiles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_table_data_profiles_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ListTableDataProfilesResponse.to_json(
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
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.list_table_data_profiles",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ListTableDataProfiles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RedactImage(
        _BaseDlpServiceRestTransport._BaseRedactImage, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.RedactImage")

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
            request: dlp.RedactImageRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.RedactImageResponse:
            r"""Call the redact image method over HTTP.

            Args:
                request (~.dlp.RedactImageRequest):
                    The request object. Request to search for potentially
                sensitive info in an image and redact it
                by covering it with a colored rectangle.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.RedactImageResponse:
                    Results of redacting an image.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseRedactImage._get_http_options()
            )
            request, metadata = self._interceptor.pre_redact_image(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseRedactImage,
                    "_BaseRedactImage__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.RedactImage",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "RedactImage",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._RedactImage._get_response(
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
            resp = dlp.RedactImageResponse()
            pb_resp = dlp.RedactImageResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_redact_image(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_redact_image_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.RedactImageResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.redact_image",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "RedactImage",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ReidentifyContent(
        _BaseDlpServiceRestTransport._BaseReidentifyContent, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.ReidentifyContent")

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
            request: dlp.ReidentifyContentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ReidentifyContentResponse:
            r"""Call the reidentify content method over HTTP.

            Args:
                request (~.dlp.ReidentifyContentRequest):
                    The request object. Request to re-identify an item.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ReidentifyContentResponse:
                    Results of re-identifying an item.
            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseReidentifyContent._get_http_options()
            )
            request, metadata = self._interceptor.pre_reidentify_content(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseReidentifyContent,
                    "_BaseReidentifyContent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.ReidentifyContent",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ReidentifyContent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._ReidentifyContent._get_response(
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
            resp = dlp.ReidentifyContentResponse()
            pb_resp = dlp.ReidentifyContentResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_reidentify_content(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_reidentify_content_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ReidentifyContentResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.reidentify_content",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "ReidentifyContent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SearchConnections(
        _BaseDlpServiceRestTransport._BaseSearchConnections, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.SearchConnections")

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
            request: dlp.SearchConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.SearchConnectionsResponse:
            r"""Call the search connections method over HTTP.

            Args:
                request (~.dlp.SearchConnectionsRequest):
                    The request object. Request message for
                SearchConnections.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.SearchConnectionsResponse:
                    Response message for
                SearchConnections.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseSearchConnections._get_http_options()
            )
            request, metadata = self._interceptor.pre_search_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseSearchConnections,
                    "_BaseSearchConnections__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.SearchConnections",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "SearchConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._SearchConnections._get_response(
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
            resp = dlp.SearchConnectionsResponse()
            pb_resp = dlp.SearchConnectionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_search_connections(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_search_connections_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.SearchConnectionsResponse.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.search_connections",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "SearchConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnection(
        _BaseDlpServiceRestTransport._BaseUpdateConnection, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateConnection")

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
            request: dlp.UpdateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.Connection:
            r"""Call the update connection method over HTTP.

            Args:
                request (~.dlp.UpdateConnectionRequest):
                    The request object. Request message for UpdateConnection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.Connection:
                    A data connection to allow the DLP
                API to profile data in locations that
                require additional configuration.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseUpdateConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateConnection,
                    "_BaseUpdateConnection__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateConnection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateConnection._get_response(
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
            resp = dlp.Connection()
            pb_resp = dlp.Connection.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_connection(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_connection_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_connection",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateContentPolicy(
        _BaseDlpServiceRestTransport._BaseUpdateContentPolicy, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateContentPolicy")

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
            request: dlp.UpdateContentPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.ContentPolicy:
            r"""Call the update content policy method over HTTP.

            Args:
                request (~.dlp.UpdateContentPolicyRequest):
                    The request object. Request message for
                UpdateContentPolicy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.ContentPolicy:
                    A policy to apply to content based on
                its inspection findings.

            """

            http_options = _BaseDlpServiceRestTransport._BaseUpdateContentPolicy._get_http_options()
            request, metadata = self._interceptor.pre_update_content_policy(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateContentPolicy,
                    "_BaseUpdateContentPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateContentPolicy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateContentPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateContentPolicy._get_response(
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
            resp = dlp.ContentPolicy()
            pb_resp = dlp.ContentPolicy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_content_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_content_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.ContentPolicy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_content_policy",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateContentPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDeidentifyTemplate(
        _BaseDlpServiceRestTransport._BaseUpdateDeidentifyTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateDeidentifyTemplate")

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
            request: dlp.UpdateDeidentifyTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DeidentifyTemplate:
            r"""Call the update deidentify
            template method over HTTP.

                Args:
                    request (~.dlp.UpdateDeidentifyTemplateRequest):
                        The request object. Request message for
                    UpdateDeidentifyTemplate.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.dlp.DeidentifyTemplate:
                        DeidentifyTemplates contains
                    instructions on how to de-identify
                    content. See
                    https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
                    to learn more.

            """

            http_options = _BaseDlpServiceRestTransport._BaseUpdateDeidentifyTemplate._get_http_options()
            request, metadata = self._interceptor.pre_update_deidentify_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateDeidentifyTemplate,
                    "_BaseUpdateDeidentifyTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateDeidentifyTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateDeidentifyTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateDeidentifyTemplate._get_response(
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
            resp = dlp.DeidentifyTemplate()
            pb_resp = dlp.DeidentifyTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_deidentify_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_deidentify_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DeidentifyTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_deidentify_template",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateDeidentifyTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateDiscoveryConfig(
        _BaseDlpServiceRestTransport._BaseUpdateDiscoveryConfig, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateDiscoveryConfig")

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
            request: dlp.UpdateDiscoveryConfigRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.DiscoveryConfig:
            r"""Call the update discovery config method over HTTP.

            Args:
                request (~.dlp.UpdateDiscoveryConfigRequest):
                    The request object. Request message for
                UpdateDiscoveryConfig.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.DiscoveryConfig:
                    Configuration for discovery to scan resources for
                profile generation. Only one discovery configuration may
                exist per organization, folder, or project.

                The generated data profiles are retained according to
                the [data retention policy]
                (https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles#retention).

            """

            http_options = _BaseDlpServiceRestTransport._BaseUpdateDiscoveryConfig._get_http_options()
            request, metadata = self._interceptor.pre_update_discovery_config(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateDiscoveryConfig,
                    "_BaseUpdateDiscoveryConfig__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateDiscoveryConfig",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateDiscoveryConfig",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateDiscoveryConfig._get_response(
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
            resp = dlp.DiscoveryConfig()
            pb_resp = dlp.DiscoveryConfig.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_discovery_config(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_discovery_config_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.DiscoveryConfig.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_discovery_config",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateDiscoveryConfig",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateInspectTemplate(
        _BaseDlpServiceRestTransport._BaseUpdateInspectTemplate, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateInspectTemplate")

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
            request: dlp.UpdateInspectTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.InspectTemplate:
            r"""Call the update inspect template method over HTTP.

            Args:
                request (~.dlp.UpdateInspectTemplateRequest):
                    The request object. Request message for
                UpdateInspectTemplate.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.InspectTemplate:
                    The inspectTemplate contains a
                configuration (set of types of sensitive
                data to be detected) to be used anywhere
                you otherwise would normally specify
                InspectConfig. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates
                to learn more.

            """

            http_options = _BaseDlpServiceRestTransport._BaseUpdateInspectTemplate._get_http_options()
            request, metadata = self._interceptor.pre_update_inspect_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateInspectTemplate,
                    "_BaseUpdateInspectTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateInspectTemplate",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateInspectTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateInspectTemplate._get_response(
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
            resp = dlp.InspectTemplate()
            pb_resp = dlp.InspectTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_inspect_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_inspect_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.InspectTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_inspect_template",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateInspectTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateJobTrigger(
        _BaseDlpServiceRestTransport._BaseUpdateJobTrigger, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateJobTrigger")

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
            request: dlp.UpdateJobTriggerRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.JobTrigger:
            r"""Call the update job trigger method over HTTP.

            Args:
                request (~.dlp.UpdateJobTriggerRequest):
                    The request object. Request message for UpdateJobTrigger.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.JobTrigger:
                    Contains a configuration to make API
                calls on a repeating basis. See
                https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers
                to learn more.

            """

            http_options = (
                _BaseDlpServiceRestTransport._BaseUpdateJobTrigger._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_job_trigger(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateJobTrigger,
                    "_BaseUpdateJobTrigger__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateJobTrigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateJobTrigger",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateJobTrigger._get_response(
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
            resp = dlp.JobTrigger()
            pb_resp = dlp.JobTrigger.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_job_trigger(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_job_trigger_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.JobTrigger.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_job_trigger",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateJobTrigger",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateStoredInfoType(
        _BaseDlpServiceRestTransport._BaseUpdateStoredInfoType, DlpServiceRestStub
    ):
        def __hash__(self):
            return hash("DlpServiceRestTransport.UpdateStoredInfoType")

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
            request: dlp.UpdateStoredInfoTypeRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> dlp.StoredInfoType:
            r"""Call the update stored info type method over HTTP.

            Args:
                request (~.dlp.UpdateStoredInfoTypeRequest):
                    The request object. Request message for
                UpdateStoredInfoType.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.dlp.StoredInfoType:
                    StoredInfoType resource message that
                contains information about the current
                version and any pending updates.

            """

            http_options = _BaseDlpServiceRestTransport._BaseUpdateStoredInfoType._get_http_options()
            request, metadata = self._interceptor.pre_update_stored_info_type(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDlpServiceRestTransport._BaseUpdateStoredInfoType,
                    "_BaseUpdateStoredInfoType__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.privacy.dlp_v2.DlpServiceClient.UpdateStoredInfoType",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateStoredInfoType",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DlpServiceRestTransport._UpdateStoredInfoType._get_response(
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
            resp = dlp.StoredInfoType()
            pb_resp = dlp.StoredInfoType.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_stored_info_type(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_stored_info_type_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = dlp.StoredInfoType.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.privacy.dlp_v2.DlpServiceClient.update_stored_info_type",
                    extra={
                        "serviceName": "google.privacy.dlp.v2.DlpService",
                        "rpcName": "UpdateStoredInfoType",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def activate_job_trigger(
        self,
    ) -> Callable[[dlp.ActivateJobTriggerRequest], dlp.DlpJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ActivateJobTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_dlp_job(self) -> Callable[[dlp.CancelDlpJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CancelDlpJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_connection(
        self,
    ) -> Callable[[dlp.CreateConnectionRequest], dlp.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_content_policy(
        self,
    ) -> Callable[[dlp.CreateContentPolicyRequest], dlp.ContentPolicy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateContentPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_deidentify_template(
        self,
    ) -> Callable[[dlp.CreateDeidentifyTemplateRequest], dlp.DeidentifyTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDeidentifyTemplate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_discovery_config(
        self,
    ) -> Callable[[dlp.CreateDiscoveryConfigRequest], dlp.DiscoveryConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDiscoveryConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_dlp_job(self) -> Callable[[dlp.CreateDlpJobRequest], dlp.DlpJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateDlpJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_inspect_template(
        self,
    ) -> Callable[[dlp.CreateInspectTemplateRequest], dlp.InspectTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateInspectTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_job_trigger(
        self,
    ) -> Callable[[dlp.CreateJobTriggerRequest], dlp.JobTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateJobTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_stored_info_type(
        self,
    ) -> Callable[[dlp.CreateStoredInfoTypeRequest], dlp.StoredInfoType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateStoredInfoType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deidentify_content(
        self,
    ) -> Callable[[dlp.DeidentifyContentRequest], dlp.DeidentifyContentResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeidentifyContent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_connection(
        self,
    ) -> Callable[[dlp.DeleteConnectionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_content_policy(
        self,
    ) -> Callable[[dlp.DeleteContentPolicyRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteContentPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_deidentify_template(
        self,
    ) -> Callable[[dlp.DeleteDeidentifyTemplateRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDeidentifyTemplate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_discovery_config(
        self,
    ) -> Callable[[dlp.DeleteDiscoveryConfigRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDiscoveryConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_dlp_job(self) -> Callable[[dlp.DeleteDlpJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteDlpJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_file_store_data_profile(
        self,
    ) -> Callable[[dlp.DeleteFileStoreDataProfileRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFileStoreDataProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_inspect_template(
        self,
    ) -> Callable[[dlp.DeleteInspectTemplateRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteInspectTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_job_trigger(
        self,
    ) -> Callable[[dlp.DeleteJobTriggerRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteJobTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_stored_info_type(
        self,
    ) -> Callable[[dlp.DeleteStoredInfoTypeRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteStoredInfoType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_table_data_profile(
        self,
    ) -> Callable[[dlp.DeleteTableDataProfileRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteTableDataProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def finish_dlp_job(self) -> Callable[[dlp.FinishDlpJobRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FinishDlpJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_column_data_profile(
        self,
    ) -> Callable[[dlp.GetColumnDataProfileRequest], dlp.ColumnDataProfile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetColumnDataProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_connection(self) -> Callable[[dlp.GetConnectionRequest], dlp.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_content_policy(
        self,
    ) -> Callable[[dlp.GetContentPolicyRequest], dlp.ContentPolicy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetContentPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_deidentify_template(
        self,
    ) -> Callable[[dlp.GetDeidentifyTemplateRequest], dlp.DeidentifyTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDeidentifyTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_discovery_config(
        self,
    ) -> Callable[[dlp.GetDiscoveryConfigRequest], dlp.DiscoveryConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDiscoveryConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_dlp_job(self) -> Callable[[dlp.GetDlpJobRequest], dlp.DlpJob]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetDlpJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_file_store_data_profile(
        self,
    ) -> Callable[[dlp.GetFileStoreDataProfileRequest], dlp.FileStoreDataProfile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFileStoreDataProfile(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_inspect_template(
        self,
    ) -> Callable[[dlp.GetInspectTemplateRequest], dlp.InspectTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetInspectTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_job_trigger(self) -> Callable[[dlp.GetJobTriggerRequest], dlp.JobTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetJobTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_project_data_profile(
        self,
    ) -> Callable[[dlp.GetProjectDataProfileRequest], dlp.ProjectDataProfile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetProjectDataProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_stored_info_type(
        self,
    ) -> Callable[[dlp.GetStoredInfoTypeRequest], dlp.StoredInfoType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetStoredInfoType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_table_data_profile(
        self,
    ) -> Callable[[dlp.GetTableDataProfileRequest], dlp.TableDataProfile]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetTableDataProfile(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def hybrid_inspect_dlp_job(
        self,
    ) -> Callable[[dlp.HybridInspectDlpJobRequest], dlp.HybridInspectResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._HybridInspectDlpJob(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def hybrid_inspect_job_trigger(
        self,
    ) -> Callable[[dlp.HybridInspectJobTriggerRequest], dlp.HybridInspectResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._HybridInspectJobTrigger(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def inspect_content(
        self,
    ) -> Callable[[dlp.InspectContentRequest], dlp.InspectContentResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InspectContent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_column_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListColumnDataProfilesRequest], dlp.ListColumnDataProfilesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListColumnDataProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_connections(
        self,
    ) -> Callable[[dlp.ListConnectionsRequest], dlp.ListConnectionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnections(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_content_policies(
        self,
    ) -> Callable[[dlp.ListContentPoliciesRequest], dlp.ListContentPoliciesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListContentPolicies(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_deidentify_templates(
        self,
    ) -> Callable[
        [dlp.ListDeidentifyTemplatesRequest], dlp.ListDeidentifyTemplatesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDeidentifyTemplates(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_discovery_configs(
        self,
    ) -> Callable[[dlp.ListDiscoveryConfigsRequest], dlp.ListDiscoveryConfigsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDiscoveryConfigs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_dlp_jobs(
        self,
    ) -> Callable[[dlp.ListDlpJobsRequest], dlp.ListDlpJobsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListDlpJobs(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_file_store_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListFileStoreDataProfilesRequest], dlp.ListFileStoreDataProfilesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFileStoreDataProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_info_types(
        self,
    ) -> Callable[[dlp.ListInfoTypesRequest], dlp.ListInfoTypesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInfoTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_inspect_templates(
        self,
    ) -> Callable[[dlp.ListInspectTemplatesRequest], dlp.ListInspectTemplatesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListInspectTemplates(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_job_triggers(
        self,
    ) -> Callable[[dlp.ListJobTriggersRequest], dlp.ListJobTriggersResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListJobTriggers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_project_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListProjectDataProfilesRequest], dlp.ListProjectDataProfilesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListProjectDataProfiles(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_stored_info_types(
        self,
    ) -> Callable[[dlp.ListStoredInfoTypesRequest], dlp.ListStoredInfoTypesResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListStoredInfoTypes(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_table_data_profiles(
        self,
    ) -> Callable[
        [dlp.ListTableDataProfilesRequest], dlp.ListTableDataProfilesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListTableDataProfiles(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def redact_image(
        self,
    ) -> Callable[[dlp.RedactImageRequest], dlp.RedactImageResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RedactImage(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def reidentify_content(
        self,
    ) -> Callable[[dlp.ReidentifyContentRequest], dlp.ReidentifyContentResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ReidentifyContent(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def search_connections(
        self,
    ) -> Callable[[dlp.SearchConnectionsRequest], dlp.SearchConnectionsResponse]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SearchConnections(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_connection(
        self,
    ) -> Callable[[dlp.UpdateConnectionRequest], dlp.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnection(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_content_policy(
        self,
    ) -> Callable[[dlp.UpdateContentPolicyRequest], dlp.ContentPolicy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateContentPolicy(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_deidentify_template(
        self,
    ) -> Callable[[dlp.UpdateDeidentifyTemplateRequest], dlp.DeidentifyTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDeidentifyTemplate(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_discovery_config(
        self,
    ) -> Callable[[dlp.UpdateDiscoveryConfigRequest], dlp.DiscoveryConfig]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateDiscoveryConfig(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_inspect_template(
        self,
    ) -> Callable[[dlp.UpdateInspectTemplateRequest], dlp.InspectTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateInspectTemplate(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_job_trigger(
        self,
    ) -> Callable[[dlp.UpdateJobTriggerRequest], dlp.JobTrigger]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateJobTrigger(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_stored_info_type(
        self,
    ) -> Callable[[dlp.UpdateStoredInfoTypeRequest], dlp.StoredInfoType]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateStoredInfoType(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def kind(self) -> str:
        return "rest"

    def close(self):
        self._session.close()


__all__ = ("DlpServiceRestTransport",)
