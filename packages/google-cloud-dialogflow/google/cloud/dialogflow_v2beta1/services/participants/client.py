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
    Iterable,
    Iterator,
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

import google.protobuf.field_mask_pb2 as field_mask_pb2  # type: ignore
import google.protobuf.timestamp_pb2 as timestamp_pb2  # type: ignore
import google.rpc.status_pb2 as status_pb2  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore

from google.cloud.dialogflow_v2beta1.services.participants import pagers
from google.cloud.dialogflow_v2beta1.types import participant, session
from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant

from .transports.base import DEFAULT_CLIENT_INFO, ParticipantsTransport
from .transports.grpc import ParticipantsGrpcTransport
from .transports.grpc_asyncio import ParticipantsGrpcAsyncIOTransport
from .transports.rest import ParticipantsRestTransport


class ParticipantsClientMeta(type):
    """Metaclass for the Participants client.

    This provides class-level methods for building and retrieving
    support objects (e.g. transport) without polluting the client instance
    objects.
    """

    _transport_registry = OrderedDict()  # type: Dict[str, Type[ParticipantsTransport]]
    _transport_registry["grpc"] = ParticipantsGrpcTransport
    _transport_registry["grpc_asyncio"] = ParticipantsGrpcAsyncIOTransport
    _transport_registry["rest"] = ParticipantsRestTransport

    def get_transport_class(
        cls,
        label: Optional[str] = None,
    ) -> Type[ParticipantsTransport]:
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


class ParticipantsClient(metaclass=ParticipantsClientMeta):
    """Service for managing
    [Participants][google.cloud.dialogflow.v2beta1.Participant].
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
            ParticipantsClient: The constructed client.
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
            ParticipantsClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(filename)
        kwargs["credentials"] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    @property
    def transport(self) -> ParticipantsTransport:
        """Returns the transport used by the client instance.

        Returns:
            ParticipantsTransport: The transport used by the client
                instance.
        """
        return self._transport

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
    def context_path(
        project: str,
        session: str,
        context: str,
    ) -> str:
        """Returns a fully-qualified context string."""
        return "projects/{project}/agent/sessions/{session}/contexts/{context}".format(
            project=project,
            session=session,
            context=context,
        )

    @staticmethod
    def parse_context_path(path: str) -> Dict[str, str]:
        """Parses a context path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/agent/sessions/(?P<session>.+?)/contexts/(?P<context>.+?)$",
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
    def intent_path(
        project: str,
        intent: str,
    ) -> str:
        """Returns a fully-qualified intent string."""
        return "projects/{project}/agent/intents/{intent}".format(
            project=project,
            intent=intent,
        )

    @staticmethod
    def parse_intent_path(path: str) -> Dict[str, str]:
        """Parses a intent path into its component segments."""
        m = re.match(r"^projects/(?P<project>.+?)/agent/intents/(?P<intent>.+?)$", path)
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
    def session_entity_type_path(
        project: str,
        session: str,
        entity_type: str,
    ) -> str:
        """Returns a fully-qualified session_entity_type string."""
        return "projects/{project}/agent/sessions/{session}/entityTypes/{entity_type}".format(
            project=project,
            session=session,
            entity_type=entity_type,
        )

    @staticmethod
    def parse_session_entity_type_path(path: str) -> Dict[str, str]:
        """Parses a session_entity_type path into its component segments."""
        m = re.match(
            r"^projects/(?P<project>.+?)/agent/sessions/(?P<session>.+?)/entityTypes/(?P<entity_type>.+?)$",
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
            Union[str, ParticipantsTransport, Callable[..., ParticipantsTransport]]
        ] = None,
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the participants client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ParticipantsTransport,Callable[..., ParticipantsTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ParticipantsTransport constructor.
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
        self._client_cert_source = ParticipantsClient._get_client_cert_source(
            self._client_options.client_cert_source, self._use_client_cert
        )
        self._universe_domain = get_universe_domain(
            universe_domain_opt,
            self._universe_domain_env,
            default_universe=ParticipantsClient._DEFAULT_UNIVERSE,
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
        transport_provided = isinstance(transport, ParticipantsTransport)
        if transport_provided:
            # transport is a ParticipantsTransport instance.
            if credentials or self._client_options.credentials_file or api_key_value:
                raise ValueError(
                    "When providing a transport instance, "
                    "provide its credentials directly."
                )
            if self._client_options.scopes:
                raise ValueError(
                    "When providing a transport instance, provide its scopes directly."
                )
            self._transport = cast(ParticipantsTransport, transport)
            self._api_endpoint = self._transport.host

        self._api_endpoint = self._api_endpoint or get_api_endpoint(
            api_override=self._client_options.api_endpoint,
            universe_domain=self._universe_domain,
            default_universe=ParticipantsClient._DEFAULT_UNIVERSE,
            default_mtls_endpoint=ParticipantsClient.DEFAULT_MTLS_ENDPOINT,
            default_endpoint_template=ParticipantsClient._DEFAULT_ENDPOINT_TEMPLATE,
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
                Type[ParticipantsTransport], Callable[..., ParticipantsTransport]
            ] = (
                ParticipantsClient.get_transport_class(transport)
                if isinstance(transport, str) or transport is None
                else cast(Callable[..., ParticipantsTransport], transport)
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
                    "Created client `google.cloud.dialogflow_v2beta1.ParticipantsClient`.",
                    extra={
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
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
                        "serviceName": "google.cloud.dialogflow.v2beta1.Participants",
                        "credentialsType": None,
                    },
                )

    def create_participant(
        self,
        request: Optional[Union[gcd_participant.CreateParticipantRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        participant: Optional[gcd_participant.Participant] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_participant.Participant:
        r"""Creates a new participant in a conversation.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_create_participant():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CreateParticipantRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.create_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CreateParticipantRequest, dict]):
                The request object. The request message for
                [Participants.CreateParticipant][google.cloud.dialogflow.v2beta1.Participants.CreateParticipant].
            parent (str):
                Required. Resource identifier of the conversation adding
                the participant. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            participant (google.cloud.dialogflow_v2beta1.types.Participant):
                Required. The participant to create.
                This corresponds to the ``participant`` field
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
            google.cloud.dialogflow_v2beta1.types.Participant:
                Represents a conversation participant
                (human agent, virtual agent, end-user).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [parent, participant]
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
        if not isinstance(request, gcd_participant.CreateParticipantRequest):
            request = gcd_participant.CreateParticipantRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent
            if participant is not None:
                request.participant = participant

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.create_participant]

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

    def get_participant(
        self,
        request: Optional[Union[participant.GetParticipantRequest, dict]] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.Participant:
        r"""Retrieves a conversation participant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_get_participant():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GetParticipantRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GetParticipantRequest, dict]):
                The request object. The request message for
                [Participants.GetParticipant][google.cloud.dialogflow.v2beta1.Participants.GetParticipant].
            name (str):
                Required. The name of the participant. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

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
            google.cloud.dialogflow_v2beta1.types.Participant:
                Represents a conversation participant
                (human agent, virtual agent, end-user).

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
        if not isinstance(request, participant.GetParticipantRequest):
            request = participant.GetParticipantRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if name is not None:
                request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.get_participant]

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

    def list_participants(
        self,
        request: Optional[Union[participant.ListParticipantsRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListParticipantsPager:
        r"""Returns the list of all participants in the specified
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

            def sample_list_participants():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListParticipantsRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_participants(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListParticipantsRequest, dict]):
                The request object. The request message for
                [Participants.ListParticipants][google.cloud.dialogflow.v2beta1.Participants.ListParticipants].
            parent (str):
                Required. The conversation to list all participants
                from. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.

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
            google.cloud.dialogflow_v2beta1.services.participants.pagers.ListParticipantsPager:
                The response message for
                   [Participants.ListParticipants][google.cloud.dialogflow.v2beta1.Participants.ListParticipants].

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
        if not isinstance(request, participant.ListParticipantsRequest):
            request = participant.ListParticipantsRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_participants]

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
        response = pagers.ListParticipantsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def update_participant(
        self,
        request: Optional[Union[gcd_participant.UpdateParticipantRequest, dict]] = None,
        *,
        participant: Optional[gcd_participant.Participant] = None,
        update_mask: Optional[field_mask_pb2.FieldMask] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_participant.Participant:
        r"""Updates the specified participant.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_update_participant():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.UpdateParticipantRequest(
                )

                # Make the request
                response = client.update_participant(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.UpdateParticipantRequest, dict]):
                The request object. The request message for
                [Participants.UpdateParticipant][google.cloud.dialogflow.v2beta1.Participants.UpdateParticipant].
            participant (google.cloud.dialogflow_v2beta1.types.Participant):
                Required. The participant to update.
                This corresponds to the ``participant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (google.protobuf.field_mask_pb2.FieldMask):
                Required. The mask to specify which
                fields to update.

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
            google.cloud.dialogflow_v2beta1.types.Participant:
                Represents a conversation participant
                (human agent, virtual agent, end-user).

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [participant, update_mask]
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
        if not isinstance(request, gcd_participant.UpdateParticipantRequest):
            request = gcd_participant.UpdateParticipantRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if participant is not None:
                request.participant = participant
            if update_mask is not None:
                request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.update_participant]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("participant.name", request.participant.name),)
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

    def analyze_content(
        self,
        request: Optional[Union[gcd_participant.AnalyzeContentRequest, dict]] = None,
        *,
        participant: Optional[str] = None,
        text_input: Optional[session.TextInput] = None,
        audio_input: Optional[gcd_participant.AudioInput] = None,
        event_input: Optional[session.EventInput] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> gcd_participant.AnalyzeContentResponse:
        r"""Adds a text (chat, for example), or audio (phone recording, for
        example) message from a participant into the conversation.

        Note: Always use agent versions for production traffic sent to
        virtual agents. See `Versions and
        environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_analyze_content():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.AnalyzeContentRequest(
                    participant="participant_value",
                )

                # Make the request
                response = client.analyze_content(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.AnalyzeContentRequest, dict]):
                The request object. The request message for
                [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent].
            participant (str):
                Required. The name of the participant this text comes
                from. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

                This corresponds to the ``participant`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            text_input (google.cloud.dialogflow_v2beta1.types.TextInput):
                The natural language text to be
                processed.

                This corresponds to the ``text_input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            audio_input (google.cloud.dialogflow_v2beta1.types.AudioInput):
                The natural language speech audio to
                be processed.

                This corresponds to the ``audio_input`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            event_input (google.cloud.dialogflow_v2beta1.types.EventInput):
                An input event to send to Dialogflow.
                This corresponds to the ``event_input`` field
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
            google.cloud.dialogflow_v2beta1.types.AnalyzeContentResponse:
                The response message for
                   [Participants.AnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.AnalyzeContent].

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [participant, text_input, audio_input, event_input]
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
        if not isinstance(request, gcd_participant.AnalyzeContentRequest):
            request = gcd_participant.AnalyzeContentRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if participant is not None:
                request.participant = participant
            if text_input is not None:
                request.text_input = text_input
            if audio_input is not None:
                request.audio_input = audio_input
            if event_input is not None:
                request.event_input = event_input

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.analyze_content]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("participant", request.participant),)
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

    def streaming_analyze_content(
        self,
        requests: Optional[Iterator[participant.StreamingAnalyzeContentRequest]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Iterable[participant.StreamingAnalyzeContentResponse]:
        r"""Adds a text (e.g., chat) or audio (e.g., phone recording)
        message from a participant into the conversation. Note: This
        method is only available through the gRPC API (not REST).

        The top-level message sent to the client by the server is
        ``StreamingAnalyzeContentResponse``. Multiple response messages
        can be returned in order. The first one or more messages contain
        the ``recognition_result`` field. Each result represents a more
        complete transcript of what the user said. The next message
        contains the ``reply_text`` field, and potentially the
        ``reply_audio`` and/or the ``automated_agent_reply`` fields.

        Note: Always use agent versions for production traffic sent to
        virtual agents. See `Versions and
        environments <https://cloud.google.com/dialogflow/es/docs/agents-versions>`__.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_streaming_analyze_content():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                audio_config = dialogflow_v2beta1.InputAudioConfig()
                audio_config.audio_encoding = "AUDIO_ENCODING_ALAW"
                audio_config.sample_rate_hertz = 1817
                audio_config.language_code = "language_code_value"

                request = dialogflow_v2beta1.StreamingAnalyzeContentRequest(
                    audio_config=audio_config,
                    input_audio=b'input_audio_blob',
                    participant="participant_value",
                )

                # This method expects an iterator which contains
                # 'dialogflow_v2beta1.StreamingAnalyzeContentRequest' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = client.streaming_analyze_content(requests=request_generator())

                # Handle the response
                for response in stream:
                    print(response)

        Args:
            requests (Iterator[google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentRequest]):
                The request object iterator. The top-level message sent by the client to the
                [Participants.StreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent]
                method.

                Multiple request messages should be sent in order:

                1. The first message must contain
                   [participant][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.participant],
                   [config][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.config]
                   and optionally
                   [query_params][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.query_params].
                   If you want to receive an audio response, it should
                   also contain
                   [reply_audio_config][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.reply_audio_config].
                   The message must not contain
                   [input][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.input].

                2. If
                   [config][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.config]
                   in the first message was set to
                   [audio_config][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.audio_config],
                   all subsequent messages must contain
                   [input_audio][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.input_audio]
                   to continue with Speech recognition. If you decide to
                   rather analyze text input after you already started
                   Speech recognition, please send a message with
                   [StreamingAnalyzeContentRequest.input_text][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.input_text].

                   However, note that:

                   - Dialogflow will bill you for the audio so far.
                   - Dialogflow discards all Speech recognition results
                     in favor of the text input.

                3. If
                   [StreamingAnalyzeContentRequest.config][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.config]
                   in the first message was set to
                   [StreamingAnalyzeContentRequest.text_config][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.text_config],
                   then the second message must contain only
                   [input_text][google.cloud.dialogflow.v2beta1.StreamingAnalyzeContentRequest.input_text].
                   Moreover, you must not send more than two messages.

                After you sent all input, you must half-close or abort
                the request stream.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            Iterable[google.cloud.dialogflow_v2beta1.types.StreamingAnalyzeContentResponse]:
                The top-level message returned from the
                StreamingAnalyzeContent method.

                   Multiple response messages can be returned in order:

                   1. If the input was set to streaming audio, the first
                      one or more messages contain recognition_result.
                      Each recognition_result represents a more complete
                      transcript of what the user said. When a user
                      speaks multiple sentences, the API will emit
                      multiple messages where is_final = true. Each time
                      the system detects a distinct pause or completed
                      thought, it locks in that segment, marks it
                      is_final = true, and then immediately starts a new
                      recognition cycle for the next sentence on the
                      same stream.

                   2. In virtual agent stage: if
                      enable_partial_automated_agent_reply is true, the
                      following N (currently 1 <= N <= 4) messages
                      contain automated_agent_reply and optionally
                      reply_audio returned by the virtual agent. The
                      first (N-1) automated_agent_reply`s will have
                      \`automated_agent_reply_type set to PARTIAL. The
                      last automated_agent_reply has
                      automated_agent_reply_type set to FINAL. If
                      enable_partial_automated_agent_reply is not
                      enabled, response stream only contains the final
                      reply.

                      In human assist stage: the following N (N >= 1)
                      messages contain human_agent_suggestion_results,
                      end_user_suggestion_results or message.

        """

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.streaming_analyze_content
        ]

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            requests,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def streaming_reactive_companion_suggestions(
        self,
        requests: Optional[
            Iterator[participant.StreamingReactiveCompanionSuggestionsRequest]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Iterable[participant.StreamingReactiveCompanionSuggestionsResponse]:
        r"""External streaming API for human-agent queries to the
        companion bot.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_streaming_reactive_companion_suggestions():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.StreamingReactiveCompanionSuggestionsRequest(
                    text_input="text_input_value",
                    participant="participant_value",
                )

                # This method expects an iterator which contains
                # 'dialogflow_v2beta1.StreamingReactiveCompanionSuggestionsRequest' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = client.streaming_reactive_companion_suggestions(requests=request_generator())

                # Handle the response
                for response in stream:
                    print(response)

        Args:
            requests (Iterator[google.cloud.dialogflow_v2beta1.types.StreamingReactiveCompanionSuggestionsRequest]):
                The request object iterator. The request message for
                [Participants.StreamingReactiveCompanionSuggestions][google.cloud.dialogflow.v2beta1.Participants.StreamingReactiveCompanionSuggestions].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            Iterable[google.cloud.dialogflow_v2beta1.types.StreamingReactiveCompanionSuggestionsResponse]:
                The response message for
                   [Participants.StreamingReactiveCompanionSuggestions][google.cloud.dialogflow.v2beta1.Participants.StreamingReactiveCompanionSuggestions].

        """

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.streaming_reactive_companion_suggestions
        ]

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            requests,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def bidi_streaming_analyze_content(
        self,
        requests: Optional[
            Iterator[participant.BidiStreamingAnalyzeContentRequest]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> Iterable[participant.BidiStreamingAnalyzeContentResponse]:
        r"""Bidirectional endless streaming version of
        [StreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.StreamingAnalyzeContent].

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_bidi_streaming_analyze_content():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                config = dialogflow_v2beta1.Config()
                config.voice_session_config.input_audio_encoding = "AUDIO_ENCODING_ALAW"
                config.voice_session_config.input_audio_sample_rate_hertz = 3097
                config.voice_session_config.output_audio_encoding = "OUTPUT_AUDIO_ENCODING_ALAW"
                config.voice_session_config.output_audio_sample_rate_hertz = 3226
                config.participant = "participant_value"

                request = dialogflow_v2beta1.BidiStreamingAnalyzeContentRequest(
                    config=config,
                )

                # This method expects an iterator which contains
                # 'dialogflow_v2beta1.BidiStreamingAnalyzeContentRequest' objects
                # Here we create a generator that yields a single `request` for
                # demonstrative purposes.
                requests = [request]

                def request_generator():
                    for request in requests:
                        yield request

                # Make the request
                stream = client.bidi_streaming_analyze_content(requests=request_generator())

                # Handle the response
                for response in stream:
                    print(response)

        Args:
            requests (Iterator[google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentRequest]):
                The request object iterator. The request message for
                [Participants.BidiStreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.BidiStreamingAnalyzeContent].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            Iterable[google.cloud.dialogflow_v2beta1.types.BidiStreamingAnalyzeContentResponse]:
                The response message for
                   [Participants.BidiStreamingAnalyzeContent][google.cloud.dialogflow.v2beta1.Participants.BidiStreamingAnalyzeContent].

        """

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[
            self._transport.bidi_streaming_analyze_content
        ]

        # Validate the universe domain.
        self._validate_universe_domain()

        # Send the request.
        response = rpc(
            requests,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def suggest_articles(
        self,
        request: Optional[Union[participant.SuggestArticlesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.SuggestArticlesResponse:
        r"""Gets suggested articles for a participant based on specific
        historical messages.

        Note that
        [ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
        will only list the auto-generated suggestions, while
        [CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion]
        will try to compile suggestion based on the provided
        conversation context in the real time.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_suggest_articles():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestArticlesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_articles(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestArticlesRequest, dict]):
                The request object. The request message for
                [Participants.SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles].
            parent (str):
                Required. The name of the participant to fetch
                suggestion for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

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
            google.cloud.dialogflow_v2beta1.types.SuggestArticlesResponse:
                The response message for
                   [Participants.SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles].

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
        if not isinstance(request, participant.SuggestArticlesRequest):
            request = participant.SuggestArticlesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.suggest_articles]

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

    def suggest_faq_answers(
        self,
        request: Optional[Union[participant.SuggestFaqAnswersRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.SuggestFaqAnswersResponse:
        r"""Gets suggested faq answers for a participant based on
        specific historical messages.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_suggest_faq_answers():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestFaqAnswersRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_faq_answers(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersRequest, dict]):
                The request object. The request message for
                [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers].
            parent (str):
                Required. The name of the participant to fetch
                suggestion for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

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
            google.cloud.dialogflow_v2beta1.types.SuggestFaqAnswersResponse:
                The request message for
                   [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers].

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
        if not isinstance(request, participant.SuggestFaqAnswersRequest):
            request = participant.SuggestFaqAnswersRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.suggest_faq_answers]

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

    def suggest_smart_replies(
        self,
        request: Optional[Union[participant.SuggestSmartRepliesRequest, dict]] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.SuggestSmartRepliesResponse:
        r"""Gets smart replies for a participant based on
        specific historical messages.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_suggest_smart_replies():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestSmartRepliesRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_smart_replies(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesRequest, dict]):
                The request object. The request message for
                [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies].
            parent (str):
                Required. The name of the participant to fetch
                suggestion for. Format:
                ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.

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
            google.cloud.dialogflow_v2beta1.types.SuggestSmartRepliesResponse:
                The response message for
                   [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2beta1.Participants.SuggestSmartReplies].

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
        if not isinstance(request, participant.SuggestSmartRepliesRequest):
            request = participant.SuggestSmartRepliesRequest(request)
            # If we have keyword arguments corresponding to fields on the
            # request, apply these.
            if parent is not None:
                request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.suggest_smart_replies]

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

    def suggest_knowledge_assist(
        self,
        request: Optional[
            Union[participant.SuggestKnowledgeAssistRequest, dict]
        ] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.SuggestKnowledgeAssistResponse:
        r"""Gets knowledge assist suggestions based on historical
        messages.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_suggest_knowledge_assist():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.SuggestKnowledgeAssistRequest(
                    parent="parent_value",
                )

                # Make the request
                response = client.suggest_knowledge_assist(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistRequest, dict]):
                The request object. The request message for
                [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.SuggestKnowledgeAssistResponse:
                The response message for
                   [Participants.SuggestKnowledgeAssist][google.cloud.dialogflow.v2beta1.Participants.SuggestKnowledgeAssist].

        """
        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, participant.SuggestKnowledgeAssistRequest):
            request = participant.SuggestKnowledgeAssistRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.suggest_knowledge_assist]

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

    def list_suggestions(
        self,
        request: Optional[Union[participant.ListSuggestionsRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListSuggestionsPager:
        r"""Deprecated: Use inline suggestion, event based suggestion or
        Suggestion\* API instead. See
        [HumanAgentAssistantConfig.name][google.cloud.dialogflow.v2beta1.HumanAgentAssistantConfig.name]
        for more details. Removal Date: 2020-09-01.

        Retrieves suggestions for live agents.

        This method should be used by human agent client software to
        fetch auto generated suggestions in real-time, while the
        conversation with an end user is in progress. The functionality
        is implemented in terms of the `list
        pagination <https://cloud.google.com/apis/design/design_patterns#list_pagination>`__
        design pattern. The client app should use the
        ``next_page_token`` field to fetch the next batch of
        suggestions. ``suggestions`` are sorted by ``create_time`` in
        descending order. To fetch latest suggestion, just set
        ``page_size`` to 1. To fetch new suggestions without
        duplication, send request with filter
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

            def sample_list_suggestions():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListSuggestionsRequest(
                )

                # Make the request
                page_result = client.list_suggestions(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListSuggestionsRequest, dict]):
                The request object. The request message for
                [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.services.participants.pagers.ListSuggestionsPager:
                The response message for
                   [Participants.ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        warnings.warn(
            "ParticipantsClient.list_suggestions is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, participant.ListSuggestionsRequest):
            request = participant.ListSuggestionsRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.list_suggestions]

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
        response = pagers.ListSuggestionsPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    def compile_suggestion(
        self,
        request: Optional[Union[participant.CompileSuggestionRequest, dict]] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> participant.CompileSuggestionResponse:
        r"""Deprecated. use
        [SuggestArticles][google.cloud.dialogflow.v2beta1.Participants.SuggestArticles]
        and
        [SuggestFaqAnswers][google.cloud.dialogflow.v2beta1.Participants.SuggestFaqAnswers]
        instead.

        Gets suggestions for a participant based on specific historical
        messages.

        Note that
        [ListSuggestions][google.cloud.dialogflow.v2beta1.Participants.ListSuggestions]
        will only list the auto-generated suggestions, while
        [CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion]
        will try to compile suggestion based on the provided
        conversation context in the real time.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import dialogflow_v2beta1

            def sample_compile_suggestion():
                # Create a client
                client = dialogflow_v2beta1.ParticipantsClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.CompileSuggestionRequest(
                )

                # Make the request
                response = client.compile_suggestion(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CompileSuggestionRequest, dict]):
                The request object. The request message for
                [Participants.CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.dialogflow_v2beta1.types.CompileSuggestionResponse:
                The response message for
                   [Participants.CompileSuggestion][google.cloud.dialogflow.v2beta1.Participants.CompileSuggestion].

        """
        warnings.warn(
            "ParticipantsClient.compile_suggestion is deprecated", DeprecationWarning
        )

        # Create or coerce a protobuf request object.
        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, participant.CompileSuggestionRequest):
            request = participant.CompileSuggestionRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._transport._wrapped_methods[self._transport.compile_suggestion]

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

    def __enter__(self) -> "ParticipantsClient":
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

__all__ = ("ParticipantsClient",)
