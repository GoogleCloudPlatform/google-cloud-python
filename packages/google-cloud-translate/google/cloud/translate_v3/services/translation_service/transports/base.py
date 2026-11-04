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

from google.cloud.translate_v3 import gapic_version as package_version
from google.cloud.translate_v3._compat import (
    ASYNC_WRAP_METHOD_SUPPORTS_KIND as _ASYNC_WRAP_METHOD_SUPPORTS_KIND,
)
from google.cloud.translate_v3._compat import (
    WRAP_METHOD_SUPPORTS_TRACING as _WRAP_METHOD_SUPPORTS_TRACING,
)

_ASYNC_WRAP_METHOD_SUPPORTS_TRACING = _WRAP_METHOD_SUPPORTS_TRACING
_WRAP_METHOD_SUPPORTS_KIND = _WRAP_METHOD_SUPPORTS_TRACING

import google.api_core
import google.auth  # type: ignore
import google.protobuf
import google.protobuf.empty_pb2 as empty_pb2  # type: ignore
from google.api_core import client_options as client_options_lib
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1, operations_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.cloud.location import locations_pb2  # type: ignore
from google.iam.v1 import (
    iam_policy_pb2,  # type: ignore
    policy_pb2,  # type: ignore
)
from google.longrunning import operations_pb2  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.translate_v3.types import (
    adaptive_mt,
    automl_translation,
    common,
    translation_service,
)

DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)
DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


class TranslationServiceTransport(abc.ABC):
    """Abstract transport class for TranslationService."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/cloud-translation",
    )

    DEFAULT_HOST: str = "translate.googleapis.com"

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
        client_options: Optional[Union[client_options_lib.ClientOptions, dict]] = None,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to (default: 'translate.googleapis.com').
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
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client, containing options such as
                custom OpenTelemetry tracer providers.
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

        self._client_options = client_options
        self._wrapped_methods: Dict[Callable, Callable] = {}

    @property
    def host(self):
        return self._host

    def _wrap_method(self, func, *args, **kwargs):
        """Wrap an RPC method with common client-level features.

        Applies retry, timeout, metadata, and tracing wrappers to the
        underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method.wrap_method(func, *args, **kwargs)

    def _wrap_async_method(self, func, *args, **kwargs):
        """Wrap an async RPC method with common client-level features.

        Applies asynchronous retry, timeout, metadata, and tracing wrappers
        to the underlying RPC method callable. If the runtime `google-api-core`
        version supports tracing, transport attributes (`client_options` and
        `kind`) are injected. Otherwise, tracing-specific arguments are
        stripped for backward compatibility with older `google-api-core`
        versions.
        """
        if _ASYNC_WRAP_METHOD_SUPPORTS_TRACING:
            kwargs["client_options"] = self._client_options
            try:
                kind = self.kind
            except NotImplementedError:
                kind = None
            if kind:
                kwargs["kind"] = kind
            return gapic_v1.method_async.wrap_method(func, *args, **kwargs)
        # Fallback for older runtime versions of google-api-core:
        # - Era 1 (< 2.29.0): Neither tracing args nor `kind` are supported.
        # - Era 2 (>= 2.29.0, < 2.36.0): `kind` is supported (prevents REST from
        #   falling back to gRPC wrapping), but tracing args are not.
        # (These fallbacks can be removed once google-api-core < 2.36.0 is no longer supported.)
        for k in ["client_options", "method_name", "is_streaming"]:
            kwargs.pop(k, None)

        try:
            kind = self.kind
        except NotImplementedError:
            kind = None

        if _ASYNC_WRAP_METHOD_SUPPORTS_KIND and kind:
            kwargs["kind"] = kind
        else:
            kwargs.pop("kind", None)

        return gapic_v1.method_async.wrap_method(func, *args, **kwargs)

    def _prep_wrapped_messages(self, client_info):
        """Precompute and cache wrapped methods for RPC dispatch."""
        self._wrapped_methods = {
            self.translate_text: self._wrap_method(
                self.translate_text,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/TranslateText",
            ),
            self.romanize_text: self._wrap_method(
                self.romanize_text,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/RomanizeText",
            ),
            self.detect_language: self._wrap_method(
                self.detect_language,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DetectLanguage",
            ),
            self.get_supported_languages: self._wrap_method(
                self.get_supported_languages,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetSupportedLanguages",
            ),
            self.translate_document: self._wrap_method(
                self.translate_document,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/TranslateDocument",
            ),
            self.batch_translate_text: self._wrap_method(
                self.batch_translate_text,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/BatchTranslateText",
            ),
            self.batch_translate_document: self._wrap_method(
                self.batch_translate_document,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/BatchTranslateDocument",
            ),
            self.create_glossary: self._wrap_method(
                self.create_glossary,
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/CreateGlossary",
            ),
            self.update_glossary: self._wrap_method(
                self.update_glossary,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/UpdateGlossary",
            ),
            self.list_glossaries: self._wrap_method(
                self.list_glossaries,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListGlossaries",
            ),
            self.get_glossary: self._wrap_method(
                self.get_glossary,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetGlossary",
            ),
            self.delete_glossary: self._wrap_method(
                self.delete_glossary,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.DeadlineExceeded,
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=600.0,
                ),
                default_timeout=600.0,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DeleteGlossary",
            ),
            self.get_glossary_entry: self._wrap_method(
                self.get_glossary_entry,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetGlossaryEntry",
            ),
            self.list_glossary_entries: self._wrap_method(
                self.list_glossary_entries,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListGlossaryEntries",
            ),
            self.create_glossary_entry: self._wrap_method(
                self.create_glossary_entry,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/CreateGlossaryEntry",
            ),
            self.update_glossary_entry: self._wrap_method(
                self.update_glossary_entry,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/UpdateGlossaryEntry",
            ),
            self.delete_glossary_entry: self._wrap_method(
                self.delete_glossary_entry,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DeleteGlossaryEntry",
            ),
            self.create_dataset: self._wrap_method(
                self.create_dataset,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/CreateDataset",
            ),
            self.get_dataset: self._wrap_method(
                self.get_dataset,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetDataset",
            ),
            self.list_datasets: self._wrap_method(
                self.list_datasets,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListDatasets",
            ),
            self.delete_dataset: self._wrap_method(
                self.delete_dataset,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DeleteDataset",
            ),
            self.create_adaptive_mt_dataset: self._wrap_method(
                self.create_adaptive_mt_dataset,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/CreateAdaptiveMtDataset",
            ),
            self.delete_adaptive_mt_dataset: self._wrap_method(
                self.delete_adaptive_mt_dataset,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DeleteAdaptiveMtDataset",
            ),
            self.get_adaptive_mt_dataset: self._wrap_method(
                self.get_adaptive_mt_dataset,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetAdaptiveMtDataset",
            ),
            self.list_adaptive_mt_datasets: self._wrap_method(
                self.list_adaptive_mt_datasets,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListAdaptiveMtDatasets",
            ),
            self.adaptive_mt_translate: self._wrap_method(
                self.adaptive_mt_translate,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/AdaptiveMtTranslate",
            ),
            self.get_adaptive_mt_file: self._wrap_method(
                self.get_adaptive_mt_file,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetAdaptiveMtFile",
            ),
            self.delete_adaptive_mt_file: self._wrap_method(
                self.delete_adaptive_mt_file,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DeleteAdaptiveMtFile",
            ),
            self.import_adaptive_mt_file: self._wrap_method(
                self.import_adaptive_mt_file,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ImportAdaptiveMtFile",
            ),
            self.list_adaptive_mt_files: self._wrap_method(
                self.list_adaptive_mt_files,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListAdaptiveMtFiles",
            ),
            self.list_adaptive_mt_sentences: self._wrap_method(
                self.list_adaptive_mt_sentences,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListAdaptiveMtSentences",
            ),
            self.import_data: self._wrap_method(
                self.import_data,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ImportData",
            ),
            self.export_data: self._wrap_method(
                self.export_data,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ExportData",
            ),
            self.list_examples: self._wrap_method(
                self.list_examples,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListExamples",
            ),
            self.create_model: self._wrap_method(
                self.create_model,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/CreateModel",
            ),
            self.list_models: self._wrap_method(
                self.list_models,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/ListModels",
            ),
            self.get_model: self._wrap_method(
                self.get_model,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/GetModel",
            ),
            self.delete_model: self._wrap_method(
                self.delete_model,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.translation.v3.TranslationService/DeleteModel",
            ),
            self.get_location: self._wrap_method(
                self.get_location,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/GetLocation",
            ),
            self.list_locations: self._wrap_method(
                self.list_locations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.cloud.location.Locations/ListLocations",
            ),
            self.cancel_operation: self._wrap_method(
                self.cancel_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/CancelOperation",
            ),
            self.delete_operation: self._wrap_method(
                self.delete_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/DeleteOperation",
            ),
            self.get_operation: self._wrap_method(
                self.get_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/GetOperation",
            ),
            self.list_operations: self._wrap_method(
                self.list_operations,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/ListOperations",
            ),
            self.wait_operation: self._wrap_method(
                self.wait_operation,
                default_timeout=None,
                client_info=client_info,
                method_name="google.longrunning.Operations/WaitOperation",
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
    def translate_text(
        self,
    ) -> Callable[
        [translation_service.TranslateTextRequest],
        Union[
            translation_service.TranslateTextResponse,
            Awaitable[translation_service.TranslateTextResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def romanize_text(
        self,
    ) -> Callable[
        [translation_service.RomanizeTextRequest],
        Union[
            translation_service.RomanizeTextResponse,
            Awaitable[translation_service.RomanizeTextResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def detect_language(
        self,
    ) -> Callable[
        [translation_service.DetectLanguageRequest],
        Union[
            translation_service.DetectLanguageResponse,
            Awaitable[translation_service.DetectLanguageResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_supported_languages(
        self,
    ) -> Callable[
        [translation_service.GetSupportedLanguagesRequest],
        Union[
            translation_service.SupportedLanguages,
            Awaitable[translation_service.SupportedLanguages],
        ],
    ]:
        raise NotImplementedError()

    @property
    def translate_document(
        self,
    ) -> Callable[
        [translation_service.TranslateDocumentRequest],
        Union[
            translation_service.TranslateDocumentResponse,
            Awaitable[translation_service.TranslateDocumentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def batch_translate_text(
        self,
    ) -> Callable[
        [translation_service.BatchTranslateTextRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def batch_translate_document(
        self,
    ) -> Callable[
        [translation_service.BatchTranslateDocumentRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_glossary(
        self,
    ) -> Callable[
        [translation_service.CreateGlossaryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_glossary(
        self,
    ) -> Callable[
        [translation_service.UpdateGlossaryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_glossaries(
        self,
    ) -> Callable[
        [translation_service.ListGlossariesRequest],
        Union[
            translation_service.ListGlossariesResponse,
            Awaitable[translation_service.ListGlossariesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_glossary(
        self,
    ) -> Callable[
        [translation_service.GetGlossaryRequest],
        Union[translation_service.Glossary, Awaitable[translation_service.Glossary]],
    ]:
        raise NotImplementedError()

    @property
    def delete_glossary(
        self,
    ) -> Callable[
        [translation_service.DeleteGlossaryRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_glossary_entry(
        self,
    ) -> Callable[
        [translation_service.GetGlossaryEntryRequest],
        Union[common.GlossaryEntry, Awaitable[common.GlossaryEntry]],
    ]:
        raise NotImplementedError()

    @property
    def list_glossary_entries(
        self,
    ) -> Callable[
        [translation_service.ListGlossaryEntriesRequest],
        Union[
            translation_service.ListGlossaryEntriesResponse,
            Awaitable[translation_service.ListGlossaryEntriesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_glossary_entry(
        self,
    ) -> Callable[
        [translation_service.CreateGlossaryEntryRequest],
        Union[common.GlossaryEntry, Awaitable[common.GlossaryEntry]],
    ]:
        raise NotImplementedError()

    @property
    def update_glossary_entry(
        self,
    ) -> Callable[
        [translation_service.UpdateGlossaryEntryRequest],
        Union[common.GlossaryEntry, Awaitable[common.GlossaryEntry]],
    ]:
        raise NotImplementedError()

    @property
    def delete_glossary_entry(
        self,
    ) -> Callable[
        [translation_service.DeleteGlossaryEntryRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def create_dataset(
        self,
    ) -> Callable[
        [automl_translation.CreateDatasetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_dataset(
        self,
    ) -> Callable[
        [automl_translation.GetDatasetRequest],
        Union[automl_translation.Dataset, Awaitable[automl_translation.Dataset]],
    ]:
        raise NotImplementedError()

    @property
    def list_datasets(
        self,
    ) -> Callable[
        [automl_translation.ListDatasetsRequest],
        Union[
            automl_translation.ListDatasetsResponse,
            Awaitable[automl_translation.ListDatasetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def delete_dataset(
        self,
    ) -> Callable[
        [automl_translation.DeleteDatasetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def create_adaptive_mt_dataset(
        self,
    ) -> Callable[
        [adaptive_mt.CreateAdaptiveMtDatasetRequest],
        Union[adaptive_mt.AdaptiveMtDataset, Awaitable[adaptive_mt.AdaptiveMtDataset]],
    ]:
        raise NotImplementedError()

    @property
    def delete_adaptive_mt_dataset(
        self,
    ) -> Callable[
        [adaptive_mt.DeleteAdaptiveMtDatasetRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def get_adaptive_mt_dataset(
        self,
    ) -> Callable[
        [adaptive_mt.GetAdaptiveMtDatasetRequest],
        Union[adaptive_mt.AdaptiveMtDataset, Awaitable[adaptive_mt.AdaptiveMtDataset]],
    ]:
        raise NotImplementedError()

    @property
    def list_adaptive_mt_datasets(
        self,
    ) -> Callable[
        [adaptive_mt.ListAdaptiveMtDatasetsRequest],
        Union[
            adaptive_mt.ListAdaptiveMtDatasetsResponse,
            Awaitable[adaptive_mt.ListAdaptiveMtDatasetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def adaptive_mt_translate(
        self,
    ) -> Callable[
        [adaptive_mt.AdaptiveMtTranslateRequest],
        Union[
            adaptive_mt.AdaptiveMtTranslateResponse,
            Awaitable[adaptive_mt.AdaptiveMtTranslateResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_adaptive_mt_file(
        self,
    ) -> Callable[
        [adaptive_mt.GetAdaptiveMtFileRequest],
        Union[adaptive_mt.AdaptiveMtFile, Awaitable[adaptive_mt.AdaptiveMtFile]],
    ]:
        raise NotImplementedError()

    @property
    def delete_adaptive_mt_file(
        self,
    ) -> Callable[
        [adaptive_mt.DeleteAdaptiveMtFileRequest],
        Union[empty_pb2.Empty, Awaitable[empty_pb2.Empty]],
    ]:
        raise NotImplementedError()

    @property
    def import_adaptive_mt_file(
        self,
    ) -> Callable[
        [adaptive_mt.ImportAdaptiveMtFileRequest],
        Union[
            adaptive_mt.ImportAdaptiveMtFileResponse,
            Awaitable[adaptive_mt.ImportAdaptiveMtFileResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_adaptive_mt_files(
        self,
    ) -> Callable[
        [adaptive_mt.ListAdaptiveMtFilesRequest],
        Union[
            adaptive_mt.ListAdaptiveMtFilesResponse,
            Awaitable[adaptive_mt.ListAdaptiveMtFilesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_adaptive_mt_sentences(
        self,
    ) -> Callable[
        [adaptive_mt.ListAdaptiveMtSentencesRequest],
        Union[
            adaptive_mt.ListAdaptiveMtSentencesResponse,
            Awaitable[adaptive_mt.ListAdaptiveMtSentencesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def import_data(
        self,
    ) -> Callable[
        [automl_translation.ImportDataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def export_data(
        self,
    ) -> Callable[
        [automl_translation.ExportDataRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_examples(
        self,
    ) -> Callable[
        [automl_translation.ListExamplesRequest],
        Union[
            automl_translation.ListExamplesResponse,
            Awaitable[automl_translation.ListExamplesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def create_model(
        self,
    ) -> Callable[
        [automl_translation.CreateModelRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_models(
        self,
    ) -> Callable[
        [automl_translation.ListModelsRequest],
        Union[
            automl_translation.ListModelsResponse,
            Awaitable[automl_translation.ListModelsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_model(
        self,
    ) -> Callable[
        [automl_translation.GetModelRequest],
        Union[automl_translation.Model, Awaitable[automl_translation.Model]],
    ]:
        raise NotImplementedError()

    @property
    def delete_model(
        self,
    ) -> Callable[
        [automl_translation.DeleteModelRequest],
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
    def delete_operation(
        self,
    ) -> Callable[
        [operations_pb2.DeleteOperationRequest],
        None,
    ]:
        raise NotImplementedError()

    @property
    def wait_operation(
        self,
    ) -> Callable[
        [operations_pb2.WaitOperationRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_location(
        self,
    ) -> Callable[
        [locations_pb2.GetLocationRequest],
        Union[locations_pb2.Location, Awaitable[locations_pb2.Location]],
    ]:
        raise NotImplementedError()

    @property
    def list_locations(
        self,
    ) -> Callable[
        [locations_pb2.ListLocationsRequest],
        Union[
            locations_pb2.ListLocationsResponse,
            Awaitable[locations_pb2.ListLocationsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def kind(self) -> str:
        raise NotImplementedError()


__all__ = ("TranslationServiceTransport",)
