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

from google.cloud.dialogflow_v2beta1 import gapic_version as package_version
from google.cloud.dialogflow_v2beta1._compat import (
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

import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.dialogflow_v2beta1.services.conversations import pagers
from google.cloud.dialogflow_v2beta1.types import (
    conversation,
    conversation_profile,
    generator,
    participant,
)
from google.cloud.dialogflow_v2beta1.types import conversation as gcd_conversation

from .transports.base import DEFAULT_CLIENT_INFO, ConversationsTransport
from .transports.grpc import ConversationsGrpcTransport
from .transports.grpc_asyncio import ConversationsGrpcAsyncIOTransport
from .transports.rest import ConversationsRestTransport


class ConversationsClientMeta(type):
    """Metaclass for the Conversations client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[ConversationsTransport]]
    _transport_registry["grpc"] = ConversationsGrpcTransport
    _transport_registry["grpc_asyncio"] = ConversationsGrpcAsyncIOTransport
    _transport_registry["rest"] = ConversationsRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[ConversationsTransport]:
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


class ConversationsClient(metaclass=ConversationsClientMeta):
    """Service for managing
    [Conversations][google.cloud.dialogflow.v2beta1.Conversation].
    """

    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = "dialogflow.googleapis.com"
    DEFAULT_MTLS_ENDPOINT = get_default_mtls_endpoint(DEFAULT_ENDPOINT)

    _DEFAULT_ENDPOINT_TEMPLATE = "dialogflow.{UNIVERSE_DOMAIN}"
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
            ConversationsClient: The constructed client.
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
            ConversationsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ConversationsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ConversationsTransport: The transport used by the client
                instance.
        """
        return self._transport

    @staticmethod
    def agent_path(
        project: str,
    ) -> str:
        """Returns a fully-qualified agent string."""
        return "projects/{project}/agent".format(
            project=project,
        )

    @staticmethod
    def parse_agent_path(path: str) -> Dict[str, str]:
        """Parses a agent path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/agent$", path)
        return m.groupdict() if m else {}

    @staticmethod
    def answer_record_path(
        project: str,
        answer_record: str,
    ) -> str:
        """Returns a fully-qualified answer_record string."""
        return "projects/{project}/answerRecords/{answer_record}".format(
            project=project,
            answer_record=answer_record,
        )

    @staticmethod
    def parse_answer_record_path(path: str) -> Dict[str, str]:
        """Parses a answer_record path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/answerRecords/(?P<answer_record>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def app_path(
        project: str,
        location: str,
        app: str,
    ) -> str:
        """Returns a fully-qualified app string."""
        return "projects/{project}/locations/{location}/apps/{app}".format(
            project=project,
            location=location,
            app=app,
        )

    @staticmethod
    def parse_app_path(path: str) -> Dict[str, str]:
        """Parses a app path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/apps/(?P<app>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def ces_tool_path(
        project: str,
        location: str,
        app: str,
        tool: str,
    ) -> str:
        """Returns a fully-qualified ces_tool string."""
        return "projects/{project}/locations/{location}/apps/{app}/tools/{tool}".format(
            project=project,
            location=location,
            app=app,
            tool=tool,
        )

    @staticmethod
    def parse_ces_tool_path(path: str) -> Dict[str, str]:
        """Parses a ces_tool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/apps/(?P<app>.+?)/tools/(?P<tool>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def companion_agent_path(
        project: str,
        location: str,
        companion_agent: str,
    ) -> str:
        """Returns a fully-qualified companion_agent string."""
        return "projects/{project}/locations/{location}/companionAgents/{companion_agent}".format(
            project=project,
            location=location,
            companion_agent=companion_agent,
        )

    @staticmethod
    def parse_companion_agent_path(path: str) -> Dict[str, str]:
        """Parses a companion_agent path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/companionAgents/(?P<companion_agent>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def conversation_path(
        project: str,
        conversation: str,
    ) -> str:
        """Returns a fully-qualified conversation string."""
        return "projects/{project}/conversations/{conversation}".format(
            project=project,
            conversation=conversation,
        )

    @staticmethod
    def parse_conversation_path(path: str) -> Dict[str, str]:
        """Parses a conversation path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversations/(?P<conversation>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def conversation_profile_path(
        project: str,
        conversation_profile: str,
    ) -> str:
        """Returns a fully-qualified conversation_profile string."""
        return "projects/{project}/conversationProfiles/{conversation_profile}".format(
            project=project,
            conversation_profile=conversation_profile,
        )

    @staticmethod
    def parse_conversation_profile_path(path: str) -> Dict[str, str]:
        """Parses a conversation_profile path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversationProfiles/(?P<conversation_profile>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def cx_security_settings_path(
        project: str,
        location: str,
        security_settings: str,
    ) -> str:
        """Returns a fully-qualified cx_security_settings string."""
        return "projects/{project}/locations/{location}/securitySettings/{security_settings}".format(
            project=project,
            location=location,
            security_settings=security_settings,
        )

    @staticmethod
    def parse_cx_security_settings_path(path: str) -> Dict[str, str]:
        """Parses a cx_security_settings path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/securitySettings/(?P<security_settings>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def data_store_path(
        project: str,
        location: str,
        collection: str,
        data_store: str,
    ) -> str:
        """Returns a fully-qualified data_store string."""
        return "projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}".format(
            project=project,
            location=location,
            collection=collection,
            data_store=data_store,
        )

    @staticmethod
    def parse_data_store_path(path: str) -> Dict[str, str]:
        """Parses a data_store path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/collections/(?P<collection>.+?)/dataStores/(?P<data_store>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def document_path(
        project: str,
        knowledge_base: str,
        document: str,
    ) -> str:
        """Returns a fully-qualified document string."""
        return "projects/{project}/knowledgeBases/{knowledge_base}/documents/{document}".format(
            project=project,
            knowledge_base=knowledge_base,
            document=document,
        )

    @staticmethod
    def parse_document_path(path: str) -> Dict[str, str]:
        """Parses a document path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/knowledgeBases/(?P<knowledge_base>.+?)/documents/(?P<document>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def generator_path(
        project: str,
        location: str,
        generator: str,
    ) -> str:
        """Returns a fully-qualified generator string."""
        return "projects/{project}/locations/{location}/generators/{generator}".format(
            project=project,
            location=location,
            generator=generator,
        )

    @staticmethod
    def parse_generator_path(path: str) -> Dict[str, str]:
        """Parses a generator path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/generators/(?P<generator>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def knowledge_base_path(
        project: str,
        knowledge_base: str,
    ) -> str:
        """Returns a fully-qualified knowledge_base string."""
        return "projects/{project}/knowledgeBases/{knowledge_base}".format(
            project=project,
            knowledge_base=knowledge_base,
        )

    @staticmethod
    def parse_knowledge_base_path(path: str) -> Dict[str, str]:
        """Parses a knowledge_base path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/knowledgeBases/(?P<knowledge_base>.+?)$", path
        )
        return m.groupdict() if m else {}

    @staticmethod
    def message_path(
        project: str,
        conversation: str,
        message: str,
    ) -> str:
        """Returns a fully-qualified message string."""
        return (
            "projects/{project}/conversations/{conversation}/messages/{message}".format(
                project=project,
                conversation=conversation,
                message=message,
            )
        )

    @staticmethod
    def parse_message_path(path: str) -> Dict[str, str]:
        """Parses a message path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/conversations/(?P<conversation>.+?)/messages/(?P<message>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def phrase_set_path(
        project: str,
        location: str,
        phrase_set: str,
    ) -> str:
        """Returns a fully-qualified phrase_set string."""
        return "projects/{project}/locations/{location}/phraseSets/{phrase_set}".format(
            project=project,
            location=location,
            phrase_set=phrase_set,
        )

    @staticmethod
    def parse_phrase_set_path(path: str) -> Dict[str, str]:
        """Parses a phrase_set path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/phraseSets/(?P<phrase_set>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def tool_path(
        project: str,
        location: str,
        tool: str,
    ) -> str:
        """Returns a fully-qualified tool string."""
        return "projects/{project}/locations/{location}/tools/{tool}".format(
            project=project,
            location=location,
            tool=tool,
        )

    @staticmethod
    def parse_tool_path(path: str) -> Dict[str, str]:
        """Parses a tool path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/tools/(?P<tool>.+?)$",
            path,
        )
        return m.groupdict() if m else {}

    @staticmethod
    def toolset_path(
        project: str,
        location: str,
        app: str,
        toolset: str,
    ) -> str:
        """Returns a fully-qualified toolset string."""
        return "projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}".format(
            project=project,
            location=location,
            app=app,
            toolset=toolset,
        )

    @staticmethod
    def parse_toolset_path(path: str) -> Dict[str, str]:
        """Parses a toolset path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/locations/(?P<location>.+?)/apps/(?P<app>.+?)/toolsets/(?P<toolset>.+?)$",
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
            Union[str, ConversationsTransport, Callable[..., ConversationsTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the conversations client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ConversationsTransport,Callable[..., ConversationsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ConversationsTransport constructor.
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
        self._client_cert_source = ConversationsClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=ConversationsClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, ConversationsTransport)
        if transport_provided:
            # transport is a ConversationsTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(ConversationsTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=ConversationsClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=ConversationsClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=ConversationsClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[ConversationsTransport], Callable[..., ConversationsTransport]
            ] = (
                ConversationsClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., ConversationsTransport], transport)
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
                    "Created client `google.cloud.dialogflow_v2beta1.ConversationsClient`.",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
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
                        "serviceName": "google.cloud.dialogflow.v2beta1.Conversations",
                        "credentialsType": None,
                    },
                )

    def create_conversation(
        self,
        request: Optional[
            Union[gcd_conversation.CreateConversationRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        conversation: Optional[gcd_conversation.Conversation] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation.Conversation:
        r"""Creates a new conversation. Conversations are auto-completed
        after 24 hours.

        Conversation Lifecycle: There are two stages during a
        conversation: Automated Agent Stage and Assist Stage.

        For Automated Agent Stage, there will be a dialogflow agent
        responding to user queries.

        For Assist Stage, there's no dialogflow agent responding to user
        queries. But we will provide suggestions which are generated
        from conversation.

        If
        [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile]
        is configured for a dialogflow agent, conversation will start
        from ``Automated Agent Stage``, otherwise, it will start from
        ``Assist Stage``. And during ``Automated Agent Stage``, once an
        [Intent][google.cloud.dialogflow.v2beta1.Intent] with
        [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff]
        is triggered, conversation will transfer to Assist Stage.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_create_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                conversation = dialogflow_v2beta1.Conversation()
                conversation.conversation_profile = "conversation_profile_value"

                request = dialogflow_v2beta1.CreateConversationRequest(
                    parent="parent_value",
                    conversation=conversation,
                )

                # Make the request
                response = client.create_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CreateConversationRequest, dict]):
                The request object. The request message for
                [Conversations.CreateConversation][google.cloud.dialogflow.v2beta1.Conversations.CreateConversation].
            parent (str):
                Required. Resource identifier of the project creating
                the conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            conversation (google.cloud.dialogflow_v2beta1.types.Conversation):
                Required. The conversation to create.
                This corresponds to the ``conversation`` field
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
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, conversation]
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
        if not isinstance(request, gcd_conversation.CreateConversationRequest):
            request = gcd_conversation.CreateConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if conversation is not None:
                request.conversation = conversation

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

    def list_conversations(
        self,
        request: Optional[Union[conversation.ListConversationsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListConversationsPager:
        r"""Returns the list of all conversations in the
        specified project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_list_conversations():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListConversationsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_conversations(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListConversationsRequest, dict]):
                The request object. The request message for
                [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].
            parent (str):
                Required. The project from which to list all
                conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>``.

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
            google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListConversationsPager:
                The response message for
                   [Conversations.ListConversations][google.cloud.dialogflow.v2beta1.Conversations.ListConversations].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
        if not isinstance(request, conversation.ListConversationsRequest):
            request = conversation.ListConversationsRequest(request)
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

    def get_conversation(
        self,
        request: Optional[Union[conversation.GetConversationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.Conversation:
        r"""Retrieves the specific conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_get_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GetConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GetConversationRequest, dict]):
                The request object. The request message for
                [Conversations.GetConversation][google.cloud.dialogflow.v2beta1.Conversations.GetConversation].
            name (str):
                Required. The name of the conversation. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

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
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

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
        if not isinstance(request, conversation.GetConversationRequest):
            request = conversation.GetConversationRequest(request)
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

    def complete_conversation(
        self,
        request: Optional[Union[conversation.CompleteConversationRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.Conversation:
        r"""Completes the specified conversation. Finished
        conversations are purged from the database after 30
        days.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_complete_conversation():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CompleteConversationRequest(
                    name="name_value",
                )

                # Make the request
                response = client.complete_conversation(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CompleteConversationRequest, dict]):
                The request object. The request message for
                [Conversations.CompleteConversation][google.cloud.dialogflow.v2beta1.Conversations.CompleteConversation].
            name (str):
                Required. Resource identifier of the conversation to
                close. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

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
            google.cloud.dialogflow_v2beta1.types.Conversation:
                Represents a conversation.
                A conversation is an interaction between
                an agent, including live agents and
                Dialogflow agents, and a support
                customer. Conversations can include
                phone calls and text-based chat
                sessions.

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
        if not isinstance(request, conversation.CompleteConversationRequest):
            request = conversation.CompleteConversationRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.complete_conversation]

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

    def ingest_context_references(
        self,
        request: Optional[
            Union[gcd_conversation.IngestContextReferencesRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        context_references: Optional[
            MutableMapping[str, gcd_conversation.Conversation.ContextReference]
        ] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation.IngestContextReferencesResponse:
        r"""Data ingestion API.
        Ingests context references for an existing conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_ingest_context_references():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.IngestContextReferencesRequest(
                    conversation="conversation_value",
                )

                # Make the request
                response = client.ingest_context_references(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.IngestContextReferencesRequest, dict]):
                The request object. The request message for
                [ConversationsService.IngestContextReferences][].
            conversation (str):
                Required. Resource identifier of the conversation to
                ingest context information for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``conversation`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            context_references (MutableMapping[str, google.cloud.dialogflow_v2beta1.types.Conversation.ContextReference]):
                Required. The context references to
                ingest. The key is the name of the
                context reference and the value contains
                the contents of the context reference.
                The key is used to incorporate ingested
                context references to enhance the
                generator.

                This corresponds to the ``context_references`` field
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
            google.cloud.dialogflow_v2beta1.types.IngestContextReferencesResponse:
                The response message for
                [ConversationsService.IngestContextReferences][].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation, context_references]
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
        if not isinstance(request, gcd_conversation.IngestContextReferencesRequest):
            request = gcd_conversation.IngestContextReferencesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if conversation is not None:
                request.conversation = conversation
            if context_references is not None:
                request.context_references = context_references

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.ingest_context_references
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

    def batch_create_messages(
        self,
        request: Optional[Union[conversation.BatchCreateMessagesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        requests: Optional[MutableSequence[conversation.CreateMessageRequest]] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.BatchCreateMessagesResponse:
        r"""Batch ingests messages to conversation. Customers can
        use this RPC to ingest historical messages to
        conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_batch_create_messages():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                requests = dialogflow_v2beta1.CreateMessageRequest()
                requests.parent = "parent_value"

                request = dialogflow_v2beta1.BatchCreateMessagesRequest(
                    parent="parent_value",
                    requests=requests,
                )

                # Make the request
                response = client.batch_create_messages(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesRequest, dict]):
                The request object. The request message for
                [Conversations.BatchCreateMessagesRequest][].
            parent (str):
                Required. Resource identifier of the conversation to
                create message. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            requests (MutableSequence[google.cloud.dialogflow_v2beta1.types.CreateMessageRequest]):
                Required. A maximum of 300 messages can be created in a
                batch. [CreateMessageRequest.message.send_time][] is
                required. All created messages will have identical
                [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].

                This corresponds to the ``requests`` field
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
            google.cloud.dialogflow_v2beta1.types.BatchCreateMessagesResponse:
                The request message for
                [Conversations.BatchCreateMessagesResponse][].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, requests]
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
        if not isinstance(request, conversation.BatchCreateMessagesRequest):
            request = conversation.BatchCreateMessagesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if requests is not None:
                request.requests = requests

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.batch_create_messages]

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

    def list_messages(
        self,
        request: Optional[Union[conversation.ListMessagesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListMessagesPager:
        r"""Lists messages that belong to a given conversation. ``messages``
        are ordered by ``create_time`` in descending order. To fetch
        updates without duplication, send request with filter
        ``create_time_epoch_microseconds > [first item's create_time of previous request]``
        and empty page_token.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_list_messages():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListMessagesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_messages(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListMessagesRequest, dict]):
                The request object. The request message for
                [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].
            parent (str):
                Required. The name of the conversation to list messages
                for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``

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
            google.cloud.dialogflow_v2beta1.services.conversations.pagers.ListMessagesPager:
                The response message for
                   [Conversations.ListMessages][google.cloud.dialogflow.v2beta1.Conversations.ListMessages].

                Iterating over this object will yield results and
                resolve additional pages automatically.

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
        if not isinstance(request, conversation.ListMessagesRequest):
            request = conversation.ListMessagesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_messages]

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
        response = pagers.ListMessagesPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def suggest_conversation_summary(
        self,
        request: Optional[
            Union[gcd_conversation.SuggestConversationSummaryRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_conversation.SuggestConversationSummaryResponse:
        r"""Suggest summary for a conversation based on specific
        historical messages. The range of the messages to be
        used for summary can be specified in the request.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_suggest_conversation_summary():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestConversationSummaryRequest(
                    conversation="conversation_value",
                )

                # Make the request
                response = client.suggest_conversation_summary(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryRequest, dict]):
                The request object. The request message for
                [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].
            conversation (str):
                Required. The conversation to fetch suggestion for.
                Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``conversation`` field
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
            google.cloud.dialogflow_v2beta1.types.SuggestConversationSummaryResponse:
                The response message for
                   [Conversations.SuggestConversationSummary][google.cloud.dialogflow.v2beta1.Conversations.SuggestConversationSummary].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation]
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
        if not isinstance(request, gcd_conversation.SuggestConversationSummaryRequest):
            request = gcd_conversation.SuggestConversationSummaryRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if conversation is not None:
                request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.suggest_conversation_summary
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

    def generate_stateless_summary(
        self,
        request: Optional[
            Union[conversation.GenerateStatelessSummaryRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.GenerateStatelessSummaryResponse:
        r"""Generates and returns a summary for a conversation
        that does not have a resource created for it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_generate_stateless_summary():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                stateless_conversation = dialogflow_v2beta1.MinimalConversation()
                stateless_conversation.parent = "parent_value"

                conversation_profile = dialogflow_v2beta1.ConversationProfile()
                conversation_profile.display_name = "display_name_value"

                request = dialogflow_v2beta1.GenerateStatelessSummaryRequest(
                    stateless_conversation=stateless_conversation,
                    conversation_profile=conversation_profile,
                )

                # Make the request
                response = client.generate_stateless_summary(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryRequest, dict]):
                The request object. The request message for
                [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.GenerateStatelessSummaryResponse:
                The response message for
                   [Conversations.GenerateStatelessSummary][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSummary].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, conversation.GenerateStatelessSummaryRequest):
            request = conversation.GenerateStatelessSummaryRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_stateless_summary
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (
                    (
                        "stateless_conversation.parent",
                        request.stateless_conversation.parent,
                    ),
                )
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

    def generate_stateless_suggestion(
        self,
        request: Optional[
            Union[conversation.GenerateStatelessSuggestionRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.GenerateStatelessSuggestionResponse:
        r"""Generates and returns a suggestion for a conversation
        that does not have a resource created for it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_generate_stateless_suggestion():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                generator = dialogflow_v2beta1.Generator()
                generator.published_model = "published_model_value"

                request = dialogflow_v2beta1.GenerateStatelessSuggestionRequest(
                    generator=generator,
                    parent="parent_value",
                )

                # Make the request
                response = client.generate_stateless_suggestion(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionRequest, dict]):
                The request object. The request message for
                [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.GenerateStatelessSuggestionResponse:
                The response message for
                   [Conversations.GenerateStatelessSuggestion][google.cloud.dialogflow.v2beta1.Conversations.GenerateStatelessSuggestion].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, conversation.GenerateStatelessSuggestionRequest):
            request = conversation.GenerateStatelessSuggestionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.generate_stateless_suggestion
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

    def search_knowledge(
        self,
        request: Optional[Union[conversation.SearchKnowledgeRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> conversation.SearchKnowledgeResponse:
        r"""Get answers for the given query based on knowledge
        documents.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_search_knowledge():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SearchKnowledgeRequest(
                    parent="parent_value",
                    conversation_profile="conversation_profile_value",
                    session_id="session_id_value",
                )

                # Make the request
                response = client.search_knowledge(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SearchKnowledgeRequest, dict]):
                The request object. The request message for
                [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.SearchKnowledgeResponse:
                The response message for
                   [Conversations.SearchKnowledge][google.cloud.dialogflow.v2beta1.Conversations.SearchKnowledge].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, conversation.SearchKnowledgeRequest):
            request = conversation.SearchKnowledgeRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.search_knowledge]

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

    def generate_suggestions(
        self,
        request: Optional[
            Union[gcd_conversation.GenerateSuggestionsRequest, dict]
        ] = None,
        *,
        conversation: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.GenerateSuggestionsResponse:
        r"""Generates all the suggestions using generators
        configured in the conversation profile. A generator is
        used only if its trigger event is matched.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_generate_suggestions():
                # Create a client
                client = dialogflow_v2beta1.ConversationsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GenerateSuggestionsRequest(
                    conversation="conversation_value",
                )

                # Make the request
                response = client.generate_suggestions(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsRequest, dict]):
                The request object. The request message for
                [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].
            conversation (str):
                Required. The conversation for which the suggestions are
                generated. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                The conversation must be created with a conversation
                profile which has generators configured in it to be able
                to get suggestions.

                This corresponds to the ``conversation`` field
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
            google.cloud.dialogflow_v2beta1.types.GenerateSuggestionsResponse:
                The response message for
                   [Conversations.GenerateSuggestions][google.cloud.dialogflow.v2beta1.Conversations.GenerateSuggestions].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [conversation]
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
        if not isinstance(request, gcd_conversation.GenerateSuggestionsRequest):
            request = gcd_conversation.GenerateSuggestionsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if conversation is not None:
                request.conversation = conversation

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.generate_suggestions]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("conversation", request.conversation),)
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

    def __enter__(self) -> "ConversationsClient":
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

    def get_location(
        self,
        request: Optional[Union[locations_pb2.GetLocationRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.Location:
        r"""Gets information about a location.

        Args:
            request (:class:`~.location_pb2.GetLocationRequest`):
                The request object. Request message for
                `GetLocation` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.Location:
                Location object.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.GetLocationRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.GetLocationRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_location]

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

    def list_locations(
        self,
        request: Optional[Union[locations_pb2.ListLocationsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> locations_pb2.ListLocationsResponse:
        r"""Lists information about the supported locations for this service.

        Args:
            request (:class:`~.location_pb2.ListLocationsRequest`):
                The request object. Request message for
                `ListLocations` method.
            retry (google.api_core.retry.Retry): Designation of what errors,
                 if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        Returns:
            ~.location_pb2.ListLocationsResponse:
                Response message for ``ListLocations`` method.
        """
        # Create or coerce a protobuf request object.
        # The request isn't a proto-plus wrapped type,
        # so it must be constructed via keyword expansion.
        if request is None:
            request_pb = locations_pb2.ListLocationsRequest()
        elif isinstance(request, dict):
            request_pb = locations_pb2.ListLocationsRequest(**request)
        else:
            request_pb = request

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_locations]

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


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__

__all__ = ("ConversationsClient",)
