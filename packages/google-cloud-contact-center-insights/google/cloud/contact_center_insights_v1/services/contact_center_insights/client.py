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
import json
import logging as std_logging
import os
import re
import warnings
from collections import OrderedDict
from http import HTTPStatus
from typing import (
    Callable,
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

import google.protobuf
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.exceptions import MutualTLSChannelError  # type: ignore
from google.auth.transport import mtls  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.contact_center_insights_v1 import gapic_version as package_version
from google.cloud.contact_center_insights_v1._compat import (
    get_api_endpoint,
    get_default_mtls_endpoint,
    get_universe_domain,
    read_environment_variables,
    should_use_client_cert,
)

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object, None]  # type: ignore

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)

import google.api_core.operation as operation  # type: ignore
import google.api_core.operation_async as operation_async  # type: ignore
import google.protobuf.duration_pb2 as duration_pb2  # type: ignore
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.contact_center_insights_v1.services.contact_center_insights import (
    pagers,
)
from google.cloud.contact_center_insights_v1.types import (
    contact_center_insights,
    resources,
)

from .transports.base import DEFAULT_CLIENT_INFO, ContactCenterInsightsTransport
from .transports.grpc import ContactCenterInsightsGrpcTransport
from .transports.grpc_asyncio import ContactCenterInsightsGrpcAsyncIOTransport
from .transports.rest import ContactCenterInsightsRestTransport


class ContactCenterInsightsClientMeta(type):
    """Metaclass for the ContactCenterInsights client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[ContactCenterInsightsTransport]]
    _transport_registry["grpc"] = ContactCenterInsightsGrpcTransport
    _transport_registry["grpc_asyncio"] = ContactCenterInsightsGrpcAsyncIOTransport
    _transport_registry["rest"] = ContactCenterInsightsRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[ContactCenterInsightsTransport]:
        """Returns an appropriate transport class.

        Args:
            label: The name of the desired transport. If none is
                provided, then the first transport in the registry is used.

        Returns:
            The transport class to use.
        """
        # If a specific transport is requested, return that one.
        if label:
            return cls._transport_registry[label]

        # No transport is requested; return the default (that is, the first one
        # in the dictionary).
        return next(iter(cls._transport_registry.values()))


class ContactCenterInsightsClient(metaclass=ContactCenterInsightsClientMeta):
    """An API that lets users analyze and explore their business
    conversation data.
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "contactcenterinsights.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "contactcenterinsights.{UNIVERSE_DOMAIN}"
    _DEFAULT_UNIVERSE = "googleapis.com"

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ContactCenterInsightsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_info(info)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ContactCenterInsightsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ContactCenterInsightsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ContactCenterInsightsTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def analysis_path(
        project: str,
        location: str,
        conversation: str,
        analysis: str,
    ) -> str:
        """Returns a fully-qualified analysis string."""
        return "projects/{project}/locations/{location}/conversations/{conversation}/analyses/{analysis}".format(
            project=project,
            location=location,
            conversation=conversation,
            analysis=analysis,
        )

    @staticmethod
    def parse_analysis_path(path: str) -> Dict[str, str]:
        """Parses a analysis path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/conversations/(?P<conversation>.+?)/analyses/(?P<analysis>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def analysis_rule_path(
        project: str,
        location: str,
        analysis_rule: str,
    ) -> str:
        """Returns a fully-qualified analysis_rule string."""
        return "projects/{project}/locations/{location}/analysisRules/{analysis_rule}".format(
            project=project,
            location=location,
            analysis_rule=analysis_rule,
        )

    @staticmethod
    def parse_analysis_rule_path(path: str) -> Dict[str, str]:
        """Parses a analysis_rule path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/analysisRules/(?P<analysis_rule>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def conversation_path(
        project: str,
        location: str,
        conversation: str,
    ) -> str:
        """Returns a fully-qualified conversation string."""
        return "projects/{project}/locations/{location}/conversations/{conversation}".format(
            project=project,
            location=location,
            conversation=conversation,
        )

    @staticmethod
    def parse_conversation_path(path: str) -> Dict[str, str]:
        """Parses a conversation path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/conversations/(?P<conversation>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def conversation_profile_path(
        project: str,
        location: str,
        conversation_profile: str,
    ) -> str:
        """Returns a fully-qualified conversation_profile string."""
        return "projects/{project}/locations/{location}/conversationProfiles/{conversation_profile}".format(
            project=project,
            location=location,
            conversation_profile=conversation_profile,
        )

    @staticmethod
    def parse_conversation_profile_path(path: str) -> Dict[str, str]:
        """Parses a conversation_profile path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/conversationProfiles/(?P<conversation_profile>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def encryption_spec_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified encryption_spec string."""
        return "projects/{project}/locations/{location}/encryptionSpec".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_encryption_spec_path(path: str) -> Dict[str, str]:
        """Parses a encryption_spec path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/encryptionSpec$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def feedback_label_path(
        project: str,
        location: str,
        conversation: str,
        feedback_label: str,
    ) -> str:
        """Returns a fully-qualified feedback_label string."""
        return "projects/{project}/locations/{location}/conversations/{conversation}/feedbackLabels/{feedback_label}".format(
            project=project,
            location=location,
            conversation=conversation,
            feedback_label=feedback_label,
        )

    @staticmethod
    def parse_feedback_label_path(path: str) -> Dict[str, str]:
        """Parses a feedback_label path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/conversations/(?P<conversation>.+?)/feedbackLabels/(?P<feedback_label>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def issue_path(
        project: str,
        location: str,
        issue_model: str,
        issue: str,
    ) -> str:
        """Returns a fully-qualified issue string."""
        return "projects/{project}/locations/{location}/issueModels/{issue_model}/issues/{issue}".format(
            project=project,
            location=location,
            issue_model=issue_model,
            issue=issue,
        )

    @staticmethod
    def parse_issue_path(path: str) -> Dict[str, str]:
        """Parses a issue path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/issueModels/(?P<issue_model>.+?)/issues/(?P<issue>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def issue_model_path(
        project: str,
        location: str,
        issue_model: str,
    ) -> str:
        """Returns a fully-qualified issue_model string."""
        return (
            "projects/{project}/locations/{location}/issueModels/{issue_model}".format(
                project=project,
                location=location,
                issue_model=issue_model,
            )
        )

    @staticmethod
    def parse_issue_model_path(path: str) -> Dict[str, str]:
        """Parses a issue_model path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/issueModels/(?P<issue_model>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def participant_path(
        project: str,
        conversation: str,
        participant: str,
    ) -> str:
        """Returns a fully-qualified participant string."""
        return "projects/{project}/conversations/{conversation}/participants/{participant}".format(
            project=project,
            conversation=conversation,
            participant=participant,
        )

    @staticmethod
    def parse_participant_path(path: str) -> Dict[str, str]:
        """Parses a participant path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversations/(?P<conversation>.+?)/participants/(?P<participant>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def phrase_matcher_path(
        project: str,
        location: str,
        phrase_matcher: str,
    ) -> str:
        """Returns a fully-qualified phrase_matcher string."""
        return "projects/{project}/locations/{location}/phraseMatchers/{phrase_matcher}".format(
            project=project,
            location=location,
            phrase_matcher=phrase_matcher,
        )

    @staticmethod
    def parse_phrase_matcher_path(path: str) -> Dict[str, str]:
        """Parses a phrase_matcher path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/phraseMatchers/(?P<phrase_matcher>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def qa_question_path(
        project: str,
        location: str,
        qa_scorecard: str,
        revision: str,
        qa_question: str,
    ) -> str:
        """Returns a fully-qualified qa_question string."""
        return "projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}/revisions/{revision}/qaQuestions/{qa_question}".format(
            project=project,
            location=location,
            qa_scorecard=qa_scorecard,
            revision=revision,
            qa_question=qa_question,
        )

    @staticmethod
    def parse_qa_question_path(path: str) -> Dict[str, str]:
        """Parses a qa_question path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/qaScorecards/(?P<qa_scorecard>.+?)/revisions/(?P<revision>.+?)/qaQuestions/(?P<qa_question>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def qa_scorecard_path(
        project: str,
        location: str,
        qa_scorecard: str,
    ) -> str:
        """Returns a fully-qualified qa_scorecard string."""
        return "projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}".format(
            project=project,
            location=location,
            qa_scorecard=qa_scorecard,
        )

    @staticmethod
    def parse_qa_scorecard_path(path: str) -> Dict[str, str]:
        """Parses a qa_scorecard path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/qaScorecards/(?P<qa_scorecard>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def qa_scorecard_result_path(
        project: str,
        location: str,
        qa_scorecard_result: str,
    ) -> str:
        """Returns a fully-qualified qa_scorecard_result string."""
        return "projects/{project}/locations/{location}/qaScorecardResults/{qa_scorecard_result}".format(
            project=project,
            location=location,
            qa_scorecard_result=qa_scorecard_result,
        )

    @staticmethod
    def parse_qa_scorecard_result_path(path: str) -> Dict[str, str]:
        """Parses a qa_scorecard_result path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/qaScorecardResults/(?P<qa_scorecard_result>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def qa_scorecard_revision_path(
        project: str,
        location: str,
        qa_scorecard: str,
        revision: str,
    ) -> str:
        """Returns a fully-qualified qa_scorecard_revision string."""
        return "projects/{project}/locations/{location}/qaScorecards/{qa_scorecard}/revisions/{revision}".format(
            project=project,
            location=location,
            qa_scorecard=qa_scorecard,
            revision=revision,
        )

    @staticmethod
    def parse_qa_scorecard_revision_path(path: str) -> Dict[str, str]:
        """Parses a qa_scorecard_revision path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/qaScorecards/(?P<qa_scorecard>.+?)/revisions/(?P<revision>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def recognizer_path(
        project: str,
        location: str,
        recognizer: str,
    ) -> str:
        """Returns a fully-qualified recognizer string."""
        return (
            "projects/{project}/locations/{location}/recognizers/{recognizer}".format(
                project=project,
                location=location,
                recognizer=recognizer,
            )
        )

    @staticmethod
    def parse_recognizer_path(path: str) -> Dict[str, str]:
        """Parses a recognizer path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/recognizers/(?P<recognizer>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def settings_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified settings string."""
        return "projects/{project}/locations/{location}/settings".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_settings_path(path: str) -> Dict[str, str]:
        """Parses a settings path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/settings$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def view_path(
        project: str,
        location: str,
        view: str,
    ) -> str:
        """Returns a fully-qualified view string."""
        return "projects/{project}/locations/{location}/views/{view}".format(
            project=project,
            location=location,
            view=view,
        )

    @staticmethod
    def parse_view_path(path: str) -> Dict[str, str]:
        """Parses a view path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/views/(?P<view>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def common_billing_account_path(
        billing_account: str,
    ) -> str:
        """Returns a fully-qualified billing_account string."""
        return "billingAccounts/{billing_account}".format(
            billing_account=billing_account,
        )

    @staticmethod
    def parse_common_billing_account_path(path: str) -> Dict[str, str]:
        """Parse a billing_account path into its component segments."""
        m = re.match(r"^billingAccounts/(?P<billing_account>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_folder_path(
        folder: str,
    ) -> str:
        """Returns a fully-qualified folder string."""
        return "folders/{folder}".format(
            folder=folder,
        )

    @staticmethod
    def parse_common_folder_path(path: str) -> Dict[str, str]:
        """Parse a folder path into its component segments."""
        m = re.match(r"^folders/(?P<folder>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_organization_path(
        organization: str,
    ) -> str:
        """Returns a fully-qualified organization string."""
        return "organizations/{organization}".format(
            organization=organization,
        )

    @staticmethod
    def parse_common_organization_path(path: str) -> Dict[str, str]:
        """Parse a organization path into its component segments."""
        m = re.match(r"^organizations/(?P<organization>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_project_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified project string."""
        return "projects/{project}".format(
            project=project,
        )

    @staticmethod
    def parse_common_project_path(path: str) -> Dict[str, str]:
        """Parse a project path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def common_location_path(
        project: str,
        location: str,
    ) -> str:
        """Returns a fully-qualified location string."""
        return "projects/{project}/locations/{location}".format(
            project=project,
            location=location,
        )

    @staticmethod
    def parse_common_location_path(path: str) -> Dict[str, str]:
        """Parse a location path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)$", path)
        return m.groupdict() if m else {}

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[client_options_lib.ClientOptions] = None
    ):
        """Deprecated. Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """

        warnings.warn(
            "get_mtls_endpoint_and_cert_source is deprecated. Use the api_endpoint property instead.",
            DeprecationWarning,
        )
        if client_options is None:
            client_options = client_options_lib.ClientOptions()
        use_client_cert = should_use_client_cert()
        use_mtls_endpoint = os.getenv("GOOGLE_API_USE_MTLS_ENDPOINT", "auto")
        if use_mtls_endpoint not in ("auto", "never", "always"):
            raise MutualTLSChannelError(
                "Environment variable `GOOGLE_API_USE_MTLS_ENDPOINT` must be `never`, `auto` or `always`"
            )

        # Figure out the client cert source to use.
        client_cert_source = None
        if use_client_cert:
            if client_options.client_cert_source:
                client_cert_source = client_options.client_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()

        # Figure out which api endpoint to use.
        if client_options.api_endpoint is not None:
            api_endpoint = client_options.api_endpoint
        elif use_mtls_endpoint == "always" or (
            use_mtls_endpoint == "auto" and client_cert_source
        ):
            api_endpoint = cls.DEFAULT_MTLS_ENDPOINT  # type: ignore
        else:
            api_endpoint = cls.DEFAULT_ENDPOINT

        return api_endpoint, client_cert_source

    @staticmethod
    def _get_client_cert_source(provided_cert_source, use_cert_flag):
        """Return the client cert source to be used by the client.

        Args:
            provided_cert_source (bytes): The client certificate source provided.
            use_cert_flag (bool): A flag indicating whether to use the client certificate.

        Returns:
            bytes or None: The client cert source to be used by the client.
        """
        client_cert_source = None
        if use_cert_flag:
            if provided_cert_source:
                client_cert_source = provided_cert_source
            elif mtls.has_default_client_cert_source():
                client_cert_source = mtls.default_client_cert_source()
        return client_cert_source

    def _validate_universe_domain(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            ValueError: If the configured universe domain is not valid.
        """

        # NOTE (b/349488459): universe validation is disabled until further notice.
        return True

    def _add_cred_info_for_auth_errors(
        self, error: core_exceptions.GoogleAPICallError
    ) -> None:
        """Adds credential info string to error details for 401/403/404 errors.

        Args:
            error (google.api_core.exceptions.GoogleAPICallError): The error to add the cred info.
        """
        if error.code not in [
            HTTPStatus.UNAUTHORIZED,
            HTTPStatus.FORBIDDEN,
            HTTPStatus.NOT_FOUND,
        ]:
            return

        cred = self._transport._credentials

        # get_cred_info is only available in google-auth>=2.35.0
        if not hasattr(cred, "get_cred_info"):
            return

        # ignore the type check since pypy test fails when get_cred_info
        # is not available
        cred_info = cred.get_cred_info()  # type: ignore
        if cred_info and hasattr(error._details, "append"):
            error._details.append(json.dumps(cred_info))

    @property
    def api_endpoint(self) -> str:
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used by the client instance.
        """
        return self._universe_domain

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                ContactCenterInsightsTransport,
                Callable[..., ContactCenterInsightsTransport],
            ]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the contact center insights client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ContactCenterInsightsTransport,Callable[..., ContactCenterInsightsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ContactCenterInsightsTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that the ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client_options = client_options
        if isinstance(self._client_options, dict):
            self._client_options = client_options_lib.from_dict(self._client_options)
        if self._client_options is None:
            self._client_options = client_options_lib.ClientOptions()
        self._client_options = cast(
            client_options_lib.ClientOptions, self._client_options
        )

        universe_domain_opt = getattr(self._client_options, "universe_domain", None)

        self._use_client_cert, self._use_mtls_endpoint, self._universe_domain_env = (
            read_environment_variables()
        )
        self._client_cert_source = ContactCenterInsightsClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=ContactCenterInsightsClient._DEFAULT_UNIVERSE,
        )
        self._api_endpoint: str = ""  # updated below, depending on `transport`

        # Initialize the universe domain validation.
        self._is_universe_domain_valid = False

        if CLIENT_LOGGING_SUPPORTED:  # pragma: NO COVER
            # Setup logging.
            client_logging.initialize_logging()

        api_key_value = getattr(self._client_options, "api_key", None)
        if api_key_value and credentials:
            raise ValueError(
                "client_options.api_key and credentials are mutually exclusive"
            )

        # Save or instantiate the transport.
        # Ordinarily, we provide the transport, but allowing a custom transport
        # instance provides an extensibility point for unusual situations.
        transport_provided = isinstance(transport, ContactCenterInsightsTransport)
        if transport_provided:
            # transport is a ContactCenterInsightsTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(ContactCenterInsightsTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=ContactCenterInsightsClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=ContactCenterInsightsClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=ContactCenterInsightsClient._DEFAULT_ENDPOINT_TEMPLATE,
            use_mtls=self._use_mtls_endpoint == "always"
            or (self._use_mtls_endpoint == "auto" and self._client_cert_source),
        )

        if not transport_provided:
            import google.auth._default  # type: ignore

            if api_key_value and hasattr(
                google.auth._default, "get_api_key_credentials"
            ):
                credentials = google.auth._default.get_api_key_credentials(
                    api_key_value
                )

            transport_init: Union[
                Type[ContactCenterInsightsTransport],
                Callable[..., ContactCenterInsightsTransport],
            ] = (
                ContactCenterInsightsClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., ContactCenterInsightsTransport], transport)
            )
            # initialize with the provided callable or the passed in class
            self._transport = transport_init(
                credentials=credentials,
                credentials_file=self._client_options.credentials_file,
                host=self._api_endpoint,
                scopes=self._client_options.scopes,
                client_cert_source_for_mtls=self._client_cert_source,
                quota_project_id=self._client_options.quota_project_id,
                client_info=client_info,
                always_use_jwt_access=True,
                api_audience=self._client_options.api_audience,
            )

        if "async" not in str(self._transport):
            if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
                std_logging.DEBUG
            ):  # pragma: NO COVER
                _LOGGER.debug(
                    "Created client `google.cloud.contactcenterinsights_v1.ContactCenterInsightsClient`.",
                    extra={
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "universeDomain": getattr(
                            self._transport._credentials, "universe_domain", ""
                        ),
                        "credentialsType": f"{type(self._transport._credentials).__module__}.{type(self._transport._credentials).__qualname__}",
                        "credentialsInfo": getattr(
                            self.transport._credentials, "get_cred_info", lambda: None
                        )(),
                    }
                    if hasattr(self._transport, "_credentials")
                    else {
                        "serviceName": "google.cloud.contactcenterinsights.v1.ContactCenterInsights",
                        "credentialsType": None,
                    },
                )

    def create_conversation(
        self,
        request: Optional[
            Union[contact_center_insights.CreateConversationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        conversation: Optional[resources.Conversation] = None,
        conversation_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Conversation:
        r"""Creates a conversation. Note that this method does not support
        audio transcription or redaction. Use ``conversations.upload``
        instead.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_conversation():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateConversationRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateConversationRequest, dict]):
                The request object. Request to create a conversation.
            parent (str):
                Required. The parent resource of the
                conversation.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation (google.cloud.contact_center_insights_v1.types.Conversation):
                Required. The conversation resource
                to create.

                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation_id (str):
                A unique ID for the new conversation. This ID will
                become the final component of the conversation's
                resource name. If no ID is specified, a server-generated
                ID will be used.

                This value should be 4-64 characters and must match the
                regular expression ``^[a-z0-9-]{4,64}$``. Valid
                characters are ``[a-z][0-9]-``

                This corresponds to the ``conversation_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Conversation:
                The conversation resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, conversation, conversation_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateConversationRequest):
            request = contact_center_insights.CreateConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if conversation is not None:
                request.conversation = conversation
            if conversation_id is not None:
                request.conversation_id = conversation_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def upload_conversation(
        self,
        request: Optional[
            Union[contact_center_insights.UploadConversationRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Create a long-running conversation upload operation. This method
        differs from ``CreateConversation`` by allowing audio
        transcription and optional DLP redaction.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_upload_conversation():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UploadConversationRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.upload_conversation(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UploadConversationRequest, dict]):
                The request object. Request to upload a conversation.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.Conversation`
                The conversation resource.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UploadConversationRequest):
            request = contact_center_insights.UploadConversationRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.upload_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.Conversation,
            metadata_type=contact_center_insights.UploadConversationMetadata,
        )

        # Done; return the response.
        return response

    def update_conversation(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateConversationRequest, dict]
        ] = None,
        *,
        conversation: Optional[resources.Conversation] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Conversation:
        r"""Updates a conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_conversation():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateConversationRequest(
                )

                # Make the request
                response = client.update_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateConversationRequest, dict]):
                The request object. The request to update a conversation.
            conversation (google.cloud.contact_center_insights_v1.types.Conversation):
                Required. The new values for the
                conversation.

                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The list of fields to be updated. All possible fields
                can be updated by passing ``*``, or a subset of the
                following updateable fields can be provided:

                - ``agent_id``
                - ``language_code``
                - ``labels``
                - ``metadata``
                - ``quality_metadata``
                - ``call_metadata``
                - ``start_time``
                - ``expire_time`` or ``ttl``
                - ``data_source.gcs_source.audio_uri`` or
                  ``data_source.dialogflow_source.audio_uri``

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Conversation:
                The conversation resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateConversationRequest):
            request = contact_center_insights.UpdateConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if conversation is not None:
                request.conversation = conversation
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation.name", request.conversation.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_conversation(
        self,
        request: Optional[
            Union[contact_center_insights.GetConversationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Conversation:
        r"""Gets a conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_conversation():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetConversationRequest, dict]):
                The request object. The request to get a conversation.
            name (str):
                Required. The name of the
                conversation to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Conversation:
                The conversation resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetConversationRequest):
            request = contact_center_insights.GetConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_conversations(
        self,
        request: Optional[
            Union[contact_center_insights.ListConversationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListConversationsPager:
        r"""Lists conversations.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_conversations():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListConversationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversations(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListConversationsRequest, dict]):
                The request object. Request to list conversations.
            parent (str):
                Required. The parent resource of the
                conversation.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListConversationsPager:
                The response of listing
                conversations.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListConversationsRequest):
            request = contact_center_insights.ListConversationsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_conversations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListConversationsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_conversation(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteConversationRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_conversation():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteConversationRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_conversation(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteConversationRequest, dict]):
                The request object. The request to delete a conversation.
            name (str):
                Required. The name of the
                conversation to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteConversationRequest):
            request = contact_center_insights.DeleteConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_conversation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def create_analysis(
        self,
        request: Optional[
            Union[contact_center_insights.CreateAnalysisRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        analysis: Optional[resources.Analysis] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates an analysis. The long running operation is
        done when the analysis has completed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_analysis():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateAnalysisRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_analysis(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateAnalysisRequest, dict]):
                The request object. The request to create an analysis.
            parent (str):
                Required. The parent resource of the
                analysis.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            analysis (google.cloud.contact_center_insights_v1.types.Analysis):
                Required. The analysis to create.
                This corresponds to the ``analysis`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.Analysis`
                The analysis resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, analysis]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateAnalysisRequest):
            request = contact_center_insights.CreateAnalysisRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if analysis is not None:
                request.analysis = analysis

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_analysis]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.Analysis,
            metadata_type=contact_center_insights.CreateAnalysisOperationMetadata,
        )

        # Done; return the response.
        return response

    def get_analysis(
        self,
        request: Optional[
            Union[contact_center_insights.GetAnalysisRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Analysis:
        r"""Gets an analysis.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_analysis():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetAnalysisRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_analysis(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetAnalysisRequest, dict]):
                The request object. The request to get an analysis.
            name (str):
                Required. The name of the analysis to
                get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Analysis:
                The analysis resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetAnalysisRequest):
            request = contact_center_insights.GetAnalysisRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_analysis]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_analyses(
        self,
        request: Optional[
            Union[contact_center_insights.ListAnalysesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAnalysesPager:
        r"""Lists analyses.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_analyses():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListAnalysesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_analyses(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListAnalysesRequest, dict]):
                The request object. The request to list analyses.
            parent (str):
                Required. The parent resource of the
                analyses.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListAnalysesPager:
                The response to list analyses.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListAnalysesRequest):
            request = contact_center_insights.ListAnalysesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_analyses]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAnalysesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_analysis(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteAnalysisRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an analysis.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_analysis():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteAnalysisRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_analysis(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteAnalysisRequest, dict]):
                The request object. The request to delete an analysis.
            name (str):
                Required. The name of the analysis to
                delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteAnalysisRequest):
            request = contact_center_insights.DeleteAnalysisRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_analysis]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def bulk_analyze_conversations(
        self,
        request: Optional[
            Union[contact_center_insights.BulkAnalyzeConversationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        analysis_percentage: Optional[float] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Analyzes multiple conversations in a single request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_bulk_analyze_conversations():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.BulkAnalyzeConversationsRequest(
                    parent="parent_value",
                    filter="filter_value",
                    analysis_percentage=0.20170000000000002,
                )

                # Make the request
                operation = client.bulk_analyze_conversations(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.BulkAnalyzeConversationsRequest, dict]):
                The request object. The request to analyze conversations
                in bulk.
            parent (str):
                Required. The parent resource to
                create analyses in.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (str):
                Required. Filter used to select the
                subset of conversations to analyze.

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            analysis_percentage (float):
                Required. Percentage of selected conversation to
                analyze, between [0, 100].

                This corresponds to the ``analysis_percentage`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.BulkAnalyzeConversationsResponse`
                The response for a bulk analyze conversations operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, filter, analysis_percentage]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.BulkAnalyzeConversationsRequest
        ):
            request = contact_center_insights.BulkAnalyzeConversationsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if filter is not None:
                request.filter = filter
            if analysis_percentage is not None:
                request.analysis_percentage = analysis_percentage

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.bulk_analyze_conversations
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.BulkAnalyzeConversationsResponse,
            metadata_type=contact_center_insights.BulkAnalyzeConversationsMetadata,
        )

        # Done; return the response.
        return response

    def bulk_delete_conversations(
        self,
        request: Optional[
            Union[contact_center_insights.BulkDeleteConversationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes multiple conversations in a single request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_bulk_delete_conversations():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.BulkDeleteConversationsRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.bulk_delete_conversations(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.BulkDeleteConversationsRequest, dict]):
                The request object. The request to delete conversations
                in bulk.
            parent (str):
                Required. The parent resource to
                delete conversations from. Format:

                projects/{project}/locations/{location}

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (str):
                Filter used to select the subset of
                conversations to delete.

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.BulkDeleteConversationsResponse`
                The response for a bulk delete conversations operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, filter]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.BulkDeleteConversationsRequest
        ):
            request = contact_center_insights.BulkDeleteConversationsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if filter is not None:
                request.filter = filter

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.bulk_delete_conversations
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.BulkDeleteConversationsResponse,
            metadata_type=contact_center_insights.BulkDeleteConversationsMetadata,
        )

        # Done; return the response.
        return response

    def ingest_conversations(
        self,
        request: Optional[
            Union[contact_center_insights.IngestConversationsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Imports conversations and processes them according to
        the user's configuration.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_ingest_conversations():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                gcs_source = contact_center_insights_v1.GcsSource()
                gcs_source.bucket_uri = "bucket_uri_value"

                transcript_object_config = contact_center_insights_v1.TranscriptObjectConfig()
                transcript_object_config.medium = "CHAT"

                request = contact_center_insights_v1.IngestConversationsRequest(
                    gcs_source=gcs_source,
                    transcript_object_config=transcript_object_config,
                    parent="parent_value",
                )

                # Make the request
                operation = client.ingest_conversations(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.IngestConversationsRequest, dict]):
                The request object. The request to ingest conversations.
            parent (str):
                Required. The parent resource for new
                conversations.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.IngestConversationsResponse`
                The response to an IngestConversations operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.IngestConversationsRequest):
            request = contact_center_insights.IngestConversationsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.ingest_conversations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.IngestConversationsResponse,
            metadata_type=contact_center_insights.IngestConversationsMetadata,
        )

        # Done; return the response.
        return response

    def export_insights_data(
        self,
        request: Optional[
            Union[contact_center_insights.ExportInsightsDataRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Export insights data to a destination defined in the
        request body.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_export_insights_data():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                big_query_destination = contact_center_insights_v1.BigQueryDestination()
                big_query_destination.dataset = "dataset_value"

                request = contact_center_insights_v1.ExportInsightsDataRequest(
                    big_query_destination=big_query_destination,
                    parent="parent_value",
                )

                # Make the request
                operation = client.export_insights_data(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ExportInsightsDataRequest, dict]):
                The request object. The request to export insights.
            parent (str):
                Required. The parent resource to
                export data from.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.ExportInsightsDataResponse`
                Response for an export insights operation.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ExportInsightsDataRequest):
            request = contact_center_insights.ExportInsightsDataRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.export_insights_data]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.ExportInsightsDataResponse,
            metadata_type=contact_center_insights.ExportInsightsDataMetadata,
        )

        # Done; return the response.
        return response

    def create_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.CreateIssueModelRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        issue_model: Optional[resources.IssueModel] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Creates an issue model.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateIssueModelRequest(
                    parent="parent_value",
                )

                # Make the request
                operation = client.create_issue_model(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateIssueModelRequest, dict]):
                The request object. The request to create an issue model.
            parent (str):
                Required. The parent resource of the
                issue model.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            issue_model (google.cloud.contact_center_insights_v1.types.IssueModel):
                Required. The issue model to create.
                This corresponds to the ``issue_model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.IssueModel`
                The issue model resource.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, issue_model]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateIssueModelRequest):
            request = contact_center_insights.CreateIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if issue_model is not None:
                request.issue_model = issue_model

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            resources.IssueModel,
            metadata_type=contact_center_insights.CreateIssueModelMetadata,
        )

        # Done; return the response.
        return response

    def update_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateIssueModelRequest, dict]
        ] = None,
        *,
        issue_model: Optional[resources.IssueModel] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.IssueModel:
        r"""Updates an issue model.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateIssueModelRequest(
                )

                # Make the request
                response = client.update_issue_model(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateIssueModelRequest, dict]):
                The request object. The request to update an issue model.
            issue_model (google.cloud.contact_center_insights_v1.types.IssueModel):
                Required. The new values for the
                issue model.

                This corresponds to the ``issue_model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.IssueModel:
                The issue model resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [issue_model, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateIssueModelRequest):
            request = contact_center_insights.UpdateIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if issue_model is not None:
                request.issue_model = issue_model
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("issue_model.name", request.issue_model.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.GetIssueModelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.IssueModel:
        r"""Gets an issue model.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetIssueModelRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_issue_model(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetIssueModelRequest, dict]):
                The request object. The request to get an issue model.
            name (str):
                Required. The name of the issue model
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.IssueModel:
                The issue model resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetIssueModelRequest):
            request = contact_center_insights.GetIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_issue_models(
        self,
        request: Optional[
            Union[contact_center_insights.ListIssueModelsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> contact_center_insights.ListIssueModelsResponse:
        r"""Lists issue models.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_issue_models():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListIssueModelsRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.list_issue_models(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListIssueModelsRequest, dict]):
                The request object. Request to list issue models.
            parent (str):
                Required. The parent resource of the
                issue model.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.ListIssueModelsResponse:
                The response of listing issue models.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListIssueModelsRequest):
            request = contact_center_insights.ListIssueModelsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_issue_models]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteIssueModelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deletes an issue model.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteIssueModelRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.delete_issue_model(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteIssueModelRequest, dict]):
                The request object. The request to delete an issue model.
            name (str):
                Required. The name of the issue model
                to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteIssueModelRequest):
            request = contact_center_insights.DeleteIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=contact_center_insights.DeleteIssueModelMetadata,
        )

        # Done; return the response.
        return response

    def deploy_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.DeployIssueModelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Deploys an issue model. Returns an error if a model
        is already deployed. An issue model can only be used in
        analysis after it has been deployed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_deploy_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeployIssueModelRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.deploy_issue_model(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeployIssueModelRequest, dict]):
                The request object. The request to deploy an issue model.
            name (str):
                Required. The issue model to deploy.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.DeployIssueModelResponse`
                The response to deploy an issue model.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeployIssueModelRequest):
            request = contact_center_insights.DeployIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.deploy_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.DeployIssueModelResponse,
            metadata_type=contact_center_insights.DeployIssueModelMetadata,
        )

        # Done; return the response.
        return response

    def undeploy_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.UndeployIssueModelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Undeploys an issue model.
        An issue model can not be used in analysis after it has
        been undeployed.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_undeploy_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UndeployIssueModelRequest(
                    name="name_value",
                )

                # Make the request
                operation = client.undeploy_issue_model(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UndeployIssueModelRequest, dict]):
                The request object. The request to undeploy an issue
                model.
            name (str):
                Required. The issue model to
                undeploy.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.UndeployIssueModelResponse`
                The response to undeploy an issue model.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UndeployIssueModelRequest):
            request = contact_center_insights.UndeployIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.undeploy_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.UndeployIssueModelResponse,
            metadata_type=contact_center_insights.UndeployIssueModelMetadata,
        )

        # Done; return the response.
        return response

    def export_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.ExportIssueModelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Exports an issue model to the provided destination.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_export_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                gcs_destination = contact_center_insights_v1.GcsDestination()
                gcs_destination.object_uri = "object_uri_value"

                request = contact_center_insights_v1.ExportIssueModelRequest(
                    gcs_destination=gcs_destination,
                    name="name_value",
                )

                # Make the request
                operation = client.export_issue_model(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ExportIssueModelRequest, dict]):
                The request object. Request to export an issue model.
            name (str):
                Required. The issue model to export.
                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.ExportIssueModelResponse`
                Response from export issue model

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ExportIssueModelRequest):
            request = contact_center_insights.ExportIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.export_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.ExportIssueModelResponse,
            metadata_type=contact_center_insights.ExportIssueModelMetadata,
        )

        # Done; return the response.
        return response

    def import_issue_model(
        self,
        request: Optional[
            Union[contact_center_insights.ImportIssueModelRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Imports an issue model from a Cloud Storage bucket.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_import_issue_model():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                gcs_source = contact_center_insights_v1.GcsSource()
                gcs_source.object_uri = "object_uri_value"

                request = contact_center_insights_v1.ImportIssueModelRequest(
                    gcs_source=gcs_source,
                    parent="parent_value",
                )

                # Make the request
                operation = client.import_issue_model(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ImportIssueModelRequest, dict]):
                The request object. Request to import an issue model.
            parent (str):
                Required. The parent resource of the
                issue model.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.ImportIssueModelResponse`
                Response from import issue model

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ImportIssueModelRequest):
            request = contact_center_insights.ImportIssueModelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.import_issue_model]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.ImportIssueModelResponse,
            metadata_type=contact_center_insights.ImportIssueModelMetadata,
        )

        # Done; return the response.
        return response

    def get_issue(
        self,
        request: Optional[Union[contact_center_insights.GetIssueRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Issue:
        r"""Gets an issue.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_issue():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetIssueRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_issue(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetIssueRequest, dict]):
                The request object. The request to get an issue.
            name (str):
                Required. The name of the issue to
                get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Issue:
                The issue resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetIssueRequest):
            request = contact_center_insights.GetIssueRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_issue]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_issues(
        self,
        request: Optional[
            Union[contact_center_insights.ListIssuesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> contact_center_insights.ListIssuesResponse:
        r"""Lists issues.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_issues():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListIssuesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.list_issues(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListIssuesRequest, dict]):
                The request object. Request to list issues.
            parent (str):
                Required. The parent resource of the
                issue.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.ListIssuesResponse:
                The response of listing issues.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListIssuesRequest):
            request = contact_center_insights.ListIssuesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_issues]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_issue(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateIssueRequest, dict]
        ] = None,
        *,
        issue: Optional[resources.Issue] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Issue:
        r"""Updates an issue.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_issue():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateIssueRequest(
                )

                # Make the request
                response = client.update_issue(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateIssueRequest, dict]):
                The request object. The request to update an issue.
            issue (google.cloud.contact_center_insights_v1.types.Issue):
                Required. The new values for the
                issue.

                This corresponds to the ``issue`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Issue:
                The issue resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [issue, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateIssueRequest):
            request = contact_center_insights.UpdateIssueRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if issue is not None:
                request.issue = issue
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_issue]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("issue.name", request.issue.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_issue(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteIssueRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes an issue.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_issue():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteIssueRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_issue(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteIssueRequest, dict]):
                The request object. The request to delete an issue.
            name (str):
                Required. The name of the issue to
                delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteIssueRequest):
            request = contact_center_insights.DeleteIssueRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_issue]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def calculate_issue_model_stats(
        self,
        request: Optional[
            Union[contact_center_insights.CalculateIssueModelStatsRequest, dict]
        ] = None,
        *,
        issue_model: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> contact_center_insights.CalculateIssueModelStatsResponse:
        r"""Gets an issue model's statistics.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_calculate_issue_model_stats():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CalculateIssueModelStatsRequest(
                    issue_model="issue_model_value",
                )

                # Make the request
                response = client.calculate_issue_model_stats(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CalculateIssueModelStatsRequest, dict]):
                The request object. Request to get statistics of an issue
                model.
            issue_model (str):
                Required. The resource name of the
                issue model to query against.

                This corresponds to the ``issue_model`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.CalculateIssueModelStatsResponse:
                Response of querying an issue model's
                statistics.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [issue_model]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.CalculateIssueModelStatsRequest
        ):
            request = contact_center_insights.CalculateIssueModelStatsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if issue_model is not None:
                request.issue_model = issue_model

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.calculate_issue_model_stats
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("issue_model", request.issue_model),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_phrase_matcher(
        self,
        request: Optional[
            Union[contact_center_insights.CreatePhraseMatcherRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        phrase_matcher: Optional[resources.PhraseMatcher] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.PhraseMatcher:
        r"""Creates a phrase matcher.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_phrase_matcher():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                phrase_matcher = contact_center_insights_v1.PhraseMatcher()
                phrase_matcher.type_ = "ANY_OF"

                request = contact_center_insights_v1.CreatePhraseMatcherRequest(
                    parent="parent_value",
                    phrase_matcher=phrase_matcher,
                )

                # Make the request
                response = client.create_phrase_matcher(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreatePhraseMatcherRequest, dict]):
                The request object. Request to create a phrase matcher.
            parent (str):
                Required. The parent resource of the phrase matcher.
                Required. The location to create a phrase matcher for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>`` or
                ``projects/<Project Number>/locations/<Location ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            phrase_matcher (google.cloud.contact_center_insights_v1.types.PhraseMatcher):
                Required. The phrase matcher resource
                to create.

                This corresponds to the ``phrase_matcher`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.PhraseMatcher:
                The phrase matcher resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, phrase_matcher]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreatePhraseMatcherRequest):
            request = contact_center_insights.CreatePhraseMatcherRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if phrase_matcher is not None:
                request.phrase_matcher = phrase_matcher

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_phrase_matcher]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_phrase_matcher(
        self,
        request: Optional[
            Union[contact_center_insights.GetPhraseMatcherRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.PhraseMatcher:
        r"""Gets a phrase matcher.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_phrase_matcher():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetPhraseMatcherRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_phrase_matcher(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetPhraseMatcherRequest, dict]):
                The request object. The request to get a a phrase
                matcher.
            name (str):
                Required. The name of the phrase
                matcher to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.PhraseMatcher:
                The phrase matcher resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetPhraseMatcherRequest):
            request = contact_center_insights.GetPhraseMatcherRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_phrase_matcher]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_phrase_matchers(
        self,
        request: Optional[
            Union[contact_center_insights.ListPhraseMatchersRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListPhraseMatchersPager:
        r"""Lists phrase matchers.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_phrase_matchers():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListPhraseMatchersRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_phrase_matchers(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListPhraseMatchersRequest, dict]):
                The request object. Request to list phrase matchers.
            parent (str):
                Required. The parent resource of the
                phrase matcher.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListPhraseMatchersPager:
                The response of listing phrase
                matchers.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListPhraseMatchersRequest):
            request = contact_center_insights.ListPhraseMatchersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_phrase_matchers]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListPhraseMatchersPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_phrase_matcher(
        self,
        request: Optional[
            Union[contact_center_insights.DeletePhraseMatcherRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a phrase matcher.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_phrase_matcher():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeletePhraseMatcherRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_phrase_matcher(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeletePhraseMatcherRequest, dict]):
                The request object. The request to delete a phrase
                matcher.
            name (str):
                Required. The name of the phrase
                matcher to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeletePhraseMatcherRequest):
            request = contact_center_insights.DeletePhraseMatcherRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_phrase_matcher]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def update_phrase_matcher(
        self,
        request: Optional[
            Union[contact_center_insights.UpdatePhraseMatcherRequest, dict]
        ] = None,
        *,
        phrase_matcher: Optional[resources.PhraseMatcher] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.PhraseMatcher:
        r"""Updates a phrase matcher.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_phrase_matcher():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                phrase_matcher = contact_center_insights_v1.PhraseMatcher()
                phrase_matcher.type_ = "ANY_OF"

                request = contact_center_insights_v1.UpdatePhraseMatcherRequest(
                    phrase_matcher=phrase_matcher,
                )

                # Make the request
                response = client.update_phrase_matcher(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdatePhraseMatcherRequest, dict]):
                The request object. The request to update a phrase
                matcher.
            phrase_matcher (google.cloud.contact_center_insights_v1.types.PhraseMatcher):
                Required. The new values for the
                phrase matcher.

                This corresponds to the ``phrase_matcher`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.PhraseMatcher:
                The phrase matcher resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [phrase_matcher, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdatePhraseMatcherRequest):
            request = contact_center_insights.UpdatePhraseMatcherRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if phrase_matcher is not None:
                request.phrase_matcher = phrase_matcher
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_phrase_matcher]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("phrase_matcher.name", request.phrase_matcher.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def calculate_stats(
        self,
        request: Optional[
            Union[contact_center_insights.CalculateStatsRequest, dict]
        ] = None,
        *,
        location: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> contact_center_insights.CalculateStatsResponse:
        r"""Gets conversation statistics.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_calculate_stats():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CalculateStatsRequest(
                    location="location_value",
                )

                # Make the request
                response = client.calculate_stats(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CalculateStatsRequest, dict]):
                The request object. The request for calculating
                conversation statistics.
            location (str):
                Required. The location of the
                conversations.

                This corresponds to the ``location`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.CalculateStatsResponse:
                The response for calculating
                conversation statistics.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [location]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CalculateStatsRequest):
            request = contact_center_insights.CalculateStatsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if location is not None:
                request.location = location

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.calculate_stats]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_settings(
        self,
        request: Optional[
            Union[contact_center_insights.GetSettingsRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Settings:
        r"""Gets project-level settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_settings():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetSettingsRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetSettingsRequest, dict]):
                The request object. The request to get project-level
                settings.
            name (str):
                Required. The name of the settings
                resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Settings:
                The CCAI Insights project wide settings.
                   Use these settings to configure the behavior of
                   Insights. View these settings with
                   [getsettings](https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/getSettings)
                   and change the settings with
                   [updateSettings](https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/updateSettings).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetSettingsRequest):
            request = contact_center_insights.GetSettingsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_settings]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_settings(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateSettingsRequest, dict]
        ] = None,
        *,
        settings: Optional[resources.Settings] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.Settings:
        r"""Updates project-level settings.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_settings():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateSettingsRequest(
                )

                # Make the request
                response = client.update_settings(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateSettingsRequest, dict]):
                The request object. The request to update project-level
                settings.
            settings (google.cloud.contact_center_insights_v1.types.Settings):
                Required. The new settings values.
                This corresponds to the ``settings`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.Settings:
                The CCAI Insights project wide settings.
                   Use these settings to configure the behavior of
                   Insights. View these settings with
                   [getsettings](https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/getSettings)
                   and change the settings with
                   [updateSettings](https://cloud.google.com/contact-center/insights/docs/reference/rest/v1/projects.locations/updateSettings).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [settings, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateSettingsRequest):
            request = contact_center_insights.UpdateSettingsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if settings is not None:
                request.settings = settings
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_settings]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("settings.name", request.settings.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_analysis_rule(
        self,
        request: Optional[
            Union[contact_center_insights.CreateAnalysisRuleRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        analysis_rule: Optional[resources.AnalysisRule] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AnalysisRule:
        r"""Creates a analysis rule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_analysis_rule():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateAnalysisRuleRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_analysis_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateAnalysisRuleRequest, dict]):
                The request object. The request to create a analysis rule. analysis_rule_id
                will be generated by the server.
            parent (str):
                Required. The parent resource of the analysis rule.
                Required. The location to create a analysis rule for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>`` or
                ``projects/<Project Number>/locations/<Location ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            analysis_rule (google.cloud.contact_center_insights_v1.types.AnalysisRule):
                Required. The analysis rule resource
                to create.

                This corresponds to the ``analysis_rule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.AnalysisRule:
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
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, analysis_rule]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateAnalysisRuleRequest):
            request = contact_center_insights.CreateAnalysisRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if analysis_rule is not None:
                request.analysis_rule = analysis_rule

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_analysis_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_analysis_rule(
        self,
        request: Optional[
            Union[contact_center_insights.GetAnalysisRuleRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AnalysisRule:
        r"""Get a analysis rule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_analysis_rule():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetAnalysisRuleRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_analysis_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetAnalysisRuleRequest, dict]):
                The request object. The request for getting a analysis
                rule.
            name (str):
                Required. The name of the
                AnalysisRule to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.AnalysisRule:
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
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetAnalysisRuleRequest):
            request = contact_center_insights.GetAnalysisRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_analysis_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_analysis_rules(
        self,
        request: Optional[
            Union[contact_center_insights.ListAnalysisRulesRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAnalysisRulesPager:
        r"""Lists analysis rules.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_analysis_rules():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListAnalysisRulesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_analysis_rules(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListAnalysisRulesRequest, dict]):
                The request object. The request to list analysis rules.
            parent (str):
                Required. The parent resource of the
                analysis rules.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListAnalysisRulesPager:
                The response of listing views.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListAnalysisRulesRequest):
            request = contact_center_insights.ListAnalysisRulesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_analysis_rules]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAnalysisRulesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_analysis_rule(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateAnalysisRuleRequest, dict]
        ] = None,
        *,
        analysis_rule: Optional[resources.AnalysisRule] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.AnalysisRule:
        r"""Updates a analysis rule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_analysis_rule():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateAnalysisRuleRequest(
                )

                # Make the request
                response = client.update_analysis_rule(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateAnalysisRuleRequest, dict]):
                The request object. The request to update a analysis
                rule.
            analysis_rule (google.cloud.contact_center_insights_v1.types.AnalysisRule):
                Required. The new analysis rule.
                This corresponds to the ``analysis_rule`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Optional. The list of fields to be updated. If the
                update_mask is not provided, the update will be applied
                to all fields.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.AnalysisRule:
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
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [analysis_rule, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateAnalysisRuleRequest):
            request = contact_center_insights.UpdateAnalysisRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if analysis_rule is not None:
                request.analysis_rule = analysis_rule
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_analysis_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("analysis_rule.name", request.analysis_rule.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_analysis_rule(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteAnalysisRuleRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a analysis rule.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_analysis_rule():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteAnalysisRuleRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_analysis_rule(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteAnalysisRuleRequest, dict]):
                The request object. The request to delete a analysis
                rule.
            name (str):
                Required. The name of the analysis
                rule to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteAnalysisRuleRequest):
            request = contact_center_insights.DeleteAnalysisRuleRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_analysis_rule]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def get_encryption_spec(
        self,
        request: Optional[
            Union[contact_center_insights.GetEncryptionSpecRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.EncryptionSpec:
        r"""Gets location-level encryption key specification.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_encryption_spec():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetEncryptionSpecRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_encryption_spec(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetEncryptionSpecRequest, dict]):
                The request object. The request to get location-level
                encryption specification.
            name (str):
                Required. The name of the encryption
                spec resource to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.EncryptionSpec:
                A customer-managed encryption key specification that can be applied to all
                   created resources (e.g. Conversation).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetEncryptionSpecRequest):
            request = contact_center_insights.GetEncryptionSpecRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_encryption_spec]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def initialize_encryption_spec(
        self,
        request: Optional[
            Union[contact_center_insights.InitializeEncryptionSpecRequest, dict]
        ] = None,
        *,
        encryption_spec: Optional[resources.EncryptionSpec] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Initializes a location-level encryption key
        specification. An error will result if the location has
        resources already created before the initialization.
        After the encryption specification is initialized at a
        location, it is immutable and all newly created
        resources under the location will be encrypted with the
        existing specification.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_initialize_encryption_spec():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                encryption_spec = contact_center_insights_v1.EncryptionSpec()
                encryption_spec.kms_key = "kms_key_value"

                request = contact_center_insights_v1.InitializeEncryptionSpecRequest(
                    encryption_spec=encryption_spec,
                )

                # Make the request
                operation = client.initialize_encryption_spec(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.InitializeEncryptionSpecRequest, dict]):
                The request object. The request to initialize a
                location-level encryption specification.
            encryption_spec (google.cloud.contact_center_insights_v1.types.EncryptionSpec):
                Required. The encryption spec used for CMEK encryption.
                It is required that the kms key is in the same region as
                the endpoint. The same key will be used for all
                provisioned resources, if encryption is available. If
                the ``kms_key_name`` field is left empty, no encryption
                will be enforced.

                This corresponds to the ``encryption_spec`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.InitializeEncryptionSpecResponse`
                The response to initialize a location-level encryption
                specification.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [encryption_spec]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.InitializeEncryptionSpecRequest
        ):
            request = contact_center_insights.InitializeEncryptionSpecRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if encryption_spec is not None:
                request.encryption_spec = encryption_spec

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.initialize_encryption_spec
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("encryption_spec.name", request.encryption_spec.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.InitializeEncryptionSpecResponse,
            metadata_type=contact_center_insights.InitializeEncryptionSpecMetadata,
        )

        # Done; return the response.
        return response

    def create_view(
        self,
        request: Optional[
            Union[contact_center_insights.CreateViewRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        view: Optional[resources.View] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.View:
        r"""Creates a view.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_view():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateViewRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_view(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateViewRequest, dict]):
                The request object. The request to create a view.
            parent (str):
                Required. The parent resource of the view. Required. The
                location to create a view for. Format:
                ``projects/<Project ID>/locations/<Location ID>`` or
                ``projects/<Project Number>/locations/<Location ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            view (google.cloud.contact_center_insights_v1.types.View):
                Required. The view resource to
                create.

                This corresponds to the ``view`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.View:
                The View resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, view]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateViewRequest):
            request = contact_center_insights.CreateViewRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if view is not None:
                request.view = view

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_view]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_view(
        self,
        request: Optional[Union[contact_center_insights.GetViewRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.View:
        r"""Gets a view.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_view():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetViewRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_view(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetViewRequest, dict]):
                The request object. The request to get a view.
            name (str):
                Required. The name of the view to
                get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.View:
                The View resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetViewRequest):
            request = contact_center_insights.GetViewRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_view]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_views(
        self,
        request: Optional[Union[contact_center_insights.ListViewsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListViewsPager:
        r"""Lists views.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_views():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListViewsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_views(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListViewsRequest, dict]):
                The request object. The request to list views.
            parent (str):
                Required. The parent resource of the
                views.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListViewsPager:
                The response of listing views.

                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListViewsRequest):
            request = contact_center_insights.ListViewsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_views]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListViewsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_view(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateViewRequest, dict]
        ] = None,
        *,
        view: Optional[resources.View] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.View:
        r"""Updates a view.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_view():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateViewRequest(
                )

                # Make the request
                response = client.update_view(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateViewRequest, dict]):
                The request object. The request to update a view.
            view (google.cloud.contact_center_insights_v1.types.View):
                Required. The new view.
                This corresponds to the ``view`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                The list of fields to be updated.
                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.View:
                The View resource.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [view, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateViewRequest):
            request = contact_center_insights.UpdateViewRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if view is not None:
                request.view = view
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_view]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("view.name", request.view.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_view(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteViewRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a view.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_view():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteViewRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_view(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteViewRequest, dict]):
                The request object. The request to delete a view.
            name (str):
                Required. The name of the view to
                delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteViewRequest):
            request = contact_center_insights.DeleteViewRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_view]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def query_metrics(
        self,
        request: Optional[
            Union[contact_center_insights.QueryMetricsRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Query metrics.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_query_metrics():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.QueryMetricsRequest(
                    location="location_value",
                    filter="filter_value",
                )

                # Make the request
                operation = client.query_metrics(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.QueryMetricsRequest, dict]):
                The request object. The request for querying metrics.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.QueryMetricsResponse`
                The response for querying metrics.

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.QueryMetricsRequest):
            request = contact_center_insights.QueryMetricsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.query_metrics]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("location", request.location),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.QueryMetricsResponse,
            metadata_type=contact_center_insights.QueryMetricsMetadata,
        )

        # Done; return the response.
        return response

    def create_qa_question(
        self,
        request: Optional[
            Union[contact_center_insights.CreateQaQuestionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        qa_question: Optional[resources.QaQuestion] = None,
        qa_question_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaQuestion:
        r"""Create a QaQuestion.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_qa_question():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateQaQuestionRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_qa_question(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateQaQuestionRequest, dict]):
                The request object. The request for creating a
                QaQuestion.
            parent (str):
                Required. The parent resource of the
                QaQuestion.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            qa_question (google.cloud.contact_center_insights_v1.types.QaQuestion):
                Required. The QaQuestion to create.
                This corresponds to the ``qa_question`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            qa_question_id (str):
                Optional. A unique ID for the new question. This ID will
                become the final component of the question's resource
                name. If no ID is specified, a server-generated ID will
                be used.

                This value should be 4-64 characters and must match the
                regular expression ``^[a-z0-9-]{4,64}$``. Valid
                characters are ``[a-z][0-9]-``.

                This corresponds to the ``qa_question_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaQuestion:
                A single question to be scored by the
                Insights QA feature.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, qa_question, qa_question_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateQaQuestionRequest):
            request = contact_center_insights.CreateQaQuestionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if qa_question is not None:
                request.qa_question = qa_question
            if qa_question_id is not None:
                request.qa_question_id = qa_question_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_qa_question]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_qa_question(
        self,
        request: Optional[
            Union[contact_center_insights.GetQaQuestionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaQuestion:
        r"""Gets a QaQuestion.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_qa_question():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetQaQuestionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_qa_question(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetQaQuestionRequest, dict]):
                The request object. The request for a QaQuestion.
            name (str):
                Required. The name of the QaQuestion
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaQuestion:
                A single question to be scored by the
                Insights QA feature.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetQaQuestionRequest):
            request = contact_center_insights.GetQaQuestionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_qa_question]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_qa_question(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateQaQuestionRequest, dict]
        ] = None,
        *,
        qa_question: Optional[resources.QaQuestion] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaQuestion:
        r"""Updates a QaQuestion.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_qa_question():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateQaQuestionRequest(
                )

                # Make the request
                response = client.update_qa_question(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateQaQuestionRequest, dict]):
                The request object. The request for updating a
                QaQuestion.
            qa_question (google.cloud.contact_center_insights_v1.types.QaQuestion):
                Required. The QaQuestion to update.
                This corresponds to the ``qa_question`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to be updated. All possible
                fields can be updated by passing ``*``, or a subset of
                the following updateable fields can be provided:

                - ``abbreviation``
                - ``answer_choices``
                - ``answer_instructions``
                - ``order``
                - ``question_body``
                - ``tags``

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaQuestion:
                A single question to be scored by the
                Insights QA feature.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [qa_question, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateQaQuestionRequest):
            request = contact_center_insights.UpdateQaQuestionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if qa_question is not None:
                request.qa_question = qa_question
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_qa_question]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("qa_question.name", request.qa_question.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_qa_question(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteQaQuestionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a QaQuestion.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_qa_question():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteQaQuestionRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_qa_question(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteQaQuestionRequest, dict]):
                The request object. The request for deleting a
                QaQuestion.
            name (str):
                Required. The name of the QaQuestion
                to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteQaQuestionRequest):
            request = contact_center_insights.DeleteQaQuestionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_qa_question]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def list_qa_questions(
        self,
        request: Optional[
            Union[contact_center_insights.ListQaQuestionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListQaQuestionsPager:
        r"""Lists QaQuestions.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_qa_questions():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListQaQuestionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_qa_questions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListQaQuestionsRequest, dict]):
                The request object. Request to list QaQuestions.
            parent (str):
                Required. The parent resource of the
                questions.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListQaQuestionsPager:
                The response from a ListQaQuestions
                request.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListQaQuestionsRequest):
            request = contact_center_insights.ListQaQuestionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_qa_questions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListQaQuestionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_qa_scorecard(
        self,
        request: Optional[
            Union[contact_center_insights.CreateQaScorecardRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        qa_scorecard: Optional[resources.QaScorecard] = None,
        qa_scorecard_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecard:
        r"""Create a QaScorecard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_qa_scorecard():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateQaScorecardRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_qa_scorecard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateQaScorecardRequest, dict]):
                The request object. The request for creating a
                QaScorecard.
            parent (str):
                Required. The parent resource of the
                QaScorecard.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            qa_scorecard (google.cloud.contact_center_insights_v1.types.QaScorecard):
                Required. The QaScorecard to create.
                This corresponds to the ``qa_scorecard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            qa_scorecard_id (str):
                Optional. A unique ID for the new QaScorecard. This ID
                will become the final component of the QaScorecard's
                resource name. If no ID is specified, a server-generated
                ID will be used.

                This value should be 4-64 characters and must match the
                regular expression ``^[a-z0-9-]{4,64}$``. Valid
                characters are ``[a-z][0-9]-``.

                This corresponds to the ``qa_scorecard_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaScorecard:
                A QaScorecard represents a collection
                of questions to be scored during
                analysis.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, qa_scorecard, qa_scorecard_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateQaScorecardRequest):
            request = contact_center_insights.CreateQaScorecardRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if qa_scorecard is not None:
                request.qa_scorecard = qa_scorecard
            if qa_scorecard_id is not None:
                request.qa_scorecard_id = qa_scorecard_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_qa_scorecard]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_qa_scorecard(
        self,
        request: Optional[
            Union[contact_center_insights.GetQaScorecardRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecard:
        r"""Gets a QaScorecard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_qa_scorecard():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetQaScorecardRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_qa_scorecard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetQaScorecardRequest, dict]):
                The request object. The request for a QaScorecard. By
                default, returns the latest revision.
            name (str):
                Required. The name of the QaScorecard
                to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaScorecard:
                A QaScorecard represents a collection
                of questions to be scored during
                analysis.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetQaScorecardRequest):
            request = contact_center_insights.GetQaScorecardRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_qa_scorecard]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_qa_scorecard(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateQaScorecardRequest, dict]
        ] = None,
        *,
        qa_scorecard: Optional[resources.QaScorecard] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecard:
        r"""Updates a QaScorecard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_qa_scorecard():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UpdateQaScorecardRequest(
                )

                # Make the request
                response = client.update_qa_scorecard(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateQaScorecardRequest, dict]):
                The request object. The request for updating a
                QaScorecard.
            qa_scorecard (google.cloud.contact_center_insights_v1.types.QaScorecard):
                Required. The QaScorecard to update.
                This corresponds to the ``qa_scorecard`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to be updated. All possible
                fields can be updated by passing ``*``, or a subset of
                the following updateable fields can be provided:

                - ``description``
                - ``display_name``

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaScorecard:
                A QaScorecard represents a collection
                of questions to be scored during
                analysis.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [qa_scorecard, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateQaScorecardRequest):
            request = contact_center_insights.UpdateQaScorecardRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if qa_scorecard is not None:
                request.qa_scorecard = qa_scorecard
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_qa_scorecard]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("qa_scorecard.name", request.qa_scorecard.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_qa_scorecard(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteQaScorecardRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a QaScorecard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_qa_scorecard():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteQaScorecardRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_qa_scorecard(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteQaScorecardRequest, dict]):
                The request object. The request for deleting a
                QaScorecard.
            name (str):
                Required. The name of the QaScorecard
                to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteQaScorecardRequest):
            request = contact_center_insights.DeleteQaScorecardRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_qa_scorecard]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def list_qa_scorecards(
        self,
        request: Optional[
            Union[contact_center_insights.ListQaScorecardsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListQaScorecardsPager:
        r"""Lists QaScorecards.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_qa_scorecards():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListQaScorecardsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_qa_scorecards(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListQaScorecardsRequest, dict]):
                The request object. Request to list QaScorecards.
            parent (str):
                Required. The parent resource of the
                scorecards.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListQaScorecardsPager:
                The response from a ListQaScorecards
                request.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListQaScorecardsRequest):
            request = contact_center_insights.ListQaScorecardsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_qa_scorecards]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListQaScorecardsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_qa_scorecard_revision(
        self,
        request: Optional[
            Union[contact_center_insights.CreateQaScorecardRevisionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        qa_scorecard_revision: Optional[resources.QaScorecardRevision] = None,
        qa_scorecard_revision_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecardRevision:
        r"""Creates a QaScorecardRevision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_qa_scorecard_revision():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.CreateQaScorecardRevisionRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_qa_scorecard_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateQaScorecardRevisionRequest, dict]):
                The request object. The request for creating a
                QaScorecardRevision.
            parent (str):
                Required. The parent resource of the
                QaScorecardRevision.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            qa_scorecard_revision (google.cloud.contact_center_insights_v1.types.QaScorecardRevision):
                Required. The QaScorecardRevision to
                create.

                This corresponds to the ``qa_scorecard_revision`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            qa_scorecard_revision_id (str):
                Optional. A unique ID for the new QaScorecardRevision.
                This ID will become the final component of the
                QaScorecardRevision's resource name. If no ID is
                specified, a server-generated ID will be used.

                This value should be 4-64 characters and must match the
                regular expression ``^[a-z0-9-]{4,64}$``. Valid
                characters are ``[a-z][0-9]-``.

                This corresponds to the ``qa_scorecard_revision_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaScorecardRevision:
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
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, qa_scorecard_revision, qa_scorecard_revision_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.CreateQaScorecardRevisionRequest
        ):
            request = contact_center_insights.CreateQaScorecardRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if qa_scorecard_revision is not None:
                request.qa_scorecard_revision = qa_scorecard_revision
            if qa_scorecard_revision_id is not None:
                request.qa_scorecard_revision_id = qa_scorecard_revision_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.create_qa_scorecard_revision
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_qa_scorecard_revision(
        self,
        request: Optional[
            Union[contact_center_insights.GetQaScorecardRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecardRevision:
        r"""Gets a QaScorecardRevision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_qa_scorecard_revision():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetQaScorecardRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_qa_scorecard_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetQaScorecardRevisionRequest, dict]):
                The request object. The request for a
                QaScorecardRevision.
            name (str):
                Required. The name of the
                QaScorecardRevision to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.QaScorecardRevision:
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
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.GetQaScorecardRevisionRequest
        ):
            request = contact_center_insights.GetQaScorecardRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.get_qa_scorecard_revision
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def tune_qa_scorecard_revision(
        self,
        request: Optional[
            Union[contact_center_insights.TuneQaScorecardRevisionRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        filter: Optional[str] = None,
        validate_only: Optional[bool] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Fine tune one or more QaModels.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_tune_qa_scorecard_revision():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.TuneQaScorecardRevisionRequest(
                    parent="parent_value",
                    filter="filter_value",
                )

                # Make the request
                operation = client.tune_qa_scorecard_revision(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionRequest, dict]):
                The request object. Request for TuneQaScorecardRevision
                endpoint.
            parent (str):
                Required. The parent resource for new
                fine tuning job instance.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            filter (str):
                Required. Filter for selecting the
                feedback labels that needs to be used
                for training. This filter can be used to
                limit the feedback labels used for
                tuning to a feedback labels created or
                updated for a specific time-window etc.

                This corresponds to the ``filter`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            validate_only (bool):
                Optional. Run in validate only mode,
                no fine tuning will actually run. Data
                quality validations like training data
                distributions will run. Even when set to
                false, the data quality validations will
                still run but once the validations
                complete we will proceed with the fine
                tune, if applicable.

                This corresponds to the ``validate_only`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.TuneQaScorecardRevisionResponse`
                Response for TuneQaScorecardRevision endpoint.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, filter, validate_only]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.TuneQaScorecardRevisionRequest
        ):
            request = contact_center_insights.TuneQaScorecardRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if filter is not None:
                request.filter = filter
            if validate_only is not None:
                request.validate_only = validate_only

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.tune_qa_scorecard_revision
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.TuneQaScorecardRevisionResponse,
            metadata_type=contact_center_insights.TuneQaScorecardRevisionMetadata,
        )

        # Done; return the response.
        return response

    def deploy_qa_scorecard_revision(
        self,
        request: Optional[
            Union[contact_center_insights.DeployQaScorecardRevisionRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecardRevision:
        r"""Deploy a QaScorecardRevision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_deploy_qa_scorecard_revision():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeployQaScorecardRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.deploy_qa_scorecard_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeployQaScorecardRevisionRequest, dict]):
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
            google.cloud.contact_center_insights_v1.types.QaScorecardRevision:
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
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.DeployQaScorecardRevisionRequest
        ):
            request = contact_center_insights.DeployQaScorecardRevisionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.deploy_qa_scorecard_revision
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def undeploy_qa_scorecard_revision(
        self,
        request: Optional[
            Union[contact_center_insights.UndeployQaScorecardRevisionRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.QaScorecardRevision:
        r"""Undeploy a QaScorecardRevision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_undeploy_qa_scorecard_revision():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.UndeployQaScorecardRevisionRequest(
                    name="name_value",
                )

                # Make the request
                response = client.undeploy_qa_scorecard_revision(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UndeployQaScorecardRevisionRequest, dict]):
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
            google.cloud.contact_center_insights_v1.types.QaScorecardRevision:
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
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.UndeployQaScorecardRevisionRequest
        ):
            request = contact_center_insights.UndeployQaScorecardRevisionRequest(
                request
            )

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.undeploy_qa_scorecard_revision
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_qa_scorecard_revision(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteQaScorecardRevisionRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Deletes a QaScorecardRevision.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_qa_scorecard_revision():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteQaScorecardRevisionRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_qa_scorecard_revision(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteQaScorecardRevisionRequest, dict]):
                The request object. The request to delete a
                QaScorecardRevision.
            name (str):
                Required. The name of the
                QaScorecardRevision to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.DeleteQaScorecardRevisionRequest
        ):
            request = contact_center_insights.DeleteQaScorecardRevisionRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.delete_qa_scorecard_revision
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def list_qa_scorecard_revisions(
        self,
        request: Optional[
            Union[contact_center_insights.ListQaScorecardRevisionsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListQaScorecardRevisionsPager:
        r"""Lists all revisions under the parent QaScorecard.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_qa_scorecard_revisions():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListQaScorecardRevisionsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_qa_scorecard_revisions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListQaScorecardRevisionsRequest, dict]):
                The request object. Request to list QaScorecardRevisions
            parent (str):
                Required. The parent resource of the
                scorecard revisions. To list all
                revisions of all scorecards, substitute
                the QaScorecard ID with a '-' character.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListQaScorecardRevisionsPager:
                The response from a
                ListQaScorecardRevisions request.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.ListQaScorecardRevisionsRequest
        ):
            request = contact_center_insights.ListQaScorecardRevisionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.list_qa_scorecard_revisions
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListQaScorecardRevisionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def create_feedback_label(
        self,
        request: Optional[
            Union[contact_center_insights.CreateFeedbackLabelRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        feedback_label: Optional[resources.FeedbackLabel] = None,
        feedback_label_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.FeedbackLabel:
        r"""Create feedback label.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_create_feedback_label():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                feedback_label = contact_center_insights_v1.FeedbackLabel()
                feedback_label.label = "label_value"

                request = contact_center_insights_v1.CreateFeedbackLabelRequest(
                    parent="parent_value",
                    feedback_label=feedback_label,
                )

                # Make the request
                response = client.create_feedback_label(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.CreateFeedbackLabelRequest, dict]):
                The request object. The request for creating a feedback
                label.
            parent (str):
                Required. The parent resource of the
                feedback label.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            feedback_label (google.cloud.contact_center_insights_v1.types.FeedbackLabel):
                Required. The feedback label to
                create.

                This corresponds to the ``feedback_label`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            feedback_label_id (str):
                Optional. The ID of the feedback
                label to create. If one is not specified
                it will be generated by the server.

                This corresponds to the ``feedback_label_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.FeedbackLabel:
                Represents a conversation, resource,
                and label provided by the user.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, feedback_label, feedback_label_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.CreateFeedbackLabelRequest):
            request = contact_center_insights.CreateFeedbackLabelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if feedback_label is not None:
                request.feedback_label = feedback_label
            if feedback_label_id is not None:
                request.feedback_label_id = feedback_label_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_feedback_label]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def list_feedback_labels(
        self,
        request: Optional[
            Union[contact_center_insights.ListFeedbackLabelsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListFeedbackLabelsPager:
        r"""List feedback labels.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_feedback_labels():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListFeedbackLabelsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_feedback_labels(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListFeedbackLabelsRequest, dict]):
                The request object. The request for listing feedback
                labels.
            parent (str):
                Required. The parent resource of the
                feedback labels.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListFeedbackLabelsPager:
                The response for listing feedback
                labels.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.ListFeedbackLabelsRequest):
            request = contact_center_insights.ListFeedbackLabelsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_feedback_labels]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListFeedbackLabelsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def get_feedback_label(
        self,
        request: Optional[
            Union[contact_center_insights.GetFeedbackLabelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.FeedbackLabel:
        r"""Get feedback label.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_get_feedback_label():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.GetFeedbackLabelRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_feedback_label(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.GetFeedbackLabelRequest, dict]):
                The request object. The request for getting a feedback
                label.
            name (str):
                Required. The name of the feedback
                label to get.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.FeedbackLabel:
                Represents a conversation, resource,
                and label provided by the user.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.GetFeedbackLabelRequest):
            request = contact_center_insights.GetFeedbackLabelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_feedback_label]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_feedback_label(
        self,
        request: Optional[
            Union[contact_center_insights.UpdateFeedbackLabelRequest, dict]
        ] = None,
        *,
        feedback_label: Optional[resources.FeedbackLabel] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> resources.FeedbackLabel:
        r"""Update feedback label.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_update_feedback_label():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                feedback_label = contact_center_insights_v1.FeedbackLabel()
                feedback_label.label = "label_value"

                request = contact_center_insights_v1.UpdateFeedbackLabelRequest(
                    feedback_label=feedback_label,
                )

                # Make the request
                response = client.update_feedback_label(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.UpdateFeedbackLabelRequest, dict]):
                The request object. The request for updating a feedback
                label.
            feedback_label (google.cloud.contact_center_insights_v1.types.FeedbackLabel):
                Required. The feedback label to
                update.

                This corresponds to the ``feedback_label`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The list of fields to be
                updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.types.FeedbackLabel:
                Represents a conversation, resource,
                and label provided by the user.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [feedback_label, update_mask]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.UpdateFeedbackLabelRequest):
            request = contact_center_insights.UpdateFeedbackLabelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if feedback_label is not None:
                request.feedback_label = feedback_label
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_feedback_label]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("feedback_label.name", request.feedback_label.name),)
            ),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def delete_feedback_label(
        self,
        request: Optional[
            Union[contact_center_insights.DeleteFeedbackLabelRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Delete feedback label.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_delete_feedback_label():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.DeleteFeedbackLabelRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_feedback_label(request=request)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.DeleteFeedbackLabelRequest, dict]):
                The request object. The request for deleting a feedback
                label.
            name (str):
                Required. The name of the feedback
                label to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, contact_center_insights.DeleteFeedbackLabelRequest):
            request = contact_center_insights.DeleteFeedbackLabelRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.delete_feedback_label]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    def list_all_feedback_labels(
        self,
        request: Optional[
            Union[contact_center_insights.ListAllFeedbackLabelsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListAllFeedbackLabelsPager:
        r"""List all feedback labels by project number.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_list_all_feedback_labels():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                request = contact_center_insights_v1.ListAllFeedbackLabelsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_all_feedback_labels(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.ListAllFeedbackLabelsRequest, dict]):
                The request object. The request for listing all feedback
                labels.
            parent (str):
                Required. The parent resource of all
                feedback labels per project.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.contact_center_insights_v1.services.contact_center_insights.pagers.ListAllFeedbackLabelsPager:
                The response for listing all feedback
                labels.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.ListAllFeedbackLabelsRequest
        ):
            request = contact_center_insights.ListAllFeedbackLabelsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_all_feedback_labels]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__iter__` convenience method.
        response = pagers.ListAllFeedbackLabelsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def bulk_upload_feedback_labels(
        self,
        request: Optional[
            Union[contact_center_insights.BulkUploadFeedbackLabelsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Upload feedback labels in bulk.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_bulk_upload_feedback_labels():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                gcs_source = contact_center_insights_v1.GcsSource()
                gcs_source.format_ = "JSON"
                gcs_source.object_uri = "object_uri_value"

                request = contact_center_insights_v1.BulkUploadFeedbackLabelsRequest(
                    gcs_source=gcs_source,
                    parent="parent_value",
                )

                # Make the request
                operation = client.bulk_upload_feedback_labels(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsRequest, dict]):
                The request object. The request for bulk uploading
                feedback labels.
            parent (str):
                Required. The parent resource for new
                feedback labels.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.BulkUploadFeedbackLabelsResponse`
                Response for the Bulk Upload Feedback Labels API.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.BulkUploadFeedbackLabelsRequest
        ):
            request = contact_center_insights.BulkUploadFeedbackLabelsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.bulk_upload_feedback_labels
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.BulkUploadFeedbackLabelsResponse,
            metadata_type=contact_center_insights.BulkUploadFeedbackLabelsMetadata,
        )

        # Done; return the response.
        return response

    def bulk_download_feedback_labels(
        self,
        request: Optional[
            Union[contact_center_insights.BulkDownloadFeedbackLabelsRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operation.Operation:
        r"""Download feedback labels in bulk.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contact_center_insights_v1

            def sample_bulk_download_feedback_labels():
                # Create a client
                client = contact_center_insights_v1.ContactCenterInsightsClient()

                # Initialize request argument(s)
                gcs_destination = contact_center_insights_v1.GcsDestination()
                gcs_destination.format_ = "JSON"
                gcs_destination.object_uri = "object_uri_value"

                request = contact_center_insights_v1.BulkDownloadFeedbackLabelsRequest(
                    gcs_destination=gcs_destination,
                    parent="parent_value",
                )

                # Make the request
                operation = client.bulk_download_feedback_labels(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsRequest, dict]):
                The request object. Request for the
                BulkDownloadFeedbackLabel endpoint.
            parent (str):
                Required. The parent resource for new
                feedback labels.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.api_core.operation.Operation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.contact_center_insights_v1.types.BulkDownloadFeedbackLabelsResponse`
                Response for the BulkDownloadFeedbackLabel endpoint.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(
            request, contact_center_insights.BulkDownloadFeedbackLabelsRequest
        ):
            request = contact_center_insights.BulkDownloadFeedbackLabelsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.bulk_download_feedback_labels
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation.from_gapic(
            response,
            self._transport.operations_client,
            contact_center_insights.BulkDownloadFeedbackLabelsResponse,
            metadata_type=contact_center_insights.BulkDownloadFeedbackLabelsMetadata,
        )

        # Done; return the response.
        return response

    def __enter__(self) -> "ContactCenterInsightsClient":
        return self

    def __exit__(self, type, value, traceback):
        """Releases underlying transport's resources.

        .. warning::
            ONLY use as a context manager if the transport is NOT shared
            with other clients! Exiting the with block will CLOSE the transport
            and may cause errors in other clients!
        """
        self.transport.close()

    def list_operations(
        self,
        request: Optional[Union[operations_pb2.ListOperationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.ListOperationsResponse:
        r"""Lists operations that match the specified filter in the request.

        Args:
            request (:class:`~.operations_pb2.ListOperationsRequest`):
                The request object. Request message for
                `ListOperations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.ListOperationsResponse:
                Response message for ``ListOperations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.ListOperationsRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.ListOperationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_operations]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e

    def get_operation(
        self,
        request: Optional[Union[operations_pb2.GetOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> operations_pb2.Operation:
        r"""Gets the latest state of a long-running operation.

        Args:
            request (:class:`~.operations_pb2.GetOperationRequest`):
                The request object. Request message for
                `GetOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.operations_pb2.Operation:
                An ``Operation`` object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.GetOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.GetOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        try:
            # Send the request.
            response = rpc(
                request_pb,
                retry=retry,
                timeout=timeout,
                metadata=metadata,
            )

            # Done; return the response.
            return response
        except core_exceptions.GoogleAPICallError as e:
            self._add_cred_info_for_auth_errors(e)
            raise e

    def cancel_operation(
        self,
        request: Optional[Union[operations_pb2.CancelOperationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> None:
        r"""Starts asynchronous cancellation on a long-running operation.

        The server makes a best effort to cancel the operation, but success
        is not guaranteed.  If the server doesn't support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.

        Args:
            request (:class:`~.operations_pb2.CancelOperationRequest`):
                The request object. Request message for
                `CancelOperation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                    if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            None
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = operations_pb2.CancelOperationRequest()
        elif isinstance(request, dict):
            request_pb = operations_pb2.CancelOperationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.cancel_operation]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request_pb.name),)),
        )

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        rpc(
            request_pb,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

__all__ = ("ContactCenterInsightsClient",)
