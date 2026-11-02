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
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1, rest_helpers, rest_streaming
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.requests import AuthorizedSession  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.designcenter_v1._compat import trace_http_request, transcode_request
from google.cloud.designcenter_v1.types import (
    apphub_integration_messages,
    authoring,
    authoring_messages,
    best_practices,
    best_practices_messages,
    catalog_management,
    catalog_management_messages,
    deployment_messages,
    deployment_resources,
    sharing,
    sharing_messages,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseDesignCenterRestTransport

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


class DesignCenterRestInterceptor:
    """Interceptor for DesignCenter.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the DesignCenterRestTransport.

    .. code-block:: python
        class MyCustomDesignCenterInterceptor(DesignCenterRestInterceptor):
            def pre_commit_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_commit_application_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_application_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_catalog_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_catalog_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_catalog_template_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_catalog_template_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_component(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_component(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_space(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_application_template_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_catalog_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_catalog_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_catalog_template_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_catalog_template_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_component(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_deploy_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_application_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_application_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_application_template_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_application_template_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_application_template_revision_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_application_template_revision_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_application_assessment_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_application_assessment_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_fetch_frameworks(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_fetch_frameworks(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_application_assessment_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_application_assessment_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_application_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_application_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_application_template_assessment_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_application_template_assessment_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_application_template_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_application_template_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_application_template_revision_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_application_template_revision_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_assessment_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_assessment_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_generate_terraform_plan_assessment_report(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_generate_terraform_plan_assessment_report(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application_template_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application_template_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_application_template_system_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_application_template_system_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_catalog_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_catalog_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_catalog_template_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_catalog_template_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_component(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_component(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_shared_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_shared_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_shared_template_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_shared_template_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_space(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_application_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_application_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_application_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_application_template_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_application_template_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ingest_application_template_ia_c(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_application_template_ia_c(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_applications(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_applications(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_application_template_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_application_template_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_application_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_application_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_application_template_system_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_application_template_system_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_catalogs(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_catalogs(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_catalog_template_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_catalog_template_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_catalog_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_catalog_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_components(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_components(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_connections(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_connections(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_policies(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_policies(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_shared_template_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_shared_template_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_shared_templates(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_shared_templates(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_shares(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_shares(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_spaces(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_spaces(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_preview_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_preview_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_recommend_iam_roles(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_recommend_iam_roles(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_register_app_hub_application_resources(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_register_app_hub_application_resources(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_snapshot_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_snapshot_application_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_sync_share(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_sync_share(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_application_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_application_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_catalog(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_catalog(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_catalog_template(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_catalog_template(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_component(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_component(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_connection(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_connection(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_policy(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_policy(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_space(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_space(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = DesignCenterRestTransport(interceptor=MyCustomDesignCenterInterceptor())
        client = DesignCenterClient(transport=transport)


    """

    def pre_commit_application_template(
        self,
        request: authoring_messages.CommitApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.CommitApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for commit_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_commit_application_template(
        self, response: authoring.ApplicationTemplateRevision
    ) -> authoring.ApplicationTemplateRevision:
        """Post-rpc interceptor for commit_application_template

        DEPRECATED. Please use the `post_commit_application_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_commit_application_template` interceptor runs
        before the `post_commit_application_template_with_metadata` interceptor.
        """
        return response

    def post_commit_application_template_with_metadata(
        self,
        response: authoring.ApplicationTemplateRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring.ApplicationTemplateRevision, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for commit_application_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_commit_application_template_with_metadata`
        interceptor in new development instead of the `post_commit_application_template` interceptor.
        When both interceptors are used, this `post_commit_application_template_with_metadata` interceptor runs after the
        `post_commit_application_template` interceptor. The (possibly modified) response returned by
        `post_commit_application_template` will be passed to
        `post_commit_application_template_with_metadata`.
        """
        return response, metadata

    def pre_create_application(
        self,
        request: deployment_messages.CreateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.CreateApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_application(
        self, response: deployment_resources.Application
    ) -> deployment_resources.Application:
        """Post-rpc interceptor for create_application

        DEPRECATED. Please use the `post_create_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_application` interceptor runs
        before the `post_create_application_with_metadata` interceptor.
        """
        return response

    def post_create_application_with_metadata(
        self,
        response: deployment_resources.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_resources.Application, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_application_with_metadata`
        interceptor in new development instead of the `post_create_application` interceptor.
        When both interceptors are used, this `post_create_application_with_metadata` interceptor runs after the
        `post_create_application` interceptor. The (possibly modified) response returned by
        `post_create_application` will be passed to
        `post_create_application_with_metadata`.
        """
        return response, metadata

    def pre_create_application_template(
        self,
        request: authoring_messages.CreateApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.CreateApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_application_template(
        self, response: authoring.ApplicationTemplate
    ) -> authoring.ApplicationTemplate:
        """Post-rpc interceptor for create_application_template

        DEPRECATED. Please use the `post_create_application_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_application_template` interceptor runs
        before the `post_create_application_template_with_metadata` interceptor.
        """
        return response

    def post_create_application_template_with_metadata(
        self,
        response: authoring.ApplicationTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.ApplicationTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_application_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_application_template_with_metadata`
        interceptor in new development instead of the `post_create_application_template` interceptor.
        When both interceptors are used, this `post_create_application_template_with_metadata` interceptor runs after the
        `post_create_application_template` interceptor. The (possibly modified) response returned by
        `post_create_application_template` will be passed to
        `post_create_application_template_with_metadata`.
        """
        return response, metadata

    def pre_create_catalog(
        self,
        request: catalog_management_messages.CreateCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.CreateCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_catalog(
        self, response: catalog_management.Catalog
    ) -> catalog_management.Catalog:
        """Post-rpc interceptor for create_catalog

        DEPRECATED. Please use the `post_create_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_catalog` interceptor runs
        before the `post_create_catalog_with_metadata` interceptor.
        """
        return response

    def post_create_catalog_with_metadata(
        self,
        response: catalog_management.Catalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog_management.Catalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_catalog_with_metadata`
        interceptor in new development instead of the `post_create_catalog` interceptor.
        When both interceptors are used, this `post_create_catalog_with_metadata` interceptor runs after the
        `post_create_catalog` interceptor. The (possibly modified) response returned by
        `post_create_catalog` will be passed to
        `post_create_catalog_with_metadata`.
        """
        return response, metadata

    def pre_create_catalog_template(
        self,
        request: catalog_management_messages.CreateCatalogTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.CreateCatalogTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_catalog_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_catalog_template(
        self, response: catalog_management.CatalogTemplate
    ) -> catalog_management.CatalogTemplate:
        """Post-rpc interceptor for create_catalog_template

        DEPRECATED. Please use the `post_create_catalog_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_catalog_template` interceptor runs
        before the `post_create_catalog_template_with_metadata` interceptor.
        """
        return response

    def post_create_catalog_template_with_metadata(
        self,
        response: catalog_management.CatalogTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management.CatalogTemplate, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for create_catalog_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_catalog_template_with_metadata`
        interceptor in new development instead of the `post_create_catalog_template` interceptor.
        When both interceptors are used, this `post_create_catalog_template_with_metadata` interceptor runs after the
        `post_create_catalog_template` interceptor. The (possibly modified) response returned by
        `post_create_catalog_template` will be passed to
        `post_create_catalog_template_with_metadata`.
        """
        return response, metadata

    def pre_create_catalog_template_revision(
        self,
        request: catalog_management_messages.CreateCatalogTemplateRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.CreateCatalogTemplateRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_catalog_template_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_catalog_template_revision(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_catalog_template_revision

        DEPRECATED. Please use the `post_create_catalog_template_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_catalog_template_revision` interceptor runs
        before the `post_create_catalog_template_revision_with_metadata` interceptor.
        """
        return response

    def post_create_catalog_template_revision_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_catalog_template_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_catalog_template_revision_with_metadata`
        interceptor in new development instead of the `post_create_catalog_template_revision` interceptor.
        When both interceptors are used, this `post_create_catalog_template_revision_with_metadata` interceptor runs after the
        `post_create_catalog_template_revision` interceptor. The (possibly modified) response returned by
        `post_create_catalog_template_revision` will be passed to
        `post_create_catalog_template_revision_with_metadata`.
        """
        return response, metadata

    def pre_create_component(
        self,
        request: authoring_messages.CreateComponentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.CreateComponentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_component

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_component(
        self, response: authoring.Component
    ) -> authoring.Component:
        """Post-rpc interceptor for create_component

        DEPRECATED. Please use the `post_create_component_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_component` interceptor runs
        before the `post_create_component_with_metadata` interceptor.
        """
        return response

    def post_create_component_with_metadata(
        self,
        response: authoring.Component,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.Component, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_component

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_component_with_metadata`
        interceptor in new development instead of the `post_create_component` interceptor.
        When both interceptors are used, this `post_create_component_with_metadata` interceptor runs after the
        `post_create_component` interceptor. The (possibly modified) response returned by
        `post_create_component` will be passed to
        `post_create_component_with_metadata`.
        """
        return response, metadata

    def pre_create_connection(
        self,
        request: authoring_messages.CreateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.CreateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_connection(
        self, response: authoring.Connection
    ) -> authoring.Connection:
        """Post-rpc interceptor for create_connection

        DEPRECATED. Please use the `post_create_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_connection` interceptor runs
        before the `post_create_connection_with_metadata` interceptor.
        """
        return response

    def post_create_connection_with_metadata(
        self,
        response: authoring.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_connection_with_metadata`
        interceptor in new development instead of the `post_create_connection` interceptor.
        When both interceptors are used, this `post_create_connection_with_metadata` interceptor runs after the
        `post_create_connection` interceptor. The (possibly modified) response returned by
        `post_create_connection` will be passed to
        `post_create_connection_with_metadata`.
        """
        return response, metadata

    def pre_create_policy(
        self,
        request: best_practices_messages.CreatePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.CreatePolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_policy(
        self, response: best_practices.Policy
    ) -> best_practices.Policy:
        """Post-rpc interceptor for create_policy

        DEPRECATED. Please use the `post_create_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_policy` interceptor runs
        before the `post_create_policy_with_metadata` interceptor.
        """
        return response

    def post_create_policy_with_metadata(
        self,
        response: best_practices.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[best_practices.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_policy_with_metadata`
        interceptor in new development instead of the `post_create_policy` interceptor.
        When both interceptors are used, this `post_create_policy_with_metadata` interceptor runs after the
        `post_create_policy` interceptor. The (possibly modified) response returned by
        `post_create_policy` will be passed to
        `post_create_policy_with_metadata`.
        """
        return response, metadata

    def pre_create_share(
        self,
        request: sharing_messages.CreateShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.CreateShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for create_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_share(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_share

        DEPRECATED. Please use the `post_create_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_share` interceptor runs
        before the `post_create_share_with_metadata` interceptor.
        """
        return response

    def post_create_share_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_share_with_metadata`
        interceptor in new development instead of the `post_create_share` interceptor.
        When both interceptors are used, this `post_create_share_with_metadata` interceptor runs after the
        `post_create_share` interceptor. The (possibly modified) response returned by
        `post_create_share` will be passed to
        `post_create_share_with_metadata`.
        """
        return response, metadata

    def pre_create_space(
        self,
        request: catalog_management_messages.CreateSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.CreateSpaceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_create_space(
        self, response: catalog_management.Space
    ) -> catalog_management.Space:
        """Post-rpc interceptor for create_space

        DEPRECATED. Please use the `post_create_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_create_space` interceptor runs
        before the `post_create_space_with_metadata` interceptor.
        """
        return response

    def post_create_space_with_metadata(
        self,
        response: catalog_management.Space,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog_management.Space, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_create_space_with_metadata`
        interceptor in new development instead of the `post_create_space` interceptor.
        When both interceptors are used, this `post_create_space_with_metadata` interceptor runs after the
        `post_create_space` interceptor. The (possibly modified) response returned by
        `post_create_space` will be passed to
        `post_create_space_with_metadata`.
        """
        return response, metadata

    def pre_delete_application(
        self,
        request: deployment_messages.DeleteApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.DeleteApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_delete_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_application

        DEPRECATED. Please use the `post_delete_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_delete_application` interceptor runs
        before the `post_delete_application_with_metadata` interceptor.
        """
        return response

    def post_delete_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_delete_application_with_metadata`
        interceptor in new development instead of the `post_delete_application` interceptor.
        When both interceptors are used, this `post_delete_application_with_metadata` interceptor runs after the
        `post_delete_application` interceptor. The (possibly modified) response returned by
        `post_delete_application` will be passed to
        `post_delete_application_with_metadata`.
        """
        return response, metadata

    def pre_delete_application_template(
        self,
        request: authoring_messages.DeleteApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.DeleteApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def pre_delete_application_template_revision(
        self,
        request: authoring_messages.DeleteApplicationTemplateRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.DeleteApplicationTemplateRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_application_template_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def pre_delete_catalog(
        self,
        request: catalog_management_messages.DeleteCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.DeleteCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_delete_catalog(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_catalog

        DEPRECATED. Please use the `post_delete_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_delete_catalog` interceptor runs
        before the `post_delete_catalog_with_metadata` interceptor.
        """
        return response

    def post_delete_catalog_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_delete_catalog_with_metadata`
        interceptor in new development instead of the `post_delete_catalog` interceptor.
        When both interceptors are used, this `post_delete_catalog_with_metadata` interceptor runs after the
        `post_delete_catalog` interceptor. The (possibly modified) response returned by
        `post_delete_catalog` will be passed to
        `post_delete_catalog_with_metadata`.
        """
        return response, metadata

    def pre_delete_catalog_template(
        self,
        request: catalog_management_messages.DeleteCatalogTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.DeleteCatalogTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_catalog_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_delete_catalog_template(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_catalog_template

        DEPRECATED. Please use the `post_delete_catalog_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_delete_catalog_template` interceptor runs
        before the `post_delete_catalog_template_with_metadata` interceptor.
        """
        return response

    def post_delete_catalog_template_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_catalog_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_delete_catalog_template_with_metadata`
        interceptor in new development instead of the `post_delete_catalog_template` interceptor.
        When both interceptors are used, this `post_delete_catalog_template_with_metadata` interceptor runs after the
        `post_delete_catalog_template` interceptor. The (possibly modified) response returned by
        `post_delete_catalog_template` will be passed to
        `post_delete_catalog_template_with_metadata`.
        """
        return response, metadata

    def pre_delete_catalog_template_revision(
        self,
        request: catalog_management_messages.DeleteCatalogTemplateRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.DeleteCatalogTemplateRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_catalog_template_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_delete_catalog_template_revision(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_catalog_template_revision

        DEPRECATED. Please use the `post_delete_catalog_template_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_delete_catalog_template_revision` interceptor runs
        before the `post_delete_catalog_template_revision_with_metadata` interceptor.
        """
        return response

    def post_delete_catalog_template_revision_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_catalog_template_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_delete_catalog_template_revision_with_metadata`
        interceptor in new development instead of the `post_delete_catalog_template_revision` interceptor.
        When both interceptors are used, this `post_delete_catalog_template_revision_with_metadata` interceptor runs after the
        `post_delete_catalog_template_revision` interceptor. The (possibly modified) response returned by
        `post_delete_catalog_template_revision` will be passed to
        `post_delete_catalog_template_revision_with_metadata`.
        """
        return response, metadata

    def pre_delete_component(
        self,
        request: authoring_messages.DeleteComponentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.DeleteComponentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_component

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def pre_delete_connection(
        self,
        request: authoring_messages.DeleteConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.DeleteConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def pre_delete_policy(
        self,
        request: best_practices_messages.DeletePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.DeletePolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def pre_delete_share(
        self,
        request: sharing_messages.DeleteShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.DeleteShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for delete_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_delete_share(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_share

        DEPRECATED. Please use the `post_delete_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_delete_share` interceptor runs
        before the `post_delete_share_with_metadata` interceptor.
        """
        return response

    def post_delete_share_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_delete_share_with_metadata`
        interceptor in new development instead of the `post_delete_share` interceptor.
        When both interceptors are used, this `post_delete_share_with_metadata` interceptor runs after the
        `post_delete_share` interceptor. The (possibly modified) response returned by
        `post_delete_share` will be passed to
        `post_delete_share_with_metadata`.
        """
        return response, metadata

    def pre_delete_space(
        self,
        request: catalog_management_messages.DeleteSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.DeleteSpaceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def pre_deploy_application(
        self,
        request: deployment_messages.DeployApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.DeployApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deploy_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_deploy_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deploy_application

        DEPRECATED. Please use the `post_deploy_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_deploy_application` interceptor runs
        before the `post_deploy_application_with_metadata` interceptor.
        """
        return response

    def post_deploy_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_deploy_application_with_metadata`
        interceptor in new development instead of the `post_deploy_application` interceptor.
        When both interceptors are used, this `post_deploy_application_with_metadata` interceptor runs after the
        `post_deploy_application` interceptor. The (possibly modified) response returned by
        `post_deploy_application` will be passed to
        `post_deploy_application_with_metadata`.
        """
        return response, metadata

    def pre_export_application_ia_c(
        self,
        request: deployment_messages.ExportApplicationIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.ExportApplicationIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_application_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_export_application_ia_c(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_application_ia_c

        DEPRECATED. Please use the `post_export_application_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_export_application_ia_c` interceptor runs
        before the `post_export_application_ia_c_with_metadata` interceptor.
        """
        return response

    def post_export_application_ia_c_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_application_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_export_application_ia_c_with_metadata`
        interceptor in new development instead of the `post_export_application_ia_c` interceptor.
        When both interceptors are used, this `post_export_application_ia_c_with_metadata` interceptor runs after the
        `post_export_application_ia_c` interceptor. The (possibly modified) response returned by
        `post_export_application_ia_c` will be passed to
        `post_export_application_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_export_application_template_ia_c(
        self,
        request: authoring_messages.ExportApplicationTemplateIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ExportApplicationTemplateIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_application_template_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_export_application_template_ia_c(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_application_template_ia_c

        DEPRECATED. Please use the `post_export_application_template_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_export_application_template_ia_c` interceptor runs
        before the `post_export_application_template_ia_c_with_metadata` interceptor.
        """
        return response

    def post_export_application_template_ia_c_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_application_template_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_export_application_template_ia_c_with_metadata`
        interceptor in new development instead of the `post_export_application_template_ia_c` interceptor.
        When both interceptors are used, this `post_export_application_template_ia_c_with_metadata` interceptor runs after the
        `post_export_application_template_ia_c` interceptor. The (possibly modified) response returned by
        `post_export_application_template_ia_c` will be passed to
        `post_export_application_template_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_export_application_template_revision_ia_c(
        self,
        request: authoring_messages.ExportApplicationTemplateRevisionIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ExportApplicationTemplateRevisionIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_application_template_revision_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_export_application_template_revision_ia_c(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_application_template_revision_ia_c

        DEPRECATED. Please use the `post_export_application_template_revision_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_export_application_template_revision_ia_c` interceptor runs
        before the `post_export_application_template_revision_ia_c_with_metadata` interceptor.
        """
        return response

    def post_export_application_template_revision_ia_c_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_application_template_revision_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_export_application_template_revision_ia_c_with_metadata`
        interceptor in new development instead of the `post_export_application_template_revision_ia_c` interceptor.
        When both interceptors are used, this `post_export_application_template_revision_ia_c_with_metadata` interceptor runs after the
        `post_export_application_template_revision_ia_c` interceptor. The (possibly modified) response returned by
        `post_export_application_template_revision_ia_c` will be passed to
        `post_export_application_template_revision_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_fetch_application_assessment_report(
        self,
        request: best_practices_messages.FetchApplicationAssessmentReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.FetchApplicationAssessmentReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_application_assessment_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_fetch_application_assessment_report(
        self, response: best_practices_messages.FetchApplicationAssessmentReportResponse
    ) -> best_practices_messages.FetchApplicationAssessmentReportResponse:
        """Post-rpc interceptor for fetch_application_assessment_report

        DEPRECATED. Please use the `post_fetch_application_assessment_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_fetch_application_assessment_report` interceptor runs
        before the `post_fetch_application_assessment_report_with_metadata` interceptor.
        """
        return response

    def post_fetch_application_assessment_report_with_metadata(
        self,
        response: best_practices_messages.FetchApplicationAssessmentReportResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.FetchApplicationAssessmentReportResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_application_assessment_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_fetch_application_assessment_report_with_metadata`
        interceptor in new development instead of the `post_fetch_application_assessment_report` interceptor.
        When both interceptors are used, this `post_fetch_application_assessment_report_with_metadata` interceptor runs after the
        `post_fetch_application_assessment_report` interceptor. The (possibly modified) response returned by
        `post_fetch_application_assessment_report` will be passed to
        `post_fetch_application_assessment_report_with_metadata`.
        """
        return response, metadata

    def pre_fetch_frameworks(
        self,
        request: best_practices_messages.FetchFrameworksRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.FetchFrameworksRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for fetch_frameworks

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_fetch_frameworks(
        self, response: best_practices_messages.FetchFrameworksResponse
    ) -> best_practices_messages.FetchFrameworksResponse:
        """Post-rpc interceptor for fetch_frameworks

        DEPRECATED. Please use the `post_fetch_frameworks_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_fetch_frameworks` interceptor runs
        before the `post_fetch_frameworks_with_metadata` interceptor.
        """
        return response

    def post_fetch_frameworks_with_metadata(
        self,
        response: best_practices_messages.FetchFrameworksResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.FetchFrameworksResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for fetch_frameworks

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_fetch_frameworks_with_metadata`
        interceptor in new development instead of the `post_fetch_frameworks` interceptor.
        When both interceptors are used, this `post_fetch_frameworks_with_metadata` interceptor runs after the
        `post_fetch_frameworks` interceptor. The (possibly modified) response returned by
        `post_fetch_frameworks` will be passed to
        `post_fetch_frameworks_with_metadata`.
        """
        return response, metadata

    def pre_generate_application_assessment_report(
        self,
        request: best_practices_messages.GenerateApplicationAssessmentReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.GenerateApplicationAssessmentReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_application_assessment_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_application_assessment_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_application_assessment_report

        DEPRECATED. Please use the `post_generate_application_assessment_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_application_assessment_report` interceptor runs
        before the `post_generate_application_assessment_report_with_metadata` interceptor.
        """
        return response

    def post_generate_application_assessment_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_application_assessment_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_application_assessment_report_with_metadata`
        interceptor in new development instead of the `post_generate_application_assessment_report` interceptor.
        When both interceptors are used, this `post_generate_application_assessment_report_with_metadata` interceptor runs after the
        `post_generate_application_assessment_report` interceptor. The (possibly modified) response returned by
        `post_generate_application_assessment_report` will be passed to
        `post_generate_application_assessment_report_with_metadata`.
        """
        return response, metadata

    def pre_generate_application_ia_c(
        self,
        request: deployment_messages.GenerateApplicationIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.GenerateApplicationIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_application_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_application_ia_c(
        self, response: deployment_messages.GenerateApplicationIaCResponse
    ) -> deployment_messages.GenerateApplicationIaCResponse:
        """Post-rpc interceptor for generate_application_ia_c

        DEPRECATED. Please use the `post_generate_application_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_application_ia_c` interceptor runs
        before the `post_generate_application_ia_c_with_metadata` interceptor.
        """
        return response

    def post_generate_application_ia_c_with_metadata(
        self,
        response: deployment_messages.GenerateApplicationIaCResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.GenerateApplicationIaCResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_application_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_application_ia_c_with_metadata`
        interceptor in new development instead of the `post_generate_application_ia_c` interceptor.
        When both interceptors are used, this `post_generate_application_ia_c_with_metadata` interceptor runs after the
        `post_generate_application_ia_c` interceptor. The (possibly modified) response returned by
        `post_generate_application_ia_c` will be passed to
        `post_generate_application_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_generate_application_template_assessment_report(
        self,
        request: best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_application_template_assessment_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_application_template_assessment_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_application_template_assessment_report

        DEPRECATED. Please use the `post_generate_application_template_assessment_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_application_template_assessment_report` interceptor runs
        before the `post_generate_application_template_assessment_report_with_metadata` interceptor.
        """
        return response

    def post_generate_application_template_assessment_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_application_template_assessment_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_application_template_assessment_report_with_metadata`
        interceptor in new development instead of the `post_generate_application_template_assessment_report` interceptor.
        When both interceptors are used, this `post_generate_application_template_assessment_report_with_metadata` interceptor runs after the
        `post_generate_application_template_assessment_report` interceptor. The (possibly modified) response returned by
        `post_generate_application_template_assessment_report` will be passed to
        `post_generate_application_template_assessment_report_with_metadata`.
        """
        return response, metadata

    def pre_generate_application_template_ia_c(
        self,
        request: authoring_messages.GenerateApplicationTemplateIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GenerateApplicationTemplateIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_application_template_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_application_template_ia_c(
        self, response: authoring_messages.GenerateApplicationTemplateIaCResponse
    ) -> authoring_messages.GenerateApplicationTemplateIaCResponse:
        """Post-rpc interceptor for generate_application_template_ia_c

        DEPRECATED. Please use the `post_generate_application_template_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_application_template_ia_c` interceptor runs
        before the `post_generate_application_template_ia_c_with_metadata` interceptor.
        """
        return response

    def post_generate_application_template_ia_c_with_metadata(
        self,
        response: authoring_messages.GenerateApplicationTemplateIaCResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GenerateApplicationTemplateIaCResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_application_template_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_application_template_ia_c_with_metadata`
        interceptor in new development instead of the `post_generate_application_template_ia_c` interceptor.
        When both interceptors are used, this `post_generate_application_template_ia_c_with_metadata` interceptor runs after the
        `post_generate_application_template_ia_c` interceptor. The (possibly modified) response returned by
        `post_generate_application_template_ia_c` will be passed to
        `post_generate_application_template_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_generate_application_template_revision_ia_c(
        self,
        request: authoring_messages.GenerateApplicationTemplateRevisionIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GenerateApplicationTemplateRevisionIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_application_template_revision_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_application_template_revision_ia_c(
        self,
        response: authoring_messages.GenerateApplicationTemplateRevisionIaCResponse,
    ) -> authoring_messages.GenerateApplicationTemplateRevisionIaCResponse:
        """Post-rpc interceptor for generate_application_template_revision_ia_c

        DEPRECATED. Please use the `post_generate_application_template_revision_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_application_template_revision_ia_c` interceptor runs
        before the `post_generate_application_template_revision_ia_c_with_metadata` interceptor.
        """
        return response

    def post_generate_application_template_revision_ia_c_with_metadata(
        self,
        response: authoring_messages.GenerateApplicationTemplateRevisionIaCResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GenerateApplicationTemplateRevisionIaCResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for generate_application_template_revision_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_application_template_revision_ia_c_with_metadata`
        interceptor in new development instead of the `post_generate_application_template_revision_ia_c` interceptor.
        When both interceptors are used, this `post_generate_application_template_revision_ia_c_with_metadata` interceptor runs after the
        `post_generate_application_template_revision_ia_c` interceptor. The (possibly modified) response returned by
        `post_generate_application_template_revision_ia_c` will be passed to
        `post_generate_application_template_revision_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_generate_assessment_report(
        self,
        request: best_practices_messages.GenerateAssessmentReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.GenerateAssessmentReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_assessment_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_assessment_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_assessment_report

        DEPRECATED. Please use the `post_generate_assessment_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_assessment_report` interceptor runs
        before the `post_generate_assessment_report_with_metadata` interceptor.
        """
        return response

    def post_generate_assessment_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_assessment_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_assessment_report_with_metadata`
        interceptor in new development instead of the `post_generate_assessment_report` interceptor.
        When both interceptors are used, this `post_generate_assessment_report_with_metadata` interceptor runs after the
        `post_generate_assessment_report` interceptor. The (possibly modified) response returned by
        `post_generate_assessment_report` will be passed to
        `post_generate_assessment_report_with_metadata`.
        """
        return response, metadata

    def pre_generate_terraform_plan_assessment_report(
        self,
        request: best_practices_messages.GenerateTerraformPlanAssessmentReportRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.GenerateTerraformPlanAssessmentReportRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for generate_terraform_plan_assessment_report

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_generate_terraform_plan_assessment_report(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for generate_terraform_plan_assessment_report

        DEPRECATED. Please use the `post_generate_terraform_plan_assessment_report_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_generate_terraform_plan_assessment_report` interceptor runs
        before the `post_generate_terraform_plan_assessment_report_with_metadata` interceptor.
        """
        return response

    def post_generate_terraform_plan_assessment_report_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for generate_terraform_plan_assessment_report

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_generate_terraform_plan_assessment_report_with_metadata`
        interceptor in new development instead of the `post_generate_terraform_plan_assessment_report` interceptor.
        When both interceptors are used, this `post_generate_terraform_plan_assessment_report_with_metadata` interceptor runs after the
        `post_generate_terraform_plan_assessment_report` interceptor. The (possibly modified) response returned by
        `post_generate_terraform_plan_assessment_report` will be passed to
        `post_generate_terraform_plan_assessment_report_with_metadata`.
        """
        return response, metadata

    def pre_get_application(
        self,
        request: deployment_messages.GetApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.GetApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_application(
        self, response: deployment_resources.Application
    ) -> deployment_resources.Application:
        """Post-rpc interceptor for get_application

        DEPRECATED. Please use the `post_get_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_application` interceptor runs
        before the `post_get_application_with_metadata` interceptor.
        """
        return response

    def post_get_application_with_metadata(
        self,
        response: deployment_resources.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_resources.Application, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_application_with_metadata`
        interceptor in new development instead of the `post_get_application` interceptor.
        When both interceptors are used, this `post_get_application_with_metadata` interceptor runs after the
        `post_get_application` interceptor. The (possibly modified) response returned by
        `post_get_application` will be passed to
        `post_get_application_with_metadata`.
        """
        return response, metadata

    def pre_get_application_template(
        self,
        request: authoring_messages.GetApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GetApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_application_template(
        self, response: authoring.ApplicationTemplate
    ) -> authoring.ApplicationTemplate:
        """Post-rpc interceptor for get_application_template

        DEPRECATED. Please use the `post_get_application_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_application_template` interceptor runs
        before the `post_get_application_template_with_metadata` interceptor.
        """
        return response

    def post_get_application_template_with_metadata(
        self,
        response: authoring.ApplicationTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.ApplicationTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_application_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_application_template_with_metadata`
        interceptor in new development instead of the `post_get_application_template` interceptor.
        When both interceptors are used, this `post_get_application_template_with_metadata` interceptor runs after the
        `post_get_application_template` interceptor. The (possibly modified) response returned by
        `post_get_application_template` will be passed to
        `post_get_application_template_with_metadata`.
        """
        return response, metadata

    def pre_get_application_template_revision(
        self,
        request: authoring_messages.GetApplicationTemplateRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GetApplicationTemplateRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_application_template_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_application_template_revision(
        self, response: authoring.ApplicationTemplateRevision
    ) -> authoring.ApplicationTemplateRevision:
        """Post-rpc interceptor for get_application_template_revision

        DEPRECATED. Please use the `post_get_application_template_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_application_template_revision` interceptor runs
        before the `post_get_application_template_revision_with_metadata` interceptor.
        """
        return response

    def post_get_application_template_revision_with_metadata(
        self,
        response: authoring.ApplicationTemplateRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring.ApplicationTemplateRevision, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_application_template_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_application_template_revision_with_metadata`
        interceptor in new development instead of the `post_get_application_template_revision` interceptor.
        When both interceptors are used, this `post_get_application_template_revision_with_metadata` interceptor runs after the
        `post_get_application_template_revision` interceptor. The (possibly modified) response returned by
        `post_get_application_template_revision` will be passed to
        `post_get_application_template_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_application_template_system_revision(
        self,
        request: authoring_messages.GetApplicationTemplateSystemRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GetApplicationTemplateSystemRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_application_template_system_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_application_template_system_revision(
        self, response: authoring.ApplicationTemplateSystemRevision
    ) -> authoring.ApplicationTemplateSystemRevision:
        """Post-rpc interceptor for get_application_template_system_revision

        DEPRECATED. Please use the `post_get_application_template_system_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_application_template_system_revision` interceptor runs
        before the `post_get_application_template_system_revision_with_metadata` interceptor.
        """
        return response

    def post_get_application_template_system_revision_with_metadata(
        self,
        response: authoring.ApplicationTemplateSystemRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring.ApplicationTemplateSystemRevision,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_application_template_system_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_application_template_system_revision_with_metadata`
        interceptor in new development instead of the `post_get_application_template_system_revision` interceptor.
        When both interceptors are used, this `post_get_application_template_system_revision_with_metadata` interceptor runs after the
        `post_get_application_template_system_revision` interceptor. The (possibly modified) response returned by
        `post_get_application_template_system_revision` will be passed to
        `post_get_application_template_system_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_catalog(
        self,
        request: catalog_management_messages.GetCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.GetCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_catalog(
        self, response: catalog_management.Catalog
    ) -> catalog_management.Catalog:
        """Post-rpc interceptor for get_catalog

        DEPRECATED. Please use the `post_get_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_catalog` interceptor runs
        before the `post_get_catalog_with_metadata` interceptor.
        """
        return response

    def post_get_catalog_with_metadata(
        self,
        response: catalog_management.Catalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog_management.Catalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_catalog_with_metadata`
        interceptor in new development instead of the `post_get_catalog` interceptor.
        When both interceptors are used, this `post_get_catalog_with_metadata` interceptor runs after the
        `post_get_catalog` interceptor. The (possibly modified) response returned by
        `post_get_catalog` will be passed to
        `post_get_catalog_with_metadata`.
        """
        return response, metadata

    def pre_get_catalog_template(
        self,
        request: catalog_management_messages.GetCatalogTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.GetCatalogTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_catalog_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_catalog_template(
        self, response: catalog_management.CatalogTemplate
    ) -> catalog_management.CatalogTemplate:
        """Post-rpc interceptor for get_catalog_template

        DEPRECATED. Please use the `post_get_catalog_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_catalog_template` interceptor runs
        before the `post_get_catalog_template_with_metadata` interceptor.
        """
        return response

    def post_get_catalog_template_with_metadata(
        self,
        response: catalog_management.CatalogTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management.CatalogTemplate, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for get_catalog_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_catalog_template_with_metadata`
        interceptor in new development instead of the `post_get_catalog_template` interceptor.
        When both interceptors are used, this `post_get_catalog_template_with_metadata` interceptor runs after the
        `post_get_catalog_template` interceptor. The (possibly modified) response returned by
        `post_get_catalog_template` will be passed to
        `post_get_catalog_template_with_metadata`.
        """
        return response, metadata

    def pre_get_catalog_template_revision(
        self,
        request: catalog_management_messages.GetCatalogTemplateRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.GetCatalogTemplateRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_catalog_template_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_catalog_template_revision(
        self, response: catalog_management.CatalogTemplateRevision
    ) -> catalog_management.CatalogTemplateRevision:
        """Post-rpc interceptor for get_catalog_template_revision

        DEPRECATED. Please use the `post_get_catalog_template_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_catalog_template_revision` interceptor runs
        before the `post_get_catalog_template_revision_with_metadata` interceptor.
        """
        return response

    def post_get_catalog_template_revision_with_metadata(
        self,
        response: catalog_management.CatalogTemplateRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management.CatalogTemplateRevision,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for get_catalog_template_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_catalog_template_revision_with_metadata`
        interceptor in new development instead of the `post_get_catalog_template_revision` interceptor.
        When both interceptors are used, this `post_get_catalog_template_revision_with_metadata` interceptor runs after the
        `post_get_catalog_template_revision` interceptor. The (possibly modified) response returned by
        `post_get_catalog_template_revision` will be passed to
        `post_get_catalog_template_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_component(
        self,
        request: authoring_messages.GetComponentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GetComponentRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_component

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_component(self, response: authoring.Component) -> authoring.Component:
        """Post-rpc interceptor for get_component

        DEPRECATED. Please use the `post_get_component_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_component` interceptor runs
        before the `post_get_component_with_metadata` interceptor.
        """
        return response

    def post_get_component_with_metadata(
        self,
        response: authoring.Component,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.Component, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_component

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_component_with_metadata`
        interceptor in new development instead of the `post_get_component` interceptor.
        When both interceptors are used, this `post_get_component_with_metadata` interceptor runs after the
        `post_get_component` interceptor. The (possibly modified) response returned by
        `post_get_component` will be passed to
        `post_get_component_with_metadata`.
        """
        return response, metadata

    def pre_get_connection(
        self,
        request: authoring_messages.GetConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.GetConnectionRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_connection(
        self, response: authoring.Connection
    ) -> authoring.Connection:
        """Post-rpc interceptor for get_connection

        DEPRECATED. Please use the `post_get_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_connection` interceptor runs
        before the `post_get_connection_with_metadata` interceptor.
        """
        return response

    def post_get_connection_with_metadata(
        self,
        response: authoring.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_connection_with_metadata`
        interceptor in new development instead of the `post_get_connection` interceptor.
        When both interceptors are used, this `post_get_connection_with_metadata` interceptor runs after the
        `post_get_connection` interceptor. The (possibly modified) response returned by
        `post_get_connection` will be passed to
        `post_get_connection_with_metadata`.
        """
        return response, metadata

    def pre_get_policy(
        self,
        request: best_practices_messages.GetPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.GetPolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_policy(self, response: best_practices.Policy) -> best_practices.Policy:
        """Post-rpc interceptor for get_policy

        DEPRECATED. Please use the `post_get_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_policy` interceptor runs
        before the `post_get_policy_with_metadata` interceptor.
        """
        return response

    def post_get_policy_with_metadata(
        self,
        response: best_practices.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[best_practices.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_policy_with_metadata`
        interceptor in new development instead of the `post_get_policy` interceptor.
        When both interceptors are used, this `post_get_policy_with_metadata` interceptor runs after the
        `post_get_policy` interceptor. The (possibly modified) response returned by
        `post_get_policy` will be passed to
        `post_get_policy_with_metadata`.
        """
        return response, metadata

    def pre_get_share(
        self,
        request: sharing_messages.GetShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.GetShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_share(self, response: sharing.Share) -> sharing.Share:
        """Post-rpc interceptor for get_share

        DEPRECATED. Please use the `post_get_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_share` interceptor runs
        before the `post_get_share_with_metadata` interceptor.
        """
        return response

    def post_get_share_with_metadata(
        self, response: sharing.Share, metadata: Sequence[Tuple[str, Union[str, bytes]]]
    ) -> Tuple[sharing.Share, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_share_with_metadata`
        interceptor in new development instead of the `post_get_share` interceptor.
        When both interceptors are used, this `post_get_share_with_metadata` interceptor runs after the
        `post_get_share` interceptor. The (possibly modified) response returned by
        `post_get_share` will be passed to
        `post_get_share_with_metadata`.
        """
        return response, metadata

    def pre_get_shared_template(
        self,
        request: sharing_messages.GetSharedTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.GetSharedTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_shared_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_shared_template(
        self, response: sharing.SharedTemplate
    ) -> sharing.SharedTemplate:
        """Post-rpc interceptor for get_shared_template

        DEPRECATED. Please use the `post_get_shared_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_shared_template` interceptor runs
        before the `post_get_shared_template_with_metadata` interceptor.
        """
        return response

    def post_get_shared_template_with_metadata(
        self,
        response: sharing.SharedTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sharing.SharedTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_shared_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_shared_template_with_metadata`
        interceptor in new development instead of the `post_get_shared_template` interceptor.
        When both interceptors are used, this `post_get_shared_template_with_metadata` interceptor runs after the
        `post_get_shared_template` interceptor. The (possibly modified) response returned by
        `post_get_shared_template` will be passed to
        `post_get_shared_template_with_metadata`.
        """
        return response, metadata

    def pre_get_shared_template_revision(
        self,
        request: sharing_messages.GetSharedTemplateRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.GetSharedTemplateRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_shared_template_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_shared_template_revision(
        self, response: sharing.SharedTemplateRevision
    ) -> sharing.SharedTemplateRevision:
        """Post-rpc interceptor for get_shared_template_revision

        DEPRECATED. Please use the `post_get_shared_template_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_shared_template_revision` interceptor runs
        before the `post_get_shared_template_revision_with_metadata` interceptor.
        """
        return response

    def post_get_shared_template_revision_with_metadata(
        self,
        response: sharing.SharedTemplateRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[sharing.SharedTemplateRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_shared_template_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_shared_template_revision_with_metadata`
        interceptor in new development instead of the `post_get_shared_template_revision` interceptor.
        When both interceptors are used, this `post_get_shared_template_revision_with_metadata` interceptor runs after the
        `post_get_shared_template_revision` interceptor. The (possibly modified) response returned by
        `post_get_shared_template_revision` will be passed to
        `post_get_shared_template_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_space(
        self,
        request: catalog_management_messages.GetSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.GetSpaceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_space(
        self, response: catalog_management.Space
    ) -> catalog_management.Space:
        """Post-rpc interceptor for get_space

        DEPRECATED. Please use the `post_get_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_get_space` interceptor runs
        before the `post_get_space_with_metadata` interceptor.
        """
        return response

    def post_get_space_with_metadata(
        self,
        response: catalog_management.Space,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog_management.Space, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_get_space_with_metadata`
        interceptor in new development instead of the `post_get_space` interceptor.
        When both interceptors are used, this `post_get_space_with_metadata` interceptor runs after the
        `post_get_space` interceptor. The (possibly modified) response returned by
        `post_get_space` will be passed to
        `post_get_space_with_metadata`.
        """
        return response, metadata

    def pre_import_application_ia_c(
        self,
        request: deployment_messages.ImportApplicationIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.ImportApplicationIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_application_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_import_application_ia_c(
        self, response: deployment_messages.ImportApplicationIaCResponse
    ) -> deployment_messages.ImportApplicationIaCResponse:
        """Post-rpc interceptor for import_application_ia_c

        DEPRECATED. Please use the `post_import_application_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_import_application_ia_c` interceptor runs
        before the `post_import_application_ia_c_with_metadata` interceptor.
        """
        return response

    def post_import_application_ia_c_with_metadata(
        self,
        response: deployment_messages.ImportApplicationIaCResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.ImportApplicationIaCResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for import_application_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_import_application_ia_c_with_metadata`
        interceptor in new development instead of the `post_import_application_ia_c` interceptor.
        When both interceptors are used, this `post_import_application_ia_c_with_metadata` interceptor runs after the
        `post_import_application_ia_c` interceptor. The (possibly modified) response returned by
        `post_import_application_ia_c` will be passed to
        `post_import_application_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_import_application_template(
        self,
        request: authoring_messages.ImportApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ImportApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_import_application_template(
        self, response: authoring.ApplicationTemplate
    ) -> authoring.ApplicationTemplate:
        """Post-rpc interceptor for import_application_template

        DEPRECATED. Please use the `post_import_application_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_import_application_template` interceptor runs
        before the `post_import_application_template_with_metadata` interceptor.
        """
        return response

    def post_import_application_template_with_metadata(
        self,
        response: authoring.ApplicationTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.ApplicationTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_application_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_import_application_template_with_metadata`
        interceptor in new development instead of the `post_import_application_template` interceptor.
        When both interceptors are used, this `post_import_application_template_with_metadata` interceptor runs after the
        `post_import_application_template` interceptor. The (possibly modified) response returned by
        `post_import_application_template` will be passed to
        `post_import_application_template_with_metadata`.
        """
        return response, metadata

    def pre_import_application_template_ia_c(
        self,
        request: authoring_messages.ImportApplicationTemplateIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ImportApplicationTemplateIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_application_template_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_import_application_template_ia_c(
        self, response: authoring_messages.ImportApplicationTemplateIaCResponse
    ) -> authoring_messages.ImportApplicationTemplateIaCResponse:
        """Post-rpc interceptor for import_application_template_ia_c

        DEPRECATED. Please use the `post_import_application_template_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_import_application_template_ia_c` interceptor runs
        before the `post_import_application_template_ia_c_with_metadata` interceptor.
        """
        return response

    def post_import_application_template_ia_c_with_metadata(
        self,
        response: authoring_messages.ImportApplicationTemplateIaCResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ImportApplicationTemplateIaCResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for import_application_template_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_import_application_template_ia_c_with_metadata`
        interceptor in new development instead of the `post_import_application_template_ia_c` interceptor.
        When both interceptors are used, this `post_import_application_template_ia_c_with_metadata` interceptor runs after the
        `post_import_application_template_ia_c` interceptor. The (possibly modified) response returned by
        `post_import_application_template_ia_c` will be passed to
        `post_import_application_template_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_ingest_application_template_ia_c(
        self,
        request: authoring_messages.IngestApplicationTemplateIaCRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.IngestApplicationTemplateIaCRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for ingest_application_template_ia_c

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_ingest_application_template_ia_c(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for ingest_application_template_ia_c

        DEPRECATED. Please use the `post_ingest_application_template_ia_c_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_ingest_application_template_ia_c` interceptor runs
        before the `post_ingest_application_template_ia_c_with_metadata` interceptor.
        """
        return response

    def post_ingest_application_template_ia_c_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for ingest_application_template_ia_c

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_ingest_application_template_ia_c_with_metadata`
        interceptor in new development instead of the `post_ingest_application_template_ia_c` interceptor.
        When both interceptors are used, this `post_ingest_application_template_ia_c_with_metadata` interceptor runs after the
        `post_ingest_application_template_ia_c` interceptor. The (possibly modified) response returned by
        `post_ingest_application_template_ia_c` will be passed to
        `post_ingest_application_template_ia_c_with_metadata`.
        """
        return response, metadata

    def pre_list_applications(
        self,
        request: deployment_messages.ListApplicationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.ListApplicationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_applications

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_applications(
        self, response: deployment_messages.ListApplicationsResponse
    ) -> deployment_messages.ListApplicationsResponse:
        """Post-rpc interceptor for list_applications

        DEPRECATED. Please use the `post_list_applications_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_applications` interceptor runs
        before the `post_list_applications_with_metadata` interceptor.
        """
        return response

    def post_list_applications_with_metadata(
        self,
        response: deployment_messages.ListApplicationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.ListApplicationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_applications

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_applications_with_metadata`
        interceptor in new development instead of the `post_list_applications` interceptor.
        When both interceptors are used, this `post_list_applications_with_metadata` interceptor runs after the
        `post_list_applications` interceptor. The (possibly modified) response returned by
        `post_list_applications` will be passed to
        `post_list_applications_with_metadata`.
        """
        return response, metadata

    def pre_list_application_template_revisions(
        self,
        request: authoring_messages.ListApplicationTemplateRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListApplicationTemplateRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_application_template_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_application_template_revisions(
        self, response: authoring_messages.ListApplicationTemplateRevisionsResponse
    ) -> authoring_messages.ListApplicationTemplateRevisionsResponse:
        """Post-rpc interceptor for list_application_template_revisions

        DEPRECATED. Please use the `post_list_application_template_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_application_template_revisions` interceptor runs
        before the `post_list_application_template_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_application_template_revisions_with_metadata(
        self,
        response: authoring_messages.ListApplicationTemplateRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListApplicationTemplateRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_application_template_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_application_template_revisions_with_metadata`
        interceptor in new development instead of the `post_list_application_template_revisions` interceptor.
        When both interceptors are used, this `post_list_application_template_revisions_with_metadata` interceptor runs after the
        `post_list_application_template_revisions` interceptor. The (possibly modified) response returned by
        `post_list_application_template_revisions` will be passed to
        `post_list_application_template_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_application_templates(
        self,
        request: authoring_messages.ListApplicationTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListApplicationTemplatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_application_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_application_templates(
        self, response: authoring_messages.ListApplicationTemplatesResponse
    ) -> authoring_messages.ListApplicationTemplatesResponse:
        """Post-rpc interceptor for list_application_templates

        DEPRECATED. Please use the `post_list_application_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_application_templates` interceptor runs
        before the `post_list_application_templates_with_metadata` interceptor.
        """
        return response

    def post_list_application_templates_with_metadata(
        self,
        response: authoring_messages.ListApplicationTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListApplicationTemplatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_application_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_application_templates_with_metadata`
        interceptor in new development instead of the `post_list_application_templates` interceptor.
        When both interceptors are used, this `post_list_application_templates_with_metadata` interceptor runs after the
        `post_list_application_templates` interceptor. The (possibly modified) response returned by
        `post_list_application_templates` will be passed to
        `post_list_application_templates_with_metadata`.
        """
        return response, metadata

    def pre_list_application_template_system_revisions(
        self,
        request: authoring_messages.ListApplicationTemplateSystemRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListApplicationTemplateSystemRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_application_template_system_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_application_template_system_revisions(
        self,
        response: authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
    ) -> authoring_messages.ListApplicationTemplateSystemRevisionsResponse:
        """Post-rpc interceptor for list_application_template_system_revisions

        DEPRECATED. Please use the `post_list_application_template_system_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_application_template_system_revisions` interceptor runs
        before the `post_list_application_template_system_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_application_template_system_revisions_with_metadata(
        self,
        response: authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_application_template_system_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_application_template_system_revisions_with_metadata`
        interceptor in new development instead of the `post_list_application_template_system_revisions` interceptor.
        When both interceptors are used, this `post_list_application_template_system_revisions_with_metadata` interceptor runs after the
        `post_list_application_template_system_revisions` interceptor. The (possibly modified) response returned by
        `post_list_application_template_system_revisions` will be passed to
        `post_list_application_template_system_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_catalogs(
        self,
        request: catalog_management_messages.ListCatalogsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListCatalogsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_catalogs

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_catalogs(
        self, response: catalog_management_messages.ListCatalogsResponse
    ) -> catalog_management_messages.ListCatalogsResponse:
        """Post-rpc interceptor for list_catalogs

        DEPRECATED. Please use the `post_list_catalogs_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_catalogs` interceptor runs
        before the `post_list_catalogs_with_metadata` interceptor.
        """
        return response

    def post_list_catalogs_with_metadata(
        self,
        response: catalog_management_messages.ListCatalogsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListCatalogsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_catalogs

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_catalogs_with_metadata`
        interceptor in new development instead of the `post_list_catalogs` interceptor.
        When both interceptors are used, this `post_list_catalogs_with_metadata` interceptor runs after the
        `post_list_catalogs` interceptor. The (possibly modified) response returned by
        `post_list_catalogs` will be passed to
        `post_list_catalogs_with_metadata`.
        """
        return response, metadata

    def pre_list_catalog_template_revisions(
        self,
        request: catalog_management_messages.ListCatalogTemplateRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListCatalogTemplateRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_catalog_template_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_catalog_template_revisions(
        self, response: catalog_management_messages.ListCatalogTemplateRevisionsResponse
    ) -> catalog_management_messages.ListCatalogTemplateRevisionsResponse:
        """Post-rpc interceptor for list_catalog_template_revisions

        DEPRECATED. Please use the `post_list_catalog_template_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_catalog_template_revisions` interceptor runs
        before the `post_list_catalog_template_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_catalog_template_revisions_with_metadata(
        self,
        response: catalog_management_messages.ListCatalogTemplateRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListCatalogTemplateRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_catalog_template_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_catalog_template_revisions_with_metadata`
        interceptor in new development instead of the `post_list_catalog_template_revisions` interceptor.
        When both interceptors are used, this `post_list_catalog_template_revisions_with_metadata` interceptor runs after the
        `post_list_catalog_template_revisions` interceptor. The (possibly modified) response returned by
        `post_list_catalog_template_revisions` will be passed to
        `post_list_catalog_template_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_catalog_templates(
        self,
        request: catalog_management_messages.ListCatalogTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListCatalogTemplatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_catalog_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_catalog_templates(
        self, response: catalog_management_messages.ListCatalogTemplatesResponse
    ) -> catalog_management_messages.ListCatalogTemplatesResponse:
        """Post-rpc interceptor for list_catalog_templates

        DEPRECATED. Please use the `post_list_catalog_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_catalog_templates` interceptor runs
        before the `post_list_catalog_templates_with_metadata` interceptor.
        """
        return response

    def post_list_catalog_templates_with_metadata(
        self,
        response: catalog_management_messages.ListCatalogTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListCatalogTemplatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_catalog_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_catalog_templates_with_metadata`
        interceptor in new development instead of the `post_list_catalog_templates` interceptor.
        When both interceptors are used, this `post_list_catalog_templates_with_metadata` interceptor runs after the
        `post_list_catalog_templates` interceptor. The (possibly modified) response returned by
        `post_list_catalog_templates` will be passed to
        `post_list_catalog_templates_with_metadata`.
        """
        return response, metadata

    def pre_list_components(
        self,
        request: authoring_messages.ListComponentsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListComponentsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_components

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_components(
        self, response: authoring_messages.ListComponentsResponse
    ) -> authoring_messages.ListComponentsResponse:
        """Post-rpc interceptor for list_components

        DEPRECATED. Please use the `post_list_components_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_components` interceptor runs
        before the `post_list_components_with_metadata` interceptor.
        """
        return response

    def post_list_components_with_metadata(
        self,
        response: authoring_messages.ListComponentsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListComponentsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_components

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_components_with_metadata`
        interceptor in new development instead of the `post_list_components` interceptor.
        When both interceptors are used, this `post_list_components_with_metadata` interceptor runs after the
        `post_list_components` interceptor. The (possibly modified) response returned by
        `post_list_components` will be passed to
        `post_list_components_with_metadata`.
        """
        return response, metadata

    def pre_list_connections(
        self,
        request: authoring_messages.ListConnectionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListConnectionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_connections

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_connections(
        self, response: authoring_messages.ListConnectionsResponse
    ) -> authoring_messages.ListConnectionsResponse:
        """Post-rpc interceptor for list_connections

        DEPRECATED. Please use the `post_list_connections_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_connections` interceptor runs
        before the `post_list_connections_with_metadata` interceptor.
        """
        return response

    def post_list_connections_with_metadata(
        self,
        response: authoring_messages.ListConnectionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.ListConnectionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_connections

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_connections_with_metadata`
        interceptor in new development instead of the `post_list_connections` interceptor.
        When both interceptors are used, this `post_list_connections_with_metadata` interceptor runs after the
        `post_list_connections` interceptor. The (possibly modified) response returned by
        `post_list_connections` will be passed to
        `post_list_connections_with_metadata`.
        """
        return response, metadata

    def pre_list_policies(
        self,
        request: best_practices_messages.ListPoliciesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.ListPoliciesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_policies

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_policies(
        self, response: best_practices_messages.ListPoliciesResponse
    ) -> best_practices_messages.ListPoliciesResponse:
        """Post-rpc interceptor for list_policies

        DEPRECATED. Please use the `post_list_policies_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_policies` interceptor runs
        before the `post_list_policies_with_metadata` interceptor.
        """
        return response

    def post_list_policies_with_metadata(
        self,
        response: best_practices_messages.ListPoliciesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.ListPoliciesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_policies

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_policies_with_metadata`
        interceptor in new development instead of the `post_list_policies` interceptor.
        When both interceptors are used, this `post_list_policies_with_metadata` interceptor runs after the
        `post_list_policies` interceptor. The (possibly modified) response returned by
        `post_list_policies` will be passed to
        `post_list_policies_with_metadata`.
        """
        return response, metadata

    def pre_list_shared_template_revisions(
        self,
        request: sharing_messages.ListSharedTemplateRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.ListSharedTemplateRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_shared_template_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_shared_template_revisions(
        self, response: sharing_messages.ListSharedTemplateRevisionsResponse
    ) -> sharing_messages.ListSharedTemplateRevisionsResponse:
        """Post-rpc interceptor for list_shared_template_revisions

        DEPRECATED. Please use the `post_list_shared_template_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_shared_template_revisions` interceptor runs
        before the `post_list_shared_template_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_shared_template_revisions_with_metadata(
        self,
        response: sharing_messages.ListSharedTemplateRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.ListSharedTemplateRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_shared_template_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_shared_template_revisions_with_metadata`
        interceptor in new development instead of the `post_list_shared_template_revisions` interceptor.
        When both interceptors are used, this `post_list_shared_template_revisions_with_metadata` interceptor runs after the
        `post_list_shared_template_revisions` interceptor. The (possibly modified) response returned by
        `post_list_shared_template_revisions` will be passed to
        `post_list_shared_template_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_shared_templates(
        self,
        request: sharing_messages.ListSharedTemplatesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.ListSharedTemplatesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_shared_templates

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_shared_templates(
        self, response: sharing_messages.ListSharedTemplatesResponse
    ) -> sharing_messages.ListSharedTemplatesResponse:
        """Post-rpc interceptor for list_shared_templates

        DEPRECATED. Please use the `post_list_shared_templates_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_shared_templates` interceptor runs
        before the `post_list_shared_templates_with_metadata` interceptor.
        """
        return response

    def post_list_shared_templates_with_metadata(
        self,
        response: sharing_messages.ListSharedTemplatesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.ListSharedTemplatesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_shared_templates

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_shared_templates_with_metadata`
        interceptor in new development instead of the `post_list_shared_templates` interceptor.
        When both interceptors are used, this `post_list_shared_templates_with_metadata` interceptor runs after the
        `post_list_shared_templates` interceptor. The (possibly modified) response returned by
        `post_list_shared_templates` will be passed to
        `post_list_shared_templates_with_metadata`.
        """
        return response, metadata

    def pre_list_shares(
        self,
        request: sharing_messages.ListSharesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.ListSharesRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for list_shares

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_shares(
        self, response: sharing_messages.ListSharesResponse
    ) -> sharing_messages.ListSharesResponse:
        """Post-rpc interceptor for list_shares

        DEPRECATED. Please use the `post_list_shares_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_shares` interceptor runs
        before the `post_list_shares_with_metadata` interceptor.
        """
        return response

    def post_list_shares_with_metadata(
        self,
        response: sharing_messages.ListSharesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.ListSharesResponse, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for list_shares

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_shares_with_metadata`
        interceptor in new development instead of the `post_list_shares` interceptor.
        When both interceptors are used, this `post_list_shares_with_metadata` interceptor runs after the
        `post_list_shares` interceptor. The (possibly modified) response returned by
        `post_list_shares` will be passed to
        `post_list_shares_with_metadata`.
        """
        return response, metadata

    def pre_list_spaces(
        self,
        request: catalog_management_messages.ListSpacesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListSpacesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_spaces

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_spaces(
        self, response: catalog_management_messages.ListSpacesResponse
    ) -> catalog_management_messages.ListSpacesResponse:
        """Post-rpc interceptor for list_spaces

        DEPRECATED. Please use the `post_list_spaces_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_list_spaces` interceptor runs
        before the `post_list_spaces_with_metadata` interceptor.
        """
        return response

    def post_list_spaces_with_metadata(
        self,
        response: catalog_management_messages.ListSpacesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.ListSpacesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_spaces

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_list_spaces_with_metadata`
        interceptor in new development instead of the `post_list_spaces` interceptor.
        When both interceptors are used, this `post_list_spaces_with_metadata` interceptor runs after the
        `post_list_spaces` interceptor. The (possibly modified) response returned by
        `post_list_spaces` will be passed to
        `post_list_spaces_with_metadata`.
        """
        return response, metadata

    def pre_preview_application(
        self,
        request: deployment_messages.PreviewApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.PreviewApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for preview_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_preview_application(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for preview_application

        DEPRECATED. Please use the `post_preview_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_preview_application` interceptor runs
        before the `post_preview_application_with_metadata` interceptor.
        """
        return response

    def post_preview_application_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for preview_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_preview_application_with_metadata`
        interceptor in new development instead of the `post_preview_application` interceptor.
        When both interceptors are used, this `post_preview_application_with_metadata` interceptor runs after the
        `post_preview_application` interceptor. The (possibly modified) response returned by
        `post_preview_application` will be passed to
        `post_preview_application_with_metadata`.
        """
        return response, metadata

    def pre_recommend_iam_roles(
        self,
        request: deployment_messages.RecommendIAMRolesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.RecommendIAMRolesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for recommend_iam_roles

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_recommend_iam_roles(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for recommend_iam_roles

        DEPRECATED. Please use the `post_recommend_iam_roles_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_recommend_iam_roles` interceptor runs
        before the `post_recommend_iam_roles_with_metadata` interceptor.
        """
        return response

    def post_recommend_iam_roles_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for recommend_iam_roles

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_recommend_iam_roles_with_metadata`
        interceptor in new development instead of the `post_recommend_iam_roles` interceptor.
        When both interceptors are used, this `post_recommend_iam_roles_with_metadata` interceptor runs after the
        `post_recommend_iam_roles` interceptor. The (possibly modified) response returned by
        `post_recommend_iam_roles` will be passed to
        `post_recommend_iam_roles_with_metadata`.
        """
        return response, metadata

    def pre_register_app_hub_application_resources(
        self,
        request: apphub_integration_messages.RegisterAppHubApplicationResourcesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        apphub_integration_messages.RegisterAppHubApplicationResourcesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for register_app_hub_application_resources

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_register_app_hub_application_resources(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for register_app_hub_application_resources

        DEPRECATED. Please use the `post_register_app_hub_application_resources_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_register_app_hub_application_resources` interceptor runs
        before the `post_register_app_hub_application_resources_with_metadata` interceptor.
        """
        return response

    def post_register_app_hub_application_resources_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for register_app_hub_application_resources

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_register_app_hub_application_resources_with_metadata`
        interceptor in new development instead of the `post_register_app_hub_application_resources` interceptor.
        When both interceptors are used, this `post_register_app_hub_application_resources_with_metadata` interceptor runs after the
        `post_register_app_hub_application_resources` interceptor. The (possibly modified) response returned by
        `post_register_app_hub_application_resources` will be passed to
        `post_register_app_hub_application_resources_with_metadata`.
        """
        return response, metadata

    def pre_snapshot_application_template(
        self,
        request: authoring_messages.SnapshotApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.SnapshotApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for snapshot_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_snapshot_application_template(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for snapshot_application_template

        DEPRECATED. Please use the `post_snapshot_application_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_snapshot_application_template` interceptor runs
        before the `post_snapshot_application_template_with_metadata` interceptor.
        """
        return response

    def post_snapshot_application_template_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for snapshot_application_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_snapshot_application_template_with_metadata`
        interceptor in new development instead of the `post_snapshot_application_template` interceptor.
        When both interceptors are used, this `post_snapshot_application_template_with_metadata` interceptor runs after the
        `post_snapshot_application_template` interceptor. The (possibly modified) response returned by
        `post_snapshot_application_template` will be passed to
        `post_snapshot_application_template_with_metadata`.
        """
        return response, metadata

    def pre_sync_share(
        self,
        request: sharing_messages.SyncShareRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        sharing_messages.SyncShareRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for sync_share

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_sync_share(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for sync_share

        DEPRECATED. Please use the `post_sync_share_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_sync_share` interceptor runs
        before the `post_sync_share_with_metadata` interceptor.
        """
        return response

    def post_sync_share_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for sync_share

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_sync_share_with_metadata`
        interceptor in new development instead of the `post_sync_share` interceptor.
        When both interceptors are used, this `post_sync_share_with_metadata` interceptor runs after the
        `post_sync_share` interceptor. The (possibly modified) response returned by
        `post_sync_share` will be passed to
        `post_sync_share_with_metadata`.
        """
        return response, metadata

    def pre_update_application(
        self,
        request: deployment_messages.UpdateApplicationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_messages.UpdateApplicationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_application

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_application(
        self, response: deployment_resources.Application
    ) -> deployment_resources.Application:
        """Post-rpc interceptor for update_application

        DEPRECATED. Please use the `post_update_application_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_application` interceptor runs
        before the `post_update_application_with_metadata` interceptor.
        """
        return response

    def post_update_application_with_metadata(
        self,
        response: deployment_resources.Application,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        deployment_resources.Application, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_application

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_application_with_metadata`
        interceptor in new development instead of the `post_update_application` interceptor.
        When both interceptors are used, this `post_update_application_with_metadata` interceptor runs after the
        `post_update_application` interceptor. The (possibly modified) response returned by
        `post_update_application` will be passed to
        `post_update_application_with_metadata`.
        """
        return response, metadata

    def pre_update_application_template(
        self,
        request: authoring_messages.UpdateApplicationTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.UpdateApplicationTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_application_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_application_template(
        self, response: authoring.ApplicationTemplate
    ) -> authoring.ApplicationTemplate:
        """Post-rpc interceptor for update_application_template

        DEPRECATED. Please use the `post_update_application_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_application_template` interceptor runs
        before the `post_update_application_template_with_metadata` interceptor.
        """
        return response

    def post_update_application_template_with_metadata(
        self,
        response: authoring.ApplicationTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.ApplicationTemplate, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_application_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_application_template_with_metadata`
        interceptor in new development instead of the `post_update_application_template` interceptor.
        When both interceptors are used, this `post_update_application_template_with_metadata` interceptor runs after the
        `post_update_application_template` interceptor. The (possibly modified) response returned by
        `post_update_application_template` will be passed to
        `post_update_application_template_with_metadata`.
        """
        return response, metadata

    def pre_update_catalog(
        self,
        request: catalog_management_messages.UpdateCatalogRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.UpdateCatalogRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_catalog

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_catalog(
        self, response: catalog_management.Catalog
    ) -> catalog_management.Catalog:
        """Post-rpc interceptor for update_catalog

        DEPRECATED. Please use the `post_update_catalog_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_catalog` interceptor runs
        before the `post_update_catalog_with_metadata` interceptor.
        """
        return response

    def post_update_catalog_with_metadata(
        self,
        response: catalog_management.Catalog,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog_management.Catalog, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_catalog

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_catalog_with_metadata`
        interceptor in new development instead of the `post_update_catalog` interceptor.
        When both interceptors are used, this `post_update_catalog_with_metadata` interceptor runs after the
        `post_update_catalog` interceptor. The (possibly modified) response returned by
        `post_update_catalog` will be passed to
        `post_update_catalog_with_metadata`.
        """
        return response, metadata

    def pre_update_catalog_template(
        self,
        request: catalog_management_messages.UpdateCatalogTemplateRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.UpdateCatalogTemplateRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_catalog_template

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_catalog_template(
        self, response: catalog_management.CatalogTemplate
    ) -> catalog_management.CatalogTemplate:
        """Post-rpc interceptor for update_catalog_template

        DEPRECATED. Please use the `post_update_catalog_template_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_catalog_template` interceptor runs
        before the `post_update_catalog_template_with_metadata` interceptor.
        """
        return response

    def post_update_catalog_template_with_metadata(
        self,
        response: catalog_management.CatalogTemplate,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management.CatalogTemplate, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Post-rpc interceptor for update_catalog_template

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_catalog_template_with_metadata`
        interceptor in new development instead of the `post_update_catalog_template` interceptor.
        When both interceptors are used, this `post_update_catalog_template_with_metadata` interceptor runs after the
        `post_update_catalog_template` interceptor. The (possibly modified) response returned by
        `post_update_catalog_template` will be passed to
        `post_update_catalog_template_with_metadata`.
        """
        return response, metadata

    def pre_update_component(
        self,
        request: authoring_messages.UpdateComponentRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.UpdateComponentRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_component

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_component(
        self, response: authoring.Component
    ) -> authoring.Component:
        """Post-rpc interceptor for update_component

        DEPRECATED. Please use the `post_update_component_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_component` interceptor runs
        before the `post_update_component_with_metadata` interceptor.
        """
        return response

    def post_update_component_with_metadata(
        self,
        response: authoring.Component,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.Component, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_component

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_component_with_metadata`
        interceptor in new development instead of the `post_update_component` interceptor.
        When both interceptors are used, this `post_update_component_with_metadata` interceptor runs after the
        `post_update_component` interceptor. The (possibly modified) response returned by
        `post_update_component` will be passed to
        `post_update_component_with_metadata`.
        """
        return response, metadata

    def pre_update_connection(
        self,
        request: authoring_messages.UpdateConnectionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        authoring_messages.UpdateConnectionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_connection

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_connection(
        self, response: authoring.Connection
    ) -> authoring.Connection:
        """Post-rpc interceptor for update_connection

        DEPRECATED. Please use the `post_update_connection_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_connection` interceptor runs
        before the `post_update_connection_with_metadata` interceptor.
        """
        return response

    def post_update_connection_with_metadata(
        self,
        response: authoring.Connection,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[authoring.Connection, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_connection

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_connection_with_metadata`
        interceptor in new development instead of the `post_update_connection` interceptor.
        When both interceptors are used, this `post_update_connection_with_metadata` interceptor runs after the
        `post_update_connection` interceptor. The (possibly modified) response returned by
        `post_update_connection` will be passed to
        `post_update_connection_with_metadata`.
        """
        return response, metadata

    def pre_update_policy(
        self,
        request: best_practices_messages.UpdatePolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        best_practices_messages.UpdatePolicyRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_policy(
        self, response: best_practices.Policy
    ) -> best_practices.Policy:
        """Post-rpc interceptor for update_policy

        DEPRECATED. Please use the `post_update_policy_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_policy` interceptor runs
        before the `post_update_policy_with_metadata` interceptor.
        """
        return response

    def post_update_policy_with_metadata(
        self,
        response: best_practices.Policy,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[best_practices.Policy, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_policy

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_policy_with_metadata`
        interceptor in new development instead of the `post_update_policy` interceptor.
        When both interceptors are used, this `post_update_policy_with_metadata` interceptor runs after the
        `post_update_policy` interceptor. The (possibly modified) response returned by
        `post_update_policy` will be passed to
        `post_update_policy_with_metadata`.
        """
        return response, metadata

    def pre_update_space(
        self,
        request: catalog_management_messages.UpdateSpaceRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        catalog_management_messages.UpdateSpaceRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_space

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_update_space(
        self, response: catalog_management.Space
    ) -> catalog_management.Space:
        """Post-rpc interceptor for update_space

        DEPRECATED. Please use the `post_update_space_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code. This `post_update_space` interceptor runs
        before the `post_update_space_with_metadata` interceptor.
        """
        return response

    def post_update_space_with_metadata(
        self,
        response: catalog_management.Space,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[catalog_management.Space, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_space

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the DesignCenter server but before it is returned to user code.

        We recommend only using this `post_update_space_with_metadata`
        interceptor in new development instead of the `post_update_space` interceptor.
        When both interceptors are used, this `post_update_space_with_metadata` interceptor runs after the
        `post_update_space` interceptor. The (possibly modified) response returned by
        `post_update_space` will be passed to
        `post_update_space_with_metadata`.
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
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_location(
        self, response: locations_pb2.Location
    ) -> locations_pb2.Location:
        """Post-rpc interceptor for get_location

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
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
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_locations(
        self, response: locations_pb2.ListLocationsResponse
    ) -> locations_pb2.ListLocationsResponse:
        """Post-rpc interceptor for list_locations

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code.
        """
        return response

    def pre_get_iam_policy(
        self,
        request: iam_policy_pb2.GetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.GetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for get_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code.
        """
        return response

    def pre_set_iam_policy(
        self,
        request: iam_policy_pb2.SetIamPolicyRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.SetIamPolicyRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_set_iam_policy(self, response: policy_pb2.Policy) -> policy_pb2.Policy:
        """Post-rpc interceptor for set_iam_policy

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code.
        """
        return response

    def pre_test_iam_permissions(
        self,
        request: iam_policy_pb2.TestIamPermissionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        iam_policy_pb2.TestIamPermissionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_test_iam_permissions(
        self, response: iam_policy_pb2.TestIamPermissionsResponse
    ) -> iam_policy_pb2.TestIamPermissionsResponse:
        """Post-rpc interceptor for test_iam_permissions

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
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
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
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
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_delete_operation(self, response: None) -> None:
        """Post-rpc interceptor for delete_operation

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
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
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
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
        before they are sent to the DesignCenter server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the DesignCenter server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class DesignCenterRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: DesignCenterRestInterceptor
    _client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None


class DesignCenterRestTransport(_BaseDesignCenterRestTransport):
    """REST backend synchronous transport for DesignCenter.

    Service describing handlers for resources

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "designcenter.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[DesignCenterRestInterceptor] = None,
        api_audience: Optional[str] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'designcenter.googleapis.com').
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
            interceptor (Optional[DesignCenterRestInterceptor]): Interceptor used
                to manipulate requests, request metadata, and responses.
            api_audience (Optional[str]): The intended audience for the API calls
                to the service that will be set when using certain 3rd party
                authentication flows. Audience is typically a resource identifier.
                If not set, the host value will be used as a default.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
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
            client_options=client_options,
            **kwargs,
        )
        self._session = AuthorizedSession(
            self._credentials, default_host=self.DEFAULT_HOST
        )
        self._operations_client: Optional[operations_v1.AbstractOperationsClient] = None
        if client_cert_source_for_mtls:
            self._session.configure_mtls_channel(client_cert_source_for_mtls)
        self._interceptor = interceptor or DesignCenterRestInterceptor()
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
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}:cancel",
                        "body": "*",
                    },
                ],
                "google.longrunning.Operations.DeleteOperation": [
                    {
                        "method": "delete",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.GetOperation": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*/operations/*}",
                    },
                ],
                "google.longrunning.Operations.ListOperations": [
                    {
                        "method": "get",
                        "uri": "/v1/{name=projects/*/locations/*}/operations",
                    },
                ],
            }

            rest_transport = operations_v1.OperationsRestTransport(
                host=self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                scopes=self._scopes,
                http_options=http_options,
                path_prefix="v1",
            )

            self._operations_client = operations_v1.AbstractOperationsClient(
                transport=rest_transport
            )

        # Return the client from cache.
        return self._operations_client

    class _CommitApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseCommitApplicationTemplate,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CommitApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.CommitApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplateRevision:
            r"""Call the commit application
            template method over HTTP.

                Args:
                    request (~.authoring_messages.CommitApplicationTemplateRequest):
                        The request object. Request message for
                    CommitApplicationTemplate method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring.ApplicationTemplateRevision:
                        Application template revision
                    resource.

            """

            http_options = _BaseDesignCenterRestTransport._BaseCommitApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_commit_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCommitApplicationTemplate,
                    "_BaseCommitApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CommitApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CommitApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._CommitApplicationTemplate._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplateRevision()
            pb_resp = authoring.ApplicationTemplateRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_commit_application_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_commit_application_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.ApplicationTemplateRevision.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.commit_application_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CommitApplicationTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApplication(
        _BaseDesignCenterRestTransport._BaseCreateApplication, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateApplication")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.CreateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment_resources.Application:
            r"""Call the create application method over HTTP.

            Args:
                request (~.deployment_messages.CreateApplicationRequest):
                    The request object. Message for creating an application.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment_resources.Application:
                    Represents the application resource.
            """

            http_options = _BaseDesignCenterRestTransport._BaseCreateApplication._get_http_options()
            request, metadata = self._interceptor.pre_create_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateApplication,
                    "_BaseCreateApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateApplication",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateApplication._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = deployment_resources.Application()
            pb_resp = deployment_resources.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployment_resources.Application.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_application",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseCreateApplicationTemplate,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.CreateApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplate:
            r"""Call the create application
            template method over HTTP.

                Args:
                    request (~.authoring_messages.CreateApplicationTemplateRequest):
                        The request object. Message for creating an application
                    template.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring.ApplicationTemplate:
                        Application template resource.
            """

            http_options = _BaseDesignCenterRestTransport._BaseCreateApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_create_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateApplicationTemplate,
                    "_BaseCreateApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._CreateApplicationTemplate._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplate()
            pb_resp = authoring.ApplicationTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_application_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_application_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.ApplicationTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_application_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateApplicationTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCatalog(
        _BaseDesignCenterRestTransport._BaseCreateCatalog, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateCatalog")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.CreateCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.Catalog:
            r"""Call the create catalog method over HTTP.

            Args:
                request (~.catalog_management_messages.CreateCatalogRequest):
                    The request object. Message for creating a catalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.Catalog:
                    A catalog is a collection of
                templates.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseCreateCatalog._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_catalog(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateCatalog,
                    "_BaseCreateCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateCatalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateCatalog._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.Catalog()
            pb_resp = catalog_management.Catalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.Catalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_catalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCatalogTemplate(
        _BaseDesignCenterRestTransport._BaseCreateCatalogTemplate, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateCatalogTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.CreateCatalogTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.CatalogTemplate:
            r"""Call the create catalog template method over HTTP.

            Args:
                request (~.catalog_management_messages.CreateCatalogTemplateRequest):
                    The request object. Message for creating a catalog
                template.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.CatalogTemplate:
                    A template inside a catalog.
            """

            http_options = _BaseDesignCenterRestTransport._BaseCreateCatalogTemplate._get_http_options()
            request, metadata = self._interceptor.pre_create_catalog_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateCatalogTemplate,
                    "_BaseCreateCatalogTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateCatalogTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateCatalogTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateCatalogTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.CatalogTemplate()
            pb_resp = catalog_management.CatalogTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_catalog_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_catalog_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.CatalogTemplate.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_catalog_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateCatalogTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateCatalogTemplateRevision(
        _BaseDesignCenterRestTransport._BaseCreateCatalogTemplateRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateCatalogTemplateRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.CreateCatalogTemplateRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create catalog template
            revision method over HTTP.

                Args:
                    request (~.catalog_management_messages.CreateCatalogTemplateRevisionRequest):
                        The request object. Message for creating a template
                    revisions request.
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

            http_options = _BaseDesignCenterRestTransport._BaseCreateCatalogTemplateRevision._get_http_options()
            request, metadata = self._interceptor.pre_create_catalog_template_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateCatalogTemplateRevision,
                    "_BaseCreateCatalogTemplateRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateCatalogTemplateRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateCatalogTemplateRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._CreateCatalogTemplateRevision._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_catalog_template_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_create_catalog_template_revision_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_catalog_template_revision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateCatalogTemplateRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateComponent(
        _BaseDesignCenterRestTransport._BaseCreateComponent, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateComponent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.CreateComponentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.Component:
            r"""Call the create component method over HTTP.

            Args:
                request (~.authoring_messages.CreateComponentRequest):
                    The request object. Message for creating a component.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.Component:
                    Component resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseCreateComponent._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_component(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateComponent,
                    "_BaseCreateComponent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateComponent",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateComponent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateComponent._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.Component()
            pb_resp = authoring.Component.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_component(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_component_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.Component.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_component",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateComponent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConnection(
        _BaseDesignCenterRestTransport._BaseCreateConnection, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.CreateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.Connection:
            r"""Call the create connection method over HTTP.

            Args:
                request (~.authoring_messages.CreateConnectionRequest):
                    The request object. Message for creating a connection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.Connection:
                    Connection resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseCreateConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateConnection,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateConnection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.Connection()
            pb_resp = authoring.Connection.pb(resp)

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
                    response_payload = authoring.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_connection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePolicy(
        _BaseDesignCenterRestTransport._BaseCreatePolicy, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreatePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.CreatePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> best_practices.Policy:
            r"""Call the create policy method over HTTP.

            Args:
                request (~.best_practices_messages.CreatePolicyRequest):
                    The request object. Message for creating a policy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.best_practices.Policy:
                    A Policy is a resource within an
                Application Template that refers to a
                Policy that you author outside of
                Application Design Center and attach to
                an application template.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseCreatePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreatePolicy,
                    "_BaseCreatePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreatePolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreatePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreatePolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = best_practices.Policy()
            pb_resp = best_practices.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = best_practices.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_policy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreatePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateShare(
        _BaseDesignCenterRestTransport._BaseCreateShare, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.CreateShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create share method over HTTP.

            Args:
                request (~.sharing_messages.CreateShareRequest):
                    The request object. Message for creating a share of a
                catalog.
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
                _BaseDesignCenterRestTransport._BaseCreateShare._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_share(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateShare,
                    "_BaseCreateShare__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateShare",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateShare._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_share_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_share",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateSpace(
        _BaseDesignCenterRestTransport._BaseCreateSpace, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CreateSpace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.CreateSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.Space:
            r"""Call the create space method over HTTP.

            Args:
                request (~.catalog_management_messages.CreateSpaceRequest):
                    The request object. Message for creating a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.Space:
                    Space is a top level resource for
                managing teams building applications
                through Application Design Center.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseCreateSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_create_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCreateSpace,
                    "_BaseCreateSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CreateSpace",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CreateSpace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.Space()
            pb_resp = catalog_management.Space.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_create_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.Space.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.create_space",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CreateSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteApplication(
        _BaseDesignCenterRestTransport._BaseDeleteApplication, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteApplication")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.DeleteApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete application method over HTTP.

            Args:
                request (~.deployment_messages.DeleteApplicationRequest):
                    The request object. Message for deleting an application.
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

            http_options = _BaseDesignCenterRestTransport._BaseDeleteApplication._get_http_options()
            request, metadata = self._interceptor.pre_delete_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteApplication,
                    "_BaseDeleteApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteApplication",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteApplication._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_application_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.delete_application",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseDeleteApplicationTemplate,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.DeleteApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete application
            template method over HTTP.

                Args:
                    request (~.authoring_messages.DeleteApplicationTemplateRequest):
                        The request object. Message for deleting an application
                    template.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseDesignCenterRestTransport._BaseDeleteApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_delete_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteApplicationTemplate,
                    "_BaseDeleteApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._DeleteApplicationTemplate._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteApplicationTemplateRevision(
        _BaseDesignCenterRestTransport._BaseDeleteApplicationTemplateRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteApplicationTemplateRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.DeleteApplicationTemplateRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete application
            template revision method over HTTP.

                Args:
                    request (~.authoring_messages.DeleteApplicationTemplateRevisionRequest):
                        The request object. Message for deleting an application
                    template revision.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseDesignCenterRestTransport._BaseDeleteApplicationTemplateRevision._get_http_options()
            request, metadata = (
                self._interceptor.pre_delete_application_template_revision(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteApplicationTemplateRevision,
                    "_BaseDeleteApplicationTemplateRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteApplicationTemplateRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteApplicationTemplateRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteApplicationTemplateRevision._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteCatalog(
        _BaseDesignCenterRestTransport._BaseDeleteCatalog, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteCatalog")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.DeleteCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete catalog method over HTTP.

            Args:
                request (~.catalog_management_messages.DeleteCatalogRequest):
                    The request object. Message for deleting a catalog.
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
                _BaseDesignCenterRestTransport._BaseDeleteCatalog._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_catalog(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteCatalog,
                    "_BaseDeleteCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteCatalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteCatalog._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_catalog_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.delete_catalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCatalogTemplate(
        _BaseDesignCenterRestTransport._BaseDeleteCatalogTemplate, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteCatalogTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.DeleteCatalogTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete catalog template method over HTTP.

            Args:
                request (~.catalog_management_messages.DeleteCatalogTemplateRequest):
                    The request object. Message for deleting a catalog
                template.
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

            http_options = _BaseDesignCenterRestTransport._BaseDeleteCatalogTemplate._get_http_options()
            request, metadata = self._interceptor.pre_delete_catalog_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteCatalogTemplate,
                    "_BaseDeleteCatalogTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteCatalogTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteCatalogTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteCatalogTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_catalog_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_catalog_template_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.delete_catalog_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteCatalogTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteCatalogTemplateRevision(
        _BaseDesignCenterRestTransport._BaseDeleteCatalogTemplateRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteCatalogTemplateRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.DeleteCatalogTemplateRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete catalog template
            revision method over HTTP.

                Args:
                    request (~.catalog_management_messages.DeleteCatalogTemplateRevisionRequest):
                        The request object. Message for deleting a template
                    revision.
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

            http_options = _BaseDesignCenterRestTransport._BaseDeleteCatalogTemplateRevision._get_http_options()
            request, metadata = self._interceptor.pre_delete_catalog_template_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteCatalogTemplateRevision,
                    "_BaseDeleteCatalogTemplateRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteCatalogTemplateRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteCatalogTemplateRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._DeleteCatalogTemplateRevision._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_catalog_template_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_delete_catalog_template_revision_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.delete_catalog_template_revision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteCatalogTemplateRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteComponent(
        _BaseDesignCenterRestTransport._BaseDeleteComponent, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteComponent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.DeleteComponentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete component method over HTTP.

            Args:
                request (~.authoring_messages.DeleteComponentRequest):
                    The request object. Message for deleting a component.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseDeleteComponent._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_component(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteComponent,
                    "_BaseDeleteComponent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteComponent",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteComponent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteComponent._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteConnection(
        _BaseDesignCenterRestTransport._BaseDeleteConnection, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.DeleteConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete connection method over HTTP.

            Args:
                request (~.authoring_messages.DeleteConnectionRequest):
                    The request object. Message for deleting a connection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseDeleteConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteConnection,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteConnection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeletePolicy(
        _BaseDesignCenterRestTransport._BaseDeletePolicy, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeletePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.DeletePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete policy method over HTTP.

            Args:
                request (~.best_practices_messages.DeletePolicyRequest):
                    The request object. Message for deleting a policy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseDeletePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeletePolicy,
                    "_BaseDeletePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeletePolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeletePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeletePolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeleteShare(
        _BaseDesignCenterRestTransport._BaseDeleteShare, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.DeleteShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete share method over HTTP.

            Args:
                request (~.sharing_messages.DeleteShareRequest):
                    The request object. Message for deleting a share of a
                catalog.
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
                _BaseDesignCenterRestTransport._BaseDeleteShare._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_share(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteShare,
                    "_BaseDeleteShare__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteShare",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteShare._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_delete_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_share_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.delete_share",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteSpace(
        _BaseDesignCenterRestTransport._BaseDeleteSpace, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteSpace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.DeleteSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete space method over HTTP.

            Args:
                request (~.catalog_management_messages.DeleteSpaceRequest):
                    The request object. Message for deleting a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseDeleteSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteSpace,
                    "_BaseDeleteSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteSpace",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteSpace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

    class _DeployApplication(
        _BaseDesignCenterRestTransport._BaseDeployApplication, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeployApplication")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.DeployApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deploy application method over HTTP.

            Args:
                request (~.deployment_messages.DeployApplicationRequest):
                    The request object. Message for deploying an application.
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

            http_options = _BaseDesignCenterRestTransport._BaseDeployApplication._get_http_options()
            request, metadata = self._interceptor.pre_deploy_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeployApplication,
                    "_BaseDeployApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeployApplication",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeployApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeployApplication._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_deploy_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_application_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.deploy_application",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeployApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportApplicationIaC(
        _BaseDesignCenterRestTransport._BaseExportApplicationIaC, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ExportApplicationIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.ExportApplicationIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export application ia c method over HTTP.

            Args:
                request (~.deployment_messages.ExportApplicationIaCRequest):
                    The request object. Request message for
                ExportApplicationIaC method.
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

            http_options = _BaseDesignCenterRestTransport._BaseExportApplicationIaC._get_http_options()
            request, metadata = self._interceptor.pre_export_application_ia_c(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseExportApplicationIaC,
                    "_BaseExportApplicationIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ExportApplicationIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ExportApplicationIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ExportApplicationIaC._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_export_application_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_application_ia_c_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.export_application_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ExportApplicationIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportApplicationTemplateIaC(
        _BaseDesignCenterRestTransport._BaseExportApplicationTemplateIaC,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ExportApplicationTemplateIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ExportApplicationTemplateIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export application
            template ia c method over HTTP.

                Args:
                    request (~.authoring_messages.ExportApplicationTemplateIaCRequest):
                        The request object. Request message for
                    ExportApplicationTemplateIaC method.
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

            http_options = _BaseDesignCenterRestTransport._BaseExportApplicationTemplateIaC._get_http_options()
            request, metadata = self._interceptor.pre_export_application_template_ia_c(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseExportApplicationTemplateIaC,
                    "_BaseExportApplicationTemplateIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ExportApplicationTemplateIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ExportApplicationTemplateIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._ExportApplicationTemplateIaC._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_export_application_template_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_export_application_template_ia_c_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.export_application_template_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ExportApplicationTemplateIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportApplicationTemplateRevisionIaC(
        _BaseDesignCenterRestTransport._BaseExportApplicationTemplateRevisionIaC,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "DesignCenterRestTransport.ExportApplicationTemplateRevisionIaC"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ExportApplicationTemplateRevisionIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export application
            template revision ia c method over HTTP.

                Args:
                    request (~.authoring_messages.ExportApplicationTemplateRevisionIaCRequest):
                        The request object. Request message for
                    ExportApplicationTemplateRevisionIaC
                    method.
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

            http_options = _BaseDesignCenterRestTransport._BaseExportApplicationTemplateRevisionIaC._get_http_options()
            request, metadata = (
                self._interceptor.pre_export_application_template_revision_ia_c(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseExportApplicationTemplateRevisionIaC,
                    "_BaseExportApplicationTemplateRevisionIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ExportApplicationTemplateRevisionIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ExportApplicationTemplateRevisionIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ExportApplicationTemplateRevisionIaC._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_export_application_template_revision_ia_c(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_export_application_template_revision_ia_c_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.export_application_template_revision_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ExportApplicationTemplateRevisionIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchApplicationAssessmentReport(
        _BaseDesignCenterRestTransport._BaseFetchApplicationAssessmentReport,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.FetchApplicationAssessmentReport")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.FetchApplicationAssessmentReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> best_practices_messages.FetchApplicationAssessmentReportResponse:
            r"""Call the fetch application
            assessment report method over HTTP.

                Args:
                    request (~.best_practices_messages.FetchApplicationAssessmentReportRequest):
                        The request object. Message for fetching an application
                    assessment report.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.best_practices_messages.FetchApplicationAssessmentReportResponse:
                        Message for response of fetching an
                    application assessment report.

            """

            http_options = _BaseDesignCenterRestTransport._BaseFetchApplicationAssessmentReport._get_http_options()
            request, metadata = (
                self._interceptor.pre_fetch_application_assessment_report(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseFetchApplicationAssessmentReport,
                    "_BaseFetchApplicationAssessmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.FetchApplicationAssessmentReport",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "FetchApplicationAssessmentReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._FetchApplicationAssessmentReport._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = best_practices_messages.FetchApplicationAssessmentReportResponse()
            pb_resp = (
                best_practices_messages.FetchApplicationAssessmentReportResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_fetch_application_assessment_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_fetch_application_assessment_report_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = best_practices_messages.FetchApplicationAssessmentReportResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.fetch_application_assessment_report",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "FetchApplicationAssessmentReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _FetchFrameworks(
        _BaseDesignCenterRestTransport._BaseFetchFrameworks, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.FetchFrameworks")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.FetchFrameworksRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> best_practices_messages.FetchFrameworksResponse:
            r"""Call the fetch frameworks method over HTTP.

            Args:
                request (~.best_practices_messages.FetchFrameworksRequest):
                    The request object. Request for FetchFrameworks rpc
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.best_practices_messages.FetchFrameworksResponse:
                    Response for FetchFrameworks rpc
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseFetchFrameworks._get_http_options()
            )
            request, metadata = self._interceptor.pre_fetch_frameworks(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseFetchFrameworks,
                    "_BaseFetchFrameworks__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.FetchFrameworks",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "FetchFrameworks",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._FetchFrameworks._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = best_practices_messages.FetchFrameworksResponse()
            pb_resp = best_practices_messages.FetchFrameworksResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_fetch_frameworks(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_fetch_frameworks_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        best_practices_messages.FetchFrameworksResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.fetch_frameworks",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "FetchFrameworks",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateApplicationAssessmentReport(
        _BaseDesignCenterRestTransport._BaseGenerateApplicationAssessmentReport,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GenerateApplicationAssessmentReport")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.GenerateApplicationAssessmentReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate application
            assessment report method over HTTP.

                Args:
                    request (~.best_practices_messages.GenerateApplicationAssessmentReportRequest):
                        The request object. Message for generating an application
                    assessment report.
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

            http_options = _BaseDesignCenterRestTransport._BaseGenerateApplicationAssessmentReport._get_http_options()
            request, metadata = (
                self._interceptor.pre_generate_application_assessment_report(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateApplicationAssessmentReport,
                    "_BaseGenerateApplicationAssessmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateApplicationAssessmentReport",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationAssessmentReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GenerateApplicationAssessmentReport._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_generate_application_assessment_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_application_assessment_report_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_application_assessment_report",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationAssessmentReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateApplicationIaC(
        _BaseDesignCenterRestTransport._BaseGenerateApplicationIaC, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GenerateApplicationIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.GenerateApplicationIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment_messages.GenerateApplicationIaCResponse:
            r"""Call the generate application ia c method over HTTP.

            Args:
                request (~.deployment_messages.GenerateApplicationIaCRequest):
                    The request object. Request message for
                GenerateApplicationIaC method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment_messages.GenerateApplicationIaCResponse:
                    Response message for
                GenerateApplicationIaC method.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGenerateApplicationIaC._get_http_options()
            request, metadata = self._interceptor.pre_generate_application_ia_c(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateApplicationIaC,
                    "_BaseGenerateApplicationIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateApplicationIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GenerateApplicationIaC._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = deployment_messages.GenerateApplicationIaCResponse()
            pb_resp = deployment_messages.GenerateApplicationIaCResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_generate_application_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_application_ia_c_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        deployment_messages.GenerateApplicationIaCResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_application_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateApplicationTemplateAssessmentReport(
        _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateAssessmentReport,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "DesignCenterRestTransport.GenerateApplicationTemplateAssessmentReport"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate application
            template assessment report method over HTTP.

                Args:
                    request (~.best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest):
                        The request object. Message for generate assessment
                    report application template.
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

            http_options = _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateAssessmentReport._get_http_options()
            request, metadata = (
                self._interceptor.pre_generate_application_template_assessment_report(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateAssessmentReport,
                    "_BaseGenerateApplicationTemplateAssessmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateApplicationTemplateAssessmentReport",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationTemplateAssessmentReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GenerateApplicationTemplateAssessmentReport._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = (
                self._interceptor.post_generate_application_template_assessment_report(
                    resp
                )
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_application_template_assessment_report_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_application_template_assessment_report",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationTemplateAssessmentReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateApplicationTemplateIaC(
        _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateIaC,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GenerateApplicationTemplateIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GenerateApplicationTemplateIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.GenerateApplicationTemplateIaCResponse:
            r"""Call the generate application
            template ia c method over HTTP.

                Args:
                    request (~.authoring_messages.GenerateApplicationTemplateIaCRequest):
                        The request object. Request message for
                    GenerateApplicationTemplateIaC method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring_messages.GenerateApplicationTemplateIaCResponse:
                        Response message for
                    GenerateApplicationTemplateIaC method.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateIaC._get_http_options()
            request, metadata = (
                self._interceptor.pre_generate_application_template_ia_c(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateIaC,
                    "_BaseGenerateApplicationTemplateIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateApplicationTemplateIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationTemplateIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._GenerateApplicationTemplateIaC._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.GenerateApplicationTemplateIaCResponse()
            pb_resp = authoring_messages.GenerateApplicationTemplateIaCResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_generate_application_template_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_application_template_ia_c_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring_messages.GenerateApplicationTemplateIaCResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_application_template_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationTemplateIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateApplicationTemplateRevisionIaC(
        _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateRevisionIaC,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "DesignCenterRestTransport.GenerateApplicationTemplateRevisionIaC"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GenerateApplicationTemplateRevisionIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.GenerateApplicationTemplateRevisionIaCResponse:
            r"""Call the generate application
            template revision ia c method over HTTP.

                Args:
                    request (~.authoring_messages.GenerateApplicationTemplateRevisionIaCRequest):
                        The request object. Request message for
                    GenerateApplicationTemplateRevisionIaC
                    method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring_messages.GenerateApplicationTemplateRevisionIaCResponse:
                        Response message for
                    GenerateApplicationTemplateRevisionIaC
                    method.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateRevisionIaC._get_http_options()
            request, metadata = (
                self._interceptor.pre_generate_application_template_revision_ia_c(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateApplicationTemplateRevisionIaC,
                    "_BaseGenerateApplicationTemplateRevisionIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateApplicationTemplateRevisionIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationTemplateRevisionIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GenerateApplicationTemplateRevisionIaC._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.GenerateApplicationTemplateRevisionIaCResponse()
            pb_resp = (
                authoring_messages.GenerateApplicationTemplateRevisionIaCResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_generate_application_template_revision_ia_c(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_application_template_revision_ia_c_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring_messages.GenerateApplicationTemplateRevisionIaCResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_application_template_revision_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateApplicationTemplateRevisionIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateAssessmentReport(
        _BaseDesignCenterRestTransport._BaseGenerateAssessmentReport,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GenerateAssessmentReport")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.GenerateAssessmentReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate assessment
            report method over HTTP.

                Args:
                    request (~.best_practices_messages.GenerateAssessmentReportRequest):
                        The request object. Deprecated: Use
                    GenerateTerraformPlanAssessmentReportRequest
                    instead.  Message for the request to
                    generate a best practice report for a
                    given Terraform plan.
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

            http_options = _BaseDesignCenterRestTransport._BaseGenerateAssessmentReport._get_http_options()
            request, metadata = self._interceptor.pre_generate_assessment_report(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateAssessmentReport,
                    "_BaseGenerateAssessmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateAssessmentReport",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateAssessmentReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._GenerateAssessmentReport._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_generate_assessment_report(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_generate_assessment_report_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_assessment_report",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateAssessmentReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GenerateTerraformPlanAssessmentReport(
        _BaseDesignCenterRestTransport._BaseGenerateTerraformPlanAssessmentReport,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "DesignCenterRestTransport.GenerateTerraformPlanAssessmentReport"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.GenerateTerraformPlanAssessmentReportRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the generate terraform plan
            assessment report method over HTTP.

                Args:
                    request (~.best_practices_messages.GenerateTerraformPlanAssessmentReportRequest):
                        The request object. Message for the request to generate a
                    best practice report for a given
                    Terraform plan at the collection level.
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

            http_options = _BaseDesignCenterRestTransport._BaseGenerateTerraformPlanAssessmentReport._get_http_options()
            request, metadata = (
                self._interceptor.pre_generate_terraform_plan_assessment_report(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGenerateTerraformPlanAssessmentReport,
                    "_BaseGenerateTerraformPlanAssessmentReport__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GenerateTerraformPlanAssessmentReport",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateTerraformPlanAssessmentReport",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GenerateTerraformPlanAssessmentReport._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_generate_terraform_plan_assessment_report(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_generate_terraform_plan_assessment_report_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.generate_terraform_plan_assessment_report",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GenerateTerraformPlanAssessmentReport",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplication(
        _BaseDesignCenterRestTransport._BaseGetApplication, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetApplication")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.GetApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment_resources.Application:
            r"""Call the get application method over HTTP.

            Args:
                request (~.deployment_messages.GetApplicationRequest):
                    The request object. Message for getting an application.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment_resources.Application:
                    Represents the application resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetApplication._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_application(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetApplication,
                    "_BaseGetApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetApplication",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetApplication._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = deployment_resources.Application()
            pb_resp = deployment_resources.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployment_resources.Application.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_application",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseGetApplicationTemplate, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GetApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplate:
            r"""Call the get application template method over HTTP.

            Args:
                request (~.authoring_messages.GetApplicationTemplateRequest):
                    The request object. Message for getting an application
                template.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.ApplicationTemplate:
                    Application template resource.
            """

            http_options = _BaseDesignCenterRestTransport._BaseGetApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_get_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetApplicationTemplate,
                    "_BaseGetApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetApplicationTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplate()
            pb_resp = authoring.ApplicationTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_application_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_application_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.ApplicationTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_application_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplicationTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplicationTemplateRevision(
        _BaseDesignCenterRestTransport._BaseGetApplicationTemplateRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetApplicationTemplateRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GetApplicationTemplateRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplateRevision:
            r"""Call the get application template
            revision method over HTTP.

                Args:
                    request (~.authoring_messages.GetApplicationTemplateRevisionRequest):
                        The request object. Message for getting an application
                    template revision.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring.ApplicationTemplateRevision:
                        Application template revision
                    resource.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGetApplicationTemplateRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_application_template_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetApplicationTemplateRevision,
                    "_BaseGetApplicationTemplateRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetApplicationTemplateRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplicationTemplateRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._GetApplicationTemplateRevision._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplateRevision()
            pb_resp = authoring.ApplicationTemplateRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_application_template_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_application_template_revision_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.ApplicationTemplateRevision.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_application_template_revision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplicationTemplateRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetApplicationTemplateSystemRevision(
        _BaseDesignCenterRestTransport._BaseGetApplicationTemplateSystemRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "DesignCenterRestTransport.GetApplicationTemplateSystemRevision"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GetApplicationTemplateSystemRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplateSystemRevision:
            r"""Call the get application template
            system revision method over HTTP.

                Args:
                    request (~.authoring_messages.GetApplicationTemplateSystemRevisionRequest):
                        The request object. Message for getting an
                    ApplicationTemplateSystemRevision.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring.ApplicationTemplateSystemRevision:
                        Application template system revision
                    resource.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGetApplicationTemplateSystemRevision._get_http_options()
            request, metadata = (
                self._interceptor.pre_get_application_template_system_revision(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetApplicationTemplateSystemRevision,
                    "_BaseGetApplicationTemplateSystemRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetApplicationTemplateSystemRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplicationTemplateSystemRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetApplicationTemplateSystemRevision._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplateSystemRevision()
            pb_resp = authoring.ApplicationTemplateSystemRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_application_template_system_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_application_template_system_revision_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        authoring.ApplicationTemplateSystemRevision.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_application_template_system_revision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetApplicationTemplateSystemRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCatalog(
        _BaseDesignCenterRestTransport._BaseGetCatalog, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetCatalog")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.GetCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.Catalog:
            r"""Call the get catalog method over HTTP.

            Args:
                request (~.catalog_management_messages.GetCatalogRequest):
                    The request object. Message for getting a catalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.Catalog:
                    A catalog is a collection of
                templates.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetCatalog._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_catalog(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetCatalog,
                    "_BaseGetCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetCatalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetCatalog._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.Catalog()
            pb_resp = catalog_management.Catalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.Catalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_catalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCatalogTemplate(
        _BaseDesignCenterRestTransport._BaseGetCatalogTemplate, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetCatalogTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.GetCatalogTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.CatalogTemplate:
            r"""Call the get catalog template method over HTTP.

            Args:
                request (~.catalog_management_messages.GetCatalogTemplateRequest):
                    The request object. Message for getting a catalog
                template resource.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.CatalogTemplate:
                    A template inside a catalog.
            """

            http_options = _BaseDesignCenterRestTransport._BaseGetCatalogTemplate._get_http_options()
            request, metadata = self._interceptor.pre_get_catalog_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetCatalogTemplate,
                    "_BaseGetCatalogTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetCatalogTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetCatalogTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetCatalogTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.CatalogTemplate()
            pb_resp = catalog_management.CatalogTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_catalog_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_catalog_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.CatalogTemplate.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_catalog_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetCatalogTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetCatalogTemplateRevision(
        _BaseDesignCenterRestTransport._BaseGetCatalogTemplateRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetCatalogTemplateRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.GetCatalogTemplateRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.CatalogTemplateRevision:
            r"""Call the get catalog template
            revision method over HTTP.

                Args:
                    request (~.catalog_management_messages.GetCatalogTemplateRevisionRequest):
                        The request object. Message for GetTemplateRevision
                    Request
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.catalog_management.CatalogTemplateRevision:
                        Template revisions inside a catalog.
            """

            http_options = _BaseDesignCenterRestTransport._BaseGetCatalogTemplateRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_catalog_template_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetCatalogTemplateRevision,
                    "_BaseGetCatalogTemplateRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetCatalogTemplateRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetCatalogTemplateRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._GetCatalogTemplateRevision._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.CatalogTemplateRevision()
            pb_resp = catalog_management.CatalogTemplateRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_catalog_template_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_get_catalog_template_revision_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        catalog_management.CatalogTemplateRevision.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_catalog_template_revision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetCatalogTemplateRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetComponent(
        _BaseDesignCenterRestTransport._BaseGetComponent, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetComponent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GetComponentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.Component:
            r"""Call the get component method over HTTP.

            Args:
                request (~.authoring_messages.GetComponentRequest):
                    The request object. Message for getting a component.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.Component:
                    Component resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetComponent._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_component(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetComponent,
                    "_BaseGetComponent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetComponent",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetComponent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetComponent._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.Component()
            pb_resp = authoring.Component.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_component(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_component_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.Component.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_component",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetComponent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConnection(
        _BaseDesignCenterRestTransport._BaseGetConnection, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.GetConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.Connection:
            r"""Call the get connection method over HTTP.

            Args:
                request (~.authoring_messages.GetConnectionRequest):
                    The request object. Message for getting a connection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.Connection:
                    Connection resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_connection(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetConnection,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetConnection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.Connection()
            pb_resp = authoring.Connection.pb(resp)

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
                    response_payload = authoring.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_connection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPolicy(
        _BaseDesignCenterRestTransport._BaseGetPolicy, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.GetPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> best_practices.Policy:
            r"""Call the get policy method over HTTP.

            Args:
                request (~.best_practices_messages.GetPolicyRequest):
                    The request object. Message for getting a policy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.best_practices.Policy:
                    A Policy is a resource within an
                Application Template that refers to a
                Policy that you author outside of
                Application Design Center and attach to
                an application template.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetPolicy,
                    "_BaseGetPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetPolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = best_practices.Policy()
            pb_resp = best_practices.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = best_practices.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_policy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetPolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetShare(_BaseDesignCenterRestTransport._BaseGetShare, DesignCenterRestStub):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.GetShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sharing.Share:
            r"""Call the get share method over HTTP.

            Args:
                request (~.sharing_messages.GetShareRequest):
                    The request object. Message for getting a share of a
                catalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sharing.Share:
                    A catalog share between spaces.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetShare._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_share(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetShare,
                    "_BaseGetShare__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetShare",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetShare._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = sharing.Share()
            pb_resp = sharing.Share.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_share_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sharing.Share.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_share",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSharedTemplate(
        _BaseDesignCenterRestTransport._BaseGetSharedTemplate, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetSharedTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.GetSharedTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sharing.SharedTemplate:
            r"""Call the get shared template method over HTTP.

            Args:
                request (~.sharing_messages.GetSharedTemplateRequest):
                    The request object. Message for getting a shared
                template.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sharing.SharedTemplate:
                    A read-only template that is shared
                with a space.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGetSharedTemplate._get_http_options()
            request, metadata = self._interceptor.pre_get_shared_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetSharedTemplate,
                    "_BaseGetSharedTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetSharedTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetSharedTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetSharedTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = sharing.SharedTemplate()
            pb_resp = sharing.SharedTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_shared_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_shared_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sharing.SharedTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_shared_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetSharedTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSharedTemplateRevision(
        _BaseDesignCenterRestTransport._BaseGetSharedTemplateRevision,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetSharedTemplateRevision")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.GetSharedTemplateRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sharing.SharedTemplateRevision:
            r"""Call the get shared template
            revision method over HTTP.

                Args:
                    request (~.sharing_messages.GetSharedTemplateRevisionRequest):
                        The request object. Message for getting a shared template
                    revisions.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.sharing.SharedTemplateRevision:
                        A read-only template revision that is
                    shared with a space.

            """

            http_options = _BaseDesignCenterRestTransport._BaseGetSharedTemplateRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_shared_template_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetSharedTemplateRevision,
                    "_BaseGetSharedTemplateRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetSharedTemplateRevision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetSharedTemplateRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._GetSharedTemplateRevision._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = sharing.SharedTemplateRevision()
            pb_resp = sharing.SharedTemplateRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_shared_template_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_shared_template_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sharing.SharedTemplateRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_shared_template_revision",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetSharedTemplateRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSpace(_BaseDesignCenterRestTransport._BaseGetSpace, DesignCenterRestStub):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetSpace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.GetSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.Space:
            r"""Call the get space method over HTTP.

            Args:
                request (~.catalog_management_messages.GetSpaceRequest):
                    The request object. Results returned from
                projects.locations.spaces.get.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.Space:
                    Space is a top level resource for
                managing teams building applications
                through Application Design Center.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetSpace,
                    "_BaseGetSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetSpace",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetSpace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.Space()
            pb_resp = catalog_management.Space.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_get_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.Space.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.get_space",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportApplicationIaC(
        _BaseDesignCenterRestTransport._BaseImportApplicationIaC, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ImportApplicationIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.ImportApplicationIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment_messages.ImportApplicationIaCResponse:
            r"""Call the import application ia c method over HTTP.

            Args:
                request (~.deployment_messages.ImportApplicationIaCRequest):
                    The request object. Request message for
                ImportApplicationIaC method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment_messages.ImportApplicationIaCResponse:
                    Response message for
                ImportApplicationIaC method.

            """

            http_options = _BaseDesignCenterRestTransport._BaseImportApplicationIaC._get_http_options()
            request, metadata = self._interceptor.pre_import_application_ia_c(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseImportApplicationIaC,
                    "_BaseImportApplicationIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ImportApplicationIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ImportApplicationIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ImportApplicationIaC._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = deployment_messages.ImportApplicationIaCResponse()
            pb_resp = deployment_messages.ImportApplicationIaCResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_import_application_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_application_ia_c_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        deployment_messages.ImportApplicationIaCResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.import_application_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ImportApplicationIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseImportApplicationTemplate,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ImportApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ImportApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplate:
            r"""Call the import application
            template method over HTTP.

                Args:
                    request (~.authoring_messages.ImportApplicationTemplateRequest):
                        The request object. Request message for
                    ImportApplicationTemplate method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring.ApplicationTemplate:
                        Application template resource.
            """

            http_options = _BaseDesignCenterRestTransport._BaseImportApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_import_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseImportApplicationTemplate,
                    "_BaseImportApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ImportApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ImportApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._ImportApplicationTemplate._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplate()
            pb_resp = authoring.ApplicationTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_import_application_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_application_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.ApplicationTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.import_application_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ImportApplicationTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportApplicationTemplateIaC(
        _BaseDesignCenterRestTransport._BaseImportApplicationTemplateIaC,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ImportApplicationTemplateIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ImportApplicationTemplateIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.ImportApplicationTemplateIaCResponse:
            r"""Call the import application
            template ia c method over HTTP.

                Args:
                    request (~.authoring_messages.ImportApplicationTemplateIaCRequest):
                        The request object. Request message for
                    ImportApplicationTemplateIaC method.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring_messages.ImportApplicationTemplateIaCResponse:
                        Response message for
                    ImportApplicationTemplateIaC method.

            """

            http_options = _BaseDesignCenterRestTransport._BaseImportApplicationTemplateIaC._get_http_options()
            request, metadata = self._interceptor.pre_import_application_template_ia_c(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseImportApplicationTemplateIaC,
                    "_BaseImportApplicationTemplateIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ImportApplicationTemplateIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ImportApplicationTemplateIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._ImportApplicationTemplateIaC._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.ImportApplicationTemplateIaCResponse()
            pb_resp = authoring_messages.ImportApplicationTemplateIaCResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_import_application_template_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_import_application_template_ia_c_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        authoring_messages.ImportApplicationTemplateIaCResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.import_application_template_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ImportApplicationTemplateIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestApplicationTemplateIaC(
        _BaseDesignCenterRestTransport._BaseIngestApplicationTemplateIaC,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.IngestApplicationTemplateIaC")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.IngestApplicationTemplateIaCRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the ingest application
            template ia c method over HTTP.

                Args:
                    request (~.authoring_messages.IngestApplicationTemplateIaCRequest):
                        The request object. Request message for
                    IngestApplicationTemplateIaC method.
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

            http_options = _BaseDesignCenterRestTransport._BaseIngestApplicationTemplateIaC._get_http_options()
            request, metadata = self._interceptor.pre_ingest_application_template_ia_c(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseIngestApplicationTemplateIaC,
                    "_BaseIngestApplicationTemplateIaC__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.IngestApplicationTemplateIaC",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "IngestApplicationTemplateIaC",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._IngestApplicationTemplateIaC._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_ingest_application_template_ia_c(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_ingest_application_template_ia_c_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.ingest_application_template_ia_c",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "IngestApplicationTemplateIaC",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplications(
        _BaseDesignCenterRestTransport._BaseListApplications, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListApplications")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.ListApplicationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment_messages.ListApplicationsResponse:
            r"""Call the list applications method over HTTP.

            Args:
                request (~.deployment_messages.ListApplicationsRequest):
                    The request object. Message for requesting a list of
                applications.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment_messages.ListApplicationsResponse:
                    Message for response to listing
                applications.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListApplications._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_applications(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListApplications,
                    "_BaseListApplications__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListApplications",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplications",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListApplications._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = deployment_messages.ListApplicationsResponse()
            pb_resp = deployment_messages.ListApplicationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_applications(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_applications_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        deployment_messages.ListApplicationsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_applications",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplications",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplicationTemplateRevisions(
        _BaseDesignCenterRestTransport._BaseListApplicationTemplateRevisions,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListApplicationTemplateRevisions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ListApplicationTemplateRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.ListApplicationTemplateRevisionsResponse:
            r"""Call the list application template
            revisions method over HTTP.

                Args:
                    request (~.authoring_messages.ListApplicationTemplateRevisionsRequest):
                        The request object. Message for requesting a list of
                    application template revisions.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring_messages.ListApplicationTemplateRevisionsResponse:
                        Message for response to listing
                    application template revisions.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListApplicationTemplateRevisions._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_application_template_revisions(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListApplicationTemplateRevisions,
                    "_BaseListApplicationTemplateRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListApplicationTemplateRevisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplicationTemplateRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListApplicationTemplateRevisions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.ListApplicationTemplateRevisionsResponse()
            pb_resp = authoring_messages.ListApplicationTemplateRevisionsResponse.pb(
                resp
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_application_template_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_application_template_revisions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring_messages.ListApplicationTemplateRevisionsResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_application_template_revisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplicationTemplateRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplicationTemplates(
        _BaseDesignCenterRestTransport._BaseListApplicationTemplates,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListApplicationTemplates")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ListApplicationTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.ListApplicationTemplatesResponse:
            r"""Call the list application
            templates method over HTTP.

                Args:
                    request (~.authoring_messages.ListApplicationTemplatesRequest):
                        The request object. Message for requesting a list of
                    application templates.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring_messages.ListApplicationTemplatesResponse:
                        Message for response to listing
                    application templates.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListApplicationTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_application_templates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListApplicationTemplates,
                    "_BaseListApplicationTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListApplicationTemplates",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplicationTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._ListApplicationTemplates._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.ListApplicationTemplatesResponse()
            pb_resp = authoring_messages.ListApplicationTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_application_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_application_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        authoring_messages.ListApplicationTemplatesResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_application_templates",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplicationTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListApplicationTemplateSystemRevisions(
        _BaseDesignCenterRestTransport._BaseListApplicationTemplateSystemRevisions,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash(
                "DesignCenterRestTransport.ListApplicationTemplateSystemRevisions"
            )

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ListApplicationTemplateSystemRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.ListApplicationTemplateSystemRevisionsResponse:
            r"""Call the list application template
            system revisions method over HTTP.

                Args:
                    request (~.authoring_messages.ListApplicationTemplateSystemRevisionsRequest):
                        The request object. Message for requesting a list of
                    application template system revisions.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring_messages.ListApplicationTemplateSystemRevisionsResponse:
                        Message for response to listing
                    application template system revisions.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListApplicationTemplateSystemRevisions._get_http_options()
            request, metadata = (
                self._interceptor.pre_list_application_template_system_revisions(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListApplicationTemplateSystemRevisions,
                    "_BaseListApplicationTemplateSystemRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListApplicationTemplateSystemRevisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplicationTemplateSystemRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListApplicationTemplateSystemRevisions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.ListApplicationTemplateSystemRevisionsResponse()
            pb_resp = (
                authoring_messages.ListApplicationTemplateSystemRevisionsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_application_template_system_revisions(
                resp
            )
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_application_template_system_revisions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring_messages.ListApplicationTemplateSystemRevisionsResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_application_template_system_revisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListApplicationTemplateSystemRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCatalogs(
        _BaseDesignCenterRestTransport._BaseListCatalogs, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListCatalogs")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.ListCatalogsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management_messages.ListCatalogsResponse:
            r"""Call the list catalogs method over HTTP.

            Args:
                request (~.catalog_management_messages.ListCatalogsRequest):
                    The request object. Message for requesting a list of
                catalogs.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management_messages.ListCatalogsResponse:
                    Results returned from catalogs.list.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListCatalogs._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_catalogs(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListCatalogs,
                    "_BaseListCatalogs__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListCatalogs",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListCatalogs",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListCatalogs._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management_messages.ListCatalogsResponse()
            pb_resp = catalog_management_messages.ListCatalogsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_catalogs(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_catalogs_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        catalog_management_messages.ListCatalogsResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_catalogs",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListCatalogs",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCatalogTemplateRevisions(
        _BaseDesignCenterRestTransport._BaseListCatalogTemplateRevisions,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListCatalogTemplateRevisions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.ListCatalogTemplateRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management_messages.ListCatalogTemplateRevisionsResponse:
            r"""Call the list catalog template
            revisions method over HTTP.

                Args:
                    request (~.catalog_management_messages.ListCatalogTemplateRevisionsRequest):
                        The request object. Message for requesting list of
                    template revisions.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.catalog_management_messages.ListCatalogTemplateRevisionsResponse:
                        Message for response to listing
                    template revisions.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListCatalogTemplateRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_catalog_template_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListCatalogTemplateRevisions,
                    "_BaseListCatalogTemplateRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListCatalogTemplateRevisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListCatalogTemplateRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._ListCatalogTemplateRevisions._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management_messages.ListCatalogTemplateRevisionsResponse()
            pb_resp = (
                catalog_management_messages.ListCatalogTemplateRevisionsResponse.pb(
                    resp
                )
            )

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_catalog_template_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_catalog_template_revisions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management_messages.ListCatalogTemplateRevisionsResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_catalog_template_revisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListCatalogTemplateRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListCatalogTemplates(
        _BaseDesignCenterRestTransport._BaseListCatalogTemplates, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListCatalogTemplates")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.ListCatalogTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management_messages.ListCatalogTemplatesResponse:
            r"""Call the list catalog templates method over HTTP.

            Args:
                request (~.catalog_management_messages.ListCatalogTemplatesRequest):
                    The request object. Message for requesting a list of
                catalog templates.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management_messages.ListCatalogTemplatesResponse:
                    Message for response to listing
                catalog templates.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListCatalogTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_catalog_templates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListCatalogTemplates,
                    "_BaseListCatalogTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListCatalogTemplates",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListCatalogTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListCatalogTemplates._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management_messages.ListCatalogTemplatesResponse()
            pb_resp = catalog_management_messages.ListCatalogTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_catalog_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_catalog_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management_messages.ListCatalogTemplatesResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_catalog_templates",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListCatalogTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListComponents(
        _BaseDesignCenterRestTransport._BaseListComponents, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListComponents")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ListComponentsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.ListComponentsResponse:
            r"""Call the list components method over HTTP.

            Args:
                request (~.authoring_messages.ListComponentsRequest):
                    The request object. Message for requesting a list of
                components.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring_messages.ListComponentsResponse:
                    Message for response to listing
                components.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListComponents._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_components(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListComponents,
                    "_BaseListComponents__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListComponents",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListComponents",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListComponents._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.ListComponentsResponse()
            pb_resp = authoring_messages.ListComponentsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_components(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_components_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        authoring_messages.ListComponentsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_components",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListComponents",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConnections(
        _BaseDesignCenterRestTransport._BaseListConnections, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListConnections")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.ListConnectionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring_messages.ListConnectionsResponse:
            r"""Call the list connections method over HTTP.

            Args:
                request (~.authoring_messages.ListConnectionsRequest):
                    The request object. Message for requesting a list of
                connections.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring_messages.ListConnectionsResponse:
                    Message for response to listing
                connections.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListConnections._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_connections(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListConnections,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListConnections",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListConnections",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListConnections._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring_messages.ListConnectionsResponse()
            pb_resp = authoring_messages.ListConnectionsResponse.pb(resp)

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
                    response_payload = (
                        authoring_messages.ListConnectionsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_connections",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListConnections",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPolicies(
        _BaseDesignCenterRestTransport._BaseListPolicies, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListPolicies")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.ListPoliciesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> best_practices_messages.ListPoliciesResponse:
            r"""Call the list policies method over HTTP.

            Args:
                request (~.best_practices_messages.ListPoliciesRequest):
                    The request object. Message for requesting a list of
                policies.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.best_practices_messages.ListPoliciesResponse:
                    Message for response to listing
                policies.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListPolicies._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_policies(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListPolicies,
                    "_BaseListPolicies__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListPolicies",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListPolicies",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListPolicies._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = best_practices_messages.ListPoliciesResponse()
            pb_resp = best_practices_messages.ListPoliciesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_policies(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_policies_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        best_practices_messages.ListPoliciesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_policies",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListPolicies",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSharedTemplateRevisions(
        _BaseDesignCenterRestTransport._BaseListSharedTemplateRevisions,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListSharedTemplateRevisions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.ListSharedTemplateRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sharing_messages.ListSharedTemplateRevisionsResponse:
            r"""Call the list shared template
            revisions method over HTTP.

                Args:
                    request (~.sharing_messages.ListSharedTemplateRevisionsRequest):
                        The request object. Message for requesting a list of
                    shared template revisions.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.sharing_messages.ListSharedTemplateRevisionsResponse:
                        Message for response to listing
                    shared templates.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListSharedTemplateRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_shared_template_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListSharedTemplateRevisions,
                    "_BaseListSharedTemplateRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListSharedTemplateRevisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListSharedTemplateRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._ListSharedTemplateRevisions._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = sharing_messages.ListSharedTemplateRevisionsResponse()
            pb_resp = sharing_messages.ListSharedTemplateRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_shared_template_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_list_shared_template_revisions_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        sharing_messages.ListSharedTemplateRevisionsResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_shared_template_revisions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListSharedTemplateRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSharedTemplates(
        _BaseDesignCenterRestTransport._BaseListSharedTemplates, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListSharedTemplates")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.ListSharedTemplatesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sharing_messages.ListSharedTemplatesResponse:
            r"""Call the list shared templates method over HTTP.

            Args:
                request (~.sharing_messages.ListSharedTemplatesRequest):
                    The request object. Message for requesting list of shared
                templates.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sharing_messages.ListSharedTemplatesResponse:
                    Message for response to listing
                shared templates.

            """

            http_options = _BaseDesignCenterRestTransport._BaseListSharedTemplates._get_http_options()
            request, metadata = self._interceptor.pre_list_shared_templates(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListSharedTemplates,
                    "_BaseListSharedTemplates__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListSharedTemplates",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListSharedTemplates",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListSharedTemplates._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = sharing_messages.ListSharedTemplatesResponse()
            pb_resp = sharing_messages.ListSharedTemplatesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_shared_templates(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_shared_templates_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        sharing_messages.ListSharedTemplatesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_shared_templates",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListSharedTemplates",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListShares(
        _BaseDesignCenterRestTransport._BaseListShares, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListShares")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.ListSharesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> sharing_messages.ListSharesResponse:
            r"""Call the list shares method over HTTP.

            Args:
                request (~.sharing_messages.ListSharesRequest):
                    The request object. Message for listing shares of a
                catalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.sharing_messages.ListSharesResponse:
                    Message for response to listing
                shares of a catalog.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListShares._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_shares(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListShares,
                    "_BaseListShares__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListShares",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListShares",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListShares._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = sharing_messages.ListSharesResponse()
            pb_resp = sharing_messages.ListSharesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_shares(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_shares_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = sharing_messages.ListSharesResponse.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_shares",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListShares",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListSpaces(
        _BaseDesignCenterRestTransport._BaseListSpaces, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListSpaces")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.ListSpacesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management_messages.ListSpacesResponse:
            r"""Call the list spaces method over HTTP.

            Args:
                request (~.catalog_management_messages.ListSpacesRequest):
                    The request object. Message for requesting a list of
                spaces.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management_messages.ListSpacesResponse:
                    Results returned from
                projects.locations.spaces.list.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseListSpaces._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_spaces(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListSpaces,
                    "_BaseListSpaces__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListSpaces",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListSpaces",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListSpaces._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management_messages.ListSpacesResponse()
            pb_resp = catalog_management_messages.ListSpacesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_list_spaces(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_spaces_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        catalog_management_messages.ListSpacesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.list_spaces",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListSpaces",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _PreviewApplication(
        _BaseDesignCenterRestTransport._BasePreviewApplication, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.PreviewApplication")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.PreviewApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the preview application method over HTTP.

            Args:
                request (~.deployment_messages.PreviewApplicationRequest):
                    The request object. Message for previewing an
                application.
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

            http_options = _BaseDesignCenterRestTransport._BasePreviewApplication._get_http_options()
            request, metadata = self._interceptor.pre_preview_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BasePreviewApplication,
                    "_BasePreviewApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.PreviewApplication",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "PreviewApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._PreviewApplication._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_preview_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_preview_application_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.preview_application",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "PreviewApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RecommendIAMRoles(
        _BaseDesignCenterRestTransport._BaseRecommendIAMRoles, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.RecommendIAMRoles")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.RecommendIAMRolesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the recommend iam roles method over HTTP.

            Args:
                request (~.deployment_messages.RecommendIAMRolesRequest):
                    The request object. Request message for ``RecommendIAMRoles``.
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

            http_options = _BaseDesignCenterRestTransport._BaseRecommendIAMRoles._get_http_options()
            request, metadata = self._interceptor.pre_recommend_iam_roles(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseRecommendIAMRoles,
                    "_BaseRecommendIAMRoles__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.RecommendIAMRoles",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "RecommendIAMRoles",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._RecommendIAMRoles._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_recommend_iam_roles(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_recommend_iam_roles_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.recommend_iam_roles",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "RecommendIAMRoles",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _RegisterAppHubApplicationResources(
        _BaseDesignCenterRestTransport._BaseRegisterAppHubApplicationResources,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.RegisterAppHubApplicationResources")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: apphub_integration_messages.RegisterAppHubApplicationResourcesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the register app hub
            application resources method over HTTP.

                Args:
                    request (~.apphub_integration_messages.RegisterAppHubApplicationResourcesRequest):
                        The request object. Request message for
                    RegisterAppHubApplicationResources
                    method.
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

            http_options = _BaseDesignCenterRestTransport._BaseRegisterAppHubApplicationResources._get_http_options()
            request, metadata = (
                self._interceptor.pre_register_app_hub_application_resources(
                    request, metadata
                )
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseRegisterAppHubApplicationResources,
                    "_BaseRegisterAppHubApplicationResources__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.RegisterAppHubApplicationResources",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "RegisterAppHubApplicationResources",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._RegisterAppHubApplicationResources._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_register_app_hub_application_resources(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_register_app_hub_application_resources_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.register_app_hub_application_resources",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "RegisterAppHubApplicationResources",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SnapshotApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseSnapshotApplicationTemplate,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.SnapshotApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.SnapshotApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the snapshot application
            template method over HTTP.

                Args:
                    request (~.authoring_messages.SnapshotApplicationTemplateRequest):
                        The request object. Message for snapshotting an
                    application template asynchronously.
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

            http_options = _BaseDesignCenterRestTransport._BaseSnapshotApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_snapshot_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseSnapshotApplicationTemplate,
                    "_BaseSnapshotApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.SnapshotApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "SnapshotApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._SnapshotApplicationTemplate._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_snapshot_application_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_snapshot_application_template_with_metadata(
                    resp, response_metadata
                )
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.snapshot_application_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "SnapshotApplicationTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _SyncShare(
        _BaseDesignCenterRestTransport._BaseSyncShare, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.SyncShare")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: sharing_messages.SyncShareRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the sync share method over HTTP.

            Args:
                request (~.sharing_messages.SyncShareRequest):
                    The request object. Message for syncing a share of a
                catalog.
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
                _BaseDesignCenterRestTransport._BaseSyncShare._get_http_options()
            )
            request, metadata = self._interceptor.pre_sync_share(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseSyncShare,
                    "_BaseSyncShare__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.SyncShare",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "SyncShare",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._SyncShare._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_sync_share(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_sync_share_with_metadata(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.sync_share",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "SyncShare",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplication(
        _BaseDesignCenterRestTransport._BaseUpdateApplication, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateApplication")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: deployment_messages.UpdateApplicationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> deployment_resources.Application:
            r"""Call the update application method over HTTP.

            Args:
                request (~.deployment_messages.UpdateApplicationRequest):
                    The request object. Message for updating an application.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.deployment_resources.Application:
                    Represents the application resource.
            """

            http_options = _BaseDesignCenterRestTransport._BaseUpdateApplication._get_http_options()
            request, metadata = self._interceptor.pre_update_application(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateApplication,
                    "_BaseUpdateApplication__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateApplication",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateApplication",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdateApplication._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = deployment_resources.Application()
            pb_resp = deployment_resources.Application.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_application(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_application_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = deployment_resources.Application.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_application",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateApplication",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateApplicationTemplate(
        _BaseDesignCenterRestTransport._BaseUpdateApplicationTemplate,
        DesignCenterRestStub,
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateApplicationTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.UpdateApplicationTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.ApplicationTemplate:
            r"""Call the update application
            template method over HTTP.

                Args:
                    request (~.authoring_messages.UpdateApplicationTemplateRequest):
                        The request object. Message for updating an application
                    template.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.authoring.ApplicationTemplate:
                        Application template resource.
            """

            http_options = _BaseDesignCenterRestTransport._BaseUpdateApplicationTemplate._get_http_options()
            request, metadata = self._interceptor.pre_update_application_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateApplicationTemplate,
                    "_BaseUpdateApplicationTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateApplicationTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateApplicationTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                DesignCenterRestTransport._UpdateApplicationTemplate._get_response(
                    self._host,
                    metadata,
                    query_params,
                    self._session,
                    timeout,
                    transcoded_request,
                    body,
                    client_options=getattr(self, "_client_options", None),
                    url_template=http_options[0].get("uri") if http_options else None,
                )
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.ApplicationTemplate()
            pb_resp = authoring.ApplicationTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_application_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_application_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.ApplicationTemplate.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_application_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateApplicationTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCatalog(
        _BaseDesignCenterRestTransport._BaseUpdateCatalog, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateCatalog")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.UpdateCatalogRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.Catalog:
            r"""Call the update catalog method over HTTP.

            Args:
                request (~.catalog_management_messages.UpdateCatalogRequest):
                    The request object. Message for updating a catalog.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.Catalog:
                    A catalog is a collection of
                templates.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseUpdateCatalog._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_catalog(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateCatalog,
                    "_BaseUpdateCatalog__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateCatalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateCatalog",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdateCatalog._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.Catalog()
            pb_resp = catalog_management.Catalog.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_catalog(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_catalog_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.Catalog.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_catalog",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateCatalog",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateCatalogTemplate(
        _BaseDesignCenterRestTransport._BaseUpdateCatalogTemplate, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateCatalogTemplate")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.UpdateCatalogTemplateRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.CatalogTemplate:
            r"""Call the update catalog template method over HTTP.

            Args:
                request (~.catalog_management_messages.UpdateCatalogTemplateRequest):
                    The request object. Message for updating a catalog
                template.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.CatalogTemplate:
                    A template inside a catalog.
            """

            http_options = _BaseDesignCenterRestTransport._BaseUpdateCatalogTemplate._get_http_options()
            request, metadata = self._interceptor.pre_update_catalog_template(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateCatalogTemplate,
                    "_BaseUpdateCatalogTemplate__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateCatalogTemplate",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateCatalogTemplate",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdateCatalogTemplate._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.CatalogTemplate()
            pb_resp = catalog_management.CatalogTemplate.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_catalog_template(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_catalog_template_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.CatalogTemplate.to_json(
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_catalog_template",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateCatalogTemplate",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateComponent(
        _BaseDesignCenterRestTransport._BaseUpdateComponent, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateComponent")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.UpdateComponentRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.Component:
            r"""Call the update component method over HTTP.

            Args:
                request (~.authoring_messages.UpdateComponentRequest):
                    The request object. Message for updating a component.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.Component:
                    Component resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseUpdateComponent._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_component(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateComponent,
                    "_BaseUpdateComponent__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateComponent",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateComponent",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdateComponent._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.Component()
            pb_resp = authoring.Component.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_component(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_component_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = authoring.Component.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_component",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateComponent",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConnection(
        _BaseDesignCenterRestTransport._BaseUpdateConnection, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateConnection")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: authoring_messages.UpdateConnectionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> authoring.Connection:
            r"""Call the update connection method over HTTP.

            Args:
                request (~.authoring_messages.UpdateConnectionRequest):
                    The request object. Message for updating a connection.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.authoring.Connection:
                    Connection resource.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseUpdateConnection._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_connection(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateConnection,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateConnection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateConnection",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdateConnection._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = authoring.Connection()
            pb_resp = authoring.Connection.pb(resp)

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
                    response_payload = authoring.Connection.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_connection",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateConnection",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePolicy(
        _BaseDesignCenterRestTransport._BaseUpdatePolicy, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdatePolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: best_practices_messages.UpdatePolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> best_practices.Policy:
            r"""Call the update policy method over HTTP.

            Args:
                request (~.best_practices_messages.UpdatePolicyRequest):
                    The request object. Message for updating a policy.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.best_practices.Policy:
                    A Policy is a resource within an
                Application Template that refers to a
                Policy that you author outside of
                Application Design Center and attach to
                an application template.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseUpdatePolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdatePolicy,
                    "_BaseUpdatePolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdatePolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdatePolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdatePolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = best_practices.Policy()
            pb_resp = best_practices.Policy.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_policy(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_policy_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = best_practices.Policy.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_policy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdatePolicy",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSpace(
        _BaseDesignCenterRestTransport._BaseUpdateSpace, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.UpdateSpace")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: catalog_management_messages.UpdateSpaceRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> catalog_management.Space:
            r"""Call the update space method over HTTP.

            Args:
                request (~.catalog_management_messages.UpdateSpaceRequest):
                    The request object. Message for updating a space.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.catalog_management.Space:
                    Space is a top level resource for
                managing teams building applications
                through Application Design Center.

            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseUpdateSpace._get_http_options()
            )
            request, metadata = self._interceptor.pre_update_space(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseUpdateSpace,
                    "_BaseUpdateSpace__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.UpdateSpace",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateSpace",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._UpdateSpace._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            # Return the response
            resp = catalog_management.Space()
            pb_resp = catalog_management.Space.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)
            resp = self._interceptor.post_update_space(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_space_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = catalog_management.Space.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.designcenter_v1.DesignCenterClient.update_space",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "UpdateSpace",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def commit_application_template(
        self,
    ) -> Callable[
        [authoring_messages.CommitApplicationTemplateRequest],
        authoring.ApplicationTemplateRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CommitApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_application(
        self,
    ) -> Callable[
        [deployment_messages.CreateApplicationRequest], deployment_resources.Application
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApplication(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_application_template(
        self,
    ) -> Callable[
        [authoring_messages.CreateApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogRequest], catalog_management.Catalog
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCatalog(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogTemplateRequest],
        catalog_management.CatalogTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCatalogTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateCatalogTemplateRevisionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateCatalogTemplateRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_component(
        self,
    ) -> Callable[[authoring_messages.CreateComponentRequest], authoring.Component]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateComponent(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_connection(
        self,
    ) -> Callable[[authoring_messages.CreateConnectionRequest], authoring.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConnection(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_policy(
        self,
    ) -> Callable[[best_practices_messages.CreatePolicyRequest], best_practices.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePolicy(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_share(
        self,
    ) -> Callable[[sharing_messages.CreateShareRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateShare(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def create_space(
        self,
    ) -> Callable[
        [catalog_management_messages.CreateSpaceRequest], catalog_management.Space
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateSpace(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_application(
        self,
    ) -> Callable[
        [deployment_messages.DeleteApplicationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApplication(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_application_template(
        self,
    ) -> Callable[
        [authoring_messages.DeleteApplicationTemplateRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_application_template_revision(
        self,
    ) -> Callable[
        [authoring_messages.DeleteApplicationTemplateRevisionRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteApplicationTemplateRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCatalog(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogTemplateRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCatalogTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.DeleteCatalogTemplateRevisionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteCatalogTemplateRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_component(
        self,
    ) -> Callable[[authoring_messages.DeleteComponentRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteComponent(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_connection(
        self,
    ) -> Callable[[authoring_messages.DeleteConnectionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConnection(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_policy(
        self,
    ) -> Callable[[best_practices_messages.DeletePolicyRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePolicy(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_share(
        self,
    ) -> Callable[[sharing_messages.DeleteShareRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteShare(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def delete_space(
        self,
    ) -> Callable[[catalog_management_messages.DeleteSpaceRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteSpace(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def deploy_application(
        self,
    ) -> Callable[
        [deployment_messages.DeployApplicationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployApplication(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def export_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.ExportApplicationIaCRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportApplicationIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def export_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ExportApplicationTemplateIaCRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportApplicationTemplateIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def export_application_template_revision_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ExportApplicationTemplateRevisionIaCRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportApplicationTemplateRevisionIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def fetch_application_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.FetchApplicationAssessmentReportRequest],
        best_practices_messages.FetchApplicationAssessmentReportResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchApplicationAssessmentReport(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def fetch_frameworks(
        self,
    ) -> Callable[
        [best_practices_messages.FetchFrameworksRequest],
        best_practices_messages.FetchFrameworksResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._FetchFrameworks(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_application_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateApplicationAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateApplicationAssessmentReport(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.GenerateApplicationIaCRequest],
        deployment_messages.GenerateApplicationIaCResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateApplicationIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_application_template_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateApplicationTemplateAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateApplicationTemplateAssessmentReport(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.GenerateApplicationTemplateIaCRequest],
        authoring_messages.GenerateApplicationTemplateIaCResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateApplicationTemplateIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_application_template_revision_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.GenerateApplicationTemplateRevisionIaCRequest],
        authoring_messages.GenerateApplicationTemplateRevisionIaCResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateApplicationTemplateRevisionIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateAssessmentReport(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def generate_terraform_plan_assessment_report(
        self,
    ) -> Callable[
        [best_practices_messages.GenerateTerraformPlanAssessmentReportRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GenerateTerraformPlanAssessmentReport(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_application(
        self,
    ) -> Callable[
        [deployment_messages.GetApplicationRequest], deployment_resources.Application
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplication(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_application_template(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_application_template_revision(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateRevisionRequest],
        authoring.ApplicationTemplateRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplicationTemplateRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_application_template_system_revision(
        self,
    ) -> Callable[
        [authoring_messages.GetApplicationTemplateSystemRevisionRequest],
        authoring.ApplicationTemplateSystemRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetApplicationTemplateSystemRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogRequest], catalog_management.Catalog
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCatalog(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogTemplateRequest],
        catalog_management.CatalogTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCatalogTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_catalog_template_revision(
        self,
    ) -> Callable[
        [catalog_management_messages.GetCatalogTemplateRevisionRequest],
        catalog_management.CatalogTemplateRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetCatalogTemplateRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_component(
        self,
    ) -> Callable[[authoring_messages.GetComponentRequest], authoring.Component]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetComponent(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_connection(
        self,
    ) -> Callable[[authoring_messages.GetConnectionRequest], authoring.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConnection(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_policy(
        self,
    ) -> Callable[[best_practices_messages.GetPolicyRequest], best_practices.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPolicy(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_share(self) -> Callable[[sharing_messages.GetShareRequest], sharing.Share]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetShare(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_shared_template(
        self,
    ) -> Callable[[sharing_messages.GetSharedTemplateRequest], sharing.SharedTemplate]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSharedTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_shared_template_revision(
        self,
    ) -> Callable[
        [sharing_messages.GetSharedTemplateRevisionRequest],
        sharing.SharedTemplateRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSharedTemplateRevision(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_space(
        self,
    ) -> Callable[
        [catalog_management_messages.GetSpaceRequest], catalog_management.Space
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSpace(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def import_application_ia_c(
        self,
    ) -> Callable[
        [deployment_messages.ImportApplicationIaCRequest],
        deployment_messages.ImportApplicationIaCResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportApplicationIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def import_application_template(
        self,
    ) -> Callable[
        [authoring_messages.ImportApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def import_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.ImportApplicationTemplateIaCRequest],
        authoring_messages.ImportApplicationTemplateIaCResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportApplicationTemplateIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def ingest_application_template_ia_c(
        self,
    ) -> Callable[
        [authoring_messages.IngestApplicationTemplateIaCRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestApplicationTemplateIaC(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_applications(
        self,
    ) -> Callable[
        [deployment_messages.ListApplicationsRequest],
        deployment_messages.ListApplicationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplications(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_application_template_revisions(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplateRevisionsRequest],
        authoring_messages.ListApplicationTemplateRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplicationTemplateRevisions(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_application_templates(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplatesRequest],
        authoring_messages.ListApplicationTemplatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplicationTemplates(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_application_template_system_revisions(
        self,
    ) -> Callable[
        [authoring_messages.ListApplicationTemplateSystemRevisionsRequest],
        authoring_messages.ListApplicationTemplateSystemRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListApplicationTemplateSystemRevisions(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_catalogs(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogsRequest],
        catalog_management_messages.ListCatalogsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCatalogs(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_catalog_template_revisions(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogTemplateRevisionsRequest],
        catalog_management_messages.ListCatalogTemplateRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCatalogTemplateRevisions(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_catalog_templates(
        self,
    ) -> Callable[
        [catalog_management_messages.ListCatalogTemplatesRequest],
        catalog_management_messages.ListCatalogTemplatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListCatalogTemplates(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_components(
        self,
    ) -> Callable[
        [authoring_messages.ListComponentsRequest],
        authoring_messages.ListComponentsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListComponents(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_connections(
        self,
    ) -> Callable[
        [authoring_messages.ListConnectionsRequest],
        authoring_messages.ListConnectionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConnections(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_policies(
        self,
    ) -> Callable[
        [best_practices_messages.ListPoliciesRequest],
        best_practices_messages.ListPoliciesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPolicies(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_shared_template_revisions(
        self,
    ) -> Callable[
        [sharing_messages.ListSharedTemplateRevisionsRequest],
        sharing_messages.ListSharedTemplateRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSharedTemplateRevisions(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_shared_templates(
        self,
    ) -> Callable[
        [sharing_messages.ListSharedTemplatesRequest],
        sharing_messages.ListSharedTemplatesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSharedTemplates(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_shares(
        self,
    ) -> Callable[
        [sharing_messages.ListSharesRequest], sharing_messages.ListSharesResponse
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListShares(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def list_spaces(
        self,
    ) -> Callable[
        [catalog_management_messages.ListSpacesRequest],
        catalog_management_messages.ListSpacesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListSpaces(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def preview_application(
        self,
    ) -> Callable[
        [deployment_messages.PreviewApplicationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._PreviewApplication(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def recommend_iam_roles(
        self,
    ) -> Callable[
        [deployment_messages.RecommendIAMRolesRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RecommendIAMRoles(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def register_app_hub_application_resources(
        self,
    ) -> Callable[
        [apphub_integration_messages.RegisterAppHubApplicationResourcesRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._RegisterAppHubApplicationResources(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def snapshot_application_template(
        self,
    ) -> Callable[
        [authoring_messages.SnapshotApplicationTemplateRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SnapshotApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def sync_share(
        self,
    ) -> Callable[[sharing_messages.SyncShareRequest], operations_pb2.Operation]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._SyncShare(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_application(
        self,
    ) -> Callable[
        [deployment_messages.UpdateApplicationRequest], deployment_resources.Application
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplication(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_application_template(
        self,
    ) -> Callable[
        [authoring_messages.UpdateApplicationTemplateRequest],
        authoring.ApplicationTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateApplicationTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_catalog(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateCatalogRequest], catalog_management.Catalog
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCatalog(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_catalog_template(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateCatalogTemplateRequest],
        catalog_management.CatalogTemplate,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateCatalogTemplate(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_component(
        self,
    ) -> Callable[[authoring_messages.UpdateComponentRequest], authoring.Component]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateComponent(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_connection(
        self,
    ) -> Callable[[authoring_messages.UpdateConnectionRequest], authoring.Connection]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConnection(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_policy(
        self,
    ) -> Callable[[best_practices_messages.UpdatePolicyRequest], best_practices.Policy]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePolicy(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def update_space(
        self,
    ) -> Callable[
        [catalog_management_messages.UpdateSpaceRequest], catalog_management.Space
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSpace(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    @property
    def get_location(self):
        return self._GetLocation(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _GetLocation(
        _BaseDesignCenterRestTransport._BaseGetLocation, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetLocation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
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
                _BaseDesignCenterRestTransport._BaseGetLocation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_location(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetLocation,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetLocation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetLocation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.GetLocation",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetLocation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_locations(self):
        return self._ListLocations(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _ListLocations(
        _BaseDesignCenterRestTransport._BaseListLocations, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListLocations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
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
                _BaseDesignCenterRestTransport._BaseListLocations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_locations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListLocations,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListLocations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListLocations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.ListLocations",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListLocations",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def get_iam_policy(self):
        return self._GetIamPolicy(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _GetIamPolicy(
        _BaseDesignCenterRestTransport._BaseGetIamPolicy, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: iam_policy_pb2.GetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the get iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.GetIamPolicyRequest):
                    The request object for GetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from GetIamPolicy method.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseGetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetIamPolicy,
                    "_BaseGetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_get_iam_policy(resp)
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.GetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def set_iam_policy(self):
        return self._SetIamPolicy(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _SetIamPolicy(
        _BaseDesignCenterRestTransport._BaseSetIamPolicy, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.SetIamPolicy")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: iam_policy_pb2.SetIamPolicyRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> policy_pb2.Policy:
            r"""Call the set iam policy method over HTTP.

            Args:
                request (iam_policy_pb2.SetIamPolicyRequest):
                    The request object for SetIamPolicy method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                policy_pb2.Policy: Response from SetIamPolicy method.
            """

            http_options = (
                _BaseDesignCenterRestTransport._BaseSetIamPolicy._get_http_options()
            )
            request, metadata = self._interceptor.pre_set_iam_policy(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseSetIamPolicy,
                    "_BaseSetIamPolicy__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "SetIamPolicy",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._SetIamPolicy._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = policy_pb2.Policy()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_set_iam_policy(resp)
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.SetIamPolicy",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "SetIamPolicy",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def test_iam_permissions(self):
        return self._TestIamPermissions(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _TestIamPermissions(
        _BaseDesignCenterRestTransport._BaseTestIamPermissions, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.TestIamPermissions")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
                return response

        def __call__(
            self,
            request: iam_policy_pb2.TestIamPermissionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> iam_policy_pb2.TestIamPermissionsResponse:
            r"""Call the test iam permissions method over HTTP.

            Args:
                request (iam_policy_pb2.TestIamPermissionsRequest):
                    The request object for TestIamPermissions method.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                iam_policy_pb2.TestIamPermissionsResponse: Response from TestIamPermissions method.
            """

            http_options = _BaseDesignCenterRestTransport._BaseTestIamPermissions._get_http_options()
            request, metadata = self._interceptor.pre_test_iam_permissions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseTestIamPermissions,
                    "_BaseTestIamPermissions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "TestIamPermissions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._TestIamPermissions._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            content = response.content.decode("utf-8")
            resp = iam_policy_pb2.TestIamPermissionsResponse()
            resp = json_format.Parse(content, resp)
            resp = self._interceptor.post_test_iam_permissions(resp)
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.TestIamPermissions",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "TestIamPermissions",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def cancel_operation(self):
        return self._CancelOperation(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _CancelOperation(
        _BaseDesignCenterRestTransport._BaseCancelOperation, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.CancelOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                    data=body,
                )
                trace_ctx.record_response(response)
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
                _BaseDesignCenterRestTransport._BaseCancelOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._CancelOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                body,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_cancel_operation(None)

    @property
    def delete_operation(self):
        return self._DeleteOperation(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _DeleteOperation(
        _BaseDesignCenterRestTransport._BaseDeleteOperation, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.DeleteOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
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

            http_options = (
                _BaseDesignCenterRestTransport._BaseDeleteOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_delete_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseDeleteOperation,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.DeleteOperation",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "DeleteOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._DeleteOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
            )

            # In case of error, raise the appropriate core_exceptions.GoogleAPICallError exception
            # subclass.
            if response.status_code >= 400:
                raise core_exceptions.from_http_response(response)

            return self._interceptor.post_delete_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _GetOperation(
        _BaseDesignCenterRestTransport._BaseGetOperation, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.GetOperation")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
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
                _BaseDesignCenterRestTransport._BaseGetOperation._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._GetOperation._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "GetOperation",
                        "httpResponse": http_response,
                        "metadata": http_response["headers"],
                    },
                )
            return resp

    @property
    def list_operations(self):
        return self._ListOperations(
            self._session,
            self._host,
            self._interceptor,
            getattr(self, "_client_options", None),
        )  # type: ignore

    class _ListOperations(
        _BaseDesignCenterRestTransport._BaseListOperations, DesignCenterRestStub
    ):
        def __hash__(self):
            return hash("DesignCenterRestTransport.ListOperations")

        @staticmethod
        def _get_response(
            host,
            metadata,
            query_params,
            session,
            timeout,
            transcoded_request,
            body=None,
            client_options=None,
            url_template=None,
        ):
            """Execute the HTTP request over the transport session with
            OpenTelemetry tracing and metadata propagation."""

            uri = transcoded_request["uri"]
            method = transcoded_request["method"]
            headers = dict(metadata)
            headers["Content-Type"] = "application/json"
            url = "{host}{uri}".format(host=host, uri=uri)

            with trace_http_request(
                client_options=client_options,
                method=method,
                url=url,
                url_template=url_template,
                headers=headers,
                body=body,
            ) as trace_ctx:
                response = getattr(session, method)(
                    url,
                    timeout=timeout,
                    headers=headers,
                    params=rest_helpers.flatten_query_params(query_params, strict=True),
                )
                trace_ctx.record_response(response)
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
                _BaseDesignCenterRestTransport._BaseListOperations._get_http_options()
            )
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseDesignCenterRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.designcenter_v1.DesignCenterClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = DesignCenterRestTransport._ListOperations._get_response(
                self._host,
                metadata,
                query_params,
                self._session,
                timeout,
                transcoded_request,
                client_options=getattr(self, "_client_options", None),
                url_template=http_options[0].get("uri") if http_options else None,
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
                    "Received response for google.cloud.designcenter_v1.DesignCenterAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.designcenter.v1.DesignCenter",
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


__all__ = ("DesignCenterRestTransport",)
