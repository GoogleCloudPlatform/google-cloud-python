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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import json_format
from requests import __version__ as requests_version

from google.cloud.contact_center_insights_v1._compat import transcode_request
from google.cloud.contact_center_insights_v1.types import (
    contact_center_insights,
    resources,
)

from .base import DEFAULT_CLIENT_INFO as BASE_DEFAULT_CLIENT_INFO
from .rest_base import _BaseContactCenterInsightsRestTransport

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


class ContactCenterInsightsRestInterceptor:
    """Interceptor for ContactCenterInsights.

    Interceptors are used to manipulate requests, request metadata, and responses
    in arbitrary ways.
    Example use cases include:
    * Logging
    * Verifying requests according to service or custom semantics
    * Stripping extraneous information from responses

    These use cases and more can be enabled by injecting an
    instance of a custom subclass when constructing the ContactCenterInsightsRestTransport.

    .. code-block:: python
        class MyCustomContactCenterInsightsInterceptor(ContactCenterInsightsRestInterceptor):
            def pre_bulk_analyze_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_analyze_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_delete_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_delete_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_download_feedback_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_download_feedback_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_bulk_upload_feedback_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_bulk_upload_feedback_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_calculate_issue_model_stats(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_calculate_issue_model_stats(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_calculate_stats(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_calculate_stats(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_analysis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_analysis_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_analysis_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_feedback_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_feedback_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_phrase_matcher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_phrase_matcher(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_qa_question(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_qa_question(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_qa_scorecard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_qa_scorecard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_qa_scorecard_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_qa_scorecard_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_create_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_create_view(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_analysis_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_feedback_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_delete_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_delete_phrase_matcher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_qa_question(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_qa_scorecard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_qa_scorecard_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_delete_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def pre_deploy_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_deploy_qa_scorecard_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_deploy_qa_scorecard_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_insights_data(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_insights_data(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_export_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_export_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_analysis(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_analysis(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_analysis_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_analysis_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_encryption_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_encryption_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_feedback_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_feedback_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_phrase_matcher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_phrase_matcher(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_qa_question(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_qa_question(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_qa_scorecard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_qa_scorecard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_qa_scorecard_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_qa_scorecard_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_get_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_get_view(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_import_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_import_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_ingest_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_ingest_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_initialize_encryption_spec(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_initialize_encryption_spec(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_all_feedback_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_all_feedback_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_analyses(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_analyses(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_analysis_rules(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_analysis_rules(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_conversations(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_conversations(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_feedback_labels(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_feedback_labels(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_issue_models(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_issue_models(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_issues(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_issues(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_phrase_matchers(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_phrase_matchers(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_qa_questions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_qa_questions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_qa_scorecard_revisions(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_qa_scorecard_revisions(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_qa_scorecards(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_qa_scorecards(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_list_views(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_list_views(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_query_metrics(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_query_metrics(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_tune_qa_scorecard_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_tune_qa_scorecard_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undeploy_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undeploy_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_undeploy_qa_scorecard_revision(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_undeploy_qa_scorecard_revision(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_analysis_rule(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_analysis_rule(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_feedback_label(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_feedback_label(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_issue(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_issue(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_issue_model(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_issue_model(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_phrase_matcher(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_phrase_matcher(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_qa_question(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_qa_question(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_qa_scorecard(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_qa_scorecard(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_settings(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_settings(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_update_view(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_update_view(self, response):
                logging.log(f"Received response: {response}")
                return response

            def pre_upload_conversation(self, request, metadata):
                logging.log(f"Received request: {request}")
                return request, metadata

            def post_upload_conversation(self, response):
                logging.log(f"Received response: {response}")
                return response

        transport = ContactCenterInsightsRestTransport(interceptor=MyCustomContactCenterInsightsInterceptor())
        client = ContactCenterInsightsClient(transport=transport)


    """

    def pre_bulk_analyze_conversations(
        self,
        request: contact_center_insights.BulkAnalyzeConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.BulkAnalyzeConversationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_analyze_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_bulk_analyze_conversations(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for bulk_analyze_conversations

        DEPRECATED. Please use the `post_bulk_analyze_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_bulk_analyze_conversations` interceptor runs
        before the `post_bulk_analyze_conversations_with_metadata` interceptor.
        """
        return response

    def post_bulk_analyze_conversations_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for bulk_analyze_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_bulk_analyze_conversations_with_metadata`
        interceptor in new development instead of the `post_bulk_analyze_conversations` interceptor.
        When both interceptors are used, this `post_bulk_analyze_conversations_with_metadata` interceptor runs after the
        `post_bulk_analyze_conversations` interceptor. The (possibly modified) response returned by
        `post_bulk_analyze_conversations` will be passed to
        `post_bulk_analyze_conversations_with_metadata`.
        """
        return response, metadata

    def pre_bulk_delete_conversations(
        self,
        request: contact_center_insights.BulkDeleteConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.BulkDeleteConversationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_delete_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_bulk_delete_conversations(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for bulk_delete_conversations

        DEPRECATED. Please use the `post_bulk_delete_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_bulk_delete_conversations` interceptor runs
        before the `post_bulk_delete_conversations_with_metadata` interceptor.
        """
        return response

    def post_bulk_delete_conversations_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for bulk_delete_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_bulk_delete_conversations_with_metadata`
        interceptor in new development instead of the `post_bulk_delete_conversations` interceptor.
        When both interceptors are used, this `post_bulk_delete_conversations_with_metadata` interceptor runs after the
        `post_bulk_delete_conversations` interceptor. The (possibly modified) response returned by
        `post_bulk_delete_conversations` will be passed to
        `post_bulk_delete_conversations_with_metadata`.
        """
        return response, metadata

    def pre_bulk_download_feedback_labels(
        self,
        request: contact_center_insights.BulkDownloadFeedbackLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.BulkDownloadFeedbackLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_download_feedback_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_bulk_download_feedback_labels(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for bulk_download_feedback_labels

        DEPRECATED. Please use the `post_bulk_download_feedback_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_bulk_download_feedback_labels` interceptor runs
        before the `post_bulk_download_feedback_labels_with_metadata` interceptor.
        """
        return response

    def post_bulk_download_feedback_labels_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for bulk_download_feedback_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_bulk_download_feedback_labels_with_metadata`
        interceptor in new development instead of the `post_bulk_download_feedback_labels` interceptor.
        When both interceptors are used, this `post_bulk_download_feedback_labels_with_metadata` interceptor runs after the
        `post_bulk_download_feedback_labels` interceptor. The (possibly modified) response returned by
        `post_bulk_download_feedback_labels` will be passed to
        `post_bulk_download_feedback_labels_with_metadata`.
        """
        return response, metadata

    def pre_bulk_upload_feedback_labels(
        self,
        request: contact_center_insights.BulkUploadFeedbackLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.BulkUploadFeedbackLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for bulk_upload_feedback_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_bulk_upload_feedback_labels(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for bulk_upload_feedback_labels

        DEPRECATED. Please use the `post_bulk_upload_feedback_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_bulk_upload_feedback_labels` interceptor runs
        before the `post_bulk_upload_feedback_labels_with_metadata` interceptor.
        """
        return response

    def post_bulk_upload_feedback_labels_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for bulk_upload_feedback_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_bulk_upload_feedback_labels_with_metadata`
        interceptor in new development instead of the `post_bulk_upload_feedback_labels` interceptor.
        When both interceptors are used, this `post_bulk_upload_feedback_labels_with_metadata` interceptor runs after the
        `post_bulk_upload_feedback_labels` interceptor. The (possibly modified) response returned by
        `post_bulk_upload_feedback_labels` will be passed to
        `post_bulk_upload_feedback_labels_with_metadata`.
        """
        return response, metadata

    def pre_calculate_issue_model_stats(
        self,
        request: contact_center_insights.CalculateIssueModelStatsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CalculateIssueModelStatsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for calculate_issue_model_stats

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_calculate_issue_model_stats(
        self, response: contact_center_insights.CalculateIssueModelStatsResponse
    ) -> contact_center_insights.CalculateIssueModelStatsResponse:
        """Post-rpc interceptor for calculate_issue_model_stats

        DEPRECATED. Please use the `post_calculate_issue_model_stats_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_calculate_issue_model_stats` interceptor runs
        before the `post_calculate_issue_model_stats_with_metadata` interceptor.
        """
        return response

    def post_calculate_issue_model_stats_with_metadata(
        self,
        response: contact_center_insights.CalculateIssueModelStatsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CalculateIssueModelStatsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for calculate_issue_model_stats

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_calculate_issue_model_stats_with_metadata`
        interceptor in new development instead of the `post_calculate_issue_model_stats` interceptor.
        When both interceptors are used, this `post_calculate_issue_model_stats_with_metadata` interceptor runs after the
        `post_calculate_issue_model_stats` interceptor. The (possibly modified) response returned by
        `post_calculate_issue_model_stats` will be passed to
        `post_calculate_issue_model_stats_with_metadata`.
        """
        return response, metadata

    def pre_calculate_stats(
        self,
        request: contact_center_insights.CalculateStatsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CalculateStatsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for calculate_stats

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_calculate_stats(
        self, response: contact_center_insights.CalculateStatsResponse
    ) -> contact_center_insights.CalculateStatsResponse:
        """Post-rpc interceptor for calculate_stats

        DEPRECATED. Please use the `post_calculate_stats_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_calculate_stats` interceptor runs
        before the `post_calculate_stats_with_metadata` interceptor.
        """
        return response

    def post_calculate_stats_with_metadata(
        self,
        response: contact_center_insights.CalculateStatsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CalculateStatsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for calculate_stats

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_calculate_stats_with_metadata`
        interceptor in new development instead of the `post_calculate_stats` interceptor.
        When both interceptors are used, this `post_calculate_stats_with_metadata` interceptor runs after the
        `post_calculate_stats` interceptor. The (possibly modified) response returned by
        `post_calculate_stats` will be passed to
        `post_calculate_stats_with_metadata`.
        """
        return response, metadata

    def pre_create_analysis(
        self,
        request: contact_center_insights.CreateAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateAnalysisRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_analysis(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_analysis

        DEPRECATED. Please use the `post_create_analysis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_analysis` interceptor runs
        before the `post_create_analysis_with_metadata` interceptor.
        """
        return response

    def post_create_analysis_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_analysis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_analysis_with_metadata`
        interceptor in new development instead of the `post_create_analysis` interceptor.
        When both interceptors are used, this `post_create_analysis_with_metadata` interceptor runs after the
        `post_create_analysis` interceptor. The (possibly modified) response returned by
        `post_create_analysis` will be passed to
        `post_create_analysis_with_metadata`.
        """
        return response, metadata

    def pre_create_analysis_rule(
        self,
        request: contact_center_insights.CreateAnalysisRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateAnalysisRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_analysis_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_analysis_rule(
        self, response: resources.AnalysisRule
    ) -> resources.AnalysisRule:
        """Post-rpc interceptor for create_analysis_rule

        DEPRECATED. Please use the `post_create_analysis_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_analysis_rule` interceptor runs
        before the `post_create_analysis_rule_with_metadata` interceptor.
        """
        return response

    def post_create_analysis_rule_with_metadata(
        self,
        response: resources.AnalysisRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AnalysisRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_analysis_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_analysis_rule_with_metadata`
        interceptor in new development instead of the `post_create_analysis_rule` interceptor.
        When both interceptors are used, this `post_create_analysis_rule_with_metadata` interceptor runs after the
        `post_create_analysis_rule` interceptor. The (possibly modified) response returned by
        `post_create_analysis_rule` will be passed to
        `post_create_analysis_rule_with_metadata`.
        """
        return response, metadata

    def pre_create_conversation(
        self,
        request: contact_center_insights.CreateConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_conversation(
        self, response: resources.Conversation
    ) -> resources.Conversation:
        """Post-rpc interceptor for create_conversation

        DEPRECATED. Please use the `post_create_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_conversation` interceptor runs
        before the `post_create_conversation_with_metadata` interceptor.
        """
        return response

    def post_create_conversation_with_metadata(
        self,
        response: resources.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_conversation_with_metadata`
        interceptor in new development instead of the `post_create_conversation` interceptor.
        When both interceptors are used, this `post_create_conversation_with_metadata` interceptor runs after the
        `post_create_conversation` interceptor. The (possibly modified) response returned by
        `post_create_conversation` will be passed to
        `post_create_conversation_with_metadata`.
        """
        return response, metadata

    def pre_create_feedback_label(
        self,
        request: contact_center_insights.CreateFeedbackLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateFeedbackLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_feedback_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_feedback_label(
        self, response: resources.FeedbackLabel
    ) -> resources.FeedbackLabel:
        """Post-rpc interceptor for create_feedback_label

        DEPRECATED. Please use the `post_create_feedback_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_feedback_label` interceptor runs
        before the `post_create_feedback_label_with_metadata` interceptor.
        """
        return response

    def post_create_feedback_label_with_metadata(
        self,
        response: resources.FeedbackLabel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.FeedbackLabel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_feedback_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_feedback_label_with_metadata`
        interceptor in new development instead of the `post_create_feedback_label` interceptor.
        When both interceptors are used, this `post_create_feedback_label_with_metadata` interceptor runs after the
        `post_create_feedback_label` interceptor. The (possibly modified) response returned by
        `post_create_feedback_label` will be passed to
        `post_create_feedback_label_with_metadata`.
        """
        return response, metadata

    def pre_create_issue_model(
        self,
        request: contact_center_insights.CreateIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_issue_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for create_issue_model

        DEPRECATED. Please use the `post_create_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_issue_model` interceptor runs
        before the `post_create_issue_model_with_metadata` interceptor.
        """
        return response

    def post_create_issue_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_issue_model_with_metadata`
        interceptor in new development instead of the `post_create_issue_model` interceptor.
        When both interceptors are used, this `post_create_issue_model_with_metadata` interceptor runs after the
        `post_create_issue_model` interceptor. The (possibly modified) response returned by
        `post_create_issue_model` will be passed to
        `post_create_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_create_phrase_matcher(
        self,
        request: contact_center_insights.CreatePhraseMatcherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreatePhraseMatcherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_phrase_matcher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_phrase_matcher(
        self, response: resources.PhraseMatcher
    ) -> resources.PhraseMatcher:
        """Post-rpc interceptor for create_phrase_matcher

        DEPRECATED. Please use the `post_create_phrase_matcher_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_phrase_matcher` interceptor runs
        before the `post_create_phrase_matcher_with_metadata` interceptor.
        """
        return response

    def post_create_phrase_matcher_with_metadata(
        self,
        response: resources.PhraseMatcher,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.PhraseMatcher, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_phrase_matcher

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_phrase_matcher_with_metadata`
        interceptor in new development instead of the `post_create_phrase_matcher` interceptor.
        When both interceptors are used, this `post_create_phrase_matcher_with_metadata` interceptor runs after the
        `post_create_phrase_matcher` interceptor. The (possibly modified) response returned by
        `post_create_phrase_matcher` will be passed to
        `post_create_phrase_matcher_with_metadata`.
        """
        return response, metadata

    def pre_create_qa_question(
        self,
        request: contact_center_insights.CreateQaQuestionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateQaQuestionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_qa_question

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_qa_question(
        self, response: resources.QaQuestion
    ) -> resources.QaQuestion:
        """Post-rpc interceptor for create_qa_question

        DEPRECATED. Please use the `post_create_qa_question_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_qa_question` interceptor runs
        before the `post_create_qa_question_with_metadata` interceptor.
        """
        return response

    def post_create_qa_question_with_metadata(
        self,
        response: resources.QaQuestion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaQuestion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_qa_question

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_qa_question_with_metadata`
        interceptor in new development instead of the `post_create_qa_question` interceptor.
        When both interceptors are used, this `post_create_qa_question_with_metadata` interceptor runs after the
        `post_create_qa_question` interceptor. The (possibly modified) response returned by
        `post_create_qa_question` will be passed to
        `post_create_qa_question_with_metadata`.
        """
        return response, metadata

    def pre_create_qa_scorecard(
        self,
        request: contact_center_insights.CreateQaScorecardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateQaScorecardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_qa_scorecard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_qa_scorecard(
        self, response: resources.QaScorecard
    ) -> resources.QaScorecard:
        """Post-rpc interceptor for create_qa_scorecard

        DEPRECATED. Please use the `post_create_qa_scorecard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_qa_scorecard` interceptor runs
        before the `post_create_qa_scorecard_with_metadata` interceptor.
        """
        return response

    def post_create_qa_scorecard_with_metadata(
        self,
        response: resources.QaScorecard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecard, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_qa_scorecard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_qa_scorecard_with_metadata`
        interceptor in new development instead of the `post_create_qa_scorecard` interceptor.
        When both interceptors are used, this `post_create_qa_scorecard_with_metadata` interceptor runs after the
        `post_create_qa_scorecard` interceptor. The (possibly modified) response returned by
        `post_create_qa_scorecard` will be passed to
        `post_create_qa_scorecard_with_metadata`.
        """
        return response, metadata

    def pre_create_qa_scorecard_revision(
        self,
        request: contact_center_insights.CreateQaScorecardRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateQaScorecardRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_qa_scorecard_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_qa_scorecard_revision(
        self, response: resources.QaScorecardRevision
    ) -> resources.QaScorecardRevision:
        """Post-rpc interceptor for create_qa_scorecard_revision

        DEPRECATED. Please use the `post_create_qa_scorecard_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_qa_scorecard_revision` interceptor runs
        before the `post_create_qa_scorecard_revision_with_metadata` interceptor.
        """
        return response

    def post_create_qa_scorecard_revision_with_metadata(
        self,
        response: resources.QaScorecardRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecardRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_qa_scorecard_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_qa_scorecard_revision_with_metadata`
        interceptor in new development instead of the `post_create_qa_scorecard_revision` interceptor.
        When both interceptors are used, this `post_create_qa_scorecard_revision_with_metadata` interceptor runs after the
        `post_create_qa_scorecard_revision` interceptor. The (possibly modified) response returned by
        `post_create_qa_scorecard_revision` will be passed to
        `post_create_qa_scorecard_revision_with_metadata`.
        """
        return response, metadata

    def pre_create_view(
        self,
        request: contact_center_insights.CreateViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.CreateViewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for create_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_create_view(self, response: resources.View) -> resources.View:
        """Post-rpc interceptor for create_view

        DEPRECATED. Please use the `post_create_view_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_create_view` interceptor runs
        before the `post_create_view_with_metadata` interceptor.
        """
        return response

    def post_create_view_with_metadata(
        self,
        response: resources.View,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.View, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for create_view

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_create_view_with_metadata`
        interceptor in new development instead of the `post_create_view` interceptor.
        When both interceptors are used, this `post_create_view_with_metadata` interceptor runs after the
        `post_create_view` interceptor. The (possibly modified) response returned by
        `post_create_view` will be passed to
        `post_create_view_with_metadata`.
        """
        return response, metadata

    def pre_delete_analysis(
        self,
        request: contact_center_insights.DeleteAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteAnalysisRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_analysis_rule(
        self,
        request: contact_center_insights.DeleteAnalysisRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteAnalysisRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_analysis_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_conversation(
        self,
        request: contact_center_insights.DeleteConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_feedback_label(
        self,
        request: contact_center_insights.DeleteFeedbackLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteFeedbackLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_feedback_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_issue(
        self,
        request: contact_center_insights.DeleteIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteIssueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_issue_model(
        self,
        request: contact_center_insights.DeleteIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_delete_issue_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for delete_issue_model

        DEPRECATED. Please use the `post_delete_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_delete_issue_model` interceptor runs
        before the `post_delete_issue_model_with_metadata` interceptor.
        """
        return response

    def post_delete_issue_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for delete_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_delete_issue_model_with_metadata`
        interceptor in new development instead of the `post_delete_issue_model` interceptor.
        When both interceptors are used, this `post_delete_issue_model_with_metadata` interceptor runs after the
        `post_delete_issue_model` interceptor. The (possibly modified) response returned by
        `post_delete_issue_model` will be passed to
        `post_delete_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_delete_phrase_matcher(
        self,
        request: contact_center_insights.DeletePhraseMatcherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeletePhraseMatcherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_phrase_matcher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_qa_question(
        self,
        request: contact_center_insights.DeleteQaQuestionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteQaQuestionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_qa_question

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_qa_scorecard(
        self,
        request: contact_center_insights.DeleteQaScorecardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteQaScorecardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_qa_scorecard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_qa_scorecard_revision(
        self,
        request: contact_center_insights.DeleteQaScorecardRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteQaScorecardRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_qa_scorecard_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_delete_view(
        self,
        request: contact_center_insights.DeleteViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeleteViewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for delete_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def pre_deploy_issue_model(
        self,
        request: contact_center_insights.DeployIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeployIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deploy_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_deploy_issue_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for deploy_issue_model

        DEPRECATED. Please use the `post_deploy_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_deploy_issue_model` interceptor runs
        before the `post_deploy_issue_model_with_metadata` interceptor.
        """
        return response

    def post_deploy_issue_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_deploy_issue_model_with_metadata`
        interceptor in new development instead of the `post_deploy_issue_model` interceptor.
        When both interceptors are used, this `post_deploy_issue_model_with_metadata` interceptor runs after the
        `post_deploy_issue_model` interceptor. The (possibly modified) response returned by
        `post_deploy_issue_model` will be passed to
        `post_deploy_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_deploy_qa_scorecard_revision(
        self,
        request: contact_center_insights.DeployQaScorecardRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.DeployQaScorecardRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for deploy_qa_scorecard_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_deploy_qa_scorecard_revision(
        self, response: resources.QaScorecardRevision
    ) -> resources.QaScorecardRevision:
        """Post-rpc interceptor for deploy_qa_scorecard_revision

        DEPRECATED. Please use the `post_deploy_qa_scorecard_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_deploy_qa_scorecard_revision` interceptor runs
        before the `post_deploy_qa_scorecard_revision_with_metadata` interceptor.
        """
        return response

    def post_deploy_qa_scorecard_revision_with_metadata(
        self,
        response: resources.QaScorecardRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecardRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for deploy_qa_scorecard_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_deploy_qa_scorecard_revision_with_metadata`
        interceptor in new development instead of the `post_deploy_qa_scorecard_revision` interceptor.
        When both interceptors are used, this `post_deploy_qa_scorecard_revision_with_metadata` interceptor runs after the
        `post_deploy_qa_scorecard_revision` interceptor. The (possibly modified) response returned by
        `post_deploy_qa_scorecard_revision` will be passed to
        `post_deploy_qa_scorecard_revision_with_metadata`.
        """
        return response, metadata

    def pre_export_insights_data(
        self,
        request: contact_center_insights.ExportInsightsDataRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ExportInsightsDataRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_insights_data

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_export_insights_data(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_insights_data

        DEPRECATED. Please use the `post_export_insights_data_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_export_insights_data` interceptor runs
        before the `post_export_insights_data_with_metadata` interceptor.
        """
        return response

    def post_export_insights_data_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_insights_data

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_export_insights_data_with_metadata`
        interceptor in new development instead of the `post_export_insights_data` interceptor.
        When both interceptors are used, this `post_export_insights_data_with_metadata` interceptor runs after the
        `post_export_insights_data` interceptor. The (possibly modified) response returned by
        `post_export_insights_data` will be passed to
        `post_export_insights_data_with_metadata`.
        """
        return response, metadata

    def pre_export_issue_model(
        self,
        request: contact_center_insights.ExportIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ExportIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for export_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_export_issue_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for export_issue_model

        DEPRECATED. Please use the `post_export_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_export_issue_model` interceptor runs
        before the `post_export_issue_model_with_metadata` interceptor.
        """
        return response

    def post_export_issue_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for export_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_export_issue_model_with_metadata`
        interceptor in new development instead of the `post_export_issue_model` interceptor.
        When both interceptors are used, this `post_export_issue_model_with_metadata` interceptor runs after the
        `post_export_issue_model` interceptor. The (possibly modified) response returned by
        `post_export_issue_model` will be passed to
        `post_export_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_get_analysis(
        self,
        request: contact_center_insights.GetAnalysisRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetAnalysisRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_analysis

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_analysis(self, response: resources.Analysis) -> resources.Analysis:
        """Post-rpc interceptor for get_analysis

        DEPRECATED. Please use the `post_get_analysis_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_analysis` interceptor runs
        before the `post_get_analysis_with_metadata` interceptor.
        """
        return response

    def post_get_analysis_with_metadata(
        self,
        response: resources.Analysis,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Analysis, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_analysis

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_analysis_with_metadata`
        interceptor in new development instead of the `post_get_analysis` interceptor.
        When both interceptors are used, this `post_get_analysis_with_metadata` interceptor runs after the
        `post_get_analysis` interceptor. The (possibly modified) response returned by
        `post_get_analysis` will be passed to
        `post_get_analysis_with_metadata`.
        """
        return response, metadata

    def pre_get_analysis_rule(
        self,
        request: contact_center_insights.GetAnalysisRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetAnalysisRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_analysis_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_analysis_rule(
        self, response: resources.AnalysisRule
    ) -> resources.AnalysisRule:
        """Post-rpc interceptor for get_analysis_rule

        DEPRECATED. Please use the `post_get_analysis_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_analysis_rule` interceptor runs
        before the `post_get_analysis_rule_with_metadata` interceptor.
        """
        return response

    def post_get_analysis_rule_with_metadata(
        self,
        response: resources.AnalysisRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AnalysisRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_analysis_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_analysis_rule_with_metadata`
        interceptor in new development instead of the `post_get_analysis_rule` interceptor.
        When both interceptors are used, this `post_get_analysis_rule_with_metadata` interceptor runs after the
        `post_get_analysis_rule` interceptor. The (possibly modified) response returned by
        `post_get_analysis_rule` will be passed to
        `post_get_analysis_rule_with_metadata`.
        """
        return response, metadata

    def pre_get_conversation(
        self,
        request: contact_center_insights.GetConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_conversation(
        self, response: resources.Conversation
    ) -> resources.Conversation:
        """Post-rpc interceptor for get_conversation

        DEPRECATED. Please use the `post_get_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_conversation` interceptor runs
        before the `post_get_conversation_with_metadata` interceptor.
        """
        return response

    def post_get_conversation_with_metadata(
        self,
        response: resources.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_conversation_with_metadata`
        interceptor in new development instead of the `post_get_conversation` interceptor.
        When both interceptors are used, this `post_get_conversation_with_metadata` interceptor runs after the
        `post_get_conversation` interceptor. The (possibly modified) response returned by
        `post_get_conversation` will be passed to
        `post_get_conversation_with_metadata`.
        """
        return response, metadata

    def pre_get_encryption_spec(
        self,
        request: contact_center_insights.GetEncryptionSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetEncryptionSpecRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_encryption_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_encryption_spec(
        self, response: resources.EncryptionSpec
    ) -> resources.EncryptionSpec:
        """Post-rpc interceptor for get_encryption_spec

        DEPRECATED. Please use the `post_get_encryption_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_encryption_spec` interceptor runs
        before the `post_get_encryption_spec_with_metadata` interceptor.
        """
        return response

    def post_get_encryption_spec_with_metadata(
        self,
        response: resources.EncryptionSpec,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.EncryptionSpec, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_encryption_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_encryption_spec_with_metadata`
        interceptor in new development instead of the `post_get_encryption_spec` interceptor.
        When both interceptors are used, this `post_get_encryption_spec_with_metadata` interceptor runs after the
        `post_get_encryption_spec` interceptor. The (possibly modified) response returned by
        `post_get_encryption_spec` will be passed to
        `post_get_encryption_spec_with_metadata`.
        """
        return response, metadata

    def pre_get_feedback_label(
        self,
        request: contact_center_insights.GetFeedbackLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetFeedbackLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_feedback_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_feedback_label(
        self, response: resources.FeedbackLabel
    ) -> resources.FeedbackLabel:
        """Post-rpc interceptor for get_feedback_label

        DEPRECATED. Please use the `post_get_feedback_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_feedback_label` interceptor runs
        before the `post_get_feedback_label_with_metadata` interceptor.
        """
        return response

    def post_get_feedback_label_with_metadata(
        self,
        response: resources.FeedbackLabel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.FeedbackLabel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_feedback_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_feedback_label_with_metadata`
        interceptor in new development instead of the `post_get_feedback_label` interceptor.
        When both interceptors are used, this `post_get_feedback_label_with_metadata` interceptor runs after the
        `post_get_feedback_label` interceptor. The (possibly modified) response returned by
        `post_get_feedback_label` will be passed to
        `post_get_feedback_label_with_metadata`.
        """
        return response, metadata

    def pre_get_issue(
        self,
        request: contact_center_insights.GetIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetIssueRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_issue(self, response: resources.Issue) -> resources.Issue:
        """Post-rpc interceptor for get_issue

        DEPRECATED. Please use the `post_get_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_issue` interceptor runs
        before the `post_get_issue_with_metadata` interceptor.
        """
        return response

    def post_get_issue_with_metadata(
        self,
        response: resources.Issue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Issue, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_issue_with_metadata`
        interceptor in new development instead of the `post_get_issue` interceptor.
        When both interceptors are used, this `post_get_issue_with_metadata` interceptor runs after the
        `post_get_issue` interceptor. The (possibly modified) response returned by
        `post_get_issue` will be passed to
        `post_get_issue_with_metadata`.
        """
        return response, metadata

    def pre_get_issue_model(
        self,
        request: contact_center_insights.GetIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_issue_model(
        self, response: resources.IssueModel
    ) -> resources.IssueModel:
        """Post-rpc interceptor for get_issue_model

        DEPRECATED. Please use the `post_get_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_issue_model` interceptor runs
        before the `post_get_issue_model_with_metadata` interceptor.
        """
        return response

    def post_get_issue_model_with_metadata(
        self,
        response: resources.IssueModel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.IssueModel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_issue_model_with_metadata`
        interceptor in new development instead of the `post_get_issue_model` interceptor.
        When both interceptors are used, this `post_get_issue_model_with_metadata` interceptor runs after the
        `post_get_issue_model` interceptor. The (possibly modified) response returned by
        `post_get_issue_model` will be passed to
        `post_get_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_get_phrase_matcher(
        self,
        request: contact_center_insights.GetPhraseMatcherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetPhraseMatcherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_phrase_matcher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_phrase_matcher(
        self, response: resources.PhraseMatcher
    ) -> resources.PhraseMatcher:
        """Post-rpc interceptor for get_phrase_matcher

        DEPRECATED. Please use the `post_get_phrase_matcher_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_phrase_matcher` interceptor runs
        before the `post_get_phrase_matcher_with_metadata` interceptor.
        """
        return response

    def post_get_phrase_matcher_with_metadata(
        self,
        response: resources.PhraseMatcher,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.PhraseMatcher, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_phrase_matcher

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_phrase_matcher_with_metadata`
        interceptor in new development instead of the `post_get_phrase_matcher` interceptor.
        When both interceptors are used, this `post_get_phrase_matcher_with_metadata` interceptor runs after the
        `post_get_phrase_matcher` interceptor. The (possibly modified) response returned by
        `post_get_phrase_matcher` will be passed to
        `post_get_phrase_matcher_with_metadata`.
        """
        return response, metadata

    def pre_get_qa_question(
        self,
        request: contact_center_insights.GetQaQuestionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetQaQuestionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_qa_question

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_qa_question(
        self, response: resources.QaQuestion
    ) -> resources.QaQuestion:
        """Post-rpc interceptor for get_qa_question

        DEPRECATED. Please use the `post_get_qa_question_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_qa_question` interceptor runs
        before the `post_get_qa_question_with_metadata` interceptor.
        """
        return response

    def post_get_qa_question_with_metadata(
        self,
        response: resources.QaQuestion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaQuestion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_qa_question

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_qa_question_with_metadata`
        interceptor in new development instead of the `post_get_qa_question` interceptor.
        When both interceptors are used, this `post_get_qa_question_with_metadata` interceptor runs after the
        `post_get_qa_question` interceptor. The (possibly modified) response returned by
        `post_get_qa_question` will be passed to
        `post_get_qa_question_with_metadata`.
        """
        return response, metadata

    def pre_get_qa_scorecard(
        self,
        request: contact_center_insights.GetQaScorecardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetQaScorecardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_qa_scorecard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_qa_scorecard(
        self, response: resources.QaScorecard
    ) -> resources.QaScorecard:
        """Post-rpc interceptor for get_qa_scorecard

        DEPRECATED. Please use the `post_get_qa_scorecard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_qa_scorecard` interceptor runs
        before the `post_get_qa_scorecard_with_metadata` interceptor.
        """
        return response

    def post_get_qa_scorecard_with_metadata(
        self,
        response: resources.QaScorecard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecard, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_qa_scorecard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_qa_scorecard_with_metadata`
        interceptor in new development instead of the `post_get_qa_scorecard` interceptor.
        When both interceptors are used, this `post_get_qa_scorecard_with_metadata` interceptor runs after the
        `post_get_qa_scorecard` interceptor. The (possibly modified) response returned by
        `post_get_qa_scorecard` will be passed to
        `post_get_qa_scorecard_with_metadata`.
        """
        return response, metadata

    def pre_get_qa_scorecard_revision(
        self,
        request: contact_center_insights.GetQaScorecardRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetQaScorecardRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_qa_scorecard_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_qa_scorecard_revision(
        self, response: resources.QaScorecardRevision
    ) -> resources.QaScorecardRevision:
        """Post-rpc interceptor for get_qa_scorecard_revision

        DEPRECATED. Please use the `post_get_qa_scorecard_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_qa_scorecard_revision` interceptor runs
        before the `post_get_qa_scorecard_revision_with_metadata` interceptor.
        """
        return response

    def post_get_qa_scorecard_revision_with_metadata(
        self,
        response: resources.QaScorecardRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecardRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_qa_scorecard_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_qa_scorecard_revision_with_metadata`
        interceptor in new development instead of the `post_get_qa_scorecard_revision` interceptor.
        When both interceptors are used, this `post_get_qa_scorecard_revision_with_metadata` interceptor runs after the
        `post_get_qa_scorecard_revision` interceptor. The (possibly modified) response returned by
        `post_get_qa_scorecard_revision` will be passed to
        `post_get_qa_scorecard_revision_with_metadata`.
        """
        return response, metadata

    def pre_get_settings(
        self,
        request: contact_center_insights.GetSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for get_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_settings(self, response: resources.Settings) -> resources.Settings:
        """Post-rpc interceptor for get_settings

        DEPRECATED. Please use the `post_get_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_settings` interceptor runs
        before the `post_get_settings_with_metadata` interceptor.
        """
        return response

    def post_get_settings_with_metadata(
        self,
        response: resources.Settings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Settings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_settings_with_metadata`
        interceptor in new development instead of the `post_get_settings` interceptor.
        When both interceptors are used, this `post_get_settings_with_metadata` interceptor runs after the
        `post_get_settings` interceptor. The (possibly modified) response returned by
        `post_get_settings` will be passed to
        `post_get_settings_with_metadata`.
        """
        return response, metadata

    def pre_get_view(
        self,
        request: contact_center_insights.GetViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.GetViewRequest, Sequence[Tuple[str, Union[str, bytes]]]
    ]:
        """Pre-rpc interceptor for get_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_view(self, response: resources.View) -> resources.View:
        """Post-rpc interceptor for get_view

        DEPRECATED. Please use the `post_get_view_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_get_view` interceptor runs
        before the `post_get_view_with_metadata` interceptor.
        """
        return response

    def post_get_view_with_metadata(
        self,
        response: resources.View,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.View, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for get_view

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_get_view_with_metadata`
        interceptor in new development instead of the `post_get_view` interceptor.
        When both interceptors are used, this `post_get_view_with_metadata` interceptor runs after the
        `post_get_view` interceptor. The (possibly modified) response returned by
        `post_get_view` will be passed to
        `post_get_view_with_metadata`.
        """
        return response, metadata

    def pre_import_issue_model(
        self,
        request: contact_center_insights.ImportIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ImportIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for import_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_import_issue_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for import_issue_model

        DEPRECATED. Please use the `post_import_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_import_issue_model` interceptor runs
        before the `post_import_issue_model_with_metadata` interceptor.
        """
        return response

    def post_import_issue_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for import_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_import_issue_model_with_metadata`
        interceptor in new development instead of the `post_import_issue_model` interceptor.
        When both interceptors are used, this `post_import_issue_model_with_metadata` interceptor runs after the
        `post_import_issue_model` interceptor. The (possibly modified) response returned by
        `post_import_issue_model` will be passed to
        `post_import_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_ingest_conversations(
        self,
        request: contact_center_insights.IngestConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.IngestConversationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for ingest_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_ingest_conversations(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for ingest_conversations

        DEPRECATED. Please use the `post_ingest_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_ingest_conversations` interceptor runs
        before the `post_ingest_conversations_with_metadata` interceptor.
        """
        return response

    def post_ingest_conversations_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for ingest_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_ingest_conversations_with_metadata`
        interceptor in new development instead of the `post_ingest_conversations` interceptor.
        When both interceptors are used, this `post_ingest_conversations_with_metadata` interceptor runs after the
        `post_ingest_conversations` interceptor. The (possibly modified) response returned by
        `post_ingest_conversations` will be passed to
        `post_ingest_conversations_with_metadata`.
        """
        return response, metadata

    def pre_initialize_encryption_spec(
        self,
        request: contact_center_insights.InitializeEncryptionSpecRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.InitializeEncryptionSpecRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for initialize_encryption_spec

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_initialize_encryption_spec(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for initialize_encryption_spec

        DEPRECATED. Please use the `post_initialize_encryption_spec_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_initialize_encryption_spec` interceptor runs
        before the `post_initialize_encryption_spec_with_metadata` interceptor.
        """
        return response

    def post_initialize_encryption_spec_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for initialize_encryption_spec

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_initialize_encryption_spec_with_metadata`
        interceptor in new development instead of the `post_initialize_encryption_spec` interceptor.
        When both interceptors are used, this `post_initialize_encryption_spec_with_metadata` interceptor runs after the
        `post_initialize_encryption_spec` interceptor. The (possibly modified) response returned by
        `post_initialize_encryption_spec` will be passed to
        `post_initialize_encryption_spec_with_metadata`.
        """
        return response, metadata

    def pre_list_all_feedback_labels(
        self,
        request: contact_center_insights.ListAllFeedbackLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListAllFeedbackLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_all_feedback_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_all_feedback_labels(
        self, response: contact_center_insights.ListAllFeedbackLabelsResponse
    ) -> contact_center_insights.ListAllFeedbackLabelsResponse:
        """Post-rpc interceptor for list_all_feedback_labels

        DEPRECATED. Please use the `post_list_all_feedback_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_all_feedback_labels` interceptor runs
        before the `post_list_all_feedback_labels_with_metadata` interceptor.
        """
        return response

    def post_list_all_feedback_labels_with_metadata(
        self,
        response: contact_center_insights.ListAllFeedbackLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListAllFeedbackLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_all_feedback_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_all_feedback_labels_with_metadata`
        interceptor in new development instead of the `post_list_all_feedback_labels` interceptor.
        When both interceptors are used, this `post_list_all_feedback_labels_with_metadata` interceptor runs after the
        `post_list_all_feedback_labels` interceptor. The (possibly modified) response returned by
        `post_list_all_feedback_labels` will be passed to
        `post_list_all_feedback_labels_with_metadata`.
        """
        return response, metadata

    def pre_list_analyses(
        self,
        request: contact_center_insights.ListAnalysesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListAnalysesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_analyses

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_analyses(
        self, response: contact_center_insights.ListAnalysesResponse
    ) -> contact_center_insights.ListAnalysesResponse:
        """Post-rpc interceptor for list_analyses

        DEPRECATED. Please use the `post_list_analyses_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_analyses` interceptor runs
        before the `post_list_analyses_with_metadata` interceptor.
        """
        return response

    def post_list_analyses_with_metadata(
        self,
        response: contact_center_insights.ListAnalysesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListAnalysesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_analyses

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_analyses_with_metadata`
        interceptor in new development instead of the `post_list_analyses` interceptor.
        When both interceptors are used, this `post_list_analyses_with_metadata` interceptor runs after the
        `post_list_analyses` interceptor. The (possibly modified) response returned by
        `post_list_analyses` will be passed to
        `post_list_analyses_with_metadata`.
        """
        return response, metadata

    def pre_list_analysis_rules(
        self,
        request: contact_center_insights.ListAnalysisRulesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListAnalysisRulesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_analysis_rules

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_analysis_rules(
        self, response: contact_center_insights.ListAnalysisRulesResponse
    ) -> contact_center_insights.ListAnalysisRulesResponse:
        """Post-rpc interceptor for list_analysis_rules

        DEPRECATED. Please use the `post_list_analysis_rules_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_analysis_rules` interceptor runs
        before the `post_list_analysis_rules_with_metadata` interceptor.
        """
        return response

    def post_list_analysis_rules_with_metadata(
        self,
        response: contact_center_insights.ListAnalysisRulesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListAnalysisRulesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_analysis_rules

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_analysis_rules_with_metadata`
        interceptor in new development instead of the `post_list_analysis_rules` interceptor.
        When both interceptors are used, this `post_list_analysis_rules_with_metadata` interceptor runs after the
        `post_list_analysis_rules` interceptor. The (possibly modified) response returned by
        `post_list_analysis_rules` will be passed to
        `post_list_analysis_rules_with_metadata`.
        """
        return response, metadata

    def pre_list_conversations(
        self,
        request: contact_center_insights.ListConversationsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListConversationsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_conversations

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_conversations(
        self, response: contact_center_insights.ListConversationsResponse
    ) -> contact_center_insights.ListConversationsResponse:
        """Post-rpc interceptor for list_conversations

        DEPRECATED. Please use the `post_list_conversations_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_conversations` interceptor runs
        before the `post_list_conversations_with_metadata` interceptor.
        """
        return response

    def post_list_conversations_with_metadata(
        self,
        response: contact_center_insights.ListConversationsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListConversationsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_conversations

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_conversations_with_metadata`
        interceptor in new development instead of the `post_list_conversations` interceptor.
        When both interceptors are used, this `post_list_conversations_with_metadata` interceptor runs after the
        `post_list_conversations` interceptor. The (possibly modified) response returned by
        `post_list_conversations` will be passed to
        `post_list_conversations_with_metadata`.
        """
        return response, metadata

    def pre_list_feedback_labels(
        self,
        request: contact_center_insights.ListFeedbackLabelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListFeedbackLabelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_feedback_labels

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_feedback_labels(
        self, response: contact_center_insights.ListFeedbackLabelsResponse
    ) -> contact_center_insights.ListFeedbackLabelsResponse:
        """Post-rpc interceptor for list_feedback_labels

        DEPRECATED. Please use the `post_list_feedback_labels_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_feedback_labels` interceptor runs
        before the `post_list_feedback_labels_with_metadata` interceptor.
        """
        return response

    def post_list_feedback_labels_with_metadata(
        self,
        response: contact_center_insights.ListFeedbackLabelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListFeedbackLabelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_feedback_labels

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_feedback_labels_with_metadata`
        interceptor in new development instead of the `post_list_feedback_labels` interceptor.
        When both interceptors are used, this `post_list_feedback_labels_with_metadata` interceptor runs after the
        `post_list_feedback_labels` interceptor. The (possibly modified) response returned by
        `post_list_feedback_labels` will be passed to
        `post_list_feedback_labels_with_metadata`.
        """
        return response, metadata

    def pre_list_issue_models(
        self,
        request: contact_center_insights.ListIssueModelsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListIssueModelsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_issue_models

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_issue_models(
        self, response: contact_center_insights.ListIssueModelsResponse
    ) -> contact_center_insights.ListIssueModelsResponse:
        """Post-rpc interceptor for list_issue_models

        DEPRECATED. Please use the `post_list_issue_models_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_issue_models` interceptor runs
        before the `post_list_issue_models_with_metadata` interceptor.
        """
        return response

    def post_list_issue_models_with_metadata(
        self,
        response: contact_center_insights.ListIssueModelsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListIssueModelsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_issue_models

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_issue_models_with_metadata`
        interceptor in new development instead of the `post_list_issue_models` interceptor.
        When both interceptors are used, this `post_list_issue_models_with_metadata` interceptor runs after the
        `post_list_issue_models` interceptor. The (possibly modified) response returned by
        `post_list_issue_models` will be passed to
        `post_list_issue_models_with_metadata`.
        """
        return response, metadata

    def pre_list_issues(
        self,
        request: contact_center_insights.ListIssuesRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListIssuesRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_issues

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_issues(
        self, response: contact_center_insights.ListIssuesResponse
    ) -> contact_center_insights.ListIssuesResponse:
        """Post-rpc interceptor for list_issues

        DEPRECATED. Please use the `post_list_issues_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_issues` interceptor runs
        before the `post_list_issues_with_metadata` interceptor.
        """
        return response

    def post_list_issues_with_metadata(
        self,
        response: contact_center_insights.ListIssuesResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListIssuesResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_issues

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_issues_with_metadata`
        interceptor in new development instead of the `post_list_issues` interceptor.
        When both interceptors are used, this `post_list_issues_with_metadata` interceptor runs after the
        `post_list_issues` interceptor. The (possibly modified) response returned by
        `post_list_issues` will be passed to
        `post_list_issues_with_metadata`.
        """
        return response, metadata

    def pre_list_phrase_matchers(
        self,
        request: contact_center_insights.ListPhraseMatchersRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListPhraseMatchersRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_phrase_matchers

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_phrase_matchers(
        self, response: contact_center_insights.ListPhraseMatchersResponse
    ) -> contact_center_insights.ListPhraseMatchersResponse:
        """Post-rpc interceptor for list_phrase_matchers

        DEPRECATED. Please use the `post_list_phrase_matchers_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_phrase_matchers` interceptor runs
        before the `post_list_phrase_matchers_with_metadata` interceptor.
        """
        return response

    def post_list_phrase_matchers_with_metadata(
        self,
        response: contact_center_insights.ListPhraseMatchersResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListPhraseMatchersResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_phrase_matchers

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_phrase_matchers_with_metadata`
        interceptor in new development instead of the `post_list_phrase_matchers` interceptor.
        When both interceptors are used, this `post_list_phrase_matchers_with_metadata` interceptor runs after the
        `post_list_phrase_matchers` interceptor. The (possibly modified) response returned by
        `post_list_phrase_matchers` will be passed to
        `post_list_phrase_matchers_with_metadata`.
        """
        return response, metadata

    def pre_list_qa_questions(
        self,
        request: contact_center_insights.ListQaQuestionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListQaQuestionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_qa_questions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_qa_questions(
        self, response: contact_center_insights.ListQaQuestionsResponse
    ) -> contact_center_insights.ListQaQuestionsResponse:
        """Post-rpc interceptor for list_qa_questions

        DEPRECATED. Please use the `post_list_qa_questions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_qa_questions` interceptor runs
        before the `post_list_qa_questions_with_metadata` interceptor.
        """
        return response

    def post_list_qa_questions_with_metadata(
        self,
        response: contact_center_insights.ListQaQuestionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListQaQuestionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_qa_questions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_qa_questions_with_metadata`
        interceptor in new development instead of the `post_list_qa_questions` interceptor.
        When both interceptors are used, this `post_list_qa_questions_with_metadata` interceptor runs after the
        `post_list_qa_questions` interceptor. The (possibly modified) response returned by
        `post_list_qa_questions` will be passed to
        `post_list_qa_questions_with_metadata`.
        """
        return response, metadata

    def pre_list_qa_scorecard_revisions(
        self,
        request: contact_center_insights.ListQaScorecardRevisionsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListQaScorecardRevisionsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_qa_scorecard_revisions

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_qa_scorecard_revisions(
        self, response: contact_center_insights.ListQaScorecardRevisionsResponse
    ) -> contact_center_insights.ListQaScorecardRevisionsResponse:
        """Post-rpc interceptor for list_qa_scorecard_revisions

        DEPRECATED. Please use the `post_list_qa_scorecard_revisions_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_qa_scorecard_revisions` interceptor runs
        before the `post_list_qa_scorecard_revisions_with_metadata` interceptor.
        """
        return response

    def post_list_qa_scorecard_revisions_with_metadata(
        self,
        response: contact_center_insights.ListQaScorecardRevisionsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListQaScorecardRevisionsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_qa_scorecard_revisions

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_qa_scorecard_revisions_with_metadata`
        interceptor in new development instead of the `post_list_qa_scorecard_revisions` interceptor.
        When both interceptors are used, this `post_list_qa_scorecard_revisions_with_metadata` interceptor runs after the
        `post_list_qa_scorecard_revisions` interceptor. The (possibly modified) response returned by
        `post_list_qa_scorecard_revisions` will be passed to
        `post_list_qa_scorecard_revisions_with_metadata`.
        """
        return response, metadata

    def pre_list_qa_scorecards(
        self,
        request: contact_center_insights.ListQaScorecardsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListQaScorecardsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_qa_scorecards

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_qa_scorecards(
        self, response: contact_center_insights.ListQaScorecardsResponse
    ) -> contact_center_insights.ListQaScorecardsResponse:
        """Post-rpc interceptor for list_qa_scorecards

        DEPRECATED. Please use the `post_list_qa_scorecards_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_qa_scorecards` interceptor runs
        before the `post_list_qa_scorecards_with_metadata` interceptor.
        """
        return response

    def post_list_qa_scorecards_with_metadata(
        self,
        response: contact_center_insights.ListQaScorecardsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListQaScorecardsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_qa_scorecards

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_qa_scorecards_with_metadata`
        interceptor in new development instead of the `post_list_qa_scorecards` interceptor.
        When both interceptors are used, this `post_list_qa_scorecards_with_metadata` interceptor runs after the
        `post_list_qa_scorecards` interceptor. The (possibly modified) response returned by
        `post_list_qa_scorecards` will be passed to
        `post_list_qa_scorecards_with_metadata`.
        """
        return response, metadata

    def pre_list_views(
        self,
        request: contact_center_insights.ListViewsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListViewsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for list_views

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_views(
        self, response: contact_center_insights.ListViewsResponse
    ) -> contact_center_insights.ListViewsResponse:
        """Post-rpc interceptor for list_views

        DEPRECATED. Please use the `post_list_views_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_list_views` interceptor runs
        before the `post_list_views_with_metadata` interceptor.
        """
        return response

    def post_list_views_with_metadata(
        self,
        response: contact_center_insights.ListViewsResponse,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.ListViewsResponse,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Post-rpc interceptor for list_views

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_list_views_with_metadata`
        interceptor in new development instead of the `post_list_views` interceptor.
        When both interceptors are used, this `post_list_views_with_metadata` interceptor runs after the
        `post_list_views` interceptor. The (possibly modified) response returned by
        `post_list_views` will be passed to
        `post_list_views_with_metadata`.
        """
        return response, metadata

    def pre_query_metrics(
        self,
        request: contact_center_insights.QueryMetricsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.QueryMetricsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for query_metrics

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_query_metrics(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for query_metrics

        DEPRECATED. Please use the `post_query_metrics_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_query_metrics` interceptor runs
        before the `post_query_metrics_with_metadata` interceptor.
        """
        return response

    def post_query_metrics_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for query_metrics

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_query_metrics_with_metadata`
        interceptor in new development instead of the `post_query_metrics` interceptor.
        When both interceptors are used, this `post_query_metrics_with_metadata` interceptor runs after the
        `post_query_metrics` interceptor. The (possibly modified) response returned by
        `post_query_metrics` will be passed to
        `post_query_metrics_with_metadata`.
        """
        return response, metadata

    def pre_tune_qa_scorecard_revision(
        self,
        request: contact_center_insights.TuneQaScorecardRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.TuneQaScorecardRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for tune_qa_scorecard_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_tune_qa_scorecard_revision(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for tune_qa_scorecard_revision

        DEPRECATED. Please use the `post_tune_qa_scorecard_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_tune_qa_scorecard_revision` interceptor runs
        before the `post_tune_qa_scorecard_revision_with_metadata` interceptor.
        """
        return response

    def post_tune_qa_scorecard_revision_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for tune_qa_scorecard_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_tune_qa_scorecard_revision_with_metadata`
        interceptor in new development instead of the `post_tune_qa_scorecard_revision` interceptor.
        When both interceptors are used, this `post_tune_qa_scorecard_revision_with_metadata` interceptor runs after the
        `post_tune_qa_scorecard_revision` interceptor. The (possibly modified) response returned by
        `post_tune_qa_scorecard_revision` will be passed to
        `post_tune_qa_scorecard_revision_with_metadata`.
        """
        return response, metadata

    def pre_undeploy_issue_model(
        self,
        request: contact_center_insights.UndeployIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UndeployIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undeploy_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_undeploy_issue_model(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for undeploy_issue_model

        DEPRECATED. Please use the `post_undeploy_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_undeploy_issue_model` interceptor runs
        before the `post_undeploy_issue_model_with_metadata` interceptor.
        """
        return response

    def post_undeploy_issue_model_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undeploy_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_undeploy_issue_model_with_metadata`
        interceptor in new development instead of the `post_undeploy_issue_model` interceptor.
        When both interceptors are used, this `post_undeploy_issue_model_with_metadata` interceptor runs after the
        `post_undeploy_issue_model` interceptor. The (possibly modified) response returned by
        `post_undeploy_issue_model` will be passed to
        `post_undeploy_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_undeploy_qa_scorecard_revision(
        self,
        request: contact_center_insights.UndeployQaScorecardRevisionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UndeployQaScorecardRevisionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for undeploy_qa_scorecard_revision

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_undeploy_qa_scorecard_revision(
        self, response: resources.QaScorecardRevision
    ) -> resources.QaScorecardRevision:
        """Post-rpc interceptor for undeploy_qa_scorecard_revision

        DEPRECATED. Please use the `post_undeploy_qa_scorecard_revision_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_undeploy_qa_scorecard_revision` interceptor runs
        before the `post_undeploy_qa_scorecard_revision_with_metadata` interceptor.
        """
        return response

    def post_undeploy_qa_scorecard_revision_with_metadata(
        self,
        response: resources.QaScorecardRevision,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecardRevision, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for undeploy_qa_scorecard_revision

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_undeploy_qa_scorecard_revision_with_metadata`
        interceptor in new development instead of the `post_undeploy_qa_scorecard_revision` interceptor.
        When both interceptors are used, this `post_undeploy_qa_scorecard_revision_with_metadata` interceptor runs after the
        `post_undeploy_qa_scorecard_revision` interceptor. The (possibly modified) response returned by
        `post_undeploy_qa_scorecard_revision` will be passed to
        `post_undeploy_qa_scorecard_revision_with_metadata`.
        """
        return response, metadata

    def pre_update_analysis_rule(
        self,
        request: contact_center_insights.UpdateAnalysisRuleRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateAnalysisRuleRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_analysis_rule

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_analysis_rule(
        self, response: resources.AnalysisRule
    ) -> resources.AnalysisRule:
        """Post-rpc interceptor for update_analysis_rule

        DEPRECATED. Please use the `post_update_analysis_rule_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_analysis_rule` interceptor runs
        before the `post_update_analysis_rule_with_metadata` interceptor.
        """
        return response

    def post_update_analysis_rule_with_metadata(
        self,
        response: resources.AnalysisRule,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.AnalysisRule, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_analysis_rule

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_analysis_rule_with_metadata`
        interceptor in new development instead of the `post_update_analysis_rule` interceptor.
        When both interceptors are used, this `post_update_analysis_rule_with_metadata` interceptor runs after the
        `post_update_analysis_rule` interceptor. The (possibly modified) response returned by
        `post_update_analysis_rule` will be passed to
        `post_update_analysis_rule_with_metadata`.
        """
        return response, metadata

    def pre_update_conversation(
        self,
        request: contact_center_insights.UpdateConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_conversation(
        self, response: resources.Conversation
    ) -> resources.Conversation:
        """Post-rpc interceptor for update_conversation

        DEPRECATED. Please use the `post_update_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_conversation` interceptor runs
        before the `post_update_conversation_with_metadata` interceptor.
        """
        return response

    def post_update_conversation_with_metadata(
        self,
        response: resources.Conversation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Conversation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_conversation_with_metadata`
        interceptor in new development instead of the `post_update_conversation` interceptor.
        When both interceptors are used, this `post_update_conversation_with_metadata` interceptor runs after the
        `post_update_conversation` interceptor. The (possibly modified) response returned by
        `post_update_conversation` will be passed to
        `post_update_conversation_with_metadata`.
        """
        return response, metadata

    def pre_update_feedback_label(
        self,
        request: contact_center_insights.UpdateFeedbackLabelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateFeedbackLabelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_feedback_label

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_feedback_label(
        self, response: resources.FeedbackLabel
    ) -> resources.FeedbackLabel:
        """Post-rpc interceptor for update_feedback_label

        DEPRECATED. Please use the `post_update_feedback_label_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_feedback_label` interceptor runs
        before the `post_update_feedback_label_with_metadata` interceptor.
        """
        return response

    def post_update_feedback_label_with_metadata(
        self,
        response: resources.FeedbackLabel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.FeedbackLabel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_feedback_label

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_feedback_label_with_metadata`
        interceptor in new development instead of the `post_update_feedback_label` interceptor.
        When both interceptors are used, this `post_update_feedback_label_with_metadata` interceptor runs after the
        `post_update_feedback_label` interceptor. The (possibly modified) response returned by
        `post_update_feedback_label` will be passed to
        `post_update_feedback_label_with_metadata`.
        """
        return response, metadata

    def pre_update_issue(
        self,
        request: contact_center_insights.UpdateIssueRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateIssueRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_issue

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_issue(self, response: resources.Issue) -> resources.Issue:
        """Post-rpc interceptor for update_issue

        DEPRECATED. Please use the `post_update_issue_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_issue` interceptor runs
        before the `post_update_issue_with_metadata` interceptor.
        """
        return response

    def post_update_issue_with_metadata(
        self,
        response: resources.Issue,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Issue, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_issue

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_issue_with_metadata`
        interceptor in new development instead of the `post_update_issue` interceptor.
        When both interceptors are used, this `post_update_issue_with_metadata` interceptor runs after the
        `post_update_issue` interceptor. The (possibly modified) response returned by
        `post_update_issue` will be passed to
        `post_update_issue_with_metadata`.
        """
        return response, metadata

    def pre_update_issue_model(
        self,
        request: contact_center_insights.UpdateIssueModelRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateIssueModelRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_issue_model

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_issue_model(
        self, response: resources.IssueModel
    ) -> resources.IssueModel:
        """Post-rpc interceptor for update_issue_model

        DEPRECATED. Please use the `post_update_issue_model_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_issue_model` interceptor runs
        before the `post_update_issue_model_with_metadata` interceptor.
        """
        return response

    def post_update_issue_model_with_metadata(
        self,
        response: resources.IssueModel,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.IssueModel, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_issue_model

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_issue_model_with_metadata`
        interceptor in new development instead of the `post_update_issue_model` interceptor.
        When both interceptors are used, this `post_update_issue_model_with_metadata` interceptor runs after the
        `post_update_issue_model` interceptor. The (possibly modified) response returned by
        `post_update_issue_model` will be passed to
        `post_update_issue_model_with_metadata`.
        """
        return response, metadata

    def pre_update_phrase_matcher(
        self,
        request: contact_center_insights.UpdatePhraseMatcherRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdatePhraseMatcherRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_phrase_matcher

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_phrase_matcher(
        self, response: resources.PhraseMatcher
    ) -> resources.PhraseMatcher:
        """Post-rpc interceptor for update_phrase_matcher

        DEPRECATED. Please use the `post_update_phrase_matcher_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_phrase_matcher` interceptor runs
        before the `post_update_phrase_matcher_with_metadata` interceptor.
        """
        return response

    def post_update_phrase_matcher_with_metadata(
        self,
        response: resources.PhraseMatcher,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.PhraseMatcher, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_phrase_matcher

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_phrase_matcher_with_metadata`
        interceptor in new development instead of the `post_update_phrase_matcher` interceptor.
        When both interceptors are used, this `post_update_phrase_matcher_with_metadata` interceptor runs after the
        `post_update_phrase_matcher` interceptor. The (possibly modified) response returned by
        `post_update_phrase_matcher` will be passed to
        `post_update_phrase_matcher_with_metadata`.
        """
        return response, metadata

    def pre_update_qa_question(
        self,
        request: contact_center_insights.UpdateQaQuestionRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateQaQuestionRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_qa_question

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_qa_question(
        self, response: resources.QaQuestion
    ) -> resources.QaQuestion:
        """Post-rpc interceptor for update_qa_question

        DEPRECATED. Please use the `post_update_qa_question_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_qa_question` interceptor runs
        before the `post_update_qa_question_with_metadata` interceptor.
        """
        return response

    def post_update_qa_question_with_metadata(
        self,
        response: resources.QaQuestion,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaQuestion, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_qa_question

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_qa_question_with_metadata`
        interceptor in new development instead of the `post_update_qa_question` interceptor.
        When both interceptors are used, this `post_update_qa_question_with_metadata` interceptor runs after the
        `post_update_qa_question` interceptor. The (possibly modified) response returned by
        `post_update_qa_question` will be passed to
        `post_update_qa_question_with_metadata`.
        """
        return response, metadata

    def pre_update_qa_scorecard(
        self,
        request: contact_center_insights.UpdateQaScorecardRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateQaScorecardRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_qa_scorecard

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_qa_scorecard(
        self, response: resources.QaScorecard
    ) -> resources.QaScorecard:
        """Post-rpc interceptor for update_qa_scorecard

        DEPRECATED. Please use the `post_update_qa_scorecard_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_qa_scorecard` interceptor runs
        before the `post_update_qa_scorecard_with_metadata` interceptor.
        """
        return response

    def post_update_qa_scorecard_with_metadata(
        self,
        response: resources.QaScorecard,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.QaScorecard, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_qa_scorecard

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_qa_scorecard_with_metadata`
        interceptor in new development instead of the `post_update_qa_scorecard` interceptor.
        When both interceptors are used, this `post_update_qa_scorecard_with_metadata` interceptor runs after the
        `post_update_qa_scorecard` interceptor. The (possibly modified) response returned by
        `post_update_qa_scorecard` will be passed to
        `post_update_qa_scorecard_with_metadata`.
        """
        return response, metadata

    def pre_update_settings(
        self,
        request: contact_center_insights.UpdateSettingsRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateSettingsRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_settings

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_settings(self, response: resources.Settings) -> resources.Settings:
        """Post-rpc interceptor for update_settings

        DEPRECATED. Please use the `post_update_settings_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_settings` interceptor runs
        before the `post_update_settings_with_metadata` interceptor.
        """
        return response

    def post_update_settings_with_metadata(
        self,
        response: resources.Settings,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.Settings, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_settings

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_settings_with_metadata`
        interceptor in new development instead of the `post_update_settings` interceptor.
        When both interceptors are used, this `post_update_settings_with_metadata` interceptor runs after the
        `post_update_settings` interceptor. The (possibly modified) response returned by
        `post_update_settings` will be passed to
        `post_update_settings_with_metadata`.
        """
        return response, metadata

    def pre_update_view(
        self,
        request: contact_center_insights.UpdateViewRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UpdateViewRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for update_view

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_update_view(self, response: resources.View) -> resources.View:
        """Post-rpc interceptor for update_view

        DEPRECATED. Please use the `post_update_view_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_update_view` interceptor runs
        before the `post_update_view_with_metadata` interceptor.
        """
        return response

    def post_update_view_with_metadata(
        self,
        response: resources.View,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[resources.View, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for update_view

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_update_view_with_metadata`
        interceptor in new development instead of the `post_update_view` interceptor.
        When both interceptors are used, this `post_update_view_with_metadata` interceptor runs after the
        `post_update_view` interceptor. The (possibly modified) response returned by
        `post_update_view` will be passed to
        `post_update_view_with_metadata`.
        """
        return response, metadata

    def pre_upload_conversation(
        self,
        request: contact_center_insights.UploadConversationRequest,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[
        contact_center_insights.UploadConversationRequest,
        Sequence[Tuple[str, Union[str, bytes]]],
    ]:
        """Pre-rpc interceptor for upload_conversation

        Override in a subclass to manipulate the request or metadata
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_upload_conversation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for upload_conversation

        DEPRECATED. Please use the `post_upload_conversation_with_metadata`
        interceptor instead.

        Override in a subclass to read or manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code. This `post_upload_conversation` interceptor runs
        before the `post_upload_conversation_with_metadata` interceptor.
        """
        return response

    def post_upload_conversation_with_metadata(
        self,
        response: operations_pb2.Operation,
        metadata: Sequence[Tuple[str, Union[str, bytes]]],
    ) -> Tuple[operations_pb2.Operation, Sequence[Tuple[str, Union[str, bytes]]]]:
        """Post-rpc interceptor for upload_conversation

        Override in a subclass to read or manipulate the response or metadata after it
        is returned by the ContactCenterInsights server but before it is returned to user code.

        We recommend only using this `post_upload_conversation_with_metadata`
        interceptor in new development instead of the `post_upload_conversation` interceptor.
        When both interceptors are used, this `post_upload_conversation_with_metadata` interceptor runs after the
        `post_upload_conversation` interceptor. The (possibly modified) response returned by
        `post_upload_conversation` will be passed to
        `post_upload_conversation_with_metadata`.
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
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_cancel_operation(self, response: None) -> None:
        """Post-rpc interceptor for cancel_operation

        Override in a subclass to manipulate the response
        after it is returned by the ContactCenterInsights server but before
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
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_get_operation(
        self, response: operations_pb2.Operation
    ) -> operations_pb2.Operation:
        """Post-rpc interceptor for get_operation

        Override in a subclass to manipulate the response
        after it is returned by the ContactCenterInsights server but before
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
        before they are sent to the ContactCenterInsights server.
        """
        return request, metadata

    def post_list_operations(
        self, response: operations_pb2.ListOperationsResponse
    ) -> operations_pb2.ListOperationsResponse:
        """Post-rpc interceptor for list_operations

        Override in a subclass to manipulate the response
        after it is returned by the ContactCenterInsights server but before
        it is returned to user code.
        """
        return response


@dataclasses.dataclass
class ContactCenterInsightsRestStub:
    _session: AuthorizedSession
    _host: str
    _interceptor: ContactCenterInsightsRestInterceptor


class ContactCenterInsightsRestTransport(_BaseContactCenterInsightsRestTransport):
    """REST backend synchronous transport for ContactCenterInsights.

    An API that lets users analyze and explore their business
    conversation data.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends JSON representations of protocol buffers over HTTP/1.1
    """

    def __init__(
        self,
        *,
        host: str = "contactcenterinsights.googleapis.com",
        credentials: Optional[ga_credentials.Credentials] = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        client_cert_source_for_mtls: Optional[Callable[[], Tuple[bytes, bytes]]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        url_scheme: str = "https",
        interceptor: Optional[ContactCenterInsightsRestInterceptor] = None,
        api_audience: Optional[str] = None,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'contactcenterinsights.googleapis.com').
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
            interceptor (Optional[ContactCenterInsightsRestInterceptor]): Interceptor used
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
        self._interceptor = interceptor or ContactCenterInsightsRestInterceptor()
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

    class _BulkAnalyzeConversations(
        _BaseContactCenterInsightsRestTransport._BaseBulkAnalyzeConversations,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.BulkAnalyzeConversations")

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
            request: contact_center_insights.BulkAnalyzeConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the bulk analyze
            conversations method over HTTP.

                Args:
                    request (~.contact_center_insights.BulkAnalyzeConversationsRequest):
                        The request object. The request to analyze conversations
                    in bulk.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseBulkAnalyzeConversations._get_http_options()
            request, metadata = self._interceptor.pre_bulk_analyze_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseBulkAnalyzeConversations,
                    "_BaseBulkAnalyzeConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.BulkAnalyzeConversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkAnalyzeConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._BulkAnalyzeConversations._get_response(
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

            resp = self._interceptor.post_bulk_analyze_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_analyze_conversations_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.bulk_analyze_conversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkAnalyzeConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkDeleteConversations(
        _BaseContactCenterInsightsRestTransport._BaseBulkDeleteConversations,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.BulkDeleteConversations")

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
            request: contact_center_insights.BulkDeleteConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the bulk delete conversations method over HTTP.

            Args:
                request (~.contact_center_insights.BulkDeleteConversationsRequest):
                    The request object. The request to delete conversations
                in bulk.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseBulkDeleteConversations._get_http_options()
            request, metadata = self._interceptor.pre_bulk_delete_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseBulkDeleteConversations,
                    "_BaseBulkDeleteConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.BulkDeleteConversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkDeleteConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._BulkDeleteConversations._get_response(
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

            resp = self._interceptor.post_bulk_delete_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_delete_conversations_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.bulk_delete_conversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkDeleteConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkDownloadFeedbackLabels(
        _BaseContactCenterInsightsRestTransport._BaseBulkDownloadFeedbackLabels,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.BulkDownloadFeedbackLabels")

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
            request: contact_center_insights.BulkDownloadFeedbackLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the bulk download feedback
            labels method over HTTP.

                Args:
                    request (~.contact_center_insights.BulkDownloadFeedbackLabelsRequest):
                        The request object. Request for the
                    BulkDownloadFeedbackLabel endpoint.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseBulkDownloadFeedbackLabels._get_http_options()
            request, metadata = self._interceptor.pre_bulk_download_feedback_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseBulkDownloadFeedbackLabels,
                    "_BaseBulkDownloadFeedbackLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.BulkDownloadFeedbackLabels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkDownloadFeedbackLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._BulkDownloadFeedbackLabels._get_response(
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

            resp = self._interceptor.post_bulk_download_feedback_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_bulk_download_feedback_labels_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.bulk_download_feedback_labels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkDownloadFeedbackLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _BulkUploadFeedbackLabels(
        _BaseContactCenterInsightsRestTransport._BaseBulkUploadFeedbackLabels,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.BulkUploadFeedbackLabels")

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
            request: contact_center_insights.BulkUploadFeedbackLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the bulk upload feedback
            labels method over HTTP.

                Args:
                    request (~.contact_center_insights.BulkUploadFeedbackLabelsRequest):
                        The request object. The request for bulk uploading
                    feedback labels.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseBulkUploadFeedbackLabels._get_http_options()
            request, metadata = self._interceptor.pre_bulk_upload_feedback_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseBulkUploadFeedbackLabels,
                    "_BaseBulkUploadFeedbackLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.BulkUploadFeedbackLabels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkUploadFeedbackLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._BulkUploadFeedbackLabels._get_response(
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

            resp = self._interceptor.post_bulk_upload_feedback_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_bulk_upload_feedback_labels_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.bulk_upload_feedback_labels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "BulkUploadFeedbackLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CalculateIssueModelStats(
        _BaseContactCenterInsightsRestTransport._BaseCalculateIssueModelStats,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CalculateIssueModelStats")

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
            request: contact_center_insights.CalculateIssueModelStatsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.CalculateIssueModelStatsResponse:
            r"""Call the calculate issue model
            stats method over HTTP.

                Args:
                    request (~.contact_center_insights.CalculateIssueModelStatsRequest):
                        The request object. Request to get statistics of an issue
                    model.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.contact_center_insights.CalculateIssueModelStatsResponse:
                        Response of querying an issue model's
                    statistics.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCalculateIssueModelStats._get_http_options()
            request, metadata = self._interceptor.pre_calculate_issue_model_stats(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCalculateIssueModelStats,
                    "_BaseCalculateIssueModelStats__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CalculateIssueModelStats",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CalculateIssueModelStats",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._CalculateIssueModelStats._get_response(
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
            resp = contact_center_insights.CalculateIssueModelStatsResponse()
            pb_resp = contact_center_insights.CalculateIssueModelStatsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_calculate_issue_model_stats(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_calculate_issue_model_stats_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = contact_center_insights.CalculateIssueModelStatsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.calculate_issue_model_stats",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CalculateIssueModelStats",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CalculateStats(
        _BaseContactCenterInsightsRestTransport._BaseCalculateStats,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CalculateStats")

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
            request: contact_center_insights.CalculateStatsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.CalculateStatsResponse:
            r"""Call the calculate stats method over HTTP.

            Args:
                request (~.contact_center_insights.CalculateStatsRequest):
                    The request object. The request for calculating
                conversation statistics.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.CalculateStatsResponse:
                    The response for calculating
                conversation statistics.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCalculateStats._get_http_options()
            request, metadata = self._interceptor.pre_calculate_stats(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCalculateStats,
                    "_BaseCalculateStats__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CalculateStats",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CalculateStats",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._CalculateStats._get_response(
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
            resp = contact_center_insights.CalculateStatsResponse()
            pb_resp = contact_center_insights.CalculateStatsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_calculate_stats(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_calculate_stats_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.CalculateStatsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.calculate_stats",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CalculateStats",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAnalysis(
        _BaseContactCenterInsightsRestTransport._BaseCreateAnalysis,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateAnalysis")

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
            request: contact_center_insights.CreateAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create analysis method over HTTP.

            Args:
                request (~.contact_center_insights.CreateAnalysisRequest):
                    The request object. The request to create an analysis.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_create_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateAnalysis,
                    "_BaseCreateAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateAnalysis",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._CreateAnalysis._get_response(
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

            resp = self._interceptor.post_create_analysis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_analysis_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_analysis",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateAnalysis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateAnalysisRule(
        _BaseContactCenterInsightsRestTransport._BaseCreateAnalysisRule,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateAnalysisRule")

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
            request: contact_center_insights.CreateAnalysisRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AnalysisRule:
            r"""Call the create analysis rule method over HTTP.

            Args:
                request (~.contact_center_insights.CreateAnalysisRuleRequest):
                    The request object. The request to create a analysis rule. analysis_rule_id
                will be generated by the server.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.AnalysisRule:
                    The CCAI Insights project wide
                analysis rule. This rule will be applied
                to all conversations that match the
                filter defined in the rule. For a
                conversation matches the filter, the
                annotators specified in the rule will be
                run. If a conversation matches multiple
                rules, a union of all the annotators
                will be run. One project can have
                multiple analysis rules.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateAnalysisRule._get_http_options()
            request, metadata = self._interceptor.pre_create_analysis_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateAnalysisRule,
                    "_BaseCreateAnalysisRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateAnalysisRule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateAnalysisRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreateAnalysisRule._get_response(
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
            resp = resources.AnalysisRule()
            pb_resp = resources.AnalysisRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_analysis_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_analysis_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AnalysisRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_analysis_rule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateAnalysisRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateConversation(
        _BaseContactCenterInsightsRestTransport._BaseCreateConversation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateConversation")

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
            request: contact_center_insights.CreateConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Conversation:
            r"""Call the create conversation method over HTTP.

            Args:
                request (~.contact_center_insights.CreateConversationRequest):
                    The request object. Request to create a conversation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Conversation:
                    The conversation resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateConversation._get_http_options()
            request, metadata = self._interceptor.pre_create_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateConversation,
                    "_BaseCreateConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateConversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreateConversation._get_response(
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
            resp = resources.Conversation()
            pb_resp = resources.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_conversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateFeedbackLabel(
        _BaseContactCenterInsightsRestTransport._BaseCreateFeedbackLabel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateFeedbackLabel")

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
            request: contact_center_insights.CreateFeedbackLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.FeedbackLabel:
            r"""Call the create feedback label method over HTTP.

            Args:
                request (~.contact_center_insights.CreateFeedbackLabelRequest):
                    The request object. The request for creating a feedback
                label.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.FeedbackLabel:
                    Represents a conversation, resource,
                and label provided by the user.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateFeedbackLabel._get_http_options()
            request, metadata = self._interceptor.pre_create_feedback_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateFeedbackLabel,
                    "_BaseCreateFeedbackLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateFeedbackLabel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateFeedbackLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreateFeedbackLabel._get_response(
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
            resp = resources.FeedbackLabel()
            pb_resp = resources.FeedbackLabel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_feedback_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_feedback_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.FeedbackLabel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_feedback_label",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateFeedbackLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseCreateIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateIssueModel")

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
            request: contact_center_insights.CreateIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the create issue model method over HTTP.

            Args:
                request (~.contact_center_insights.CreateIssueModelRequest):
                    The request object. The request to create an issue model.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_create_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateIssueModel,
                    "_BaseCreateIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreateIssueModel._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_issue_model_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreatePhraseMatcher(
        _BaseContactCenterInsightsRestTransport._BaseCreatePhraseMatcher,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreatePhraseMatcher")

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
            request: contact_center_insights.CreatePhraseMatcherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.PhraseMatcher:
            r"""Call the create phrase matcher method over HTTP.

            Args:
                request (~.contact_center_insights.CreatePhraseMatcherRequest):
                    The request object. Request to create a phrase matcher.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.PhraseMatcher:
                    The phrase matcher resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreatePhraseMatcher._get_http_options()
            request, metadata = self._interceptor.pre_create_phrase_matcher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreatePhraseMatcher,
                    "_BaseCreatePhraseMatcher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreatePhraseMatcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreatePhraseMatcher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreatePhraseMatcher._get_response(
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
            resp = resources.PhraseMatcher()
            pb_resp = resources.PhraseMatcher.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_phrase_matcher(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_phrase_matcher_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.PhraseMatcher.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_phrase_matcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreatePhraseMatcher",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateQaQuestion(
        _BaseContactCenterInsightsRestTransport._BaseCreateQaQuestion,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateQaQuestion")

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
            request: contact_center_insights.CreateQaQuestionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaQuestion:
            r"""Call the create qa question method over HTTP.

            Args:
                request (~.contact_center_insights.CreateQaQuestionRequest):
                    The request object. The request for creating a
                QaQuestion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaQuestion:
                    A single question to be scored by the
                Insights QA feature.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateQaQuestion._get_http_options()
            request, metadata = self._interceptor.pre_create_qa_question(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateQaQuestion,
                    "_BaseCreateQaQuestion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateQaQuestion",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateQaQuestion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreateQaQuestion._get_response(
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
            resp = resources.QaQuestion()
            pb_resp = resources.QaQuestion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_qa_question(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_qa_question_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaQuestion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_qa_question",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateQaQuestion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateQaScorecard(
        _BaseContactCenterInsightsRestTransport._BaseCreateQaScorecard,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateQaScorecard")

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
            request: contact_center_insights.CreateQaScorecardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecard:
            r"""Call the create qa scorecard method over HTTP.

            Args:
                request (~.contact_center_insights.CreateQaScorecardRequest):
                    The request object. The request for creating a
                QaScorecard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaScorecard:
                    A QaScorecard represents a collection
                of questions to be scored during
                analysis.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateQaScorecard._get_http_options()
            request, metadata = self._interceptor.pre_create_qa_scorecard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateQaScorecard,
                    "_BaseCreateQaScorecard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateQaScorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateQaScorecard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CreateQaScorecard._get_response(
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
            resp = resources.QaScorecard()
            pb_resp = resources.QaScorecard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_qa_scorecard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_qa_scorecard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecard.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_qa_scorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateQaScorecard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateQaScorecardRevision(
        _BaseContactCenterInsightsRestTransport._BaseCreateQaScorecardRevision,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateQaScorecardRevision")

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
            request: contact_center_insights.CreateQaScorecardRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecardRevision:
            r"""Call the create qa scorecard
            revision method over HTTP.

                Args:
                    request (~.contact_center_insights.CreateQaScorecardRevisionRequest):
                        The request object. The request for creating a
                    QaScorecardRevision.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.QaScorecardRevision:
                        A revision of a QaScorecard.

                    Modifying published scorecard fields
                    would invalidate existing scorecard
                    results — the questions may have
                    changed, or the score weighting will
                    make existing scores impossible to
                    understand. So changes must create a new
                    revision, rather than modifying the
                    existing resource.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateQaScorecardRevision._get_http_options()
            request, metadata = self._interceptor.pre_create_qa_scorecard_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateQaScorecardRevision,
                    "_BaseCreateQaScorecardRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateQaScorecardRevision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateQaScorecardRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._CreateQaScorecardRevision._get_response(
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
            resp = resources.QaScorecardRevision()
            pb_resp = resources.QaScorecardRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_qa_scorecard_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_qa_scorecard_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecardRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_qa_scorecard_revision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateQaScorecardRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _CreateView(
        _BaseContactCenterInsightsRestTransport._BaseCreateView,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CreateView")

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
            request: contact_center_insights.CreateViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.View:
            r"""Call the create view method over HTTP.

            Args:
                request (~.contact_center_insights.CreateViewRequest):
                    The request object. The request to create a view.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.View:
                    The View resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseCreateView._get_http_options()
            request, metadata = self._interceptor.pre_create_view(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCreateView,
                    "_BaseCreateView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CreateView",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._CreateView._get_response(
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
            resp = resources.View()
            pb_resp = resources.View.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_create_view(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_create_view_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.View.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.create_view",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CreateView",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeleteAnalysis(
        _BaseContactCenterInsightsRestTransport._BaseDeleteAnalysis,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteAnalysis")

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
            request: contact_center_insights.DeleteAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete analysis method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteAnalysisRequest):
                    The request object. The request to delete an analysis.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_delete_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteAnalysis,
                    "_BaseDeleteAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteAnalysis",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._DeleteAnalysis._get_response(
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

    class _DeleteAnalysisRule(
        _BaseContactCenterInsightsRestTransport._BaseDeleteAnalysisRule,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteAnalysisRule")

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
            request: contact_center_insights.DeleteAnalysisRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete analysis rule method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteAnalysisRuleRequest):
                    The request object. The request to delete a analysis
                rule.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteAnalysisRule._get_http_options()
            request, metadata = self._interceptor.pre_delete_analysis_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteAnalysisRule,
                    "_BaseDeleteAnalysisRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteAnalysisRule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteAnalysisRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeleteAnalysisRule._get_response(
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

    class _DeleteConversation(
        _BaseContactCenterInsightsRestTransport._BaseDeleteConversation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteConversation")

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
            request: contact_center_insights.DeleteConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete conversation method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteConversationRequest):
                    The request object. The request to delete a conversation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteConversation._get_http_options()
            request, metadata = self._interceptor.pre_delete_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteConversation,
                    "_BaseDeleteConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteConversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeleteConversation._get_response(
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

    class _DeleteFeedbackLabel(
        _BaseContactCenterInsightsRestTransport._BaseDeleteFeedbackLabel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteFeedbackLabel")

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
            request: contact_center_insights.DeleteFeedbackLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete feedback label method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteFeedbackLabelRequest):
                    The request object. The request for deleting a feedback
                label.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteFeedbackLabel._get_http_options()
            request, metadata = self._interceptor.pre_delete_feedback_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteFeedbackLabel,
                    "_BaseDeleteFeedbackLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteFeedbackLabel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteFeedbackLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeleteFeedbackLabel._get_response(
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

    class _DeleteIssue(
        _BaseContactCenterInsightsRestTransport._BaseDeleteIssue,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteIssue")

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
            request: contact_center_insights.DeleteIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete issue method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteIssueRequest):
                    The request object. The request to delete an issue.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteIssue._get_http_options()
            request, metadata = self._interceptor.pre_delete_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteIssue,
                    "_BaseDeleteIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteIssue",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._DeleteIssue._get_response(
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

    class _DeleteIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseDeleteIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteIssueModel")

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
            request: contact_center_insights.DeleteIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the delete issue model method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteIssueModelRequest):
                    The request object. The request to delete an issue model.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_delete_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteIssueModel,
                    "_BaseDeleteIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeleteIssueModel._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_delete_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_delete_issue_model_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.delete_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeletePhraseMatcher(
        _BaseContactCenterInsightsRestTransport._BaseDeletePhraseMatcher,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeletePhraseMatcher")

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
            request: contact_center_insights.DeletePhraseMatcherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete phrase matcher method over HTTP.

            Args:
                request (~.contact_center_insights.DeletePhraseMatcherRequest):
                    The request object. The request to delete a phrase
                matcher.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeletePhraseMatcher._get_http_options()
            request, metadata = self._interceptor.pre_delete_phrase_matcher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeletePhraseMatcher,
                    "_BaseDeletePhraseMatcher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeletePhraseMatcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeletePhraseMatcher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeletePhraseMatcher._get_response(
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

    class _DeleteQaQuestion(
        _BaseContactCenterInsightsRestTransport._BaseDeleteQaQuestion,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteQaQuestion")

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
            request: contact_center_insights.DeleteQaQuestionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete qa question method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteQaQuestionRequest):
                    The request object. The request for deleting a
                QaQuestion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteQaQuestion._get_http_options()
            request, metadata = self._interceptor.pre_delete_qa_question(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteQaQuestion,
                    "_BaseDeleteQaQuestion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteQaQuestion",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteQaQuestion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeleteQaQuestion._get_response(
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

    class _DeleteQaScorecard(
        _BaseContactCenterInsightsRestTransport._BaseDeleteQaScorecard,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteQaScorecard")

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
            request: contact_center_insights.DeleteQaScorecardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete qa scorecard method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteQaScorecardRequest):
                    The request object. The request for deleting a
                QaScorecard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteQaScorecard._get_http_options()
            request, metadata = self._interceptor.pre_delete_qa_scorecard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteQaScorecard,
                    "_BaseDeleteQaScorecard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteQaScorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteQaScorecard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeleteQaScorecard._get_response(
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

    class _DeleteQaScorecardRevision(
        _BaseContactCenterInsightsRestTransport._BaseDeleteQaScorecardRevision,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteQaScorecardRevision")

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
            request: contact_center_insights.DeleteQaScorecardRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete qa scorecard
            revision method over HTTP.

                Args:
                    request (~.contact_center_insights.DeleteQaScorecardRevisionRequest):
                        The request object. The request to delete a
                    QaScorecardRevision.
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteQaScorecardRevision._get_http_options()
            request, metadata = self._interceptor.pre_delete_qa_scorecard_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteQaScorecardRevision,
                    "_BaseDeleteQaScorecardRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteQaScorecardRevision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteQaScorecardRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._DeleteQaScorecardRevision._get_response(
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

    class _DeleteView(
        _BaseContactCenterInsightsRestTransport._BaseDeleteView,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeleteView")

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
            request: contact_center_insights.DeleteViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ):
            r"""Call the delete view method over HTTP.

            Args:
                request (~.contact_center_insights.DeleteViewRequest):
                    The request object. The request to delete a view.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeleteView._get_http_options()
            request, metadata = self._interceptor.pre_delete_view(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeleteView,
                    "_BaseDeleteView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeleteView",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeleteView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._DeleteView._get_response(
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

    class _DeployIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseDeployIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeployIssueModel")

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
            request: contact_center_insights.DeployIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the deploy issue model method over HTTP.

            Args:
                request (~.contact_center_insights.DeployIssueModelRequest):
                    The request object. The request to deploy an issue model.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeployIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_deploy_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeployIssueModel,
                    "_BaseDeployIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeployIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeployIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._DeployIssueModel._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_deploy_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_issue_model_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.deploy_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeployIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _DeployQaScorecardRevision(
        _BaseContactCenterInsightsRestTransport._BaseDeployQaScorecardRevision,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.DeployQaScorecardRevision")

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
            request: contact_center_insights.DeployQaScorecardRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecardRevision:
            r"""Call the deploy qa scorecard
            revision method over HTTP.

                Args:
                    request (~.contact_center_insights.DeployQaScorecardRevisionRequest):
                        The request object. The request to deploy a
                    QaScorecardRevision
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.QaScorecardRevision:
                        A revision of a QaScorecard.

                    Modifying published scorecard fields
                    would invalidate existing scorecard
                    results — the questions may have
                    changed, or the score weighting will
                    make existing scores impossible to
                    understand. So changes must create a new
                    revision, rather than modifying the
                    existing resource.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseDeployQaScorecardRevision._get_http_options()
            request, metadata = self._interceptor.pre_deploy_qa_scorecard_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseDeployQaScorecardRevision,
                    "_BaseDeployQaScorecardRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.DeployQaScorecardRevision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeployQaScorecardRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._DeployQaScorecardRevision._get_response(
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
            resp = resources.QaScorecardRevision()
            pb_resp = resources.QaScorecardRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_deploy_qa_scorecard_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_deploy_qa_scorecard_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecardRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.deploy_qa_scorecard_revision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "DeployQaScorecardRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportInsightsData(
        _BaseContactCenterInsightsRestTransport._BaseExportInsightsData,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ExportInsightsData")

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
            request: contact_center_insights.ExportInsightsDataRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export insights data method over HTTP.

            Args:
                request (~.contact_center_insights.ExportInsightsDataRequest):
                    The request object. The request to export insights.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseExportInsightsData._get_http_options()
            request, metadata = self._interceptor.pre_export_insights_data(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseExportInsightsData,
                    "_BaseExportInsightsData__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ExportInsightsData",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ExportInsightsData",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ExportInsightsData._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_insights_data(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_insights_data_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.export_insights_data",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ExportInsightsData",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ExportIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseExportIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ExportIssueModel")

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
            request: contact_center_insights.ExportIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the export issue model method over HTTP.

            Args:
                request (~.contact_center_insights.ExportIssueModelRequest):
                    The request object. Request to export an issue model.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseExportIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_export_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseExportIssueModel,
                    "_BaseExportIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ExportIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ExportIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ExportIssueModel._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_export_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_export_issue_model_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.export_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ExportIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAnalysis(
        _BaseContactCenterInsightsRestTransport._BaseGetAnalysis,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetAnalysis")

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
            request: contact_center_insights.GetAnalysisRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Analysis:
            r"""Call the get analysis method over HTTP.

            Args:
                request (~.contact_center_insights.GetAnalysisRequest):
                    The request object. The request to get an analysis.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Analysis:
                    The analysis resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetAnalysis._get_http_options()
            request, metadata = self._interceptor.pre_get_analysis(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetAnalysis,
                    "_BaseGetAnalysis__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetAnalysis",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetAnalysis",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetAnalysis._get_response(
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
            resp = resources.Analysis()
            pb_resp = resources.Analysis.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_analysis(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_analysis_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Analysis.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_analysis",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetAnalysis",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetAnalysisRule(
        _BaseContactCenterInsightsRestTransport._BaseGetAnalysisRule,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetAnalysisRule")

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
            request: contact_center_insights.GetAnalysisRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AnalysisRule:
            r"""Call the get analysis rule method over HTTP.

            Args:
                request (~.contact_center_insights.GetAnalysisRuleRequest):
                    The request object. The request for getting a analysis
                rule.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.AnalysisRule:
                    The CCAI Insights project wide
                analysis rule. This rule will be applied
                to all conversations that match the
                filter defined in the rule. For a
                conversation matches the filter, the
                annotators specified in the rule will be
                run. If a conversation matches multiple
                rules, a union of all the annotators
                will be run. One project can have
                multiple analysis rules.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetAnalysisRule._get_http_options()
            request, metadata = self._interceptor.pre_get_analysis_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetAnalysisRule,
                    "_BaseGetAnalysisRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetAnalysisRule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetAnalysisRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._GetAnalysisRule._get_response(
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
            resp = resources.AnalysisRule()
            pb_resp = resources.AnalysisRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_analysis_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_analysis_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AnalysisRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_analysis_rule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetAnalysisRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetConversation(
        _BaseContactCenterInsightsRestTransport._BaseGetConversation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetConversation")

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
            request: contact_center_insights.GetConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Conversation:
            r"""Call the get conversation method over HTTP.

            Args:
                request (~.contact_center_insights.GetConversationRequest):
                    The request object. The request to get a conversation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Conversation:
                    The conversation resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetConversation._get_http_options()
            request, metadata = self._interceptor.pre_get_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetConversation,
                    "_BaseGetConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetConversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._GetConversation._get_response(
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
            resp = resources.Conversation()
            pb_resp = resources.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_conversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetEncryptionSpec(
        _BaseContactCenterInsightsRestTransport._BaseGetEncryptionSpec,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetEncryptionSpec")

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
            request: contact_center_insights.GetEncryptionSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.EncryptionSpec:
            r"""Call the get encryption spec method over HTTP.

            Args:
                request (~.contact_center_insights.GetEncryptionSpecRequest):
                    The request object. The request to get location-level
                encryption specification.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.EncryptionSpec:
                    A customer-managed encryption key specification that can
                be applied to all created resources (e.g.
                ``Conversation``).

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetEncryptionSpec._get_http_options()
            request, metadata = self._interceptor.pre_get_encryption_spec(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetEncryptionSpec,
                    "_BaseGetEncryptionSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetEncryptionSpec",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetEncryptionSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._GetEncryptionSpec._get_response(
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
            resp = resources.EncryptionSpec()
            pb_resp = resources.EncryptionSpec.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_encryption_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_encryption_spec_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.EncryptionSpec.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_encryption_spec",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetEncryptionSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetFeedbackLabel(
        _BaseContactCenterInsightsRestTransport._BaseGetFeedbackLabel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetFeedbackLabel")

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
            request: contact_center_insights.GetFeedbackLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.FeedbackLabel:
            r"""Call the get feedback label method over HTTP.

            Args:
                request (~.contact_center_insights.GetFeedbackLabelRequest):
                    The request object. The request for getting a feedback
                label.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.FeedbackLabel:
                    Represents a conversation, resource,
                and label provided by the user.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetFeedbackLabel._get_http_options()
            request, metadata = self._interceptor.pre_get_feedback_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetFeedbackLabel,
                    "_BaseGetFeedbackLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetFeedbackLabel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetFeedbackLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._GetFeedbackLabel._get_response(
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
            resp = resources.FeedbackLabel()
            pb_resp = resources.FeedbackLabel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_feedback_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_feedback_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.FeedbackLabel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_feedback_label",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetFeedbackLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIssue(
        _BaseContactCenterInsightsRestTransport._BaseGetIssue,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetIssue")

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
            request: contact_center_insights.GetIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Issue:
            r"""Call the get issue method over HTTP.

            Args:
                request (~.contact_center_insights.GetIssueRequest):
                    The request object. The request to get an issue.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Issue:
                    The issue resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetIssue._get_http_options()
            request, metadata = self._interceptor.pre_get_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetIssue,
                    "_BaseGetIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetIssue",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetIssue._get_response(
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
            resp = resources.Issue()
            pb_resp = resources.Issue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_issue_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Issue.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_issue",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseGetIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetIssueModel")

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
            request: contact_center_insights.GetIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.IssueModel:
            r"""Call the get issue model method over HTTP.

            Args:
                request (~.contact_center_insights.GetIssueModelRequest):
                    The request object. The request to get an issue model.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.IssueModel:
                    The issue model resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_get_issue_model(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetIssueModel,
                    "_BaseGetIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetIssueModel._get_response(
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
            resp = resources.IssueModel()
            pb_resp = resources.IssueModel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_issue_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.IssueModel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetPhraseMatcher(
        _BaseContactCenterInsightsRestTransport._BaseGetPhraseMatcher,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetPhraseMatcher")

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
            request: contact_center_insights.GetPhraseMatcherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.PhraseMatcher:
            r"""Call the get phrase matcher method over HTTP.

            Args:
                request (~.contact_center_insights.GetPhraseMatcherRequest):
                    The request object. The request to get a a phrase
                matcher.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.PhraseMatcher:
                    The phrase matcher resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetPhraseMatcher._get_http_options()
            request, metadata = self._interceptor.pre_get_phrase_matcher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetPhraseMatcher,
                    "_BaseGetPhraseMatcher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetPhraseMatcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetPhraseMatcher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._GetPhraseMatcher._get_response(
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
            resp = resources.PhraseMatcher()
            pb_resp = resources.PhraseMatcher.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_phrase_matcher(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_phrase_matcher_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.PhraseMatcher.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_phrase_matcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetPhraseMatcher",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetQaQuestion(
        _BaseContactCenterInsightsRestTransport._BaseGetQaQuestion,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetQaQuestion")

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
            request: contact_center_insights.GetQaQuestionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaQuestion:
            r"""Call the get qa question method over HTTP.

            Args:
                request (~.contact_center_insights.GetQaQuestionRequest):
                    The request object. The request for a QaQuestion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaQuestion:
                    A single question to be scored by the
                Insights QA feature.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetQaQuestion._get_http_options()
            request, metadata = self._interceptor.pre_get_qa_question(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetQaQuestion,
                    "_BaseGetQaQuestion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetQaQuestion",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetQaQuestion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetQaQuestion._get_response(
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
            resp = resources.QaQuestion()
            pb_resp = resources.QaQuestion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_qa_question(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_qa_question_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaQuestion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_qa_question",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetQaQuestion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetQaScorecard(
        _BaseContactCenterInsightsRestTransport._BaseGetQaScorecard,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetQaScorecard")

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
            request: contact_center_insights.GetQaScorecardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecard:
            r"""Call the get qa scorecard method over HTTP.

            Args:
                request (~.contact_center_insights.GetQaScorecardRequest):
                    The request object. The request for a QaScorecard. By
                default, returns the latest revision.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaScorecard:
                    A QaScorecard represents a collection
                of questions to be scored during
                analysis.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetQaScorecard._get_http_options()
            request, metadata = self._interceptor.pre_get_qa_scorecard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetQaScorecard,
                    "_BaseGetQaScorecard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetQaScorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetQaScorecard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetQaScorecard._get_response(
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
            resp = resources.QaScorecard()
            pb_resp = resources.QaScorecard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_qa_scorecard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_qa_scorecard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecard.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_qa_scorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetQaScorecard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetQaScorecardRevision(
        _BaseContactCenterInsightsRestTransport._BaseGetQaScorecardRevision,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetQaScorecardRevision")

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
            request: contact_center_insights.GetQaScorecardRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecardRevision:
            r"""Call the get qa scorecard revision method over HTTP.

            Args:
                request (~.contact_center_insights.GetQaScorecardRevisionRequest):
                    The request object. The request for a
                QaScorecardRevision.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaScorecardRevision:
                    A revision of a QaScorecard.

                Modifying published scorecard fields
                would invalidate existing scorecard
                results — the questions may have
                changed, or the score weighting will
                make existing scores impossible to
                understand. So changes must create a new
                revision, rather than modifying the
                existing resource.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetQaScorecardRevision._get_http_options()
            request, metadata = self._interceptor.pre_get_qa_scorecard_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetQaScorecardRevision,
                    "_BaseGetQaScorecardRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetQaScorecardRevision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetQaScorecardRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetQaScorecardRevision._get_response(
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
            resp = resources.QaScorecardRevision()
            pb_resp = resources.QaScorecardRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_qa_scorecard_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_qa_scorecard_revision_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecardRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_qa_scorecard_revision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetQaScorecardRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetSettings(
        _BaseContactCenterInsightsRestTransport._BaseGetSettings,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetSettings")

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
            request: contact_center_insights.GetSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Settings:
            r"""Call the get settings method over HTTP.

            Args:
                request (~.contact_center_insights.GetSettingsRequest):
                    The request object. The request to get project-level
                settings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Settings:
                    The CCAI Insights project wide settings. Use these
                settings to configure the behavior of Insights. View
                these settings with
                ```getsettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/getSettings>`__
                and change the settings with
                ```updateSettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/updateSettings>`__.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetSettings._get_http_options()
            request, metadata = self._interceptor.pre_get_settings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetSettings,
                    "_BaseGetSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetSettings",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetSettings._get_response(
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
            resp = resources.Settings()
            pb_resp = resources.Settings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Settings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_settings",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _GetView(
        _BaseContactCenterInsightsRestTransport._BaseGetView,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetView")

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
            request: contact_center_insights.GetViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.View:
            r"""Call the get view method over HTTP.

            Args:
                request (~.contact_center_insights.GetViewRequest):
                    The request object. The request to get a view.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.View:
                    The View resource.
            """

            http_options = (
                _BaseContactCenterInsightsRestTransport._BaseGetView._get_http_options()
            )
            request, metadata = self._interceptor.pre_get_view(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetView,
                    "_BaseGetView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetView",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetView._get_response(
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
            resp = resources.View()
            pb_resp = resources.View.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_get_view(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_get_view_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.View.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.get_view",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetView",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ImportIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseImportIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ImportIssueModel")

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
            request: contact_center_insights.ImportIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the import issue model method over HTTP.

            Args:
                request (~.contact_center_insights.ImportIssueModelRequest):
                    The request object. Request to import an issue model.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseImportIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_import_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseImportIssueModel,
                    "_BaseImportIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ImportIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ImportIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ImportIssueModel._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_import_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_import_issue_model_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.import_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ImportIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _IngestConversations(
        _BaseContactCenterInsightsRestTransport._BaseIngestConversations,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.IngestConversations")

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
            request: contact_center_insights.IngestConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the ingest conversations method over HTTP.

            Args:
                request (~.contact_center_insights.IngestConversationsRequest):
                    The request object. The request to ingest conversations.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseIngestConversations._get_http_options()
            request, metadata = self._interceptor.pre_ingest_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseIngestConversations,
                    "_BaseIngestConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.IngestConversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "IngestConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._IngestConversations._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_ingest_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_ingest_conversations_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ingest_conversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "IngestConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _InitializeEncryptionSpec(
        _BaseContactCenterInsightsRestTransport._BaseInitializeEncryptionSpec,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.InitializeEncryptionSpec")

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
            request: contact_center_insights.InitializeEncryptionSpecRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the initialize encryption
            spec method over HTTP.

                Args:
                    request (~.contact_center_insights.InitializeEncryptionSpecRequest):
                        The request object. The request to initialize a
                    location-level encryption specification.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseInitializeEncryptionSpec._get_http_options()
            request, metadata = self._interceptor.pre_initialize_encryption_spec(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseInitializeEncryptionSpec,
                    "_BaseInitializeEncryptionSpec__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.InitializeEncryptionSpec",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "InitializeEncryptionSpec",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._InitializeEncryptionSpec._get_response(
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

            resp = self._interceptor.post_initialize_encryption_spec(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_initialize_encryption_spec_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.initialize_encryption_spec",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "InitializeEncryptionSpec",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAllFeedbackLabels(
        _BaseContactCenterInsightsRestTransport._BaseListAllFeedbackLabels,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListAllFeedbackLabels")

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
            request: contact_center_insights.ListAllFeedbackLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListAllFeedbackLabelsResponse:
            r"""Call the list all feedback labels method over HTTP.

            Args:
                request (~.contact_center_insights.ListAllFeedbackLabelsRequest):
                    The request object. The request for listing all feedback
                labels.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListAllFeedbackLabelsResponse:
                    The response for listing all feedback
                labels.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListAllFeedbackLabels._get_http_options()
            request, metadata = self._interceptor.pre_list_all_feedback_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListAllFeedbackLabels,
                    "_BaseListAllFeedbackLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListAllFeedbackLabels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListAllFeedbackLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListAllFeedbackLabels._get_response(
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
            resp = contact_center_insights.ListAllFeedbackLabelsResponse()
            pb_resp = contact_center_insights.ListAllFeedbackLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_all_feedback_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_all_feedback_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListAllFeedbackLabelsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_all_feedback_labels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListAllFeedbackLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAnalyses(
        _BaseContactCenterInsightsRestTransport._BaseListAnalyses,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListAnalyses")

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
            request: contact_center_insights.ListAnalysesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListAnalysesResponse:
            r"""Call the list analyses method over HTTP.

            Args:
                request (~.contact_center_insights.ListAnalysesRequest):
                    The request object. The request to list analyses.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListAnalysesResponse:
                    The response to list analyses.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListAnalyses._get_http_options()
            request, metadata = self._interceptor.pre_list_analyses(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListAnalyses,
                    "_BaseListAnalyses__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListAnalyses",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListAnalyses",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._ListAnalyses._get_response(
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
            resp = contact_center_insights.ListAnalysesResponse()
            pb_resp = contact_center_insights.ListAnalysesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_analyses(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_analyses_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListAnalysesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_analyses",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListAnalyses",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListAnalysisRules(
        _BaseContactCenterInsightsRestTransport._BaseListAnalysisRules,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListAnalysisRules")

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
            request: contact_center_insights.ListAnalysisRulesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListAnalysisRulesResponse:
            r"""Call the list analysis rules method over HTTP.

            Args:
                request (~.contact_center_insights.ListAnalysisRulesRequest):
                    The request object. The request to list analysis rules.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListAnalysisRulesResponse:
                    The response of listing views.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListAnalysisRules._get_http_options()
            request, metadata = self._interceptor.pre_list_analysis_rules(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListAnalysisRules,
                    "_BaseListAnalysisRules__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListAnalysisRules",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListAnalysisRules",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListAnalysisRules._get_response(
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
            resp = contact_center_insights.ListAnalysisRulesResponse()
            pb_resp = contact_center_insights.ListAnalysisRulesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_analysis_rules(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_analysis_rules_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListAnalysisRulesResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_analysis_rules",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListAnalysisRules",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListConversations(
        _BaseContactCenterInsightsRestTransport._BaseListConversations,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListConversations")

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
            request: contact_center_insights.ListConversationsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListConversationsResponse:
            r"""Call the list conversations method over HTTP.

            Args:
                request (~.contact_center_insights.ListConversationsRequest):
                    The request object. Request to list conversations.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListConversationsResponse:
                    The response of listing
                conversations.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListConversations._get_http_options()
            request, metadata = self._interceptor.pre_list_conversations(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListConversations,
                    "_BaseListConversations__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListConversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListConversations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListConversations._get_response(
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
            resp = contact_center_insights.ListConversationsResponse()
            pb_resp = contact_center_insights.ListConversationsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_conversations(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_conversations_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListConversationsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_conversations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListConversations",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListFeedbackLabels(
        _BaseContactCenterInsightsRestTransport._BaseListFeedbackLabels,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListFeedbackLabels")

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
            request: contact_center_insights.ListFeedbackLabelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListFeedbackLabelsResponse:
            r"""Call the list feedback labels method over HTTP.

            Args:
                request (~.contact_center_insights.ListFeedbackLabelsRequest):
                    The request object. The request for listing feedback
                labels.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListFeedbackLabelsResponse:
                    The response for listing feedback
                labels.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListFeedbackLabels._get_http_options()
            request, metadata = self._interceptor.pre_list_feedback_labels(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListFeedbackLabels,
                    "_BaseListFeedbackLabels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListFeedbackLabels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListFeedbackLabels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListFeedbackLabels._get_response(
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
            resp = contact_center_insights.ListFeedbackLabelsResponse()
            pb_resp = contact_center_insights.ListFeedbackLabelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_feedback_labels(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_feedback_labels_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListFeedbackLabelsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_feedback_labels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListFeedbackLabels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIssueModels(
        _BaseContactCenterInsightsRestTransport._BaseListIssueModels,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListIssueModels")

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
            request: contact_center_insights.ListIssueModelsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListIssueModelsResponse:
            r"""Call the list issue models method over HTTP.

            Args:
                request (~.contact_center_insights.ListIssueModelsRequest):
                    The request object. Request to list issue models.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListIssueModelsResponse:
                    The response of listing issue models.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListIssueModels._get_http_options()
            request, metadata = self._interceptor.pre_list_issue_models(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListIssueModels,
                    "_BaseListIssueModels__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListIssueModels",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListIssueModels",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListIssueModels._get_response(
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
            resp = contact_center_insights.ListIssueModelsResponse()
            pb_resp = contact_center_insights.ListIssueModelsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_issue_models(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_issue_models_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListIssueModelsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_issue_models",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListIssueModels",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListIssues(
        _BaseContactCenterInsightsRestTransport._BaseListIssues,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListIssues")

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
            request: contact_center_insights.ListIssuesRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListIssuesResponse:
            r"""Call the list issues method over HTTP.

            Args:
                request (~.contact_center_insights.ListIssuesRequest):
                    The request object. Request to list issues.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListIssuesResponse:
                    The response of listing issues.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListIssues._get_http_options()
            request, metadata = self._interceptor.pre_list_issues(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListIssues,
                    "_BaseListIssues__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListIssues",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListIssues",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._ListIssues._get_response(
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
            resp = contact_center_insights.ListIssuesResponse()
            pb_resp = contact_center_insights.ListIssuesResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_issues(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_issues_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListIssuesResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_issues",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListIssues",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListPhraseMatchers(
        _BaseContactCenterInsightsRestTransport._BaseListPhraseMatchers,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListPhraseMatchers")

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
            request: contact_center_insights.ListPhraseMatchersRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListPhraseMatchersResponse:
            r"""Call the list phrase matchers method over HTTP.

            Args:
                request (~.contact_center_insights.ListPhraseMatchersRequest):
                    The request object. Request to list phrase matchers.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListPhraseMatchersResponse:
                    The response of listing phrase
                matchers.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListPhraseMatchers._get_http_options()
            request, metadata = self._interceptor.pre_list_phrase_matchers(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListPhraseMatchers,
                    "_BaseListPhraseMatchers__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListPhraseMatchers",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListPhraseMatchers",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListPhraseMatchers._get_response(
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
            resp = contact_center_insights.ListPhraseMatchersResponse()
            pb_resp = contact_center_insights.ListPhraseMatchersResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_phrase_matchers(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_phrase_matchers_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListPhraseMatchersResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_phrase_matchers",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListPhraseMatchers",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListQaQuestions(
        _BaseContactCenterInsightsRestTransport._BaseListQaQuestions,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListQaQuestions")

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
            request: contact_center_insights.ListQaQuestionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListQaQuestionsResponse:
            r"""Call the list qa questions method over HTTP.

            Args:
                request (~.contact_center_insights.ListQaQuestionsRequest):
                    The request object. Request to list QaQuestions.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListQaQuestionsResponse:
                    The response from a ListQaQuestions
                request.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListQaQuestions._get_http_options()
            request, metadata = self._interceptor.pre_list_qa_questions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListQaQuestions,
                    "_BaseListQaQuestions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListQaQuestions",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListQaQuestions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListQaQuestions._get_response(
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
            resp = contact_center_insights.ListQaQuestionsResponse()
            pb_resp = contact_center_insights.ListQaQuestionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_qa_questions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_qa_questions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListQaQuestionsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_qa_questions",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListQaQuestions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListQaScorecardRevisions(
        _BaseContactCenterInsightsRestTransport._BaseListQaScorecardRevisions,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListQaScorecardRevisions")

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
            request: contact_center_insights.ListQaScorecardRevisionsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListQaScorecardRevisionsResponse:
            r"""Call the list qa scorecard
            revisions method over HTTP.

                Args:
                    request (~.contact_center_insights.ListQaScorecardRevisionsRequest):
                        The request object. Request to list QaScorecardRevisions
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.contact_center_insights.ListQaScorecardRevisionsResponse:
                        The response from a
                    ListQaScorecardRevisions request.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListQaScorecardRevisions._get_http_options()
            request, metadata = self._interceptor.pre_list_qa_scorecard_revisions(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListQaScorecardRevisions,
                    "_BaseListQaScorecardRevisions__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListQaScorecardRevisions",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListQaScorecardRevisions",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._ListQaScorecardRevisions._get_response(
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
            resp = contact_center_insights.ListQaScorecardRevisionsResponse()
            pb_resp = contact_center_insights.ListQaScorecardRevisionsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_qa_scorecard_revisions(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_qa_scorecard_revisions_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = contact_center_insights.ListQaScorecardRevisionsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_qa_scorecard_revisions",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListQaScorecardRevisions",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListQaScorecards(
        _BaseContactCenterInsightsRestTransport._BaseListQaScorecards,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListQaScorecards")

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
            request: contact_center_insights.ListQaScorecardsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListQaScorecardsResponse:
            r"""Call the list qa scorecards method over HTTP.

            Args:
                request (~.contact_center_insights.ListQaScorecardsRequest):
                    The request object. Request to list QaScorecards.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListQaScorecardsResponse:
                    The response from a ListQaScorecards
                request.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListQaScorecards._get_http_options()
            request, metadata = self._interceptor.pre_list_qa_scorecards(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListQaScorecards,
                    "_BaseListQaScorecards__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListQaScorecards",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListQaScorecards",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._ListQaScorecards._get_response(
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
            resp = contact_center_insights.ListQaScorecardsResponse()
            pb_resp = contact_center_insights.ListQaScorecardsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_qa_scorecards(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_qa_scorecards_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListQaScorecardsResponse.to_json(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_qa_scorecards",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListQaScorecards",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _ListViews(
        _BaseContactCenterInsightsRestTransport._BaseListViews,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListViews")

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
            request: contact_center_insights.ListViewsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> contact_center_insights.ListViewsResponse:
            r"""Call the list views method over HTTP.

            Args:
                request (~.contact_center_insights.ListViewsRequest):
                    The request object. The request to list views.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.contact_center_insights.ListViewsResponse:
                    The response of listing views.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseListViews._get_http_options()
            request, metadata = self._interceptor.pre_list_views(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListViews,
                    "_BaseListViews__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListViews",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListViews",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._ListViews._get_response(
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
            resp = contact_center_insights.ListViewsResponse()
            pb_resp = contact_center_insights.ListViewsResponse.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_list_views(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_list_views_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = (
                        contact_center_insights.ListViewsResponse.to_json(response)
                    )
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.list_views",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListViews",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _QueryMetrics(
        _BaseContactCenterInsightsRestTransport._BaseQueryMetrics,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.QueryMetrics")

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
            request: contact_center_insights.QueryMetricsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the query metrics method over HTTP.

            Args:
                request (~.contact_center_insights.QueryMetricsRequest):
                    The request object. The request for querying metrics.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseQueryMetrics._get_http_options()
            request, metadata = self._interceptor.pre_query_metrics(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseQueryMetrics,
                    "_BaseQueryMetrics__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.QueryMetrics",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "QueryMetrics",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._QueryMetrics._get_response(
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

            resp = self._interceptor.post_query_metrics(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_query_metrics_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.query_metrics",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "QueryMetrics",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _TuneQaScorecardRevision(
        _BaseContactCenterInsightsRestTransport._BaseTuneQaScorecardRevision,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.TuneQaScorecardRevision")

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
            request: contact_center_insights.TuneQaScorecardRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the tune qa scorecard
            revision method over HTTP.

                Args:
                    request (~.contact_center_insights.TuneQaScorecardRevisionRequest):
                        The request object. Request for TuneQaScorecardRevision
                    endpoint.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseTuneQaScorecardRevision._get_http_options()
            request, metadata = self._interceptor.pre_tune_qa_scorecard_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseTuneQaScorecardRevision,
                    "_BaseTuneQaScorecardRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.TuneQaScorecardRevision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "TuneQaScorecardRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._TuneQaScorecardRevision._get_response(
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

            resp = self._interceptor.post_tune_qa_scorecard_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_tune_qa_scorecard_revision_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.tune_qa_scorecard_revision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "TuneQaScorecardRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeployIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseUndeployIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UndeployIssueModel")

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
            request: contact_center_insights.UndeployIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the undeploy issue model method over HTTP.

            Args:
                request (~.contact_center_insights.UndeployIssueModelRequest):
                    The request object. The request to undeploy an issue
                model.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseUndeployIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_undeploy_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUndeployIssueModel,
                    "_BaseUndeployIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UndeployIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UndeployIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UndeployIssueModel._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_undeploy_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_undeploy_issue_model_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.undeploy_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UndeployIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UndeployQaScorecardRevision(
        _BaseContactCenterInsightsRestTransport._BaseUndeployQaScorecardRevision,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash(
                "ContactCenterInsightsRestTransport.UndeployQaScorecardRevision"
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
            request: contact_center_insights.UndeployQaScorecardRevisionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecardRevision:
            r"""Call the undeploy qa scorecard
            revision method over HTTP.

                Args:
                    request (~.contact_center_insights.UndeployQaScorecardRevisionRequest):
                        The request object. The request to undeploy a
                    QaScorecardRevision
                    retry (google.api_core.retry.Retry): Designation of what errors, if any,
                        should be retried.
                    timeout (float): The timeout for this request.
                    metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                        sent along with the request as metadata. Normally, each value must be of type `str`,
                        but for metadata keys ending with the suffix `-bin`, the corresponding values must
                        be of type `bytes`.

                Returns:
                    ~.resources.QaScorecardRevision:
                        A revision of a QaScorecard.

                    Modifying published scorecard fields
                    would invalidate existing scorecard
                    results — the questions may have
                    changed, or the score weighting will
                    make existing scores impossible to
                    understand. So changes must create a new
                    revision, rather than modifying the
                    existing resource.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUndeployQaScorecardRevision._get_http_options()
            request, metadata = self._interceptor.pre_undeploy_qa_scorecard_revision(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUndeployQaScorecardRevision,
                    "_BaseUndeployQaScorecardRevision__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UndeployQaScorecardRevision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UndeployQaScorecardRevision",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._UndeployQaScorecardRevision._get_response(
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
            resp = resources.QaScorecardRevision()
            pb_resp = resources.QaScorecardRevision.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_undeploy_qa_scorecard_revision(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = (
                self._interceptor.post_undeploy_qa_scorecard_revision_with_metadata(
                    resp, response_metadata
                )
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecardRevision.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.undeploy_qa_scorecard_revision",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UndeployQaScorecardRevision",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateAnalysisRule(
        _BaseContactCenterInsightsRestTransport._BaseUpdateAnalysisRule,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateAnalysisRule")

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
            request: contact_center_insights.UpdateAnalysisRuleRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.AnalysisRule:
            r"""Call the update analysis rule method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateAnalysisRuleRequest):
                    The request object. The request to update a analysis
                rule.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.AnalysisRule:
                    The CCAI Insights project wide
                analysis rule. This rule will be applied
                to all conversations that match the
                filter defined in the rule. For a
                conversation matches the filter, the
                annotators specified in the rule will be
                run. If a conversation matches multiple
                rules, a union of all the annotators
                will be run. One project can have
                multiple analysis rules.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateAnalysisRule._get_http_options()
            request, metadata = self._interceptor.pre_update_analysis_rule(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateAnalysisRule,
                    "_BaseUpdateAnalysisRule__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateAnalysisRule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateAnalysisRule",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdateAnalysisRule._get_response(
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
            resp = resources.AnalysisRule()
            pb_resp = resources.AnalysisRule.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_analysis_rule(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_analysis_rule_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.AnalysisRule.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_analysis_rule",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateAnalysisRule",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateConversation(
        _BaseContactCenterInsightsRestTransport._BaseUpdateConversation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateConversation")

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
            request: contact_center_insights.UpdateConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Conversation:
            r"""Call the update conversation method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateConversationRequest):
                    The request object. The request to update a conversation.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Conversation:
                    The conversation resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateConversation._get_http_options()
            request, metadata = self._interceptor.pre_update_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateConversation,
                    "_BaseUpdateConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateConversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdateConversation._get_response(
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
            resp = resources.Conversation()
            pb_resp = resources.Conversation.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_conversation_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Conversation.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_conversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateFeedbackLabel(
        _BaseContactCenterInsightsRestTransport._BaseUpdateFeedbackLabel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateFeedbackLabel")

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
            request: contact_center_insights.UpdateFeedbackLabelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.FeedbackLabel:
            r"""Call the update feedback label method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateFeedbackLabelRequest):
                    The request object. The request for updating a feedback
                label.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.FeedbackLabel:
                    Represents a conversation, resource,
                and label provided by the user.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateFeedbackLabel._get_http_options()
            request, metadata = self._interceptor.pre_update_feedback_label(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateFeedbackLabel,
                    "_BaseUpdateFeedbackLabel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateFeedbackLabel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateFeedbackLabel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdateFeedbackLabel._get_response(
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
            resp = resources.FeedbackLabel()
            pb_resp = resources.FeedbackLabel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_feedback_label(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_feedback_label_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.FeedbackLabel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_feedback_label",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateFeedbackLabel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIssue(
        _BaseContactCenterInsightsRestTransport._BaseUpdateIssue,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateIssue")

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
            request: contact_center_insights.UpdateIssueRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Issue:
            r"""Call the update issue method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateIssueRequest):
                    The request object. The request to update an issue.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Issue:
                    The issue resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateIssue._get_http_options()
            request, metadata = self._interceptor.pre_update_issue(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateIssue,
                    "_BaseUpdateIssue__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateIssue",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateIssue",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._UpdateIssue._get_response(
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
            resp = resources.Issue()
            pb_resp = resources.Issue.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_issue(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_issue_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Issue.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_issue",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateIssue",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateIssueModel(
        _BaseContactCenterInsightsRestTransport._BaseUpdateIssueModel,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateIssueModel")

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
            request: contact_center_insights.UpdateIssueModelRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.IssueModel:
            r"""Call the update issue model method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateIssueModelRequest):
                    The request object. The request to update an issue model.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.IssueModel:
                    The issue model resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateIssueModel._get_http_options()
            request, metadata = self._interceptor.pre_update_issue_model(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateIssueModel,
                    "_BaseUpdateIssueModel__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateIssueModel",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateIssueModel",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdateIssueModel._get_response(
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
            resp = resources.IssueModel()
            pb_resp = resources.IssueModel.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_issue_model(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_issue_model_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.IssueModel.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_issue_model",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateIssueModel",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdatePhraseMatcher(
        _BaseContactCenterInsightsRestTransport._BaseUpdatePhraseMatcher,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdatePhraseMatcher")

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
            request: contact_center_insights.UpdatePhraseMatcherRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.PhraseMatcher:
            r"""Call the update phrase matcher method over HTTP.

            Args:
                request (~.contact_center_insights.UpdatePhraseMatcherRequest):
                    The request object. The request to update a phrase
                matcher.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.PhraseMatcher:
                    The phrase matcher resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdatePhraseMatcher._get_http_options()
            request, metadata = self._interceptor.pre_update_phrase_matcher(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdatePhraseMatcher,
                    "_BaseUpdatePhraseMatcher__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdatePhraseMatcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdatePhraseMatcher",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdatePhraseMatcher._get_response(
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
            resp = resources.PhraseMatcher()
            pb_resp = resources.PhraseMatcher.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_phrase_matcher(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_phrase_matcher_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.PhraseMatcher.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_phrase_matcher",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdatePhraseMatcher",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateQaQuestion(
        _BaseContactCenterInsightsRestTransport._BaseUpdateQaQuestion,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateQaQuestion")

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
            request: contact_center_insights.UpdateQaQuestionRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaQuestion:
            r"""Call the update qa question method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateQaQuestionRequest):
                    The request object. The request for updating a
                QaQuestion.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaQuestion:
                    A single question to be scored by the
                Insights QA feature.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateQaQuestion._get_http_options()
            request, metadata = self._interceptor.pre_update_qa_question(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateQaQuestion,
                    "_BaseUpdateQaQuestion__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateQaQuestion",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateQaQuestion",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdateQaQuestion._get_response(
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
            resp = resources.QaQuestion()
            pb_resp = resources.QaQuestion.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_qa_question(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_qa_question_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaQuestion.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_qa_question",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateQaQuestion",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateQaScorecard(
        _BaseContactCenterInsightsRestTransport._BaseUpdateQaScorecard,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateQaScorecard")

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
            request: contact_center_insights.UpdateQaScorecardRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.QaScorecard:
            r"""Call the update qa scorecard method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateQaScorecardRequest):
                    The request object. The request for updating a
                QaScorecard.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.QaScorecard:
                    A QaScorecard represents a collection
                of questions to be scored during
                analysis.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateQaScorecard._get_http_options()
            request, metadata = self._interceptor.pre_update_qa_scorecard(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateQaScorecard,
                    "_BaseUpdateQaScorecard__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateQaScorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateQaScorecard",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UpdateQaScorecard._get_response(
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
            resp = resources.QaScorecard()
            pb_resp = resources.QaScorecard.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_qa_scorecard(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_qa_scorecard_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.QaScorecard.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_qa_scorecard",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateQaScorecard",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateSettings(
        _BaseContactCenterInsightsRestTransport._BaseUpdateSettings,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateSettings")

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
            request: contact_center_insights.UpdateSettingsRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.Settings:
            r"""Call the update settings method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateSettingsRequest):
                    The request object. The request to update project-level
                settings.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.Settings:
                    The CCAI Insights project wide settings. Use these
                settings to configure the behavior of Insights. View
                these settings with
                ```getsettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/getSettings>`__
                and change the settings with
                ```updateSettings`` <https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/updateSettings>`__.

            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateSettings._get_http_options()
            request, metadata = self._interceptor.pre_update_settings(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateSettings,
                    "_BaseUpdateSettings__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateSettings",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateSettings",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._UpdateSettings._get_response(
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
            resp = resources.Settings()
            pb_resp = resources.Settings.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_settings(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_settings_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.Settings.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_settings",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateSettings",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UpdateView(
        _BaseContactCenterInsightsRestTransport._BaseUpdateView,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UpdateView")

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
            request: contact_center_insights.UpdateViewRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> resources.View:
            r"""Call the update view method over HTTP.

            Args:
                request (~.contact_center_insights.UpdateViewRequest):
                    The request object. The request to update a view.
                retry (google.api_core.retry.Retry): Designation of what errors, if any,
                    should be retried.
                timeout (float): The timeout for this request.
                metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                    sent along with the request as metadata. Normally, each value must be of type `str`,
                    but for metadata keys ending with the suffix `-bin`, the corresponding values must
                    be of type `bytes`.

            Returns:
                ~.resources.View:
                    The View resource.
            """

            http_options = _BaseContactCenterInsightsRestTransport._BaseUpdateView._get_http_options()
            request, metadata = self._interceptor.pre_update_view(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUpdateView,
                    "_BaseUpdateView__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UpdateView",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateView",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._UpdateView._get_response(
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
            resp = resources.View()
            pb_resp = resources.View.pb(resp)

            json_format.Parse(response.content, pb_resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_update_view(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_update_view_with_metadata(
                resp, response_metadata
            )
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                logging.DEBUG
            ):  # pragma: NO COVER
                try:
                    response_payload = resources.View.to_json(response)
                except:
                    response_payload = None
                http_response = {
                    "payload": response_payload,
                    "headers": dict(response.headers),
                    "status": response.status_code,
                }
                _LOGGER.debug(
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.update_view",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UpdateView",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    class _UploadConversation(
        _BaseContactCenterInsightsRestTransport._BaseUploadConversation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.UploadConversation")

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
            request: contact_center_insights.UploadConversationRequest,
            *,
            retry: OptionalRetry = gapic_v1.method.DEFAULT,
            timeout: Optional[float] = None,
            metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
        ) -> operations_pb2.Operation:
            r"""Call the upload conversation method over HTTP.

            Args:
                request (~.contact_center_insights.UploadConversationRequest):
                    The request object. Request to upload a conversation.
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

            http_options = _BaseContactCenterInsightsRestTransport._BaseUploadConversation._get_http_options()
            request, metadata = self._interceptor.pre_upload_conversation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseUploadConversation,
                    "_BaseUploadConversation__REQUIRED_FIELDS_DEFAULT_VALUES",
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.UploadConversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UploadConversation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._UploadConversation._get_response(
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
            resp = operations_pb2.Operation()
            json_format.Parse(response.content, resp, ignore_unknown_fields=True)

            resp = self._interceptor.post_upload_conversation(resp)
            response_metadata = [(k, str(v)) for k, v in response.headers.items()]
            resp, _ = self._interceptor.post_upload_conversation_with_metadata(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.upload_conversation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "UploadConversation",
                        "metadata": http_response["headers"],
                        "httpResponse": http_response,
                    },
                )
            return resp

    @property
    def bulk_analyze_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.BulkAnalyzeConversationsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkAnalyzeConversations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def bulk_delete_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.BulkDeleteConversationsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkDeleteConversations(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def bulk_download_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.BulkDownloadFeedbackLabelsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkDownloadFeedbackLabels(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def bulk_upload_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.BulkUploadFeedbackLabelsRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._BulkUploadFeedbackLabels(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def calculate_issue_model_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateIssueModelStatsRequest],
        contact_center_insights.CalculateIssueModelStatsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CalculateIssueModelStats(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def calculate_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateStatsRequest],
        contact_center_insights.CalculateStatsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CalculateStats(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_analysis(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRuleRequest], resources.AnalysisRule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateAnalysisRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.CreateConversationRequest], resources.Conversation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.CreateFeedbackLabelRequest], resources.FeedbackLabel
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateFeedbackLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.CreateIssueModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.CreatePhraseMatcherRequest], resources.PhraseMatcher
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreatePhraseMatcher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaQuestionRequest], resources.QaQuestion
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateQaQuestion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaScorecardRequest], resources.QaScorecard
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateQaScorecard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def create_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateQaScorecardRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def create_view(
        self,
    ) -> Callable[[contact_center_insights.CreateViewRequest], resources.View]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._CreateView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_analysis(
        self,
    ) -> Callable[[contact_center_insights.DeleteAnalysisRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_analysis_rule(
        self,
    ) -> Callable[[contact_center_insights.DeleteAnalysisRuleRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteAnalysisRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_conversation(
        self,
    ) -> Callable[[contact_center_insights.DeleteConversationRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteFeedbackLabelRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteFeedbackLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_issue(
        self,
    ) -> Callable[[contact_center_insights.DeleteIssueRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteIssueModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.DeletePhraseMatcherRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeletePhraseMatcher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_qa_question(
        self,
    ) -> Callable[[contact_center_insights.DeleteQaQuestionRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteQaQuestion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_qa_scorecard(
        self,
    ) -> Callable[[contact_center_insights.DeleteQaScorecardRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteQaScorecard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def delete_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteQaScorecardRevisionRequest], empty_pb2.Empty
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteQaScorecardRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def delete_view(
        self,
    ) -> Callable[[contact_center_insights.DeleteViewRequest], empty_pb2.Empty]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeleteView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeployIssueModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def deploy_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.DeployQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._DeployQaScorecardRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def export_insights_data(
        self,
    ) -> Callable[
        [contact_center_insights.ExportInsightsDataRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportInsightsData(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def export_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.ExportIssueModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ExportIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_analysis(
        self,
    ) -> Callable[[contact_center_insights.GetAnalysisRequest], resources.Analysis]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAnalysis(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.GetAnalysisRuleRequest], resources.AnalysisRule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetAnalysisRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.GetConversationRequest], resources.Conversation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_encryption_spec(
        self,
    ) -> Callable[
        [contact_center_insights.GetEncryptionSpecRequest], resources.EncryptionSpec
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetEncryptionSpec(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.GetFeedbackLabelRequest], resources.FeedbackLabel
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetFeedbackLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_issue(
        self,
    ) -> Callable[[contact_center_insights.GetIssueRequest], resources.Issue]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_issue_model(
        self,
    ) -> Callable[[contact_center_insights.GetIssueModelRequest], resources.IssueModel]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.GetPhraseMatcherRequest], resources.PhraseMatcher
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetPhraseMatcher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_qa_question(
        self,
    ) -> Callable[[contact_center_insights.GetQaQuestionRequest], resources.QaQuestion]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetQaQuestion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaScorecardRequest], resources.QaScorecard
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetQaScorecard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetQaScorecardRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def get_settings(
        self,
    ) -> Callable[[contact_center_insights.GetSettingsRequest], resources.Settings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def get_view(
        self,
    ) -> Callable[[contact_center_insights.GetViewRequest], resources.View]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._GetView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def import_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.ImportIssueModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ImportIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def ingest_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.IngestConversationsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._IngestConversations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def initialize_encryption_spec(
        self,
    ) -> Callable[
        [contact_center_insights.InitializeEncryptionSpecRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._InitializeEncryptionSpec(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_all_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.ListAllFeedbackLabelsRequest],
        contact_center_insights.ListAllFeedbackLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAllFeedbackLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_analyses(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysesRequest],
        contact_center_insights.ListAnalysesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAnalyses(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_analysis_rules(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysisRulesRequest],
        contact_center_insights.ListAnalysisRulesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListAnalysisRules(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.ListConversationsRequest],
        contact_center_insights.ListConversationsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListConversations(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.ListFeedbackLabelsRequest],
        contact_center_insights.ListFeedbackLabelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListFeedbackLabels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_issue_models(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssueModelsRequest],
        contact_center_insights.ListIssueModelsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIssueModels(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_issues(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssuesRequest],
        contact_center_insights.ListIssuesResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListIssues(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_phrase_matchers(
        self,
    ) -> Callable[
        [contact_center_insights.ListPhraseMatchersRequest],
        contact_center_insights.ListPhraseMatchersResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListPhraseMatchers(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_qa_questions(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaQuestionsRequest],
        contact_center_insights.ListQaQuestionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListQaQuestions(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_qa_scorecard_revisions(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaScorecardRevisionsRequest],
        contact_center_insights.ListQaScorecardRevisionsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListQaScorecardRevisions(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def list_qa_scorecards(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaScorecardsRequest],
        contact_center_insights.ListQaScorecardsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListQaScorecards(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def list_views(
        self,
    ) -> Callable[
        [contact_center_insights.ListViewsRequest],
        contact_center_insights.ListViewsResponse,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._ListViews(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def query_metrics(
        self,
    ) -> Callable[
        [contact_center_insights.QueryMetricsRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._QueryMetrics(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def tune_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.TuneQaScorecardRevisionRequest],
        operations_pb2.Operation,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._TuneQaScorecardRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def undeploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployIssueModelRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeployIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def undeploy_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployQaScorecardRevisionRequest],
        resources.QaScorecardRevision,
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UndeployQaScorecardRevision(
            self._session, self._host, self._interceptor
        )  # type: ignore

    @property
    def update_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateAnalysisRuleRequest], resources.AnalysisRule
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateAnalysisRule(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateConversationRequest], resources.Conversation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateFeedbackLabelRequest], resources.FeedbackLabel
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateFeedbackLabel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_issue(
        self,
    ) -> Callable[[contact_center_insights.UpdateIssueRequest], resources.Issue]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIssue(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateIssueModelRequest], resources.IssueModel
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateIssueModel(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.UpdatePhraseMatcherRequest], resources.PhraseMatcher
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdatePhraseMatcher(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateQaQuestionRequest], resources.QaQuestion
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateQaQuestion(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateQaScorecardRequest], resources.QaScorecard
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateQaScorecard(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_settings(
        self,
    ) -> Callable[[contact_center_insights.UpdateSettingsRequest], resources.Settings]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateSettings(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def update_view(
        self,
    ) -> Callable[[contact_center_insights.UpdateViewRequest], resources.View]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UpdateView(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def upload_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UploadConversationRequest], operations_pb2.Operation
    ]:
        # The return type is fine, but mypy isn't sophisticated enough to determine what's going on here.
        # In C++ this would require a dynamic_cast
        return self._UploadConversation(self._session, self._host, self._interceptor)  # type: ignore

    @property
    def cancel_operation(self):
        return self._CancelOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _CancelOperation(
        _BaseContactCenterInsightsRestTransport._BaseCancelOperation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.CancelOperation")

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

            http_options = _BaseContactCenterInsightsRestTransport._BaseCancelOperation._get_http_options()
            request, metadata = self._interceptor.pre_cancel_operation(
                request, metadata
            )
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseCancelOperation,
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.CancelOperation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "CancelOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = (
                ContactCenterInsightsRestTransport._CancelOperation._get_response(
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

            return self._interceptor.post_cancel_operation(None)

    @property
    def get_operation(self):
        return self._GetOperation(self._session, self._host, self._interceptor)  # type: ignore

    class _GetOperation(
        _BaseContactCenterInsightsRestTransport._BaseGetOperation,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.GetOperation")

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

            http_options = _BaseContactCenterInsightsRestTransport._BaseGetOperation._get_http_options()
            request, metadata = self._interceptor.pre_get_operation(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseGetOperation,
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "GetOperation",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._GetOperation._get_response(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsAsyncClient.GetOperation",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
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
        _BaseContactCenterInsightsRestTransport._BaseListOperations,
        ContactCenterInsightsRestStub,
    ):
        def __hash__(self):
            return hash("ContactCenterInsightsRestTransport.ListOperations")

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

            http_options = _BaseContactCenterInsightsRestTransport._BaseListOperations._get_http_options()
            request, metadata = self._interceptor.pre_list_operations(request, metadata)
            transcoded_request, body, query_params = transcode_request(
                http_options,
                request,
                required_fields_default_values=getattr(
                    _BaseContactCenterInsightsRestTransport._BaseListOperations,
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
                    f"Sending request for google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "rpcName": "ListOperations",
                        "httpRequest": http_request,
                        "metadata": http_request["headers"],
                    },
                )

            # Send the request
            response = ContactCenterInsightsRestTransport._ListOperations._get_response(
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
                    "Received response for google.cloud.contactcenterinsights_v1.ContactCenterInsightsAsyncClient.ListOperations",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
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


__all__ = ("ContactCenterInsightsRestTransport",)
