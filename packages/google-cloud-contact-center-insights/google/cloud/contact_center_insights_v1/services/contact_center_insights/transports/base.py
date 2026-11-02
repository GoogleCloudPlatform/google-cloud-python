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
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.contact_center_insights_v1 import gapic_version as package_version
from google.cloud.contact_center_insights_v1.types import (
    contact_center_insights,
    resources,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class ContactCenterInsightsTransport(abc.ABC):
    """Abstract transport class for ContactCenterInsights."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "contactcenterinsights.googleapis.com"

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
                 The hostname to connect to (default: 'contactcenterinsights.googleapis.com').
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
            self.create_conversation: gapic_v1.method.wrap_method(
                self.create_conversation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.upload_conversation: gapic_v1.method.wrap_method(
                self.upload_conversation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_conversation: gapic_v1.method.wrap_method(
                self.update_conversation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_conversation: gapic_v1.method.wrap_method(
                self.get_conversation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_conversations: gapic_v1.method.wrap_method(
                self.list_conversations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_conversation: gapic_v1.method.wrap_method(
                self.delete_conversation,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_analysis: gapic_v1.method.wrap_method(
                self.create_analysis,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_analysis: gapic_v1.method.wrap_method(
                self.get_analysis,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_analyses: gapic_v1.method.wrap_method(
                self.list_analyses,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_analysis: gapic_v1.method.wrap_method(
                self.delete_analysis,
                default_timeout=None,
                client_info=client_info,
            ),
            self.bulk_analyze_conversations: gapic_v1.method.wrap_method(
                self.bulk_analyze_conversations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.bulk_delete_conversations: gapic_v1.method.wrap_method(
                self.bulk_delete_conversations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.ingest_conversations: gapic_v1.method.wrap_method(
                self.ingest_conversations,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export_insights_data: gapic_v1.method.wrap_method(
                self.export_insights_data,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_issue_model: gapic_v1.method.wrap_method(
                self.create_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_issue_model: gapic_v1.method.wrap_method(
                self.update_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_issue_model: gapic_v1.method.wrap_method(
                self.get_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_issue_models: gapic_v1.method.wrap_method(
                self.list_issue_models,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_issue_model: gapic_v1.method.wrap_method(
                self.delete_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.deploy_issue_model: gapic_v1.method.wrap_method(
                self.deploy_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undeploy_issue_model: gapic_v1.method.wrap_method(
                self.undeploy_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.export_issue_model: gapic_v1.method.wrap_method(
                self.export_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.import_issue_model: gapic_v1.method.wrap_method(
                self.import_issue_model,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_issue: gapic_v1.method.wrap_method(
                self.get_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_issues: gapic_v1.method.wrap_method(
                self.list_issues,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_issue: gapic_v1.method.wrap_method(
                self.update_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_issue: gapic_v1.method.wrap_method(
                self.delete_issue,
                default_timeout=None,
                client_info=client_info,
            ),
            self.calculate_issue_model_stats: gapic_v1.method.wrap_method(
                self.calculate_issue_model_stats,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_phrase_matcher: gapic_v1.method.wrap_method(
                self.create_phrase_matcher,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_phrase_matcher: gapic_v1.method.wrap_method(
                self.get_phrase_matcher,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_phrase_matchers: gapic_v1.method.wrap_method(
                self.list_phrase_matchers,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_phrase_matcher: gapic_v1.method.wrap_method(
                self.delete_phrase_matcher,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_phrase_matcher: gapic_v1.method.wrap_method(
                self.update_phrase_matcher,
                default_timeout=None,
                client_info=client_info,
            ),
            self.calculate_stats: gapic_v1.method.wrap_method(
                self.calculate_stats,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_settings: gapic_v1.method.wrap_method(
                self.get_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_settings: gapic_v1.method.wrap_method(
                self.update_settings,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_analysis_rule: gapic_v1.method.wrap_method(
                self.create_analysis_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_analysis_rule: gapic_v1.method.wrap_method(
                self.get_analysis_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_analysis_rules: gapic_v1.method.wrap_method(
                self.list_analysis_rules,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_analysis_rule: gapic_v1.method.wrap_method(
                self.update_analysis_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_analysis_rule: gapic_v1.method.wrap_method(
                self.delete_analysis_rule,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_encryption_spec: gapic_v1.method.wrap_method(
                self.get_encryption_spec,
                default_timeout=None,
                client_info=client_info,
            ),
            self.initialize_encryption_spec: gapic_v1.method.wrap_method(
                self.initialize_encryption_spec,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_view: gapic_v1.method.wrap_method(
                self.create_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_view: gapic_v1.method.wrap_method(
                self.get_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_views: gapic_v1.method.wrap_method(
                self.list_views,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_view: gapic_v1.method.wrap_method(
                self.update_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_view: gapic_v1.method.wrap_method(
                self.delete_view,
                default_timeout=None,
                client_info=client_info,
            ),
            self.query_metrics: gapic_v1.method.wrap_method(
                self.query_metrics,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_qa_question: gapic_v1.method.wrap_method(
                self.create_qa_question,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_qa_question: gapic_v1.method.wrap_method(
                self.get_qa_question,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_qa_question: gapic_v1.method.wrap_method(
                self.update_qa_question,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_qa_question: gapic_v1.method.wrap_method(
                self.delete_qa_question,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_qa_questions: gapic_v1.method.wrap_method(
                self.list_qa_questions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_qa_scorecard: gapic_v1.method.wrap_method(
                self.create_qa_scorecard,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_qa_scorecard: gapic_v1.method.wrap_method(
                self.get_qa_scorecard,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_qa_scorecard: gapic_v1.method.wrap_method(
                self.update_qa_scorecard,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_qa_scorecard: gapic_v1.method.wrap_method(
                self.delete_qa_scorecard,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_qa_scorecards: gapic_v1.method.wrap_method(
                self.list_qa_scorecards,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_qa_scorecard_revision: gapic_v1.method.wrap_method(
                self.create_qa_scorecard_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_qa_scorecard_revision: gapic_v1.method.wrap_method(
                self.get_qa_scorecard_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.tune_qa_scorecard_revision: gapic_v1.method.wrap_method(
                self.tune_qa_scorecard_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.deploy_qa_scorecard_revision: gapic_v1.method.wrap_method(
                self.deploy_qa_scorecard_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.undeploy_qa_scorecard_revision: gapic_v1.method.wrap_method(
                self.undeploy_qa_scorecard_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_qa_scorecard_revision: gapic_v1.method.wrap_method(
                self.delete_qa_scorecard_revision,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_qa_scorecard_revisions: gapic_v1.method.wrap_method(
                self.list_qa_scorecard_revisions,
                default_timeout=None,
                client_info=client_info,
            ),
            self.create_feedback_label: gapic_v1.method.wrap_method(
                self.create_feedback_label,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_feedback_labels: gapic_v1.method.wrap_method(
                self.list_feedback_labels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.get_feedback_label: gapic_v1.method.wrap_method(
                self.get_feedback_label,
                default_timeout=None,
                client_info=client_info,
            ),
            self.update_feedback_label: gapic_v1.method.wrap_method(
                self.update_feedback_label,
                default_timeout=None,
                client_info=client_info,
            ),
            self.delete_feedback_label: gapic_v1.method.wrap_method(
                self.delete_feedback_label,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_all_feedback_labels: gapic_v1.method.wrap_method(
                self.list_all_feedback_labels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.bulk_upload_feedback_labels: gapic_v1.method.wrap_method(
                self.bulk_upload_feedback_labels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.bulk_download_feedback_labels: gapic_v1.method.wrap_method(
                self.bulk_download_feedback_labels,
                default_timeout=None,
                client_info=client_info,
            ),
            self.cancel_operation: gapic_v1.method.wrap_method(
                self.cancel_operation,
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
    def create_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.CreateConversationRequest],
        Union[resources.Conversation, Awaitable[resources.Conversation]],
    ]:
        raise NotImplementedError()

    @property
    def upload_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UploadConversationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateConversationRequest],
        Union[resources.Conversation, Awaitable[resources.Conversation]],
    ]:
        raise NotImplementedError()

    @property
    def get_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.GetConversationRequest],
        Union[resources.Conversation, Awaitable[resources.Conversation]],
    ]:
        raise NotImplementedError()

    @property
    def list_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.ListConversationsRequest],
        Union[
            contact_center_insights.ListConversationsResponse,
            Awaitable[contact_center_insights.ListConversationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_conversation(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteConversationRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_analysis(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_analysis(
        self,
    ) -> Callable[
        [contact_center_insights.GetAnalysisRequest],
        Union[resources.Analysis, Awaitable[resources.Analysis]],
    ]:
        raise NotImplementedError()

    @property
    def list_analyses(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysesRequest],
        Union[
            contact_center_insights.ListAnalysesResponse,
            Awaitable[contact_center_insights.ListAnalysesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_analysis(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteAnalysisRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def bulk_analyze_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.BulkAnalyzeConversationsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def bulk_delete_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.BulkDeleteConversationsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def ingest_conversations(
        self,
    ) -> Callable[
        [contact_center_insights.IngestConversationsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_insights_data(
        self,
    ) -> Callable[
        [contact_center_insights.ExportInsightsDataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.CreateIssueModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateIssueModelRequest],
        Union[resources.IssueModel, Awaitable[resources.IssueModel]],
    ]:
        raise NotImplementedError()

    @property
    def get_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.GetIssueModelRequest],
        Union[resources.IssueModel, Awaitable[resources.IssueModel]],
    ]:
        raise NotImplementedError()

    @property
    def list_issue_models(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssueModelsRequest],
        Union[
            contact_center_insights.ListIssueModelsResponse,
            Awaitable[contact_center_insights.ListIssueModelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteIssueModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def deploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.DeployIssueModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def undeploy_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployIssueModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.ExportIssueModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def import_issue_model(
        self,
    ) -> Callable[
        [contact_center_insights.ImportIssueModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_issue(
        self,
    ) -> Callable[
        [contact_center_insights.GetIssueRequest],
        Union[resources.Issue, Awaitable[resources.Issue]],
    ]:
        raise NotImplementedError()

    @property
    def list_issues(
        self,
    ) -> Callable[
        [contact_center_insights.ListIssuesRequest],
        Union[
            contact_center_insights.ListIssuesResponse,
            Awaitable[contact_center_insights.ListIssuesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_issue(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateIssueRequest],
        Union[resources.Issue, Awaitable[resources.Issue]],
    ]:
        raise NotImplementedError()

    @property
    def delete_issue(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteIssueRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def calculate_issue_model_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateIssueModelStatsRequest],
        Union[
            contact_center_insights.CalculateIssueModelStatsResponse,
            Awaitable[contact_center_insights.CalculateIssueModelStatsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.CreatePhraseMatcherRequest],
        Union[resources.PhraseMatcher, Awaitable[resources.PhraseMatcher]],
    ]:
        raise NotImplementedError()

    @property
    def get_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.GetPhraseMatcherRequest],
        Union[resources.PhraseMatcher, Awaitable[resources.PhraseMatcher]],
    ]:
        raise NotImplementedError()

    @property
    def list_phrase_matchers(
        self,
    ) -> Callable[
        [contact_center_insights.ListPhraseMatchersRequest],
        Union[
            contact_center_insights.ListPhraseMatchersResponse,
            Awaitable[contact_center_insights.ListPhraseMatchersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.DeletePhraseMatcherRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def update_phrase_matcher(
        self,
    ) -> Callable[
        [contact_center_insights.UpdatePhraseMatcherRequest],
        Union[resources.PhraseMatcher, Awaitable[resources.PhraseMatcher]],
    ]:
        raise NotImplementedError()

    @property
    def calculate_stats(
        self,
    ) -> Callable[
        [contact_center_insights.CalculateStatsRequest],
        Union[
            contact_center_insights.CalculateStatsResponse,
            Awaitable[contact_center_insights.CalculateStatsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_settings(
        self,
    ) -> Callable[
        [contact_center_insights.GetSettingsRequest],
        Union[resources.Settings, Awaitable[resources.Settings]],
    ]:
        raise NotImplementedError()

    @property
    def update_settings(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateSettingsRequest],
        Union[resources.Settings, Awaitable[resources.Settings]],
    ]:
        raise NotImplementedError()

    @property
    def create_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.CreateAnalysisRuleRequest],
        Union[resources.AnalysisRule, Awaitable[resources.AnalysisRule]],
    ]:
        raise NotImplementedError()

    @property
    def get_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.GetAnalysisRuleRequest],
        Union[resources.AnalysisRule, Awaitable[resources.AnalysisRule]],
    ]:
        raise NotImplementedError()

    @property
    def list_analysis_rules(
        self,
    ) -> Callable[
        [contact_center_insights.ListAnalysisRulesRequest],
        Union[
            contact_center_insights.ListAnalysisRulesResponse,
            Awaitable[contact_center_insights.ListAnalysisRulesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateAnalysisRuleRequest],
        Union[resources.AnalysisRule, Awaitable[resources.AnalysisRule]],
    ]:
        raise NotImplementedError()

    @property
    def delete_analysis_rule(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteAnalysisRuleRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_encryption_spec(
        self,
    ) -> Callable[
        [contact_center_insights.GetEncryptionSpecRequest],
        Union[resources.EncryptionSpec, Awaitable[resources.EncryptionSpec]],
    ]:
        raise NotImplementedError()

    @property
    def initialize_encryption_spec(
        self,
    ) -> Callable[
        [contact_center_insights.InitializeEncryptionSpecRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_view(
        self,
    ) -> Callable[
        [contact_center_insights.CreateViewRequest],
        Union[resources.View, Awaitable[resources.View]],
    ]:
        raise NotImplementedError()

    @property
    def get_view(
        self,
    ) -> Callable[
        [contact_center_insights.GetViewRequest],
        Union[resources.View, Awaitable[resources.View]],
    ]:
        raise NotImplementedError()

    @property
    def list_views(
        self,
    ) -> Callable[
        [contact_center_insights.ListViewsRequest],
        Union[
            contact_center_insights.ListViewsResponse,
            Awaitable[contact_center_insights.ListViewsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_view(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateViewRequest],
        Union[resources.View, Awaitable[resources.View]],
    ]:
        raise NotImplementedError()

    @property
    def delete_view(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteViewRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def query_metrics(
        self,
    ) -> Callable[
        [contact_center_insights.QueryMetricsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaQuestionRequest],
        Union[resources.QaQuestion, Awaitable[resources.QaQuestion]],
    ]:
        raise NotImplementedError()

    @property
    def get_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaQuestionRequest],
        Union[resources.QaQuestion, Awaitable[resources.QaQuestion]],
    ]:
        raise NotImplementedError()

    @property
    def update_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateQaQuestionRequest],
        Union[resources.QaQuestion, Awaitable[resources.QaQuestion]],
    ]:
        raise NotImplementedError()

    @property
    def delete_qa_question(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteQaQuestionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_qa_questions(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaQuestionsRequest],
        Union[
            contact_center_insights.ListQaQuestionsResponse,
            Awaitable[contact_center_insights.ListQaQuestionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaScorecardRequest],
        Union[resources.QaScorecard, Awaitable[resources.QaScorecard]],
    ]:
        raise NotImplementedError()

    @property
    def get_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaScorecardRequest],
        Union[resources.QaScorecard, Awaitable[resources.QaScorecard]],
    ]:
        raise NotImplementedError()

    @property
    def update_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateQaScorecardRequest],
        Union[resources.QaScorecard, Awaitable[resources.QaScorecard]],
    ]:
        raise NotImplementedError()

    @property
    def delete_qa_scorecard(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteQaScorecardRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_qa_scorecards(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaScorecardsRequest],
        Union[
            contact_center_insights.ListQaScorecardsResponse,
            Awaitable[contact_center_insights.ListQaScorecardsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.CreateQaScorecardRevisionRequest],
        Union[resources.QaScorecardRevision, Awaitable[resources.QaScorecardRevision]],
    ]:
        raise NotImplementedError()

    @property
    def get_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.GetQaScorecardRevisionRequest],
        Union[resources.QaScorecardRevision, Awaitable[resources.QaScorecardRevision]],
    ]:
        raise NotImplementedError()

    @property
    def tune_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.TuneQaScorecardRevisionRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def deploy_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.DeployQaScorecardRevisionRequest],
        Union[resources.QaScorecardRevision, Awaitable[resources.QaScorecardRevision]],
    ]:
        raise NotImplementedError()

    @property
    def undeploy_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.UndeployQaScorecardRevisionRequest],
        Union[resources.QaScorecardRevision, Awaitable[resources.QaScorecardRevision]],
    ]:
        raise NotImplementedError()

    @property
    def delete_qa_scorecard_revision(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteQaScorecardRevisionRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_qa_scorecard_revisions(
        self,
    ) -> Callable[
        [contact_center_insights.ListQaScorecardRevisionsRequest],
        Union[
            contact_center_insights.ListQaScorecardRevisionsResponse,
            Awaitable[contact_center_insights.ListQaScorecardRevisionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.CreateFeedbackLabelRequest],
        Union[resources.FeedbackLabel, Awaitable[resources.FeedbackLabel]],
    ]:
        raise NotImplementedError()

    @property
    def list_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.ListFeedbackLabelsRequest],
        Union[
            contact_center_insights.ListFeedbackLabelsResponse,
            Awaitable[contact_center_insights.ListFeedbackLabelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.GetFeedbackLabelRequest],
        Union[resources.FeedbackLabel, Awaitable[resources.FeedbackLabel]],
    ]:
        raise NotImplementedError()

    @property
    def update_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.UpdateFeedbackLabelRequest],
        Union[resources.FeedbackLabel, Awaitable[resources.FeedbackLabel]],
    ]:
        raise NotImplementedError()

    @property
    def delete_feedback_label(
        self,
    ) -> Callable[
        [contact_center_insights.DeleteFeedbackLabelRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def list_all_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.ListAllFeedbackLabelsRequest],
        Union[
            contact_center_insights.ListAllFeedbackLabelsResponse,
            Awaitable[contact_center_insights.ListAllFeedbackLabelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def bulk_upload_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.BulkUploadFeedbackLabelsRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def bulk_download_feedback_labels(
        self,
    ) -> Callable[
        [contact_center_insights.BulkDownloadFeedbackLabelsRequest],
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
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("ContactCenterInsightsTransport",)
